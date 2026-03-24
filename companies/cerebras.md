---
company: Cerebras Systems
founded: 2015
headquarters: Sunnyvale, California, USA
sector: AI Hardware / Semiconductors
stage: Pre-IPO (targeting Q2 2026 IPO)
latest_valuation: $23 billion (Series H, February 2026)
total_funding: ~$4.3 billion (across 8 rounds)
employees: ~500 (estimate; exact figure uncertain)
website: https://www.cerebras.ai
ticker_pending: CBRS (Nasdaq, planned)
founders:
- name: Andrew Feldman
  role: Co-Founder & CEO
  background: Previously co-founded SeaMicro (sold to AMD for $334M). Stanford BA Economics/PoliSci, Stanford MBA. Former
    VP at Force10 Networks (sold to Dell for $800M).
  origin: American (inferred from name)
- name: Gary Lauterbach
  role: Co-Founder
  background: Co-founded SeaMicro with Feldman.
  origin: American (inferred from name)
- name: Sean Lie
  role: Co-Founder
  background: Previously at SeaMicro.
  origin: Chinese-American (inferred from name)
- name: Jean-Philippe Fricker
  role: Co-Founder
  background: Previously at SeaMicro.
  origin: French (inferred from name)
- name: Michael James
  role: Co-Founder
  background: Previously at SeaMicro.
  origin: American (inferred from name)
last_updated: 2026-03-20
one_liner: Cerebras Systems is an AI semiconductor company that designs and manufactures the world's largest computer chips
  -- Wafer-Scale Engines (WSE) -- purpose-built for AI training and inference
website_verified: true
linkedin: https://www.linkedin.com/company/cerebras-systems
twitter: '@CerebrasSystems'
crunchbase: https://www.crunchbase.com/organization/cerebras
crunchbase_verified: true
latest_valuation_m: 23000
data_notes: Valuation updated to $23B after Series H (Feb 2026). Previous $8.1B was from Series G (Oct 2025). Sum of disclosed
  rounds is ~$2.8B; total_raised_m of $4.3B includes undisclosed early rounds and secondary transactions.
total_raised_m: 4300
funding_rounds:
- stage: Seed
  date: 2015-12
  lead_investors:
  - Benchmark
  - Foundation Capital
  - Eclipse Ventures
  source: https://www.crunchbase.com/organization/cerebras-systems
  notes: Exact seed amount undisclosed. Company founded 2015; seed preceded Series A.
- stage: Series A
  date: 2016-05
  amount_m: 27.0
  lead_investors:
  - Benchmark
  - Foundation Capital
  source: https://www.crunchbase.com/organization/cerebras-systems
- stage: Series B
  date: 2016-12
  amount_m: 25.0
  lead_investors:
  - Coatue Management
  source: https://www.crunchbase.com/organization/cerebras-systems
- stage: Series C
  date: 2017-01
  amount_m: 60.0
  lead_investors:
  - VY Capital
  source: https://www.crunchbase.com/organization/cerebras-systems
- stage: Series D
  date: 2018-11
  amount_m: 88.0
  lead_investors:
  - Altimeter
  - VY Capital
  source: https://www.crunchbase.com/organization/cerebras-systems
- stage: Series E
  date: 2019-11
  amount_m: 272.0
  lead_investors:
  - Undisclosed
  source: https://en.wikipedia.org/wiki/Cerebras
- stage: Series F
  date: 2021-11
  amount_m: 250.0
  lead_investors:
  - Alpha Wave Ventures
  source: https://www.cerebras.ai/press-release/cerebras-systems-raises-250m-in-funding-for-over-4b-valuation-to-advance-the-future-of-artificial-intelligence-compute
- stage: Series G
  date: 2025-09
  amount_m: 1100.0
  lead_investors:
  - Fidelity
  - Atreides Management
  source: https://www.cerebras.ai/press-release/series-g
- stage: Series H
  date: 2026-02
  amount_m: 1000.0
  lead_investors:
  - Tiger Global
  source: https://www.cerebras.ai/press-release/cerebras-systems-raises-usd1-billion-series-h
name: Cerebras Systems
linkedin_verified: true
status: active
---

# Cerebras Systems

