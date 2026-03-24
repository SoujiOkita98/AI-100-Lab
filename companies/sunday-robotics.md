---
website: https://www.sunday.ai
sector: Consumer Robotics / Household Automation
product: Memo (autonomous household robot)
founded: ~202
headquarters: California, USA (exact city unconfirmed; likely San Francisco Bay Area)
founders:
- name: Tony Zhao
  role: Co-founder & CEO
  background: 'Stanford CS PhD candidate (advisor: Chelsea Finn); BS in EECS from UC Berkeley (2021, worked with Sergey Levine
    and Dan Klein); Stanford Robotics Fellow 2022-23; creator of ALOHA and ACT (Action Chunking with Transformers)'
  origin: Chinese-American
- name: Cheng Chi
  role: Co-founder & CTO
  background: 'Columbia University PhD student (advisor: Shuran Song, later moved to Stanford); creator of Diffusion Policy
    and UMI (Universal Manipulation Interface); RSS 2024 Best Systems Paper Finalist for UMI'
  origin: Chinese
team_size: 70+ engineers and researchers
team_origins:
- Stanford University
- Tesla
- DeepMind
- Waymo
- Meta
- OpenAI
- Apple
funding_rounds:
- stage: Seed / Series A (emerged from stealth)
  date: November 2025
  amount_m: 35.0
  lead_investors:
  - Benchmark
  - Conviction
- stage: Series B
  date: March 12, 2026
  amount_m: 165.0
  valuation_m: 1150.0
  lead_investors:
  - Coatue (Thomas Laffont joined board)
  other_investors:
  - Bain Capital Ventures
  - Fidelity Management & Research Company
  - Tiger Global
  - Benchmark (follow-on)
  - Conviction (follow-on)
  - Xtal Ventures
status: Pre-revenue; beta deployment planned for late 2026
last_updated: 2026-03-20
one_liner: Sunday is building Memo, an autonomous household robot designed to help families with everyday chores such as doing
  dishes, laundry, and tidying up
website_verified: true
crunchbase: https://www.crunchbase.com/organization/sunday-robotics
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/sunday-robotics/
name: Sunday
linkedin_verified: true
total_raised_m: 200.0
latest_valuation_m: 1150.0
---

# Sunday Robotics

## Overview

Sunday is building Memo, an autonomous household robot designed to help families with everyday chores such as doing dishes, laundry, and tidying up. The company was founded by two Stanford-affiliated PhD roboticists -- Tony Zhao and Cheng Chi -- who are responsible for some of the most influential recent advances in robot learning, including ALOHA, Diffusion Policy, Action Chunking with Transformers (ACT), and UMI (Universal Manipulation Interface).

The company emerged from stealth in November 2025 and reached unicorn status ($1.15B valuation) just four months later with an oversubscribed $165M Series B led by Coatue in March 2026.

## Founders and Academic Lineage

**Tony Zhao (CEO)** studied EECS at UC Berkeley (BS 2021), working under Sergey Levine and Dan Klein, then pursued a PhD in CS at Stanford under Chelsea Finn before dropping out to start Sunday. At Stanford, he created ALOHA -- a low-cost (~$20K) open-source bimanual teleoperation system -- and ACT (Action Chunking with Transformers), which predicts sequences of actions rather than single steps, dramatically improving imitation learning performance. He and Chi first connected on X (Twitter) after noticing each other's papers, published roughly a month apart.

**Cheng Chi (CTO)** began his PhD at Columbia under Shuran Song, later moving to Stanford when Song joined Stanford's faculty. Chi authored Diffusion Policy (RSS 2023, later IJRR 2024), which applied diffusion models to visuomotor policy learning and outperformed prior state-of-the-art by an average of 46.9% across benchmarks. He also developed UMI (Universal Manipulation Interface), a framework for collecting manipulation training data from human demonstrations, which was a Best Systems Paper Finalist at RSS 2024.

Together, their academic work (ALOHA, Diffusion Policy, ACT, UMI) forms much of the modern foundation for learning-based robot manipulation. They started Sunday in a garage, using 3D printers to build prototype hardware.

## The Robot: Memo

Memo is a wheeled mobile manipulator with a soft silicone-clad exterior, purpose-built for residential environments. Key design choices:

- **Wheeled base** (not bipedal legs) -- prioritizes stability and reliability in home settings over humanoid form factor
- **Soft silicone exterior** -- designed for safe operation around families and children
- **Purpose-built residential hardware** -- engineered specifically for the home, not adapted from industrial or lab robots

Target tasks include dishes, laundry, clearing tables, and general tidying. The company prioritizes robustness over feature breadth -- doing a few tasks reliably rather than many tasks poorly.

## Data Collection: The Skill Capture Glove

Sunday's most distinctive technical innovation is its **Skill Capture Glove** system, a low-cost (~$200-$400 per unit) wearable that records human hand movements during household tasks. This is the evolution of Chi's UMI research into a commercial data pipeline.

- Over **2,000 gloves** shipped to a distributed network of U.S.-based "Memory Developers" -- everyday people who wear the gloves while performing chores in their own homes
- Data collected from **500+ real homes** across diverse household environments
- Approximately **10 million real-world household episodes** collected to date
- Cost is roughly **100x cheaper** per data collection unit compared to traditional teleoperation or in-lab approaches

This crowdsourced, in-home data collection strategy is a key differentiator. Rather than relying on simulation or lab demonstrations, Sunday trains Memo on the messy reality of actual homes -- different kitchens, different dish types, different family routines. This approach directly addresses the sim-to-real gap that has historically plagued household robotics.

## Business Model

