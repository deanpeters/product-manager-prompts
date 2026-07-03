# porters-five-forces-prompt.md
<!--
## Description:
Reads an industry's structure through Porter's Five Forces with
cited evidence: rivalry, threat of new entrants, threat of
substitutes, buyer power, and supplier power — each force rated
with the documented signals that justify the rating, plus the
profit-pool implication most five-forces decks skip.

## Usage Note:
Use before entering a market, when margins are eroding and nobody
can say why, or to pressure-test a strategy that assumes the
industry is kinder than it is. Pairs upstream with
market-landscape-scan-prompt.md (who plays) — this asks what the
structure does to everyone who plays. Include AI-driven substitution
explicitly; in 2026 it is the substitute threat in most knowledge
industries.

## When NOT to Use:
- You need one company's position: use swot-analysis-prompt.md;
  five forces reads the industry, not a player.
- Nascent categories with no stable structure: the forces are still
  forming; run the landscape scan and revisit.

## Required Context Keys:
1. The industry or segment (be specific: "clinical data management
   SaaS," not "healthcare")
2. The decision this analysis should support
3. Geography, if the structure differs by region

## Missing Context Rule:
Ask at most 3 questions:
1. "Which industry or segment, as precisely as you can name it?"
2. "What decision should this support?"
3. "Any geographic boundary?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show the search plan (3 bullets) first; continue unless revised.
2. Rate each force weak / moderate / strong, and justify the rating
   with documented signals — concentration data, switching costs,
   entry examples, substitute adoption, margin trends. The rating
   without the signals is vibes.
3. Every signal carries a URL and a Fact / Inference / Assumption
   label. Never invent market share, margin data, or entrants.
4. Treat AI-driven substitution as a named candidate in the
   substitutes force.
5. Close with where the profit pool sits and who is squeezing it —
   the analysis exists to answer that.

## Pedagogic Notes:
- Forces-with-signals teaches the difference between naming a
  framework and using one: each rating must survive "how do you
  know?"
- Buyer/supplier power analysis trains PMs to see pricing power as
  structural, not a negotiation skill.
- The profit-pool close teaches that five forces is an argument
  about where margin goes, not a diagram for slide four.

## Attribution:
Created by Dean Peters (Productside.com). Framework: Michael E.
Porter, "How Competitive Forces Shape Strategy" (HBR, 1979).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Purpose

Read an industry's structure through the five forces, with evidence.
Workflow: **search plan -> force-by-force ratings with signals ->
profit-pool implication -> next-step options.**

## Mode

**Just Enough Mode**: 2-4 signals per force, strongest evidence
only. **Verbose Mode** only if asked. If a landscape scan is in
session, build on it; search only gaps.

## Before You Start

Ask at most 3 questions:

1. Which industry or segment, precisely?
2. What decision should this support?
3. Any geographic boundary?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: what you'll search per force, source
types (filings, analyst coverage, trade press, pricing pages,
funding databases), fact/inference separation. Continue unless
revised.

## Source + Trust Rules

Real, checkable URLs with dates. Do not invent **market share,
margin data, entrant names, funding rounds, or adoption figures.**
Label every signal: **Fact** / **Inference** / **Assumption**.

# Five Forces: [Industry / Segment]

**As-of date:** | **Boundary:** | **Decision supported:**

## 1. Competitive Rivalry — [weak / moderate / strong]

- Signals: [concentration, growth rate, differentiation, exit
  barriers — each with URL + label]
- What it means here: [one sentence]

## 2. Threat of New Entrants — [weak / moderate / strong]

- Signals: [entry barriers, capital needs, recent entrants and how
  they fared, regulation — each with URL + label]
- What it means here: [one sentence]

## 3. Threat of Substitutes — [weak / moderate / strong]

- Signals: [substitute adoption, price-performance trajectory,
  switching evidence — each with URL + label]
- AI-driven substitution, named and assessed: [labeled]
- What it means here: [one sentence]

## 4. Buyer Power — [weak / moderate / strong]

- Signals: [buyer concentration, switching costs, price
  transparency, backward-integration examples — URL + label]
- What it means here: [one sentence]

## 5. Supplier Power — [weak / moderate / strong]

- Signals: [supplier concentration (including cloud/model/platform
  dependencies), input differentiation — URL + label]
- What it means here: [one sentence]

## 6. The Profit Pool (the "so what")

- Where margin sits today, and the force squeezing it: [labeled]
- Structure trend: [tightening / loosening, on what evidence]
- For your decision: [2 sentences tying structure to the decision
  named above]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Trace the strongest force into your strategy's exposed
   assumptions
2. Run the landscape scan to name the players behind each force
3. Feed the profit-pool read into an Ansoff growth-options analysis
4. Schedule-ready version: which force signals should a re-run
   watch?

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`,
or a custom path.
