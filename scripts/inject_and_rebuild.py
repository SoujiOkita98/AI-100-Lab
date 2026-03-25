#!/usr/bin/env python3
"""
inject_and_rebuild.py

Reads new_data.json (containing new companies, founder origin updates, and new rounds),
merges into data/*.json, and rebuilds the SQLite database.

new_data.json format:
{
  "origin_updates": [
    {"company_slug": "xxx", "founder_name": "Foo Bar", "origin": "Chinese-American"}
  ],
  "new_companies": [
    {
      "slug": "my-co",
      "name": "My Co",
      "status": "active",
      "founded_year": 2025,
      "hq": "San Francisco, CA",
      "website": "https://myco.com",
      "sectors": ["AI"],
      "one_liner": "Does cool stuff",
      "total_raised_m": 10.0,
      "latest_valuation_m": null,
      "founders": [
        {"name": "John Doe", "role": "CEO", "origin": "Chinese-American", "background": "..."}
      ],
      "rounds": [
        {"stage": "Seed", "date": "2025-06", "amount_m": 10.0, "lead_investors": ["Sequoia"], "source": "..."}
      ]
    }
  ]
}
"""

import json
import sqlite3
import sys
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
EXPORTS_DIR = BASE / "exports"


def load_json(name):
    with open(DATA_DIR / name, "r") as f:
        return json.load(f)


