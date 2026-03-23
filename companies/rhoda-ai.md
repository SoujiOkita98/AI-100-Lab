---
company: Rhoda AI
website: https://www.rhoda.ai
founded: ~202
headquarters: Menlo Park, CA (unconfirmed; inferred from Stanford ties and investor base)
sector: AI / Robotics / Physical AI
stage: Series A
total_funding: $450M
valuation: $1.7B (post-money, as of March 2026)
lead_investor: Premji Invest
other_investors:
- Capricorn Investment Group
- Khosla Ventures
- Leitmotif
- Matter Venture Partners
- Mayfield
- Prelude Ventures
- Temasek
- Xora
notable_angels:
- John Doerr
legal_counsel: Wilson Sonsini Goodrich & Rosati
last_updated: 2026-03-20
funding_rounds:
- stage: Series A
  date: 2026-03
  amount_m: 450
  valuation_m: 1700
  lead_investors:
  - Capricorn Investment Group
  - Khosla Ventures
  - Premji Invest
  - Temasek
  - Mayfield
  source: https://www.bloomberg.com/news/articles/2026-03-10/ai-robotics-startup-rhoda-valued-at-1-7-billion-in-new-funding
one_liner: Rhoda AI emerged from stealth on March 10, 2026, announcing a $450 million Series A at a $1.7 billion valuation
website_verified: true
crunchbase: https://www.crunchbase.com/organization/rhoda-ai
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/rhoda-ai
---

# Rhoda AI

## Overview

Rhoda AI emerged from stealth on March 10, 2026, announcing a $450 million Series A at a $1.7 billion valuation. The company is building a robotics intelligence platform called **FutureVision** that uses video-predictive control to enable robots to operate autonomously in dynamic, real-world environments -- not just controlled lab settings. The round was led by Premji Invest, with participation from Temasek, Khosla Ventures, Mayfield, and others.

## Founders and Leadership

### Jagdeep Singh -- CEO and Co-founder
Singh is a serial deep-tech entrepreneur with a track record of founding companies that reach public markets or high-profile acquisitions. He holds an MS in Computer Science from Stanford University and an MBA from UC Berkeley. Previous companies include:

- **QuantumScape** (NYSE: QS) -- co-founder and CEO; solid-state battery company for EVs, taken public via SPAC.
- **Infinera** (NASDAQ: INFN) -- optical networking.
- **Lightera** -- acquired by Ciena.
- **Raxium** -- acquired by Google (micro-LED display technology).

Singh's pattern is building hardware-heavy, deep-science companies and scaling them to significant outcomes. Multiple investors cite his ability to recruit exceptional technical talent.

### Eric Ryan Chan -- Chief Science Officer and Co-founder
Chan is a Stanford PhD researcher specializing in computer vision and generative modeling. Before Rhoda, he was a generative model architect at **WorldLabs** (the 3D generative AI company founded by Fei-Fei Li). His academic work is highly cited in neural rendering and 3D-aware generative models.

### Gordon Wetzstein -- Co-founder
Wetzstein is an Associate Professor of Electrical Engineering (and, by courtesy, Computer Science) at Stanford University. He heads the **Stanford Computational Imaging Lab** and co-directs the Stanford Center for Image Systems Engineering. His research spans computational optics, neural rendering, and AI for vision -- providing the scientific foundations for Rhoda's video-predictive architecture.

### Other Named Team Members
Andrew Wooten, Changan Chen, Steve Tirado, Alex Bergman, and Vincent Clerc are listed as part of the leadership team. Specific roles and backgrounds for these individuals were not detailed in available sources. [Uncertainty flag: titles and responsibilities beyond the three co-founders are unclear from public reporting.]

## Technology: FutureVision and Direct Video Action (DVA)

Rhoda's core innovation is a **Direct Video Action (DVA)** model architecture:

1. **Internet-scale video pretraining** -- Rather than relying primarily on teleoperated robot trajectory data (the standard approach), Rhoda trains foundational models on millions of publicly available internet videos. This gives the system a broad prior understanding of how the physical world works.

2. **Video-predictive control loop** -- The robot continuously observes its environment, predicts future visual states using video-based modeling, and converts those predictions into motor actions. This runs as a closed feedback loop updating every few hundred milliseconds.

3. **Real-world generalization** -- The claimed advantage is that robots trained this way can adapt to novel, unstructured environments (factories, warehouses, etc.) rather than only performing well in controlled settings with known objects and layouts.

This approach positions Rhoda in the emerging "physical AI" or "world model" category alongside companies like Figure, Physical Intelligence (Pi), and Skild AI, but with a distinctive emphasis on video prediction as the core representation rather than language-conditioned policies or pure simulation.

## Business Model

