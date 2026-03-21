---
name: "Physical Intelligence"
status: active
founded: 2024
hq: "San Francisco, CA"
website: "https://www.physicalintelligence.company"
sector: ["foundation models", "robotics", "physical AI", "embodied intelligence", "reinforcement learning"]
one_liner: "Building general-purpose foundation models that give any robot the ability to perform any task in the physical world."
logo: ""

total_raised_m: 1070
latest_valuation_m: 5600
funding_rounds:
  - stage: "Seed"
    date: 2024-03
    amount_m: 70
    valuation_m: 400
    lead_investors: ["Thrive Capital"]
    source: "https://www.crunchbase.com/funding_round/physical-intelligence-834b-seed--0936ae55"
    notes: "7 investors participated. Initial capital to develop foundational models and learning algorithms for robots."

  - stage: "Series A"
    date: 2024-11
    amount_m: 400
    valuation_m: 2000
    lead_investors: ["Jeff Bezos", "Lux Capital", "Thrive Capital"]
    source: "https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html"
    notes: "Other investors include OpenAI's startup fund, Redpoint Ventures, and Bond. Some sources report valuation at $2.4B rather than $2B -- exact figure uncertain."

  - stage: "Series B"
    date: 2025-11
    amount_m: 600
    valuation_m: 5600
    lead_investors: ["CapitalG"]
    source: "https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/"
    notes: "CapitalG (Alphabet's independent growth fund) led. Participation from Lux Capital, Thrive Capital, Jeff Bezos, Index Ventures, T. Rowe Price, Redpoint Ventures, Sequoia Capital, Bond, and NVIDIA (NVentures). Funding earmarked for data collection, strategic partnerships, and team growth."

founders:
  - name: "Karol Hausman"
    role: "Co-Founder & CEO"
    background: "Staff Research Scientist at Google DeepMind. Adjunct Professor at Stanford University where he co-taught CS 224R (Deep Reinforcement Learning). PhD from University of Southern California. Research focus on robot learning and reinforcement learning."
    origin: "Polish (uncertain -- inferred from name)"

  - name: "Lachy Groom"
    role: "Co-Founder"
    background: "Joined Stripe as ~30th employee. Led Stripe Issuing and guided core payments product, global expansion, and enterprise partnerships. After Stripe, spent ~5 years as a prolific angel investor (early bets on Figma, Notion, Ramp, Lattice). Brings commercial/product intuition to the team."
    origin: "Australian"

  - name: "Sergey Levine"
    role: "Co-Founder"
    background: "Professor at UC Berkeley. One of the most cited researchers in robotics and reinforcement learning. Previously at Google Brain/DeepMind. PhD advisor to Chelsea Finn. Pioneered key methods in offline RL and robot learning from demonstration."
    origin: "Russian-American (uncertain)"

  - name: "Chelsea Finn"
    role: "Co-Founder"
    background: "Assistant Professor of Computer Science and Electrical Engineering at Stanford University. PhD from UC Berkeley under Pieter Abbeel and Sergey Levine (2018). Known for meta-learning (MAML algorithm). Runs the IRIS lab at Stanford. Previously at Google."
    origin: "American"

  - name: "Brian Ichter"
    role: "Co-Founder"
    background: "Former Research Scientist at Google DeepMind and Google Brain. PhD in Aeronautics and Astronautics from Stanford University. Research focus on enabling mobile robotic systems for complex tasks."
    origin: "American (uncertain)"

  - name: "Adnan Esmail"
    role: "Co-Founder"
    background: "Former SVP of Engineering at Anduril Industries. Previously worked on hardware technologies at Tesla. Studied Mechanical Engineering, Physics, Electrical Engineering, and Computer Science at MIT."
    origin: "Uncertain"

  - name: "Quan Vuong"
    role: "Co-Founder"
    background: "Deep experience in reinforcement learning and robotics engineering. Previously at Google DeepMind."
    origin: "Vietnamese (inferred from name -- uncertain)"

team_composition: "The founding team is unusual in combining three world-class academic researchers (Hausman/Stanford, Levine/Berkeley, Finn/Stanford) with deep industry experience from Google DeepMind, a defense-tech/hardware operator (Esmail from Anduril/Tesla), and a Silicon Valley business/product leader (Groom from Stripe). This blend of academic rigor, engineering depth, and commercial instinct is rare in robotics startups."

