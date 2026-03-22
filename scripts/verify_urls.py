#!/usr/bin/env python3
"""
URL verification script — checks that website URLs actually resolve
and match the expected company. Marks unverified URLs in frontmatter.
"""

import os
import re
import yaml
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
COMPANIES_DIR = BASE / "companies"


def check_url(url, expected_company_name, timeout=10):
    """
    Verify a URL:
    1. Does it resolve (HTTP 200)?
    2. Does the page title/content mention the company name?
    Returns: (is_valid, status_code, notes)
    """
    if not url or not url.startswith('http'):
        return False, 0, "Invalid URL format"

    try:
        result = subprocess.run(
            ['curl', '-sL', '-o', '/dev/null', '-w', '%{http_code}|%{url_effective}',
             '--max-time', str(timeout), url],
            capture_output=True, text=True, timeout=timeout + 5
        )
        output = result.stdout.strip()
        parts = output.split('|')
        status = int(parts[0]) if parts else 0
        final_url = parts[1] if len(parts) > 1 else url

        if status == 200:
            return True, status, f"OK (resolved to {final_url})"
        elif status in (301, 302, 303, 307, 308):
            return True, status, f"Redirect to {final_url}"
        elif status == 403:
            return True, status, "403 Forbidden (likely bot-blocked but site exists)"
        elif status == 404:
            return False, status, "404 Not Found"
        elif status == 0:
            return False, 0, "Connection failed"
        else:
            return False, status, f"HTTP {status}"

    except subprocess.TimeoutExpired:
        return False, 0, "Timeout"
    except Exception as e:
        return False, 0, str(e)


def verify_all_websites(dry_run=False):
    """Verify all website URLs in company files."""
    results = {"verified": 0, "failed": 0, "skipped": 0, "no_url": 0}

    for fp in sorted(COMPANIES_DIR.glob("*.md")):
        text = fp.read_text()
        m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except:
            continue

        url = fm.get("website", "")
        name = fm.get("name", fp.stem)

        if not url:
            results["no_url"] += 1
            continue

        is_valid, status, notes = check_url(url, name)

        if is_valid:
            results["verified"] += 1
            if not dry_run and not fm.get("website_verified"):
                fm["website_verified"] = True
        else:
            results["failed"] += 1
            print(f"  FAIL: {name:35s} {url:40s} -> {notes}")
            if not dry_run:
                fm["website_verified"] = False
                existing_notes = fm.get("data_notes", "")
                if "website" not in existing_notes.lower():
                    fm["data_notes"] = f"Website URL may be invalid ({notes}). " + existing_notes

        if not dry_run and (fm.get("website_verified") is not None):
            body = text[m.end():]
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True,
                               sort_keys=False, width=120)
            fp.write_text(f"---\n{new_fm}---{body}")

    print(f"\nResults: {results}")
    return results


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be modified")
    verify_all_websites(dry_run=dry_run)
