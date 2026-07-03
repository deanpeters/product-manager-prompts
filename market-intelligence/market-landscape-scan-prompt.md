# market-landscape-scan-prompt.md
<!--
## Description:
Autonomous market discovery: maps a segment's players (direct,
adjacent, substitutes, emerging), how the market segments, where the
money and momentum are, and where the whitespace is — with cited
evidence and labeled inference. Produces the landscape view that
feeds market sizing, positioning, and competitor selection.

## Usage Note:
Use when entering or re-evaluating a market, scoping a new product
line, or preparing strategy work that needs a defensible view of who
plays where. Downstream: feeds
market-intelligence/tam-sam-som-analysis-prompt.md (sizing),
competitive-research-snapshot-prompt.md (deep-dive on selected
players), and prompts/positioning-statement.md.

## When NOT to Use:
- You know the players and need depth on a few: use the competitive
  research snapshot.
- You need a market size: this maps structure, not magnitude; use
  the TAM/SAM/SOM prompt (they pair well).

## Required Context Keys:
1. The market, segment, or problem space to map
2. The decision this landscape should support
3. Geography or boundary, if narrower than global

## Missing Context Rule:
Ask at most 3 questions:
1. "What market or problem space, in your words?"
2. "What decision should this landscape support?"
3. "Any boundary — geography, buyer size, price band?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show the search plan (3 bullets) before researching; continue
   unless revised.
2. Map by how buyers see the market, not vendor marketing
   categories; note where the two disagree.
3. Include substitutes and non-consumption ("they use spreadsheets")
   as competitors.
4. Never invent companies, funding, market share, or product claims.
5. Label key points Fact, Inference, or Assumption; real checkable
   URLs.
6. Just Enough Mode by default; Verbose only if asked.
7. Keep the output schema exactly; it is a stable base for re-scans.

## Pedagogic Notes:
- Segmenting by buyer view versus vendor category teaches PMs that
  analyst quadrants are a map someone else drew for their own
  purposes.
- Treating non-consumption as a competitor is the most commercially
  useful habit in market analysis.
- Whitespace claims must survive the "or is it a dead zone?" test:
  empty space is either opportunity or evidence of no demand.

## Attribution:
Created by Dean Peters (Productside.com).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Purpose

Map a market's structure using a workflow, not a one-shot answer.
Workflow: **search plan -> segmentation -> player mapping ->
dynamics -> whitespace -> next-step options.**

## Mode

**Just Enough Mode** by default: short bullets, strongest findings,
real URLs, labeled facts/inferences/assumptions. **Verbose Mode**
only if asked.

## Before You Start

Ask at most 3 questions:

1. What market or problem space, in your words?
2. What decision should this landscape support?
3. Any boundary — geography, buyer size, price band?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Before researching, show a **3-bullet plan**: what you will search,
source types, how you will separate facts from inferences. Then
continue unless asked to revise.

## Source + Trust Rules

Real, checkable URLs. Mixed sources: analyst and review sites,
company and pricing pages, funding databases, industry press, trade
bodies, practitioner communities.
Do not invent **companies, products, funding rounds, market share,
growth rates, or customer claims.**
Label: **Fact**, **Inference**, **Assumption**.

# Market Landscape Snapshot

## 1. Scope

**Market / problem space:**
**Boundary:**
**Decision supported:**
**As-of date:**

## 2. How This Market Segments

- [3-5 segments as buyers experience them, each 1 bullet]
- [Where vendor categories disagree with buyer reality: 1 bullet]

## 3. Player Map

### Direct players
- **[Name]:** [who they serve; wedge; 1 signal of momentum; URL]

### Adjacent players (could enter)
- **[Name]:** [why adjacency matters; URL]

### Substitutes and non-consumption
- **[What buyers do instead]:** [why it persists]

### Emerging entrants
- **[Name]:** [what bet they are making; funding/traction signal; URL]

Cap the full map at 12 players; strongest signal only.

## 4. Dynamics

- **Where the money is:** [2 bullets, labeled]
- **Where the momentum is:** [2 bullets, labeled]
- **Consolidation or fragmentation:** [1 bullet]
- **Technology or regulatory shifts in play:** [1-2 bullets]

## 5. Whitespace and Dead Zones

- **[Apparent gap]:** opportunity or dead zone? [evidence either way]
- [2-3 of these, each with the honest counter-reading]

## 6. So What?

- **3** implications for the decision named in Scope
- **2** players to deep-dive next
- **3** assumptions to validate

Each bullet: label, confidence, URL where relevant.

## Final Step

Offer exactly 4 options:

1. Run the competitive research snapshot on the deep-dive players
2. Run TAM/SAM/SOM sizing on the most promising segment
3. Draft a positioning hypothesis against this landscape
4. Schedule-ready version: what should a quarterly re-scan watch?

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
