---
company: Cleanlab
founded: 2021
headquarters: San Francisco, CA
ceo: Curtis Northcutt (now Director, AI Research at Handshake)
co_founders:
- Curtis Northcutt (CEO) — MIT PhD, Machine Learning
- Jonas Mueller (Chief Scientist) — MIT PhD, Machine Learning
- Anish Athalye (CTO) — MIT PhD, Systems
sector: Data-Centric AI / Data Quality / AI Reliability
total_funding: ~$30M
status: Acquired by Handshake (January 2026)
founders:
- name: Curtis Northcutt
  role: Co-Founder & CEO (now Director AI Research at Handshake)
  background: MIT PhD in Machine Learning.
  origin: American (inferred from name)
- name: Jonas Mueller
  role: Co-Founder & Chief Scientist
  background: MIT PhD in Machine Learning.
  origin: German-American (inferred from name)
- name: Anish Athalye
  role: Co-Founder & CTO
  background: MIT PhD in Systems.
  origin: Indian-American (inferred from name)
profile_updated: 2026-03-20
one_liner: Cleanlab is a data-centric AI company that pioneered automated data quality tools for machine learning
data_notes: 'Needs verification: website, founders. Profile may be incomplete.'
website: https://cleanlab.ai
website_verified: true
linkedin: https://www.linkedin.com/company/cleanlab
crunchbase: https://www.crunchbase.com/organization/cleanlab
crunchbase_verified: true
total_raised_m: 30
funding_rounds:
- stage: Seed
  date: '2022'
  amount_m: 5.0
  lead_investors:
  - Bain Capital Ventures
  source: https://www.crunchbase.com/organization/cleanlab
- stage: Series A
  date: 2023-10
  amount_m: 25.0
  lead_investors:
  - Menlo Ventures
  source: https://www.crunchbase.com/organization/cleanlab
name: Cleanlab
linkedin_verified: true
---

# Cleanlab

## Overview

Cleanlab is a data-centric AI company that pioneered automated data quality tools for machine learning. Spun out of MIT research on **confident learning** — a theoretical framework for identifying and correcting label errors in datasets — Cleanlab built both an influential open-source library and a commercial platform (Cleanlab Studio) used by enterprises to detect and fix issues in training data, reduce LLM hallucinations, and improve AI reliability. In January 2026, Cleanlab was acquired by Handshake, the AI data-labeling company, in a talent-focused deal.

## Origins and Founding Story

Cleanlab's intellectual roots trace to **Curtis Northcutt's PhD research at MIT**, where he developed **confident learning** — a principled, theoretically grounded framework for estimating label noise and identifying mislabeled examples in datasets. The foundational paper, *Confident Learning: Estimating Uncertainty in Dataset Labels* (published in the Journal of Artificial Intelligence Research), won the **IJCAI-JAIR 5-Year Test-of-Time Award** and demonstrated that even canonical datasets like ImageNet contain over 100,000 label errors.

The open-source `cleanlab` Python package was released first as a research tool and gained significant traction, accumulating **9,000+ GitHub stars** and over **1 million downloads**. In **2021**, Northcutt co-founded the company with fellow MIT PhDs **Jonas Mueller** and **Anish Athalye** to commercialize these data quality techniques for enterprise use.

## Founders and Key People

| Name | Role | Background |
|------|------|------------|
| **Curtis Northcutt** | Co-Founder & CEO | PhD in CS (Machine Learning), MIT. Invented confident learning. 1,500+ citations. Previously contributed to improving Alexa, Siri, and Google Assistant. Now Director of AI Research & Strategy at Handshake. |
| **Jonas Mueller** | Co-Founder & Chief Scientist | PhD in CS (Machine Learning), MIT. 4,000+ citations. Built Amazon Web Services' AutoML service (AutoGluon), used by thousands of companies. |
| **Anish Athalye** | Co-Founder & CTO | PhD in CS (Systems), MIT. 7,000+ citations. 30,000+ GitHub stars across projects. ICML Best Paper Award winner. |

All three founders are MIT PhDs, and the broader team included researchers and engineers with backgrounds from frontier AI labs. The combined founders have earned over **20,000 citations** and contributed to products at Amazon, Apple, Google, and Meta prior to Cleanlab.

## Technology and Products

### Core Technology: Confident Learning

Cleanlab's algorithms use model predictions and out-of-sample predicted probabilities to estimate a **confident joint** — a matrix that characterizes the joint distribution of noisy and true labels. This enables principled detection of:

- **Label errors** in classification, regression, and multi-label tasks
- **Outliers and near-duplicates** in datasets
- **Annotator quality** for multi-annotator workflows
- **Data points most valuable** to label next (active learning)

The approach is model-agnostic and works with any ML framework (PyTorch, TensorFlow, scikit-learn, XGBoost, HuggingFace, etc.).

### Open-Source Library (`cleanlab`)

The standard data-centric AI package for Python. Key capabilities:

- Multi-label classification, token classification, image segmentation, object detection
- Consensus estimation for multi-annotator data
- Active learning with annotator quality weighting
- Compatible with any dataset and any model

### Cleanlab Studio (Commercial Product)

A no-code SaaS platform that runs optimized versions of the open-source algorithms on top of AutoML models, presenting detected issues in a smart data-editing interface. Targeted at enterprise ML teams who need to audit and improve training data at scale without writing code.

### Trustworthy Language Model (TLM)

Announced alongside the Series A in October 2023, the TLM provides a **real-time trustworthiness score** for every LLM output — enabling detection of hallucinations, retrieval failures, and knowledge gaps in LLM, RAG, and agent systems. Described as "the first reliable way to assess the trustworthiness of LLM outputs."

## Business Model

Cleanlab operated a **freemium / open-core model**:

