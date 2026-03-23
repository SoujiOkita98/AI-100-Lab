---
company: Wayve
legal_name: Wayve Technologies Ltd.
domain: Autonomous Driving / Embodied AI
other_offices:
- Vancouver, Canada
- San Francisco / Silicon Valley, USA
- Germany (testing hub, opened ~2025)
- Japan (testing hub, opened ~2025)
founded: 2017
founders:
- name: Alex Kendall
  role: Co-Founder & CEO
  origin: New Zealand
  education: PhD in Deep Learning, Computer Vision & Robotics, University of Cambridge (Trinity College)
- name: Amar Shah
  role: Co-Founder (departed 2020)
  education: PhD in Machine Learning, University of Cambridge (supervised by Zoubin Ghahramani & Yoshua Bengio)
  prior: Quantitative Strategist, Goldman Sachs
  origin: Indian-British
website: https://wayve.ai
headcount_estimate: ~833 (Jan 2026)
valuation: $8.6B (post-money, Feb 2026)
total_funding: ~$2.5B
stage: Series D
last_updated: 2026-03-20
funding_rounds:
- stage: Seed
  date: 2017-09
  amount_m: 2.15
  lead_investors:
  - Compound
  - Firstminute Capital
  source: https://tracxn.com/d/companies/wayve/__go5_Z58BAb4tRQ9srOvG14MIffdlqtv-Xbv6nI1E3eg/funding-and-investors
- stage: Series A
  date: 2019-11
  amount_m: 20
  lead_investors:
  - Eclipse Ventures
  source: https://en.wikipedia.org/wiki/Wayve
- stage: Series B
  date: 2022-01
  amount_m: 200
  lead_investors:
  - Eclipse Ventures
  source: https://en.wikipedia.org/wiki/Wayve
  notes: Also included D1 Capital, Moore Strategic Ventures, Linse Capital, Microsoft, Virgin Group.
- stage: Series C
  date: 2024-05
  amount_m: 1050
  valuation_m: 2500
  lead_investors:
  - SoftBank Vision Fund 2
  source: https://techcrunch.com/2024/05/06/wayve-raises-1-billion-led-by-softbank-to-take-self-driving-to-cars-and-robots/
  notes: Also included Nvidia, Microsoft, Eclipse Ventures.
- stage: Series D
  date: 2026-02
  amount_m: 1200
  valuation_m: 8600
  lead_investors:
  - Eclipse Ventures
  - Balderton Capital
  - SoftBank Vision Fund 2
  source: https://techcrunch.com/2026/02/24/self-driving-tech-startup-wayve-raises-1-2b-from-nvidia-uber-and-three-automakers/
  notes: Also included Microsoft, Nvidia, Uber, Mercedes-Benz, Nissan, Stellantis, Ontario Teachers', Baillie Gifford.
one_liner: Wayve is a London-based autonomous driving company building end-to-end AI systems that learn to drive from data
  and experience, without relying on hand-coded rules or high-definition maps
website_verified: true
linkedin: https://www.linkedin.com/company/wayve-technologies
crunchbase: https://www.crunchbase.com/organization/wayve
crunchbase_verified: true
twitter: '@wayve_ai'
headquarters: London, United Kingdom
name: Wayve
linkedin_verified: true
---

# Wayve

## Overview

Wayve is a London-based autonomous driving company building end-to-end AI systems that learn to drive from data and experience, without relying on hand-coded rules or high-definition maps. The company brands its approach **AV2.0** -- a departure from the traditional AV1.0 stack of modular perception-planning-control pipelines. Wayve's AI Driver runs entirely on onboard compute and embedded sensors, making it transferable across vehicle platforms, geographies, and driving conditions without city-specific fine-tuning.

Wayve claims to be the first and only AV developer to drive **zero-shot in more than 500 cities** across Europe, North America, and Japan -- meaning no location-specific engineering was required before deployment.

## Founders and Key People

### Alex Kendall -- Co-Founder & CEO

