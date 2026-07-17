# Competitive Research on Steroids: A Category Compendium

**The premise:** The intelligence community solved this problem decades ago. They don't collect "data." They run *collection disciplines*, each with its own sources, tradecraft, and blind spots. Then they fuse them. Product teams should steal the whole playbook.

**How to use this:** Each discipline below tells you (1) what to collect, (2) where to collect it, (3) what signal → inference chains to run, and (4) which Product Manager artifact it feeds (TAM/SAM/SOM, ICPs, Personas, Battle Cards, Roadmap Bets, Win/Loss, Positioning, Messaging). For which of this directory's runnable prompts cover which discipline, see the coverage table in [the market-intelligence README](../README.md).

---

## Instantiate for Any Engagement

Fill these six variables once, and every discipline below becomes company-specific. Leave them blank and this stays a teaching artifact.

~~~
[TARGET]      = The competitor, partner, or acquirer you're researching
[MARKET]      = The category and its NAICS/SIC/NACE codes (or nearest equivalent)
[GEOGRAPHY]   = Regions in scope, at COUNTRY level, not continent level
                (drives which registries, statistics bureaus, and filings apply,
                and which Regional Source Overlay to load)
[BUYER]       = Who signs the check (drives review sites, job titles, conferences)
[CAPABILITY]  = The strategic move you suspect (platform play, market entry,
                pricing shift, compliance land-grab, etc.)
[DECISION]    = What this research will change (roadmap bet, positioning,
                pricing, market entry, deal defense, ICP refresh)
~~~

If [DECISION] is blank, stop. Research without a decision is a hobby.

Every example in this document is illustrative, not prescriptive. Swap in your own [TARGET] and [CAPABILITY]. For engagements outside the US, load the matching **Regional Source Overlay** (see the closing section) after completing this block.

---

## The Eight Disciplines

| Discipline | Intel Community Name | Plain English | Primary Product Manager Artifact |
|---|---|---|---|
| 1. OSINT | Open Source Intelligence | Press, social, periodicals, analysts | Battle Cards, Positioning |
| 2. FININT | Financial Intelligence | Filings, earnings calls, procurement | Battle Cards, SOM capture rates |
| 3. GEOINT/DEMOINT | Geospatial & Demographic Intelligence | Census, labor, trade, and economic statistics | TAM/SAM/SOM, ICPs, Personas, Messaging |
| 4. TECHINT | Technical Intelligence | Patents, technographics, changelogs | Roadmap Bets |
| 5. HUMINT | Human Intelligence | Talent moves, employee chatter, win/loss | Roadmap Bets, Battle Cards |
| 6. SIGINT | Signals Intelligence | Web diffs, pricing changes, job posts | Battle Cards, Pricing Strategy |
| 7. MASINT | Measurement & Signature | Supply chain, ops indicators | Threat Assessment |
| 8. All-Source Fusion | n/a | Cross-validation and confidence stacking | Everything above |

---

## 1. OSINT: The Journalist's Desk

*What a good beat reporter knows before the press release drops.*

### Sources

| Source Type | Free | Paid |
|---|---|---|
| [TARGET] press & newsroom | Company newsroom pages, Google Alerts, PR Newswire feeds | Meltwater, Cision |
| Industry periodicals | Trade publications, association newsletters, vertical Substacks for [MARKET] | Analyst subscriptions |
| Analyst coverage | Gartner/Forrester press summaries, free webinar replays | Gartner, Forrester, IDC full reports |
| Social & community | LinkedIn exec posts, Reddit, Hacker News, X | Brandwatch, Sprout listening |
| Review sites | Whichever your [BUYER] reads: G2, Capterra, TrustRadius, app stores, Trustpilot | G2 Buyer Intent data |
| Conference footprint | Session titles, sponsor tiers, booth size, speaker rosters at [MARKET] events | n/a |
| Prediction markets | Polymarket, Kalshi, Metaculus, Manifold (crowd-priced odds on regulation, approvals, elections, tech milestones relevant to [MARKET]) | n/a |

