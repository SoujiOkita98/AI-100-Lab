---
name: VAST Data
sector: AI / Data Infrastructure & Storage Platform
founded: 2016
headquarters: New York, NY (R&D center in Tel Aviv, Israel)
website: https://www.vastdata.com
status: Private
latest_valuation: ~$30B (Series F, March 2026)
total_funding: ~$1.38B
founders:
- Renen Hallak (CEO)
- Shachar Fienblit (Chief R&D Officer)
- Jeff Denworth (Co-founder, VP Products)
- Alon Horev (CTO)
employees_approx: ~500-1,000 (estimate; exact figure uncertain)
research_date: 2026-03-20
confidence: high
funding_rounds:
- stage: Series A
  date: 2018-03
  amount_m: 25
  lead_investors: []
  source: https://www.crunchbase.com/funding_round/vast-data-series-a--ac86d6f8
- stage: Series B
  date: 2019-02
  amount_m: 40
  valuation_m: 400
  lead_investors:
  - Goldman Sachs
  - 83North
  - Norwest
  - TPG
  source: https://news.crunchbase.com/venture/vast-data-secures-100m-for-storage-triples-valuation-to-1-2b/
- stage: Series C
  date: 2020-04
  amount_m: 100
  valuation_m: 1200
  lead_investors: []
  source: https://news.crunchbase.com/venture/vast-data-secures-100m-for-storage-triples-valuation-to-1-2b/
- stage: Series D
  date: 2021-05
  amount_m: 83
  valuation_m: 3700
  lead_investors: []
  source: https://www.crunchbase.com/funding_round/vast-data-series-d--d8e5307b
- stage: Series E
  date: 2023-12
  amount_m: 118
  valuation_m: 9100
  lead_investors:
  - Fidelity Management & Research
  source: https://www.vastdata.com/press-releases/vast-series-e-funding-triples-valuation
- stage: Series F
  date: 2026-03
  amount_m: 500
  valuation_m: 30000
  lead_investors:
  - Nvidia
  - CapitalG (Alphabet)
  source: https://www.hpcwire.com/2026/03/12/vast-tops-off-with-series-f-at-a-30-billion-valuation/
  notes: ~$500M primary + ~$500M secondary tender.
one_liner: VAST Data is an AI-native data infrastructure company that has built a unified storage and data platform designed
  from the ground up for AI workloads
website_verified: true
---

# VAST Data

## Overview

VAST Data is an AI-native data infrastructure company that has built a unified storage and data platform designed from the ground up for AI workloads. The company's core innovation is its **Disaggregated Shared Everything (DASE)** architecture, which eliminates the traditional tradeoffs between performance, scale, and simplicity in enterprise storage. Originally known as a high-performance AI storage vendor, VAST has evolved into an operating-system-level provider with its **VAST AI OS** -- positioning itself as the data control plane for distributed, agentic AI computing. The company is widely considered the most valuable private high-tech company in Israel.

## Founding Story and Team Origins

VAST Data was founded in 2016 by a team of Israeli storage industry veterans who had previously built and scaled enterprise storage products at major companies.

- **Renen Hallak (CEO & Co-founder)**: Israeli-born engineer who served as VP of R&D at **XtremIO**, the all-flash storage startup acquired by Dell EMC in 2012 for approximately $430M. At XtremIO, Hallak led a team of roughly 200 engineers and contributed to products that generated over $1 billion in revenue for Dell EMC. He was recognized by Goldman Sachs as one of their "100 Most Intriguing Entrepreneurs." Hallak is known for running a lean, no-frills operation -- press reports note VAST avoids flashy offices and lavish corporate events, focusing resources on engineering.

- **Shachar Fienblit (Co-founder & Chief R&D Officer)**: Israeli engineer with deep expertise in software-defined storage. Previously held leadership roles at **Kaminario** (an Israeli flash storage company) and **IBM**. Leads the R&D organization based primarily in Tel Aviv.

- **Jeff Denworth (Co-founder)**: American; initial VP of Products. Brought over two decades of experience in storage sales and marketing, including serving as SVP of Marketing at **CTERA Networks** (an Israeli cloud storage company). Denworth provides the go-to-market and business development perspective among the founding team.

