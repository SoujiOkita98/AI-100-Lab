---
founded: 2022
headquarters: San Francisco, CA
sector: AI Agents / Enterprise Automation
status: Effectively gutted via Amazon acqui-hire (June 2024); nominally independent with ~20 employees
website: https://www.adept.ai
peak_valuation: ~$1B (Series B, March 2023)
key_event: Amazon acqui-hire of co-founders and ~66% of staff (June 2024)
current_ceo: Zach Brock (formerly Head of Engineering)
founders:
- name: David Luan
  role: Co-Founder & former CEO (now at Amazon)
  background: Led Google's large model program. Former head of engineering at OpenAI.
  origin: Chinese-American (inferred from name)
- name: Ashish Vaswani
  role: Co-Founder & former Chief Scientist (left for Essential AI)
  background: Co-author of the Transformer paper ('Attention Is All You Need'). Former Google Brain researcher.
  origin: Indian (inferred from name)
- name: Niki Parmar
  role: Co-Founder & former CTO (left for Essential AI)
  background: Co-author of the Transformer paper. Former Google Brain researcher.
  origin: Indian (inferred from name)
profile_created: 2026-03-20
confidence: high
funding_rounds:
- stage: Series A
  date: 2022-04
  amount_m: 65.0
  lead_investors:
  - Addition
  - Greylock
  source: https://www.crunchbase.com/funding_round/adept-48e7-series-a--03865118
- stage: Series B
  date: 2023-03
  amount_m: 350.0
  valuation_m: 1000.0
  lead_investors:
  - General Catalyst
  - Spark Capital
  source: https://techcrunch.com/2023/03/15/adept-a-startup-training-ai-to-use-existing-software-and-apis-raises-350m/
  notes: Acquired by Amazon June 2024.
one_liner: Adept AI was founded in 2022 to build AI agents that could interact with any software on behalf of users — an "agentic
  AI" company before the term became mainstream
website_verified: true
linkedin: https://www.linkedin.com/company/adeptai
crunchbase: https://www.crunchbase.com/organization/adept-ai
crunchbase_verified: true
name: Adept AI
linkedin_verified: true
total_raised_m: 415.0
---

# Adept AI

## Overview

Adept AI was founded in 2022 to build AI agents that could interact with any software on behalf of users — an "agentic AI" company before the term became mainstream. The company's vision was a general-purpose AI teammate that could operate enterprise software tools (clicking buttons, filling forms, navigating workflows) using natural-language instructions. Adept was notable for assembling an extraordinary founding team that included co-authors of the original Transformer paper ("Attention Is All You Need," 2017).

In practice, Adept became one of the most dramatic cautionary tales in the AI startup era: after raising over $400M and reaching unicorn status, its founding team fragmented, and the company was effectively absorbed by Amazon through an acqui-hire deal in mid-2024.

## Founders

| Name | Role at Adept | Background | Post-Adept |
|------|---------------|------------|------------|
| **David Luan** | Co-founder & CEO | VP Engineering at OpenAI (2017-2020); led GPT, CLIP, DALL-E teams. Previously at Google Research. | Joined Amazon as VP of Autonomy / AGI Lab head (June 2024). Left Amazon in Feb 2026 "to cook up something new." |
| **Ashish Vaswani** | Co-founder & Chief Scientist | Lead author of "Attention Is All You Need" (Transformer paper). Google Brain. | Left Adept ~Nov 2022 over reported differences with investors. Co-founded **Essential AI** in 2023 with Niki Parmar. |
| **Niki Parmar** | Co-founder & CTO | Co-author of Transformer paper. Google Brain. | Left Adept ~Nov 2022 alongside Vaswani. Co-founded **Essential AI**. Later joined **Anthropic**. |
| **Kelsey Szot** | Co-founder | ML research background | Joined Amazon (June 2024) |
| **Augustus Odena** | Co-founder | Google Brain alumni | Joined Amazon (June 2024); subsequently left |
| **Maxwell Nye** | Co-founder | ML researcher | Joined Amazon (June 2024); subsequently left |
| **Erich Elsen** | Co-founder | DeepMind alumni | Joined Amazon (June 2024); subsequently left |

