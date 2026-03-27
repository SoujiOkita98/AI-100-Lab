---
founded: 2017
headquarters: Palo Alto, CA
sector: AI Hardware / AI Infrastructure (Full-Stack)
stage: Late-stage Private
employees: ~400-415 (as of early 2026)
website: https://sambanova.ai
founders:
- name: Rodrigo Liang
  role: CEO
  background: 20+ years in semiconductor engineering at Sun Microsystems and Oracle; BS/MS EE from Stanford; born in Taipei,
    grew up in Brazil
  origin: Taiwanese-Brazilian
- name: Kunle Olukotun
  role: Co-Founder & Chief Technologist
  background: Stanford Professor of EE and CS; pioneer of multicore processors; founded Afara Websystems (acquired by Sun
    for ~$62M); PhD from Michigan
  origin: Nigerian
- name: Christopher Re
  role: Co-Founder
  background: Stanford Professor of CS; MacArthur Fellow; co-founded Snorkel AI (unicorn); two companies acquired by Apple
    (Lattice/DeepDive 2017, Inductiv/HoloClean 2020)
  origin: American
last_updated: 2026-03-20
one_liner: SambaNova Systems is a full-stack AI infrastructure company that designs custom AI processors (Reconfigurable Dataflow
  Units, or RDUs), accompanying software, and enterprise services
website_verified: true
crunchbase: https://www.crunchbase.com/organization/sambanova
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/sambanova
data_notes: Funding corrected from $2.5B to ~$1.49B after cross-verification against Tracxn/Sacra. Previous figure was significantly
  inflated.
total_raised_m: 1490.0
name: SambaNova Systems
linkedin_verified: true
status: active
funding_rounds:
- stage: Series A
  date: 2018-03
  amount_m: 56.0
  lead_investors:
  - Walden International
  - GV
- stage: Series B
  date: 2019-04
  amount_m: 150.0
  lead_investors:
  - Intel Capital
- stage: Series C
  date: 2020-02
  amount_m: 250.0
  lead_investors:
  - BlackRock
- stage: Series D
  date: 2021-04
  amount_m: 676.0
  lead_investors:
  - SoftBank Vision Fund 2
- stage: Series E
  date: 2026-02
  amount_m: 350.0
  lead_investors:
  - Vista Equity Partners
confidence: medium
---

# SambaNova Systems

## Overview

SambaNova Systems is a full-stack AI infrastructure company that designs custom AI processors (Reconfigurable Dataflow Units, or RDUs), accompanying software, and enterprise services. Founded in 2017 by three Stanford University researchers, SambaNova builds an alternative to NVIDIA's GPU-centric AI compute stack by rethinking chip architecture from first principles around dataflow rather than instruction-based execution. The company sells integrated hardware-software systems and cloud-based inference services to enterprises, national laboratories, and sovereign AI customers worldwide.

The name "SambaNova" means "new dance" in Portuguese, chosen by co-founder Rodrigo Liang, who grew up in Brazil.

## Founders and Team

All three co-founders came from Stanford University, where the core intellectual property -- reconfigurable dataflow architecture -- was conceived.

| Name | Role | Background |
|---|---|---|
| **Kunle Olukotun** | Co-Founder & Chief Technologist | Cadence Design Professor of Electrical Engineering and Computer Science at Stanford. Pioneer of the multicore processor. Previously founded Afara Websystems (acquired by Sun Microsystems in 2002 for ~$62M). Director of Stanford's Pervasive Parallelism Lab. BS/MS from University of Michigan, PhD from Michigan. |
| **Christopher Re** | Co-Founder | Associate Professor of Computer Science at Stanford. MacArthur Fellow. Research spans machine learning systems and data management. Serial founder: also co-founded Snorkel AI (unicorn, programmatic data labeling), and two companies acquired by Apple -- Lattice/DeepDive (2017) and Inductiv/HoloClean (2020). |
| **Rodrigo Liang** | Co-Founder & CEO | 20+ years in semiconductor engineering. Previously led large processor design teams at Sun Microsystems and Oracle. Career began at Hewlett-Packard. BS and MS in Electrical Engineering from Stanford. Born in Taipei, grew up in Brazil. |

**Stanford DNA:** SambaNova is a textbook Stanford-origin AI company. Olukotun and Re were faculty colleagues who decided to build a new computing architecture purpose-built for AI workloads, rather than adapting legacy GPU or CPU designs. Liang, a Stanford-trained engineer and industry veteran, was brought in to lead commercialization.

