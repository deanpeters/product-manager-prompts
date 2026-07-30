# full-spectrum-company-sweep-prompt.md
<!--
## Description:
Everything about one company, in one run. Sweeps all seven collection
disciplines back to back -- OSINT, FININT, TECHINT, HUMINT, GEOINT and
DEMOINT, SIGINT, MASINT -- carries each discipline's signals forward
into a single inventory, applies the confidence-stacking rule across
them, and ends with a call-ready brief: a sixty-second verbal summary,
the three things worth saying, the questions you will be asked with
answers, and the claims you must not make. Built for the product
manager who has to speak comprehensively about a company on short
notice.

## Standalone: yes

## Usage Note:
Reach for this when a company suddenly matters and you have one
sitting to get smart: a call scheduled for this afternoon, an exec who
just asked what you know about an acquirer, a competitor that turned
up in three lost deals this month, a partner about to see your
roadmap. Give it a company name and what the conversation is for, pick
a depth, and let it run. Rapid mode fits a coffee break; deep mode is
a research afternoon. Every claim carries a source and a Fact /
Inference / Assumption label, so you know which sentences you can say
out loud and which ones you have to hedge.

## When NOT to Use:
- You need maximum rigor on one discipline -- forensic financials, a
  full technology teardown, a systematic people sweep. This runs each
  discipline at collection-floor depth to fit them all in one pass.
- The subject is a market or category rather than a company: sizing,
  landscape, and forces analysis answer different questions.
- You already hold recent discipline sweeps and only need them
  reconciled: that is a synthesis job, not a collection job.
- The company is pre-public, pre-product, and pre-press: most
  disciplines will return nothing and the honest output is a short
  list of what cannot be known yet.

## Required Context Keys:
1. The company (name, and market or product line if ambiguous)
2. What the conversation or decision is -- a sales call, a partnership
   review, an acquisition rumor, a competitive threat
3. Depth: rapid, standard, or deep
4. Your relationship to them: competitor, prospect, partner, acquirer,
   vendor, or unknown

## Missing Context Rule:
Ask at most 3 questions, one at a time, offering three context-aware
options plus "Other" on each. Two standing bypasses at every turn:
"take your best guess" (answer it yourself, name the assumption) and
"bulk drop" (the user pastes what they already have; extract answers,
account for found / inferred / missing, ask only about gaps). If the
user has already given enough context, reduce or skip the questions
and say so. On silence, default to: standard depth, competitor
relationship, general strategic briefing, and proceed.

## Instructions:
1. Do the research. Never ask the user for facts that are publicly
   discoverable.
2. Run all seven disciplines in the fixed order below. Coverage you
   can defend beats whatever the search engine served first.
3. Announce each discipline as it starts and keep its findings in its
   own section, so the reader can see which channel produced which
   claim.
4. Real, checkable URLs with dates on every signal. Never invent
   financial figures, quotes, headcounts, review counts, patent
   numbers, or customer names.
5. Label everything Fact / Inference / Assumption. What a company says
   about itself is a claim, not a fact about the market.
6. A discipline that returns nothing gets reported as a gap, not
   padded. Empty sections are findings.
7. Apply the confidence-stacking rule in fusion: one discipline is a
   watch item, two is a working hypothesis, three or more is
   actionable, and disagreement between disciplines is itself a
   signal that someone is bluffing.
8. Close with the call-ready brief. That is the deliverable; the
   research is the evidence behind it.
9. ASCII only, no emojis.

## Pedagogic Notes:
- Running disciplines in a fixed order teaches collection discipline:
  what you swept is defensible, what you stumbled across is not.
- Keeping per-discipline sections visible before fusing teaches where
  a conclusion came from, which is what lets someone challenge one
  link instead of dismissing the whole brief.
- Confidence stacking teaches that corroboration across independent
  channels -- not the vividness of any single find -- is what turns a
  signal into something worth saying to an executive.
- The say / said-about gap and the do-not-say list teach the
  difference between what is true, what is defensible, and what will
  get you corrected in front of a customer.
- Reporting empty disciplines as gaps teaches that knowing what you
  do not know is part of the brief, not an embarrassment to hide.

## Attribution:
Created by Dean Peters (Productside.com). Collection and fusion
doctrine from the Competitive Research Compendium in this directory's
reference/ shelf.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 30, 2026
-->

## Purpose

Hello, Chatbot AI Assistant (that's you, ChatGPT, Claude, Gemini,
Perplexity, etc.). Act as an **all-source intelligence analyst**
briefing a product manager who has to speak about one company
comprehensively, soon, and be right.

Workflow: **intake -> search plan -> seven discipline sweeps ->
signal inventory -> fusion with confidence stacking -> call-ready
brief -> gaps.**

You do the fieldwork. The user supplies the target and the reason.

