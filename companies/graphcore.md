---
company: Graphcore
legal_name: Graphcore Ltd. (wholly owned subsidiary of SoftBank Group Corp.)
founded: 2016
headquarters: Bristol, United Kingdom
sector: AI Hardware / Semiconductors (IPU Architecture)
stage: Acquired (SoftBank, July 2024)
acquisition_price: ~$500 million (reported; company disputed figure without disclosing actual amount)
total_funding_pre_acquisition: ~$730 million
employees: ~500 at peak; reduced pre-acquisition
website: https://www.graphcore.ai
founders:
- name: Nigel Toon
  role: Co-Founder & CEO
  background: 30+ years in semiconductors; former CEO of Icera (acquired by Nvidia for ~$367M) and XMOS
  origin: British
- name: Simon Knowles
  role: Co-Founder & CTO
  background: Chief architect of the IPU; co-founded Icera and Element 14 (acquired by Broadcom); one of UK's most accomplished
    chip designers
  origin: British
last_updated: 2026-03-20
one_liner: Graphcore was a British AI chip company that designed the Intelligence Processing Unit (IPU), a novel processor
  architecture built specifically for machine learning workloads
website_verified: true
crunchbase: https://www.crunchbase.com/organization/graphcore
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/graphcore
total_raised_m: 720.0
name: Graphcore
linkedin_verified: true
---

# Graphcore

## Overview

Graphcore was a British AI chip company that designed the Intelligence Processing Unit (IPU), a novel processor architecture built specifically for machine learning workloads. Founded in 2016 in Bristol by semiconductor veterans Nigel Toon and Simon Knowles, Graphcore was once valued at $2.8 billion and was considered the most promising European challenger to Nvidia's GPU dominance.

In July 2024, SoftBank acquired Graphcore for a reported ~$500 million -- a fraction of its peak valuation and less than the total capital invested. The acquisition is widely viewed as one of the most significant cautionary tales in AI hardware, illustrating how even well-funded, technically sophisticated chip startups can fail to achieve commercial traction against Nvidia's ecosystem moat.

## Founders and Team

| Name | Role | Background |
|---|---|---|
| **Nigel Toon** | Co-Founder & CEO | 30+ years in semiconductor industry. Previously CEO of Icera (acquired by Nvidia for ~$367M in 2011) and XMOS. Deep experience in chip commercialization. |
| **Simon Knowles** | Co-Founder & CTO | Chief architect of the IPU. Previously co-founded Icera with Toon. Earlier, co-founded Element 14 (acquired by Broadcom). One of the UK's most accomplished chip designers. |

The Toon-Knowles partnership is remarkable: they co-founded multiple semiconductor companies together over two decades, including Icera (sold to Nvidia) and Element 14 (sold to Broadcom). Graphcore was their most ambitious project.

## Funding History (Pre-Acquisition)

| Round | Date | Amount | Valuation | Lead/Notable Investors |
|---|---|---|---|---|
| Series A | 2016 | $30M | Undisclosed | Bosch, Samsung, Dell, Amadeus Capital |
| Series B | 2017 | $50M | Undisclosed | Sequoia Capital, Atomico |
| Series C | 2018 | $200M | ~$1.7B | BMW i Ventures, Microsoft, Dell, Bosch |
| Series D | 2020 | $150M | ~$2.8B | Ontario Teachers' Pension Plan, Fidelity, Baillie Gifford |
| Series E | 2022 | $200M+ | ~$2.8B (flat) | Ontario Teachers', Draper Esprit |

**Total raised:** ~$730 million across all rounds.

**Notable investors:** Sequoia Capital, Microsoft, Samsung, Bosch, BMW, Fidelity, Baillie Gifford, Atomico, Ontario Teachers' Pension Plan.

## Technology: The IPU

The Intelligence Processing Unit (IPU) was designed around a "Bulk Synchronous Parallel" (BSP) model, optimized for the irregular, sparse computations common in machine learning -- as opposed to GPUs, which excel at dense, regular matrix operations.

Key features:
- **Massively parallel:** Thousands of independent processing tiles, each with local SRAM
- **In-Processor Memory (IPM):** Large on-chip SRAM (up to 900 MB per chip in later generations) to reduce reliance on external DRAM
- **Sparse compute optimization:** Designed to efficiently handle the sparsity patterns common in ML models
- **Poplar SDK:** Custom software stack and compiler for programming the IPU

