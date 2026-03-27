#!/usr/bin/env python3
"""
Schema validation script — reports all deviations from the canonical schema.
Read-only: does NOT modify any files.

Usage:
  python3 scripts/validate_schema.py              # Full report
  python3 scripts/validate_schema.py --summary    # Counts only
  python3 scripts/validate_schema.py --file replit # Single file
"""

import re
import yaml
import sys
from pathlib import Path
from collections import Counter

BASE = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE / "companies"

# === CANONICAL SCHEMA ===

REQUIRED_COMPANY_FIELDS = {"name", "founded", "headquarters", "website", "sector", "one_liner", "status"}

STANDARD_COMPANY_FIELDS = REQUIRED_COMPANY_FIELDS | {
    "total_raised_m", "latest_valuation_m", "founders", "funding_rounds",
    "confidence", "last_updated", "linkedin", "linkedin_verified",
    "twitter", "crunchbase", "crunchbase_verified", "website_verified",
    "employees", "revenue_signals", "business_model", "key_customers",
    "data_notes", "logo",
}

RENAME_COMPANY_FIELDS = {
    "company": "name", "company_name": "name", "company_name_en": "name",
    "hq": "headquarters", "location": "headquarters",
    "hq_city": "REMOVE (merge into headquarters)",
    "hq_country": "REMOVE (merge into headquarters)",
    "total_funding_usd": "total_raised_m (convert to millions)",
    "total_funding": "total_raised_m", "total_raised": "total_raised_m",
    "total_funding_raised": "total_raised_m",
    "latest_valuation": "latest_valuation_m",
    "valuation": "latest_valuation_m",
    "slug": "REMOVE (filename is slug)",
    "domain": "REMOVE", "legal_name": "REMOVE",
    "incorporated_country": "REMOVE",
    "tags": "sector",
}

STANDARD_ROUND_FIELDS = {"stage", "date", "amount_m", "valuation_m",
                          "lead_investors", "other_investors", "source", "notes"}

RENAME_ROUND_FIELDS = {
    "round": "stage",
    "amount": "amount_m",
    "amount_usd": "amount_m (divide by 1M)",
    "amount_eur": "amount_m (convert EUR to USD millions)",
    "valuation": "valuation_m",
    "valuation_usd": "valuation_m (divide by 1M)",
    "valuation_eur": "valuation_m (convert EUR to USD millions)",
    "lead_investor": "lead_investors (make list)",
    "lead": "lead_investors",
    "participants": "other_investors",
    "contributors": "other_investors",
    "co_leads": "lead_investors (merge)",
    "angel_investors": "other_investors",
    "note": "notes",
}

STANDARD_FOUNDER_FIELDS = {"name", "role", "background", "origin", "prior"}

RENAME_FOUNDER_FIELDS = {
    "education": "background (merge into background)",
    "nationality": "origin",
    "ethnicity": "origin",
    "prior_experience": "background (merge into background)",
    "notable": "background (merge into background)",
    "age_approx": "REMOVE",
    "source": "REMOVE",
    "current": "REMOVE",
}


def validate_file(fp):
    """Validate a single company file. Returns list of (severity, message) tuples."""
    issues = []
    text = fp.read_text()

    # Check frontmatter exists
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return [("ERROR", "No YAML frontmatter found")]

    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return [("ERROR", f"YAML parse error: {e}")]

    if not isinstance(fm, dict):
        return [("ERROR", "Frontmatter is not a dict")]

    # Check required fields
    for field in REQUIRED_COMPANY_FIELDS:
        if not fm.get(field):
            issues.append(("MISSING", f"Required field '{field}' is empty or missing"))

    # Check for non-standard company fields
    for key in fm.keys():
        if key in RENAME_COMPANY_FIELDS:
            target = RENAME_COMPANY_FIELDS[key]
            issues.append(("RENAME", f"'{key}' → {target}"))
        elif key not in STANDARD_COMPANY_FIELDS:
            issues.append(("EXTRA", f"Non-standard field '{key}'"))

    # Validate founders
    founders = fm.get("founders", [])
    if isinstance(founders, list):
        for i, f in enumerate(founders):
            if isinstance(f, str):
                issues.append(("FORMAT", f"Founder [{i}] is a string, should be dict"))
            elif isinstance(f, dict):
                if not f.get("name"):
                    issues.append(("MISSING", f"Founder [{i}] has no 'name'"))
                for key in f.keys():
                    if key in RENAME_FOUNDER_FIELDS:
                        target = RENAME_FOUNDER_FIELDS[key]
                        issues.append(("RENAME", f"Founder '{f.get('name','?')}': '{key}' → {target}"))
                    elif key not in STANDARD_FOUNDER_FIELDS:
                        issues.append(("EXTRA", f"Founder '{f.get('name','?')}': non-standard field '{key}'"))

    # Validate funding rounds
    rounds = fm.get("funding_rounds", [])
    if isinstance(rounds, list):
        for i, r in enumerate(rounds):
            if not isinstance(r, dict):
                issues.append(("FORMAT", f"Round [{i}] is not a dict"))
                continue
            for key in r.keys():
                if key in RENAME_ROUND_FIELDS:
                    target = RENAME_ROUND_FIELDS[key]
                    issues.append(("RENAME", f"Round '{r.get('stage', r.get('round', f'[{i}]'))}': '{key}' → {target}"))
                elif key not in STANDARD_ROUND_FIELDS:
                    issues.append(("EXTRA", f"Round '{r.get('stage', f'[{i}]')}': non-standard field '{key}'"))

    return issues


def main():
    summary_only = "--summary" in sys.argv
    single_file = None
    for arg in sys.argv[1:]:
        if arg.startswith("--file"):
            idx = sys.argv.index(arg)
            if idx + 1 < len(sys.argv):
                single_file = sys.argv[idx + 1]

    files = sorted(COMPANIES_DIR.glob("*.md"))
    if single_file:
        files = [f for f in files if single_file in f.stem]

    severity_counts = Counter()
    issue_type_counts = Counter()
    files_with_issues = 0
    clean_files = 0

    for fp in files:
        issues = validate_file(fp)
        if issues:
            files_with_issues += 1
            if not summary_only:
                print(f"\n{'='*60}")
                print(f"  {fp.stem}")
                print(f"{'='*60}")
                for severity, msg in issues:
                    print(f"  [{severity}] {msg}")
                    severity_counts[severity] += 1
                    issue_type_counts[msg.split("'")[1] if "'" in msg else msg[:30]] += 1
            else:
                for severity, msg in issues:
                    severity_counts[severity] += 1
        else:
            clean_files += 1

    print(f"\n{'='*60}")
    print(f"  SUMMARY: {len(files)} files checked")
    print(f"{'='*60}")
    print(f"  Clean files: {clean_files}")
    print(f"  Files with issues: {files_with_issues}")
    print(f"\n  By severity:")
    for sev, count in severity_counts.most_common():
        print(f"    {sev:10s}: {count}")


if __name__ == "__main__":
    main()
