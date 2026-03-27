#!/usr/bin/env python3
"""
normalize_and_export.py

Parses all company markdown files in companies/, extracts YAML frontmatter,
normalizes field names to the canonical schema, and exports:
  1. exports/master.csv — flat CSV with one row per company
  2. exports/funding_rounds.csv — one row per funding round
  3. exports/founders.csv — one row per founder
  4. A consistency report to stdout

Usage:
    python3 scripts/normalize_and_export.py
"""

import os
import re
import csv
import yaml
import json
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE_DIR / "companies"
EXPORTS_DIR = BASE_DIR / "exports"
EXPORTS_DIR.mkdir(exist_ok=True)

# === Field name mapping: various agent-generated names -> canonical ===
FIELD_MAP = {
    # name
    "company": "name", "company_name": "name", "brand_name": "name",
    # status
    "stage": None,  # ambiguous, skip
    # founded
    "founded": "founded_year", "founded_year": "founded_year", "year_founded": "founded_year",
    # hq
    "headquarters": "hq", "hq": "hq", "location": "hq",
    # website
    "website": "website", "domain": "website", "url": "website",
    # sector
    "sector": "sector", "sectors": "sector", "tags": None,
    # one liner
    "one_liner": "one_liner", "description": "one_liner", "tagline": "one_liner",
    # funding
    "total_raised_m": "total_raised_m", "total_funding": "total_raised_m",
    "total_funding_raised": "total_raised_m", "total_funding_m": "total_raised_m",
    # valuation
    "latest_valuation_m": "latest_valuation_m", "latest_valuation": "latest_valuation_m",
    "valuation": "latest_valuation_m", "estimated_valuation": "latest_valuation_m",
    # rounds
    "funding_rounds": "funding_rounds",
    # founders
    "founders": "founders",
    # business
    "business_model": "business_model",
    "revenue_signals": "revenue_signals", "arr": "revenue_signals",
    "arr_estimate": "revenue_signals",
    # customers
    "customers": "key_customers", "key_customers": "key_customers",
    # meta
    "sources": "sources",
    "last_updated": "last_updated", "research_date": "last_updated",
    "confidence": "confidence",
    # logo
    "logo": "logo",
}


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None, text
    try:
        data = yaml.safe_load(match.group(1))
        body = text[match.end():]
        return data if isinstance(data, dict) else None, body
    except yaml.YAMLError as e:
        print(f"  YAML error in {filepath.name}: {e}")
        return None, text


def parse_valuation_string(val):
    """Convert various valuation formats to float (millions)."""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip().lower().replace(",", "").replace("$", "")
    # Handle "7.2B" or "$7.2B"
    m = re.match(r"([\d.]+)\s*b", s)
    if m:
        return float(m.group(1)) * 1000
    m = re.match(r"([\d.]+)\s*m", s)
    if m:
        return float(m.group(1))
    # Handle plain numbers
    try:
        v = float(s)
        # Heuristic: if < 1000, likely billions
        if v < 500:
            return v * 1000
        return v
    except ValueError:
        return None


def parse_funding_string(val):
    """Convert various funding total formats to float (millions)."""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip().lower().replace(",", "").replace("$", "").replace("~", "").replace("+", "")
    m = re.match(r"([\d.]+)\s*b", s)
    if m:
        return float(m.group(1)) * 1000
    m = re.match(r"([\d.]+)\s*m", s)
    if m:
        return float(m.group(1))
    try:
        return float(s)
    except ValueError:
        return None


def extract_founded_year(val):
    """Extract a 4-digit year from various date formats."""
    if val is None:
        return None
    s = str(val).strip()
    m = re.search(r"((?:19|20)\d{2})", s)
    return int(m.group(1)) if m else None


def normalize(raw, slug):
    """Normalize raw frontmatter dict to canonical fields."""
    out = {"slug": slug}

    # Map known fields
    for raw_key, raw_val in raw.items():
        canon = FIELD_MAP.get(raw_key.lower().strip())
        if canon and canon not in out:
            out[canon] = raw_val

    # If name is missing, derive from slug
    if "name" not in out or not out["name"]:
        out["name"] = slug.replace("-", " ").title()

    # Normalize founded_year
    out["founded_year"] = extract_founded_year(out.get("founded_year"))

    # Normalize funding
    out["total_raised_m"] = parse_funding_string(out.get("total_raised_m"))
    out["latest_valuation_m"] = parse_valuation_string(out.get("latest_valuation_m"))

    # Ensure lists
    for key in ["sector", "key_customers", "sources"]:
        v = out.get(key)
        if isinstance(v, str):
            out[key] = [v]
        elif not isinstance(v, list):
            out[key] = []

    # Normalize sector to first 3
    out["sector"] = out.get("sector", [])[:3]

    # Ensure founders is a list of dicts
    founders = out.get("founders", [])
    if not isinstance(founders, list):
        founders = []
    out["founders"] = founders

    # Ensure funding_rounds is a list
    rounds = out.get("funding_rounds", [])
    if not isinstance(rounds, list):
        rounds = []
    out["funding_rounds"] = rounds

    # Fill defaults
    out.setdefault("hq", None)
    out.setdefault("website", None)
    out.setdefault("one_liner", None)
    out.setdefault("status", "active")
    out.setdefault("business_model", None)
    out.setdefault("revenue_signals", None)
    out.setdefault("confidence", "medium")
    out.setdefault("last_updated", str(date.today()))

    return out