## Overview

Cerebras Systems is an AI semiconductor company that designs and manufactures the world's largest computer chips -- Wafer-Scale Engines (WSE) -- purpose-built for AI training and inference. Rather than cutting a silicon wafer into hundreds of small chips, Cerebras uses the entire wafer as a single processor, delivering orders-of-magnitude more compute cores, on-chip memory, and interconnect bandwidth than conventional GPUs. The company positions itself as the primary architectural alternative to NVIDIA's GPU-dominated AI compute stack.

## Founders and Team

All five co-founders previously worked together at **SeaMicro**, a microserver startup founded in 2007 that AMD acquired for ~$334 million in 2012. This shared history gives the founding team deep experience shipping novel silicon at scale.

| Name | Role | Background |
|---|---|---|
| **Andrew Feldman** | Co-Founder & CEO | Stanford BS and Stanford GSB MBA. Previously co-founded SeaMicro; VP roles at Force10 Networks (sold to Dell for ~$800M) and RiverStone Networks (IPO 2001). Grew up on the Stanford campus (parents were faculty). |
| **Gary Lauterbach** | Co-Founder & CTO (retired) | Co-founded SeaMicro with Feldman. Deep background in chip architecture. Now retired from day-to-day role. |
| **Sean Lie** | Co-Founder & CTO / Chief Hardware Architect | Lead architect of the WSE chip line. Previously at SeaMicro. Now serves as CTO following Lauterbach's retirement. |
| **Michael James** | Co-Founder & Chief Software Architect | Leads software stack (CSoft platform, compiler, runtime). Previously at SeaMicro. |
| **Jean-Philippe Fricker** | Co-Founder & Chief System Architect | Oversees full-system integration (cooling, power delivery, networking). Previously at SeaMicro. |