business_model: "Software-centric 'intelligence layer' for robotics. Physical Intelligence develops foundation models (vision-language-action models) that serve as plug-and-play brains for third-party robot hardware. The emerging model is an API/SaaS approach -- providing robotic intelligence as a service rather than building vertically integrated robots. One source mentions a $300/month/robot subscription pricing, though this is unconfirmed and may be speculative. Early commercial traction is through partnerships with hardware companies (Weave Robotics for home/laundry, Ultra for warehouse automation). The company has also open-sourced parts of its stack (openpi on GitHub) to build ecosystem adoption."

products_and_models:
  - "pi0 (October 2024): First generalist robot policy. 3B-parameter vision-language-action flow model built on PaliGemma. Trained on diverse embodied data to follow text instructions and generate robot actions."
  - "pi0.5 (September 2025): Upgraded model with improved open-world generalization."
  - "pi0.6 (November 2025): Hierarchical model (high-level subtask prediction + low-level action generation). Vision-language backbone from Gemma3 4B. 63ms inference per action chunk on a single H100 GPU. Significant improvements in speed and success rates over pi0.5."
  - "pi0.6-star (in development as of early 2026): Next iteration under active development."
  - "openpi: Open-source release of pi0 weights and code on GitHub."

customers_and_partnerships:
  - "Weave Robotics: Home/laundry robots. Pi0.6 reduced human interventions in laundry folding by 50% in live San Francisco laundromat deployments."
  - "Ultra: Industrial warehouse automation. Pi0.6 achieved 96.4% autonomy during full-shift e-commerce order packaging at Ultra's customer site."
  - "AgiBot: Hardware collaboration for deploying embodied intelligence into third-party robot frames."
  - "NVIDIA: Investor and technology partner (NVentures participation in Series B)."

revenue_signals: "Pre-revenue or very early revenue as of late 2025. The $5.6B valuation is based on technology potential rather than current revenue. Competitor Skild AI reportedly generated $30M in revenue from its deployed 'Skild Brain' product, suggesting the market is beginning to monetize but Physical Intelligence has prioritized research over commercialization so far. The Weave and Ultra partnerships (announced February 2026) represent the first public evidence of live commercial deployments using Pi's models."

competitors:
  - "Skild AI (Carnegie Mellon spinout, 'omni-bodied' Skild Brain, reportedly $30M revenue)"
  - "Figure AI (humanoid robots with integrated AI)"
  - "1X Technologies (humanoid robots, OpenAI-backed)"
  - "Covariant (warehouse robotics AI, acquired by Amazon in 2024)"
  - "Google DeepMind Robotics (RT-2, internal research)"
  - "Tesla Optimus (vertically integrated humanoid)"

sources:
  - "https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html"
  - "https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/"
  - "https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding"
  - "https://techcrunch.com/2026/01/30/physical-intelligence-stripe-veteran-lachy-grooms-latest-bet-is-building-silicon-valleys-buzziest-robot-brains/"
  - "https://www.capitalg.com/insights/physical-intelligence-bringing-general-purpose-ai-into-the-physical-world"
  - "https://news.crunchbase.com/ai/robot-brain-startup-unicorn-physical-intelligence-bezos/"
  - "https://www.humanoidsdaily.com/news/the-api-fication-of-robotics-physical-intelligence-unveils-real-world-performance-data-with-weave-and-ultra"
  - "https://www.pi.website/blog/pi0"
  - "https://www.physicalintelligence.company/blog/pi05"
  - "https://website.pi-asset.com/pi06star/PI06_model_card.pdf"
  - "https://www.pi.website/blog/partner"
  - "https://eutechfuture.com/artificial-intelligence/physical-intelligence-building-foundation-models-for-robots-to-interact-with-the-real-world/"
  - "https://sacra.com/c/physical-intelligence/"
  - "https://en.wikipedia.org/wiki/Chelsea_Finn"
  - "https://github.com/Physical-Intelligence/openpi"