### Signal → Inference Chains

- [TARGET] exec suddenly posting about a new problem space → positioning pivot incoming (execs test messaging on social 3-6 months before launch)
- Sponsor tier jump at a [MARKET] conference → market entry or doubling down
- Review complaints clustering on one feature → their roadmap pressure point = your battle card ammo
- Analyst briefing requests (visible via analyst posts) → category creation attempt
- Webinar topics shifting → what they're teaching the market is what they're about to sell
- Sudden silence on a product line → sunset in progress
- Prediction-market odds moving on a regulation, approval, or milestone that gates [MARKET] → crowd-priced expectations for scenario planning and roadmap timing; treat as a leading indicator of consensus, not ground truth, and check liquidity before you trust the number

### Feeds
**Battle Cards** (objection handling from review mining), **Positioning** (their words vs. customer words gap), **Win/Loss context**.

---

## 2. FININT: The Forensic Accountant

*Follow the money. Companies lie in press releases. They lie less in filings, because lying there is a felony.*

### Sources

| Source Type | Free | Paid |
|---|---|---|
| Public filings | SEC EDGAR (US), Companies House (UK), BRIS and European e-Justice company search (EU), national securities regulators and exchanges for [GEOGRAPHY] | AlphaSense, Sentieo |
| Earnings calls | Company IR pages, Seeking Alpha transcripts | AlphaSense (search across calls) |
| Private company signals | Crunchbase free tier, state/national incorporation records, insolvency registers, beneficial-ownership registers where legally accessible | PitchBook, CB Insights |
| Government spend & procurement | USAspending.gov, SAM.gov (US), TED and national procurement portals (EU), Etimad, Monaqasat, EONEPS and country platforms (MENA), development-bank procurement (World Bank, IsDB, EBRD, AfDB, UNGM) | GovWin |
| Competition & state-aid cases | European Commission merger, antitrust, cartel, and state-aid databases; national competition authorities | n/a |
| State & sovereign capital | Sovereign wealth fund reports, state-owned enterprise annual reports, public-private partnership pipelines | n/a |

### Signal → Inference Chains

- **Risk Factors section changes year-over-year in an annual filing** → what genuinely scares them (they must disclose it)
- Segment reporting restructure → strategic reprioritization; follow which segment got promoted
- Earnings call Q&A dodges (analysts ask, execs deflect) → soft spot, probe it in your positioning
- New entity registrations, subsidiaries, or branches in [GEOGRAPHY] → market entry before any announcement
- Deferred revenue trends → their actual sales momentum vs. their stated momentum
- Merger filings → market definitions and named competitors, straight from [TARGET]'s own lawyers
- Contract modifications expanding an incumbent's procurement scope → locked-in account, plan around it
- Sovereign fund or state-aid money backing [TARGET] → their runway math just changed; discount-pressure plays won't work
- Prior Information Notices and expressions of interest → tenders telegraphed 3-24 months out

### Feeds
**Battle Cards** (financial stress = discount pressure = "they'll be desperate at quarter-end" plays), **SOM capture rates** (their revenue ÷ claimed customer count = deal size reality check, feeding the GEOINT/DEMOINT sizing recipe), **account targeting** (procurement award patterns).

---

## 3. GEOINT/DEMOINT: The Cartographer

*The terrain map, not troop movement. Government statistics are free intelligence most Product Managers never open, and they're the backbone of every ICP, Persona, and TAM that survives scrutiny.*

### Sources

