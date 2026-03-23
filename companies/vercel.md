---
name: Vercel
legal_name: Vercel Inc.
former_name: ZEIT
founded: 2015
headquarters: San Francisco, CA
ceo: Guillermo Rauch
cofounders:
- Guillermo Rauch
- Tony Kovanen
- Naoyuki Kanezawa
sector: Developer Tools / Frontend Cloud / AI Code Generation
stage: Late-stage (Series F)
latest_valuation: $9.3B (September 2025)
total_funding: ~$863M across 6 rounds
latest_round: Series F ($300M, September 2025)
annual_recurring_revenue: $200M (May 2025)
employees: ~875 (early 2026)
website: https://vercel.com
key_products:
- Vercel Platform (frontend cloud / deployment)
- Next.js (open-source React framework)
- v0 (AI code generation, v0.app)
- Vercel AI SDK (open-source TypeScript toolkit)
- Vercel AI Gateway
profile_updated: 2026-03-20
one_liner: Vercel is a frontend cloud platform that enables developers to build, deploy, and scale web applications with minimal
  configuration
website_verified: true
crunchbase: https://www.crunchbase.com/organization/vercel
crunchbase_verified: false
---

# Vercel

## Company Overview

Vercel is a frontend cloud platform that enables developers to build, deploy, and scale web applications with minimal configuration. The company is best known for creating **Next.js**, the dominant React framework (200M+ weekly npm downloads), and more recently for **v0**, an AI-powered code generation tool that has attracted over 6 million developers. Vercel's thesis is that the frontend is the new full-stack, and AI will make every team member a builder.

Originally founded in 2015 as **ZEIT**, the company rebranded to Vercel in April 2020 to improve enterprise and investor recognition. Its first product was a CLI tool called "now" that let developers deploy an app to a global CDN with a single command.

## Founders and Leadership

### Guillermo Rauch -- Founder & CEO

Guillermo Rauch was born in December 1990 in Lanus, an industrial suburb on the outskirts of Buenos Aires, Argentina. He is entirely self-taught: he began programming at age 10, spent his early teens advocating for Linux, and learned English by reading software manuals. By 16, he had become a core contributor to MooTools (a popular JavaScript framework at the time), and at 18 he landed his first full-time frontend engineering job and relocated to San Francisco.

Before Vercel, Rauch created several widely-adopted open-source projects including **Socket.IO** (real-time WebSocket library) and **Mongoose** (MongoDB ODM for Node.js). He also founded **Cloudup**, a file-sharing startup acquired by Automattic (the company behind WordPress). These projects gave him deep credibility in the JavaScript ecosystem and a thesis about developer experience (DX) as a competitive moat.

Rauch was named an EY World Entrepreneur of the Year 2025 finalist representing Argentina.

### Co-founders

- **Tony Kovanen** -- co-founded ZEIT with Rauch in 2015. [Limited public information on current role.]
- **Naoyuki Kanezawa** -- co-founded ZEIT; notably also a co-creator of Socket.IO. [Limited public information on current role.]

### Key Executives (as of 2025-2026)

| Role | Name | Background |
|------|------|-----------|
| CEO | Guillermo Rauch | See above |
| CTO | Malte Ubl | Former Google engineer; led the AMP project |
| COO | Jeanne DeWitt Grosser | Former Chief Business Officer at Stripe |
| CPO | Tom Occhino | Former engineering lead at Meta (React team) |
| CFO | Marten Abrahamsen | [Details unconfirmed] |
| CTO of Security | Talha Tariq | Former HashiCorp and IBM |

The leadership team is notable for its concentration of talent from the React/frontend ecosystem (Tom Occhino helped create React at Facebook) and top-tier SaaS companies (Stripe, Google, HashiCorp).

## Team Origins and Culture

Vercel's founding team has strong roots in Latin America (Rauch from Argentina, Kanezawa from Japan) and the open-source JavaScript community. The company grew from 3 employees in 2015 to approximately 875 by early 2026. Headcount grew ~34% year-over-year in 2025. The team includes roughly 66 engineers focused on product development and 37 quota-carrying sales reps, reflecting its transition from a developer-first tool to an enterprise platform. Vercel operates as a distributed/remote-friendly company headquartered in San Francisco.

## Funding History

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|----------------|
| Series A | Apr 2020 | $21M | ~$100M (est.) | Accel |
| Series B | Dec 2020 | $40M | Undisclosed | GV (Google Ventures) |
| Series C | Jun 2021 | $102M | ~$1.5B (est.) | Bedrock Capital, others |
| Series D | Nov 2021 | $150M | $2.5B | GIC, others |
| Series E | May 2024 | $250M | $3.25B | Accel |
| Series F | Sep 2025 | $300M | $9.3B | Accel, GIC |

**Total raised: ~$863M**

