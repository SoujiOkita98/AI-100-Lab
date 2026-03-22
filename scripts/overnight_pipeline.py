#!/usr/bin/env python3
"""
Overnight pipeline: scrape VC portfolios, identify AI gaps, research them.
Run this and come back to a comprehensive dataset.
"""

import subprocess
import json
import os
import re
import csv
import time
import ast
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SCRIPTS = BASE / "scripts"
COMPANIES_DIR = BASE / "companies"
EXPORTS_DIR = BASE / "exports"


def get_existing():
    """Get existing company slugs and names."""
    slugs = set(f.replace('.md', '') for f in os.listdir(COMPANIES_DIR) if f.endswith('.md'))
    names = set()
    csv_path = EXPORTS_DIR / "companies_clean.csv"
    if csv_path.exists():
        with open(csv_path) as f:
            for row in csv.DictReader(f):
                names.add(row['name'].lower().strip())
    return slugs, names


def browser_open(url):
    try:
        subprocess.run(['browser-use', 'open', url], capture_output=True, text=True, timeout=30)
        time.sleep(4)
        return True
    except:
        return False


def browser_eval(js):
    try:
        result = subprocess.run(['browser-use', 'eval', js], capture_output=True, text=True, timeout=30)
        output = result.stdout.strip()
        if output.startswith('result: '):
            output = output[8:]
        return output
    except:
        return "[]"


def browser_scroll():
    for _ in range(15):
        try:
            subprocess.run(['browser-use', 'scroll', '0', '3000'], capture_output=True, text=True, timeout=10)
            time.sleep(0.5)
        except:
            pass


def parse_list(raw):
    try:
        return ast.literal_eval(raw)
    except:
        try:
            return json.loads(raw)
        except:
            return []


def scrape_vc_portfolio(name, url, js_selector):
    """Generic VC portfolio scraper."""
    cache_path = SCRIPTS / f"{name}_companies.txt"
    if cache_path.exists() and os.path.getsize(cache_path) > 100:
        print(f"  {name}: using cache ({sum(1 for _ in open(cache_path))} companies)")
        return [l.strip() for l in open(cache_path) if l.strip()]

    print(f"  {name}: scraping {url}...")
    if not browser_open(url):
        print(f"  {name}: failed to open")
        return []

    browser_scroll()
    time.sleep(2)

    raw = browser_eval(js_selector)
    companies = parse_list(raw)

    # Deduplicate and clean
    companies = list(dict.fromkeys(c.strip() for c in companies if c and len(c.strip()) > 1 and len(c.strip()) < 80))

    with open(cache_path, 'w') as f:
        for c in companies:
            f.write(c + '\n')

    print(f"  {name}: found {len(companies)} companies")
    return companies