| Source Type | Free | Paid |
|---|---|---|
| US market structure | Census Bureau (County Business Patterns, Economic Census, NAICS establishment counts), BEA | IBISWorld, Statista, Grand View Research |
| US labor & buyers | BLS (occupation counts, wages, industry employment), FRED (macro conditions gating budgets) | TalentNeuron (demand-side) |
| EU market structure | Eurostat, PRODCOM manufacturing statistics, national statistical institutes, ECB data | national data resellers |
| EU trade flows | Eurostat COMEXT, Access2Markets, TARIC (tariffs, quotas, rules of origin) | Panjiva, S&P Global |
| MENA regional | GCC-Stat and Marsa Data Portal, Arab Development Portal, ESCWA, Arab Monetary Fund, SESRIC | n/a |
| MENA national | GASTAT (Saudi), FCSC (UAE), CAPMAS (Egypt), HCP (Morocco), INS (Tunisia), ONS (Algeria), and peers | n/a |
| Global cross-check | World Bank Data and Enterprise Surveys, IMF country reports, OECD.Stat, UN Comtrade, ITC Trade Map | n/a |

### Signal → Inference Chains

- Establishment counts by industry code and employee band → the denominator for bottom-up TAM
- Regional industry concentration → where your SOM actually lives, and where field sales should live
- Occupation growth curves for your [BUYER] and end-user roles → is the population you sell to growing or shrinking
- Wage trends in buyer roles → willingness-to-pay ceiling shifts; pricing corridor validation
- Firmographic distributions (size bands, legal forms, sectors) → ICP boundaries drawn from data, not vibes
- Buyer-title prevalence by [GEOGRAPHY] → Persona localization; the "VP of Product" you message in Boston is a "Head of Digital" in Frankfurt and may not exist in Riyadh
- Language, regulatory, and disclosure environment per country → messaging localization and evidence standards (see Regional Source Overlays)
- Trade-flow shifts in product-specific codes → market entry or supply relocation before any announcement

### The TAM/SAM/SOM Recipe (GEOINT/DEMOINT's signature dish)

~~~
TAM: Establishment counts for [MARKET] (Census/NAICS, Eurostat/NACE,
     GCC-Stat, or national equivalent for [GEOGRAPHY])
     × employment/spend benchmarks (BLS, Eurostat, trade associations)
     (validate against two independent analyst reports; if they disagree by 3x, say so)

SAM: TAM filtered by your actual constraints: [GEOGRAPHY], segment, compliance
     requirements, tech prerequisites (see TECHINT technographics),
     local-content and vendor-registration eligibility where applicable
     (regional industry concentration data shows where your SOM actually lives)

SOM: SAM × realistic capture rate derived from [TARGET] public filings via FININT
     (their revenue ÷ their claimed customer count = deal size reality check)
~~~

### Feeds
**TAM/SAM/SOM** (this is the backbone), **ICP definition** (firmographic boundaries), **Personas** (occupation, wage, title-prevalence data), **Messaging localization**, **market entry prioritization**, **pricing corridor validation**.

---

## 4. TECHINT: The Patent Examiner

*R&D leaves fingerprints 12-18 months before products ship.*

### Sources

| Source Type | Free | Paid |
|---|---|---|
| Patents | patents.google.com, USPTO Patent Center, EPO Espacenet, WIPO PatentScope | Clarivate, LexisNexis PatentSight+ |
| Technographics | BuiltWith free lookups, Wappalyzer | HG Insights, BuiltWith Pro, 6sense |
| Product telemetry | Public changelogs, API docs diffs, status pages, GitHub org activity | n/a |
| Standards bodies | Whichever govern [MARKET]: IETF, W3C, ISO committees, CEN/CENELEC/ETSI work programs (EU), industry consortia | n/a |
| Funded research | CORDIS and Horizon Europe project databases (participants, deliverables, pilot sites, collaboration networks), university project repositories | n/a |
| Academic & preprints | arXiv, Google Scholar, Semantic Scholar, SSRN, proceedings of the conferences that matter to [MARKET] (NeurIPS, ICML, IEEE venues, etc.) | Dimensions, Scopus |
| Trademark filings | USPTO TESS, EUIPO, WIPO Global Brand Database | Corsearch |

### Signal → Inference Chains