- **Open-source library** (`cleanlab`): Free, MIT-licensed, driving community adoption and awareness.
- **Cleanlab Studio**: Commercial SaaS platform with enterprise pricing for no-code data quality workflows.
- **TLM API**: API access for real-time AI reliability scoring integrated into production LLM pipelines.

Revenue in 2023 was reported at approximately **$3.2M** with around **100 customers** ([source: Latka](https://getlatka.com/companies/cleanlab.ai)). [Uncertainty: this figure comes from a third-party estimate and may not be precise.]

## Funding History

| Round | Date | Amount | Lead Investors | Notable Participants |
|-------|------|--------|---------------|---------------------|
| Seed | July 2023 | $5M | Bain Capital Ventures | — |
| Series A | October 2023 | $25M | Menlo Ventures, TQ Ventures | Bain Capital Ventures, Databricks Ventures |
| **Total Raised** | — | **~$30M** | — | — |

Matt Murphy (Menlo Ventures) and Schuster Tanger (TQ Ventures) joined the board at Series A. Valuation was not publicly disclosed.

## Customers and Traction

- **1 million+ downloads** of the open-source library
- **Billions of AI data points cleaned** (per company claims)
- Used by **100+ Fortune 100 companies** (per company claims)
- Named customers include **Berkeley Research Group** and **BBVA**
- Deployments across finance, healthcare, customer service, and other sectors
- Case study: Cleanlab Studio improved LLM performance by **37%** by systematically improving training data — without changing model architecture or hyperparameters

## Acquisition by Handshake (January 2026)

On **January 28, 2026**, AI data-labeling company **Handshake** acquired Cleanlab in what was widely characterized as an **acqui-hire**. Key details:

- **Nine Cleanlab employees** joined Handshake's research organization, including all three co-founders
- Curtis Northcutt took the role of **Director, AI Research & Strategy** at Handshake
- Handshake acquired Cleanlab's latest research and technologies in confident learning, data-centric AI, and LLM evaluation
- **Financial terms were not disclosed**
- Cleanlab reportedly had acquisition interest from **Mercor, Surge, and Scale AI**, but chose Handshake because "rivals often rely on [Handshake's] network for talent" (per TechCrunch)
- The deal reflects the intense demand for specialized AI research talent in the data labeling/quality sector

The Cleanlab open-source library remains available on GitHub as of this writing.

## What Makes Cleanlab Interesting (Research Perspective)

1. **Theory-to-product pipeline**: Rare example of a peer-reviewed ML theory (confident learning) being directly commercialized. The IJCAI-JAIR Test-of-Time Award validates the research's lasting impact.

2. **Data-centric AI thesis**: Cleanlab operationalized Andrew Ng's "data-centric AI" vision — the idea that improving data quality yields better returns than improving model architecture. Their ImageNet label errors finding (100K+ errors in the gold-standard dataset) was a landmark result.

3. **Open-source flywheel**: The open-source library created awareness and trust, driving enterprise adoption of the commercial platform — a proven go-to-market in developer tools.

4. **LLM reliability pivot**: The TLM product showed Cleanlab's ability to evolve from structured-data label cleaning to LLM trustworthiness scoring — a much larger market as generative AI deployed at scale.

5. **Acquisition outcome signals**: Despite raising $30M and building a real product with revenue, Cleanlab was ultimately acqui-hired rather than scaling independently. This is instructive for studying the "build vs. buy" dynamics in AI infrastructure, where specialized research teams may be more valuable as talent acquisitions than as standalone businesses.

6. **MIT pedigree**: All three founders hold MIT PhDs with a combined 20,000+ citations. The company illustrates how elite research programs produce both foundational IP and founding teams for AI startups.

## Sources

- [Cleanlab Series A Announcement (BusinessWire)](https://www.businesswire.com/news/home/20231010484401/en/Cleanlab-Raises-%2425M-Series-A-to-Automatically-Increase-the-Value-and-Accuracy-of-the-Worlds-Enterprise-Data-Used-by-AI-ML-and-Analytics-Solutions)
- [Letter from the CEO: Handshake acquires Cleanlab](https://cleanlab.ai/blog/handshake-acquires-cleanlab/)
- [AI data labeler Handshake buys Cleanlab (TechCrunch)](https://techcrunch.com/2026/01/28/ai-data-labeler-handshake-buys-cleanlab-an-acquisition-target-of-multiple-others/)
- [Handshake Acquires Cleanlab (Handshake Blog)](https://joinhandshake.com/blog/our-team/handshake-acquires-cleanlab/)
- [Curtis Northcutt Personal Site](https://www.curtisnorthcutt.com/)
- [Cleanlab GitHub Repository](https://github.com/cleanlab/cleanlab)
- [Cleanlab About Page](https://cleanlab.ai/about/)
- [Cleanlab Series A — CEO Blog Post](https://cleanlab.ai/blog/series-a-announcement/)
- [Cleanlab Seed Funding — CEO Blog Post](https://cleanlab.ai/blog/announcing-cleanlab-studio/)
- [TQ Ventures and Menlo Ventures Co-Lead (Goodwin)](https://www.goodwinlaw.com/en/news-and-events/news/2023/10/announcements-technology-vc-tq-ventures-menlo-ventures)
- [Cleanlab on Crunchbase](https://www.crunchbase.com/organization/cleanlab)
- [Cleanlab TLM Hallucination Detection (GlobeNewsWire)](https://www.globenewswire.com/news-release/2024/04/25/2869699/0/en/Cleanlab-Announces-Billion-Dollar-Breakthrough-in-Detecting-AI-Hallucinations.html)
- [Cleanlab on CBInsights](https://www.cbinsights.com/company/cleanlab)
