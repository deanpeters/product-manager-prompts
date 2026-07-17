# geoint-demoint-collection-prompt.md
<!--
## Description:
Runs a GEOINT/DEMOINT (Geospatial and Demographic Intelligence)
collection sweep on a market: establishment counts by industry
code, occupation and wage statistics, firmographic distributions,
regional industry concentration, and trade flows — the government
statistics most Product Managers never open. Every signal lands in
a fusion-ready inventory with a source URL, date, evidence label,
and the inference chain it supports. The cartographer's discipline:
the terrain map, not troop movement — and the backbone of every
ICP, Persona, and TAM that survives scrutiny.

## Usage Note:
One of seven discipline collection prompts feeding
all-source-fusion-prompt.md; doctrine in
reference/competitive-research-compendium.md (GEOINT/DEMOINT
discipline). This prompt reads the terrain; for the full sizing
recipe (TAM x filters x capture rate) hand off to
tam-sam-som-analysis-prompt.md, and for macro-factor deltas to
pestel-delta-monitor-prompt.md. For EU and MENA statistical
sources, load reference/regional-source-overlays-eu-mena.md.

## When NOT to Use:
- You need the finished market-size number: run tam-sam-som-analysis;
  this sweep produces its denominators and corridors.
- You are watching macro shifts quarter over quarter: that is the
  PESTEL delta monitor's job.
- The question is about one competitor, not the terrain: use the
  company-focused disciplines (OSINT, FININT, TECHINT).

## Required Context Keys:
1. The [MARKET] and its industry codes (NAICS/SIC/NACE or nearest
   equivalent)
2. The [GEOGRAPHY] in scope, at country level
3. The [BUYER] and end-user roles (drives occupation and wage
   lookups)
4. The [DECISION] this terrain read will feed

## Missing Context Rule:
Ask at most 3 questions:
1. "Which market — and do you know its industry codes, or should I
   propose them?"
2. "Which countries are in scope?"
3. "Who is the buyer and who is the end user, by job title?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show a 3-bullet search plan first: statistics sources for the
   [GEOGRAPHY], the industry codes to pull, the occupations to
   look up. Continue unless revised.
2. Sweep in this order: establishment counts by industry code and
   size band, occupation counts and growth for [BUYER] and end-user
   roles, wage trends in those roles, regional industry
   concentration, firmographic distributions (size bands, legal
   forms, sectors), trade flows in product-specific codes.
3. Use official statistics first (census bureaus, labor statistics,
   statistical institutes, trade databases); analyst reports only
   as cross-checks — if two independent estimates disagree by 3x,
   say so rather than averaging.
4. Log every signal in the Signal Inventory: what was observed,
   source URL with date, Fact / Inference / Assumption label, the
   inference chain it supports, and the artifact it feeds.
5. Run the compendium's GEOINT/DEMOINT inference chains explicitly:
   establishment counts = the bottom-up TAM denominator; regional
   concentration = where SOM actually lives and where field sales
   should live; occupation growth curves = is the population you
   sell to growing or shrinking; wage trends = willingness-to-pay
   ceiling shifts; firmographic distributions = ICP boundaries from
   data, not vibes; buyer-title prevalence by [GEOGRAPHY] = persona
   localization (the VP of Product in Boston is a Head of Digital
   in Frankfurt and may not exist in Riyadh); trade-flow shifts =
   market entry or supply relocation before any announcement.
6. Name the statistical vintage of every dataset — statistics lag,
   and sizing rot is slow but real; flag anything older than the
   decision's horizon.
7. Keep the schema stable so run N and N+1 are diffable; if a
   prior terrain read is in session, lead with the delta.

## Pedagogic Notes:
- Pulling establishment counts by industry code teaches bottom-up
  sizing discipline: a denominator you can cite beats a top-down
  percentage of someone else's TAM.
- Drawing ICP boundaries from firmographic distributions builds
  the habit of segmenting on observable structure instead of
  aspiration.
- Persona localization by title prevalence teaches that messaging
  is terrain-dependent: the same product meets a different org
  chart in every geography.

## Attribution:
Created by Dean Peters (Productside.com). Collection doctrine from
the Competitive Research Compendium in this directory's reference/
shelf, GEOINT/DEMOINT discipline.

## Licensing:
MIT License

Date: July 16, 2026
-->

## Purpose

Map the terrain of one market from official statistics and land
every signal in a fusion-ready inventory.
Workflow: **search plan -> counts, occupations, wages, trade ->
signal inventory -> inference chains -> ICP and persona read ->
gaps and handoffs.**

## Mode

**Just Enough Mode**: strongest signals only, max 5 inference
chains, one-line watch items. **Verbose Mode** only if asked.

This is a collection prompt: it gathers and labels; it does not
verdict. Confidence rating across disciplines belongs to
[all-source-fusion-prompt.md](all-source-fusion-prompt.md).

## Before You Start

Ask at most 3 questions:

1. Which market — known industry codes, or should I propose them?
2. Which countries are in scope?
3. Who is the buyer and who is the end user, by title?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: the statistics sources for the
[GEOGRAPHY] (for EU and MENA, per the regional overlay), the
industry codes, and the occupations. Continue unless revised.

## Source + Trust Rules

Real, checkable URLs with dates and dataset vintages on every
signal. Do not invent **establishment counts, employment figures,
wage levels, growth rates, or trade volumes.** Official statistics
outrank analyst estimates; where independent estimates disagree by
3x, report the disagreement. Label every signal: **Fact** /
**Inference** / **Assumption**.

# GEOINT/DEMOINT Collection: [MARKET] in [GEOGRAPHY]

**As-of date:** | **Decision supported:** | **Prior read:** [date
or "first run"]

## 1. Signal Inventory (fusion-ready)

| Signal | Source (URL, date, vintage) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| [What was observed] | [URL, date, data year] | [F/I/A] | [What it implies] | [TAM / ICP / Persona / Messaging / ...] |

## 2. Strongest Inference Chains (max 5, ranked)

- [Signal cluster] -> [inference, labeled] -> [artifact it should
  change, and the move]

## 3. Terrain Read

- **TAM denominator:** [establishment count, code, size bands,
  vintage — hands off to tam-sam-som-analysis]
- **Where SOM lives:** [regional concentration, sourced]
- **Buyer population trajectory:** [occupation growth, sourced]
- **WTP corridor:** [wage trend read, labeled Inference]
- **ICP boundary candidates:** [firmographic cut, labeled]
- **Persona localization notes:** [title prevalence by country]

## 4. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 5. Collection Gaps and Handoffs

- [Uncovered dataset or stale vintage] — [impact on confidence]
- Deep dives: full sizing recipe -> tam-sam-som-analysis; macro
  deltas -> pestel-delta-monitor; regional sources -> reference
  overlay

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Feed this inventory into all-source fusion with the other
   disciplines
2. Run the denominators into a full TAM/SAM/SOM analysis
3. Draft ICP boundaries and persona localization notes from the
   terrain read
4. Schedule-ready version: save as the baseline the annual terrain
   refresh diffs against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
