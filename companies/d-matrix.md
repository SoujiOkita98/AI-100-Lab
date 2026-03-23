---
company: d-Matrix
legal_name: d-Matrix Corp.
founded: 2019
headquarters: Santa Clara, California, USA
sector: AI Hardware / Semiconductors (In-Memory Compute)
stage: Growth (Series C)
latest_valuation: $2 billion (Series C, November 2025)
total_funding: ~$450 million
employees: ~200 (estimate)
website: https://www.d-matrix.ai
last_updated: 2026-03-20
one_liner: In-memory AI inference accelerator chips — Corsair series targeting 10x faster inference than GPUs. $2B valuation.
website_verified: true
linkedin: https://www.linkedin.com/company/d-matrix
crunchbase: https://www.crunchbase.com/organization/d-matrix
crunchbase_verified: true
twitter: '@dMatrix_AI'
founders:
- name: Sid Sheth
  role: CEO
  background: MSEE from Purdue. Former SVP/GM at Inphi Corporation (grew to $1B+). Prior at NetLogic Microsystems (now Broadcom)
    and Intel.
  origin: Indian-American
- name: Sudeep Bhoja
  role: CTO
  background: Semiconductor industry veteran.
  origin: Indian-American
total_raised_m: 450
funding_rounds:
- stage: Series A
  date: '2021'
  amount_m: 65
  lead_investors:
  - Undisclosed
  source: https://www.crunchbase.com/organization/d-matrix
- stage: Series B
  date: 2023-09
  amount_m: 110
  lead_investors:
  - Temasek
  source: https://www.crunchbase.com/organization/d-matrix
- stage: Series C
  date: 2025-11
  amount_m: 275
  lead_investors:
  - Bullhound Capital
  - Triatomic Capital
  - Temasek
  source: https://www.crunchbase.com/organization/d-matrix
name: d-Matrix
linkedin_verified: true
---

# d-Matrix

## Overview

d-Matrix is building an AI inference accelerator based on Digital In-Memory Compute (DIMC) -- a chip architecture that performs AI computations (specifically matrix multiplications) directly inside the memory circuits rather than shuttling data back and forth between separate compute and memory units. This approach attacks the "memory wall" problem that limits GPU performance on inference workloads, where the bottleneck is often data movement rather than raw compute.

The company's first product, the Corsair inference platform, is a PCIe card containing two custom chiplets, each with 1 GB of SRAM. d-Matrix claims Corsair can perform 9,600 trillion operations per second (TOPS) in MXINT4 format, delivering dramatically better inference performance-per-watt than Nvidia GPUs.

## Founders and Team

| Name | Role | Background |
|---|---|---|
| **Sid Sheth** | Co-Founder & CEO | 20+ years in semiconductor innovation. Previously SVP & GM of the Networking Business Unit at Inphi Corporation, where he grew the networking division into a $200M business before Inphi's $10B acquisition by Marvell Technology. Prior to Inphi, held worldwide marketing roles at NetLogic Microsystems (now Broadcom). MSEE from Purdue University. |
| **Sudeep Bhoja** | Co-Founder & CTO | Deep technical background in high-speed chip design. Previously at Inphi (with Sheth) working on data center interconnect technology. |

The co-founding team's Inphi connection is notable: both founders come from a company that was successfully acquired by Marvell for $10B, giving them firsthand experience building and scaling a data center semiconductor business.

## Funding History

| Round | Date | Amount | Valuation | Lead Investor(s) | Notes |
|---|---|---|---|---|---|
| Series A | ~2021 | ~$65M (est.) | Undisclosed | Undisclosed | Early funding to develop DIMC technology |
| Series B | Sep 2023 | $110M | Undisclosed | Temasek (Singapore) | Funds to commercialize Corsair platform |
| Series C | Nov 2025 | $275M | $2B | Bullhound Capital, Triatomic Capital, Temasek | Brings total to ~$450M |