def export_master_csv(companies):
    """Export flat CSV with one row per company."""
    path = EXPORTS_DIR / "master.csv"
    fields = [
        "slug", "name", "status", "founded_year", "hq", "website",
        "sector", "one_liner", "total_raised_m", "latest_valuation_m",
        "business_model", "revenue_signals",
        "num_founders", "num_rounds", "key_customers", "confidence",
        "last_updated"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for c in sorted(companies, key=lambda x: x["slug"]):
            row = dict(c)
            row["sector"] = "; ".join(row.get("sector", []))
            row["key_customers"] = "; ".join(row.get("key_customers", [])[:10])
            row["num_founders"] = len(row.get("founders", []))
            row["num_rounds"] = len(row.get("funding_rounds", []))
            w.writerow(row)
    print(f"Wrote {len(companies)} rows to {path}")


def export_founders_csv(companies):
    """Export one row per founder."""
    path = EXPORTS_DIR / "founders.csv"
    fields = ["company_slug", "company_name", "founder_name", "role", "background", "origin", "status"]
    rows = []
    for c in companies:
        for f in c.get("founders", []):
            if isinstance(f, dict):
                rows.append({
                    "company_slug": c["slug"],
                    "company_name": c["name"],
                    "founder_name": f.get("name", ""),
                    "role": f.get("role", ""),
                    "background": f.get("background", ""),
                    "origin": f.get("origin", f.get("nationality", f.get("ethnic_origin", ""))),
                    "status": f.get("status", ""),
                })
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} founder rows to {path}")


def export_funding_csv(companies):
    """Export one row per funding round."""
    path = EXPORTS_DIR / "funding_rounds.csv"
    fields = ["company_slug", "company_name", "stage", "date", "amount_m", "valuation_m", "lead_investors", "source"]
    rows = []
    for c in companies:
        for r in c.get("funding_rounds", []):
            if isinstance(r, dict):
                leads = r.get("lead_investors", [])
                if isinstance(leads, list):
                    leads = "; ".join(str(l) for l in leads)
                rows.append({
                    "company_slug": c["slug"],
                    "company_name": c["name"],
                    "stage": r.get("stage", ""),
                    "date": r.get("date", ""),
                    "amount_m": r.get("amount_m", ""),
                    "valuation_m": r.get("valuation_m", ""),
                    "lead_investors": leads,
                    "source": r.get("source", ""),
                })
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} funding round rows to {path}")


def main():
    companies = []
    issues = []

    for md_file in sorted(COMPANIES_DIR.glob("*.md")):
        slug = md_file.stem
        raw, body = parse_frontmatter(md_file)
        if raw is None:
            issues.append(f"NO FRONTMATTER: {slug}")
            continue

        normalized = normalize(raw, slug)
        companies.append(normalized)

        # Check for missing critical fields
        for field in ["name", "founded_year", "total_raised_m"]:
            if not normalized.get(field):
                issues.append(f"MISSING {field}: {slug}")

    print(f"\n{'='*60}")
    print(f"PARSED: {len(companies)} companies")
    print(f"ISSUES: {len(issues)}")
    for i in issues:
        print(f"  - {i}")
    print(f"{'='*60}\n")

    export_master_csv(companies)
    export_founders_csv(companies)
    export_funding_csv(companies)

    # Summary stats
    with_val = sum(1 for c in companies if c.get("latest_valuation_m"))
    with_founders = sum(1 for c in companies if len(c.get("founders", [])) > 0)
    with_rounds = sum(1 for c in companies if len(c.get("funding_rounds", [])) > 0)
    print(f"\nCoverage:")
    print(f"  Companies with valuation: {with_val}/{len(companies)}")
    print(f"  Companies with founders:  {with_founders}/{len(companies)}")
    print(f"  Companies with rounds:    {with_rounds}/{len(companies)}")


if __name__ == "__main__":
    main()
