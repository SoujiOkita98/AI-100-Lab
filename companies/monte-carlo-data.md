---
name: Monte Carlo
legal_name: Monte Carlo Data, Inc.
founded: 2019
headquarters: San Francisco, California, USA
website: https://www.montecarlodata.com
sector: Data Observability & AI Data Quality
stage: Late-stage / Growth
latest_valuation_usd: 1600000000
latest_valuation_date: 2022-05
total_funding_usd: ~236_000_000
revenue_run_rate_usd: ~82_000_000
revenue_run_rate_date: 2025
employee_count_approx: 559
employee_count_date: 2025
ipo_status: Private
founders:
- name: Barr Moses
  role: Co-Founder & CEO
  origin: Israeli
  education: Stanford University (MBA); Israeli Defense Forces intelligence unit
  prior: First Round Capital (mentor); Gainsight (VP of Customer Operations)
- name: Lior Gavish
  role: Co-Founder & CTO
  origin: Israeli
  education: Technion (inferred from Israeli tech ecosystem)
  prior: Yahoo (Engineering)
- name: Itay Bleier
  role: Co-Founder
  origin: Israeli
- name: Jordan Van Horn
  role: Co-Founder
  origin: American
funding_rounds:
- round: Series A
  date: 2020-09
  amount_usd: 16000000
  lead_investors:
  - Accel
  source: https://www.montecarlodata.com/blog-monte-carlo-raises-series-c-brings-funding-to-101m-to-help-companies-trust-their-data/
- round: Series B
  date: 2021-02
  amount_usd: 25000000
  lead_investors:
  - Redpoint Ventures
  source: https://techcrunch.com/2021/02/09/monte-carlo-raises-25m-for-its-data-observability-service/
- round: Series C
  date: 2021-08
  amount_usd: 60000000
  lead_investors:
  - ICONIQ Growth
  other_investors:
  - Salesforce Ventures
  - Accel
  - GGV Capital
  - Redpoint Ventures
  source: https://www.montecarlodata.com/blog-monte-carlo-raises-series-c-brings-funding-to-101m-to-help-companies-trust-their-data/
- round: Series D
  date: 2022-05
  amount_usd: 135000000
  valuation_usd: 1600000000
  lead_investors:
  - IVP
  other_investors:
  - Accel
  - GGV Capital
  - Redpoint Ventures
  - ICONIQ Growth
  - Salesforce Ventures
  - GIC
  source: https://techcrunch.com/2022/05/24/monte-carlo-raises-135m-series-d-at-1-6b-price-showing-that-unicorn-rounds-are-still-a-thing/
one_liner: Monte Carlo is the pioneer and market leader in data observability -- a category the company essentially created
website_verified: true
---

# Monte Carlo

## Overview

Monte Carlo is the pioneer and market leader in data observability -- a category the company essentially created. The platform uses machine learning to automatically monitor and alert on data quality issues across an organization's entire data stack, functioning as an "immune system" for enterprise data. Monte Carlo detects data freshness, volume, schema, distribution, and lineage anomalies without requiring users to manually define rules or thresholds.

Founded in 2019 by a team of Israeli-American entrepreneurs, Monte Carlo raised $236 million and achieved a $1.6 billion unicorn valuation in just three years. The company became the first data observability unicorn, a milestone reached in May 2022.