- Born and raised in New Zealand. Attended the University of Cambridge as a Woolf Fisher Scholar.
- Completed his PhD in Deep Learning, Computer Vision, and Robotics under Professor Roberto Cipolla in the Machine Intelligence Laboratory.
- Elected Fellow of Trinity College, Cambridge (2017).
- Awards: BMVA Prize (2018), ELLIS Prize (2019), Royal Academy of Engineering Silver Medal, OBE for services to AI, MIT Technology Review Innovators Under 35.
- Originally served as CTO; became CEO in 2020 after co-founder Amar Shah's departure.

### Amar Shah -- Co-Founder (departed 2020)

- PhD in Machine Learning at Cambridge, supervised by Zoubin Ghahramani (and collaboration with Yoshua Bengio).
- Previously a Quantitative Strategist at Goldman Sachs.
- Served as Wayve's first CEO. Left the company in 2020; later listed as Entrepreneur in Residence at Firstminute Capital.

### Other Senior Leaders

| Name | Title | Background |
|------|-------|------------|
| Jamie Shotton | Chief Scientist | ~10 years at Microsoft as Partner Director of Science; led Mixed Reality & AI Labs. Joined Wayve 2021. |
| Vijay Badrinarayanan | VP, AI | Previously at Magic Leap (US AR/XR unicorn). Joined 2020. Leads applied research in representation learning, simulation, and vision-language models. |
| Dan McCloskey | VP, Hardware | Based in San Francisco. Joined 2021. Leads hardware teams. |
| Pablo Castellanos Garcia | VP, Engineering | Oversees fleet operations, road testing, vehicle maintenance, and fleet management. |

The team skews heavily toward deep learning PhDs and alumni of top computer vision / robotics labs (Cambridge, Oxford, Microsoft Research, DeepMind, etc.).

## Funding History

| Round | Date | Amount | Lead Investors | Notable Participants |
|-------|------|--------|----------------|---------------------|
| Seed | 2018 | Undisclosed | -- | Balderton Capital, Compound |
| Series A | Nov 2019 | $20M | Eclipse Ventures | Balderton Capital |
| Series B | Jan 2022 | $200M | Eclipse Ventures | D1 Capital Partners, Moore Strategic Ventures, Linse Capital |
| Series C | May 2024 | $1.05B | SoftBank Vision Fund 2 | Microsoft, NVIDIA, Eclipse Ventures |
| Series D | Feb 2026 | $1.2B (up to $1.5B with Uber tranche) | Eclipse, Balderton, SoftBank Vision Fund 2 | NVIDIA, Microsoft, Uber, Mercedes-Benz, Nissan, Stellantis, Ontario Teachers' Pension Plan, Baillie Gifford, British Business Bank, Schroders Capital, Icehouse Ventures |

**Total raised: ~$2.5B.** Post-money valuation at Series D: **$8.6 billion**.

The additional $300M from Uber in the Series D is contingent on deploying Wayve-powered robotaxis, starting in London.

## Technology

### End-to-End Learned Driving (AV2.0)

Wayve's core thesis is that autonomous driving should be solved with a single neural network trained end-to-end on driving data, rather than a stack of hand-engineered modules. Their models take raw sensor inputs (cameras, radar) and output driving actions directly.

### Key Technical Components

- **AI Driver**: The production autonomy system. Spans L2+ ("hands off") through L3/L4 ("eyes off") driving capabilities.
- **LINGO-2**: A vision-language-action model (VLAM) -- the first closed-loop driving model tested on public roads that can explain its reasoning in natural language while driving. It generates both driving behavior and textual predictions from the same model.
- **Ghost Gym**: A neural simulator that creates photorealistic 4D worlds for training, testing, and debugging end-to-end AI driving models.
- **No HD Maps Required**: Unlike competitors (Waymo, Cruise), Wayve does not rely on centimeter-accurate pre-mapped environments. This is critical for scalability.

### Compute Infrastructure