def save_json(name, data):
    with open(DATA_DIR / name, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {len(data)} records to data/{name}")


def apply_origin_updates(founders, updates):
    """Update origin fields for existing founders."""
    updated = 0
    for upd in updates:
        slug = upd["company_slug"]
        name = upd["founder_name"]
        new_origin = upd["origin"]
        new_name = upd.get("real_name")  # For "Unknown" founders

        for f in founders:
            if f["company_slug"] == slug and (f["name"] == name or (name == "Unknown" and f["name"] == "Unknown")):
                if new_name and f["name"] == "Unknown":
                    f["name"] = new_name
                if new_origin:
                    f["origin"] = new_origin
                if upd.get("background"):
                    f["background"] = upd["background"]
                updated += 1
                break
    print(f"  Updated origins for {updated} founders")
    return founders


def add_new_companies(companies, founders, rounds, new_companies):
    """Add new companies, founders, and rounds."""
    existing_slugs = {c["slug"] for c in companies}
    added = 0
    skipped = 0

    for nc in new_companies:
        slug = nc["slug"]
        if slug in existing_slugs:
            print(f"  SKIP {slug}: already exists")
            skipped += 1
            continue

        # Add company
        companies.append({
            "slug": slug,
            "name": nc["name"],
            "status": nc.get("status", "active"),
            "founded_year": nc.get("founded_year"),
            "hq": nc.get("hq"),
            "website": nc.get("website"),
            "sectors": nc.get("sectors", []),
            "one_liner": nc.get("one_liner"),
            "logo_file": None,
            "total_raised_m": nc.get("total_raised_m"),
            "latest_valuation_m": nc.get("latest_valuation_m"),
            "latest_round": None,
            "latest_round_date": None,
            "business_model": nc.get("business_model"),
            "revenue_signals": None,
            "key_customers": [],
            "employee_count": None,
            "team_china_profile": None,
            "engagement": {
                "status": "none",
                "first_contact_date": None,
                "source": None,
                "owner": None,
                "notes": None
            },
            "sources": nc.get("sources", []),
            "confidence": nc.get("confidence", "Medium"),
            "last_updated": str(date.today())
        })

        # Add founders
        for f in nc.get("founders", []):
            founders.append({
                "company_slug": slug,
                "name": f.get("name", ""),
                "role": f.get("role", ""),
                "background": f.get("background", ""),
                "origin": f.get("origin", ""),
                "origin_detail": "",
                "status": "unknown",
                "departed_to": ""
            })

        # Add rounds
        for r in nc.get("rounds", []):
            leads = r.get("lead_investors", [])
            if isinstance(leads, str):
                leads = [leads]
            rounds.append({
                "company_slug": slug,
                "stage": r.get("stage", ""),
                "date": r.get("date", ""),
                "amount_m": r.get("amount_m"),
                "valuation_m": r.get("valuation_m"),
                "lead_investors": leads,
                "source": r.get("source", ""),
                "notes": r.get("notes", "")
            })

        existing_slugs.add(slug)
        added += 1

    print(f"  Added {added} new companies, skipped {skipped}")
    return companies, founders, rounds


def rebuild_sqlite(companies, founders, rounds):
    """Rebuild the SQLite database from JSON data."""
    db_path = EXPORTS_DIR / "ai100lab.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS companies")
    cur.execute("DROP TABLE IF EXISTS founders")
    cur.execute("DROP TABLE IF EXISTS rounds")

    cur.execute("""CREATE TABLE companies (
        slug TEXT PRIMARY KEY,
        name TEXT,
        status TEXT,
        founded_year INTEGER,
        hq TEXT,
        website TEXT,
        sector TEXT,
        one_liner TEXT,
        total_raised_m REAL,
        latest_valuation_m REAL,
        employees TEXT,
        revenue_signals TEXT,
        business_model TEXT,
        key_customers TEXT,
        team_china_profile TEXT,
        confidence TEXT,
        last_updated TEXT
    )""")

    cur.execute("""CREATE TABLE founders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_slug TEXT,
        name TEXT,
        role TEXT,
        background TEXT,
        origin TEXT,
        prior TEXT
    )""")

    cur.execute("""CREATE TABLE rounds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_slug TEXT,
        stage TEXT,
        date TEXT,
        amount_m REAL,
        valuation_m REAL,
        lead_investors TEXT,
        other_investors TEXT,
        source TEXT,
        notes TEXT
    )""")

    for c in companies:
        sectors = c.get("sectors", [])
        if isinstance(sectors, list):
            sectors = "; ".join(sectors)
        customers = c.get("key_customers", [])
        if isinstance(customers, list):
            customers = "; ".join(str(x) for x in customers)
        cur.execute("""INSERT INTO companies VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            c["slug"], c["name"], c.get("status"), c.get("founded_year"),
            c.get("hq"), c.get("website"), sectors, c.get("one_liner"),
            c.get("total_raised_m"), c.get("latest_valuation_m"),
            str(c.get("employee_count", "")) or None,
            c.get("revenue_signals"), c.get("business_model"),
            customers or None, c.get("team_china_profile"),
            c.get("confidence"), c.get("last_updated")
        ))

    for f in founders:
        cur.execute("""INSERT INTO founders (company_slug, name, role, background, origin, prior)
                       VALUES (?,?,?,?,?,?)""", (
            f["company_slug"], f["name"], f.get("role", ""),
            f.get("background", ""), f.get("origin", ""),
            f.get("prior", f.get("departed_to", ""))
        ))

    for r in rounds:
        leads = r.get("lead_investors", "")
        if isinstance(leads, list):
            leads = "; ".join(leads)
        others = r.get("other_investors", "")
        if isinstance(others, list):
            others = "; ".join(others)
        cur.execute("""INSERT INTO rounds (company_slug, stage, date, amount_m, valuation_m,
                       lead_investors, other_investors, source, notes)
                       VALUES (?,?,?,?,?,?,?,?,?)""", (
            r["company_slug"], r.get("stage", ""), r.get("date", ""),
            r.get("amount_m"), r.get("valuation_m"),
            leads, others, r.get("source", ""), r.get("notes", "")
        ))

    # Indexes
    cur.execute("CREATE INDEX IF NOT EXISTS idx_founders_slug ON founders(company_slug)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_rounds_slug ON rounds(company_slug)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_rounds_stage ON rounds(stage)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_rounds_date ON rounds(date)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_founders_origin ON founders(origin)")

    conn.commit()
    conn.close()
    print(f"  Rebuilt SQLite: {len(companies)} companies, {len(rounds)} rounds, {len(founders)} founders")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 inject_and_rebuild.py <new_data.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        new_data = json.load(f)

    print("Loading existing data...")
    companies = load_json("companies.json")
    founders = load_json("founders.json")
    rounds = load_json("rounds.json")
    print(f"  Existing: {len(companies)} companies, {len(founders)} founders, {len(rounds)} rounds")

    # Apply origin updates
    origin_updates = new_data.get("origin_updates", [])
    if origin_updates:
        print(f"\nApplying {len(origin_updates)} origin updates...")
        founders = apply_origin_updates(founders, origin_updates)

    # Add new companies
    new_companies = new_data.get("new_companies", [])
    if new_companies:
        print(f"\nAdding {len(new_companies)} new companies...")
        companies, founders, rounds = add_new_companies(companies, founders, rounds, new_companies)

    # Sort
    companies.sort(key=lambda x: x["slug"])
    founders.sort(key=lambda x: (x["company_slug"], x["name"]))
    rounds.sort(key=lambda x: (x["company_slug"], x.get("date", "")))

    # Save JSON
    print("\nSaving JSON...")
    save_json("companies.json", companies)
    save_json("founders.json", founders)
    save_json("rounds.json", rounds)

    # Rebuild SQLite
    print("\nRebuilding SQLite...")
    rebuild_sqlite(companies, founders, rounds)

    print("\nDone!")


if __name__ == "__main__":
    main()
