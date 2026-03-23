---
company: Bland AI
website: https://www.bland.ai
domain: AI Phone Calling Agents / Conversational Voice AI
founded: 2023
headquarters: San Francisco, CA
founders:
- name: Isaiah N. Granet
  role: Co-Founder & CEO
  origin: American
- name: Sobhan Nejad
  role: Co-Founder & COO
  origin: Iranian-American
headcount_estimate: 65-107 (sources vary; Y Combinator reports 65, PitchBook reports 107)
total_funding: $65M (across 3 rounds)
latest_round: Series B - $40M (January 2025)
lead_investors:
- Emergence Capital (Series B)
- Scale Venture Partners (Series A)
- Y Combinator (Seed / W24 batch)
notable_angels:
- Max Levchin (PayPal co-founder)
- Jeff Lawson (Twilio founder)
- Piotr Dabkowski
yc_batch: W24
valuation: undisclosed
last_updated: 2026-03-20
confidence: high on funding and founders; moderate on headcount and revenue
one_liner: Enterprise platform for automating phone calls with AI voice agents that sound human, handling both inbound and
  outbound calls at scale
website_verified: true
crunchbase: https://www.crunchbase.com/organization/bland-ai
crunchbase_verified: true
linkedin: https://www.linkedin.com/company/bland-ai
twitter: '@usebland'
total_raised_m: 65
funding_rounds:
- stage: Seed
  date: 2023-2024
  amount_m: 9
  lead_investors:
  - Y Combinator
  source: https://www.crunchbase.com/organization/bland-ai
- stage: Series A
  date: 2024-08
  amount_m: 16
  lead_investors:
  - Scale Venture Partners
  source: https://www.crunchbase.com/organization/bland-ai
- stage: Series B
  date: 2025-01
  amount_m: 40
  lead_investors:
  - Emergence Capital
  source: https://www.crunchbase.com/organization/bland-ai
name: Bland AI
linkedin_verified: true
---

# Bland AI

## One-Liner

Enterprise platform for automating phone calls with AI voice agents that sound human, handling both inbound and outbound calls at scale.

## Company Overview

Bland AI builds programmable AI phone agents for enterprises. The platform replaces or augments human call center agents for use cases including customer support, sales, appointment scheduling, payment reminders, and lead qualification. Bland controls the entire technology stack -- hardware, models, and servers -- claiming zero dependency on third-party AI providers like OpenAI or Anthropic.

The company emerged from Y Combinator's W24 batch and has grown rapidly, raising $65M total across seed, Series A, and Series B rounds in under two years.

## Founders and Team

### Isaiah N. Granet (CEO)

- Studied Computer Science and Economics at Washington University in St. Louis (BS 2022).
- After graduating, worked as a software engineer at Lantern, an AI startup.
- Met Sobhan Nejad while both were working at early-stage startups; they bonded over software development and launched Bland together in 2023.

### Sobhan Nejad (COO)

- Self-taught path into tech: applied to UCLA, Stanford, and UC Berkeley but was rejected from all of them. Instead of attending community college, he began cold-emailing and cold-calling startup founders.
- Landed a remote internship and later a full-time role at Shogun (an e-commerce platform startup).
- His personal experience with cold calling reportedly informed Bland's product direction.

### Notable Team Members

- **Noah Kravitz** -- heads GTM (go-to-market); also a WashU alum (BS 2022).

The founding story is notable: two young builders who skipped or took unconventional routes through higher education, met in the startup ecosystem, and shipped a product that resonated with enterprise buyers almost immediately.

## Funding History

| Round    | Date          | Amount | Lead Investor         | Notable Participants                          |
|----------|---------------|--------|-----------------------|-----------------------------------------------|
| Seed     | 2023-2024     | ~$9M*  | Y Combinator          | --                                            |
| Series A | August 2024   | $16M   | Scale Venture Partners| Y Combinator, Max Levchin, Jeff Lawson        |
| Series B | January 2025  | $40M   | Emergence Capital      | Yaz El-Baba (board), Gordon Ritter (observer) |

*Seed amount is inferred ($65M total minus $16M Series A minus $40M Series B). Some sources report total raised as $59.6M, which would put the seed closer to ~$3.6M. The exact seed figure is uncertain.

## Business Model

### Pricing (as of late 2025 / early 2026)

Bland uses a **tiered subscription + per-minute usage** model:

- **Start plan**: $0.14/min
- **Build plan**: $299/month (lower per-minute rate)
- **Scale plan**: $499/month (lowest per-minute rate, ~$0.09/min)

Enterprise customers get dedicated instances with options for on-premise or VPC deployment.

### Revenue Indicators

- One customer (MPA) publicly stated Bland added "$42 million in tangible revenue" to their business in a few months (per Bland case study).
- Getlatka reported $3.8M in revenue with a 25-person team in 2024, though this figure may be outdated given subsequent growth.
- Revenue figures are not officially disclosed as Bland is a private company.

## Technology

Bland operates a **fully vertically integrated voice AI stack**:

