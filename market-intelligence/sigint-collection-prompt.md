# sigint-collection-prompt.md
<!--
## Description:
Runs a SIGINT (Signals Intelligence) collection sweep on a target
company: website and pricing-page diffs, SEO/SEM moves, app-store
metadata shifts, new SSL certificates and subdomains, case-study
patterns, and webinar/event cadence. Every signal lands in a
fusion-ready inventory with a source URL, date, evidence label,
and the inference chain it supports. The wiretap you are allowed
to have: companies broadcast constantly through what they change
on the public internet; most competitors never listen.

## Usage Note:
One of seven discipline collection prompts feeding
all-source-fusion-prompt.md; doctrine in
reference/competitive-research-compendium.md (SIGINT discipline).
The freshest discipline on the collection floor — this is what
keeps battle cards from going stale, on a weekly cadence. For
scheduled diffing against a baseline hand off to
competitive-intel-watch-prompt.md; for the pricing time series,
pricing-packaging-tracker-prompt.md. This prompt owns the
discipline-wide sweep across all the broadcast channels at once.

## When NOT to Use:
- You want the governed weekly routine: run
  loops/fusion-cadence-routine.md or competitive-watch-routine.md;
  this is the manual sweep they schedule.
- You only need pricing history: the pricing-packaging tracker
  already owns that series.
- You need what has not shipped yet: TECHINT reads the 12-18 month
  fingerprints; SIGINT reads the launch staging.

## Required Context Keys:
1. The [TARGET] company and its primary web properties
2. The [DECISION] this collection will feed
3. A prior snapshot date, if any (turns the sweep into a diff)

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company, and which of their web properties matter most?"
2. "What decision should this collection feed?"
3. "Is there a prior snapshot to diff against, and from when?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show a 3-bullet search plan first: properties to diff, archive
   sources for the before-state, metadata sources. Continue unless
   revised.
2. Sweep in this order: website diffs against archived versions,
   pricing and packaging pages, SEO/SEM posture (including whether
   they bid on your brand terms), app-store version notes and
   metadata, certificate-transparency logs for new subdomains,
   case-study and customer-page patterns, webinar and event
   cadence.
3. Log every signal in the Signal Inventory: what was observed,
   the before/after where diffable, source URL with date, Fact /
   Inference / Assumption label, the inference chain it supports,
   and the artifact it feeds.
4. Run the compendium's SIGINT inference chains explicitly: a new
   subdomain certificate (capability.target.com) = launch staging,
   often weeks ahead; a pricing tier removed = packaging overhaul,
   usually toward enterprise; sudden SEM bidding on your brand
   terms = they consider you the threat now; case-study pattern
   shifts (new vertical or geography appearing) = segment push;
   visible messaging A/B tests across archive diffs = they are
   unsure of positioning — hit the wound.
5. Anchor every diff with both dates: what the page said before,
   what it says now, when each was captured. A change without a
   before-state is an observation, not a diff.
6. Mark launch-staging signals (certs, hidden pages, beta
   endpoints) for TECHINT and HUMINT cross-checks — staging plus
   patents plus hiring is a high-confidence fusion story.
7. Keep the schema stable so run N and N+1 are diffable; if a
   prior sweep is in session, lead with the delta.

## Pedagogic Notes:
- Diffing against archives instead of reading today's site teaches
  the core SIGINT insight: the change is the signal, not the
  content.
- Watching what a company tests (messaging A/B, pricing
  experiments) builds the habit of reading uncertainty as
  exploitable intel.
- The both-dates rule enforces evidentiary hygiene: a diff you
  cannot date is a story you cannot defend.

## Attribution:
Created by Dean Peters (Productside.com). Collection doctrine from
the Competitive Research Compendium in this directory's reference/
shelf, SIGINT discipline.

## Licensing:
MIT License

Date: July 16, 2026
-->

## Purpose

Listen to one company's public-internet broadcast and land every
signal in a fusion-ready inventory.
Workflow: **search plan -> diffs across properties and metadata ->
signal inventory -> inference chains -> launch-staging flags ->
gaps and handoffs.**

## Mode

**Just Enough Mode**: strongest signals only, max 5 inference
chains, one-line watch items. **Verbose Mode** only if asked.

This is a collection prompt: it gathers and labels; it does not
verdict. Confidence rating across disciplines belongs to
[all-source-fusion-prompt.md](all-source-fusion-prompt.md).

## Before You Start

Ask at most 3 questions:

1. Which company, and which web properties matter most?
2. What decision should this collection feed?
3. Prior snapshot to diff against, and from when?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: properties to diff, archive sources for
the before-state, metadata and certificate sources. Continue
unless revised.

## Source + Trust Rules

Real, checkable URLs with dates on every signal; diffs carry both
the before and after capture dates. Do not invent **page content,
prices, tiers, certificate records, app-store notes, ad placements,
or archive states.** Label every signal: **Fact** / **Inference** /
**Assumption**. Public observation only: no scraping in violation
of terms you agreed to, no authenticated or paywalled areas
presented as public record.

# SIGINT Collection: [TARGET]

**As-of date:** | **Decision supported:** | **Prior sweep:** [date
or "first run"]

## 1. Signal Inventory (fusion-ready)

| Signal | Before -> After | Source (URLs, dates) | Label | Inference chain | Feeds |
|---|---|---|---|---|---|
| [What changed] | [then -> now] | [URLs, both dates] | [F/I/A] | [What it implies] | [Battle card / Pricing / Positioning / ...] |

## 2. Strongest Inference Chains (max 5, ranked)

- [Signal cluster] -> [inference, labeled] -> [artifact it should
  change, and the move]

## 3. Launch-Staging Flags

- [Cert / subdomain / hidden page / beta signal] — [what it stages,
  labeled Inference] — [cross-check: TECHINT for the R&D trail,
  HUMINT for the hiring trail]

## 4. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 5. Collection Gaps and Handoffs

- [Property or channel not diffable this run] — [why]
- Deep dives: scheduled diffing -> competitive-intel-watch; price
  series -> pricing-packaging-tracker; weekly governance ->
  loops/fusion-cadence-routine

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Feed this inventory into all-source fusion with the other
   disciplines
2. Push the freshest shifts into battle card updates now
3. Run TECHINT and HUMINT cross-checks on the launch-staging flags
4. Schedule-ready version: save as the baseline the weekly SIGINT
   sweep diffs against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
