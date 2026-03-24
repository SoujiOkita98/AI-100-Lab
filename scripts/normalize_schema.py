#!/usr/bin/env python3
"""
Schema normalization script — fixes field names to match canonical schema.

Usage:
  python3 scripts/normalize_schema.py                    # Dry run (default)
  python3 scripts/normalize_schema.py --apply            # Actually modify files
  python3 scripts/normalize_schema.py --apply --batch 20 # Fix 20 files then stop
  python3 scripts/normalize_schema.py --file replit       # Single file
"""

import re
import yaml
import sys
import copy
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE / "companies"


def normalize_money_to_millions(val):
    """Convert raw USD or string money values to float millions."""
    if val is None or val == "":
        return None
    if isinstance(val, (int, float)):
        if val > 10_000_000:
            return round(val / 1_000_000, 1)
        return round(float(val), 1)
    s = str(val).strip().replace(",", "").replace("_", "")
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[~$><+]", "", s).strip()
    if not s or not any(c.isdigit() for c in s):
        return None
    if s.upper().endswith("B"):
        try: return round(float(s[:-1]) * 1000, 1)
        except: return None
    if s.upper().endswith("M"):
        try: return round(float(s[:-1]), 1)
        except: return None
    try:
        v = float(s)
        if v > 10_000_000:
            return round(v / 1_000_000, 1)
        return round(v, 1)
    except:
        return None


def raw_usd_to_millions(val):
    """Convert a value known to be raw USD to millions."""
    if val is None or val == "":
        return None
    s = str(val).strip().replace(",", "").replace("_", "")
    s = re.sub(r"[~$><+]", "", s).strip()
    try:
        return round(float(re.sub(r"[^0-9.]", "", s)) / 1_000_000, 1)
    except:
        return None