Wayve trains on NVIDIA infrastructure and its on-vehicle system runs on NVIDIA's automotive compute platforms. The company has a deep collaboration with NVIDIA on both training and deployment hardware.

## Business Model

Wayve operates as a **horizontal AI platform / software licensor** rather than a vertically integrated robotaxi operator:

1. **OEM Licensing**: Licenses AI Driver to automakers (Nissan, Mercedes-Benz, Stellantis) for integration into production vehicles. Provides tools for customization per vehicle platform and brand.
2. **Robotaxi Platform**: Partners with mobility platforms (Uber) to deploy L4 robotaxis using Wayve's AI on partner-operated fleets, rather than owning and operating its own fleet.
3. **Lower Capital Intensity**: By not owning vehicles or building maps, Wayve avoids the massive capex that sank Cruise and burdens Waymo.

This is analogous to Android vs. Apple in mobile: Wayve wants to be the operating system for autonomy across many OEMs, not a single vertically integrated player.

## Customers and Partnerships

### Nissan (Production Partnership)
- Signed a definitive production partnership in 2025.
- Wayve AI Driver will be integrated into Nissan's next-generation **ProPILOT** ADAS system.
- First mass-produced vehicles expected in Japan and other markets from fiscal year 2027.

### Uber (Robotaxi Deployment)
- Multi-year agreement to deploy Wayve-powered robotaxis on the Uber network.
- First service launch planned for **London in 2026**.
- Plans to scale to **10+ markets globally**.
- MoU signed with Uber and Nissan jointly for a **Tokyo robotaxi pilot by late 2026** using the Nissan LEAF.

### Mercedes-Benz, Stellantis
- Strategic investors in the Series D. Exact deployment timelines not yet public, but their investment signals intent to integrate Wayve's autonomy stack. [Uncertainty: specific deal terms undisclosed.]

## What Makes Wayve Interesting

1. **The anti-Waymo thesis**: While Waymo spent $10B+ building HD maps and hand-coded systems city by city, Wayve bets that a single learned model can generalize across cities and countries without per-location engineering. The 500-city zero-shot result is the strongest evidence yet that this can work.

2. **Platform play in a winner-take-most market**: Most AV companies are vertically integrated (own cars, own fleet, own maps). Wayve is the rare horizontal player -- licensing to multiple OEMs and mobility platforms. If it works, this is a far larger addressable market.

3. **Cambridge deep learning pedigree**: Alex Kendall published some of the most-cited papers in the field (Bayesian deep learning for perception, PoseNet for camera relocalization). The team is stacked with top-tier ML talent from Cambridge, Microsoft Research, and DeepMind.

4. **Multimodal foundation model approach**: LINGO-2 represents a frontier in combining vision, language, and action in a single model for real-world robotics -- not just autonomous driving but a potential path toward general embodied AI.

5. **Capital efficiency vs. US competitors**: Wayve has raised ~$2.5B total. Waymo has consumed $10B+. Cruise burned $8B+ before imploding. If Wayve can deliver comparable or better autonomy at a fraction of the cost, the unit economics of the platform model could be dramatically superior.

6. **Europe-first regulatory advantage**: Based in the UK with strong ties to European regulators and automakers. The EU and UK are developing AV regulatory frameworks that could favor Wayve's approach. The company is positioning to be the autonomy layer for European and Japanese auto industry -- markets largely unserved by US AV players.

7. **Strategic investor alignment**: Having NVIDIA (compute), Microsoft (cloud/AI), Uber (demand), and three major OEMs (Nissan, Mercedes, Stellantis) as investors creates a reinforcing ecosystem around Wayve's platform.

## Key Risks

- End-to-end learned driving is still unproven at scale in safety-critical production deployment. The gap between impressive demos and certified L3/L4 production vehicles is significant.
- Competition from Tesla FSD (also end-to-end), Waymo (massive head start in deployment), and Chinese players (Baidu Apollo, Huawei, Momenta).
- Regulatory timelines for L3/L4 approval remain uncertain, particularly in the UK and EU.
- Revenue is essentially pre-commercial as of early 2026; the company is still burning through venture capital.