**Notable investors:** Temasek (Singapore sovereign wealth fund), Qatar Investment Authority (QIA), EDBI (Singapore), M12 (Microsoft's Venture Fund), Nautilus Venture Partners, Industry Ventures, Mirae Asset.

The Microsoft involvement via M12 is strategically significant -- it signals potential integration with Azure infrastructure.

## Technology: Corsair and Digital In-Memory Compute

Traditional AI accelerators (including GPUs) suffer from the "memory wall": data must be moved from memory (DRAM/HBM) to compute units and back, consuming enormous energy and creating latency bottlenecks. d-Matrix's approach embeds compute logic directly into the SRAM cells:

- **Corsair platform:** PCIe card with two custom chiplets, each containing 1 GB of SRAM with embedded compute
- **Chiplet architecture:** Uses a modular chiplet design for better yields and scalability
- **9,600 TOPS** in MXINT4 format
- **Ultra-low latency:** Designed for real-time, latency-sensitive inference (financial services, recommendation engines, conversational AI)
- **Energy efficiency:** Dramatically reduces data movement energy -- the dominant power cost in inference

**Shipping status:** Corsair has been sampled to customers as of late 2024. The company launched its first AI chip publicly in November 2024 with Microsoft as a backer.

## Business Model

d-Matrix sells Corsair inference accelerator cards and systems to enterprises and cloud providers, targeting workloads where inference latency and energy efficiency are critical. Key target markets include:

- Cloud inference (competing with Nvidia H100/B200 for LLM serving)
- Financial services (ultra-low-latency trading and risk models)
- Telecommunications
- Enterprise AI deployments

## What Makes d-Matrix Interesting

1. **In-memory compute is the right architectural insight for inference.** The memory wall is arguably the single biggest bottleneck in AI inference, and d-Matrix has the most mature in-memory compute solution in the market. While Nvidia addresses this with ever-larger HBM stacks, d-Matrix attacks the root cause by eliminating data movement entirely.

2. **Sovereign wealth fund backing signals long-term conviction.** Having Temasek, QIA, and EDBI as investors -- entities with decade-long investment horizons -- provides patient capital that hardware startups desperately need. These are not VCs who need a 5-year exit.

3. **Experienced semiconductor operators, not first-time founders.** Sheth and Bhoja built and sold a $10B semiconductor business at Inphi/Marvell. They know how to navigate TSMC relationships, manage tapeouts, and sell to hyperscaler procurement teams. This operational experience is rare among AI chip startups.

4. **Microsoft as a strategic backer.** M12's investment and Microsoft's public endorsement of d-Matrix suggests potential Azure integration -- a distribution channel that could be transformative.

5. **Chiplet architecture future-proofs the design.** Using chiplets rather than monolithic dies improves manufacturing yields and allows d-Matrix to scale performance by adding more chiplets without full redesigns.

## Key Risks

- **Nvidia's HBM strategy competes indirectly.** Nvidia is addressing memory bottlenecks with massive HBM stacks (up to 192GB on B200). While this is architecturally inferior to in-memory compute, Nvidia's ecosystem advantages may make "good enough" memory bandwidth sufficient for most customers.
- **Software ecosystem.** Developers must port workloads to d-Matrix's software stack. The CUDA moat remains the biggest barrier for all Nvidia alternatives.
- **Scale of production.** Moving from samples and early deployments to high-volume manufacturing is where many chip startups stumble.
- **In-memory compute is still early.** The technology is proven in concept but has limited production track record at datacenter scale.

## Comparable Companies

- Cerebras (wafer-scale; different approach to memory bandwidth)
- Groq (acquired by Nvidia; deterministic inference architecture)
- Etched (transformer-specific ASIC for inference)
- Positron AI (inference-focused; FPGA-based first gen)
- EnCharge AI (analog in-memory compute; earlier stage)

---

*Profile compiled 2026-03-20. Sources: [SiliconANGLE](https://siliconangle.com/2025/11/12/chip-startup-d-matrix-raises-275m-speed-inference-memory-compute/), [d-Matrix Press Release](https://www.d-matrix.ai/announcements/d-matrix-raises-275-million-to-power-the-age-of-ai-inference/), [DCD](https://www.datacenterdynamics.com/en/news/chip-startup-d-matrix-raises-275m-against-2bn-valuation/), [BusinessWire](https://www.businesswire.com/news/home/20230906216008/en/d-Matrix-Announces-110-Million-in-Series-B-Funding), [American Bazaar](https://americanbazaaronline.com/2024/11/22/microsoft-backed-startup-d-matrix-introduces-its-first-ai-chip-20393/).*
