---
company: Tenstorrent
legal_name: Tenstorrent Inc.
founded: 2016
headquarters: Toronto, Ontario, Canada (with offices in Austin, TX and Santa Clara, CA)
sector: AI Hardware / Semiconductors / RISC-V IP Licensing
stage: Growth (Series D+)
latest_valuation: $3.2 billion (2025 round led by Fidelity)
total_funding: ~$1.18 billion (across 10 rounds)
employees: ~400+ (estimate)
website: https://tenstorrent.com
last_updated: 2026-03-20
one_liner: Tenstorrent is a Canadian AI chip and RISC-V processor company led by legendary chip architect Jim Keller
website_verified: true
crunchbase: https://www.crunchbase.com/organization/tenstorrent
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/tenstorrent-inc.
---

# Tenstorrent

## Overview

Tenstorrent is a Canadian AI chip and RISC-V processor company led by legendary chip architect Jim Keller. The company has a dual strategy: (1) building AI accelerator chips based on its proprietary Tensix compute cores, and (2) licensing high-performance RISC-V CPU IP (the Ascalon core) to customers who want to build their own custom silicon. This combination positions Tenstorrent as both an AI chip competitor to Nvidia and a CPU IP licensor competing with Arm Holdings -- a unique dual positioning in the semiconductor industry.

Tenstorrent's AI accelerators (Grayskull, Wormhole, and the upcoming Blackhole) use a novel dataflow architecture that routes data directly between compute cores rather than through a central memory hierarchy, reducing latency and power consumption for AI workloads.

## Founders and Team

| Name | Role | Background |
|---|---|---|
| **Ljubisa Bajic** | Co-Founder & CTO (formerly CEO) | Grew up in Serbia (then Yugoslavia), attended high school in Moscow for its math programs, moved to Canada in 1985 to study electrical engineering. Worked at VLSI Technology and Nvidia in Silicon Valley, then at AMD (2014) where he first worked under Jim Keller. Founded Tenstorrent in 2016. Swapped to CTO role when Keller became CEO in 2025. |
| **Ivan Hamer** | Co-Founder | Limited public profile. Co-founded with Bajic and Trajkovic. |
| **Milos Trajkovic** | Co-Founder | Limited public profile. Co-founded alongside Bajic. |
| **Jim Keller** | CEO (joined 2021 as CTO; became CEO 2025) | One of the most accomplished chip architects alive. Led or contributed to: AMD K8 (Athlon 64), AMD Zen (Ryzen), Apple A4/A5 processors, Tesla's Full Self-Driving chip, and was SVP at Intel. Joined Tenstorrent as CTO in January 2021; became CEO in 2025. His involvement alone is the company's strongest recruiting and fundraising asset. |

**Note on Jim Keller:** Keller has left Tenstorrent's co-founder Ljubisa Bajic as the original founder who recruited Keller. Bajic and Keller first worked together at AMD, where Bajic was on the team Keller led. Their collaboration at Tenstorrent represents a reversal of that dynamic.

## Funding History

| Round | Date | Amount | Valuation | Lead/Notable Investors |
|---|---|---|---|---|
| Early rounds | 2016-2020 | ~$87M combined | Undisclosed | Real Ventures, Eclipse Ventures |
| Series C | May 2021 | $200M | ~$1B (unicorn) | Fidelity Management & Research |
| Series D | Dec 2024 | $693M | $2.6B | Samsung Securities, AFW Partners, XTX Markets, Bezos Expeditions, Baillie Gifford, Fidelity, LG Electronics, Hyundai Motor Group, Export Development Canada, Healthcare of Ontario Pension Plan |
| Follow-on | 2025 | ~$200M+ (est.) | $3.2B | Fidelity Management (led) |

**Total raised:** ~$1.18 billion across 10 rounds.

**Notable investors:** Fidelity, Bezos Expeditions (Jeff Bezos), Samsung, LG Electronics, Hyundai Motor Group, Baillie Gifford, XTX Markets, Export Development Canada.

