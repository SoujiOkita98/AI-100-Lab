---
name: Anomalo
founded: 2018
headquarters: San Francisco, California, USA
website: https://www.anomalo.com
one_liner: AI-powered data quality platform that automatically detects, explains, and resolves data issues across enterprise
  data warehouses and lakehouses
sector: AI Data Quality & Observability
stage: Growth
latest_valuation_usd: null
latest_valuation_date: null
employee_count_approx: 100
employee_count_date: 2025
ipo_status: Private
founders:
- name: Elliot Shmukler
  role: Co-Founder & CEO
  origin: American (Russian-Jewish heritage)
  prior: Instacart (VP of Product & Growth); LinkedIn (Head of Growth); Wealthfront
- name: Jeremy Stanley
  role: Co-Founder & CTO
  background: PhD (inferred from technical background)
  origin: American
  prior: Instacart (VP of Data Science)
funding_rounds:
- stage: Seed
  date: 2021
  lead_investors:
  - Foundation Capital
  other_investors:
  - Two Sigma Ventures
  source: https://www.anomalo.com/blog/anomalo-raises-a-33-million-series-a-led-by-norwest-venture-partners/
- stage: Series A
  date: 2022
  amount_m: 33.0
  lead_investors:
  - Norwest Venture Partners
  other_investors:
  - Foundation Capital
  - Two Sigma Ventures
  source: https://www.anomalo.com/blog/anomalo-raises-a-33-million-series-a-led-by-norwest-venture-partners/
- stage: Series B
  date: 2024-01
  amount_m: 33.0
  lead_investors:
  - SignalFire
  other_investors:
  - Databricks Ventures
  - Norwest Venture Partners
  - Two Sigma Ventures
  - Foundation Capital
  source: https://www.globenewswire.com/news-release/2024/01/24/2815554/0/en/Anomalo-Reports-Record-Demand-for-Its-Data-Quality-Platform-as-It-Raises-a-33-Million-Growth-Round-With-Participation-From-Strategic-Investor-Databricks-Ventures.html
strategic_investors:
- Databricks Ventures
- Snowflake Ventures
website_verified: true
crunchbase: https://www.crunchbase.com/organization/anomalo
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/anomalo
twitter: '@anomalo_hq'
linkedin_verified: true
total_raised_m: 72.0
status: active
confidence: high
last_updated: '2026-03-24'
---

# Anomalo

## Overview

Anomalo is an AI-powered data quality platform that uses machine learning to automatically detect anomalies, data quality issues, and data pipeline failures across enterprise data warehouses -- without requiring users to write manual validation rules. The platform learns normal data patterns through unsupervised ML and alerts data teams when something deviates from expectations, covering freshness, volume, distribution, schema, and content-level quality.

Founded in 2018 by two former Instacart executives, Anomalo has raised approximately $72 million and is backed by both Databricks Ventures and Snowflake Ventures as strategic investors -- a notable dual endorsement from the two dominant cloud data warehouse platforms.

