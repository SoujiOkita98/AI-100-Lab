---
founded: '2018'
headquarters: San Francisco, CA (510 Treat Ave, San Francisco, CA 94110)
sector: AI Infrastructure / Data Labeling & Training
website: https://labelbox.com
founders:
- name: Manu Sharma
  role: CEO & Co-founder
  background: Aerospace engineer (Embry-Riddle, Stanford); former engineer at Planet Labs and DroneDeploy; born in Roorkee,
    India
  origin: Indian-American
- name: Brian Rieger
  role: President & Co-founder
  background: Former Boeing 787 aerodynamicist; Forbes 30 Under 30; built aerospace hardware for the ISS
  origin: American
- name: Dan Rasmuson
  role: Co-founder
  background: Software developer; early work in medical diagnostic imaging tools
  origin: American
latest_round: Series D ($110M, Jan 2022)
key_investors:
- SoftBank Vision Fund 2 (led Series D)
- Andreessen Horowitz
- Gradient Ventures (Google)
- Kleiner Perkins
- First Round Capital
- B Capital Group
- Databricks Ventures
- Snowpoint Ventures
- ARK Invest (Cathie Wood)
employee_count: ~150-340 (conflicting reports; see notes)
status: Private
last_updated: 2026-03-20
confidence: medium-high
funding_rounds:
- stage: Seed
  date: 2018-07
  amount_m: 3.9
  lead_investors:
  - First Round Capital
  - Kleiner Perkins
  source: https://tracxn.com/d/companies/labelbox/
- stage: Series A
  date: 2019-01
  amount_m: 10.0
  lead_investors:
  - Gradient Ventures
  source: https://labelbox.com/blog/labelbox-series-a/
- stage: Series B
  date: 2020-02
  amount_m: 25.0
  lead_investors:
  - Andreessen Horowitz
  source: https://labelbox.com/blog/series-b-announcement/
- stage: Series C
  date: 2021-02
  amount_m: 40.0
  lead_investors:
  - B Capital Group
  source: https://www.globenewswire.com/news-release/2021/02/12/2175106/0/en/
- stage: Series D
  date: 2022-01
  amount_m: 110.0
  lead_investors:
  - SoftBank Vision Fund
  source: https://www.crunchbase.com/organization/labelbox
one_liner: Labelbox is an AI data infrastructure company that provides an integrated platform for data labeling, model evaluation,
  and expert-sourced training data
website_verified: true
linkedin: https://www.linkedin.com/company/labelbox
crunchbase: https://www.crunchbase.com/organization/labelbox
crunchbase_verified: true
name: Labelbox
linkedin_verified: true
total_raised_m: 189.0
latest_valuation_m: 1000.0
---

# Labelbox

## Overview

Labelbox is an AI data infrastructure company that provides an integrated platform for data labeling, model evaluation, and expert-sourced training data. Originally focused on image annotation for computer vision, the company has evolved into a broader "data factory for AI teams," now serving the full lifecycle of training data creation -- including RLHF (reinforcement learning from human feedback) workflows for large language models. As of 2026, Labelbox positions itself as a three-pillar business: software platform, managed labeling services, and an expert network (Alignerr).

## Founding Story

Labelbox was co-founded in March 2018 by **Manu Sharma**, **Brian Rieger**, and **Dan Rasmuson** -- three friends with shared roots in aerospace engineering.

**Manu Sharma** grew up in industrial towns across northern India (born in Roorkee) and came to the US to study aerospace engineering at Embry-Riddle Aeronautical University and later Stanford, where he studied robotics, EE, CS, and industrial design. At Embry-Riddle he worked on blended wing body aircraft, bio-inspired flexible wings, and famously launched a camera to near-space via balloon for under $200. He is also a pilot who learned to fly with Dick Rutan (first nonstop unrefueled circumnavigation of the globe). Before Labelbox, Sharma was an early engineer at **DroneDeploy** (where he built systems for flying drones over the internet) and then worked at **Planet Labs**, the satellite imaging company operating hundreds of LEO satellites. It was at Planet Labs -- building production computer vision systems to detect objects from satellite imagery -- that Sharma encountered the core pain point: engineering teams were spending enormous effort just building internal tools to create and manage training data. This became the thesis for Labelbox.

