---
company: Positron AI
legal_name: Positron AI Inc.
founded: 2023
headquarters: Austin, Texas, USA
sector: AI Hardware / Semiconductors (Inference)
stage: Growth (Series B)
latest_valuation: $1 billion+ (Series B, February 2026)
total_funding: ~$305 million
employees: ~50-100 (estimate)
website: https://www.positron.ai
last_updated: 2026-03-20
one_liner: Positron AI is building energy-efficient, Made-in-America AI inference hardware
---

# Positron AI

## Overview

Positron AI is building energy-efficient, Made-in-America AI inference hardware. The company's first-generation product, the Atlas system, is built on Intel Altera FPGAs and is already shipping to U.S. customers -- making Positron one of the few AI chip startups with production hardware in the field. Positron claims Atlas delivers 70% faster inference at 66% lower power consumption than Nvidia H100/H200 setups, cutting data center CapEx by 50%.

What distinguishes Positron from most AI chip startups is its emphasis on domestic manufacturing: Atlas systems are entirely designed, manufactured, and assembled in the United States, positioning the company at the intersection of AI hardware innovation and the growing "sovereign chip" movement.

## Founders and Team

| Name | Role | Background |
|---|---|---|
| **Thomas Sohmers** | Co-Founder & CTO | Received a Thiel Fellowship in 2013 at age 17, moved to the Bay Area, and founded REX Computing, where he designed processors for mobile base stations and HPC. Later served as Director of Technology Strategy at Groq and held roles at Lambda Labs. Over a decade of semiconductor experience before age 30. |
| **Barrett Woodside** | Co-Founder | Limited public profile. |
| **Edward Kmett** | Co-Founder | Limited public profile. Known in the Haskell programming community. |
| **Mitesh Agrawal** | CEO (joined Feb 2025) | Former COO of Lambda, where he helped scale revenue from $500K to nearly $500M annualized run rate and raised hundreds of millions in capital. Brought in as a professional CEO to lead commercialization. |

The Sohmers-to-Agrawal transition is a classic founder-to-operator handoff: Sohmers (the Thiel Fellow chip prodigy) built the technology, then recruited a proven commercial operator (Agrawal from Lambda) to scale the business.

## Funding History

| Round | Date | Amount | Valuation | Lead/Notable Investors | Notes |
|---|---|---|---|---|---|
| Seed / Series A | Feb 2025 | $23.5M | Undisclosed | Flume Ventures, Valor Equity Partners, Atreides Management, Resilience Reserve | "Made in America" positioning |
| Series A extension | 2025 | $51.6M | Undisclosed | DFJ Growth, Valor Equity Partners, Atreides Management, Flume Ventures | Expanded manufacturing capacity |
| Series B | Feb 2026 | $230M | $1B+ (unicorn) | Arena Private Wealth, Jump Trading, Unless; Qatar Investment Authority (QIA) strategic | Reached unicorn status at ~34 months old |

**Total raised:** ~$305 million.

**Notable investors:**
- **Jump Trading** -- Major quantitative trading firm; suggests inference speed is relevant to financial services
- **Qatar Investment Authority (QIA)** -- Sovereign wealth fund; "sovereign AI" angle
- **Valor Equity Partners** -- Known for Tesla, SpaceX investments
- **Atreides Management** -- Gavin Baker's tech-focused fund
- **DFJ Growth** -- Growth-stage venture firm

## Technology: Atlas and Asimov

### Atlas (1st Generation -- Shipping)
- Built on **Intel Altera FPGAs** (not custom ASICs)
- **Made in USA:** Designed, manufactured, and assembled domestically
- **Performance claims:** 70% faster inference than H100/H200; 66% lower power; 50% CapEx reduction
- **Target:** Transformer model inference
- Can match Nvidia H100 performance at less than one-third the power (company claim)

### Asimov (Next Generation -- In Development)
- Custom silicon chip (moving beyond FPGAs to ASICs)
- Targeting **tapeout in 2026**, production in early 2027
- Expected to significantly surpass Atlas performance
- Manufactured in Arizona

## Business Model

Positron sells inference systems directly to enterprises, cloud providers, and government customers. The "Made in America" positioning opens doors to:
- U.S. government and defense customers with domestic sourcing requirements
- Enterprises seeking supply chain security amid U.S.-China chip tensions
- Sovereign AI deployments (Qatar's QIA investment signals this)

## What Makes Positron Interesting

1. **Actually shipping hardware.** In a market full of vaporware and benchmark slides, Positron has production Atlas systems deployed with U.S. customers. This is a massive credibility advantage.

2. **The FPGA-to-ASIC ladder is smart strategy.** Starting with FPGAs (Atlas) lets Positron get product to market quickly, learn from real deployments, and refine the architecture before committing to the much more expensive and irreversible ASIC tapeout (Asimov). This is the same playbook that worked for several successful chip companies.

3. **Made-in-America is a geopolitical tailwind.** With CHIPS Act funding flowing, U.S.-China chip tensions escalating, and growing demand for domestic AI infrastructure, Positron's all-American supply chain is a genuine competitive advantage for government and defense customers.

4. **Thomas Sohmers is a semiconductor prodigy.** A Thiel Fellow who designed processors at 17, worked at Groq (where he saw LPU inference architecture firsthand), then started Positron. He has been building chips for over a decade and is still under 30.

5. **Financial trading firms as investors and potential customers.** Jump Trading co-leading the Series B signals that ultra-low-latency inference has immediate applications in quantitative finance -- a market with high willingness to pay and demanding performance requirements.

## Key Risks

- **FPGA limitations.** Atlas is built on Intel FPGAs, which are inherently less efficient than custom ASICs for any specific workload. The transition to Asimov (custom ASIC) is critical but introduces significant execution risk.
- **Performance claims need third-party validation.** The 70% faster / 66% lower power claims have not been independently verified in published benchmarks.
- **Small scale.** ~$305M in funding and ~34 months old. Competing against Nvidia's tens of billions in R&D and manufacturing scale.
- **Asimov execution risk.** Tapeout targeted for 2026, production for 2027. First-time ASIC design carries substantial risk.

## Comparable Companies

- Groq (acquired by Nvidia; inference-focused LPU)
- Etched (transformer ASIC; inference-focused, pre-production)
- d-Matrix (in-memory compute; inference-focused)
- Cerebras (wafer-scale; training + inference)

---

*Profile compiled 2026-03-20. Sources: [TechCrunch](https://techcrunch.com/2026/02/04/exclusive-positron-raises-230m-series-b-to-take-on-nvidias-ai-chips/), [BusinessWire](https://www.businesswire.com/news/home/20260204250472/en/Positron-AI-Raises-230-Million-Series-B), [BusinessWire Seed](https://www.businesswire.com/news/home/20250211936199/en/Positron-Secures-23.5M-to-Design-And-Manufacture-Energy-Efficient-Made-In-America-AI-Chips), [Cerebral Valley](https://cerebralvalley.ai/blog/positron-is-pushing-the-boundaries-of-ai-hardware-2THN3t9OrS6n50HC3YyWPu), [DFJ Growth](https://dfjgrowth.com/story/positron-building-the-ai-inference-brain/).*
