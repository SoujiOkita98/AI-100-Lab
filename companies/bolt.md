---
name: Bolt.new (StackBlitz)
legal_entity: StackBlitz Inc.
website: https://bolt.new
parent_product: https://stackblitz.com
founded: 2017
headquarters: San Francisco, CA
founders:
- name: Eric Simons
  role: CEO & Co-Founder
  origin: American
- name: Albert Pai
  role: CTO & Co-Founder
  origin: Chinese-American
stage: Series B
total_funding_raised: ~$135M
latest_valuation: ~$700M (January 2025)
estimated_arr: ~$40M (March 2025)
team_size: ~35 (as of early 2025)
sector: AI-Powered Development Tools / Vibe Coding
tags:
- ai-coding
- browser-ide
- webassembly
- no-code
- developer-tools
- vibe-coding
last_updated: 2026-03-20
confidence: high on funding and founder data; moderate on 2026 revenue and team size
funding_rounds:
- stage: Seed
  date: 2022-04
  amount_m: 7.9
  lead_investors:
  - Greylock
  - GV
  source: https://blog.stackblitz.com/posts/seed-funding/
- stage: Series A
  date: 2024-11
  amount_m: 22
  lead_investors:
  - Emergence Capital
  - GV
  source: https://www.linkedin.com/posts/boltdotnew_
- stage: Series B
  date: 2025-01
  amount_m: 105.5
  valuation_m: 700
  lead_investors:
  - Emergence Capital
  - GV
  source: https://www.bloomberg.com/news/articles/2025-01-21/
---

# Bolt.new / StackBlitz

## One-Liner

AI-powered full-stack application builder that runs entirely in the browser, turning natural-language prompts into deployable web apps in minutes.

## Company Overview

StackBlitz is the company behind **Bolt.new**, the breakout AI coding product that became one of the fastest-growing software products in history upon its October 2024 launch. Bolt lets users describe an application in plain English and generates a fully functional, editable full-stack web app inside a browser-based IDE -- no local setup, no terminal, no deployment friction.

The underlying technology is **WebContainers**, a WebAssembly-based micro-operating system that boots a Node.js runtime inside a browser tab. This gives Bolt a significant moat: unlike competitors that run code on remote servers, Bolt executes everything client-side in the browser's security sandbox, resulting in faster feedback loops, lower infrastructure costs, and offline capability.

## Founders & Team

### Eric Simons -- CEO & Co-Founder

- Born in Naperville, Illinois. Started coding at age 13.
- Famously lived undetected in AOL's headquarters for nearly two months at age 19 -- sleeping in the office, using the company gym, and surviving on free snacks while coding on his first startup.
- Co-founded **Thinkster** (a code education platform) in 2013 with Albert Pai. Thinkster was acquired by a private equity firm in December 2018.
- Co-founded StackBlitz in 2017 after seeing firsthand (via Thinkster) how much beginner developers struggled with setting up local development environments.
- Spent roughly 7 years building StackBlitz and WebContainers before the Bolt.new breakout.

### Albert Pai -- CTO & Co-Founder

- Childhood friend of Eric Simons from the Chicago area; they began coding together as teenagers.
- Also co-founded Thinkster and served as its CTO before co-founding StackBlitz.
- Architect of the WebContainers technology that powers both StackBlitz and Bolt.

### Team

As of early 2025, the team was reported at approximately 35 people -- remarkably lean for a product generating $40M+ ARR. The company has intentionally stayed small, emphasizing engineering talent over headcount. (*Note: 2026 team size is uncertain; the company has likely grown since the Series B.*)

## Funding History

| Round    | Date           | Amount     | Lead Investor(s)                | Valuation         |
|----------|----------------|------------|---------------------------------|-------------------|
| Seed     | April 2022     | $7.9M      | —                               | Undisclosed       |
| Series A | November 2024  | ~$22M      | —                               | Undisclosed       |
| Series B | January 2025   | $105.5M    | Emergence Capital, GV (Google Ventures) | ~$700M post-money |