### Products Shipped
- **Mk1 IPU (GC2; Colossus):** First generation, 2018
- **Mk2 IPU (GC200; Bow):** Second generation, 2022. First chip to use TSMC's wafer-on-wafer 3D technology.
- **IPU-POD systems:** Rack-scale systems for data center deployment

## What Went Wrong

Graphcore's story is one of the most instructive failures in AI hardware. Despite world-class founders, strong technology, and $730M in funding, the company could not achieve commercial liftoff.

1. **The CUDA moat proved insurmountable.** Graphcore's Poplar SDK, while technically capable, required developers to rewrite their code. Most AI researchers and engineers had already committed to CUDA/PyTorch on Nvidia GPUs. The switching cost was simply too high for most customers, even when IPU performance was competitive.

2. **Timing mismatch.** Graphcore designed the IPU for the ML workloads of 2016-2018 (CNNs, RNNs, sparse models). The transformer revolution (2020-2023) shifted the industry toward dense matrix operations where GPUs excel. The IPU's advantages in sparse computation became less relevant as transformers became the dominant architecture.

3. **Revenue never materialized at scale.** Despite winning some research partnerships (Microsoft Azure listed IPU instances for a time), Graphcore reportedly generated only tens of millions in revenue -- a fraction of what was needed to sustain a chip company burning $200M+ annually.

4. **Nvidia's competitive response was relentless.** Every time Graphcore shipped a new generation, Nvidia had already leapfrogged with A100, H100, etc. The pace of Nvidia's product cadence made it nearly impossible for any startup to maintain a performance lead.

5. **Loss of China market.** U.S. export controls on advanced AI chips affected Graphcore's ability to sell in China, which had been one of its most promising markets.

## The SoftBank Acquisition

In July 2024, SoftBank acquired Graphcore for a reported ~$500M, though Graphcore stated this figure was inaccurate without disclosing the actual price. Key dynamics:

- **Fire sale pricing:** $500M is less than the ~$730M total invested, and a fraction of the $2.8B peak valuation. Investors took significant losses.
- **SoftBank's Arm connection:** SoftBank also owns Arm Holdings. The likely strategic rationale is integrating Graphcore's AI accelerator IP with Arm's CPU cores to compete against Nvidia in the data center.
- **Graphcore continues operating** as a wholly owned SoftBank subsidiary, maintaining the Graphcore brand and Bristol headquarters.

## Lessons for AI Hardware Startups

Graphcore's trajectory offers critical lessons for every company in this database:

1. **Software ecosystem > silicon performance.** A technically superior chip means nothing if developers will not adopt your programming model. CUDA's dominance is not about Nvidia's hardware -- it is about the millions of developers, libraries, tutorials, and production codebases built on CUDA.

2. **Architecture bets can age badly.** Designing a chip takes 3-5 years. If the AI landscape shifts during that period (as it did with the transformer revolution), your chip may be optimized for the wrong workload.

3. **$730M is not enough if burn rate is too high.** Graphcore burned through nearly three-quarters of a billion dollars without achieving product-market fit. AI chip startups must manage burn rate ruthlessly and find revenue early.

4. **Even great founders can lose.** Toon and Knowles had previously built and sold two successful chip companies. Pedigree is necessary but not sufficient.

## Comparable Companies

- Habana Labs (acquired by Intel for $2B in 2019; Intel later de-emphasized the products)
- Cerebras (wafer-scale; still independent and growing)
- SambaNova (dataflow architecture; struggling commercially)
- Wave Computing (filed for bankruptcy in 2020; cautionary tale)

---

*Profile compiled 2026-03-20. Sources: [TechCrunch](https://techcrunch.com/2024/07/11/softbank-acquires-uk-ai-chipmaker-graphcore/), [TuringPost](https://www.turingpost.com/p/graphcore-unicorn-softbank-acquisition-happened), [Wikipedia](https://en.wikipedia.org/wiki/Graphcore), [EE Times](https://www.eetimes.com/ai-chip-startup-graphcore-acquired-by-softbank/), [TrendForce](https://www.trendforce.com/news/2024/07/16/news-softbank-acquired-graphcore-hinting-at-a-battle-between-ipu-and-gpu/).*
