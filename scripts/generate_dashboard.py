#!/usr/bin/env python3
"""
Generate docs/index.html dashboard from live dataset.
Reads exports/companies.csv, founders.csv, rounds.csv
and produces a self-contained static HTML page with current stats.
"""

import csv
import json
from collections import Counter
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent.parent
EXPORTS = BASE / "exports"
DOCS = BASE / "docs"


def load_csv(name):
    with open(EXPORTS / name) as f:
        return list(csv.DictReader(f))


def safe_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0


def main():
    companies = load_csv("companies.csv")
    founders = load_csv("founders.csv")
    rounds = load_csv("rounds.csv")

    n_companies = len(companies)
    n_founders = len(founders)
    n_rounds = len(rounds)

    # Total capital
    total_capital = sum(safe_float(c.get("total_raised_m", 0)) for c in companies)
    if total_capital > 1000:
        capital_str = f"${total_capital/1000:.0f}B+"
    else:
        capital_str = f"${total_capital:.0f}M"

    # Median raised
    raised_vals = sorted([safe_float(c["total_raised_m"]) for c in companies if safe_float(c.get("total_raised_m", 0)) > 0])
    median_raised = raised_vals[len(raised_vals) // 2] if raised_vals else 0
    median_str = f"${median_raised:.0f}M"

    # Countries
    hq_countries = set()
    for c in companies:
        hq = c.get("hq", "")
        parts = [p.strip() for p in hq.split(",")]
        if len(parts) >= 2:
            hq_countries.add(parts[-1])
    n_countries = len(hq_countries)

    # Geographic distribution
    geo = Counter()
    for c in companies:
        hq = c.get("hq", "").strip()
        if ", CA" in hq:
            geo["California"] += 1
        elif ", NY" in hq or "New York" in hq:
            geo["New York"] += 1
        elif any(x in hq for x in ["China", "Beijing", "Shanghai", "Shenzhen", "Hong Kong"]):
            geo["China / HK"] += 1
        elif any(x in hq for x in ["United Kingdom", "London", "Oxford", ", UK"]):
            geo["UK"] += 1
        elif any(x in hq for x in ["Israel", "Tel Aviv"]):
            geo["Israel"] += 1
        elif any(x in hq for x in ["Germany", "Berlin", "Munich"]):
            geo["Germany"] += 1
        elif any(x in hq for x in ["France", "Paris"]):
            geo["France"] += 1
        elif any(x in hq for x in ["Canada", "Toronto", "Montreal"]):
            geo["Canada"] += 1
        elif any(x in hq for x in [", TX", ", MA", ", WA", ", IL", ", CO", ", VA", ", PA",
                                     "Boston", "Seattle", "Austin", "Chicago", "Pittsburgh"]):
            geo["Other US"] += 1
        else:
            geo["Other"] += 1

    # Founder origins
    origin_counts = Counter()
    for f in founders:
        o = f.get("origin", "").strip()
        if o:
            origin_counts[o] += 1

    top_origins = origin_counts.most_common(12)

    # Founded year distribution
    year_counts = Counter()
    for c in companies:
        y = c.get("founded_year", "").strip()
        if y and y.isdigit():
            year_counts[int(y)] += 1

    # Top geo for bars
    top_geo = geo.most_common(10)
    geo_max = max(v for _, v in top_geo) if top_geo else 1

    # Origin max
    origin_max = max(v for _, v in top_origins) if top_origins else 1

    # Year histogram
    years = sorted(year_counts.keys())
    if years:
        year_range = range(max(min(years), 2013), max(years) + 1)
    else:
        year_range = range(2013, 2026)
    year_max = max(year_counts.values()) if year_counts else 1

    today = date.today().strftime("%B %d, %Y")

    # Build HTML
    geo_bars = ""
    for label, count in top_geo:
        pct = count / geo_max * 100
        geo_bars += f'    <div class="bar-row"><div class="bar-label">{label}</div><div class="bar-track"><div class="bar-fill" style="width:{pct:.0f}%; background:var(--accent);"></div></div><div style="font-size:11px;width:35px;text-align:right;">{count}</div></div>\n'

    origin_bars = ""
    for label, count in top_origins:
        pct = count / origin_max * 100
        origin_bars += f'    <div class="bar-row"><div class="bar-label">{label}</div><div class="bar-track"><div class="bar-fill" style="width:{pct:.0f}%; background:var(--green);"></div></div><div style="font-size:11px;width:35px;text-align:right;">{count}</div></div>\n'

    year_bars = ""
    for y in year_range:
        cnt = year_counts.get(y, 0)
        pct = cnt / year_max * 100
        color = "var(--accent)" if y >= 2023 else "var(--ink)"
        year_bars += f'    <div class="hist-bar-wrap"><div class="hist-bar" style="height:{pct:.0f}%; background:{color};"></div><div class="hist-label">\'{y % 100:02d}</div></div>\n'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI-100-Lab — Research Dashboard</title>
<style>
  :root {{ --ink: #1a1a1a; --muted: #666; --faint: #999; --rule: #ddd; --bg: #fff; --bg-alt: #f7f7f5; --accent: #1a5faa; --green: #137333; --amber: #b06000; --red: #c0392b; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; color: var(--ink); background: var(--bg); line-height: 1.55; max-width: 1080px; margin: 0 auto; padding: 48px 32px; }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .masthead {{ border-bottom: 2px solid var(--ink); padding-bottom: 20px; margin-bottom: 32px; }}
  .masthead h1 {{ font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }}
  .masthead .subtitle {{ font-size: 14px; color: var(--muted); margin-top: 6px; }}
  .masthead .meta {{ font-size: 12px; color: var(--faint); margin-top: 8px; display: flex; gap: 20px; flex-wrap: wrap; }}
  h2 {{ font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: var(--faint); margin: 40px 0 16px; padding-bottom: 8px; border-bottom: 1px solid var(--rule); }}
  .kpi-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 1px; background: var(--rule); border: 1px solid var(--rule); border-radius: 6px; overflow: hidden; margin-bottom: 32px; }}
  .kpi {{ background: var(--bg); padding: 16px; text-align: center; }}
  .kpi .num {{ font-size: 26px; font-weight: 700; color: var(--ink); font-variant-numeric: tabular-nums; }}
  .kpi .unit {{ font-size: 12px; color: var(--muted); margin-top: 2px; }}
  .row {{ display: grid; gap: 24px; margin-bottom: 24px; }}
  .row-2 {{ grid-template-columns: 1fr 1fr; }}
  .chart-container {{ border: 1px solid var(--rule); border-radius: 6px; padding: 16px; background: var(--bg); }}
  .chart-title {{ font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: var(--faint); margin-bottom: 12px; }}
  .bar-chart {{ display: flex; flex-direction: column; gap: 6px; }}
  .bar-row {{ display: flex; align-items: center; gap: 8px; font-size: 12px; }}
  .bar-label {{ width: 120px; text-align: right; color: var(--muted); font-size: 11px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex-shrink: 0; }}
  .bar-track {{ flex: 1; height: 16px; background: var(--bg-alt); border-radius: 2px; overflow: hidden; }}
  .bar-fill {{ height: 100%; border-radius: 2px; }}
  .histogram {{ display: flex; align-items: flex-end; gap: 2px; height: 120px; padding-top: 8px; }}
  .hist-bar-wrap {{ flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px; height: 100%; justify-content: flex-end; }}
  .hist-bar {{ width: 100%; border-radius: 2px 2px 0 0; min-height: 2px; }}
  .hist-label {{ font-size: 8px; color: var(--faint); transform: rotate(-45deg); white-space: nowrap; margin-top: 4px; }}
  .footer {{ margin-top: 48px; padding-top: 16px; border-top: 1px solid var(--rule); font-size: 11px; color: var(--faint); display: flex; justify-content: space-between; }}
  @media (max-width: 768px) {{ .kpi-grid {{ grid-template-columns: repeat(3, 1fr); }} .row-2 {{ grid-template-columns: 1fr; }} .bar-label {{ width: 80px; }} }}
</style>
</head>
<body>

<div class="masthead">
  <h1>AI-100-Lab</h1>
  <div class="subtitle">A research-grade database of {n_companies:,} AI and robotics startups worldwide &mdash; funding rounds, founder profiles, investor networks, and origin analysis.</div>
  <div class="meta">
    <span>Auto-generated from live data &middot; {today}</span>
    <span>{n_countries}+ countries covered</span>
    <span>License: CC BY 4.0</span>
    <span><a href="https://github.com/SoujiOkita98/AI-100-Lab">Source repository</a></span>
  </div>
</div>

<div class="kpi-grid">
  <div class="kpi"><div class="num">{n_companies:,}</div><div class="unit">Companies</div></div>
  <div class="kpi"><div class="num">{n_founders:,}</div><div class="unit">Founders</div></div>
  <div class="kpi"><div class="num">{n_rounds:,}</div><div class="unit">Funding rounds</div></div>
  <div class="kpi"><div class="num">{capital_str}</div><div class="unit">Total capital (USD)</div></div>
  <div class="kpi"><div class="num">{median_str}</div><div class="unit">Median raised</div></div>
  <div class="kpi"><div class="num">{n_countries}+</div><div class="unit">Countries</div></div>
</div>

<h2>Company Formation by Year</h2>
<div class="chart-container">
  <div class="chart-title">Number of AI/robotics companies founded per year (n = {n_companies:,})</div>
  <div class="histogram">
{year_bars}  </div>
</div>

<h2>Geographic Distribution</h2>
<div class="row row-2">
  <div class="chart-container">
    <div class="chart-title">Companies by HQ region</div>
    <div class="bar-chart">
{geo_bars}    </div>
  </div>
  <div class="chart-container">
    <div class="chart-title">Top founder origins</div>
    <div class="bar-chart">
{origin_bars}    </div>
  </div>
</div>

<div class="footer">
  <span>AI-100-Lab &middot; <a href="https://github.com/SoujiOkita98/AI-100-Lab">github.com/SoujiOkita98/AI-100-Lab</a></span>
  <span>Built with <a href="https://claude.ai/claude-code">Claude Code</a> &middot; Maintained by Gavin Zhu</span>
</div>

</body>
</html>"""

    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.html").write_text(html)
    print(f"Dashboard generated: {n_companies} companies, {n_founders} founders, {n_rounds} rounds")


if __name__ == "__main__":
    main()