Sources: [Cerebras Company Page](https://www.cerebras.ai/company), [Contrary Research](https://research.contrary.com/company/cerebras), [Eclipse Capital Interview](https://eclipse.capital/blog/accelerating-discovery-andrew-feldman-co-founder-and-ceo-cerebras-systems/)

## Technology & Products

### Wafer-Scale Engine (WSE)

Cerebras' core innovation is using an entire 300 mm silicon wafer as a single chip rather than dicing it into individual dies. Three generations have been produced:

| Generation | Year | Transistors | Compute Cores | On-Chip SRAM | Process Node |
|---|---|---|---|---|---|
| WSE-1 | 2019 | 1.2 trillion | 400,000 | 18 GB | 16 nm (TSMC) |
| WSE-2 | 2021 | 2.6 trillion | 850,000 | 40 GB | 7 nm (TSMC) |
| WSE-3 | 2024 | 4 trillion | 900,000 | 44 GB | 5 nm (TSMC) |

The WSE-3 measures 46,255 mm squared (21.5 cm per side) and delivers 125 peak petaflops of AI compute -- claimed to be 28x more compute than the NVIDIA B200.

### CS-3 System

The CS-3 is the full rackmount AI supercomputer built around the WSE-3, with up to 1.2 petabytes of attached memory (via MemoryX technology) and Cerebras' SwarmX fabric for multi-system clustering. It is designed to train frontier models 10x larger than GPT-4.

### Cerebras Inference

Cerebras also offers cloud-based inference services, marketing dramatically lower latency and higher tokens-per-second than GPU-based alternatives.

Sources: [Cerebras Chip Page](https://www.cerebras.ai/chip), [IEEE Spectrum on WSE-3](https://spectrum.ieee.org/cerebras-chip-cs3), [Wikipedia](https://en.wikipedia.org/wiki/Cerebras)

## Funding History

| Round | Date | Amount | Post-Money Valuation | Lead Investor(s) | Source |
|---|---|---|---|---|---|
| Series A | May 2016 | $27M | Undisclosed | Benchmark, Foundation Capital, Eclipse Ventures | [Crunchbase](https://www.crunchbase.com/organization/cerebras-systems) |
| Series B | Dec 2016 | ~$25M | Undisclosed | Coatue Management | [Crunchbase](https://www.crunchbase.com/organization/cerebras-systems) |
| Series C | Jan 2017 | $60M | Undisclosed | VY Capital | [Crunchbase](https://www.crunchbase.com/organization/cerebras-systems) |
| Series D | Nov 2018 | $88M | ~$1B (unicorn) | Altimeter, VY Capital, Coatue, Benchmark, others | [MicroVentures](https://microventures.com/microventures-portfolio-company-cerebras-history-and-milestones) |
| Series E | Nov 2019 | $272M | ~$2.4B | Undisclosed (likely existing syndicate) | [Wikipedia](https://en.wikipedia.org/wiki/Cerebras) |
| Series F | Nov 2021 | $250M | ~$4B | Alpha Wave Ventures, Abu Dhabi Growth Fund (ADG) | [Cerebras Press Release](https://www.cerebras.ai/press-release/cerebras-systems-raises-250m-in-funding-for-over-4b-valuation-to-advance-the-future-of-artificial-intelligence-compute) |
| Series G | Sep 2025 | $1.1B | $8.1B | Fidelity Management & Research, Atreides Management | [Cerebras Press Release](https://www.cerebras.ai/press-release/series-g), [TechCrunch](https://techcrunch.com/2025/09/30/a-year-after-filing-to-ipo-still-private-cerebras-systems-raises-1-1b/) |
| Series H | Feb 2026 | $1.0B | ~$23B | Tiger Global | [Cerebras Press Release](https://www.cerebras.ai/press-release/cerebras-systems-raises-usd1-billion-series-h), [DCD](https://www.datacenterdynamics.com/en/news/cerebras-systems-raises-1bn-at-23bn-valuation/) |

**Notable investors across rounds:** Benchmark, Coatue, Tiger Global, Fidelity, Altimeter, Alpha Wave Global, AMD (Series H), Valor Equity Partners, 1789 Capital.

**Note:** Series A-C amounts and lead investors are sourced from Crunchbase and Tracxn; some early-round details may be approximate. The Series E lead investor is not confirmed in public sources.

## Business Model

Cerebras operates a **vertically integrated hardware + cloud compute** model:

1. **Hardware sales:** Selling CS-3 (and prior CS-2) systems to enterprises, national labs, and sovereign AI programs. Systems are priced in the millions of dollars per unit.
2. **Cloud inference services:** Cerebras Inference offers pay-per-token cloud access, competing directly with NVIDIA-powered cloud inference.
3. **Large-scale compute partnerships:** Multi-year deals to supply AI compute capacity (e.g., the OpenAI partnership).

### Revenue

| Period | Revenue | Notes |
|---|---|---|
| 2022 | ~$25M | Early commercial traction |
| 2023 | ~$79M | ~3x year-over-year growth |
| H1 2024 | ~$136M | Annualized run rate approaching $270M+ |
| 2025 (est.) | >$1B | Company estimate; driven in part by new contracts |

**Customer concentration risk:** In H1 2024, approximately 87% of revenue came from G42, a UAE-based technology conglomerate. This concentration triggered a CFIUS (Committee on Foreign Investment in the U.S.) national security review and was a major factor in the withdrawal of Cerebras' initial IPO filing in late 2024/early 2025. G42 is no longer listed among investors in the latest filings.

Sources: [CNBC](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html), [Sacra](https://sacra.com/c/cerebras-systems/), [InsiderFinance](https://www.insiderfinance.io/news/openai-cerebras-deal-diversifies-cerebras)

## Key Customers

- **OpenAI** -- Multiyear deal (through 2028) to deliver 750 MW of computing power for inference, valued at >$10B. Signed January 2026. This is the single most significant contract in Cerebras' history and dramatically diversifies revenue away from G42.
- **Oracle** -- Oracle's cloud infrastructure now includes Cerebras chips alongside NVIDIA and AMD GPUs.
- **U.S. Department of Energy / National Labs** -- Argonne, Livermore, and others use Cerebras systems for scientific computing.
- **U.S. Department of Defense**
- **Mayo Clinic** -- Medical diagnostics and personalized medicine AI.
- **GlaxoSmithKline** -- Epigenomics research.
- **TotalEnergies** -- Energy sector AI applications.
- **Meta, AWS, IBM, Mistral, Cognition, AlphaSense, Notion** -- Listed as customers or partners as of 2025.

Sources: [Cerebras Series G Press Release](https://www.cerebras.ai/press-release/series-g), [CNBC on OpenAI Deal](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html), [CNBC on Oracle](https://www.cnbc.com/2026/03/10/ai-chipmaker-cerebras-namedropped-by-oracle-alongside-nvidia-and-amd-.html)

## IPO Status

Cerebras has had a turbulent path to going public:

1. **September 2024:** Filed S-1 with the SEC for a Nasdaq IPO.
2. **Late 2024 / Early 2025:** Withdrew the IPO filing after CFIUS review of G42's minority investment raised national security concerns. Simultaneously raised the $1.1B Series G instead.
3. **December 2025:** Reports surfaced that Cerebras was rekindling IPO plans, targeting early 2026.
4. **February 2026:** Closed $1B Series H at $23B valuation. G42 no longer listed among investors, resolving the regulatory overhang.
5. **March 2026 (current):** Cerebras has confidentially refiled for IPO, targeting **Q2 2026**. Morgan Stanley is reported as lead underwriter. Planned ticker: **CBRS** on Nasdaq.

Sources: [SiliconANGLE](https://siliconangle.com/2025/12/21/report-ai-chipmaker-cerebras-systems-rekindles-ipo-plans-targeting-early-2026-listing/), [Seeking Alpha](https://seekingalpha.com/news/4533742-ai-chipmaker-cerebras-targets-q2-2026-for-ipo-launch-report), [GuruFocus](https://www.gurufocus.com/news/4078450/cerebras-systems-cbrs-plans-2026-ipo-following-federal-clearance)

## What Makes Cerebras Interesting

1. **Radical hardware bet that actually shipped.** Building a chip the size of a dinner plate was considered borderline impossible. Cerebras solved yield, thermal management, and interconnect problems that had stymied wafer-scale computing for decades -- and is now on its third generation.

2. **The only credible architectural alternative to NVIDIA at scale.** While many startups have attempted custom AI accelerators (Graphcore, Habana/Intel, Groq, SambaNova), Cerebras is arguably the furthest along in winning large enterprise and hyperscaler contracts. The OpenAI deal is a landmark validation.

3. **$10B+ OpenAI contract transforms the business.** This single deal addresses the company's biggest weakness (G42 revenue concentration) and provides multi-year revenue visibility heading into the IPO.

4. **Valuation tripled in 5 months** (from $8.1B in Sep 2025 to $23B in Feb 2026), reflecting accelerating commercial traction and the OpenAI partnership.

5. **Founder-team cohesion.** The five co-founders have worked together across multiple companies (SeaMicro, and now Cerebras) for nearly two decades, an unusual level of team continuity in the startup world.

6. **Inference, not just training.** While initially focused on training, Cerebras has pivoted aggressively into inference -- which is where the bulk of long-term AI compute spending is expected to land. Their wafer-scale architecture offers latency advantages that are structurally difficult for GPU clusters to match.

## Key Risks

- **NVIDIA dominance:** NVIDIA controls ~80%+ of the AI accelerator market and has a massive software moat (CUDA ecosystem). Cerebras must continually prove its software stack (CSoft) is production-ready.
- **Customer concentration (improving):** The G42 dependency was severe. While the OpenAI deal helps, execution on diversification is still in progress.
- **Geopolitical/regulatory risk:** The CFIUS episode demonstrated how geopolitical factors can derail business plans. Export controls on advanced AI chips remain a moving target.
- **Capital intensity:** Fabricating wafer-scale chips at TSMC is extraordinarily expensive. Cerebras must maintain access to sufficient capital and fab capacity.

## Comparable Companies

- NVIDIA (public; dominant GPU incumbent)
- AMD (public; GPU + custom AI silicon)
- Groq (private; LPU inference chips)
- SambaNova Systems (private; dataflow architecture)
- Graphcore (acquired by SoftBank, 2024; IPU architecture)
- d-Matrix (private; in-memory compute for inference)

---

*Profile compiled 2026-03-20. Data sourced from public filings, press releases, and news reports. Where figures are estimated or uncertain, this is noted. All source URLs are inline above.*