def normalize_file(fp, apply=False):
    """Normalize a single file. Returns (changes_list, new_text_or_None)."""
    text = fp.read_text()
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return [], None

    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except:
        return [("SKIP", "YAML parse error")], None

    original = copy.deepcopy(fm)
    changes = []
    body = text[m.end():]

    # === COMPANY-LEVEL FIELD RENAMES ===

    # name
    if not fm.get("name"):
        for alt in ["company", "company_name", "company_name_en"]:
            if fm.get(alt):
                fm["name"] = fm.pop(alt)
                changes.append(f"Renamed '{alt}' -> 'name'")
                break

    # Remove slug/domain/legal_name (filename is slug)
    for field in ["slug", "domain", "legal_name", "incorporated_country"]:
        if field in fm:
            fm.pop(field)
            changes.append(f"Removed '{field}'")

    # headquarters
    if not fm.get("headquarters"):
        for alt in ["hq", "location"]:
            if fm.get(alt):
                fm["headquarters"] = fm.pop(alt)
                changes.append(f"Renamed '{alt}' -> 'headquarters'")
                break
        # Merge hq_city + hq_country
        if not fm.get("headquarters") and fm.get("hq_city"):
            city = fm.pop("hq_city", "")
            country = fm.pop("hq_country", "")
            fm["headquarters"] = f"{city}, {country}".strip(", ")
            changes.append(f"Merged hq_city+hq_country -> 'headquarters'")
    else:
        # Remove redundant hq_city/hq_country if headquarters exists
        for field in ["hq_city", "hq_country"]:
            if field in fm:
                fm.pop(field)
                changes.append(f"Removed redundant '{field}'")

    # total_raised_m
    if fm.get("total_raised_m") is None:
        for alt in ["total_funding_usd", "total_funding", "total_raised",
                     "total_funding_raised", "total_known_funding",
                     "total_funding_confirmed", "total_funding_estimated"]:
            if fm.get(alt) is not None:
                val = normalize_money_to_millions(fm.pop(alt))
                if val is not None:
                    fm["total_raised_m"] = val
                    changes.append(f"Converted '{alt}' -> 'total_raised_m' ({val}M)")
                break

    # latest_valuation_m
    if fm.get("latest_valuation_m") is None:
        for alt in ["latest_valuation", "valuation", "last_valuation_usd",
                     "reported_valuation_usd"]:
            if fm.get(alt) is not None:
                val = normalize_money_to_millions(fm.pop(alt))
                if val is not None:
                    fm["latest_valuation_m"] = val
                    changes.append(f"Converted '{alt}' -> 'latest_valuation_m' ({val}M)")
                break

    # sector from tags
    if not fm.get("sector") and fm.get("tags"):
        fm["sector"] = fm.pop("tags")
        changes.append("Renamed 'tags' -> 'sector'")

    # status default
    if not fm.get("status"):
        fm["status"] = "active"
        changes.append("Added default 'status': 'active'")

    # === FOUNDER NORMALIZATION ===
    founders = fm.get("founders", [])
    if isinstance(founders, list):
        new_founders = []
        for f in founders:
            if isinstance(f, str):
                # Parse "Name (Role)" format
                match = re.match(r"^(.+?)\s*\((.+?)\)$", f.strip())
                if match:
                    new_founders.append({"name": match.group(1).strip(), "role": match.group(2).strip()})
                else:
                    new_founders.append({"name": f.strip(), "role": "Co-founder"})
                changes.append(f"Converted string founder '{f[:30]}' to dict")
            elif isinstance(f, dict):
                nf = {}
                nf["name"] = f.get("name", "")
                nf["role"] = f.get("role", "")

                # Build background from multiple fields
                bg_parts = []
                if f.get("background"):
                    bg_parts.append(str(f["background"]).strip())
                if f.get("education"):
                    edu = f["education"]
                    if isinstance(edu, list):
                        edu = "; ".join(str(e) for e in edu)
                    bg_parts.append(str(edu).strip())
                    changes.append(f"Merged founder '{nf['name']}' education -> background")
                if f.get("prior_experience"):
                    exp = f["prior_experience"]
                    if isinstance(exp, list):
                        exp = "; ".join(str(e) for e in exp)
                    bg_parts.append(str(exp).strip())
                    changes.append(f"Merged founder '{nf['name']}' prior_experience -> background")
                if f.get("notable"):
                    bg_parts.append(str(f["notable"]).strip())
                    changes.append(f"Merged founder '{nf['name']}' notable -> background")
                if bg_parts:
                    nf["background"] = " ".join(bg_parts).strip()

                # Origin from nationality/ethnicity
                origin = f.get("origin") or f.get("nationality") or f.get("ethnicity")
                if origin:
                    nf["origin"] = str(origin).strip()
                    if f.get("nationality") and not f.get("origin"):
                        changes.append(f"Renamed founder '{nf['name']}' nationality -> origin")
                    if f.get("ethnicity") and not f.get("origin"):
                        changes.append(f"Renamed founder '{nf['name']}' ethnicity -> origin")

                if f.get("prior"):
                    nf["prior"] = f["prior"]

                new_founders.append(nf)
            else:
                new_founders.append(f)

        if new_founders:
            fm["founders"] = new_founders

    # === FUNDING ROUND NORMALIZATION ===
    rounds = fm.get("funding_rounds", [])
    if isinstance(rounds, list):
        new_rounds = []
        for r in rounds:
            if not isinstance(r, dict):
                continue
            nr = {}

            # stage
            nr["stage"] = r.get("stage") or r.get("round", "")
            if r.get("round") and not r.get("stage"):
                changes.append(f"Renamed round 'round' -> 'stage' ({nr['stage']})")

            nr["date"] = r.get("date", "")

            # amount_m
            if r.get("amount_usd") is not None:
                nr["amount_m"] = raw_usd_to_millions(r["amount_usd"])
                changes.append(f"Converted round amount_usd -> amount_m ({nr['amount_m']})")
            elif r.get("amount_m") is not None:
                nr["amount_m"] = normalize_money_to_millions(r["amount_m"])
            elif r.get("amount") is not None:
                nr["amount_m"] = normalize_money_to_millions(r["amount"])
                changes.append(f"Renamed round 'amount' -> 'amount_m'")
            elif r.get("amount_eur") is not None:
                # Rough EUR->USD conversion (1.1x)
                val = normalize_money_to_millions(r["amount_eur"])
                if val:
                    nr["amount_m"] = round(val * 1.1, 1)
                changes.append(f"Converted round amount_eur -> amount_m (~USD)")

            # valuation_m
            if r.get("valuation_usd") is not None:
                nr["valuation_m"] = raw_usd_to_millions(r["valuation_usd"])
                changes.append(f"Converted round valuation_usd -> valuation_m")
            elif r.get("valuation_m") is not None:
                nr["valuation_m"] = normalize_money_to_millions(r["valuation_m"])
            elif r.get("valuation") is not None:
                nr["valuation_m"] = normalize_money_to_millions(r["valuation"])
                changes.append(f"Renamed round 'valuation' -> 'valuation_m'")

            # lead_investors (normalize to list)
            leads = r.get("lead_investors") or r.get("lead_investor") or r.get("lead")
            if leads:
                if isinstance(leads, str):
                    leads = [leads]
                nr["lead_investors"] = leads
                if r.get("lead_investor"):
                    changes.append("Renamed round 'lead_investor' -> 'lead_investors'")

            # other_investors
            others = r.get("other_investors") or r.get("participants") or r.get("contributors")
            if others:
                if isinstance(others, str):
                    others = [others]
                nr["other_investors"] = others

            if r.get("source") or r.get("source_url"):
                nr["source"] = r.get("source") or r.get("source_url", "")
            if r.get("notes") or r.get("note"):
                nr["notes"] = r.get("notes") or r.get("note", "")

            new_rounds.append(nr)

        fm["funding_rounds"] = new_rounds

    # Check if anything changed
    if fm == original:
        return [], None

    if not apply:
        return changes, None

    # Write the file
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True,
                       sort_keys=False, width=120)
    new_text = f"---\n{new_fm}---{body}"
    fp.write_text(new_text)
    return changes, new_text


