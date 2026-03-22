#!/usr/bin/env python3
"""
Systematic VC portfolio scraper using browser-use CLI.
Scrapes top VC portfolio pages, identifies AI companies, cross-references
against existing database, and outputs gaps.
"""

import subprocess
import json
import os
import re
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SCRIPTS = BASE / "scripts"
COMPANIES_DIR = BASE / "companies"


def get_existing_companies():
    """Get set of company names and slugs already in database."""
    existing_slugs = set(f.replace('.md', '') for f in os.listdir(COMPANIES_DIR) if f.endswith('.md'))

    # Also load names from CSV for fuzzy matching
    import csv
    existing_names = set()
    csv_path = BASE / "exports" / "companies_clean.csv"
    if csv_path.exists():
        with open(csv_path) as f:
            for row in csv.DictReader(f):
                existing_names.add(row['name'].lower().strip())

    return existing_slugs, existing_names


def browser_open(url):
    """Open URL in browser-use."""
    result = subprocess.run(['browser-use', 'open', url], capture_output=True, text=True, timeout=30)
    time.sleep(3)  # Wait for page load
    return result.returncode == 0


def browser_eval(js):
    """Execute JS and return result."""
    result = subprocess.run(['browser-use', 'eval', js], capture_output=True, text=True, timeout=30)
    output = result.stdout.strip()
    if output.startswith('result: '):
        output = output[8:]
    return output


def browser_scroll_to_bottom():
    """Scroll to bottom to load all content."""
    for _ in range(10):
        subprocess.run(['browser-use', 'scroll', '0', '5000'], capture_output=True, text=True, timeout=10)
        time.sleep(1)


def extract_company_list(js_code):
    """Extract list of company names from JS evaluation."""
    import ast
    raw = browser_eval(js_code)
    try:
        return ast.literal_eval(raw)
    except:
        # Try JSON
        try:
            return json.loads(raw)
        except:
            return []


def scrape_a16z():
    """Scrape a16z portfolio."""
    print("Scraping a16z portfolio...")
    # Already have this from earlier
    path = SCRIPTS / "a16z_companies.txt"
    if path.exists():
        return [line.strip() for line in open(path) if line.strip()]

    browser_open("https://a16z.com/portfolio/")
    time.sleep(3)
    companies = extract_company_list(
        "Array.from(document.querySelectorAll('button[aria-label]')).map(b => b.getAttribute('aria-label')).filter(n => n && !['Close menu','Back','Clear search'].includes(n))"
    )
    with open(path, 'w') as f:
        for c in companies:
            f.write(c + '\n')
    return companies


def scrape_sequoia():
    """Scrape Sequoia Capital portfolio."""
    print("Scraping Sequoia portfolio...")
    browser_open("https://www.sequoiacap.com/our-companies/")
    time.sleep(5)
    browser_scroll_to_bottom()
    companies = extract_company_list(
        "Array.from(document.querySelectorAll('[class*=company] a, [class*=portfolio] a, h3, h4')).map(el => el.textContent.trim()).filter(t => t.length > 1 && t.length < 50)"
    )
    return companies


def scrape_lightspeed():
    """Scrape Lightspeed Venture Partners portfolio."""
    print("Scraping Lightspeed portfolio...")
    browser_open("https://lsvp.com/portfolio/")
    time.sleep(5)
    browser_scroll_to_bottom()
    companies = extract_company_list(
        "Array.from(document.querySelectorAll('[class*=portfolio] a, [class*=company] h2, [class*=company] h3, [class*=card] h3')).map(el => el.textContent.trim()).filter(t => t.length > 1 && t.length < 50)"
    )
    return companies


def scrape_index_ventures():
    """Scrape Index Ventures portfolio."""
    print("Scraping Index Ventures portfolio...")
    browser_open("https://www.indexventures.com/companies/")
    time.sleep(5)
    browser_scroll_to_bottom()
    companies = extract_company_list(
        "Array.from(document.querySelectorAll('[class*=company] a, [class*=portfolio] a, h3 a')).map(el => el.textContent.trim()).filter(t => t.length > 1 && t.length < 50)"
    )
    return companies


def scrape_founders_fund():
    """Scrape Founders Fund portfolio."""
    print("Scraping Founders Fund portfolio...")
    browser_open("https://foundersfund.com/portfolio/")
    time.sleep(5)
    browser_scroll_to_bottom()
    companies = extract_company_list(
        "Array.from(document.querySelectorAll('a[href*=portfolio], [class*=company], [class*=portfolio] h3')).map(el => el.textContent.trim()).filter(t => t.length > 1 && t.length < 50)"
    )
    return companies


def scrape_yc():
    """Scrape Y Combinator companies directory for AI companies."""
    print("Scraping YC directory for AI companies...")
    browser_open("https://www.ycombinator.com/companies?tags=Artificial%20Intelligence&batch=W25&batch=S25&batch=W24&batch=S24")
    time.sleep(5)
    browser_scroll_to_bottom()
    companies = extract_company_list(
        "Array.from(document.querySelectorAll('[class*=company] a, [class*=CompanyName], h4 a')).map(el => el.textContent.trim()).filter(t => t.length > 1 && t.length < 80)"
    )
    return companies


VC_SCRAPERS = {
    'a16z': scrape_a16z,
    'sequoia': scrape_sequoia,
    'lightspeed': scrape_lightspeed,
    'index': scrape_index_ventures,
    'founders_fund': scrape_founders_fund,
    'yc': scrape_yc,
}


def main():
    existing_slugs, existing_names = get_existing_companies()
    print(f"Existing database: {len(existing_slugs)} companies")

    all_vc_companies = {}

    for vc_name, scraper_fn in VC_SCRAPERS.items():
        try:
            companies = scraper_fn()
            all_vc_companies[vc_name] = companies
            print(f"  {vc_name}: {len(companies)} companies found")

            # Save raw list
            with open(SCRIPTS / f"{vc_name}_companies.txt", 'w') as f:
                for c in companies:
                    f.write(c + '\n')
        except Exception as e:
            print(f"  {vc_name}: ERROR - {e}")
            all_vc_companies[vc_name] = []

    # Find companies NOT in our database
    gaps = {}
    for vc_name, companies in all_vc_companies.items():
        for company in companies:
            name_lower = company.lower().strip()
            slug_guess = re.sub(r'[^a-z0-9\s-]', '', name_lower)
            slug_guess = re.sub(r'[\s]+', '-', slug_guess).strip('-')

            if name_lower not in existing_names and slug_guess not in existing_slugs:
                if company not in gaps:
                    gaps[company] = []
                gaps[company].append(vc_name)

    # Output gaps
    print(f"\n{'='*60}")
    print(f"GAPS: {len(gaps)} companies found in VC portfolios but NOT in our database")
    print(f"{'='*60}\n")

    # Sort by number of VCs backing them (more VCs = more notable)
    sorted_gaps = sorted(gaps.items(), key=lambda x: -len(x[1]))

    with open(SCRIPTS / "vc_gaps.json", 'w') as f:
        json.dump([{"name": name, "vcs": vcs} for name, vcs in sorted_gaps], f, indent=2)

    for name, vcs in sorted_gaps[:100]:
        vc_str = ", ".join(vcs)
        print(f"  {name:40s} [{vc_str}]")

    print(f"\nFull gap list saved to scripts/vc_gaps.json")


if __name__ == "__main__":
    main()
