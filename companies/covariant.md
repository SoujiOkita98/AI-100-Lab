---
name: "Covariant"
status: "semi-active (post-acquihire)"
founded: 2017
hq: "Emeryville, CA"
website: "https://covariant.ai"
sector: ["AI robotics", "warehouse automation", "foundation models for robotics"]
one_liner: "AI robotics company building foundation models for warehouse automation; effectively acquihired by Amazon in 2024 in a controversial reverse-acquihire deal."
logo: "https://covariant.ai/favicon.ico"

total_raised_m: 222
latest_valuation_m: 625
funding_rounds:
  - stage: "Seed"
    date: 2017-11
    amount_m: 7
    valuation_m: ~
    lead_investors: ["Amplify Partners"]
    source: "https://en.wikipedia.org/wiki/Covariant_(company)"
    notes: "Founded as Embodied Intelligence. Renamed to Covariant in 2019."

  - stage: "Series A"
    date: 2019-05
    amount_m: 20
    valuation_m: ~
    lead_investors: ["Index Ventures"]
    source: "https://en.wikipedia.org/wiki/Covariant_(company)"

  - stage: "Series B"
    date: 2020-05
    amount_m: 40
    valuation_m: ~
    lead_investors: ["Index Ventures"]
    source: "https://covariant.ai/covariant-raises-usd40-million-in-series-b-funding-to-bring-ai-robotics-to-new-industries/"

  - stage: "Series C"
    date: 2021-07
    amount_m: 80
    valuation_m: ~
    lead_investors: ["Index Ventures"]
    source: "https://techcrunch.com/2021/07/27/robotic-ai-firm-covariant-raises-another-80-million/"
    notes: "Amplify Partners and Radical Ventures also participated."

  - stage: "Series C extension"
    date: 2023-04
    amount_m: 75
    valuation_m: 625
    lead_investors: ["Radical Ventures", "Index Ventures"]
    source: "https://techcrunch.com/2023/04/04/covariants-robotic-picking-at-nabs-another-75m/"
    notes: "CPPIB, Amplify Partners, Gates Frontier Holdings, AIX Ventures, Northgate Capital also participated. Brought total funding to $222M. Valuation of $625M reported in whistleblower filings."

  - stage: "Amazon reverse acquihire"
    date: 2024-08
    amount_m: 400
    valuation_m: ~
    lead_investors: ["Amazon"]
    source: "https://www.washingtonpost.com/technology/2025/01/18/amazon-antitrust-ai-whistleblower/"
    notes: "$380M upfront + $20M final licensing payment due one year after close. Not a traditional acquisition -- Amazon licensed Covariant's technology (non-exclusive) and hired 3 co-founders + ~25% of staff. Structured to avoid premerger antitrust reporting, per whistleblower complaint."

founders:
  - name: "Pieter Abbeel"
    role: "Co-Founder, President & Chief Scientist (now at Amazon)"
    background: "PhD in CS from Stanford under Andrew Ng. Professor at UC Berkeley; Director of the Berkeley Robot Learning Lab. Former researcher at OpenAI. One of the most cited robotics/RL researchers globally. Belgian-American."

  - name: "Peter Chen"
    role: "Co-Founder & CEO (now at Amazon)"
    background: "PhD student of Pieter Abbeel at UC Berkeley. Former researcher at OpenAI. Led Covariant as CEO from founding."

  - name: "Rocky Duan"
    role: "Co-Founder & CTO (now at Amazon)"
    background: "PhD student of Pieter Abbeel at UC Berkeley. Former researcher at OpenAI."

  - name: "Tianhao Zhang"
    role: "Co-Founder (remained at Covariant)"
    background: "Former student of Pieter Abbeel at UC Berkeley. Former researcher at Microsoft. One of the two leaders of the post-Amazon Covariant entity."

current_leadership:
  - name: "Ted Stinson"
    role: "CEO (appointed August 2024)"
    background: "Former COO of Covariant. Assumed CEO role after Amazon deal."
  - name: "Tianhao Zhang"
    role: "Co-Founder, technical leadership"

team_size: "~56 employees (post-Amazon deal, down from ~250 at peak)"

key_technology:
  - name: "Covariant Brain"
    description: "AI-powered robotic picking system trained on one of the largest real-world robotics datasets from warehouses globally. Enables robots to pick virtually any SKU on Day 1."
  - name: "RFM-1 (Robotics Foundation Model)"
    description: "8 billion parameter multimodal transformer trained on text, images, video, robot actions, and sensor data. Released March 2024. Provides robots with language understanding, physics reasoning, and adaptive learning through in-context learning. Represents one of the first commercial robotic foundation models."

business_model: "B2B robotics AI -- licenses the Covariant Brain software to warehouse and fulfillment center operators to automate pick-and-place operations. Deployed with integration partners like KNAPP."

customers:
  - "50+ customers and partners (as of 2024)"
  - "KNAPP (5+ year partnership)"
  - "Industries: apparel, health & beauty, grocery, pharmaceuticals"

revenue_signals: "No public revenue figures. Pre-deal, Covariant had deployed hundreds of AI-powered robotic solutions across multiple industries."

---

## Overview

Covariant was founded in 2017 as **Embodied Intelligence** by four UC Berkeley researchers -- Pieter Abbeel, Peter Chen, Rocky Duan, and Tianhao Zhang -- all of whom had worked at OpenAI and/or in Abbeel's Robot Learning Lab. The company rebranded to Covariant in 2019 and became one of the most prominent AI-for-robotics startups, focused on teaching robots to pick and handle arbitrary objects in warehouse and fulfillment center environments.

## Technology