last_updated: 2026-03-20
confidence: medium-high
confidence_notes: "Funding amounts and lead investors are well-sourced from multiple outlets (CNBC, Bloomberg, Crunchbase, TechCrunch). Series A valuation varies across sources ($2B vs $2.4B). Founder backgrounds are cross-referenced but some origins are inferred. Revenue/business model details are sparse and partially speculative -- the $300/robot/month pricing is from a single source and unconfirmed. Model technical details are sourced from the company's own blog and model cards."
---

# Physical Intelligence

## Overview

Physical Intelligence (often stylized as "pi" or using the Greek letter) is a San Francisco-based startup developing general-purpose foundation models for robotics. Founded in early 2024 by a team drawn from Google DeepMind, Stanford, UC Berkeley, Anduril, Tesla, and Stripe, the company has raised $1.07B in total funding across three rounds in under two years, reaching a $5.6B valuation as of November 2025.

The core thesis: just as large language models created a general-purpose intelligence layer for text, Physical Intelligence aims to build a general-purpose intelligence layer for the physical world -- a single foundation model that can control any robot to perform any task, trained on diverse embodied data rather than hand-coded for specific applications.

## Funding story

Physical Intelligence's fundraising trajectory has been exceptionally fast, even by AI startup standards.

**March 2024 -- Seed ($70M at ~$400M valuation).** Thrive Capital led. Seven investors participated. The company was barely formed -- founded on the reputations of its academic co-founders and the Stripe-veteran commercial acumen of Lachy Groom.

**November 2024 -- Series A ($400M at ~$2B valuation).** Jeff Bezos, Lux Capital, and Thrive Capital co-led. OpenAI's startup fund, Redpoint Ventures, and Bond also participated. This round came shortly after the company published its first major research result, the pi0 generalist policy model. Some sources report the valuation at $2.4B rather than $2B; the discrepancy likely reflects pre- vs. post-money differences.