def main():
    apply = "--apply" in sys.argv
    batch_size = None
    single_file = None

    for i, arg in enumerate(sys.argv):
        if arg == "--batch" and i + 1 < len(sys.argv):
            batch_size = int(sys.argv[i + 1])
        if arg == "--file" and i + 1 < len(sys.argv):
            single_file = sys.argv[i + 1]

    files = sorted(COMPANIES_DIR.glob("*.md"))
    if single_file:
        files = [f for f in files if single_file in f.stem]

    mode = "APPLY" if apply else "DRY RUN"
    print(f"=== Schema Normalization ({mode}) ===\n")

    modified = 0
    skipped = 0
    total_changes = 0

    for fp in files:
        if batch_size and modified >= batch_size:
            print(f"\n--- Batch limit reached ({batch_size} files). Stopping. ---")
            break

        changes, _ = normalize_file(fp, apply=apply)
        if changes:
            modified += 1
            total_changes += len(changes)
            print(f"\n  {fp.stem} ({len(changes)} changes):")
            for c in changes[:10]:
                print(f"    - {c}")
            if len(changes) > 10:
                print(f"    ... and {len(changes) - 10} more")
        else:
            skipped += 1

    print(f"\n{'='*60}")
    print(f"  {mode} complete: {modified} files would be modified, {skipped} already clean")
    print(f"  Total changes: {total_changes}")
    if not apply and modified > 0:
        print(f"\n  Run with --apply to actually modify files.")
        print(f"  Run with --apply --batch 20 to fix 20 files at a time.")


if __name__ == "__main__":
    main()