**Brian Rieger** was a Boeing aerodynamicist who worked on testing and flight certification of the 787 Dreamliner. He later co-founded an aerospace startup that put hardware on the International Space Station and was named to Forbes 30 Under 30. He and Sharma were classmates who had collaborated on academic projects before their careers diverged -- Sharma to Bay Area startups, Rieger to Boeing in Texas -- before reuniting to start Labelbox.

**Dan Rasmuson** had a software development background and had attracted the attention of a major medical diagnostic imaging company's CTO for his work on internal data labeling tools. Less public information is available about Rasmuson compared to the other two founders.

The founding team's aerospace/robotics DNA is notable -- they came to AI data infrastructure not from a pure ML research background, but from applied engineering domains (satellites, drones, aircraft) where training data bottlenecks were viscerally felt.

## Funding History

| Round | Date | Amount | Lead Investor(s) | Notable Participants |
|-------|------|--------|-------------------|---------------------|
| Seed | Jul 2018 | $3.9M | Kleiner Perkins | -- |
| Series A | 2019 | $10M | Gradient Ventures (Google) | Kleiner Perkins, First Round Capital |
| Series B | 2020 | ~$25M (est.) | [Not confirmed] | Andreessen Horowitz |
| Series C | Feb 2021 | $40M | B Capital Group | a16z, First Round, Gradient Ventures, Kleiner Perkins, Cathie Wood/ARK |
| Series D | Jan 2022 | $110M | SoftBank Vision Fund 2 | Databricks Ventures, Snowpoint Ventures, a16z, B Capital, Cathie Wood |

**Total raised:** ~$189M across 5 rounds.

**Valuation:** Estimated ~$1B at Series D. [Note: Some sources reference a Series E at $1B valuation in Oct 2025, but this could not be independently confirmed across multiple sources. The Series D in Jan 2022 is the last well-documented round.]