# VC configurations: (name, URL, JS selector to extract company names)
VCS = [
    ('a16z', 'https://a16z.com/portfolio/',
     "Array.from(document.querySelectorAll('button[aria-label]')).map(b=>b.getAttribute('aria-label')).filter(n=>n&&!['Close menu','Back','Clear search'].includes(n))"),

    ('sequoia', 'https://www.sequoiacap.com/our-companies/',
     "Array.from(document.querySelectorAll('a[class*=company], [class*=Company] span, [data-company]')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('lightspeed', 'https://lsvp.com/portfolio/',
     "Array.from(document.querySelectorAll('.portfolio-item h3, .portfolio-card h3, [class*=portfolio] a, [class*=company] a')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('index_ventures', 'https://www.indexventures.com/companies/',
     "Array.from(document.querySelectorAll('[class*=company] a, [class*=Company] a, h3 a, [data-name]')).map(el=>el.getAttribute('data-name')||el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('founders_fund', 'https://foundersfund.com/portfolio/',
     "Array.from(document.querySelectorAll('[class*=company] h3, [class*=portfolio] a, [class*=card] h3')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('khosla', 'https://www.khoslaventures.com/portfolio/',
     "Array.from(document.querySelectorAll('[class*=company] a, [class*=portfolio] h3, [class*=card] a')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('greylock', 'https://greylock.com/portfolio/',
     "Array.from(document.querySelectorAll('[class*=company] a, h3 a, [class*=portfolio] a')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('benchmark', 'https://www.benchmark.com/portfolio/',
     "Array.from(document.querySelectorAll('[class*=company], [class*=portfolio] a, h3')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('general_catalyst', 'https://www.generalcatalyst.com/portfolio',
     "Array.from(document.querySelectorAll('[class*=company] a, [class*=portfolio] h3, [class*=card] a')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),

    ('accel', 'https://www.accel.com/portfolio',
     "Array.from(document.querySelectorAll('[class*=company] a, [class*=portfolio] a, h3')).map(el=>el.textContent.trim()).filter(t=>t.length>1&&t.length<60)"),
]


def is_likely_ai(name):
    """Check if company name suggests AI/ML focus."""
    ai_words = [
        'ai', ' ai', 'ml', 'robot', 'deep', 'neural', 'auto', 'intel',
        'model', 'agent', 'cyber', 'gen ', 'llm', 'gpt', 'vision',
        'brain', 'cognitive', 'machine', 'learn', 'predict', 'autonomo',
    ]
    name_lower = name.lower()
    return any(w in name_lower or name_lower.endswith(w.strip()) for w in ai_words)


def main():
    existing_slugs, existing_names = get_existing()
    print(f"Existing database: {len(existing_slugs)} companies\n")

    # Phase 1: Scrape all VCs
    print("=" * 60)
    print("PHASE 1: Scraping VC portfolios")
    print("=" * 60)

    all_companies = {}  # company_name -> set of VCs
    for vc_name, url, js in VCS:
        companies = scrape_vc_portfolio(vc_name, url, js)
        for c in companies:
            if c not in all_companies:
                all_companies[c] = set()
            all_companies[c].add(vc_name)

    print(f"\nTotal unique companies across all VCs: {len(all_companies)}")

    # Phase 2: Find gaps
    print("\n" + "=" * 60)
    print("PHASE 2: Finding gaps")
    print("=" * 60)

    gaps = {}
    for name, vcs in all_companies.items():
        name_lower = name.lower().strip()
        slug = re.sub(r'[^a-z0-9\s-]', '', name_lower)
        slug = re.sub(r'[\s]+', '-', slug).strip('-')

        found = False
        for s in [slug, slug.replace('-ai', ''), slug.replace('-inc', ''),
                   slug.replace('-labs', ''), slug.replace('-io', '')]:
            if s in existing_slugs:
                found = True
                break
        if not found and name_lower not in existing_names:
            gaps[name] = vcs

    # Prioritize: companies backed by multiple VCs, or with AI in name
    ai_gaps = {k: v for k, v in gaps.items() if is_likely_ai(k)}
    multi_vc = {k: v for k, v in gaps.items() if len(v) >= 2}

    print(f"Total gaps: {len(gaps)}")
    print(f"Likely AI gaps: {len(ai_gaps)}")
    print(f"Multi-VC backed gaps: {len(multi_vc)}")

    # Save results
    output = {
        "total_gaps": len(gaps),
        "ai_gaps": len(ai_gaps),
        "multi_vc_gaps": len(multi_vc),
        "gaps": [
            {"name": name, "vcs": sorted(vcs), "likely_ai": is_likely_ai(name)}
            for name, vcs in sorted(gaps.items(), key=lambda x: (-len(x[1]), x[0]))
        ]
    }

    with open(SCRIPTS / "vc_gaps_full.json", 'w') as f:
        json.dump(output, f, indent=2)

    print("\n=== TOP GAPS (multi-VC or AI-named) ===")
    priority = sorted(
        [(k, v) for k, v in gaps.items() if is_likely_ai(k) or len(v) >= 2],
        key=lambda x: (-len(x[1]), x[0])
    )
    for name, vcs in priority[:80]:
        ai_tag = " [AI]" if is_likely_ai(name) else ""
        print(f"  {name:40s} ({', '.join(sorted(vcs))}){ai_tag}")

    print(f"\nResults saved to scripts/vc_gaps_full.json")
    print(f"Next step: research each gap company for AI relevance and 2024-2026 funding")


if __name__ == "__main__":
    main()
