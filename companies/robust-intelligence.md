---
name: Robust Intelligence
slug: robust-intelligence
founded: 2019
headquarters: San Francisco, CA (originally Cambridge, MA)
status: Acquired by Cisco (October 2024)
acquisition_price_reported: ~$400M (unofficial; Cisco did not publicly confirm)
sector: AI Security & Validation
total_funding: ~$44M
latest_round: Series B ($30M, December 2021)
key_investors:
- Tiger Global Management (Series B lead)
- Sequoia Capital (Seed & Series A lead)
- Harpoon Ventures
- Engineering Capital
- In-Q-Tel (U.S. intelligence community VC)
- Cisco Investments
- Sherpalo Ventures
founders:
- name: Yaron Singer
  role: CEO & Co-Founder
  background: 'Tenured Professor of Computer Science & Applied Mathematics at Harvard (Gordon McKay Professor). Israeli-born.
    PhD from UC Berkeley. Previously researcher at Google AI and consulting researcher at Microsoft. Now VP of AI & Engineering
    at Cisco Security / Foundation AI.

    '
  origin: Israeli-American
- name: Kojin Oshiba
  role: Co-Founder
  background: 'BA in Computer Science & Statistics from Harvard. Grew up in Japan. Previously ML engineer at QuantCo; co-founded
    its Japan branch. Published at ICML and NeurIPS. Forbes 30 Under 30 in Enterprise Technology (2024). Now leads AI organization
    at Cisco post-acquisition.

    '
  origin: Japanese-American
employees_at_acquisition: ~70
revenue_at_acquisition: ~$10M (reported)
profile_updated: 2026-03-20
one_liner: Robust Intelligence was an AI security and validation platform founded in 2019 as a spinout of Harvard University
website: https://www.robustintelligence.com
website_verified: false
data_notes: 'Website URL may be invalid (Connection failed). '
crunchbase: https://www.crunchbase.com/organization/robust-intelligence
crunchbase_verified: true
total_raised_m: 44
funding_rounds:
  - stage: "Seed"
    date: "2019"
    amount_m: 3
    lead_investors: ["Sequoia Capital"]
    source: "https://www.crunchbase.com/organization/robust-intelligence"
  - stage: "Series A"
    date: "2020-02"
    amount_m: 11
    lead_investors: ["Sequoia Capital"]
    source: "https://www.crunchbase.com/organization/robust-intelligence"
  - stage: "Series B"
    date: "2021-12"
    amount_m: 30
    lead_investors: ["Tiger Global Management"]
    source: "https://www.crunchbase.com/organization/robust-intelligence"
data_notes: "Acquired by Cisco in October 2024 for ~$400M."
---

# Robust Intelligence

## Overview

Robust Intelligence was an AI security and validation platform founded in 2019 as a spinout of Harvard University. The company pioneered the category of automated AI security, building what it called the industry's first **AI Firewall** -- a system that continuously tested and protected AI models before and during production deployment. In October 2024, Cisco acquired the company for a reported ~$400 million, folding its technology and team into what became **Cisco AI Defense** and **Cisco Foundation AI**.

## Founders & Origins

The company was born from academic research at Harvard's School of Engineering and Applied Sciences (SEAS). **Yaron Singer**, a tenured professor specializing in machine learning robustness, optimization, and algorithms, partnered with **Kojin Oshiba**, one of his undergraduate students, after years of joint research into adversarial ML. Singer is Israeli-born, holds a PhD from UC Berkeley, and had previously worked at Google Research. Oshiba grew up in Japan, studied CS and statistics at Harvard, and had co-founded the Japan branch of QuantCo (a data science company) before Robust Intelligence.

The founding thesis was straightforward: as enterprises deployed ML models into high-stakes decisions (finance, healthcare, autonomous systems), there was no systematic way to validate whether those models were secure, fair, or reliable. Singer and Oshiba set out to automate that validation.

## Funding History

| Round | Date | Amount | Lead Investor | Notable Participants |
|-------|------|--------|--------------|---------------------|
| Seed | ~2019 | ~$3M | Sequoia Capital | Engineering Capital, Harpoon Ventures |
| Series A | Feb/Mar 2020 | ~$11M | Sequoia Capital | Engineering Capital, Harpoon Ventures |
| Series B | Dec 2021 | $30M | Tiger Global Management | Sequoia Capital, Harpoon, Engineering Capital |

