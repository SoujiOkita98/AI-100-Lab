---
name: "Skild AI"
status: active
founded: 2023
hq: "Pittsburgh, PA"
website: "https://www.skild.ai"
sector: ["foundation models", "robotics", "physical AI", "embodied intelligence", "manufacturing automation"]
one_liner: "Building the first general-purpose, omni-bodied foundation model (the 'Skild Brain') that can control any robot, perform any task, in any environment."
logo: ""

total_raised_m: 2215
latest_valuation_m: 14000
funding_rounds:
  - stage: "Seed"
    date: 2023
    amount_m: 14.5
    valuation_m: null
    lead_investors: ["Lightspeed Venture Partners", "Sequoia Capital"]
    source: "https://sacra.com/c/skild-ai/"
    notes: "Co-led by Lightspeed and Sequoia. Initial capital to begin developing a robotics foundation model."

  - stage: "Series A"
    date: 2024-07
    amount_m: 300
    valuation_m: 1500
    lead_investors: ["Lightspeed Venture Partners", "Coatue", "SoftBank Group", "Bezos Expeditions"]
    source: "https://www.businesswire.com/news/home/20240709306400/en/Skild-AI-Raises-$300M-Series-A-To-Build-A-Scalable-AI-Foundation-Model-For-Robotics"
    notes: "Additional participants included Felicis Ventures, Sequoia, Menlo Ventures, General Catalyst, CRV, SV Angel, Carnegie Mellon University, and the Amazon Industrial Innovation Fund & Alexa Fund. Valued at $1.5B -- reaching unicorn status barely a year after founding."

  - stage: "Series B"
    date: 2025-05
    amount_m: 500
    valuation_m: 4700
    lead_investors: ["SoftBank Group"]
    source: "https://techcrunch.com/2025/12/08/softbank-and-nvidia-reportedly-in-talks-to-fund-skildai-at-14b-nearly-tripling-its-value/"
    notes: "Participation from LG Technology Ventures, Samsung, NVIDIA, and others. Some sources report this as April 2025 rather than May; exact date uncertain. Valuation reported as $4.5B-$4.7B across sources."

  - stage: "Series C"
    date: 2026-01-14
    amount_m: 1400
    valuation_m: 14000
    lead_investors: ["SoftBank Group"]
    source: "https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B"
    notes: "Participation from NVentures (NVIDIA), Macquarie Capital, Bezos Expeditions, Disruptive, 1789 Capital. Existing investors Lightspeed, Felicis, Coatue, and Sequoia doubled down. Strategic investors Samsung, LG, Schneider, CommonSpirit, and Salesforce Ventures also joined. Valuation tripled in ~7 months."

founders:
  - name: "Deepak Pathak"
    role: "Co-Founder & CEO"
    background: "Assistant Professor at the Robotics Institute, Carnegie Mellon University. PhD in AI from UC Berkeley (2014-2019). B.Tech in Computer Science from IIT Kanpur (Gold Medalist). Pioneered 'curiosity-driven' learning in robotics -- a foundational idea in self-supervised robot exploration. Over 4,000 citations by mid-2024. Co-founded VisageMap Inc. (facial recognition), which was acquired by FaceFirst."
    origin: "Indian"

  - name: "Abhinav Gupta"
    role: "Co-Founder & President"
    background: "Tenured Professor at the Robotics Institute, Carnegie Mellon University. Founding member and research leader at FAIR (Facebook AI Research) Pittsburgh lab (2018-2022), where he focused on robotics and lifelong learning systems. Research spans large-scale visual and robot learning, self-supervised learning, and scene understanding. Over 88,000 Google Scholar citations. Joined CMU Robotics Institute as a postdoc in 2009, became faculty in 2011."
    origin: "Indian"

key_team_members:
  - name: "Shikhar Bahl"
    role: "Research Scientist, Founding Team Member"
    background: "PhD from the Robotics Institute at CMU, advised by both Deepak Pathak and Abhinav Gupta. Part of the founding team from the earliest days."

team_composition: "The founding team is rooted in Carnegie Mellon University's Robotics Institute, one of the world's premier robotics research labs. Both co-founders are active CMU faculty members who bring complementary strengths: Pathak is known for self-supervised and curiosity-driven robot learning, while Gupta brings large-scale visual learning and industry experience from leading FAIR's Pittsburgh lab. The team is compact (~50-60 employees as of early 2026) but heavily research-oriented, drawn largely from the CMU robotics ecosystem. The IIT-to-CMU pipeline is notable -- both founders are Indian-born researchers who trained at top US institutions."