- Patent **clusters** (5+ filings in one classification in 12 months) → committed bet on [CAPABILITY], not exploration
- Inventor names repeating across filings → the actual product team behind the initiative; track their conference talks and LinkedIn
- Trademark filing for a product-sounding name → launch inside 6-12 months (trademarks are cheap; companies file close to launch)
- Trademark filing following a funded research project's completion → commercialization underway
- [TARGET] repeatedly appearing in funded consortia → their long-range bet, 12-48 months of lead time
- Research pilot sites → likely launch customers, named in public deliverables
- [TARGET] chairing a standards committee → they intend to shape the rules of [MARKET], not just play by them
- [TARGET]-affiliated authors publishing on arXiv or at [MARKET] conferences → R&D direction 6-24 months before patents, longer before product; a paper cluster plus a hiring surge in the same specialty is one of the strongest fusion pairs available
- Author affiliations shifting from university to [TARGET] on successive papers → they hired the lab, not just the idea
- API docs adding endpoints for an unreleased capability → beta program running now
- Public repo activity (new SDKs, scaffolding) → developer platform play
- Your prospects' tech stacks (technographics) → your SAM refinement: who *can* actually buy you

### Feeds
**Roadmap Bets** (where to accelerate vs. concede), **SAM refinement** (technographic filters), **Battle Cards** (feature-gap countdown clocks), **build/buy/partner decisions** (consortium and ecosystem maps).

---

## 5. HUMINT: The Sports Scout

*Organizations announce strategy through job boards long before press releases. People are the tell.*

### Sources

| Source Type | Free | Paid |
|---|---|---|
| Job postings | LinkedIn Jobs, [TARGET] careers pages, Indeed | JobsPikr, TalentNeuron, Revelio Labs |
| Employee sentiment | Glassdoor, Blind, Reddit communities for [MARKET] | n/a |
| Leadership moves | LinkedIn announcements, press | BoardEx, The Org |
| Win/Loss | Your own sales team debriefs, churned-customer interviews | Clozd, DoubleCheck |
| Conference hallway | Your field team's ears at [MARKET] trade shows | n/a |

### Signal → Inference Chains

- Hiring surge in one specialty (30+ postings in a quarter) → building [CAPABILITY], not a feature
- Regional specialist roles appearing for a [GEOGRAPHY] you haven't seen them in → expansion pre-announcement
- Job posts naming specific technologies → confirmed stack choices → integration roadmap intel
- Senior product/tech leader exits within 6 months of a strategy announcement → the strategy is in trouble
- Your own alumni landing at [TARGET] → reverse-engineerable knowledge transfer; assume they know your playbook
- Employee reviews mentioning "pivot," "reorg," "leadership churn" → 2 quarters of internal distraction = your window
- Win/Loss interviews: the only source that tells you *why* deals actually close (everything else is inference)

### Feeds
**Roadmap Bets** (their build signals), **Battle Cards** (org instability plays), **Win/Loss program** (ground truth for everything).

---

## 6. SIGINT: The Wiretap You're Allowed to Have

*Companies broadcast constantly through what they change on the public internet. Most competitors never listen.*

### Sources

| Source Type | Free | Paid |
|---|---|---|
| Website diffs | Wayback Machine, Visualping free tier | Visualping, Klue, Crayon (auto-monitoring) |
| Pricing pages | Manual snapshots + Wayback | Klue, Crayon, Kompyte |
| SEO/SEM moves | Google "site:" queries, free Semrush lookups | Semrush, Ahrefs, SpyFu |
| App store metadata | Version notes, screenshot changes, keyword shifts | Sensor Tower, data.ai |
| DNS/infrastructure | crt.sh (new SSL certs reveal new subdomains), DNS records | n/a |
| Webinar/event cadence | [TARGET] events pages, registration platforms | n/a |

### Signal → Inference Chains

- New subdomain SSL cert (e.g., `[capability].[target].com`) → product launch staging, often weeks ahead
- Pricing page removes a tier → packaging overhaul, usually toward enterprise
- Sudden SEM bidding on *your* brand terms → they consider you the threat now (congratulations)
- Case study page pattern shifts (new vertical or [GEOGRAPHY] appearing) → segment push
- Messaging A/B visible via Wayback diffs → they're unsure of positioning; hit the wound