## Capability Check

State in one line whether you have web access.

- **Web access:** research live, cite URLs with dates.
- **No web access:** say so plainly, run from training data, mark
  every finding as an Assumption with its knowledge vintage, and
  invent nothing. A fabricated citation is worse than an admitted
  gap, and in a briefing it is worse still -- the user will repeat it
  out loud.

## Before You Start

Read the session first. If the company, the reason, and the depth are
already clear, say "I have what I need" and go straight to the search
plan.

Otherwise ask at most 3 questions, one at a time, three context-aware
options plus "Other" on each:

1. Which company, and which part of it matters -- a product line, a
   region, the whole entity?
2. What is the conversation? (customer call, partner review,
   acquisition rumor, competitive threat, board question)
3. How deep, and how soon?
   - **Rapid** -- the highest-value pass per discipline. Enough to
     hold a conversation without embarrassing yourself.
   - **Standard** -- the collection floor per discipline. The default.
   - **Deep** -- extended sweeps, more inference chains, more
     sourcing per claim.

Tell the user at every turn that they can say "take your best guess"
or paste what they already have. On silence: standard depth,
competitor framing, general strategic briefing. Proceed.

## Search Plan First

Before sweeping, show a **4-bullet plan**: the target's formal
identity (legal entity, tickers, major subsidiaries and brands), the
sweep order, the date window, and the noise filter -- how you will
avoid same-name companies, stale acquisitions, and press-release
recycling. Continue unless the user revises it.

## Trust Rules (all disciplines)

- Real, checkable URLs with dates on every signal.
- Never invent: revenue, funding amounts, headcounts, customer names,
  patent numbers, review counts, executive quotes, outage dates.
- Label every line **Fact** (documented) / **Inference**
  (evidence-based read, chain shown) / **Assumption** (working guess,
  basis stated).
- A company's own words are a claim. An announcement is intent until
  a second discipline shows commitment -- money moved, people hired,
  code shipped, buildings leased.
- When two sources conflict, show both and say which you carried
  forward and why. Do not average them into a comfortable middle.
- Where a discipline returns nothing, write "no signal found" and
  move on. Do not pad.

---

# Full-Spectrum Company Sweep: [TARGET]

**As-of date:** | **Prepared for:** [the conversation] | **Depth:**
[rapid / standard / deep] | **Relationship:** [competitor / prospect /
partner / acquirer / vendor]

## 0. Identity and Perimeter

Establish what you are actually researching before researching it:
legal entity, headquarters, ownership status (public, private, PE-held,
subsidiary), tickers, founding year, major brands and subsidiaries,
and the same-name confusions to avoid. One short block. Errors here
poison every section below.

---

## 1. OSINT -- The Public Record

Press, analyst coverage, social, review sites, events, community
forums.

- **Positioning in their own words** -- how they describe themselves,
  sourced.
- **What customers and analysts say** -- the outside view, sourced.
- **Say vs said-about gap** -- their language minus their customers'
  language. This gap is the exposed flank.
- **Recent announcements** -- labeled intent until corroborated.

| Signal | Source (URL, date) | Label |
|---|---|---|

## 2. FININT -- Money and Commitment

Filings, funding, pricing, unit economics, and where the money
actually goes.

- **Financial posture** -- revenue, growth, profitability, burn, or
  the absence of disclosure and what that implies.
- **Funding and ownership** -- rounds, investors, debt, PE pressure,
  and the exit clock their structure implies.
- **Pricing and packaging** -- published prices, discount behavior,
  packaging changes.
- **Spend signals** -- acquisitions, buybacks, layoffs, office moves.
  Money is the least deniable signal a company emits.

| Signal | Source (URL, date) | Label |
|---|---|---|

## 3. TECHINT -- What They Have Actually Built

Product, architecture, patents, release cadence, technical debt.

- **Product surface** -- what ships today versus what is announced.
- **Release cadence and direction** -- changelogs, release notes,
  deprecations. Deprecations are especially informative: they say
  what a company has given up on.
- **Patents and technical publications** -- where they are investing
  ahead of the market.
- **Architecture and dependency signals** -- stack, integrations,
  platform bets, and the constraints those bets impose.

| Signal | Source (URL, date) | Label |
|---|---|---|

## 4. HUMINT -- People and Intent

Leadership, hiring, departures, and what people say in public.

- **Leadership** -- who runs it, where they came from, what they built
  before. Executives repeat their last playbook more often than they
  invent a new one.
- **Hiring signals** -- open roles by function and geography. A job
  posting is a roadmap with a salary band.
- **Departures and tenure** -- churn concentrated in one function is a
  finding.
- **Public statements** -- interviews, conference talks, podcasts,
  earnings-call language.

| Signal | Source (URL, date) | Label |
|---|---|---|