Sources: [Anomalo blog](https://www.anomalo.com/blog/anomalos-series-b-and-the-future-of-enterprise-data-quality/); [GlobeNewswire](https://www.globenewswire.com/news-release/2024/01/24/2815554/0/en/Anomalo-Reports-Record-Demand-for-Its-Data-Quality-Platform-as-It-Raises-a-33-Million-Growth-Round-With-Participation-From-Strategic-Investor-Databricks-Ventures.html)

## Founding Story & Team

Anomalo was co-founded by **Elliot Shmukler** (CEO) and **Jeremy Stanley** (CTO), who worked closely together at **Instacart** during its high-growth phase. Shmukler was VP of Product & Growth at Instacart (and previously Head of Growth at LinkedIn and a leader at Wealthfront), while Stanley was VP of Data Science.

At Instacart, they experienced a pivotal incident: a geographic expansion strategy ground to a halt because the underlying data was six months stale -- and nobody knew until the strategy had already been executed on bad data. They realized that the difficulty of ensuring data quality at scale was a universal enterprise problem, not just an Instacart problem.

The key insight was that manual data quality rules (the approach used by legacy tools like Great Expectations) did not scale: enterprises had thousands of tables and millions of columns, and writing rules for each was impractical. Anomalo was built on the premise that ML should learn what "normal" looks like for each dataset and automatically flag deviations -- the same approach that anomaly detection uses in cybersecurity and application monitoring.

## Business Model

Anomalo operates a **SaaS subscription model** with pricing based on the number of data tables monitored. The platform is designed as a no-code solution -- data teams connect it to their data warehouse and Anomalo automatically begins learning data patterns and detecting issues.

### Core Products & Capabilities

- **Automated Anomaly Detection**: Unsupervised ML that learns seasonality, trends, and normal distributions for every table and column; detects freshness, volume, schema, distribution, and row-level anomalies
- **Unstructured Data Monitoring**: Launched in 2025 to monitor quality of unstructured data (text files, images) flowing through data pipelines -- critical for AI/ML applications
- **Data Validation**: Customizable validation checks for business-specific rules layered on top of ML-based detection
- **Root Cause Analysis**: Automated drill-down into anomalies to identify which columns, segments, or upstream sources caused the issue
- **Alerting & Integration**: Native integrations with Slack, PagerDuty, email; embeds into existing data team workflows
- **Data Documentation**: Automated documentation of data assets based on observed patterns and metadata

### Key Customers

Anomalo serves enterprises including Discover Financial Services, CollegeBoard, Block (Square), and numerous data-intensive organizations.

### Growth Metrics

- ARR grew 177% year-over-year in fiscal Q3 2023
- ARR grew more than 15x since Series A (2021-2024)

## What Makes Anomalo Notable

1. **Dual strategic backing from Databricks and Snowflake**: Being backed by both Databricks Ventures and Snowflake Ventures is rare and strategically significant -- it signals that both dominant cloud data warehouse platforms see data quality as a critical adjacent need and view Anomalo as a trusted partner rather than a future competitor.

2. **ML-first, no-code approach**: Anomalo's unsupervised ML approach means data teams can monitor thousands of tables without writing a single rule. This is a fundamentally different paradigm from rule-based data quality tools and scales dramatically better.

3. **Instacart growth DNA**: Both founders bring deep experience in data-intensive, high-growth consumer technology. Shmukler's growth leadership at LinkedIn and Instacart informs Anomalo's product-led growth strategy, while Stanley's data science background ensures the ML core is sophisticated.

4. **Unstructured data expansion (2025)**: Anomalo's extension to unstructured data monitoring positions it uniquely at the intersection of data quality and AI -- as enterprises feed documents, images, and text into LLMs, ensuring the quality of that unstructured input becomes critical.

5. **Rapid revenue growth**: 177% YoY ARR growth and 15x ARR expansion since Series A indicate strong product-market fit in an increasingly critical category.

## Competitive Landscape

- **Monte Carlo**: Primary competitor; focuses on broader "data observability" (monitoring, lineage, incident management) vs. Anomalo's focused data quality approach
- **Great Expectations**: Open-source data validation framework; rule-based, not ML-driven
- **Soda**: Data quality platform with open-source roots
- **Bigeye**: Data observability with automated monitoring
- **Elementary**: Open-source dbt-native data observability
- **Metaplane**: Data observability for modern data stacks

## Outlook

Anomalo is in a strong position in the rapidly growing data quality market. The dual backing from Databricks and Snowflake provides distribution advantages that few competitors can match. The expansion into unstructured data monitoring for AI use cases opens a large new market as enterprises accelerate LLM deployments. Given the 15x ARR growth since Series A, the company is likely approaching a significant growth round.

---

*Profile compiled March 2026. Figures marked with ~ are approximate.*
