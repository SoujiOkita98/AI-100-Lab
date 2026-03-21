#!/usr/bin/env python3
"""
Inject funding_rounds data into existing company markdown files.
Reads round data from a JSON file and inserts/replaces funding_rounds
in each company's YAML frontmatter.

Usage:
    python3 inject_rounds.py rounds_to_inject.json
"""

import json
import re
import sys
import yaml
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE / "companies"


def inject_rounds_into_file(filepath, rounds_data):
    """Insert or replace funding_rounds in a company's frontmatter."""
    text = filepath.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        print(f"  SKIP {filepath.name}: no frontmatter found")
        return False

    fm_text = m.group(1)
    body = text[m.end():]

    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        print(f"  SKIP {filepath.name}: YAML parse error: {e}")
        return False

    # Check if funding_rounds already exists with data
    existing = fm.get("funding_rounds", [])
    if existing and isinstance(existing, list) and len(existing) > 0:
        first = existing[0]
        if isinstance(first, dict) and ("stage" in first or "round" in first):
            print(f"  SKIP {filepath.name}: already has {len(existing)} rounds")
            return False

    # Inject the new rounds
    fm["funding_rounds"] = rounds_data

    # Re-serialize frontmatter
    # Use default_flow_style=False for readable YAML
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True,
                       sort_keys=False, width=120)

    new_text = f"---\n{new_fm}---{body}"
    filepath.write_text(new_text, encoding="utf-8")
    print(f"  WROTE {filepath.name}: {len(rounds_data)} rounds injected")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 inject_rounds.py <rounds_json_file>")
        sys.exit(1)

    data_file = Path(sys.argv[1])
    with open(data_file) as f:
        all_data = json.load(f)

    injected = 0
    skipped = 0
    not_found = 0

    for entry in all_data:
        slug = entry.get("slug", "")
        rounds = entry.get("funding_rounds", [])
        if not slug or not rounds:
            continue

        filepath = COMPANIES_DIR / f"{slug}.md"
        if not filepath.exists():
            print(f"  NOT FOUND: {slug}.md")
            not_found += 1
            continue

        if inject_rounds_into_file(filepath, rounds):
            injected += 1
        else:
            skipped += 1

    print(f"\nDone: {injected} injected, {skipped} skipped, {not_found} not found")


if __name__ == "__main__":
    main()
