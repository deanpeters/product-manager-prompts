# all-source-fusion-prompt.md
<!--
## Description:
Fuses signals collected across independent intelligence disciplines
(OSINT, FININT, GEOINT/DEMOINT, TECHINT, HUMINT, SIGINT, MASINT)
into confidence-rated stories about a competitor's next move. Runs
the confidence-stacking rule — one discipline is a watch item, two
is a working hypothesis, three or more is actionable intelligence,
conflict means someone is bluffing — and ends with recommended
responses mapped to the PM artifacts each story should change.

## Usage Note:
This is the situation room, not a collection prompt. It works best
when the session already holds outputs from this directory's other
investigations (snapshot, intel watch, pricing tracker, earnings
refresh, VoC miner, PESTEL delta) — fusion then synthesizes instead
of re-searching. You can also bulk-drop findings gathered elsewhere.
Doctrine: reference/competitive-research-compendium.md, especially
the All-Source Fusion discipline and the fusion cadence.

## When NOT to Use:
- You have signals from only one discipline: that is a watch item,
  not a fusion run. Collect more channels first.
- You need fresh fieldwork: run the collection prompts in this
  directory, then fuse their outputs here.
- You want a single framework read (SWOT, five forces): those
  prompts consume fused evidence; this one produces it.

## Required Context Keys:
1. The [TARGET] company (or the market, if fusing landscape-wide)
2. The [DECISION] this fusion brief will change
3. The signals to fuse: session research, pasted findings, or both
4. Optional: the [CAPABILITY] or move you already suspect

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company or market is this fusion about?"
2. "What decision should this brief change?"
3. "What signals do I have — session research, a paste, or should
   I inventory what is in this conversation?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Inventory every signal available: session outputs from other
   investigations, pasted findings, documents provided. Tag each
   with its discipline, source URL, date, and a Fact / Inference /
   Assumption label. Do not collect new evidence unless a targeted
   gap-fill is approved.
2. Apply the independence test before stacking: two signals citing
   the same underlying source (a press release and its coverage)
   count as ONE discipline. Corroboration requires independent
   channels.
3. Cluster signals into candidate stories — hypotheses about what
   [TARGET] is doing. Name each story as a capability or move, not
   a vibe.
4. Rate each story with the confidence-stacking rule: 1 discipline
   = watch item, log it; 2 = working hypothesis, assign a probe;
   3+ = actionable intelligence, brief leadership; disciplines in
   conflict = the most interesting case, dig.
5. Apply the ambition-vs-commitment corollary: announcements are
   intent until funding, procurement, land, permits, hiring, or
   contracts corroborate them. An OSINT-only story cannot rate
   above working hypothesis.
6. Never average conflicting signals into a middle verdict. A
   conflict is a finding: name what each side implies and what
   evidence would settle it.
7. For each actionable story, name the response: which PM artifact
   changes (battle card, roadmap bet, pricing, positioning, TAM),
   and what the field or leadership should do before the move
   lands, not after.
8. Close with collection gaps: disciplines contributing zero
   signals, and which prompt in this directory would fill each.
9. Keep the output schema stable so run N and run N+1 are diffable;
   if a prior fusion brief is in session, lead with the delta.

## Pedagogic Notes:
- Confidence stacking teaches the discipline most competitive
  decks lack: separating what you can act on from what you merely
  noticed. One anecdote is not intelligence.
- The independence test builds source-criticism habit — PMs learn
  to ask "is this corroboration, or the same press release wearing
  three hats?"
- The ambition-vs-commitment corollary transfers intelligence
  tradecraft to roadmap defense: intent is cheap, committed
  resources are not.
- Ending on artifact-mapped responses keeps fusion from becoming
  competitive trivia: every story must change a decision or it is
  a watch item.

## Attribution:
Created by Dean Peters (Productside.com). Fusion doctrine from the
Competitive Research Compendium in this directory's reference/
shelf; confidence stacking after intelligence-community all-source
analysis practice.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 16, 2026
-->

## Purpose

Fuse multi-discipline signals into confidence-rated stories and
artifact-mapped responses.
Workflow: **inventory signals -> independence test -> cluster into
stories -> stack confidence -> verdicts, responses, gaps.**

## Mode

**Just Enough Mode**: max 5 stories per run, strongest first; watch
items as one-line log entries. **Verbose Mode** only if asked.

This prompt fuses; it does not collect. If the session holds outputs
from the seven discipline collection sweeps (osint-, finint-,
geoint-demoint-, techint-, humint-, sigint-, masint-collection) or
the deep-dive investigations (snapshot, intel watch, pricing
tracker, earnings refresh, VoC miner, PESTEL delta), those are the
evidence base. Otherwise ask for a paste — or recommend which
collection sweeps to run first.

## Before You Start

Ask at most 3 questions:

1. Which company or market is this fusion about?
2. What decision should this brief change?
3. What signals do I have — session research, a paste, or should I
   inventory this conversation?

If unanswered, proceed with labeled assumptions.

## Gap-Fill Rule (when collection is thin)

If 2 or fewer disciplines have signals, say so and offer a targeted
gap-fill: a **3-bullet search plan** naming which disciplines will
be swept and where. Continue only if approved — otherwise fuse what
exists and rate accordingly.

## Source + Trust Rules

Real, checkable URLs with dates on every signal. Do not invent
**signals, sources, filings, patent counts, hiring numbers, or
supply-chain data** — a fusion brief built on invented signals is
disinformation with a confidence score. Label every signal and
every story verdict: **Fact** / **Inference** / **Assumption**.
Same-source signals collapse to one discipline. Announcements are
intent until FININT, MASINT, or HUMINT corroborate.

# All-Source Fusion Brief: [TARGET / Market]

**As-of date:** | **Decision supported:** | **Prior brief:** [date
or "first run"]

## 1. Signal Inventory

| Signal | Discipline | Source (URL, date) | Label |
|---|---|---|---|
| [What was observed] | [OSINT..MASINT] | [URL, date] | [F/I/A] |

[Same-source duplicates collapsed and noted]

## 2. Fusion Stories (max 5, ranked by confidence then impact)

### Story: [TARGET]'s [capability / move]

- **Disciplines in agreement:** [count and names]
- **The story:** [2-3 sentences: what the signals say together,
  labeled Inference]
- **Verdict:** [Watch item / Working hypothesis / Actionable
  intelligence] — [why, including independence check]
- **Commitment check:** [intent only, or corroborated by funding /
  procurement / hiring / permits / contracts?]
- **Response:** [which artifact changes — battle card, roadmap bet,
  pricing, positioning, TAM — and the move to make before their
  launch, not after]

## 3. Conflicts (someone is bluffing)

- [Signal A implies X; signal B implies not-X] — [what each side
  would mean] — [the evidence that settles it, and where to look]

## 4. Watch Items (single-discipline flags, logged only)

- [Signal] — [discipline] — [what would escalate it to hypothesis]

## 5. Collection Gaps

- [Discipline with zero signals] — [which collection sweep fills
  it: osint-, finint-, geoint-demoint-, techint-, humint-, sigint-,
  or masint-collection — with the deep dives (snapshot, intel
  watch, pricing tracker, earnings refresh, VoC miner, PESTEL
  delta) where depth beats breadth]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Turn the top actionable story into a leadership brief or battle
   card update
2. Run the collection prompt that fills the biggest gap, then
   re-fuse
3. Build the probe plan for the conflicts and working hypotheses
4. Schedule-ready version: save this brief as the baseline the next
   quarterly fusion diffs against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