**Contracts:** Over $150M in commercial contracts from LG Electronics, Hyundai Motor Group, Samsung Electronics, and Japanese partners (selected for Japan's national AI chiplet initiative).

## Technology & Products

### AI Accelerators (Tensix Architecture)

Tenstorrent's AI chips use a dataflow architecture built around "Tensix" compute cores -- small, programmable tensor processing units that communicate directly with each other via on-chip mesh networks.

| Generation | Chip | Status | Key Specs |
|---|---|---|---|
| Gen 1 | Grayskull | Shipped (dev kits) | First production silicon; proved out Tensix architecture |
| Gen 2 | Wormhole | Shipping (dev kits + workstations) | Native chip-to-chip networking; scales from 1 to many chips without external switches. TT-LoudBox ($12K) and TT-QuietBox ($15K) workstations |
| Gen 3 | Blackhole | In development | Next-generation; details limited |

### RISC-V CPU IP (Ascalon)

Tenstorrent's Ascalon-X is an 8-wide decode, out-of-order, superscalar RISC-V CPU core designed to compete directly with Arm's high-performance Cortex-X series. The engineering team includes people from Apple's M-series and AMD's Zen CPU projects.

This is the "Arm killer" play: offering comparable or superior CPU performance on an open ISA (RISC-V) that does not require licensing fees to Arm Holdings. Customers like LG, Hyundai, and Samsung can build custom SoCs using Tenstorrent's CPU + AI cores without Arm royalties.

## Business Model

Tenstorrent operates three revenue streams:

1. **AI accelerator hardware:** Selling Wormhole/Blackhole dev kits and systems to AI developers and enterprises.
2. **RISC-V CPU IP licensing:** Licensing Ascalon CPU cores and Tensix AI cores to customers building custom chips (similar to Arm's licensing model, but on RISC-V).
3. **Custom silicon partnerships:** Working with automotive (Hyundai, LG), consumer electronics (Samsung), and sovereign AI programs (Japan) to co-develop application-specific chips.

## What Makes Tenstorrent Interesting

1. **Jim Keller is the ultimate semiconductor credential.** Keller has shipped more transformative chip architectures than arguably anyone alive (AMD K8, Zen, Apple A-series, Tesla FSD). His decision to leave all of these opportunities and go all-in on Tenstorrent is itself a powerful signal about the company's technology.

2. **The dual AI + RISC-V strategy is unique.** No other AI chip startup also licenses CPU IP. If RISC-V displaces Arm in even a fraction of the data center and edge computing market, the CPU licensing business alone could justify Tenstorrent's valuation -- with the AI accelerator business as upside.

3. **Open ecosystem philosophy vs. Nvidia's CUDA moat.** Tenstorrent's open-source software stack and RISC-V foundation are a deliberate anti-CUDA strategy. The pitch: avoid vendor lock-in at both the ISA level (RISC-V vs. Arm) and the AI framework level (open stack vs. CUDA).

4. **Sovereign AI and automotive traction.** Being selected for Japan's national AI chip initiative and winning contracts from Hyundai, LG, and Samsung demonstrates real commercial demand, not just VC enthusiasm. The automotive AI chip market is a massive addressable market distinct from the hyperscaler training market where Nvidia dominates.

5. **Canadian roots, global ambitions.** Headquartered in Toronto with strong ties to Canada's AI ecosystem (Vector Institute, University of Toronto). Government backing via Export Development Canada provides non-dilutive capital.

## Key Risks

- **Two-front war:** Competing simultaneously against Nvidia (AI accelerators) and Arm (CPU IP) is extraordinarily ambitious. Either market alone would be a massive challenge.
- **Ecosystem maturity:** RISC-V software ecosystem is still maturing. Customers adopting Ascalon must bet on RISC-V toolchains catching up to Arm's decades-long head start.
- **Shipping at scale:** Wormhole is available as dev kits and workstations, but Tenstorrent has not yet demonstrated datacenter-scale deployments competing directly with Nvidia A100/H100 clusters.
- **Customer concentration in automotive/CE:** Heavy reliance on Korean and Japanese industrial conglomerates.

## Comparable Companies

- Nvidia (dominant AI GPU + CUDA ecosystem)
- Arm Holdings (CPU IP licensing incumbent)
- SiFive (RISC-V CPU IP competitor)
- Cerebras, Groq, SambaNova (AI accelerator competitors)

---

*Profile compiled 2026-03-20. Sources: [Crunchbase/Caproasia](https://www.caproasia.com/2024/12/05/ai-computing-company-tenstorrent-raised-693-million-in-series-d-funding-at-2-6-billion-valuation/), [Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/tenstorrents-risc-v-based-wormhole-ai-accelerators-are-available-for-pre-order-today-pre-built-workstations-start-at-dollar12000), [DCD](https://www.datacenterdynamics.com/en/news/jim-keller-becomes-ceo-of-ai-chip-company-tenstorrent/), [Fortune](https://fortune.com/2021/05/21/tenstorrent-a-i-chips-nvidia-keller-funding/), [EE Times](https://www.eetimes.com/jim-keller-steps-into-ceo-role-at-tenstorrent/), [Digitimes](https://www.digitimes.com/news/a20250911PD235/tenstorrent-jim-keller-risc-v-semicon-2025-taiwan.html).*