- **Software platform licensing** -- FutureVision is designed to serve as the intelligence layer for robotics systems, potentially licensed to partners building their own hardware.
- **Proprietary hardware** -- The company also plans to develop its own robotic hardware that doubles as a data-collection engine, creating a flywheel of real-world data to improve models.
- **Industrial deployments** -- The company is working with partners in manufacturing and logistics. Specific customer names have not been disclosed.

[Uncertainty flag: The exact revenue model (SaaS subscription, per-robot licensing, professional services, etc.) has not been publicly detailed. The hardware vs. software split is also unclear.]

## Funding Details

| Round     | Amount | Lead Investor  | Valuation | Date         |
|-----------|--------|----------------|-----------|--------------|
| Series A  | $450M  | Premji Invest  | $1.7B     | March 2026   |

No prior rounds have been publicly disclosed. The company operated in stealth for approximately 18 months before this announcement. It is unclear whether earlier seed or pre-seed funding was raised privately.

## What Makes Them Interesting

1. **Founder pedigree**: Jagdeep Singh has taken multiple deep-tech companies to IPO or major acquisition. This is rare in robotics AI, where many founders are first-time entrepreneurs from academia.

2. **Stanford brain trust**: The co-founding team spans Stanford's Computational Imaging Lab and cutting-edge generative AI research (WorldLabs lineage). The Chan-Wetzstein axis represents some of the strongest academic talent in neural rendering and 3D vision.

3. **Video-first approach to robotics**: While most robotics AI companies train on simulation or teleoperation data, Rhoda bets that internet video contains enough physics understanding to bootstrap general robotic intelligence. This is a contrarian and capital-efficient data strategy if it works.

4. **Investor signal**: Premji Invest leading a $450M Series A for a stealth-stage company, with Temasek, Khosla, and John Doerr participating, signals very high conviction. The $1.7B valuation at Series A places Rhoda among the most richly valued robotics AI startups globally.

5. **Physical AI market sizing**: Mayfield's investment thesis frames this as a "$30 trillion physical AI market" opportunity, suggesting Rhoda is positioned not just as a robotics company but as infrastructure for the broader automation of physical work.

## Key Risks and Open Questions

- The DVA architecture is novel and unproven at industrial scale. Whether video prediction translates to reliable, safe robotic action in safety-critical environments is an open question.
- The company has not disclosed specific customers, revenue, or deployment metrics.
- Competition is fierce: Physical Intelligence, Figure, Skild AI, and others are well-funded and pursuing adjacent approaches.
- Hardware ambitions could significantly increase burn rate and execution complexity.

## Sources

- [BusinessWire press release (March 10, 2026)](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World)
- [Bloomberg: AI Robotics Startup Rhoda Valued at $1.7 Billion](https://www.bloomberg.com/news/articles/2026-03-10/ai-robotics-startup-rhoda-valued-at-1-7-billion-in-new-funding)
- [SiliconANGLE: Rhoda AI raises $450M to build foundational robotics models](https://siliconangle.com/2026/03/10/rhoda-ai-raises-450m-build-foundational-robotics-models-learn-internet-videos/)
- [The Robot Report: Rhoda AI exits stealth with $450M](https://www.therobotreport.com/rhoda-ai-exits-stealth-with-450m-to-train-robots-from-video/)
- [TechFundingNews: Khosla-backed Rhoda raises $450M at $1.7B valuation](https://techfundingnews.com/rhoda-ai-450m-series-a-stealth-exit-robotics/)
- [TNGlobal: Temasek-backed Rhoda AI raises $450M](https://technode.global/2026/03/11/temasek-backed-rhoda-ai-raises-450m-series-a-funding-to-accelerate-robotics-development/)
- [Humanoids Daily: Rhoda AI Hits $1.7B Valuation, Unveils DVA Model](https://www.humanoidsdaily.com/news/rhoda-ai-hits-1-7b-valuation-unveils-direct-video-action-model-to-bridge-the-real-world-gap)
- [PYMNTS: Rhoda AI Raises $450 Million to Automate Manufacturing and Logistics](https://www.pymnts.com/news/investment-tracker/2026/rhoda-ai-raises-450-million-to-automate-manufacturing-and-logistics/)
- [Mayfield: Why We Backed Rhoda AI](https://www.mayfield.com/why-we-backed-rhoda-ai-the-30-trillion-physical-ai-market/)
- [Wilson Sonsini advisory announcement](https://www.wsgr.com/en/insights/wilson-sonsini-advises-rhoda-ai-on-dollar450-million-funding-as-company-emerges-from-stealth.html)
- [Menlo Times profile](https://www.menlotimes.com/post/how-rhoda-ai-plans-to-bring-robots-from-controlled-laboratory-demonstrations-into-real-world-environ)