Sources: [TechCrunch](https://techcrunch.com/2022/05/24/monte-carlo-raises-135m-series-d-at-1-6b-price-showing-that-unicorn-rounds-are-still-a-thing/); [Monte Carlo blog](https://www.montecarlodata.com/blog-monte-carlo-raises-135m-series-d-to-accelerate-the-rapid-growth-of-the-data-observability-category/)

## Founding Story & Team

Monte Carlo was co-founded in 2019 by **Barr Moses** (CEO), **Lior Gavish** (CTO), **Itay Bleier**, and **Jordan Van Horn**.

Barr Moses, an Israeli-born executive, served in an intelligence unit of the Israeli Defense Forces before attending Stanford for her MBA. She worked at Gainsight as VP of Customer Operations and served as a mentor at First Round Capital before co-founding Monte Carlo. Lior Gavish, also Israeli, came from engineering roles at Yahoo.

The founding insight came from Moses's experience in operational roles: she observed that data teams spent enormous amounts of time firefighting data quality issues -- broken pipelines, missing data, schema changes, stale tables -- yet had no systematic way to detect these problems before they impacted downstream dashboards and ML models. She coined the term "data downtime" (analogous to application downtime in DevOps) and built Monte Carlo to eliminate it.

The analogy to application observability (New Relic, Datadog for software systems) was deliberate: just as DevOps teams needed monitoring and alerting for application uptime, data teams needed the same for data reliability.

## Business Model

Monte Carlo operates a **SaaS subscription model** with pricing based on the volume of data assets monitored. The platform integrates natively with cloud data warehouses, data lakes, ETL tools, and BI platforms.

### Core Products & Capabilities

- **Automated Anomaly Detection**: ML-based monitoring of data freshness, volume, schema changes, and distribution drift -- no manual rule configuration required
- **Data Lineage**: End-to-end lineage mapping from data sources through transformations to BI dashboards, enabling root cause analysis
- **Data Incident Management**: Alerting, triage, and resolution workflows for data quality incidents (integrated with Slack, PagerDuty, etc.)
- **Circuit Breakers**: Automated pipeline halts when data quality falls below defined thresholds, preventing bad data from reaching production
- **Domain-Specific Monitors**: Custom monitors for business-specific data quality rules
- **Data Observability for AI**: Monitoring data quality for ML training pipelines and AI applications

### Key Customers

Monte Carlo serves companies including JetBlue, PagerDuty, Vimeo, BigCommerce, Fox, Toast, and numerous Fortune 500 data teams.

## What Makes Monte Carlo Notable

1. **Category creator**: Monte Carlo essentially defined "data observability" as a product category, analogous to how Datadog defined application observability. CEO Barr Moses has been prolific in evangelizing the concept through writing, speaking, and thought leadership.

2. **Fastest unicorn in the data stack**: Reaching $1.6B valuation in ~3 years from founding is an exceptionally fast trajectory, particularly in infrastructure software.

3. **ML-first approach**: Unlike traditional data quality tools that require manual rule configuration, Monte Carlo uses unsupervised ML to automatically learn normal patterns in data and detect anomalies. This dramatically reduces setup time and catches issues that rule-based systems miss.

4. **Platform-agnostic positioning**: Monte Carlo integrates with the entire modern data stack -- Snowflake, Databricks, BigQuery, Redshift, dbt, Fivetran, Airflow, Looker, Tableau, and many others -- positioning itself as the observability layer across heterogeneous environments.

5. **Israeli founder pipeline**: The founding team represents the strong Israeli tech ecosystem's contribution to enterprise data infrastructure, with a direct lineage from IDF intelligence and Israeli tech companies.

## Competitive Landscape

- **Anomalo**: AI-powered data quality platform; more focused on automated validation than full observability
- **Soda**: Open-source-first data quality and observability
- **Great Expectations**: Open-source data validation framework
- **Bigeye**: Data observability with focus on data pipeline monitoring
- **Ataccama**: Enterprise data quality and governance (legacy vendor adding AI)
- **Datadog**: Application observability leader with some data pipeline monitoring capabilities

## Outlook

Data observability is becoming table stakes for enterprise data teams, particularly as AI applications increase the criticality of data quality. Gartner estimates that by 2026, 50% of enterprises with distributed data architectures will adopt data observability tools, up from less than 20% in 2024. Monte Carlo is well-positioned as the category leader, though it faces growing competition from both startups and incumbents adding observability features.

---

*Profile compiled March 2026. Figures marked with ~ are approximate. Founder backgrounds marked "inferred" are based on public information and career patterns.*
