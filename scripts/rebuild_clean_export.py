#!/usr/bin/env python3
"""
Rebuild clean, unified exports from all 264 company markdown files.
Normalizes inconsistent field names across schema versions.
"""

import os
import re
import csv
import json
import yaml
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE / "companies"
EXPORTS_DIR = BASE / "exports"


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    body = text[m.end():]
    return fm, body


def normalize_money(val):
    """Convert various money representations to float in millions USD.

    Handles: raw USD ints (134_000_000_000), millions (750.0), strings like
    "$39B", "~$1.9B", "$675M", ">$1B", "$100M+", "100_000_000_000+".
    """
    if val is None or val == "" or val == "~" or val == "[not disclosed]":
        return None
    if isinstance(val, (int, float)):
        # Heuristic: values > 10_000_000 are likely raw USD (e.g. 134_000_000_000)
        # Values <= 10_000_000 are likely already in millions (e.g. 840000 = $840B)
        if val > 10_000_000:
            return round(val / 1_000_000, 1)
        return round(float(val), 1)
    s = str(val).strip().replace(",", "").replace("_", "")
    # Strip common prefixes/suffixes: ~, $, >, <, +, parenthetical notes
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical like "(post-money)"
    s = re.sub(r"[~$><+]", "", s).strip()
    if not s or not any(c.isdigit() for c in s):
        return None
    # Handle "XB" or "XM" suffixes
    multiplier = 1
    s_upper = s.upper().rstrip()
    if s_upper.endswith("B"):
        s = s_upper[:-1].strip()
        multiplier = 1000
    elif s_upper.endswith("M"):
        s = s_upper[:-1].strip()
        multiplier = 1
    else:
        # Could be raw USD (large int) — try to parse
        try:
            raw = float(s)
            if raw > 10_000_000:
                return round(raw / 1_000_000, 1)
            return round(raw, 1)
        except ValueError:
            return None
    try:
        return round(float(s) * multiplier, 1)
    except ValueError:
        return None


def get_first(*keys, fm, default=None):
    """Return the first non-empty value from a list of candidate keys."""
    for k in keys:
        v = fm.get(k)
        if v is not None and v != "" and v != "~":
            return v
    return default