1. **Proprietary transcription model** -- converts incoming audio to text in real time.
2. **Language model / inference engine** -- determines agent response (served on optimized V100 GPUs).
3. **Proprietary text-to-speech (TTS)** -- generates human-sounding audio output; supports voice cloning from a short MP3 sample with no fine-tuning.
4. **Edge delivery network** -- low-latency infrastructure for real-time conversation.

Key technical claims:
- ~800ms average voice latency
- Up to 1 million concurrent conversations
- Complete data sovereignty (self-hosted models, no third-party LLM dependency)
- Enterprise-grade security with dedicated instances per customer

## Customers

Named enterprise customers include:

- **Better.com** (mortgage lending)
- **Sears** (retail)
- **Cleveland Cavaliers** (NBA franchise)
- **MPA** (claimed $42M revenue impact)

Use cases span customer support automation, outbound sales, appointment reminders, payment notifications, and lead qualification.

## Competitive Landscape

Bland competes in the rapidly growing voice AI agent market. Key competitors:

| Competitor     | Differentiator                                      |
|----------------|-----------------------------------------------------|
| **Retell AI**  | Lower pricing ($0.07/min), ~600ms latency, G2 2026 award winner |
| **Vapi**       | API-first, 4,200+ config points, BYO model support |
| **Synthflow**  | No-code builder, SMB-friendly                       |
| **Cognigy**    | Enterprise conversational AI with omnichannel focus |

Bland's primary differentiators are: (1) full stack ownership with zero third-party AI dependency, (2) scale capacity (1M concurrent calls), and (3) enterprise-grade data sovereignty / on-premise deployment options.

## What Makes Bland Interesting

1. **Vertical integration at speed.** Unlike most voice AI startups that assemble third-party STT, LLM, and TTS components, Bland built proprietary models across the entire stack. This gives them control over latency, cost, and data privacy -- a significant moat if the models are genuinely competitive.

2. **Unconventional founder backgrounds.** Both founders took non-traditional paths (one self-taught, one fresh out of undergrad). Sobhan Nejad's personal experience with cold calling directly shaped the product. The team has shipped at remarkable velocity -- going from founding to $65M raised in under two years.

3. **Enterprise traction early.** Landing customers like Better.com, Sears, and the Cleveland Cavaliers while still a very young company suggests strong product-market fit in the enterprise segment.

4. **Market timing.** The call center industry is massive (~$340B globally) and ripe for AI disruption. Phone calls remain the primary customer service channel for many industries (healthcare, financial services, insurance), and Bland is positioned at the intersection of this legacy infrastructure and modern AI capabilities.

5. **Investor signal quality.** Backing from Max Levchin (PayPal), Jeff Lawson (Twilio -- the company that built programmable telephony), and Emergence Capital (enterprise SaaS specialists) is a strong endorsement of both the team and the market opportunity.

## Open Questions / Uncertainties

- Exact seed round size and current valuation are not publicly confirmed.
- Headcount varies across sources (65 to 107); rapid hiring may explain the discrepancy.
- Specific revenue and growth metrics are not publicly disclosed.
- The claim of "zero dependency on OpenAI or Anthropic" for the language model layer deserves scrutiny -- it is unclear whether their proprietary inference models match frontier LLM quality for complex conversations.
- Competitive pricing pressure from Retell AI and others ($0.07/min vs. Bland's $0.09-$0.14/min) could affect market share in price-sensitive segments.

## Sources

- [Bland AI Official Website](https://www.bland.ai/)
- [Y Combinator - Bland AI Profile](https://www.ycombinator.com/companies/bland-ai)
- [WashU Skandalaris Center - $40M Series B Announcement](https://skandalaris.wustl.edu/blog/2025/01/30/washu-ai-startup-bland-com-announces-40m-series-b-funding-round-to-change-outdated-enterprise-call-practices/)
- [BusinessWire - $16M Series A Announcement](https://www.businesswire.com/news/home/20240828040767/en/Conversational-AI-Platform-Bland-AI-Raises-$16M-to-Change-Outdated-Enterprise-Call-Practices-With-Automated-Phone-Agents)
- [AI Magazine - Bland's $65M Funding](https://aimagazine.com/articles/bland-whats-behind-the-ai-phone-startups-funding-of-65m)
- [Emergence Capital - Why We're Backing Bland](https://www.emcap.com/thoughts/ai-that-speaks-volumes-why-were-backing-bland)
- [Bland AI Series A Announcement on X](https://x.com/usebland/status/1828882563588612233)
- [VentureBeat - Bland AI Scores $16M](https://venturebeat.com/ai/bland-ai-scores-16m-to-automate-enterprise-phone-calls-with-agents/)
- [Cognigy - Bland AI Overview & Alternatives 2025](https://www.cognigy.com/blog/bland-ai-company-overview-best-alternatives-in-2025)
- [Bland Voice Product Page](https://www.bland.ai/product/bland-voice)
- [Getlatka - Bland Revenue Data](https://getlatka.com/companies/bland.com)
- [Bland AI 2025 Product Recap](https://www.bland.ai/blogs/2025-bland-product-recap)
- [OpenPR - Bland AI Ranked #1 Conversational AI Platform 2026](https://www.openpr.com/news/4426714/bland-ai-ranked-1-conversational-ai-platform-for-2026)