**Investor thesis:** The investor base is notable for including both deep-tech VCs (Kleiner, a16z) and strategic AI players (Google's Gradient Ventures, Databricks). Cathie Wood's personal participation signals conviction in data labeling as a secular AI infrastructure bet.

## Business Model

Labelbox operates a **usage-based SaaS model** with three integrated revenue streams:

1. **Platform Software** -- The core labeling and evaluation platform, sold as a subscription. Customers pay based on data volume processed. The platform supports image, video, text, geospatial, and multimodal annotation. Deep integrations with AWS SageMaker and Google Cloud Vertex AI allow enterprises to apply committed cloud spend to Labelbox subscriptions.

2. **Managed Labeling Services** -- Labelbox manages annotation projects using external labeling contractors, providing quality assurance, workforce orchestration, and tooling. This is a services revenue layer on top of the platform.

3. **Alignerr Expert Network** -- Labelbox's curated network of 1M+ domain experts (software engineers, medical professionals, legal experts, financial analysts, etc.) who evaluate, train, and improve AI models. The network has a 3% acceptance rate and uses an AI interviewer ("Zara") for vetting. **Alignerr Connect** is the marketplace layer allowing customers to directly hire proven AI trainers.

**Revenue indicators (FY2025, estimated from third-party sources -- treat with caution):**
- Partner-facilitated revenue: ~$8.5M
- Platform revenue from AI lab integrations (OpenAI, Anthropic): ~$12M
- RLHF workflows now drive ~42% of enterprise AI buys
- Strategic alliances with Accenture and Deloitte reportedly contribute ~38% of enterprise ARR
- Cost-per-label reduced ~48% to ~$0.13 via auto-labeling in 2025
- 50M+ monthly annotations across customers

## Products & Technology

- **Annotate** -- Core labeling tool supporting images, video, text, documents, geospatial data, and conversational AI
- **Model Evaluation / Evaluation Studio** (released mid-2025) -- Real-time feedback on model performance with rubric-based evaluation tools for LLMs
- **RLHF Platform** -- Specialized workflows for preference labeling, human ranking/grading, and supervised fine-tuning datasets (~35% of annotation hours shifted to RLHF workflows as of FY2025)
- **Alignerr / Alignerr Connect** -- Expert network and marketplace for domain-specific AI training
- **Auto-labeling** -- Model-assisted labeling using foundation models to reduce human effort

## Customers

Labelbox claims to work with 80%+ of leading US AI labs. Named customers and partners include:

- **Walmart** -- Fortune 500 enterprise customer
- **Procter & Gamble** -- Fortune 500 enterprise customer
- **Genentech** -- Healthcare/biotech
- **Google Cloud** -- Deep partnership; LLM evaluation use case
- **OpenAI, Anthropic** -- AI lab customers (platform revenue)
- Various autonomous vehicle, defense, and e-commerce companies (not all publicly named)

## Competitive Landscape

| Competitor | Positioning |
|------------|-------------|
| **Scale AI** | Historically the largest rival; acquired by Meta in 2024, which reportedly triggered enterprise client concerns over data governance and some client migration to alternatives including Labelbox |
| **Surge AI** | Bootstrapped; focuses on "elite" labelers; reportedly surpassed $1B ARR by mid-2025 (~$25B valuation sought) |
| **V7 Labs** | Strong in platform tooling, especially for computer vision |
| **SuperAnnotate** | Platform competitor focused on annotation quality |
| **CVAT / Label Studio** | Open-source alternatives for teams with engineering resources |
| **Appen / Sama** | Legacy managed-services data annotation providers |

**Labelbox's differentiation:** The combination of (a) a self-serve software platform, (b) managed services, and (c) an expert network under one roof. The aerospace-engineering founding team brought a systems-engineering mindset -- treating training data as an end-to-end supply chain rather than just an annotation task. The pivot toward RLHF/LLM evaluation has been timely.

## Recent Developments (2025-2026)

- **Upcraft Acquisition (Feb 10, 2026):** Labelbox acquired Upcraft, a Chicago-based agentic sales automation startup founded in 2021. The strategic rationale is to integrate Upcraft's AI agent technology into Alignerr to automate outreach and engagement workflows, scaling how Labelbox recruits and manages its 1M+ expert network. Financial terms not disclosed.

- **Evaluation Studio Launch (mid-2025):** Released rubric-based evaluation tools for real-time LLM performance feedback.

- **RLHF Expansion:** ~35% of annotation hours shifted to human ranking/grading workflows; $18.4M invested in preference data infrastructure.

- **Cloud Marketplace Growth:** Native connectors for Vertex AI and SageMaker reportedly drove 28% enterprise ARR uplift in FY2025.

## Employee Count & Organization

Employee count is uncertain. Sources report conflicting figures:
- ~341 employees (one source, Aug 2025)
- ~144 employees (PitchBook, 2026 profile)
- ~88 employees (as of Dec 2023)

The wide variance may reflect the Upcraft acquisition, contractor vs. FTE counting differences, or recent restructuring. [Confidence: low on exact headcount.]

## What Makes Labelbox Interesting (Research Notes)

1. **Founding DNA:** Aerospace engineers who encountered the training data bottleneck firsthand at Planet Labs and DroneDeploy -- not ML researchers building tools for themselves, but systems engineers who saw the infrastructure gap.

2. **Pivot agility:** Successfully evolved from a computer vision labeling tool (2018) to a full-stack AI data factory encompassing LLM evaluation, RLHF, and expert sourcing -- a non-trivial business model expansion.

3. **Alignerr as a moat:** The curated expert network of 1M+ domain specialists with 3% acceptance rate is a defensible asset. As AI labs increasingly need domain-expert feedback (not just crowd-sourced labeling), this network becomes more valuable.

4. **Scale AI's Meta acquisition as tailwind:** Scale AI's 2024 acquisition by Meta created data governance concerns among enterprise and government clients, reportedly driving some toward Labelbox and other independent alternatives.

5. **Cloud marketplace integration:** The ability for enterprises to apply committed AWS/GCP cloud spend to Labelbox subscriptions reduces procurement friction -- a clever GTM strategy.

6. **Open question:** Whether the ~$189M raised is sufficient to compete long-term against well-funded competitors (Surge AI's meteoric growth) and against the trend of foundation models reducing the need for human annotation. Labelbox's bet is that expert-quality data for RLHF and evaluation becomes *more* important, not less, as models improve.

## Sources

- [Labelbox Funding & Investors - Tracxn](https://tracxn.com/d/companies/labelbox/__xzBGeM19qbagGRZx_Lc_eBB9u9Phv9DZ3UV676w6KBw/funding-and-investors)
- [Labelbox Series D Announcement - GlobeNewsWire](https://www.globenewswire.com/news-release/2022/01/06/2362270/0/en/Labelbox-Raises-110-Million-Series-D-Led-by-SoftBank-Vision-Fund-2.html)
- [Labelbox Series C Announcement - GlobeNewsWire](https://www.globenewswire.com/news-release/2021/02/12/2175106/0/en/Artificial-Intelligence-Startup-Labelbox-Closes-40-Million-in-Series-C-Funding.html)
- [Manu Sharma Bio](https://www.manuaero.com/about-manu-sharma/)
- [Manu Sharma - Crunchbase](https://www.crunchbase.com/person/manu-sharma-edbf)
- [Brian Rieger - Crunchbase](https://www.crunchbase.com/person/brian-rieger)
- [Labelbox Path to PMF - First Round Review](https://review.firstround.com/labelboxs-path-to-pmf-founders-need-to-be-contrarian-and-right-heres-how/)
- [Labelbox Brief History - CanvasBusinessModel](https://canvasbusinessmodel.com/blogs/brief-history/labelbox-brief-history)
- [Labelbox Business Model Canvas - CanvasBusinessModel](https://canvasbusinessmodel.com/products/labelbox-business-model-canvas)
- [Labelbox Acquires Upcraft - PR Newswire](http://www.prnewswire.com/news-releases/labelbox-acquires-agentic-sales-automation-startup-upcraft-to-rapidly-scale-the-human-expertise-powering-frontier-ai-302684445.html)
- [Labelbox Upcraft Blog Post](https://labelbox.com/blog/welcoming-upcraft-to-the-labelbox-team/)
- [Labelbox LLM Solution & Google Cloud Partnership - PR Newswire](https://www.prnewswire.com/news-releases/labelbox-introduces-large-language-model-llm-solution-to-help-enterprises-innovate-with-generative-ai-expands-partnership-with-google-cloud-301924810.html)
- [Labelbox Alignerr Connect](https://labelbox.com/services/alignerr-connect/)
- [Labelbox Official Site](https://labelbox.com/)
- [Labelbox vs Scale AI Comparison 2026 - AI Flow Review](https://aiflowreview.com/labelbox-vs-scale-ai-comparison-2026/)
- [RLHF Platforms in Biotech: Scale vs Labelbox - IntuitionLabs](https://intuitionlabs.ai/articles/rlhf-platforms-biotech-comparison)
- [Manu Sharma / Labelbox Interview - The Sequence](https://thesequence.substack.com/p/-manu-sharmaceo-of-labelbox-about)
- [Labelbox - Tau Ventures Profile](https://tauventures.com/labelbox-manu-sharma/)
- [Data Labeling Startups - Fortune](https://fortune.com/2020/02/04/artificial-intelligence-data-labeling-labelbox/)
- [Labelbox - Crunchbase](https://www.crunchbase.com/organization/labelbox)
- [Labelbox - CB Insights](https://www.cbinsights.com/company/labelbox)
