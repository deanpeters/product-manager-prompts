# competitive-research-snapshot-prompt.md
<!--
## Description:
Researches a company's competitive landscape as a workflow, not a
one-shot answer: search plan, competitor selection, just-enough
research, Fact/Inference/Assumption labels, real URL citations, and
next-step options. Produces a stable snapshot schema that downstream
prompts (battle cards, delta monitors) can consume and diff.

## Usage Note:
Use when a product decision needs competitive grounding: positioning,
roadmap bets, deal support, board prep. The output is a decision
support snapshot, not a market report. Because it proceeds on labeled
assumptions when questions go unanswered, it can run as an agent
task or on a schedule; re-run it and diff against the prior snapshot.
Companion: workshops/battle-card-workshop.md consumes
this snapshot when the next step is sales enablement.

## When NOT to Use:
- You need market sizing, not landscape: use
  market-intelligence/tam-sam-som-analysis-prompt.md.
- You need deep intel on one company (executive signals, strategy):
  use prompts/company-profile-executive-insights-research.md.
- The competitor set and facts are already gathered: go straight to
  the battle card or comparison artifact.

## Required Context Keys:
1. Company, product, or segment to research
2. The decision this research should support
3. Known competitors, or permission to identify them

## Missing Context Rule:
Ask only what is needed, max 3 questions:
1. "What company/product/segment?"
2. "What decision should this support?"
3. "Known competitors, or should I identify them?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show the search plan before researching; continue unless revised.
2. Just Enough Mode by default; Verbose Mode only if asked.
3. Real, checkable URLs from mixed source types.
4. Never invent competitors, features, pricing, market share,
   customer wins, roadmap items, or product claims.
5. Label key points Fact, Inference, or Assumption; keep labels short.
6. Keep the snapshot section order exactly; it is a stable schema
   for diffing runs over time.

## Pedagogic Notes:
- The search-plan gate teaches a cheap correction point: review the
  plan for 10 seconds instead of the report for 10 minutes.
- Fact / Inference / Assumption labeling teaches three-level evidence
  honesty; most competitive "facts" in decks are unlabeled inference.
- The do-not-invent list names exactly where AI fabricates in this
  domain, teaching users what to verify first.
- Just Enough Mode teaches that research value is decision support,
  not page count.

## Attribution:
Competitive Research workflow prompt created by Dean Peters
(Productside.com).

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Purpose

Research a company's competitive landscape using a workflow, not a
one-shot answer.
Workflow: **search plan -> competitor selection -> just-enough
research -> fact/inference labels -> real URL citations -> next-step
options.**

## Mode

Use **Just Enough Mode** by default: short bullets, strongest
findings only, real URLs, labeled facts/inferences/assumptions, no
giant report.
Use **Verbose Mode** only if asked.

## Before You Start

Ask only what is needed, max 3 questions:

1. What company/product/segment?
2. What decision should this support?
3. Known competitors, or should I identify them?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Before researching, show a **3-bullet plan**:

- what you'll search
- source types you'll use
- how you'll separate facts from inferences

Then continue unless I ask you to revise.

## Competitor Selection

Use provided competitors.
If none are provided, identify the top **3**. Use **4** only if
clearly needed.

For each: **Name; why relevant; source URL; confidence.**

## Source + Trust Rules

Use real, checkable URLs. Mix sources: **company sites;
product/pricing pages; customer stories; press releases; investor
materials; credible news; analyst/review sites.**
Do not invent **competitors, features, pricing, market share,
customer wins, roadmap items, or product claims.**

Label key points:

- **Fact:** source-supported
- **Inference:** evidence-based interpretation
- **Assumption:** working guess

Keep labels short.

# Competitive Research Snapshot

## 1. Scope

**Company/product:**
**Category:**
**Decision supported:**
**Competitors analyzed:**

## 2. Competitor Snapshots

For each competitor, use max **5 bullets**:

### Competitor: [Name]

- **Positioning:**
- **Relevant capability:**
- **Likely strength:**
- **Likely weakness:**
- **Key source URL:**

## 3. Quick Comparison

| Dimension | Company | Comp 1 | Comp 2 | Comp 3 |
|---|---|---|---|---|
| Target customer | | | | |
| Core use case | | | | |
| Main strength | | | | |
| Main weakness | | | | |
| Evidence quality | | | | |

## 4. So What?

Provide only:

- **3** product strategy implications
- **2** competitive risks
- **2** product opportunities
- **3** assumptions to validate

Each bullet includes: **label, confidence, source URL where
relevant.**

## Final Step

Offer exactly 4 options:

1. Competitive battlecard
2. Executive comparison matrix
3. Product risks/opportunities for next 2 quarters
4. Discovery questions to validate assumptions

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
