# tam-sam-som-analysis-prompt.md
<!--
## Description:
Runs a fully autonomous, citation-backed TAM/SAM/SOM analysis. The AI
does the heavy lifting with real-world data and clickable sources,
defaulting to strong evidence-based assumptions rather than waiting on
the user. Demonstrates the autonomous investigation interaction mode
(see interaction-modes.md).

## Usage Note:
Fill in the bracketed context block before running. This is the
autonomous sibling of prompt-generators/tam-sam-som-prompt-generator.md:
use the generator when you want to be facilitated through scoping
decisions; use this prompt when you know the scope and want a
defensible model built for you. Because it proceeds without further
input, it is suitable for agent, loop, or scheduled runs.

## When NOT to Use:
- You have not yet decided product, buyer, or geography: use the
  facilitated generator to scope first.
- You need internal-data sizing (pipeline, usage telemetry): this
  prompt is built on public evidence.
- You need a market landscape (players, segments, dynamics) rather
  than a size: that is a different investigation.

## Required Context Keys:
1. Product or service to size
2. Geography or market boundary
3. Target buyer (and secondary audience, if any)
4. Product type and delivery model
5. Pricing anchor, if one exists

## Missing Context Rule:
Ask no more than 4 total questions, and only if absolutely necessary to
refine assumptions. If the user does not respond, default to strong,
evidence-based assumptions, label them explicitly, and proceed.

## Instructions:
1. Do the research yourself using real-world data; do not ask the user
   to supply facts that are publicly discoverable.
2. Require bottom-up calculations, not just top-down percentages.
3. Cite a clickable URL for every major data point, from credible
   source classes: government statistics, industry analyst reports,
   company filings, workforce data (e.g., LinkedIn), trade bodies.
4. Where data is uncertain, show ranges and explain why.
5. Governing criterion: prioritize speed and defensibility over
   perfection.
6. Keep the output section order exactly as specified; it is a stable
   schema for comparing runs over time.
7. Use ASCII characters only; no emojis.

## Pedagogic Notes:
- Teaches the autonomous investigation mode: overridable defaults, a
  question budget, and proceed-on-silence make a prompt schedulable.
- Bottom-up modeling trains PMs to distrust top-down market-share
  arithmetic ("1% of a big number") in favor of unit-level logic.
- The evidence contract (URL per data point, named source classes)
  teaches what makes a market model defensible in an executive review.
- Best / base / worst sensitivity exposes uncertainty structurally
  instead of hiding it in hedge words.

## Attribution:
Created by Dean Peters (Productside.com). TAM/SAM/SOM framework as
popularized in venture and product strategy practice.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Context

You are a TAM/SAM/SOM modeling expert. Build a fully defensible TAM,
SAM, and SOM analysis for the product and market defined below.

Do the heavy lifting yourself using real-world data and citations. Only
ask questions if absolutely necessary to refine assumptions — no more
than 4 total — and default to strong, evidence-based assumptions if the
user does not respond.

## Scope (Overridable Defaults)

Use this positioning unless the user overrides it:

- Product or service: [What is being sized, e.g., "AI product
  management training course"]
- Geography / market boundary: [e.g., "UK and European Union"]
- Target buyer: [e.g., "Corporate L&D / HR teams buying for product
  organizations"]
- Secondary audience: [e.g., "Individual product managers"; use for
  sensitivity analysis]
- Product type: [e.g., "Premium professional training"]
- Delivery model: [e.g., "Mix of live cohort-based and self-paced"]
- Pricing anchor: [Known price point or "benchmark against comparable
  offerings"]

## Model Requirements

1. TAM: total demand across all relevant customers in the defined
   market boundary
2. SAM: the serviceable segment realistically addressable given the
   positioning above
3. SOM: realistic 3-5 year capture, benchmarked against comparable
   companies in the space

The output must include:

- Market size (currency and number of customers)
- Clear segmentation (by geography or sub-segment where possible)
- Bottom-up calculations, not just top-down percentages
- Pricing assumptions, with benchmarks
- Adoption and penetration assumptions, with justification
- Competitive benchmarks (named comparable companies)
- Demand signals relevant to this category
- All assumptions explicitly listed

## Citations

- Include a clickable URL for every major data point
- Use credible sources: government data, industry analyst reports,
  company filings, workforce data, trade bodies
- If a needed number cannot be sourced, say so, estimate with a stated
  method, and mark it as an assumption

## Process Rules

- Ask no more than 4 total questions, only if needed
- If data is uncertain, show ranges and explain why
- Prioritize speed and defensibility over perfection
- If no further input is provided, proceed immediately using
  best-available data

## Output Format

Use this exact structure:

1. Executive summary (top-line numbers)
2. TAM / SAM / SOM breakdown
3. Key assumptions
4. Sensitivity analysis (best / base / worst case)
5. Sources (with links)

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 next options:
1. Pressure-test the weakest assumption with deeper research
   (Recommended)
2. Rebuild the model for an alternate segment or geography
3. Convert the analysis into a one-slide executive summary
4. Draft the positioning statement this market model implies

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom
path.