## 5. GEOINT / DEMOINT -- Terrain and Population

Where they physically are, and which populations they serve.

- **Footprint** -- offices, data centers, manufacturing, warehouses,
  and what the geography enables or prevents.
- **Market and segment coverage** -- regions served, regulatory
  regimes entered, languages supported.
- **Customer demographics or firmographics** -- who they actually
  serve versus who they claim to serve.
- **Expansion and retreat** -- new locations opened, quietly closed.

| Signal | Source (URL, date) | Label |
|---|---|---|

## 6. SIGINT -- Emissions and Digital Exhaust

The traces a company leaves without meaning to.

- **Web and product telemetry** -- site changes, pricing page edits,
  documentation updates, status page history.
- **Job posting deltas** -- what appeared and disappeared since the
  last observable window.
- **Certifications and compliance** -- SOC 2, FedRAMP, ISO, HIPAA,
  and what markets they unlock.
- **Outages and incidents** -- public status history and how they
  communicate under pressure.

| Signal | Source (URL, date) | Label |
|---|---|---|

## 7. MASINT -- Measurable Signatures

Quantities and patterns, not narratives.

- **Scale proxies** -- app store ranks and review velocity, community
  size, support forum volume, integration counts, package download
  counts.
- **Trend direction** -- whether those proxies are rising, flat, or
  falling, with the window stated.
- **Anomalies** -- sudden discontinuities in any measured series, and
  candidate explanations.

| Signal | Source (URL, date) | Label |
|---|---|---|

---

## 8. Fusion -- Confidence Stacking

Now combine. For each story, list the disciplines that support it.

**The rule:** one discipline is a **watch item**. Two independent
disciplines make a **working hypothesis**. Three or more make it
**actionable**. Disciplines that disagree mean someone is bluffing --
usually the company's own messaging, and that contradiction is often
the most useful thing in this document.

| # | Story | Disciplines supporting | Confidence | So what |
|---|---|---|---|---|
| 1 | [What appears to be happening] | [OSINT + FININT + HUMINT] | [Watch / Hypothesis / Actionable] | [What it means for us] |

Rank by confidence, then by consequence. Cap at seven stories in
standard depth; the eighth is noise.

### Contradictions Worth Naming

- [Claim from one discipline] versus [evidence from another] -- and
  which one the money supports.

---

## 9. The Call-Ready Brief

This is what the user actually walks in with. Written to be spoken,
not read aloud verbatim.

### Sixty-Second Summary

One paragraph a PM can say from memory: who this company is, what
they are doing right now, where they are strong, where they are
exposed, and the one thing that matters most for this conversation.

### The Three Things Worth Saying

1. [Point] -- [the evidence in one clause]
2. [Point] -- [the evidence in one clause]
3. [Point] -- [the evidence in one clause]

Each must be a Fact or a well-corroborated Inference. Nothing on this
list may rest on a single Assumption.

### Questions You Will Be Asked

| Likely question | Short answer | Confidence |
|---|---|---|
| [What they will ask] | [How to answer] | [Solid / Hedge / Do not know] |

Include at least one question you cannot answer, with the honest
response. "I do not know, I will find out" is a better outcome than
a confident guess repeated by a customer.

### Do Not Say

Claims that are tempting, plausible, and not supported:

- [Claim] -- [why it does not hold up]

### If They Ask What We Do Better

Only if the relationship is competitor or prospect: the two or three
contrasts the evidence actually supports, phrased as outcomes rather
than feature lists, each traceable to a signal above.

---

## 10. Collection Gaps

- **Disciplines that returned little or nothing:** [list] -- and what
  that absence itself suggests.
- **Questions this sweep could not answer:** [list]
- **What would close each gap:** [the specific source, filing,
  conversation, or discipline-level deep sweep that would resolve it]

### Assumptions to Validate
- [The assumption that most changes the brief if wrong]
- [Second]
- [Third]

---

## Anti-Patterns to Refuse

- A confident claim built from one discipline and stated without its
  confidence level.
- Any invented number, quote, customer name, or URL.
- A brief that hides its gaps to look complete. The gap list is a
  feature; a PM who knows what they do not know outperforms one who
  does not.
- Treating a company's own announcement as evidence of commitment.
- Padding an empty discipline to fill the section.

## Final Step

Offer exactly 4 options:

1. Run the deep single-discipline sweep on whichever channel looks
   thinnest -- osint-, finint-, techint-, humint-,
   geoint-demoint-, sigint-, or masint-collection-prompt.md
   (Recommended)
2. Turn the fusion stories into a battle card with
   battle-card-builder-prompt.md
3. Set this up as a recurring watch with
   competitive-intel-watch-prompt.md so the next brief is a diff
   rather than a rebuild
4. Convert the call-ready brief into a one-page leave-behind for the
   wider team

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom path.
