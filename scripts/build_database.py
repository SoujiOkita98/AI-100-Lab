#!/usr/bin/env python3
"""
build_database.py

Parses all company markdown files (messy YAML frontmatter + body text),
extracts what it can, and outputs three clean JSON files:

  data/companies.json
  data/founders.json
  data/rounds.json

Plus CSV exports in exports/.

This is a one-time migration script. Once the JSON files exist,
they become the source of truth — not the markdown files.
"""

import os
import re
import csv
import json
import yaml
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE_DIR / "companies"
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"
DATA_DIR.mkdir(exist_ok=True)
EXPORTS_DIR.mkdir(exist_ok=True)


def parse_frontmatter(filepath):
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}, text
    try:
        data = yaml.safe_load(match.group(1))
        return (data if isinstance(data, dict) else {}), text[match.end():]
    except yaml.YAMLError:
        return {}, text


def get_val(d, *keys, default=None):
    """Get first matching key from dict."""
    for k in keys:
        if k in d and d[k] is not None:
            return d[k]
    return default


def to_float(val):
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip().lower().replace(",", "").replace("$", "").replace("~", "").replace("+", "").replace("€", "").replace("eur", "")
    s = re.sub(r"\s*(approx|approximately|estimated|est|about|over|nearly|roughly)\s*", "", s)
    m = re.match(r"([\d.]+)\s*b(?:illion)?", s)
    if m:
        return round(float(m.group(1)) * 1000, 1)
    m = re.match(r"([\d.]+)\s*m(?:illion)?", s)
    if m:
        return round(float(m.group(1)), 1)
    m = re.match(r"([\d.]+)\s*t(?:rillion)?", s)
    if m:
        return round(float(m.group(1)) * 1000000, 1)
    try:
        v = float(re.match(r"[\d.]+", s).group())
        return v
    except (ValueError, AttributeError):
        return None


def to_year(val):
    if val is None:
        return None
    m = re.search(r"((?:19|20)\d{2})", str(val))
    return int(m.group(1)) if m else None


def to_str_list(val):
    if isinstance(val, list):
        return [str(x) for x in val if x]
    if isinstance(val, str):
        return [val]
    return []


def extract_company(raw, slug):
    """Extract company-level fields."""
    name = get_val(raw, "name", "company", "company_name", "brand_name", default=slug.replace("-", " ").title())
    if isinstance(name, dict):
        name = slug.replace("-", " ").title()

    status = get_val(raw, "status", default="active")
    if isinstance(status, str):
        status = status.lower().strip()
        if "acqui" in status:
            status = "acquired"
        elif "public" in status or "ipo" in status or "nasdaq" in status or "nyse" in status:
            status = "public"
        elif "dead" in status or "shut" in status:
            status = "dead"
        elif "shell" in status or "zombie" in status:
            status = "shell"
        elif "stealth" in status:
            status = "stealth"
        else:
            status = "active"

    sectors = get_val(raw, "sector", "sectors", "tags", default=[])
    if isinstance(sectors, str):
        sectors = [s.strip() for s in sectors.split("/") if s.strip()]
    sectors = sectors[:3] if isinstance(sectors, list) else []

    total = to_float(get_val(raw, "total_raised_m", "total_funding", "total_funding_raised",
                              "total_funding_m", "total_raised", "funding_total"))
    valuation = to_float(get_val(raw, "latest_valuation_m", "latest_valuation", "valuation",
                                  "estimated_valuation", "current_valuation"))

    customers = get_val(raw, "customers", "key_customers", default=[])
    if isinstance(customers, str):
        customers = [c.strip() for c in customers.split(",")]
    customers = to_str_list(customers)[:10]

    emp = get_val(raw, "employee_count", "employees", "employees_approx",
                  "employee_count_estimate", "headcount", "team_size_estimate")
    if emp is not None:
        m = re.search(r"(\d+)", str(emp).replace(",", ""))
        emp = int(m.group(1)) if m else None

    # Derive latest round info from funding_rounds if available
    rounds_raw = get_val(raw, "funding_rounds", default=[])
    latest_round = get_val(raw, "latest_round", "last_round_stage")
    latest_round_date = get_val(raw, "latest_round_date", "last_round_date")

    return {
        "slug": slug,
        "name": str(name),
        "status": status,
        "founded_year": to_year(get_val(raw, "founded_year", "founded", "year_founded")),
        "hq": get_val(raw, "hq", "headquarters", "location", "headquartered"),
        "website": get_val(raw, "website", "domain", "url"),
        "sectors": [str(s) for s in sectors],
        "one_liner": get_val(raw, "one_liner", "description", "tagline"),
        "logo_file": get_val(raw, "logo", "logo_file"),
        "total_raised_m": total,
        "latest_valuation_m": valuation,
        "latest_round": latest_round,
        "latest_round_date": str(latest_round_date) if latest_round_date else None,
        "business_model": get_val(raw, "business_model"),
        "revenue_signals": str(get_val(raw, "revenue_signals", "arr", "arr_estimate", "revenue", default="")) or None,
        "key_customers": customers,
        "employee_count": emp,
        "team_china_profile": get_val(raw, "team_china_profile"),
        "engagement": {
            "status": "none",
            "first_contact_date": None,
            "source": None,
            "owner": None,
            "notes": None
        },
        "sources": to_str_list(get_val(raw, "sources", default=[])),
        "confidence": get_val(raw, "confidence", default="medium"),
        "last_updated": str(get_val(raw, "last_updated", "research_date", default=date.today()))
    }