The Series F was co-led by Accel and GIC (Singapore sovereign wealth fund), with participation from BlackRock, Khosla Ventures, StepStone, Schroders, Adams Street Partners, General Catalyst, GV, Notable Capital, Salesforce Ventures, and Tiger Global. Vercel also opened a $300M tender offer for early backers and employees alongside the Series F, signaling confidence and providing liquidity.

The nearly 3x valuation jump from Series E ($3.25B) to Series F ($9.3B) in about 16 months was driven by AI product traction and revenue growth.

## Products

### Vercel Platform (Frontend Cloud)

The core product: a deployment and hosting platform optimized for frontend frameworks (especially Next.js). Key features include instant global deployments, preview deployments for every pull request, edge functions, serverless functions, and built-in analytics. It functions as an opinionated, developer-friendly layer on top of cloud infrastructure.

### Next.js (Open Source)

The most popular React framework, created and maintained by Vercel. Used by companies including Walmart, TikTok, Netflix, OpenAI, and many others. With 200M+ weekly downloads, Next.js is the primary funnel through which developers discover Vercel's paid platform -- a classic open-source-to-commercial flywheel.

### v0 (AI Code Generation)

Vercel's AI-powered application builder, accessible at **v0.app** (rebranded from v0.dev in January 2026). v0 acts as an AI frontend engineer: users describe a UI or application in natural language, and v0 generates production-ready React/Next.js code using Tailwind CSS and shadcn/ui components.

**Key capabilities (as of early 2026):**
- Full-stack application building (evolved beyond UI components)
- Sandbox-based runtime that can import any GitHub repo
- Git panel for creating branches and PRs directly from chat
- Database integrations (Snowflake, AWS, etc.)
- Token-based billing (switched from fixed credits in February 2026)
- Deploy-on-merge workflow with real preview deployments
- Over 6 million developers on the platform (as of March 2026)

**2026 roadmap** centers on agentic workflows -- building end-to-end AI agent pipelines within v0 that deploy on "self-driving infrastructure." Vercel Agent (automated code reviews) is already in public beta.

### Vercel AI SDK (Open Source)

A provider-agnostic TypeScript toolkit for building AI-powered applications. Over 20 million monthly downloads. Supports 50+ AI providers (OpenAI, Anthropic, Google, etc.) and works across React, Next.js, Svelte, Vue, and Angular. Released under Apache 2.0 license. Recent features include ToolLoopAgent, human-in-the-loop approval, and DevTools for debugging.

### Vercel AI Gateway

A unified API layer that gives developers out-of-the-box access to all major AI model providers through the AI SDK.

## Business Model

Vercel operates a **usage-based B2B SaaS model** with multiple revenue streams:

1. **Platform hosting/infrastructure**: Usage-based pricing for compute, bandwidth, and storage. Free tier for hobbyists, Pro tier at $20/month/seat, and custom Enterprise plans.
2. **v0 AI product**: Separate $20/month premium tier with token-based billing (as of Feb 2026). Creates a dual flywheel -- v0 usage fees plus increased downstream infrastructure consumption as more apps get built and deployed on Vercel.
3. **Enterprise contracts**: Custom pricing for large organizations; Vercel claims 264% ROI for enterprise customers.

The strategic genius of the model is that **every product feeds the others**: Next.js (free, open source) drives developer adoption, v0 (AI) lowers the barrier to building apps, and both funnel users into paid Vercel hosting. AI usage directly increases infrastructure consumption.

## Customers

Vercel's customer base spans individual developers to Fortune 500 enterprises:

- **Tech**: OpenAI, Perplexity, ChatGPT (OpenAI's web interface runs on Next.js/Vercel)
- **Retail**: Walmart, Under Armour
- **Media/Entertainment**: Netflix, TikTok (web)
- **Enterprise**: Washington Post, Notion, Loom

The company has seen particular growth in AI-native startups building on Vercel's infrastructure, creating a network effect within the AI ecosystem.

## What Makes Vercel Interesting

1. **The open-source flywheel is unmatched in frontend.** Next.js is the de facto React framework. This is not a replaceable advantage -- it took nearly a decade to build and is deeply embedded in the ecosystem. Every Next.js user is a potential Vercel customer.

2. **v0 is a wedge into "AI for everyone" software creation.** Unlike pure coding assistants (Copilot, Cursor), v0 targets non-engineers and designers who can describe what they want in plain language and get deployable code. This expands Vercel's TAM from ~30M developers to potentially hundreds of millions of knowledge workers.

3. **The Rauch founder story is compelling.** A self-taught Argentine teenager who became one of the most influential JavaScript developers in the world, then built a $9.3B company. His deep technical credibility (Socket.IO, Mongoose, Next.js) gives Vercel authentic standing in the developer community that is difficult for competitors to replicate.

4. **AI as an infrastructure consumption multiplier.** v0 is not just a product -- it is a demand generator for Vercel's core hosting business. More AI-generated apps means more deployments, more bandwidth, more compute. The business model compounds.

5. **Capital efficiency and growth rate.** $200M ARR with ~875 employees (~$229K ARR/employee) and 82% YoY revenue growth as of 2025. The nearly 3x valuation jump to $9.3B in 16 months reflects investor conviction in the AI-driven growth trajectory.

6. **Ecosystem lock-in without vendor lock-in.** Next.js is open source and runs anywhere, but Vercel's platform is optimized for it in ways that create strong switching costs (preview deployments, edge functions, analytics, v0 integration). This is a subtle but powerful moat.

7. **Positioning at the AI application layer.** While others fight over foundation models, Vercel is building the deployment and creation layer for AI-powered applications. The AI SDK (20M+ monthly downloads) positions them as the default way TypeScript developers integrate AI into their apps.

## Risks and Open Questions

- **IPO timing**: With $9.3B valuation and $300M tender offer, an IPO seems plausible in 2026-2027, but no confirmed plans.
- **Next.js competition**: React Server Components and alternative frameworks (Remix, Astro, SvelteKit) could erode Next.js dominance, though current momentum is strong.
- **v0 competitive landscape**: Competing with Replit, Bolt, Lovable, Cursor, and others in the AI code generation space. Differentiation through deployment integration is key.
- **Profitability**: Not publicly confirmed whether Vercel is profitable. At $200M ARR with 875 employees, unit economics appear reasonable but AI compute costs for v0 could pressure margins.
- **Concentration risk**: Heavy dependence on the React/Next.js ecosystem. A major shift away from React would be existential (though unlikely near-term).

## Sources

- [Vercel Series F Announcement](https://vercel.com/blog/series-f)
- [Yahoo Finance: Vercel Closes Series F at $9.3B](https://finance.yahoo.com/news/vercel-closes-series-f-9-150000846.html)
- [GIC Newsroom: Vercel Series F](https://www.gic.com.sg/newsroom/all/vercel-closes-series-f-at-9-3b-valuation-to-scale-the-ai-cloud/)
- [SaaStr: How Vercel Hit $9.3B](https://www.saastr.com/how-vercel-hit-9-3b-and-replit-hit-3b-after-a-decade-the-long-paths-to-ai-overnight-success/)
- [Vercel & V0 Statistics (2026)](https://shipper.now/vercel-v0-stats/)
- [Latka: Vercel Revenue and Team](https://getlatka.com/companies/vercel)
- [Contrary Research: Vercel Business Breakdown](https://research.contrary.com/company/vercel)
- [Sacra: Vercel Revenue](https://sacra.com/c/vercel/)
- [Guillermo Rauch Bio](https://rauchg.com/about)
- [History of Vercel: Guillermo Rauch (Medium)](https://medium.com/history-of-vercel/history-of-vercel-1990-2009-guillermo-rauch-childhood-and-first-steps-in-programming-1dbf038ddf9a)
- [We Are Founders: Guillermo Rauch](https://www.wearefounders.uk/guillermo-rauch-founder-vercel/)
- [GV: Vercel Founder Guillermo Rauch](https://www.gv.com/news/vercel-founder-guillermo-rauch)
- [EY WEOY: Guillermo Rauch (Argentina)](https://www.ey.com/en_nl/weoy/class-of-2025/argentina)
- [Vercel Blog: Introducing the New v0](https://vercel.com/blog/introducing-the-new-v0)
- [SaaStr: v0 AI App of the Week](https://www.saastr.com/saastr-ai-app-of-the-week-v0-by-vercel-the-vibe-coding-tool-that-4-million-people-use-to-ship-real-software-not-just-demos/)
- [Taskade: V0 Review 2026](https://www.taskade.com/blog/v0-review)
- [Vercel AI SDK (GitHub)](https://github.com/vercel/ai)
- [Vercel Blog: AI SDK 6](https://vercel.com/blog/ai-sdk-6)
- [Wikipedia: Vercel](https://en.wikipedia.org/wiki/Vercel)
- [Vercel About](https://vercel.com/about)
- [The Org: Vercel Leadership](https://theorg.com/org/vercel/teams/leadership-team)
- [Crunchbase: Vercel](https://www.crunchbase.com/organization/vercel)
- [Vercel Blog: ZEIT is now Vercel](https://vercel.com/blog/zeit-is-now-vercel)
- [TechCrunch: Vercel Series D](https://techcrunch.com/2021/11/23/vercel-raises-150m-series-d-as-it-looks-to-build-an-end-to-end-front-end-development-platform/)
- [Crunchbase: Vercel Series E](https://news.crunchbase.com/cloud/vercels-cloud-web-applications-funding-valuation-accel/)
- [Bloomberg: Vercel $9.3B Valuation](https://www.bloomberg.com/news/articles/2025-09-30/vercel-notches-9-3-billion-valuation-in-latest-ai-funding-round)