## Timeline

| Year | Milestone |
|------|-----------|
| 2017 | Founded at University of Cambridge by Alex Kendall and Amar Shah |
| 2018 | Demonstrated first end-to-end learned driving on UK roads |
| 2019 | Series A ($20M); relocated HQ to London |
| 2020 | Co-founder Amar Shah departs; Alex Kendall becomes CEO |
| 2022 | Series B ($200M) |
| 2024 | Series C ($1.05B, led by SoftBank) -- largest-ever for a UK AI company at the time |
| 2025 | Nissan production partnership signed; headcount doubled to ~650; opened hubs in Germany and Japan |
| 2026 (Feb) | Series D ($1.2B); $8.6B valuation; Uber partnership announced |
| 2026 (planned) | Commercial robotaxi trials launch in London; Tokyo pilot with Uber/Nissan |
| 2027 (planned) | Supervised autonomy in mass-produced Nissan vehicles (ProPILOT integration) |

## Sources

- [Wayve Series D Press Release](https://wayve.ai/press/series-d/)
- [TechCrunch: Wayve raises $1.2B from Nvidia, Uber, and three automakers](https://techcrunch.com/2026/02/24/self-driving-tech-startup-wayve-raises-1-2b-from-nvidia-uber-and-three-automakers/)
- [Tech.eu: Wayve raises $1.2B at $8.6B valuation](https://tech.eu/2026/02/25/wayve-raises-12b-at-86b-valuation-to-scale-embodied-ai-for-autonomous-driving/)
- [Wayve Series C Press Release](https://wayve.ai/press/series-c/)
- [TechCrunch: Wayve raises $1B led by SoftBank (Series C)](https://techcrunch.com/2024/05/06/wayve-raises-1-billion-led-by-softbank-to-take-self-driving-to-cars-and-robots/)
- [Wayve Series B Press Release](https://wayve.ai/press/wayve-announces-200-million-in-funding-to-accelerate-the-development-of-av2-0-the-next-wave-of-autonomous-vehicles/)
- [Wayve Leadership Team](https://wayve.ai/company/leadership-team/)
- [Alex Kendall personal site](https://alexgkendall.com/)
- [Cambridge Engineering: Alex Kendall alumni story](https://www.eng.cam.ac.uk/news/alumni-stories-meet-alex-kendall-autonomous-vehicle-pioneer-global-ambition)
- [Wayve Wikipedia](https://en.wikipedia.org/wiki/Wayve)
- [Wayve Technology Overview](https://wayve.ai/technology/)
- [LINGO-2: Driving with Natural Language](https://wayve.ai/thinking/lingo-2-driving-with-language/)
- [Wayve and Uber Partnership](https://wayve.ai/press/wayve-and-uber-partner/)
- [Ontario Teachers' Pension Plan: Wayve investment](https://www.otpp.com/en-ca/about-us/news-and-insights/2026/wayve-secures-funding-to-deploy-global-autonomy-platform/)
- [CleanTechnica: Wayve attracts investments from NVIDIA, Microsoft, Uber, Mercedes](https://cleantechnica.com/2026/02/25/wayve-attracts-fresh-investments-from-nvidia-microsoft-uber-mercedes/)
- [Tech.eu: Wayve headcount reaches 650](https://tech.eu/2025/07/28/wayve-sees-leap-in-headcount-to-650-amid-expansion-into-new-markets/)
- [BeBeez: Wayve leadership team profile](https://bebeez.eu/2025/01/27/wayves-power-players-the-leadership-team-behind-the-nvidia-backed-autonomous-vehicle-unicorn/)
- [Wayve Investors page](https://wayve.ai/company/investors/)
- [EU-Startups: Wayve Series D](https://www.eu-startups.com/2026/02/wayve-rockets-to-e7-2-billion-valuation-with-e1-billion-series-d-bet-on-ai-driven-autonomy-backing-from-uber-and-microsoft/)