def extract_founders(raw, slug):
    """Extract founder records."""
    founders_raw = get_val(raw, "founders", default=[])
    if not isinstance(founders_raw, list):
        return []

    results = []
    for f in founders_raw:
        if not isinstance(f, dict):
            continue
        name = f.get("name", "")
        if not name:
            continue

        origin = f.get("origin", f.get("nationality", f.get("ethnic_origin",
                 f.get("national_origin", f.get("heritage", "")))))

        status = f.get("status", "unknown")
        if isinstance(status, str):
            s = status.lower()
            if "depart" in s or "left" in s or "former" in s:
                status = "departed"
            elif "active" in s or "current" in s:
                status = "active"
            else:
                status = "unknown"

        results.append({
            "company_slug": slug,
            "name": str(name),
            "role": str(f.get("role", "")),
            "background": str(f.get("background", "")),
            "origin": str(origin) if origin else "",
            "origin_detail": str(f.get("origin_detail", "")),
            "status": status,
            "departed_to": str(f.get("departed_to", ""))
        })
    return results


def extract_rounds(raw, slug):
    """Extract funding round records."""
    rounds_raw = get_val(raw, "funding_rounds", default=[])
    if not isinstance(rounds_raw, list):
        return []

    results = []
    for r in rounds_raw:
        if not isinstance(r, dict):
            continue

        leads = r.get("lead_investors", r.get("lead", []))
        if isinstance(leads, str):
            leads = [leads]
        leads = [str(l) for l in leads if l] if isinstance(leads, list) else []

        results.append({
            "company_slug": slug,
            "stage": str(r.get("stage", "")),
            "date": str(r.get("date", "")),
            "amount_m": to_float(r.get("amount_m", r.get("amount", r.get("size_m")))),
            "valuation_m": to_float(r.get("valuation_m", r.get("valuation", r.get("post_money_valuation_m")))),
            "lead_investors": leads,
            "source": str(r.get("source", "")),
            "notes": str(r.get("notes", ""))
        })
    return results


def export_csv(data, fields, filepath):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in data:
            flat = dict(row)
            for k, v in flat.items():
                if isinstance(v, list):
                    flat[k] = "; ".join(str(x) for x in v)
                elif isinstance(v, dict):
                    flat[k] = json.dumps(v)
            w.writerow(flat)