**Key observation:** Two original Transformer co-authors (Vaswani, Parmar) departed within months of founding, well before the Amazon deal. The remaining co-founders all left for Amazon in 2024, and by early 2026, four of the five who joined Amazon had departed that company as well.

## Funding History

| Round | Date | Amount | Lead Investors | Valuation |
|-------|------|--------|----------------|-----------|
| Seed | 2022 (est.) | ~$65M | Addition, Greylock | Undisclosed |
| Series A | April 2022 | ~$65M | Addition, Greylock | Undisclosed |
| Series B | March 2023 | $350M | General Catalyst, Spark Capital | ~$1B (pre-money ~$650M) |
| **Total** | | **~$415M** | | |

Other notable investors included Atlassian Ventures, Microsoft (via M12), and Workday Ventures.

**Note:** Some sources conflate the seed and Series A as a single $65M raise announced at launch in April 2022. The exact breakdown between seed and Series A is ambiguous in public reporting.

## Product & Technology

Adept's core product was **ACT-1** (Action Transformer), an AI model trained to take actions in software — clicking, typing, navigating — based on natural language commands. The system could operate across web browsers and desktop applications.

Key technical bets:
- **Multimodal action models**: Models that could "see" screens and take actions, not just generate text
- **Web interaction infrastructure**: Custom tooling for browser automation and software interaction
- **Agentic data pipelines**: Proprietary datasets of human-software interactions

The product was positioned for enterprise knowledge workers who spend time on repetitive software workflows (CRM updates, data entry, report generation, etc.).

## The Amazon Deal (June 2024)

### What Happened

On June 28, 2024, Amazon announced it had hired Adept's CEO David Luan and co-founders Augustus Odena, Maxwell Nye, Erich Elsen, and Kelsey Szot, along with approximately two-thirds of Adept's staff. Simultaneously, Amazon secured a **non-exclusive license** to Adept's AI models, datasets, and technology.

### Deal Economics

- Amazon paid Adept a **$25M licensing fee** (some reports suggest the total payout was higher)
- Investors (Greylock, General Catalyst, Spark Capital, et al.) **roughly recouped their ~$414M investment** through the deal
- This was structured to avoid triggering formal merger review (HSR filing) since Adept's corporate ownership technically did not change

### Why It Matters

The deal was a textbook "reverse acqui-hire" — Amazon got the talent and technology without technically acquiring the company. This structure drew immediate regulatory attention.

## FTC Investigation

The U.S. Federal Trade Commission opened an inquiry into the Amazon-Adept arrangement, sending formal questions to Amazon about the deal's structure. The FTC's concern: whether tech giants were using acqui-hire structures to absorb AI startups while circumventing merger notification requirements.