Covariant's core product, the **Covariant Brain**, uses AI trained on what the company describes as the largest multimodal robotics dataset collected from real warehouse operations worldwide. This enables robots to handle novel items without per-SKU programming.

In March 2024, the company unveiled **RFM-1** (Robotics Foundation Model), an 8-billion-parameter multimodal transformer trained on text, images, video, robot actions, and sensor readings. RFM-1 was notable for:

- **Physics understanding**: Generating simulated video predictions of how objects react to robotic actions.
- **Language-based tasking**: Allowing human operators to communicate with robots in natural language.
- **In-context learning**: Enabling robots to adapt their picking strategies on the fly when initial attempts fail.

## Funding History

Covariant raised **$222 million** across seed through Series C extension rounds from 2017 to 2023. Key investors included **Index Ventures** (led multiple rounds), **Radical Ventures**, **Amplify Partners**, **Canada Pension Plan Investment Board (CPPIB)**, and **Gates Frontier Holdings**. The final round in April 2023 valued the company at approximately **$625 million**.

## The Amazon Deal (August 2024)

On August 30, 2024, Amazon announced what was structured as a talent hire and licensing agreement -- not a formal acquisition:

- **Three co-founders** (Abbeel, Chen, Duan) joined Amazon, along with roughly **25% of Covariant's workforce**.
- Amazon obtained a **non-exclusive license** to Covariant's AI models, robotics software, patents, and training data.
- The deal was valued at **$380 million** upfront, with a **$20 million** final payment due one year later (total: ~$400M).
- Covariant continued to exist as an independent entity under new leadership (CEO Ted Stinson, co-founder Tianhao Zhang).

This deal followed a pattern seen across Big Tech in 2024-2025 (similar to Microsoft/Inflection AI, Amazon/Adept), where major companies effectively absorbed AI startups without triggering formal merger review.

## Whistleblower Complaint and Antitrust Scrutiny

In January 2025, the **Washington Post** reported on a whistleblower complaint filed with the **FTC**, **SEC**, and **DOJ**, alleging that:

- Amazon structured the deal specifically to **avoid premerger antitrust reporting** (the $380M exceeded the $119.5M Hart-Scott-Rodino threshold).
- The agreement included **heavy restrictions** on Covariant's ability to sell or license its technology to other companies, with financial penalties for violations.
- The arrangement effectively turned Covariant into a **"zombie" company** -- still nominally independent but hollowed out of its core talent and constrained in what it could do with its own technology.

The FTC confirmed it was reviewing the complaint but declined further comment. As of early 2026, no public enforcement action has been announced. [Uncertainty: the current status of the FTC review is unclear.]

## Impact on Amazon Robotics

Amazon reportedly leveraged Covariant's technology to accelerate its robotics pipeline. In October 2025, Amazon Robotics launched **Blue Jay**, a six-arm robot that moved from concept to production in roughly one year -- a process that previously took three or more years. Amazon attributed the accelerated timeline to "advancements in AI," though it did not explicitly credit Covariant.

## Current Status (as of March 2026)

Covariant continues to operate under Ted Stinson (CEO) and Tianhao Zhang, with approximately **56 employees**. The company maintains its Covariant Brain product and customer relationships, including a 5+ year partnership with KNAPP. However, with its three most prominent co-founders at Amazon and significant restrictions on its business, the company's long-term independent viability remains uncertain. Some industry observers have characterized it as one of several "AI zombie" companies resulting from Big Tech reverse acquihires.

[Note: Specific details on Covariant's 2025-2026 commercial traction, revenue, and whether it has successfully signed new customers post-deal are not publicly available as of this writing.]

## Sources

- [Amazon-Covariant announcement (Amazon)](https://www.aboutamazon.com/news/company-news/amazon-covariant-ai-robots)
- [Amazon hires Covariant founders (TechCrunch)](https://techcrunch.com/2024/08/31/amazon-hires-the-founders-of-robotics-ai-startup-covariant/)
- [Amazon hires Covariant founders, inks licensing deal (GeekWire)](https://www.geekwire.com/2024/amazon-hires-covariant-founders-inks-licensing-deal-with-robotics-ai-startup-in-latest-reverse-acquihire-deal/)
- [Whistleblower complaint (Washington Post)](https://www.washingtonpost.com/technology/2025/01/18/amazon-antitrust-ai-whistleblower/)
- [Whistleblower deep dive (Hard Reset Media)](https://www.hardresetmedia.com/p/whistleblower-ftc-complaint-about-amazon-covariant)
- [Unpacking Amazon's unique Covariant deal (The Robot Report)](https://www.therobotreport.com/unpacking-amazons-unique-covariant-ai-acquisition/)
- [AI zombie startups (CNBC)](https://www.cnbc.com/2025/08/19/how-ai-zombie-deals-work-meta-google.html)
- [Covariant Wikipedia](https://en.wikipedia.org/wiki/Covariant_(company))
- [Series C extension ($75M) (TechCrunch)](https://techcrunch.com/2023/04/04/covariants-robotic-picking-at-nabs-another-75m/)
- [Series C ($80M) (TechCrunch)](https://techcrunch.com/2021/07/27/robotic-ai-firm-covariant-raises-another-80-million/)
- [RFM-1 announcement (Covariant)](https://covariant.ai/insights/introducing-rfm-1-giving-robots-human-like-reasoning-capabilities/)
- [Covariant next phase blog post](https://covariant.ai/insights/introducing-the-next-phase-of-our-ai-robotics-journey/)
- [Index Ventures on Series C](https://www.indexventures.com/perspectives/congratulations-to-covariant-on-their-75m-series-c/)