- **Alon Horev (Co-founder & CTO)**: Israeli engineer formerly at **Cisco** and **IBM**. Focused on core platform engineering, having driven multiple product tracks from inception in high-scale environments.

The founding thesis was straightforward: legacy storage architectures (shared-nothing clusters, traditional SANs) were fundamentally inadequate for the data-intensive demands of deep learning and AI. The founders saw that NVMe flash and high-speed networking (NVMe over Fabrics) could enable an entirely new architecture that collapsed the storage stack.

**Key leadership addition**: Mike Wing, formerly of Dell EMC, serves as company President.

**Team composition**: The majority of VAST's employees are in the R&D organization in Tel Aviv, Israel. Sales and marketing are headquartered in New York City, with operations in San Jose, California. The Israeli engineering DNA -- rooted in the XtremIO and Kaminario storage lineage -- is central to the company's identity.

## Technology and Architecture

VAST's core technical differentiation is its **DASE (Disaggregated Shared Everything) Architecture**:

- **Disaggregated**: Separates compute (stateless "CNodes" running in containers) from storage media (NVMe SSDs), connected via NVMe over Fabrics (NVMe-oF). This allows independent scaling of compute and capacity.
- **Shared Everything**: Every compute node has direct access to all data, metadata, and state in the cluster. System state is stored on NVMe SSDs, not just in DRAM, eliminating the consistency and scaling limitations of shared-nothing architectures.
- **No East-West Traffic**: Because there is no data rebalancing or inter-node coordination overhead, DASE clusters can scale to massive sizes without performance degradation.

In 2024-2025, VAST expanded from pure storage into the **VAST AI OS**, which provides:
- A unified data platform (file, object, and database in one system)
- Built-in vector search and real-time metadata services
- Event-driven data pipelines
- Managed Kubernetes for orchestrating AI services close to the data
- Native integration with GPU compute for AI training and inference

This positions VAST not just as a storage vendor but as the **data layer operating system** for AI factories.

## Funding History

| Round | Date | Amount | Valuation | Key Investors |
|-------|------|--------|-----------|---------------|
| Seed | 2016 | Undisclosed | -- | 83North, Norwest Venture Partners, New York Venture Partners |
| Series A | 2017 | ~$30M | -- | 83North, Norwest Venture Partners |
| Series B | 2019 | ~$40M | -- | 83North, Norwest Venture Partners, Next47 (Siemens) |
| Series C | 2020 | $100M | ~$1.2B | Tiger Global Management, Goldman Sachs |
| Series D | 2022 | $100M | ~$3.7B | Fidelity, BOND Capital, Tiger Global |
| Series E | Dec 2023 | $118M | $9.1B | Fidelity Ventures, Nvidia |
| Series F | Mar 2026 | $1B | $30B | CapitalG (Alphabet), Nvidia, Fidelity, and others |

**Total funding raised**: ~$1.38 billion

**Note on Series F structure**: Approximately half of the $1B Series F went to the company as primary capital; the other half was a secondary tender allowing early investors and employees to take liquidity. This suggests an IPO is not imminent but the company is providing interim liquidity to stakeholders.

**Notable investors across rounds**: Nvidia, CapitalG (Alphabet/Google), Fidelity, Goldman Sachs, Tiger Global Management, BOND Capital, Dell, Drive Capital, Scale Asia Ventures, Whale Rock Capital Management, Next47 (Siemens), 83North, CF Private Equity, Commonfund, Greenfield Partners, Norwest Venture Partners, TPG, New York Venture Partners.

## Financial Performance

| Metric | Value | Date/Period |
|--------|-------|-------------|
| ARR | ~$200M | January 2025 |
| ARR | ~$350-400M | End of 2025 (estimate) |
| ARR target | ~$600M+ | 2026 (projected) |
| YoY growth rate | ~2.5-3x | 2024-2025 |
| Profitability | Free cash flow positive | As of mid-2025 |
| Contract length | 5-7 years typical | -- |
| Customer churn | Very low (described as "highly sticky") | -- |

**Note**: The $1.17B CoreWeave deal alone could push effective ARR significantly higher, though deal revenue recognition timing is uncertain. Some analysts suggest ARR could be approaching or exceeding $1B when factoring in the CoreWeave contract ramp.

