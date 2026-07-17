# osint-collection-prompt.md
<!--
## Description:
Runs an OSINT (Open Source Intelligence) collection sweep on a
target company: press and newsroom output, analyst coverage, exec
social posts, review-site clusters, conference footprint, webinar
cadence, and prediction-market odds. Every signal lands in a
fusion-ready inventory with a source URL, date, evidence label, and
the inference chain it supports. The journalist's-desk discipline:
what a good beat reporter knows before the press release drops.

## Usage Note:
One of seven discipline collection prompts feeding
all-source-fusion-prompt.md; doctrine in
reference/competitive-research-compendium.md (OSINT discipline).
For deep review mining hand off to voice-of-customer-miner-prompt.md;
for whole-market mapping use market-landscape-scan-prompt.md. This
prompt owns the discipline-wide sweep: what is [TARGET] saying,
being said about, and signaling in public right now.

## When NOT to Use:
- You need the full competitor set mapped: run the landscape scan
  or competitive snapshot first.
- You need review-level depth on customer pain: that is the VoC
  miner's job; this sweep only flags the clusters.
- You already ran this recently: run competitive-intel-watch to
  diff instead of re-collecting.

## Required Context Keys:
1. The [TARGET] company
2. The [DECISION] this collection will feed
3. The [MARKET] and [BUYER] (drives which reviews, events, and
   analysts matter)

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company, and in which market?"
2. "What decision should this collection feed?"
3. "Who signs the check — which review sites and events does that
   buyer actually read and attend?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show a 3-bullet search plan first: source sweep order, date
   window, and how signals will be separated from noise. Continue
   unless revised.
2. Sweep in this order: newsroom and press output, analyst
   coverage and briefing chatter, exec and company social posts,
   review-site clusters for the [BUYER]'s sites, conference and
   webinar footprint, prediction markets where a regulation or
   milestone gates [MARKET].
3. Log every signal in the Signal Inventory: what was observed,
   source URL with date, Fact / Inference / Assumption label, the
   inference chain it supports, and the artifact it feeds.
4. Run the compendium's OSINT inference chains explicitly: exec
   posting on a new problem space = positioning pivot forming;
   sponsor-tier jump = market entry or doubling down; review
   complaints clustering = their roadmap pressure point; webinar
   topic shifts = what they will sell next; sudden silence on a
   product line = sunset in progress; prediction-market moves =
   crowd-priced expectations, check liquidity first.
5. Distinguish what [TARGET] says from what customers and analysts
   say about them — the gap between the two is positioning intel.
6. Announcements are intent, not commitment: flag any signal that
   needs FININT, HUMINT, or MASINT corroboration before anyone
   acts on it.
7. Keep the schema stable so run N and N+1 are diffable; if a
   prior sweep is in session, lead with the delta.

## Pedagogic Notes:
- Sweeping in a fixed source order builds collection discipline:
  coverage you can defend beats whatever the feed served today.
- The say/said-about gap teaches positioning analysis: a company's
  words minus its customers' words equals its exposed flank.
- Flagging intent-only signals for corroboration teaches the
  difference between watching a company talk and watching it
  commit.

## Attribution:
Created by Dean Peters (Productside.com). Collection doctrine from
the Competitive Research Compendium in this directory's reference/
shelf, OSINT discipline.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 16, 2026
-->

## Purpose

Sweep the public record on one company and land every signal in a
fusion-ready inventory.
Workflow: **search plan -> ordered source sweep -> signal inventory
-> inference chains -> gaps and handoffs.**

## Mode

**Just Enough Mode**: strongest signals only, max 5 inference
chains, one-line watch items. **Verbose Mode** only if asked.

This is a collection prompt: it gathers and labels; it does not
verdict. Confidence rating across disciplines belongs to
[all-source-fusion-prompt.md](all-source-fusion-prompt.md).

## Before You Start

Ask at most 3 questions:

1. Which company, and in which market?
2. What decision should this collection feed?
3. Which review sites and events does the buyer actually use?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: sweep order (press -> analysts -> social
-> reviews -> events -> prediction markets), the date window, and
the noise filter. Continue unless revised.

## Source + Trust Rules

Real, checkable URLs with dates on every signal. Do not invent
**press quotes, analyst ratings, review counts, event sponsorships,
or market odds.** Label every signal: **Fact** / **Inference** /
**Assumption**. What [TARGET] says about itself is a claim, not a
fact about the market. Announcements are intent until another
discipline corroborates.

# OSINT Collection: [TARGET]

**As-of date:** | **Decision supported:** | **Prior sweep:** [date
or "first run"]

## 1. Signal Inventory (fusion-ready)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [What it implies] | [Battle card / Positioning / ...] |

## 2. Strongest Inference Chains (max 5, ranked)

- [Signal cluster] -> [inference, labeled] -> [artifact it should
  change, and the move]

## 3. Say vs Said-About Gap

- **They say:** [their positioning language, sourced]
- **Customers and analysts say:** [the outside view, sourced]
- **The gap:** [labeled Inference — this is positioning ammo]

## 4. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 5. Collection Gaps and Handoffs

- [Uncovered source type] — [why it was out of reach this run]
- Deep dives: review clusters -> voice-of-customer-miner; whole
  market -> market-landscape-scan; next run -> competitive-intel-
  watch diffs this inventory

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Feed this inventory into all-source fusion with the other
   disciplines
2. Hand the review clusters to the voice-of-customer miner for
   depth
3. Turn the say/said-about gap into battle card or positioning
   updates
4. Schedule-ready version: save as the baseline the next sweep
   diffs against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
