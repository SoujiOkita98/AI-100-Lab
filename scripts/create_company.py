#!/usr/bin/env python3
"""
Create new company markdown files from a JSON input.
Usage: python3 create_company.py new_companies.json
"""

import json
import sys
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE / "companies"


def slugify(name):
    """Convert company name to slug."""
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')


def create_company_file(company):
    name = company["name"]
    slug = company.get("slug") or slugify(name)
    filepath = COMPANIES_DIR / f"{slug}.md"

    if filepath.exists():
        print(f"  SKIP {slug}.md: already exists")
        return False

    # Build frontmatter
    lines = ["---"]
    lines.append(f'name: "{name}"')
    if company.get("founded"):
        lines.append(f'founded: {company["founded"]}')
    if company.get("hq"):
        lines.append(f'headquarters: "{company["hq"]}"')
    if company.get("website"):
        lines.append(f'website: {company["website"]}')
    if company.get("sector"):
        lines.append(f'sector: "{company["sector"]}"')
    if company.get("one_liner"):
        lines.append(f'one_liner: "{company["one_liner"]}"')
    lines.append("status: active")

    # Founders
    founders = company.get("founders", [])
    if founders:
        lines.append("founders:")
        for f in founders:
            if isinstance(f, dict):
                lines.append(f'  - name: "{f.get("name", "")}"')
                if f.get("role"):
                    lines.append(f'    role: "{f["role"]}"')
                if f.get("background"):
                    lines.append(f'    background: "{f["background"]}"')
            elif isinstance(f, str):
                lines.append(f'  - "{f}"')

    # Funding rounds
    rounds = company.get("funding_rounds", [])
    if rounds:
        lines.append("funding_rounds:")
        for r in rounds:
            lines.append(f'  - stage: "{r.get("stage", "")}"')
            if r.get("date"):
                lines.append(f'    date: "{r["date"]}"')
            if r.get("amount_m") is not None:
                lines.append(f'    amount_m: {r["amount_m"]}')
            if r.get("valuation_m") is not None:
                lines.append(f'    valuation_m: {r["valuation_m"]}')
            leads = r.get("lead_investors", [])
            if leads:
                leads_str = ", ".join(f'"{l}"' for l in leads)
                lines.append(f'    lead_investors: [{leads_str}]')
            if r.get("source"):
                lines.append(f'    source: "{r["source"]}"')
            if r.get("notes"):
                lines.append(f'    notes: "{r["notes"]}"')

    # Total raised
    if company.get("total_raised_m"):
        lines.append(f'total_funding: {company["total_raised_m"]}')
    if company.get("latest_valuation_m"):
        lines.append(f'latest_valuation: {company["latest_valuation_m"]}')

    lines.append("last_updated: 2026-03-21")
    lines.append("confidence: medium")
    lines.append("---")
    lines.append("")
    lines.append(f"# {name}")
    lines.append("")

    if company.get("one_liner"):
        lines.append(f"{company['one_liner']}")
        lines.append("")

    if company.get("sources"):
        lines.append("## Sources")
        lines.append("")
        for src in company["sources"]:
            lines.append(f"- {src}")
        lines.append("")

    filepath.write_text("\n".join(lines), encoding="utf-8")
    print(f"  CREATED {slug}.md")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 create_company.py <companies_json_file>")
        sys.exit(1)

    data = json.load(open(sys.argv[1]))
    created = 0
    skipped = 0
    for company in data:
        if create_company_file(company):
            created += 1
        else:
            skipped += 1

    print(f"\nDone: {created} created, {skipped} skipped")


if __name__ == "__main__":
    main()