def extract_company(fm, body, slug):
    """Extract normalized company record from frontmatter + body."""
    # Name
    name = get_first("name", "company_name", "company", "legal_name", fm=fm) or slug.replace("-", " ").title()

    # Basics
    status = get_first("status", "stage", fm=fm, default="unknown")
    founded = get_first("founded", "founded_year", fm=fm)
    if founded:
        founded = str(founded)[:4]  # Just the year

    hq = get_first("hq", "headquarters", "location", fm=fm)
    website = get_first("website", "domain", "url", fm=fm)
    if website and not website.startswith("http"):
        website = "https://" + website
    sector = get_first("sector", "sectors", "sub_sector", "tags", fm=fm)
    if isinstance(sector, list):
        sector = "; ".join(str(s) for s in sector)
    one_liner = get_first("one_liner", "description", "tagline", fm=fm)

    # Funding — many field name variants across schema versions
    total_raised_m = normalize_money(get_first(
        "total_raised_m", "total_funding_usd", "total_funding",
        "total_funding_raised", "total_known_funding", "total_funding_approx",
        "funding_total", "total_raised", "total_raised_usd", fm=fm
    ))
    latest_valuation_m = normalize_money(get_first(
        "latest_valuation_m", "latest_valuation_usd", "latest_valuation",
        "valuation", "valuation_usd", "post_money_valuation", fm=fm
    ))

    # If no top-level valuation, derive from last funding round
    if latest_valuation_m is None:
        rounds_raw = fm.get("funding_rounds", fm.get("rounds", []))
        if isinstance(rounds_raw, list):
            for r in reversed(rounds_raw):
                if not isinstance(r, dict):
                    continue
                rv = r.get("valuation_m", r.get("valuation", r.get("valuation_usd",
                     r.get("post_money_valuation"))))
                val = normalize_money(rv)
                if val and val > 0:
                    latest_valuation_m = val
                    break

    # If no top-level total raised, try summing rounds
    if total_raised_m is None:
        rounds_raw = fm.get("funding_rounds", fm.get("rounds", []))
        if isinstance(rounds_raw, list):
            total = 0
            count = 0
            for r in rounds_raw:
                if not isinstance(r, dict):
                    continue
                amt = normalize_money(r.get("amount_m", r.get("amount",
                      r.get("amount_usd"))))
                if amt and amt > 0:
                    total += amt
                    count += 1
            if count > 0:
                total_raised_m = round(total, 1)

    # Employees
    employees = get_first(
        "employee_count", "employee_count_approx", "employee_count_estimate",
        "employees", "employees_approx", "headcount", fm=fm
    )
    if employees:
        employees = str(employees).replace(",", "").replace("~", "").strip()

    # Revenue
    revenue_signals = get_first("revenue_signals", "revenue", fm=fm)
    arr = get_first("arr_estimate", "arr", "revenue_run_rate_usd", fm=fm)
    if arr and not revenue_signals:
        revenue_signals = str(arr)
    elif arr and revenue_signals:
        revenue_signals = f"{revenue_signals} | ARR: {arr}"

    # Business model
    business_model = get_first("business_model", fm=fm)

    # Customers
    customers = get_first("customers", "key_customers", fm=fm)
    if isinstance(customers, list):
        customers = "; ".join(str(c) for c in customers)

    # Team china profile
    team_china_profile = get_first("team_china_profile", "china_profile", fm=fm)

    # Confidence
    confidence = get_first("confidence", fm=fm, default="unknown")

    # Last updated
    last_updated = get_first("last_updated", "research_date", fm=fm)

    return {
        "slug": slug,
        "name": name,
        "status": status,
        "founded_year": founded,
        "hq": hq,
        "website": website,
        "sector": sector,
        "one_liner": one_liner,
        "total_raised_m": total_raised_m,
        "latest_valuation_m": latest_valuation_m,
        "employees": employees,
        "revenue_signals": revenue_signals,
        "business_model": business_model,
        "key_customers": customers,
        "team_china_profile": team_china_profile,
        "confidence": confidence,
        "last_updated": last_updated,
    }


def extract_founders(fm, slug):
    """Extract founders list from frontmatter."""
    founders_raw = fm.get("founders", [])
    if not isinstance(founders_raw, list):
        return []
    results = []
    for f in founders_raw:
        if isinstance(f, str):
            # Handle plain string founders like "Michael Intrator (CEO)"
            m = re.match(r"^(.+?)\s*\((.+?)\)\s*$", f)
            if m:
                results.append({
                    "company_slug": slug, "name": m.group(1).strip(),
                    "role": m.group(2).strip(), "background": "", "origin": "", "prior": "",
                })
            else:
                results.append({
                    "company_slug": slug, "name": f.strip(),
                    "role": "", "background": "", "origin": "", "prior": "",
                })
            continue
        if not isinstance(f, dict):
            continue
        results.append({
            "company_slug": slug,
            "name": f.get("name", ""),
            "role": f.get("role", ""),
            "background": f.get("background", f.get("education", "")),
            "origin": f.get("origin", f.get("origin_detail", "")),
            "prior": f.get("prior", ""),
        })
    return results


def extract_rounds(fm, slug):
    """Extract funding rounds from frontmatter."""
    rounds_raw = fm.get("funding_rounds", fm.get("rounds", []))
    if not isinstance(rounds_raw, list):
        return []
    results = []
    for r in rounds_raw:
        if not isinstance(r, dict):
            continue
        leads = r.get("lead_investors", r.get("lead", r.get("investors", [])))
        if isinstance(leads, list):
            leads = "; ".join(str(l) for l in leads)
        others = r.get("other_investors", [])
        if isinstance(others, list):
            others = "; ".join(str(o) for o in others)
        results.append({
            "company_slug": slug,
            "stage": r.get("stage", r.get("round", "")),
            "date": r.get("date", ""),
            "amount_m": normalize_money(r.get("amount_m", r.get("amount", r.get("amount_usd")))),
            "valuation_m": normalize_money(r.get("valuation_m", r.get("valuation", r.get("valuation_usd", r.get("post_money_valuation"))))),
            "lead_investors": leads or "",
            "other_investors": others or "",
            "source": r.get("source", r.get("source_url", "")),
            "notes": r.get("notes", ""),
        })
    return results


