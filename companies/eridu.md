---
name: Eridu
status: active
founded: 2024
website: https://eridu.ai
sector:
- AI infrastructure
- networking
- semiconductors
one_liner: AI networking startup building custom silicon and switching architecture to eliminate the networking bottleneck
  in GPU data centers.
logo: null
total_raised_m: 230
latest_valuation_m: null
funding_rounds:
- stage: Seed
  date: 2024
  amount_m: 30.0
  source: https://techcrunch.com/2026/03/10/ai-network-startup-eridu-emerges-from-stealth-with-hefty-200m-series-a/
  notes: Pre-stealth seed funding.
- stage: Series A
  date: 2026-03
  amount_m: 200.0
  lead_investors:
  - Socratic Partners
  - John Doerr
  - Matter Venture Partners
  source: https://techcrunch.com/2026/03/10/ai-network-startup-eridu-emerges-from-stealth-with-hefty-200m-series-a/
  notes: Oversubscribed. Hudson River Trading, Capricorn Investment Group, SBVA, MediaTek, Bosch Ventures, TDK Ventures, Eclipse,
    and VentureTech Alliance (TSMC investing vehicle) also participated.
founders:
- name: Drew Perkins
  role: CEO & Co-Founder
  background: Networking industry veteran since the 1980s. Helped create Point-to-Point Protocol (PPP), a key part of TCP/IP.
    Co-founded Lightera Networks (sold to Ciena for $500M+, 1999). Co-founded Infinera (IPO'd, later sold to Nokia for $2.3B
    in 2025).
  origin: American
- name: Omar Hassen
  role: Chief Product Officer & Co-Founder
  background: Deep networking chip design experience. Previously held senior roles at Broadcom, Marvell, and International
    Rectifier managing chip design divisions.
  origin: Limited public information
- name: Mike Capuano
  role: Chief Business Development & Marketing Officer & Co-Founder
  background: Most recently SVP of Business Development at Ventana Systems (RISC-V server chips). Background in semiconductor
    business development.
  origin: American
business_model: Hardware + software infrastructure. Eridu is building custom networking silicon (chips) and a high-radix switching
  architecture designed specifically for AI data center workloads. The company rethinks computer networking from scratch,
  starting with the silicon, integrating more networking functionality directly into new chips optimized for massive GPU clusters.
  Target customers are hyperscalers, AI labs, and data center operators running large-scale generative AI training. Revenue
  model likely hardware sales plus software licensing.
sources:
- https://techcrunch.com/2026/03/10/ai-network-startup-eridu-emerges-from-stealth-with-hefty-200m-series-a/
- https://eridu.ai/pr/eridu-emerges-from-stealth-with-over-200m-in-funding/
- https://www.networkworld.com/article/4143119/eridu-exits-stealth-with-200m-to-rebuild-ai-networking.html
- https://www.nextplatform.com/connect/2026/03/11/eridu-cuts-to-the-ai-networking-chase-with-high-radix-switch-system/5208996
- https://techfundingnews.com/eridu-stealth-200m-network-wall-ai/
last_updated: 2026-03-20
confidence: medium
website_verified: true
crunchbase: https://www.crunchbase.com/organization/eridu
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/eridu-ai
headquarters: San Francisco, CA
linkedin_verified: true
---

# Eridu

## Overview

Eridu is an AI networking startup that emerged from stealth in March 2026 with $230 million in total funding ($200M oversubscribed Series A + $30M seed). Founded in 2024, the company is building custom networking silicon and switching architecture designed to eliminate the "network wall" -- the growing bottleneck where GPU compute has outpaced data center networking capacity.

The company was founded by Drew Perkins, a networking industry legend who co-created the Point-to-Point Protocol and founded two companies that collectively exited for nearly $3 billion (Lightera to Ciena, Infinera IPO then to Nokia).

## Funding story

**2024 -- ~$30M Seed.** Pre-stealth funding to begin chip and architecture development.

**March 2026 -- $200M Series A (oversubscribed).** Led by Socratic Partners, legendary VC John Doerr, and Matter Venture Partners. The investor list is strategically significant: Hudson River Trading (quantitative trading firm needing fast networks), MediaTek, Bosch Ventures, TDK Ventures, and critically VentureTech Alliance (TSMC's investing vehicle). Having TSMC-affiliated capital in a chip startup is a strong signal of manufacturing pathway viability.

## Team

- **Drew Perkins (CEO):** The reason this company got $200M from stealth. Co-creator of PPP protocol. Founded Lightera Networks ($500M+ exit to Ciena) and Infinera ($2.3B exit to Nokia). Decades of networking industry experience.
- **Omar Hassen (CPO):** Chip design veteran from Broadcom and Marvell. Brings the semiconductor execution experience.
- **Mike Capuano (CBDO):** From Ventana Systems (RISC-V). Semiconductor go-to-market expertise.

## What makes them interesting

1. **Networking is the real bottleneck.** Everyone talks about GPU supply constraints, but increasingly the binding constraint in AI data centers is the network connecting those GPUs. Training runs on 100K+ GPU clusters are limited by inter-node bandwidth, not compute. Eridu is targeting the right problem.

2. **Founder credibility is exceptional.** Drew Perkins has done this before -- twice -- with combined exits of ~$3B. When a serial networking founder with this track record says he needs to rethink networking from scratch, investors listen.

3. **Full-stack approach (silicon + switching).** Eridu is not just writing software on top of existing network hardware. They are designing new chips and new switching architectures from the ground up. This is harder and slower but potentially more defensible.

4. **Strategic investor alignment.** TSMC-affiliated capital (VentureTech Alliance) suggests a credible chip manufacturing path. MediaTek and Bosch bring additional semiconductor ecosystem connections.

5. **Market timing.** As AI clusters scale to 100K+ GPUs, the demand for purpose-built AI networking is inflecting. Eridu is well-positioned if its silicon delivers on performance claims.

## Notes

- **Hardware risk.** Custom chip development is expensive, time-consuming, and risky. The path from $200M raise to shipping silicon is 18-24 months at minimum.
- **Valuation not disclosed.** Unusual for a round this size. May indicate the founders wanted to avoid valuation-driven pressure.
- **Competition:** Nvidia (NVLink/NVSwitch), Broadcom, and Arista Networks dominate current AI networking. Eridu is betting the incumbents' architectures are fundamentally inadequate for next-generation AI scale. Nexthop AI ($500M raise) is another well-funded competitor in this space.