business_model: "Software-centric 'brain-as-a-service' for robotics. Skild builds the Skild Brain -- a general-purpose foundation model -- and deploys it as the intelligence layer on third-party robot hardware. Rather than building its own robots, Skild partners with hardware OEMs (ABB Robotics, Universal Robots, Foxconn) and integrates its AI into their existing robot platforms. Revenue comes from licensing and deploying the Skild Brain across industrial customers. The company grew from zero to approximately $30M in revenue in 2025, indicating early commercial traction that most robotics AI competitors have not yet achieved."

products_and_models:
  - "Skild Brain: Claimed to be the industry's first unified, omni-bodied robotics foundation model. Can control any robot (quadrupeds, humanoids, tabletop arms, mobile manipulators) without prior knowledge of the robot's exact body form. Uses a hierarchical architecture: a low-frequency high-level manipulation/navigation policy feeds into a high-frequency low-level policy that translates commands into precise joint angles and motor torques."
  - "The model leverages in-context learning -- when introduced to a new body or environment, it adjusts behavior based on live experience rather than requiring retraining or fine-tuning."
  - "Training data strategy: Pre-trained on Internet-scale human video data and massive physics-based simulations with thousands of robot instances across multiple embodiments and environments."

customers_and_partnerships:
  - "Foxconn + NVIDIA: Deploying Skild Brain on dual-arm robots on Foxconn's assembly lines building NVIDIA Blackwell GPU server systems in Houston, TX. This is a flagship real-world deployment."
  - "ABB Robotics: Integration of Skild Brain into ABB's industrial robot portfolio for advanced manufacturing (announced March 2026)."
  - "Universal Robots (Teradyne): Partnership to deploy Skild Brain across UR's collaborative robot platforms (announced March 2026)."
  - "Mobile Industrial Robots (MiR, Teradyne): Expansion into mobile robotics applications."
  - "Samsung, LG, Schneider Electric: Strategic investors likely exploring deployment of Skild's technology in their respective domains (consumer electronics manufacturing, industrial automation)."

revenue_signals: "The company reportedly grew from zero to ~$30M in revenue in 2025, which is notable given that most competitors (including Physical Intelligence) remain pre-revenue or very early revenue. The Foxconn/NVIDIA factory deployment and March 2026 ABB/Universal Robots partnerships suggest an accelerating commercial pipeline. Revenue model details (per-robot licensing, subscription, or per-deployment fees) have not been publicly disclosed."

competitors:
  - "Physical Intelligence (San Francisco, $5.6B valuation, pi0/pi0.6 models, backed by Bezos/CapitalG)"
  - "Figure AI (humanoid robots with integrated AI)"
  - "1X Technologies (humanoid robots, OpenAI-backed)"
  - "Google DeepMind Robotics (RT-2, internal research)"
  - "Tesla Optimus (vertically integrated humanoid)"
  - "Brain Corp (autonomous mobile robots for commercial environments)"
  - "Sanctuary AI (human-like robots for complex tasks)"

sources:
  - "https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B"
  - "https://www.businesswire.com/news/home/20240709306400/en/Skild-AI-Raises-$300M-Series-A-To-Build-A-Scalable-AI-Foundation-Model-For-Robotics"
  - "https://techcrunch.com/2025/12/08/softbank-and-nvidia-reportedly-in-talks-to-fund-skildai-at-14b-nearly-tripling-its-value/"
  - "https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/"
  - "https://news.crunchbase.com/venture/robotics-startup-skild-ai-triples-valuation/"
  - "https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain"
  - "https://www.skild.ai/blogs/omni-bodied"
  - "https://www.skild.ai/blogs/series-c"
  - "https://sequoiacap.com/article/partnering-with-skild/"
  - "https://lsvp.com/stories/skild-is-bringing-generative-ai-to-the-real-world/"
  - "https://technical.ly/entrepreneurship/pittsburgh-skild-ai-nvidia-foxconn-robotics-deployment/"
  - "https://www.globenewswire.com/news-release/2026/03/17/3256839/0/en/Skild-AI-Expands-Generalized-Robot-Intelligence-Across-Industries-With-ABB-Robotics-Universal-Robots-and-NVIDIA.html"
  - "https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/"
  - "https://aibusiness.com/robotics/skild-ai-startup-builds-robot-brain"
  - "https://www.nvidia.com/en-us/case-studies/skild-ai/"
  - "https://sacra.com/c/skild-ai/"

last_updated: 2026-03-20
confidence: medium-high
confidence_notes: "Funding amounts and lead investors are well-sourced from official press releases (BusinessWire, GlobeNewsWire) and major outlets (TechCrunch, Crunchbase). Series B valuation varies slightly ($4.5B vs $4.7B) and date varies (April vs May 2025) across sources. The $30M revenue figure is cited in the Series C press release but not independently verified. Seed round details are less well-documented than later rounds. Team size estimates (~50-60) come from third-party databases and may be approximate. Founder backgrounds are cross-referenced across CMU faculty pages, Google Scholar, and press coverage."
---

# Skild AI

## Overview