- **Target price**: Under $10,000 at scale (current hand-built unit cost is ~$20,000; large-scale manufacturing expected to reduce costs by at least 50%)
- **Beta program**: 50 "Founding Family" households selected for invite-only beta in late 2026 (free for participants)
- **Revenue model**: Consumer hardware sales (specifics on subscription/service components not yet disclosed)
- **Current status**: Pre-revenue; focused on transitioning from demos to real-world deployment

The pricing target of sub-$10K positions Memo in a consumer-accessible range, though still a significant purchase. Exact go-to-market details (direct sales, retail partnerships, financing options) have not been publicly disclosed.

## What Makes Sunday Interesting

1. **Founder-research fit is exceptional.** Zhao and Chi literally wrote the papers (ALOHA, Diffusion Policy, ACT, UMI) that much of the robotics industry now builds on. They are not applying someone else's research -- they are commercializing their own foundational work.

2. **Data moat via Skill Capture Gloves.** The crowdsourced, in-home data collection pipeline is a genuine structural advantage. 10 million real-world episodes from 500+ homes is a dataset that would be extremely expensive and time-consuming for competitors to replicate. The 100x cost reduction in data collection could compound into a widening lead.

3. **Pragmatic hardware choices.** Choosing wheels over legs, and a soft-bodied design over rigid humanoid form, signals a team optimizing for near-term household deployment rather than chasing humanoid hype. This is a bet that practical utility matters more than visual impressiveness.

4. **Speed of execution.** Stealth to unicorn in four months ($35M in November 2025 to $1.15B in March 2026) reflects strong investor conviction. The oversubscribed Series B and the caliber of investors (Coatue, Bain Capital Ventures, Fidelity, Tiger Global, Benchmark) suggest the demos and data are compelling behind closed doors.

5. **Talent density.** 70+ engineers from Stanford, Tesla, DeepMind, Waymo, Meta, OpenAI, and Apple. Reports indicate Sunday has been attracting AI talent away from Tesla's Optimus program specifically.

## Key Risks and Open Questions

- **No product in market yet.** Memo has not shipped to any customer. The Thanksgiving 2026 beta timeline is ambitious for a robot that must operate safely and reliably in uncontrolled home environments.
- **Hardware manufacturing at scale** is a different challenge than building prototypes in a garage. Moving from ~$20K hand-built units to sub-$10K mass production requires supply chain, manufacturing, and quality control capabilities the team has not yet demonstrated.
- **Consumer robotics has a graveyard** of well-funded failures (Jibo, Kuri, Anki Vector). The home environment is notoriously unstructured and unforgiving.
- **Regulatory and safety considerations** for an autonomous robot operating in homes with children, pets, and fragile items are non-trivial and not yet publicly addressed.
- **Business model specifics** remain thin -- pricing, distribution, ongoing service/support costs, and unit economics are largely undisclosed.

## Sources

- [Sunday Raises $165M to Launch First Autonomous Robots by Thanksgiving (GlobeNewsWire)](https://www.globenewswire.com/news-release/2026/03/12/3254877/0/en/Sunday-Raises-165M-to-Launch-First-Autonomous-Robots-by-Thanksgiving.html)
- [Humanoid robotics maker Sunday reaches $1.15B valuation (TechCrunch)](https://techcrunch.com/2026/03/12/humanoid-robotics-maker-sunday-reaches-1-15b-valuation-to-build-household-robots/)
- [Dishwashing Home Robot Maker Sunday Hits $1.15 Billion Valuation (Bloomberg)](https://www.bloomberg.com/news/articles/2026-03-12/dishwashing-home-robot-maker-sunday-hits-1-15-billion-valuation)
- [Sunday raises $165M at $1.15B valuation (SiliconANGLE)](https://siliconangle.com/2026/03/12/sunday-raises-165m-1-15b-valuation-launch-memo-household-robot/)
- [Household Robot Maker Sunday Raise $165M (The AI Insider)](https://theaiinsider.tech/2026/03/13/household-robot-maker-sunday-raise-165m-in-series-b-funding-with-1-15b-valuation/)
- [Sunday Emerges from Stealth with $35M (The AI Insider)](https://theaiinsider.tech/2025/11/20/sunday-emerges-from-stealth-with-35m-for-household-robot-called-memo/)
- [Sunday Launches Memo (Yahoo Finance / GlobeNewsWire)](https://finance.yahoo.com/news/sunday-launches-memo-robot-actually-170000803.html)
- [Robots, Finally at Home (Bain Capital Ventures)](https://baincapitalventures.com/insight/robots-finally-at-home/)
- [Sunday Unveils Memo: Wheeled Domestic Robot (Humanoids Daily)](https://www.humanoidsdaily.com/news/sunday-unveils-memo-a-wheeled-domestic-robot-that-learns-from-200-gloves)
- [DeepMind, Tesla Vets Emerge From Stealth (Humanoids Daily)](https://www.humanoidsdaily.com/news/deepmind-tesla-vets-emerge-from-stealth-with-sunday-robotics-backed-by-conviction)
- [Tesla is bleeding AI talent to a small new robotics start-up (Electrek)](https://electrek.co/2025/11/24/tesla-bleeding-ai-talent-small-new-robotics-start-up/)
- [Tony Zhao academic page](https://tonyzhaozh.github.io/)
- [Cheng Chi academic page](https://cheng-chi.github.io/)
- [Diffusion Policy (Columbia)](https://diffusion-policy.cs.columbia.edu/)
- [Mobile ALOHA project page](https://mobile-aloha.github.io/)
- [Sunday Robotics Raises $165M Series B (MLQ)](https://mlq.ai/news/sunday-robotics-raises-165-million-series-b-at-115-billion-valuation-for-home-robot-launch/)
