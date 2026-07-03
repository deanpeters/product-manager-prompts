# pestel-delta-monitor-prompt.md
<!--
## Description:
Quarterly PESTEL refresh: re-scans the political, economic, social,
technological, environmental, and legal factors from a prior PESTEL
analysis and reports which factors materially moved, which
assumptions broke, and what new factors entered the frame — with
cited evidence.

## Usage Note:
Run prompts/pestel-analysis-prompt-template.md once to create the
baseline, then run this on a cadence (quarterly is typical) with the
prior analysis in session. Macro factors move slowly; the value is
catching the two that moved, not re-debating the twenty that did
not.

## When NOT to Use:
- No baseline PESTEL exists: run the template first.
- The business context changed fundamentally (new market, pivot):
  redo the full analysis; do not diff across a scope change.

## Required Context Keys:
1. Prior PESTEL analysis (pasted or attached)
2. The product/market scope it covered
3. Any known events since the last run worth checking

## Missing Context Rule:
Ask at most 2 questions:
1. "Do you have the prior PESTEL to paste?"
2. "Any events since then you already suspect matter?"
If unanswered and no prior analysis exists, recommend running the
PESTEL template first and stop.

## Instructions:
1. Read the prior analysis fully; diff against it, factor by factor.
2. Show the search plan (3 bullets) before researching; continue
   unless revised.
3. Report only material movement: regulation passed or proposed,
   macro shifts crossing thresholds, technology maturation,
   social-signal changes with evidence. "No material movement" per
   factor is a valid and common result.
4. Never invent regulations, statistics, or events; real URLs and
   dates.
5. Label key points Fact, Inference, or Assumption.
6. Just Enough Mode by default.

## Pedagogic Notes:
- Diffing macro factors teaches which PESTEL entries were live
  assumptions versus furniture; broken assumptions are the output.
- The cadence discipline turns PESTEL from a one-time workshop
  artifact into an operating radar.

## Attribution:
Created by Dean Peters (Productside.com). Extends the PESTEL
analysis template.

## Licensing:
MIT License

Date: July 3, 2026
-->

## Purpose

Refresh a PESTEL analysis by diffing each factor against the prior
run and reporting material movement only.
Workflow: **search plan -> factor-by-factor diff -> broken
assumptions -> new entrants to the frame -> next-step options.**

## Mode

Requires a prior PESTEL analysis. If none exists, recommend running
the PESTEL template first and stop. Just Enough Mode throughout.

## Before You Start

Ask at most 2 questions:

1. Prior PESTEL to paste?
2. Any events since then you already suspect matter?

If the prior analysis is provided, proceed; label assumptions.

## Search Plan First

Show a **3-bullet plan**: which factor categories get active
searching this cycle, source types, fact/inference separation.
Continue unless revised.

## Source + Trust Rules

Government and regulatory sources, central-bank and statistical
data, credible news, industry bodies, standards organizations. Real
URLs and dates.
Do not invent **regulations, statistics, dates, or events.**
Label: **Fact**, **Inference**, **Assumption**.

# PESTEL Delta Report

## 1. Run Header

**Scope (from prior analysis):**
**Prior analysis date:**
**This run date:**

## 2. Factor-by-Factor Delta

For each of P / E / S / T / E / L:

### [Factor]: [moved / no material movement]
- **What moved:** [1-2 bullets, labeled, cited — only if moved]
- **Prior assumption affected:** [which entry from the baseline]
- **Reading:** [Inference — implication for the product scope]

Keep "no material movement" factors to a single line each.

## 3. Broken Assumptions

- [Baseline entries now contradicted by evidence — the run's most
  important section; cited]

## 4. New to the Frame

- [Factors absent from the baseline that now warrant a slot]

## 5. So What?

- **3** implications for strategy or roadmap
- **2** factors to watch closely next cycle
- **3** assumptions to validate

Each bullet: label, confidence, URL where relevant.

## Final Step

Offer exactly 4 options:

1. Update the baseline PESTEL with these deltas (new baseline)
2. Deep-dive the most consequential moved factor
3. Trace the broken assumptions into roadmap or OKR impact
4. Set next cycle's watch priorities

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