Sources: [SambaNova Team Page](https://sambanova.ai/company/team), [University of Michigan CSE](https://cse.engin.umich.edu/stories/sambanova-founded-by-alumnus-kunle-olukotun-emerges-from-stealth-mode-with-ai-accelerated-hpc-system), [SoftBank Vision Fund Profile](https://visionfund.com/insights/dancing-with-ai), [World Economic Forum - Rodrigo Liang](https://www.weforum.org/stories/authors/rodrigo-liang/)

## Technology & Products

### Reconfigurable Dataflow Unit (RDU)

SambaNova's core innovation is the RDU -- a coarse-grained reconfigurable array architecture that executes AI workloads as streaming dataflow graphs rather than sequential instructions. This allows hundreds of operations to be fused into a single kernel call without hand-written code, exploiting on-chip pipeline, data, and tensor parallelism.

### Chip Generations

| Chip | Node | Year | Key Specs |
|---|---|---|---|
| **SN10** | 7 nm | ~2020 | First-generation RDU; Cardinal architecture |
| **SN40L** | 5 nm | 2024 | 638 BF16 TFLOPS per socket, 1040 PCUs, three-tier memory (520 MiB SRAM + 64 GiB HBM + up to 1.5 TiB DDR). Presented at IEEE ISSCC. |
| **SN50** | 5 nm | 2026 (announced Feb) | 2.5x BF16 throughput over SN40L (1.6 petaFLOPS BF16), new FP8 support at 3.2 petaFLOPS. 432 MB on-chip SRAM, 64 GB HBM2E, up to 2 TB DDR5. Supports models up to 10 trillion parameters. 256-accelerator multi-terabit interconnect. Designed for agentic AI inference. |

The **SambaRack** integrates 16 SN50 RDUs in a 20 kW air-cooled form factor -- a notable power-efficiency advantage over competing GPU racks.

### Software Stack

- **SambaFlow**: Compiler and runtime that automatically maps PyTorch/TensorFlow models onto the RDU dataflow architecture.
- **Samba-1**: A composition-of-experts (CoE) system bundling multiple specialized models (up to one trillion parameters) for enterprise generative AI. Launched February 2024.
- **SambaNova Suite / Dataflow-as-a-Service**: Cloud-hosted inference service.

Sources: [SambaNova RDU Product Page](https://sambanova.ai/products/rdu-ai-chips), [SN40L at IEEE ISSCC (arXiv)](https://arxiv.org/html/2405.07518v1), [SN50 Announcement (BusinessWire)](https://www.businesswire.com/news/home/20260226805517/en/SambaNova-Unveils-Fastest-Chip-for-Agentic-AI-Collaborates-with-Intel-and-Raises-$350M), [HPCwire](https://www.hpcwire.com/off-the-wire/sambanova-introduces-sn50-ai-chip-intel-collaboration-and-350m-in-new-funding/)

## Funding History

| Round | Date | Amount | Valuation (Post-Money) | Lead / Key Investors |
|---|---|---|---|---|
| Seed | Nov 2017 | $2M | -- | -- |
| Series A | Mar 2018 | $56M | -- | GV (Google Ventures), Walden International |
| Series B | Apr 2019 | $150M | -- | Intel Capital, GV |
| Series C | Feb 2020 | $250M | ~$2.5B | BlackRock, Intel Capital, GV |
| Series D | Apr 2021 | $676M | ~$5.1B | SoftBank Vision Fund 2, BlackRock, Intel Capital, GV, Temasek, GIC |
| Series E | Feb 2026 | $350M | ~$2.24B (down round) | Vista Equity Partners, Cambium Capital; Intel Capital, BlackRock, GV, T. Rowe Price, Battery Ventures, Mayfield, Atlantic Bridge, and others |

**Total raised: ~$1.48 billion.**

The Series E was a significant down round (~56% valuation decline from the 2021 peak). It came after reported acquisition talks with Intel fell through and a prolonged fundraising period amid intensifying competition from NVIDIA. Despite the valuation reset, the round brought in strategic partners and funded manufacturing of the SN50.

Sources: [Tracxn](https://tracxn.com/d/companies/sambanovasystems/__TvzSIBPeKIVjGmWovhh4uYJ9eAl6FPYF0Iwfg8H-YJg/funding-and-investors), [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-24/intel-backed-sambanova-raises-cash-touts-softbank-chip-contract), [TechFundingNews](https://techfundingnews.com/sambanova-sn50-ai-chip-350m-series-e-intel/), [MarketScreener](https://www.marketscreener.com/news/sambanova-systems-inc-announced-that-it-has-received-350-million-in-funding-from-a-group-of-inves-ce7e5cdadc8ff726)

## Business Model

SambaNova operates three revenue streams:

1. **Hardware systems**: Sale of DataScale rack systems (SN40L, soon SN50-based) to enterprises, national labs, and sovereign customers. This is the primary revenue driver.
2. **Dataflow-as-a-Service (DaaS)**: Subscription/usage-based cloud inference service, allowing customers to run AI models on SambaNova hardware without capital expenditure.
3. **Professional services**: Data preparation, model training, optimization, and deployment support. Reportedly 25-33% of new customer engagements include a services component.

**Revenue:** Estimated at $100-122M in 2025 (uncertainty: these figures come from third-party estimates, not official disclosures).

Sources: [Sacra](https://sacra.com/c/sambanova-systems/), [GetLatka](https://getlatka.com/companies/sambanova.ai), [VentureBeat](https://venturebeat.com/ai/how-sambanova-systems-is-tackling-dataflow-as-a-service)

## Key Customers and Partnerships

### U.S. Department of Energy National Laboratories
SambaNova has deep relationships with DOE/NNSA labs, which are among their most prominent customers:
- **Argonne National Laboratory** -- DataScale deployment for AI-driven science (weather, drug response, materials)
- **Lawrence Livermore National Laboratory (LLNL)** -- Cognitive simulation and AI research
- **Los Alamos National Laboratory (LANL)** -- Expanded deployment for inference workloads

### Enterprise and Global
- **SoftBank Corp.** -- First customer for SN50; deploying in next-generation AI data centers in Japan for sovereign and enterprise inference across Asia-Pacific
- **Accenture** -- Partner leveraging Samba-1 for enterprise AI
- **NetApp** -- Integration partner
- **Intel** -- Multi-year strategic collaboration announced February 2026 to co-deliver inference solutions; Intel also fabricates SambaNova chips

### Government & Public Sector
SambaNova positions itself for regulated and sovereign AI use cases, emphasizing on-premises deployment, data privacy, and security -- differentiators for government buyers who cannot use public cloud AI services.

Sources: [DOE/NNSA](https://www.energy.gov/nnsa/articles/nnsa-establishes-partnership-accelerate-key-artificial-intelligence-computing), [LLNL](https://www.llnl.gov/article/49821/llnl-sambanova-systems-announce-additional-ai-hardware-support-labs-cognitive), [Argonne](https://www.alcf.anl.gov/news/sambanova-delivers-next-generation-datascale-system-argonne-national-laboratory), [Bloomberg on SoftBank deal](https://www.bloomberg.com/news/articles/2026-02-24/intel-backed-sambanova-raises-cash-touts-softbank-chip-contract)

## What Makes SambaNova Interesting

1. **Deep Stanford roots**: The company is a direct product of Stanford faculty research. Two of three co-founders (Olukotun and Re) are active Stanford professors. The RDU architecture emerged from the Stanford Pervasive Parallelism Lab. Chris Re is also the co-founder of Snorkel AI and has had two startups acquired by Apple -- making him one of the most prolific academic-founders in AI.

2. **First-principles hardware design**: Rather than adapting GPUs or building GPU clones, SambaNova designed an entirely new dataflow architecture. The RDU's streaming execution model and three-tier memory hierarchy are fundamentally different from NVIDIA's approach, potentially offering structural advantages for large-model inference where memory bandwidth is the bottleneck.

3. **Full-stack integration**: SambaNova provides chips, boards, racks, compiler toolchain, model libraries, and cloud services. This Apple-like vertical integration allows end-to-end optimization but also means the company must execute across hardware, software, and services simultaneously.

4. **Government/sovereign AI beachhead**: The DOE national lab deployments give SambaNova credibility in high-performance, security-sensitive environments. This customer base is sticky and less price-sensitive than commercial cloud -- a strategic moat as sovereign AI spending accelerates globally.

5. **Survival through a brutal market**: SambaNova's valuation dropped from $5.1B to $2.24B, it laid off staff in 2025, and acquisition talks with Intel collapsed. Yet it secured $350M in new capital, launched a competitive new chip (SN50), and landed a marquee SoftBank deployment. The company's resilience -- or stubbornness -- through the NVIDIA-dominated AI chip market is notable.

6. **SN50 economics**: The claim of 3x lower inference cost than GPUs, combined with 20 kW air-cooled racks, addresses the two biggest pain points in AI infrastructure: cost and power. If validated at scale, this could open markets in power-constrained data centers and cost-sensitive enterprise deployments.

## Risks and Open Questions

- **NVIDIA dominance**: NVIDIA's CUDA ecosystem and market position remain formidable. Convincing customers to adopt a non-GPU architecture requires overcoming massive switching costs and ecosystem lock-in.
- **Down-round valuation**: The 56% valuation decline signals investor concern. The company must demonstrate that the SN50 and Intel partnership can drive meaningful revenue growth.
- **Revenue scale uncertainty**: $100-122M in estimated 2025 revenue against ~$1.5B in total capital raised suggests the company has not yet achieved capital efficiency. Official revenue figures are not publicly disclosed.
- **Chris Re's involvement**: Re has multiple ventures (notably Snorkel AI and his Stanford lab). His level of day-to-day involvement at SambaNova in 2026 is unclear.
- **Execution risk on SN50**: The chip was announced in February 2026 and is expected to ship later in the year. Manufacturing, yield, and customer adoption timelines remain uncertain.

## Key Metadata

- **Offices**: Palo Alto (HQ), Austin (TX), Cambridge (UK), Bengaluru (India)
- **Competitors**: NVIDIA, AMD, Intel (Gaudi/Habana), Cerebras, Groq, Graphcore (acquired by SoftBank), d-Matrix
- **Key IP**: Reconfigurable Dataflow Architecture, Composition of Experts (CoE) model serving

---

*Profile compiled 2026-03-20. Revenue and employee figures are estimates from third-party sources and should be verified against official disclosures when available.*