**Other investors:** Madrona Venture Group, Conviction, Mantis (The Chainsmokers' fund).

Total raised as of early 2025: approximately **$135 million**.

*No publicly disclosed funding rounds in 2026 as of this writing. A new round at a significantly higher valuation would not be surprising given the growth trajectory, but this is speculation.*

## Business Model & Pricing

Bolt.new uses a **freemium, token-based subscription model**:

| Plan      | Price/Month | Tokens/Month | Notes                          |
|-----------|-------------|--------------|--------------------------------|
| Free      | $0          | ~1M tokens   | Enough for small projects      |
| Pro       | $20         | 10M tokens   | Unused tokens roll over        |
| Pro 50    | $50         | 26M tokens   | Unused tokens roll over        |
| Pro 100   | $100        | 55M tokens   | Unused tokens roll over        |
| Pro 200   | $200        | 120M tokens  | Unused tokens roll over        |

Tokens are consumed by AI code-generation calls. The model targets two segments:
1. **Professional developers** seeking rapid prototyping and productivity gains.
2. **Non-technical users** ("the next billion developers") who want to build apps without coding expertise.

StackBlitz also maintains its original browser IDE product (stackblitz.com) with separate team/enterprise pricing, and licenses the WebContainers API to third parties.

## Growth Trajectory

Bolt.new is one of the fastest-growing software products ever measured:

- **October 2024:** Public launch.
- **30 days post-launch:** ~$4M ARR -- matching StackBlitz's entire previous annual revenue in one month.
- **60 days post-launch:** ~$20M ARR -- second-fastest to this milestone behind ChatGPT.
- **March 2025:** ~$40M ARR, ~5 million registered users, ~1 million daily active users.
- **2025 target (reported):** $100M ARR.
- Over 1 million websites deployed in partnership with Netlify.

(*2026 revenue figures are not publicly available as of this writing. Given the trajectory and competitive dynamics, the company likely continued strong growth, but exact numbers are unconfirmed.*)

## Technology & Moat

### WebContainers (Core IP)

StackBlitz spent roughly **three years** (2018-2021) building WebContainers before ever launching Bolt. This technology:

- Runs a full **Node.js runtime in the browser** via WebAssembly.
- Includes a virtualized filesystem, networking stack (mapped to Service Workers), and package manager.
- Executes npm, pnpm, and yarn natively in-browser -- up to 10x faster than local installs.
- Runs entirely in the **browser security sandbox** -- no remote server execution needed.
- Works **offline** once loaded.

This is a genuine technical moat. Competitors like Lovable and Replit rely on server-side execution, which introduces latency, infrastructure costs, and security surface area. WebContainers invert this model.

### AI Integration

Bolt uses **Anthropic's Claude** as its default model for code generation. The combination of Claude's code quality with in-browser execution creates a tight feedback loop: generate code, run it, see the result, iterate -- all without leaving the browser.

### Bolt V2 / Bolt Cloud

In 2025, Bolt launched **Bolt Cloud**, adding built-in databases, authentication, file storage, edge functions, analytics, and hosting. This addressed the biggest user complaint with V1: the "deployment gap" where users could build an app but then struggled to get it live.

## Competitive Landscape

Bolt.new operates in the rapidly growing "vibe coding" / AI app builder market. Key competitors:

| Competitor     | Key Differentiator                              | Reported ARR (2025) |
|----------------|------------------------------------------------|---------------------|
| **Lovable**    | Cleanest React code output                      | $100M (in 8 months) |
| **Replit**     | Full IDE, mobile apps, Agent 3 autonomy         | ~$100M              |
| **v0 (Vercel)**| UI component generation, Next.js integration    | Undisclosed         |
| **Cursor**     | IDE-native AI pair programming                  | Undisclosed         |

In benchmark comparisons, Bolt.new is consistently the **fastest to a working prototype** (~28 minutes vs. 35-65 for competitors), though reviewers note competitors may produce more production-ready code.

## What Makes Them Interesting

1. **WebContainers as a platform moat.** Three years of deep WebAssembly engineering created infrastructure that competitors cannot easily replicate. Running a full Node.js environment in-browser is a genuine technical achievement, not just an LLM wrapper.

2. **Near-death to record growth.** StackBlitz was reportedly close to shutting down before the Bolt launch. Eric Simons has described having a 90-day runway ultimatum. The pivot to an AI-first product on top of existing WebContainers infrastructure was a masterclass in leveraging latent technical assets.

3. **Capital efficiency.** $40M ARR with ~35 people is extraordinary. Because WebContainers run client-side, Bolt's infrastructure costs per user are structurally lower than server-side competitors.

4. **Democratization thesis.** Bolt is one of the clearest examples of AI enabling a new class of software creators. The "next billion developers" framing -- people who can describe what they want but cannot write code -- is a massive TAM expansion if the product quality holds.

5. **Founder story.** Eric Simons' arc from sleeping in AOL's headquarters as a 19-year-old to building one of the fastest-growing products in software history is compelling and authentic. Seven years of patient infrastructure investment before the AI moment arrived is a lesson in timing and persistence.

## Key Risks & Open Questions

- **Margin pressure:** Token-based pricing means Bolt's gross margins depend on LLM API costs (Anthropic/Claude). As usage scales, negotiating favorable model pricing is critical.
- **Competition intensifying:** Lovable and Replit are growing at comparable rates. The vibe coding market may commoditize quickly as frontier models improve.
- **Production quality gap:** Bolt excels at prototyping and demos but reviews suggest limitations for production-grade applications. Bolt Cloud/V2 addresses this but maturity is uncertain.
- **Retention:** Freemium token models can see high churn. Long-term retention data is not yet public.

## Sources

- [Sacra -- Bolt.new Revenue, Funding & News](https://sacra.com/c/bolt-new/)
- [Bloomberg -- AI Text-to-Code Startup StackBlitz in Talks for $700M Valuation](https://www.bloomberg.com/news/articles/2025-01-21/ai-speech-to-code-startup-stackblitz-is-in-talks-for-a-700-million-valuation)
- [Contrary Research -- Bolt Business Breakdown & Founding Story](https://research.contrary.com/company/bolt)
- [Lenny's Newsletter -- Inside Bolt: From near-death to ~$40M ARR](https://www.lennysnewsletter.com/p/inside-bolt-eric-simons)
- [Growth Unhinged -- How Bolt.new hit $40M ARR in 5 months](https://www.growthunhinged.com/p/boltnew-growth-journey)
- [GetLatka -- How Bolt.new hit $40M revenue with a 35 person team](https://getlatka.com/companies/bolt.new)
- [Shipper -- Bolt.new User and Revenue Statistics (2026)](https://shipper.now/bolt-new-stats/)
- [StackBlitz Blog -- Introducing WebContainers](https://blog.stackblitz.com/posts/introducing-webcontainers/)
- [Western Business -- StackBlitz Founder's Journey](https://westernbusiness.co.uk/stackblitz-founders/)
- [ICT Mirror -- 8 Top Facts About StackBlitz CEO Eric Simons](https://ictmirror.com/featured/stackblitz-ceo-eric-simons/)
- [The Split -- Zero to $20M ARR in Two Months](https://www.thespl.it/p/zero-to-20m-arr-in-two-months-inside)
- [Agent Talk -- We had 90 days to ship or shut down](https://agenttalk.substack.com/p/we-had-90-days-to-ship-or-shut-down)
- [Bolt.new Pricing Page](https://bolt.new/pricing)
- [Taskade -- Bolt Review 2026](https://www.taskade.com/blog/bolt-review)
- [Startup Spells -- Bolt.new: The 2nd Fastest-Growing Product in History](https://startupspells.com/p/bolt-new-second-fastest-growing-product-history-behind-chatgpt)