Skild AI is a Pittsburgh-based startup building the "Skild Brain" -- a general-purpose, omni-bodied foundation model designed to serve as a universal intelligence layer for robots. Founded in 2023 by two Carnegie Mellon University Robotics Institute professors, Deepak Pathak and Abhinav Gupta, the company has raised approximately $2.2 billion across four rounds in under three years, reaching a $14 billion valuation as of January 2026.

The core thesis: a single foundation model can learn to control any robot body, in any environment, for any task -- without task-specific retraining. This "omni-bodied" approach stands in contrast to the traditional robotics paradigm of building narrow, hand-tuned controllers for each specific robot and application.

## Funding story

Skild AI's fundraising trajectory is among the fastest in AI history, rivaling or exceeding companies like Physical Intelligence and Figure AI in pace.

**2023 -- Seed ($14.5M).** Co-led by Lightspeed Venture Partners and Sequoia Capital. The company was founded on the research reputations of Pathak and Gupta and the promise of applying foundation model scaling laws to robotics.

**July 2024 -- Series A ($300M at $1.5B valuation).** Led by Lightspeed, Coatue, SoftBank, and Bezos Expeditions. A massive Series A by any standard -- the company reached unicorn status barely a year after founding. Carnegie Mellon University itself participated as an investor, reflecting the deep institutional ties. Amazon's Industrial Innovation Fund and Alexa Fund also joined, signaling interest from the largest potential customer of robotics AI.

**May 2025 -- Series B ($500M at ~$4.7B valuation).** SoftBank led, with Samsung, LG Technology Ventures, and NVIDIA joining. The strategic investor mix shifted toward hardware OEMs and chip companies -- a signal that the Skild Brain was moving from research toward deployment. Some sources report this round as April 2025; the exact date is uncertain.

**January 14, 2026 -- Series C ($1.4B at $14B+ valuation).** SoftBank led again. NVentures (NVIDIA), Macquarie Capital, Bezos Expeditions, Disruptive, and 1789 Capital participated alongside returning investors Lightspeed, Felicis, Coatue, and Sequoia. Strategic investors Samsung, LG, Schneider Electric, CommonSpirit, and Salesforce Ventures also joined. The valuation tripled in roughly seven months -- from $4.7B to $14B.

**Total raised: ~$2.215B.**

## Founders and team

The founding team is concentrated in one institution: Carnegie Mellon University's Robotics Institute.

- **Deepak Pathak (CEO)** -- Assistant Professor at CMU's Robotics Institute. PhD from UC Berkeley (2014-2019), B.Tech from IIT Kanpur (Gold Medalist). Known for pioneering curiosity-driven learning in robotics -- enabling robots to explore and learn without explicit reward signals. Previously co-founded VisageMap (facial recognition), acquired by FaceFirst. Indian-born.

- **Abhinav Gupta (President)** -- Tenured Professor at CMU's Robotics Institute. One of the most cited researchers in computer vision and robotics globally (88,000+ Google Scholar citations). Was a founding member and research leader at FAIR (Facebook AI Research) Pittsburgh (2018-2022), where he led work on robotics and lifelong learning. Joined CMU as a postdoc in 2009, became faculty in 2011. Indian-born.

- **Shikhar Bahl** -- Research Scientist and founding team member. PhD from CMU's Robotics Institute, advised by both Pathak and Gupta.

The team is compact (~50-60 employees as of early 2026) and heavily research-oriented, drawn largely from the CMU robotics ecosystem. Both founders maintain their CMU faculty positions alongside leading Skild -- an arrangement that gives the company ongoing access to CMU's talent pipeline and research output.

The IIT-to-US-PhD pipeline is a recurring pattern: both founders are Indian-born researchers who trained at elite Indian and American institutions before becoming CMU faculty. This background in the Indian engineering and computer science tradition, combined with deep American research training, is a common profile among top AI researchers.

## Technology

The Skild Brain is built around two key architectural ideas:

**Omni-bodied generalization.** Unlike traditional robotics models tailored to a specific robot design, the Skild Brain is trained to control any robot form factor -- quadrupeds, humanoids, tabletop arms, mobile manipulators -- without prior knowledge of the robot's exact body. The model uses a hierarchical architecture: a low-frequency high-level policy handles manipulation and navigation planning, while a high-frequency low-level policy translates those plans into precise joint angles and motor torques.

**In-context adaptation.** When the Skild Brain encounters a new robot body or unfamiliar environment, it adapts its behavior based on live in-context experience -- similar to how large language models can handle new tasks via in-context learning. This means no retraining or fine-tuning is required. The company claims the model can handle unpredictable scenarios such as loss of limbs, jammed wheels, increased payload, or even an entirely new body.