def main():
    companies = []
    founders = []
    rounds = []
    issues = []

    for md_file in sorted(COMPANIES_DIR.glob("*.md")):
        slug = md_file.stem
        raw, body = parse_frontmatter(md_file)

        if not raw:
            issues.append(f"NO PARSEABLE FRONTMATTER: {slug}")
            # Still create a stub
            companies.append({
                "slug": slug, "name": slug.replace("-", " ").title(),
                "status": "active", "founded_year": None, "hq": None,
                "website": None, "sectors": [], "one_liner": None,
                "logo_file": None, "total_raised_m": None,
                "latest_valuation_m": None, "latest_round": None,
                "latest_round_date": None, "business_model": None,
                "revenue_signals": None, "key_customers": [],
                "employee_count": None, "team_china_profile": None,
                "engagement": {"status": "none", "first_contact_date": None,
                               "source": None, "owner": None, "notes": None},
                "sources": [], "confidence": "low",
                "last_updated": str(date.today())
            })
            continue

        company = extract_company(raw, slug)
        company_founders = extract_founders(raw, slug)
        company_rounds = extract_rounds(raw, slug)

        companies.append(company)
        founders.extend(company_founders)
        rounds.extend(company_rounds)

        # Flag missing critical data
        if not company["founded_year"]:
            issues.append(f"MISSING founded_year: {slug}")
        if not company["total_raised_m"]:
            issues.append(f"MISSING total_raised_m: {slug}")
        if not company_founders:
            issues.append(f"NO FOUNDERS PARSED: {slug}")
        if not company_rounds:
            issues.append(f"NO ROUNDS PARSED: {slug}")

    # Sort
    companies.sort(key=lambda x: x["slug"])
    founders.sort(key=lambda x: (x["company_slug"], x["name"]))
    rounds.sort(key=lambda x: (x["company_slug"], x["date"]))

    # Write JSON
    for name, data in [("companies", companies), ("founders", founders), ("rounds", rounds)]:
        path = DATA_DIR / f"{name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Wrote {len(data)} records to {path}")

    # Write CSVs
    export_csv(companies, [
        "slug", "name", "status", "founded_year", "hq", "website", "sectors",
        "one_liner", "total_raised_m", "latest_valuation_m", "latest_round",
        "latest_round_date", "business_model", "revenue_signals", "key_customers",
        "employee_count", "team_china_profile", "confidence", "last_updated"
    ], EXPORTS_DIR / "companies.csv")

    export_csv(founders, [
        "company_slug", "name", "role", "background", "origin", "origin_detail", "status", "departed_to"
    ], EXPORTS_DIR / "founders.csv")

    export_csv(rounds, [
        "company_slug", "stage", "date", "amount_m", "valuation_m", "lead_investors", "source", "notes"
    ], EXPORTS_DIR / "rounds.csv")

    # Report
    print(f"\n{'='*60}")
    print(f"TOTAL COMPANIES: {len(companies)}")
    print(f"TOTAL FOUNDERS:  {len(founders)}")
    print(f"TOTAL ROUNDS:    {len(rounds)}")
    print(f"\nDATA QUALITY:")
    print(f"  With founded_year:    {sum(1 for c in companies if c['founded_year'])}/{len(companies)}")
    print(f"  With total_raised:    {sum(1 for c in companies if c['total_raised_m'])}/{len(companies)}")
    print(f"  With valuation:       {sum(1 for c in companies if c['latest_valuation_m'])}/{len(companies)}")
    print(f"  With founders:        {sum(1 for c in companies if any(f['company_slug']==c['slug'] for f in founders))}/{len(companies)}")
    print(f"  With rounds:          {sum(1 for c in companies if any(r['company_slug']==c['slug'] for r in rounds))}/{len(companies)}")
    print(f"  With china profile:   {sum(1 for c in companies if c['team_china_profile'])}/{len(companies)}")
    print(f"\nISSUES ({len(issues)}):")
    for i in issues[:30]:
        print(f"  - {i}")
    if len(issues) > 30:
        print(f"  ... and {len(issues)-30} more")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