### Feeds
**Battle Cards** (freshest layer; this is what keeps cards from going stale), **Pricing Strategy**, **Positioning counter-moves**.

---

## 7. MASINT: The Satellite Photo

*Measure the physical and operational exhaust. Abnormal resource allocation never lies.*

### Sources

| Source Type | Free | Paid |
|---|---|---|
| Supply chain | Import/export records via ImportYeti (free tier), Panjiva summaries, Eurostat COMEXT and customs codes (EU), UN Comtrade | S&P Global Supply Chain Intelligence, Panjiva, ImportGenius |
| Facilities & projects | Commercial real estate news, local business journals, permits in [GEOGRAPHY]; industrial-zone and free-zone tenant announcements, environmental permits, utility-connection approvals, EPC contract awards (MENA); satellite imagery | CoStar |
| Ops capacity | Support response time sampling, status page incident frequency | n/a |
| Certifications & safety | Whichever gate [MARKET]: ISO, SOC 2, FedRAMP, CE marks; NANDO notified-body designations and Safety Gate recalls (EU); sector registries | n/a |

### Signal → Inference Chains

- 20%+ volume change in critical inputs → pre-launch or demand collapse (check which via FININT)
- New supplier geographies or country-of-origin shifts → market entry, tariff hedging, or resilience play
- Compliance certification "in process" listings, or [TARGET] selecting a notified body for a new product category → 12-36 month runway into a regulated segment, visible to anyone who checks the registry
- Product recalls or repeated safety-alert patterns → quality strain; Battle Card ammunition with a public citation
- Land allocation, power/water capacity reservations, or engineering-design contracts preceding equipment procurement → facility buildout 6-36 months before any launch announcement
- Support response times stretching + hiring freeze in support roles → cash constraint or overwhelmed by growth (disambiguate via employee sentiment)
- Office consolidations → cost compression, expect pricing aggression to follow

**Note:** Supply chain and facility signals are strongest for hardware and industrial players. The software equivalent is ops capacity plus infrastructure-scale language in job postings.

### Feeds
**Threat Assessment**, **launch prediction and capacity estimates**, **Battle Cards** (capacity-stretch objections: "ask them about their support SLAs lately").

---

## 8. All-Source Fusion: The Situation Room

*One signal is an anecdote. Three correlated signals from independent disciplines is intelligence.*

### The Confidence Stacking Rule

~~~
1 discipline flags it  → Watch item. Log it, do nothing.
2 disciplines agree    → Working hypothesis. Assign someone to probe.
3+ disciplines agree   → Actionable intelligence. Brief leadership, adjust roadmap/plays.
Disciplines conflict   → The most interesting case. Someone is bluffing. Dig.
~~~

One regional corollary from MENA tradecraft that generalizes everywhere: **treat announcements as intent until funding, procurement, land, permits, hiring, or contracts corroborate them.** Ambition is OSINT. Commitment shows up in FININT, MASINT, and HUMINT.

### Fusion Template: Detecting [TARGET]'s [CAPABILITY] Play

| Discipline | Signal (fill in what you found) |
|---|---|
| MASINT | Resource/input anomaly: ____ |
| TECHINT | Patent cluster or repo activity: ____ |
| HUMINT | Hiring pattern: ____ |
| SIGINT | Infrastructure or web change: ____ |
| FININT | Filing language, procurement award, or earnings dodge: ____ |
| GEOINT/DEMOINT | Terrain check: does the market they'd be entering actually exist at the size the move implies? ____ |

**Fusion verdict:** ____ disciplines, one story → confidence level → recommended response.

*Illustrative fill:* +20% specialized component orders (MASINT), 15 new filings in one patent class (TECHINT), 30+ platform engineers hired (HUMINT), new product subdomain cert issued (SIGINT), CFO dodges an analyst question on related capex (FININT), and the addressable segment supports the investment math (GEOINT/DEMOINT). Six disciplines, one story: high-confidence platform threat. Response: accelerate your own platform roadmap and arm sales with a maturity battle card *before* their launch, not after.

