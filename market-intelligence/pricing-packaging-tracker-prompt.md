# pricing-packaging-tracker-prompt.md
<!--
## Description:
Tracks competitor pricing and packaging over time: captures current
public pricing pages into a stable schema, diffs against the prior
capture, and reports tier changes, price moves, feature-gate shifts,
and packaging restructures — with screenshots-in-words and URLs.

## Usage Note:
Run once to create the pricing baseline for a competitor set, then
on a cadence (monthly or quarterly). Public pricing only; where
pricing is "contact sales," track what IS public (editions, gates,
published floors) and label the rest. Feeds the competitive watch,
battle cards, and pricing decisions.

## When NOT to Use:
- You need pricing strategy advice: this tracks the market; it does
  not recommend your price.
- Pricing is fully opaque across the set: expect thin results;
  win/loss and VoC mining may reveal more.

## Required Context Keys:
1. Competitor set (or the snapshot they came from)
2. Prior pricing capture, if one exists
3. Your own pricing context, if comparisons should include you

## Missing Context Rule:
Ask at most 2 questions:
1. "Which competitors' pricing should I track?"
2. "Prior capture to diff against, or is this the baseline?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Capture from live pricing pages; URL and as-of date per
   competitor. Never invent prices, tiers, limits, or discounts.
2. Diff mode when a prior capture exists: report changes only.
3. Record structure, not just numbers: tiers, billing units, feature
   gates, usage limits, free-tier boundaries, enterprise floor
   signals.
4. Mark "contact sales" honestly; infer only with labels.
5. Label key points Fact, Inference, or Assumption.
6. Keep the capture schema exactly; diffability is the point.

## Pedagogic Notes:
- Packaging changes (gates, limits, tier restructures) usually
  signal strategy earlier than price changes do.
- The stable capture schema teaches that pricing intel is a time
  series, not a screenshot.

## Attribution:
Created by Dean Peters (Productside.com).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Purpose

Track competitor pricing and packaging as a diffable time series.
Workflow: **capture (or diff) -> structure changes -> price changes ->
signals -> next-step options.**

## Mode

Baseline mode: no prior capture — produce the capture and stop.
Delta mode (default with a prior capture): diff and report changes
only. Just Enough Mode throughout.

## Before You Start

Ask at most 2 questions:

1. Which competitors' pricing should I track?
2. Prior capture to diff against, or is this the baseline?

If unanswered, proceed with labeled assumptions.

## Source + Trust Rules

Live pricing pages, plan-comparison pages, published rate cards,
credible pricing-change coverage. URL and as-of date per competitor.
Do not invent **prices, tiers, limits, discounts, or negotiated
figures.** "Contact sales" is recorded as such.
Label: **Fact**, **Inference**, **Assumption**.

# Pricing Capture / Delta Report

## 1. Run Header

**Competitor set:**
**Prior capture date:** [or "baseline run"]
**This run date:**

## 2. Pricing Capture (per competitor)

### [Competitor] — [pricing page URL, as-of date]
- **Tiers:** [name: price / unit / billing terms, one bullet each]
- **Key gates:** [which capabilities gate which tier, 2-4 bullets]
- **Usage limits:** [the limits that matter, 1-2 bullets]
- **Free tier / trial:** [boundary, 1 bullet]
- **Enterprise signals:** [published floors, "contact sales" scope]

(Baseline mode: full capture per competitor. Delta mode: this
section only for competitors with changes.)

## 3. Changes Since Last Capture (Delta Mode)

### [Competitor] — [4 to 8 word change summary]
- **Then / Now:** [old -> new, labeled Fact]
- **Evidence:** [URL, date]
- **Reading:** [Inference — repositioning, monetization push,
  response to whom?]

If nothing changed: "No pricing or packaging changes this cycle."

## 4. Signals

- [Cross-competitor patterns: direction of the market's pricing,
  labeled]
- [Implications for your pricing or battle cards: 2-3 bullets]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Update battle card pricing sections from these changes
2. Deep-dive one competitor's packaging logic
3. Compare your pricing against this capture
4. Set the cadence and watchlist for the next run

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