**Total raised:** ~$44M across all rounds. In-Q-Tel (the U.S. intelligence community's strategic VC) and Cisco Investments also participated at various stages. The company came out of stealth in late 2020 announcing the combined $14M seed + Series A.

## Product & Technology

Robust Intelligence's platform addressed three core use cases:

1. **AI Firewall (Real-Time Protection):** Sat in front of deployed AI models (including LLMs) and blocked malicious inputs -- prompt injection, jailbreaking, data poisoning -- in real time. This was their signature product and a category-defining innovation.

2. **Continuous Validation:** Automated testing of models across their lifecycle for performance degradation, data drift, broken pipelines, bias, and security vulnerabilities. Ran hundreds of pre-built tests without requiring custom code.

3. **AI Governance & Compliance:** Translated statistical test results into outputs mapped to regulatory frameworks (EU AI Act, NIST AI RMF, etc.), simplifying audit and compliance.

A key technical contribution was **algorithmic red teaming** -- automated adversarial testing of models to find failure modes before attackers do.

## Business Model

Enterprise SaaS. The platform was sold to large organizations on a subscription basis, providing continuous monitoring and protection for AI deployments. Revenue at the time of acquisition was reportedly ~$10 million, suggesting the company was still in early commercial traction relative to its valuation.

## Customers

Known enterprise customers included:

- **NEC** -- Evaluated LLM performance and eliminated risk using the platform.
- **Seven Bank (Japan)** -- Used Robust Intelligence to ensure quality of AI models powering ATM and financial services, guarding against behavioral drift.
- **CrowdStrike** -- Leveraged the platform so security teams could prioritize safety while developing AI applications at scale.
- **F5 Networks** -- Partnered with Robust Intelligence for AI application security.

The company also had traction with U.S. government and intelligence agencies, evidenced by In-Q-Tel's investment.

## Cisco Acquisition (2024)

- **Announced:** August 28, 2024
- **Completed:** ~September/October 2024
- **Reported price:** ~$400 million (per Calcalist/CTech and other sources; Cisco did not officially confirm the figure)
- **Context:** Cisco had been an investor via Cisco Investments for approximately two years prior. The acquisition gave Cisco a purpose-built AI security engine to embed into its networking and security product portfolio.

Post-acquisition, Robust Intelligence's technology became foundational to two Cisco initiatives:

- **Cisco AI Defense** -- An enterprise product that secures AI applications across the full lifecycle.
- **Cisco Foundation AI** -- A new organization within Cisco Security, announced April 2025, led by Yaron Singer (now VP of AI & Engineering). Foundation AI builds cybersecurity-specific AI models and tools, including the open-source Foundation-sec-8B model and reasoning systems for threat hunting.

As of early 2026, Singer continues to lead Foundation AI, which has released agentic security systems, adaptive retrieval frameworks, and the PEAK Threat Hunting Assistant.

## What Makes Them Interesting

1. **Category creator:** Robust Intelligence essentially defined the "AI Firewall" product category before most enterprises recognized AI security as a distinct problem. They were building AI validation tooling years before the GenAI boom made it urgent.

2. **Academic-to-startup pipeline:** A textbook example of deep research (Harvard professor + student) translating into a venture-backed company. The founding team's publication record at ICML and NeurIPS gave the product genuine technical credibility.

3. **Strategic acquirer validation:** The $400M acquisition by Cisco -- at roughly 40x reported revenue -- signals that large platform companies view AI security as critical infrastructure, not optional tooling.

4. **Intelligence community interest:** In-Q-Tel's involvement indicates the U.S. government considered AI model security a national security priority, lending further credibility.

5. **Timing and positioning:** Founded in 2019 (pre-GPT era), the company was well-positioned when the 2023-2024 GenAI explosion made prompt injection, jailbreaking, and model governance suddenly top-of-mind for every CISO.

6. **Post-acquisition impact:** Rather than being absorbed quietly, the Robust Intelligence team became the nucleus of Cisco's entire AI security strategy (Foundation AI), suggesting the acquisition was talent- and vision-driven, not just technology acqui-hire.

## Key Uncertainties

- The $400M acquisition price is widely reported but was never officially confirmed by Cisco.
- Exact revenue figures (~$10M) come from press reports and may not be precise.
- The breakdown of government vs. commercial revenue is unclear.
- It is not confirmed whether Kojin Oshiba remains at Cisco as of March 2026.

## Sources

- [Cisco Blog: Fortifying the Future of Security for AI](https://blogs.cisco.com/news/fortifying-the-future-of-security-for-ai-cisco-announces-intent-to-acquire-robust-intelligence)
- [Robust Intelligence Is Now Part of Cisco](https://www.robustintelligence.com/)
- [CTech: Inside Yaron Singer's Surprising $400M Sale to Cisco](https://www.calcalistech.com/ctechnews/article/rjgsb5npa)
- [Harvard SEAS: Startup Raises $14M](https://seas.harvard.edu/news/2020/10/seas-startup-raises-14m)
- [CTech: Israeli Harvard Professor Raises $30M from Tiger Global and Sequoia](https://www.calcalistech.com/ctech/articles/0,7340,L-3924649,00.html)
- [Robust Intelligence Series B Announcement](https://www.robustintelligence.com/blog-posts/announcing-robust-intelligences-30m-series-b)
- [Cisco Blog: Foundation AI - Building the Intelligent Future of Cybersecurity](https://blogs.cisco.com/security/foundation-ai-building-the-intelligent-future-of-cybersecurity)
- [Cisco Blog: Foundation AI Advances Agentic Security Systems](https://blogs.cisco.com/security/foundation-ai-advances-agentic-security-systems-for-ai-era)
- [F5 and Robust Intelligence Partnership](https://www.f5.com/company/blog/robust-intelligence-leading-edge-ai-application-security)
- [Crunchbase: Robust Intelligence](https://www.crunchbase.com/organization/robust-intelligence)
- [Tracxn: Robust Intelligence Funding & Investors](https://tracxn.com/d/companies/robust-intelligence/__ONz7_Uehh-r2U_U2oItHeiG90TQR80kJji6NLyKdNm4/funding-and-investors)
- [YSecurity: Robust Intelligence Case Study - SOC 2 to $400M Cisco Acquisition](https://www.ysecurity.io/customers/soc-2-type-2-robust-intelligence)
- [Kojin Oshiba Personal Site](https://kojinoshiba.com/)