def extract_investors(fm, slug):
    """Extract top-level investor lists (key_investors, notable_backers) when no rounds exist."""
    investors = get_first("key_investors", "notable_backers", "investors", fm=fm)
    if not investors:
        return []
    if isinstance(investors, str):
        investors = [i.strip() for i in investors.split(",")]
    if isinstance(investors, list):
        return [{"company_slug": slug, "investor": str(i)} for i in investors]
    return []


def main():
    companies = []
    all_founders = []
    all_rounds = []
    all_investors = []

    for filepath in sorted(COMPANIES_DIR.glob("*.md")):
        slug = filepath.stem
        fm, body = parse_frontmatter(filepath)
        if not fm:
            continue

        company = extract_company(fm, body, slug)
        companies.append(company)

        founders = extract_founders(fm, slug)
        all_founders.extend(founders)

        rounds = extract_rounds(fm, slug)
        all_rounds.extend(rounds)

        investors = extract_investors(fm, slug)
        all_investors.extend(investors)

    # Write companies CSV
    EXPORTS_DIR.mkdir(exist_ok=True)
    company_fields = list(companies[0].keys())
    with open(EXPORTS_DIR / "companies_clean.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=company_fields)
        w.writeheader()
        w.writerows(companies)

    # Write founders CSV
    if all_founders:
        founder_fields = list(all_founders[0].keys())
        with open(EXPORTS_DIR / "founders_clean.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=founder_fields)
            w.writeheader()
            w.writerows(all_founders)

    # Write rounds CSV
    if all_rounds:
        round_fields = list(all_rounds[0].keys())
        with open(EXPORTS_DIR / "rounds_clean.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=round_fields)
            w.writeheader()
            w.writerows(all_rounds)

    # Write combined JSON
    company_map = {}
    for c in companies:
        slug = c["slug"]
        company_map[slug] = {
            **c,
            "founders": [f for f in all_founders if f["company_slug"] == slug],
            "funding_rounds": [r for r in all_rounds if r["company_slug"] == slug],
            "top_investors": [i["investor"] for i in all_investors if i["company_slug"] == slug],
        }
    with open(EXPORTS_DIR / "companies_clean.json", "w") as f:
        json.dump(list(company_map.values()), f, indent=2, default=str)

    # Print summary
    print(f"Companies: {len(companies)}")
    print(f"Founders:  {len(all_founders)}")
    print(f"Rounds:    {len(all_rounds)}")
    print(f"Investor entries: {len(all_investors)}")
    print()

    # Data quality report
    total = len(companies)
    quality = {}
    for field in company_fields:
        filled = sum(1 for c in companies if c[field] is not None and c[field] != "" and c[field] != "unknown")
        quality[field] = (filled, total)

    print("=== DATA QUALITY ===")
    for field, (filled, tot) in quality.items():
        bar = "█" * int(filled / tot * 20) + "░" * (20 - int(filled / tot * 20))
        print(f"  {field:25s} {bar} {filled:3d}/{tot} ({filled/tot*100:.0f}%)")

    # Companies missing key data
    print("\n=== COMPANIES MISSING FUNDING DATA ===")
    missing_funding = [c["name"] for c in companies if c["total_raised_m"] is None]
    print(f"  {len(missing_funding)} companies missing total_raised_m")
    if len(missing_funding) <= 30:
        for name in missing_funding:
            print(f"    - {name}")

    print("\n=== COMPANIES MISSING VALUATION ===")
    missing_val = [c["name"] for c in companies if c["latest_valuation_m"] is None]
    print(f"  {len(missing_val)} companies missing latest_valuation_m")

    print("\n=== COMPANIES MISSING FOUNDERS ===")
    slugs_with_founders = set(f["company_slug"] for f in all_founders)
    missing_founders = [c["name"] for c in companies if c["slug"] not in slugs_with_founders]
    print(f"  {len(missing_founders)} companies missing founder data")

    print(f"\nExports written to {EXPORTS_DIR}/")


if __name__ == "__main__":
    main()