**Training data strategy.** Skild addresses the chronic data scarcity problem in robotics through two sources: (1) pre-training on Internet-scale human video data (learning physics and manipulation from watching humans), and (2) massive physics-based simulations with thousands of robot instances across multiple embodiments and environments. The Foxconn factory deployment is also designed to accelerate a "data flywheel" -- real-world tasks generate data that improves the model, which in turn enables more capable deployments.

## Business model

Skild operates a software-centric "brain-as-a-service" model. Rather than building its own robot hardware, the company develops the Skild Brain foundation model and deploys it as the intelligence layer on third-party robot platforms.

The go-to-market strategy centers on partnerships with major robot hardware OEMs:

- **Foxconn + NVIDIA:** Deploying Skild Brain on dual-arm robots assembling NVIDIA Blackwell GPU server systems at Foxconn's Houston, TX facility. This is the flagship real-world deployment.
- **ABB Robotics:** Integrating Skild Brain into ABB's industrial robot portfolio (announced March 17, 2026).
- **Universal Robots (Teradyne):** Deploying across UR's collaborative robot platforms (announced March 17, 2026).
- **Mobile Industrial Robots (MiR, Teradyne):** Expansion into mobile robotics.

The company reportedly grew from zero to approximately $30M in revenue in 2025 -- a claim made in the Series C announcement but not independently verified. If accurate, this makes Skild one of the first robotics foundation model companies to achieve meaningful commercial revenue, ahead of competitors like Physical Intelligence.

Specific pricing and licensing terms have not been publicly disclosed.

## What makes them interesting

1. **CMU Robotics Institute pedigree.** Pathak and Gupta represent arguably the strongest concentration of robotics research talent to come out of CMU in a single startup. Gupta's 88,000+ citations and Pathak's foundational work on curiosity-driven learning give the company deep technical credibility.

2. **Omni-bodied approach.** The claim that a single model can control any robot form factor without retraining is ambitious and, if it works at scale, could be transformative. Most competitors build models tuned to specific robot designs.

3. **Fastest capitalization in robotics AI.** $2.2B raised and $14B valuation in under three years, with the valuation tripling in seven months between Series B and C. SoftBank's repeat leadership of the B and C rounds signals strong conviction.

4. **Early revenue.** The reported $30M in 2025 revenue sets Skild apart from most robotics AI competitors who remain pre-revenue. Revenue from actual deployments (not just research contracts) suggests the technology is production-ready for at least some use cases.

5. **Industrial deployment pipeline.** The Foxconn/NVIDIA factory deployment and March 2026 partnerships with ABB and Universal Robots represent concrete, high-profile commercial deployments with established industrial customers -- not just lab demos.

6. **Data flywheel strategy.** Each factory deployment generates real-world training data that improves the model, which makes the next deployment more capable. This self-reinforcing cycle is the same dynamic that powered the scaling of LLMs with user data.

7. **Hardware-agnostic platform play.** By positioning as the "brain" rather than building robots, Skild avoids the capital-intensive hardware trap and can scale across the entire installed base of industrial robots. The ABB and Universal Robots partnerships give access to hundreds of thousands of deployed robot arms worldwide.

## Risks and open questions

- **Omni-bodied claims vs. reality.** Controlling "any robot, any task, any environment" with a single model is an extraordinary claim. Real-world manufacturing environments are unforgiving, and the gap between impressive demos and reliable 24/7 production operation is historically where robotics startups fail.

- **$14B valuation on $30M revenue.** The valuation implies massive growth expectations. At ~467x revenue, the market is pricing in the assumption that Skild will become the dominant platform for robot intelligence. If deployment scales slower than expected, the valuation may prove difficult to sustain.

- **SoftBank concentration risk.** SoftBank has led both the Series B and Series C. While this reflects strong conviction, heavy dependence on a single lead investor introduces risk if SoftBank's strategy shifts (as happened with some SoftBank Vision Fund 1 portfolio companies).

- **Faculty founders.** Both Pathak and Gupta maintain CMU faculty positions. While this provides institutional access, it also raises questions about full-time commitment as the company scales to hundreds of employees and complex industrial deployments.

- **Competitive landscape.** Physical Intelligence, Google DeepMind, Tesla Optimus, and others are pursuing overlapping goals. NVIDIA itself is investing across multiple robotics AI companies. The "winner-take-all" dynamics of foundation models could benefit Skild, or could mean that a better-resourced competitor overtakes them.

## Notes

- **Valuation discrepancy:** Series B valuation is reported as $4.5B in some sources and $4.7B in others. The difference likely reflects pre-money vs. post-money or rounding.
- **Series B timing:** Some sources say April 2025, others May 2025.
- **Revenue figure:** The ~$30M revenue claim appears in the company's own Series C announcement and press coverage. Independent verification is not available.
- **Employee count:** Third-party databases report 50-61 employees as of early 2026. This is small relative to the funding raised and may reflect a deliberate lean-team approach or may be undercounted.
