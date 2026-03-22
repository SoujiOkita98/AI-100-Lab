---
name: Assembled
slug: assembled
founded: 2018
headquarters: San Francisco, CA
website: https://www.assembled.com
sector: AI-Powered Support Operations / Workforce Management
stage: Series B
total_funding_raised: $70.7M
latest_round: Series B ($51M, May 2022)
valuation_estimate: Not publicly disclosed; Series B represented >5x valuation increase over Series A
founders:
- name: Ryan Wang
  role: Co-Founder & CEO
  background: 'ML Engineer at Stripe (~employee #80); M.S. Statistics & B.A. Economics, University of Chicago'
  origin: Chinese-American
- name: John Wang
  role: Co-Founder & CTO
  background: 'Software Engineer at Stripe (~employee #100); B.S. Computer Science, MIT; prev. Palantir, 37signals, co-founded
    Zinc'
  origin: Chinese-American
- name: Brian Sze
  role: Co-Founder
  background: Head of Business Operations at Stripe (2012-2016, employee ~30-500 scale); B.A. Economics, Stanford; prev. Obama
    for America analytics team
  origin: Chinese-American
key_investors:
- New Enterprise Associates (NEA) — led Series B
- Emergence Capital — led Series A
- Stripe — led Seed
- Basis Set Ventures
- Felicis Ventures
employee_count_estimate: ~75-150 (uncertain; 75 reported on some trackers, likely grown since 2022)
customers_notable:
- Stripe
- Etsy
- Robinhood
- Salesforce
- Zoom
- Intuit
- TaskRabbit
- Asana
- Thrasio
- Honeylove
- Ashley Furniture
- Restaurant Brands International
customer_count: 300+ (as of late 2025)
last_updated: 2026-03-20
confidence: high on funding/founders; moderate on revenue and employee count
one_liner: AI-powered support operations platform that unifies workforce management, AI agent automation, and BPO oversight
  for enterprise customer service teams
website_verified: true
linkedin: https://www.linkedin.com/company/assembledhq
---

# Assembled

## One-Liner

AI-powered support operations platform that unifies workforce management, AI agent automation, and BPO oversight for enterprise customer service teams.

## Overview

Assembled builds the operating system for modern customer support. The company started as a workforce management (WFM) tool — forecasting ticket volumes, scheduling agents, and tracking real-time performance — and has expanded into an AI-first platform that can autonomously resolve support interactions while orchestrating human agents and BPO vendors in a single pane of glass. Their largest reported customer operates a 20,000-person contact center.

## Founders and Origin Story

All three founders are former early Stripe employees who lived the pain of scaling customer support at a hypergrowth fintech company.

**Ryan Wang (CEO)** was approximately employee #80 at Stripe, where he worked on machine learning for fraud detection and support automation. He studied economics and statistics at the University of Chicago, originally intending to pursue academia. His undergraduate advisor was Steven Levitt (co-author of *Freakonomics*), who instead encouraged him to go into industry. Before Stripe, Wang worked at a boutique consulting firm led by Levitt and Daniel Kahneman.

**John Wang (CTO)** studied Computer Science at MIT and was roughly employee #100 at Stripe. Before Stripe, he worked at Palantir Technologies and 37signals (now Basecamp), and co-founded a startup called Zinc. He is a notable open-source contributor, having contributed to Ruby on Rails (particularly ActiveRecord) and participated in Google Summer of Code.

**Brian Sze (Co-Founder)** holds a B.A. in Economics from Stanford. He joined Stripe in 2012 as Head of Business Operations and led the growth team as the company scaled from ~30 to 500+ employees. Before Stripe, he worked on the analytics team for Obama for America (the 2012 presidential campaign). Sze served as Assembled's CEO from 2018 to 2021, when Ryan Wang took over the CEO role. [Note: His current title and day-to-day involvement are uncertain from public sources.]

The founding insight came directly from their Stripe experience: as Stripe scaled, its support team built internal tools for forecasting, scheduling, and performance management. The founders saw that every growing company faced the same problem with no adequate modern solution.

## Funding History

| Round     | Date       | Amount   | Lead Investor      | Notable Participants                     |
|-----------|------------|----------|--------------------|------------------------------------------|
| Seed      | Mar 2020   | $3.1M    | Stripe             | —                                        |
| Series A  | Mar 2021   | $16.6M   | Emergence Capital   | Stripe, Basis Set Ventures, Felicis Ventures |
| Series B  | May 2022   | $51M     | NEA                | Emergence Capital, Basis Set Ventures     |
| **Total** |            | **$70.7M** |                  |                                          |

The Series B represented a greater than 5x valuation increase over the Series A, per the company's own announcement. No Series C has been publicly announced as of March 2026. [Note: The absence of a new round in nearly four years is notable; the company may be profitable or close to it, or may have raised quietly.]

## Business Model

Assembled is a B2B SaaS platform. Specific pricing is not publicly disclosed, but the model appears to be **per-agent/per-seat** pricing typical of WFM software, potentially evolving toward hybrid consumption-based pricing as AI resolution volumes grow. The platform targets mid-market and enterprise customers across e-commerce, fintech, healthcare, and SaaS verticals.

Revenue has been estimated at $100M-$250M by some third-party trackers, though this range should be treated with **low confidence** — it may reflect inflated estimates common on business intelligence platforms. What is more reliably reported is 300+ customers and strong net revenue retention driven by expanding use cases within accounts.

## Product Architecture

Assembled's platform has evolved into three pillars:

1. **Workforce Management (WFM):** Demand forecasting (using historical tickets, even external signals like Reddit activity), automated scheduling, real-time adherence monitoring, and historical reporting. Supports omnichannel (voice, email, chat, social).