### The Fusion Cadence

- **Weekly:** SIGINT sweep (site diffs, pricing, job posts). 30 minutes.
- **Monthly:** OSINT + HUMINT digest. Review mining, employee sentiment, conference intel.
- **Quarterly:** FININT + TECHINT deep pass. Filings, patents, procurement awards.
- **Annual + every TAM refresh:** GEOINT/DEMOINT pass. Statistics releases lag; sizing rot is slow but real.
- **Event-driven:** MASINT alerts, material filings, leadership exits. React within 48 hours.

---

## Mapping Disciplines to Product Manager Artifacts

| Artifact | Primary Disciplines | Refresh Cadence |
|---|---|---|
| TAM/SAM/SOM | GEOINT/DEMOINT + FININT (capture rates) + TECHINT (technographics) | Annual, plus event-driven |
| ICPs & Personas | GEOINT/DEMOINT + HUMINT (win/loss ground truth) | Semi-annual |
| Messaging & localization | GEOINT/DEMOINT + OSINT | Semi-annual |
| Battle Cards | SIGINT + OSINT + HUMINT (win/loss) | Weekly SIGINT layer, monthly rebuild |
| Roadmap Bets | TECHINT + HUMINT | Quarterly |
| Positioning | OSINT + FININT (earnings language) | Semi-annual |
| Pricing Strategy | SIGINT + FININT + GEOINT/DEMOINT (wage/WTP corridors) | Event-driven |
| Threat Assessment | All-Source Fusion | Quarterly brief + event-driven |

---

## Regional Source Overlays

The disciplines do not change across markets. The sources do, and so does the evidentiary burden.

This compendium ships with a companion overlay system: after completing the Instantiate block, load the overlay matching your [GEOGRAPHY]. Each overlay maps regional sources onto the core disciplines without duplicating them.

**Currently available:** [*Regional Source Overlays: EU and MENA*](regional-source-overlays-eu-mena.md) (companion document).

Two lessons from that overlay worth internalizing regardless of region:

- **EU:** the challenge is finding the right record inside a rich but fragmented disclosure system. BRIS, TED, CORDIS, EUR-Lex, and Eurostat each hold a piece; nobody holds it all.
- **MENA:** the challenge is separating national ambition from funded, procured, permitted, operational commitment. Search in Arabic and English across the GCC and Levant, Arabic and French across North Africa, and never assume the English portal contains every notice. Record whether amounts are announced budgets, approved budgets, committed financing, tender values, or awarded contracts -- those are five different numbers wearing the same headline.

**Build-out candidates:** APAC, LATAM, Sub-Saharan Africa overlays, following the same pattern: procurement platforms, company registries, statistics bureaus, standards/regulatory databases, plus region-specific guardrails.

---

## Guardrails (The Short Version)

All of the above is legal, ethical, open-source collection. The line:

- **Yes:** anything published, filed, posted, or observable in public.
- **No:** pretexting (lying about who you are), soliciting NDA-protected info, hiring someone specifically to extract their former employer's secrets, scraping in violation of terms you agreed to.

Rules that keep the work honest:

- Document provenance on every claim. A Battle Card assertion without a source and date is an opinion wearing a badge.
- Capture and archive source documents at collection time. Portals restructure, files get replaced, historical search is not guaranteed.
- Signals inform decisions about outcomes, not feature-matching theater. The goal is never "they shipped X so we ship X." The goal is "this changes which customer problem wins the next investment."

The SCIP Code of Ethics is the industry reference. The rule of thumb: if you'd be uncomfortable explaining your method on stage at their user conference, don't use the method.

---

## One-Line Summary

Stop doing "competitive research" like a term paper. Run collection disciplines like an intelligence agency: independent channels, signal → inference chains, confidence stacking, regional overlays, and a fusion cadence. That's the steroids.