The Amazon-Adept deal was investigated alongside similar arrangements (notably Microsoft-Inflection AI and Amazon's broader investment in Anthropic). **As of March 2026, no public enforcement action has been announced** against the Amazon-Adept deal specifically. [Uncertainty: the FTC investigation may have concluded quietly or may still be ongoing.]

## At Amazon: The AGI Lab

At Amazon, David Luan led a newly established **AGI Lab** (formalized December 2024) based in San Francisco. The lab's flagship output was **Nova Act**, an AI model and developer toolkit for building agents that perform tasks autonomously in web browsers, unveiled in March 2025. This was a direct continuation of Adept's core technology vision, now backed by Amazon's resources.

However, the arrangement proved unstable:
- By early 2026, **four of the five Adept co-founders** who joined Amazon had left the company
- **David Luan announced his departure** from Amazon on February 24, 2026, saying he planned "to cook up something new" and that he had "a bet for what's next"

## Current Status (March 2026)

### Adept AI (the company)
- Continues to operate independently under CEO **Zach Brock** (former Head of Engineering) with ~20 remaining employees
- **Tim Weingarten** serves as Head of Product
- Company says it continues to develop agentic AI solutions using its remaining in-house models and infrastructure
- Effective operating capacity is severely diminished compared to peak
- [Uncertainty: it is unclear whether Adept has meaningful revenue, active enterprise customers, or a viable path forward as an independent entity]

### Former Adept Team
- **David Luan**: Left Amazon Feb 2026; next venture unannounced
- **Ashish Vaswani & Niki Parmar**: Running Essential AI (since 2023); Parmar has also been reported to have joined Anthropic
- **Other co-founders (Odena, Nye, Elsen, Szot)**: Left Amazon; current whereabouts not widely reported

## Key Takeaways

1. **Talent fragmentation killed the company before the market did.** The departure of Vaswani and Parmar in late 2022 — barely months after founding — was an early red flag. The Amazon acqui-hire completed the dissolution.

2. **The "reverse acqui-hire" became a regulatory flashpoint.** The Adept-Amazon deal, alongside Microsoft-Inflection, became central examples in the FTC's scrutiny of Big Tech's AI talent acquisition strategies.

3. **$415M in venture capital produced no durable standalone company.** Investors were made roughly whole through the Amazon deal structure, but the original vision of an independent Adept product company was never realized.

4. **The agentic AI thesis was validated, but by others.** The category Adept helped pioneer (AI agents that operate software) became one of the hottest areas in AI by 2025-2026, with competitors like Anthropic (computer use), OpenAI (Operator), and numerous startups executing on similar visions.

## Sources

- [Amazon hires founders away from AI startup Adept — TechCrunch (June 2024)](https://techcrunch.com/2024/06/28/amazon-hires-founders-away-from-ai-startup-adept/)
- [Amazon beefs up AI development, hiring execs from startup Adept — CNBC](https://www.cnbc.com/2024/06/28/amazon-hires-execs-from-ai-startup-adept-and-licenses-its-technology.html)
- [Investors in Adept AI will be paid back after Amazon hires top talent — Semafor](https://www.semafor.com/article/08/02/2024/investors-in-adept-ai-will-be-paid-back-after-amazon-hires-startups-top-talent)
- [Head of Amazon's AGI lab is leaving — GeekWire (Feb 2026)](https://www.geekwire.com/2026/head-of-amazons-agi-lab-is-leaving-in-latest-exit-from-high-profile-adept-deal/)
- [Head of Amazon's AGI lab is leaving the company — CNBC (Feb 2026)](https://www.cnbc.com/2026/02/24/head-of-amazons-agi-lab-is-leaving-the-company.html)
- [FTC is looking into Amazon's deal with AI startup Adept — Computerworld](https://www.computerworld.com/article/2518584/ftc-is-looking-into-amazons-deal-with-ai-startup-adept.html)
- [Amazon AGI Labs chief defends his reverse acqui-hire — TechCrunch (Aug 2025)](https://techcrunch.com/2025/08/23/amazon-agi-labs-chief-defends-his-reverse-acquihire/)
- [Adept, a startup training AI to use existing software and APIs, raises $350M — TechCrunch (March 2023)](https://techcrunch.com/2023/03/15/adept-a-startup-training-ai-to-use-existing-software-and-apis-raises-350m/)
- [An update from Adept (official blog)](https://www.adept.ai/blog/adept-update/)
- [Ashish Vaswani — Wikipedia](https://en.wikipedia.org/wiki/Ashish_Vaswani)
- [Transformer co-author Niki Parmar joins Anthropic — AIM](https://analyticsindiamag.com/ai-news-updates/transformer-co-author-niki-parmar-joins-anthropic-after-founding-two-ai-startups/)
- [FTC Eyes Reverse Acquihires in AI Sector — American Action Forum](https://www.americanactionforum.org/insight/ftc-eyes-reverse-acquihires-in-ai-sector/)