2. **Assembled Assist / AI Agents (launched 2024):** Generative AI that autonomously resolves support interactions across channels. Includes an AI Workflow Builder for no-code automation design. Handles routine workflows (password resets, returns, order status) while routing complex cases to humans. Built using Anthropic's Claude and Pinecone's vector database.

3. **BPO Management:** Joint capacity planning, real-time schedule syncing, and invoice validation across multiple outsourced vendor relationships.

## Key Metrics and Results

- Thrasio: automates 50%+ of support tickets via Assembled Assist, yielding ~$2M in cost savings and 50% decrease in full resolution time.
- Honeylove: 54% increase in solves per hour, 20% decrease in escalations, 18% increase in CSAT for AI-powered responses — within 5 months.
- Largest customer: 20,000-person contact center.

## Competitive Landscape

Assembled competes against:
- **Legacy WFM vendors:** NICE (inContact), Verint, Calabrio, Aspect — large incumbents with dated UX and slow innovation cycles.
- **Modern WFM startups:** Tymeshift (acquired by Zendesk), Playvox (acquired by NICE).
- **AI-first CX platforms:** Forethought, Ada, Decagon, Sierra AI, Intercom Fin — these overlap more on the AI resolution side.

Assembled's differentiation is the **unified platform** that manages both human and AI agents together. Most competitors are either WFM-only or AI-only. The ability to forecast how much work AI will handle versus humans, and dynamically adjust staffing, is a compounding advantage as AI adoption grows.

## What Makes Assembled Interesting (Research Perspective)

1. **Platform wedge strategy:** Started with WFM (a well-understood, must-have category) and expanded into AI-powered resolution. This is a classic "land with workflow, expand with intelligence" SaaS playbook executed well.

2. **Stripe DNA:** The founding team's experience scaling Stripe's support operations gives them unusual credibility with enterprise buyers. Stripe itself led the seed round — a strong signal.

3. **Human+AI orchestration thesis:** Rather than betting that AI will fully replace human agents, Assembled's architecture assumes a blended workforce of humans, AI agents, and BPOs — arguably a more realistic near-term model for complex enterprise support.

4. **Capital efficiency:** Raising $70.7M total and reportedly reaching 300+ customers with up to $100M+ revenue (if tracker estimates are directionally correct) would represent exceptional capital efficiency by 2020s standards. The lack of a new funding round since 2022 suggests possible profitability.

5. **Timing advantage in agentic AI:** As enterprises deploy AI agents for customer service at scale in 2025-2026, they need a management layer to orchestrate those agents alongside humans. Assembled is positioning itself as that orchestration layer — a potentially durable strategic position.

6. **Anthropic partnership:** Assembled builds on Claude (Anthropic's model) for its AI capabilities and is featured as an Anthropic customer case study, suggesting a meaningful technical partnership.

## Key Risks and Open Questions

- Revenue figures from third-party trackers are unreliable; actual revenue could be significantly lower than the $100M-$250M range cited.
- No new funding round announced since May 2022 — could indicate strong cash flow, or could indicate difficulty raising at desired terms.
- Brian Sze's current role and involvement are unclear from public sources.
- Employee count estimates vary (75 on some trackers); the company may be running lean or data may be stale.
- Competition from Zendesk (which acquired Tymeshift) and Salesforce (with its own AI agent offerings) is intensifying.

## Sources

- [Assembled raises $3.1M led by Stripe (TechCrunch, Mar 2020)](https://techcrunch.com/2020/03/11/assembled-raises-3-1m-led-by-stripe-to-build-the-operating-system-for-support-teams/)
- [Assembled raises $16.6M Series A (Assembled Blog)](https://www.assembled.com/blog/assembled-raises-16-6m-in-series-a-fundraising)
- [Customer support management platform Assembled lands $51M (TechCrunch, May 2022)](https://techcrunch.com/2022/05/26/customer-support-management-platform-assembled-lands-51m/)
- [Assembled Raises $51M Series B press release (PRNewswire)](https://www.prnewswire.com/news-releases/assembled-raises-51-million-led-by-nea-to-accelerate-workforce-management-platform-301555838.html)
- [Assembled: Empowering CX Teams (NEA Blog)](https://www.nea.com/blog/assembled-empowering-cx-teams-by-helping-people-serve-people)
- [From Engineer to CEO: Ryan Wang (Fund/Build/Scale Podcast)](https://fundbuildscale.podbean.com/e/from-engineer-to-ceo-ryan-wang-on-building-assembled-and-finding-product-market-fit/)
- [Ryan Wang at Shoptalk Fall 2025](https://fall.shoptalk.com/speakers/ryan-wang)
- [John Wang (Crunchbase)](https://www.crunchbase.com/person/john-wang-6ccb)
- [Brian Sze — The Rise of Strategic Support Teams (Assembled Blog)](https://www.assembled.com/blog/the-rise-of-strategic-customer-support-teams-an-interview-with-assembled-co-founder-brian-sze)
- [The Stripe Mafia (getPIN.xyz)](https://www.getpin.xyz/post/the-stripe-mafia)
- [Assembled 2024 Year in Review](https://www.assembled.com/blog/assembled-2024-year-in-review)
- [Assembled transforms support operations with Claude (Anthropic)](https://claude.com/customers/assembled)
- [Assembled delivers better AI support with Pinecone](https://www.pinecone.io/customers/assembled/)
- [Assembled About Page](https://www.assembled.com/about)
- [Assembled Crunchbase Profile](https://www.crunchbase.com/organization/assembled)
- [Assembled on Tracxn](https://tracxn.com/d/companies/assembled/__fqt0O6Yrs3NkTisKr7Rtt_k0BiHhTKPt_hb4MPe_Jk8)