VAST is described as a rare startup that is both profitable and growing at a high rate -- an unusual combination in enterprise infrastructure.

## Customers

VAST Data's customer base spans hyperscalers, neoclouds, AI labs, financial services, government, and media/entertainment:

- **Hyperscalers & Cloud**: Nvidia, Google Cloud, Microsoft, Amazon Web Services
- **Neoclouds**: CoreWeave ($1.17B deal, November 2025), Nebius, Firmus Technologies
- **AI Labs**: xAI (Elon Musk's AI company -- reportedly used for the Colossus supercomputer with 100,000+ H100 GPUs and over an exabyte of flash storage)
- **Enterprise**: Cisco, multiple Fortune 100 companies, "some of the world's largest banks"
- **Media/Entertainment**: Pixar (reported)
- **Hardware Partners**: Supermicro (joint enterprise AI data platform with Nvidia, announced at GTC 2026)

## Key Partnerships

- **Nvidia**: Strategic investor and technology partner. Deep integration between VAST AI OS and Nvidia's GPU ecosystem. Joint solutions for AI factories.
- **CoreWeave**: $1.17 billion commercial agreement (November 2025) making VAST AI OS the primary data foundation across CoreWeave's GPU-dense cloud data centers. Contracts span 3-5 years.
- **Supermicro**: Joint enterprise AI data platform solution with Nvidia, launched at GTC 2026.

## Business Model

VAST operates as an **enterprise software and infrastructure platform** company:

- **Software-defined platform**: VAST AI OS is the core product, deployable on commodity hardware
- **Subscription/recurring revenue**: Long-term contracts (5-7 year typical duration) drive high recurring revenue with very low churn
- **Land and expand**: Enterprises reportedly now write $100M+ checks for AI infrastructure, with VAST benefiting from expanding deployments
- **Strategic positioning**: Moving up the stack from storage to a full AI data operating system, increasing wallet share per customer

The evolution from "storage vendor" to "AI OS provider" is a deliberate strategy to avoid commoditization and capture more value in the AI infrastructure stack.

## What Makes VAST Data Interesting

1. **Architecture-first moat**: DASE was a genuinely novel storage architecture when introduced, and the expansion to VAST AI OS extends that architectural advantage into a full data platform. Competitors (NetApp, Pure Storage, Dell, Weka) have not replicated the disaggregated shared-everything approach.

2. **Israeli storage mafia**: The founding team comes from the XtremIO/Kaminario/CTERA lineage -- companies that collectively generated billions in revenue and exits for Dell EMC and others. This is a proven team that has built and scaled enterprise storage before.

3. **Profitable hypergrowth**: Being free-cash-flow positive while growing 2.5-3x annually is exceptionally rare for an infrastructure startup at this scale. This gives VAST strategic optionality -- it does not need to raise capital to survive.

4. **AI tailwind with real revenue**: Unlike many AI-adjacent companies, VAST has massive, verifiable enterprise contracts (the $1.17B CoreWeave deal is public). The customer list (Nvidia, xAI, CoreWeave, major banks) represents real production AI workloads, not proofs of concept.

5. **Platform expansion play**: The shift from storage to AI OS mirrors the classic infrastructure playbook (think VMware's evolution from hypervisor to cloud platform). If VAST succeeds in becoming the default data layer for AI factories, the TAM expands dramatically beyond storage.

6. **Nvidia ecosystem centrality**: VAST is deeply embedded in the Nvidia AI infrastructure ecosystem. Nvidia is both an investor and a customer, and VAST is the data platform partner for Nvidia's AI factory reference architectures. This is a powerful flywheel.

7. **$30B valuation as a private company**: VAST is now the most valuable private tech company in Israel and one of the most valuable private AI infrastructure companies globally, rivaling CoreWeave's pre-IPO valuation.

## Risks and Open Questions

- **Customer concentration**: The CoreWeave deal represents a massive portion of expected revenue. If CoreWeave faces financial difficulties (it carries significant debt), this could impact VAST.
- **IPO timing**: The Series F secondary component suggests an IPO is not imminent, but the company will face public market scrutiny eventually. Exact financials (margins, net income) are not publicly disclosed.
- **Competition**: Pure Storage, NetApp, Dell, and Weka are all pursuing AI storage workloads aggressively. Hyperscalers may also build or buy competing solutions.
- **Valuation justification**: At $30B, VAST trades at a very high multiple of current ARR (~50-75x on $400-600M ARR). This requires sustained hypergrowth to justify.

## Recognition

- **CNBC Disruptor 50** (2025)
- Goldman Sachs "100 Most Intriguing Entrepreneurs" (Renen Hallak)

## Sources

- [VAST Tops Off with Series F at $30B Valuation - HPCwire (March 2026)](https://www.hpcwire.com/2026/03/12/vast-tops-off-with-series-f-at-a-30-billion-valuation/)
- [VAST Data raises $1B at $30B valuation - Blocks and Files (March 2026)](https://www.blocksandfiles.com/flash/2026/03/11/vast-data-raises-1b-at-30b-valuation-as-ai-storage-demand-surges/5208106)
- [Vast Data raises $1 billion at $30 billion valuation - Calcalist (2026)](https://www.calcalistech.com/ctechnews/article/byoqzk2ybx)
- [VAST Data's $1.17 Billion Deal with CoreWeave - Next Platform (Nov 2025)](https://www.nextplatform.com/2025/11/07/vast-datas-1-17-billion-deal-with-coreweave-is-a-leading-indicator/)
- [Nvidia-backed Vast Data inks $1.17B AI deal with CoreWeave - Yahoo Finance (Nov 2025)](https://finance.yahoo.com/news/exclusive-nvidia-backed-vast-data-120456403.html)
- [Vast Data in talks with CapitalG, Nvidia at up to $30B valuation - TechCrunch (Aug 2025)](https://techcrunch.com/2025/08/01/vast-data-in-talks-with-alphabets-capitalg-nvidia-to-fund-round-at-up-to-30b-valuation/)
- [AI storage platform Vast Data aimed for $25B valuation - TechCrunch (June 2025)](https://techcrunch.com/2025/06/10/ai-storage-platform-vast-data-aimed-for-25b-valuation-in-new-round-sources-say/)
- [VAST Closes Series E Funding Round at $9.1B - VAST Data (Dec 2023)](https://www.vastdata.com/press-releases/vast-series-e-funding-triples-valuation)
- [Vast reshapes data infrastructure for agentic AI - SiliconANGLE (Feb 2026)](https://siliconangle.com/2026/02/20/vast-reshaes-data-infrastructure-agentic-ai-vastforward/)
- [VAST Data positions the data layer for AI scale - SiliconANGLE (Feb 2026)](https://siliconangle.com/2026/02/12/vast-data-positions-data-layer-ai-scale-vastforward/)
- [Supermicro and VAST Accelerate Path to Production AI at GTC 2026 - VAST Data](https://www.vastdata.com/blog/supermicro-vast-accelerate-path-production-ai-gtc-2026)
- [Enterprises now write $100M checks for AI infrastructure - Fierce Network](https://www.fierce-network.com/cloud/enterprises-now-writing-100m-checks-ai-infrastructure-says-vast-data-vp)
- [VAST Data: 2025 CNBC Disruptor 50](https://www.cnbc.com/2025/06/10/vast-data-cnbc-disruptor-50.html)
- [No parties or flashy offices: Israel's most promising startup - Ynet](https://www.ynetnews.com/business/article/s1ucky2vgl)
- [VAST Data DASE Architecture](https://www.vastdata.com/disaggregated-shared-everything-architecture-dase)
- [About VAST Data](https://www.vastdata.com/about)
- [VAST Data Wikipedia](https://en.wikipedia.org/wiki/VAST_Data)
- [Vast Data nears record-breaking round - Calcalist](https://www.calcalistech.com/ctechnews/article/b8kyeze8s)
- [VAST Data more than doubling valuation - Globes](https://en.globes.co.il/en/article-vast-data-more-than-doubling-valuation-in-new-raise-1001532003)
- [VAST Data plans funding round for early stockholder liquidity - Blocks and Files (Feb 2026)](https://blocksandfiles.com/2026/02/05/vast-data-plans-funding-round-so-early-stock-holders-can-get-cash/)