**November 2025 -- Series B ($600M at $5.6B valuation).** CapitalG (Alphabet's independent growth fund) led. Broad investor syndicate including Lux Capital, Thrive Capital, Bezos, Index Ventures, T. Rowe Price, Redpoint, Sequoia Capital, Bond, and NVIDIA's NVentures. The capital is earmarked for data collection, strategic partnerships, and team expansion.

**Total raised: ~$1.07B.** The company went from founding to billion-dollar-plus capitalization in approximately 20 months.

## Team

The founding team is the company's primary moat and the reason investors moved so aggressively.

- **Karol Hausman (CEO)** -- Former Staff Research Scientist at Google DeepMind and Adjunct Professor at Stanford (taught CS 224R, Deep RL). Brings both cutting-edge research credentials and the operational instinct to lead a company. Polish origin (inferred).

- **Sergey Levine** -- Professor at UC Berkeley. One of the most influential researchers in robotics and reinforcement learning globally. His work on offline RL, robot learning from demonstration, and scalable robot training is foundational to the field. He was Chelsea Finn's PhD advisor.

- **Chelsea Finn** -- Assistant Professor at Stanford (CS and EE). Creator of the MAML meta-learning algorithm, one of the most cited papers in modern ML. Runs the IRIS lab at Stanford. PhD from Berkeley (2018) under Pieter Abbeel and Levine.

- **Lachy Groom** -- The commercial/product co-founder. Joined Stripe as roughly the 30th employee, rose to lead Stripe Issuing and guide global payments expansion. After Stripe, became a prominent angel investor (Figma, Notion, Ramp, Lattice). His role is to translate world-class research into a viable business.

- **Brian Ichter** -- Former Research Scientist at Google DeepMind/Brain. PhD in Aeronautics and Astronautics from Stanford. Brings robotics systems engineering depth.

- **Adnan Esmail** -- Former SVP of Engineering at Anduril Industries, previously at Tesla. MIT-educated (Mechanical Engineering, Physics, EE, CS). Brings hardware-software integration experience from defense tech and automotive.

- **Quan Vuong** -- Reinforcement learning and robotics engineering background, previously at Google DeepMind.

The team composition is notable: three top-tier academic researchers (Hausman, Levine, Finn) combined with a defense/hardware operator (Esmail), a fintech/product leader (Groom), and deep RL engineers (Ichter, Vuong). This breadth is uncommon in robotics, where teams tend to skew either purely academic or purely engineering.

## Technology

Physical Intelligence's technical approach treats robot control as a sequence modeling problem, analogous to how LLMs treat language.

**pi0 (October 2024):** The company's first generalist robot policy -- a 3-billion-parameter vision-language-action (VLA) flow model built on top of Google's PaliGemma. It takes images and text instructions as input and generates robot actions as output. Trained on broad, diverse embodied data from multiple robot form factors.

**pi0.5 (September 2025):** Improved open-world generalization over pi0.

**pi0.6 (November 2025):** Hierarchical architecture with high-level subtask prediction and low-level action generation. Vision-language backbone initialized from Gemma3 4B. Achieves 63ms inference per action chunk on a single H100 GPU with 5 denoising steps and 3 camera inputs. Significant improvements in both speed and success rate over pi0.5.

**Recap method:** Combines imitation learning with autonomous reinforcement learning, allowing robots to practice and learn from their own mistakes -- a key ingredient for reliability in deployment.

**Open source:** The company released openpi (open-source pi0 weights and code) on GitHub, building community and ecosystem adoption.

## Business model

Physical Intelligence is positioning itself as the "intelligence layer" for robotics -- a horizontal software platform rather than a vertically integrated robot maker.

The emerging business model is API/SaaS: third-party hardware companies integrate Pi's foundation models into their robots as a plug-and-play brain. This mirrors the relationship between OpenAI's API and application developers, but for physical robots.

Early commercial evidence (as of February 2026):

- **Weave Robotics** (home/laundry): Pi0.6 reduced human interventions in laundry folding by 50% during live deployments in a San Francisco laundromat.
- **Ultra** (warehouse automation): Pi0.6 achieved 96.4% autonomy during a full-shift e-commerce order packaging deployment at a customer site.

One source mentions a $300/month/robot subscription price, but this is unconfirmed. Revenue is likely negligible or zero as of early 2026 -- the valuation is based on technology potential and team quality, not current financials.

## What makes them interesting

1. **The "OpenAI for robotics" thesis.** Physical Intelligence is making the strongest bet that foundation models can do for robotics what GPT did for language. If a single model can generalize across robot form factors and tasks, it could collapse the cost and complexity of deploying robots by orders of magnitude.

2. **Best-in-class founding team.** Hausman, Levine, and Finn represent arguably the strongest concentration of robotics/RL research talent in any single startup. Levine and Finn alone account for thousands of citations and foundational contributions to the field. Groom adds rare commercial credibility.

3. **Speed of capitalization.** $1.07B raised in ~20 months with no revenue, reaching $5.6B valuation. This reflects extreme investor conviction, but also creates high expectations.

4. **The horizontal platform play.** By providing intelligence-as-a-service to hardware partners rather than building their own robots, Pi avoids the capital-intensive hardware trap that has killed many robotics startups. The Weave and Ultra partnerships demonstrate this model working in practice.

5. **Live deployment data.** Unlike many AI robotics companies operating only in lab settings, Pi has published real-world deployment metrics (96.4% autonomy in warehouse, 50% reduction in interventions for laundry). This is early but tangible.

6. **Open-source strategy.** Releasing openpi builds ecosystem lock-in and community adoption, similar to Meta's Llama strategy for LLMs.

7. **The risk.** The company is pre-revenue at a $5.6B valuation. Robotics has a long history of overpromising and underdelivering on generalization. Competitors like Skild AI are already generating revenue ($30M reported). The gap between impressive demos and reliable, scalable commercial deployment remains the central challenge of the field.

## Notes

- **Valuation uncertainty:** The Series A valuation appears as either $2B or $2.4B across different sources. This likely reflects pre-money vs. post-money reporting differences.
- **Founder origins:** Several founders' national origins are inferred from names and partial biographical data; these should be treated as uncertain.
- **Revenue model:** The $300/robot/month pricing cited by one source (Sacra) is unconfirmed and may be speculative or placeholder pricing. The company has not publicly disclosed pricing.
- **Competitive context:** The "physical AI" space is heating up rapidly. NVIDIA has publicly partnered with multiple robotics companies. Google DeepMind, Tesla (Optimus), and several well-funded startups (Figure AI, 1X, Skild) are all pursuing overlapping goals with different approaches.
