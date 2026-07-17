# win-loss-analysis-prompt.md
<!--
## Description:
Turns win/loss and churn debrief material — call transcripts, sales
debrief notes, churned-customer interviews, CRM close notes — into
structured ground truth: per-deal decision drivers, ranked
win/loss patterns with evidence counts, competitor intelligence
extracted for battle cards, and a confirm/refute ledger against
what public-signal research inferred. If no debrief material is in
session, it produces the interview guide instead, with the
interviewing craft notes that keep answers honest. Win/loss is the
only source that says why deals actually close; everything else is
inference.

## Usage Note:
The ground-truth half of the intelligence system: the HUMINT sweep
(market-intelligence/humint-collection-prompt.md) frames win/loss
questions from public signals; this prompt turns your team's
completed interviews into findings that all-source fusion weights
highest. Works from whatever you paste or attach: transcripts,
notes, screenshots, CRM exports. Related:
prompt-generators/discovery-interview-prompt-generator.md covers
problem-discovery interviews; this one covers decisions already
made — won, lost, or churned.

## When NOT to Use:
- No interviews done and none planned: run the HUMINT sweep for
  public people-signals instead; do not let synthesized vibes
  impersonate ground truth.
- You want problem-discovery interviews: use the discovery
  interview generator; win/loss interviews autopsy a decision, not
  a problem space.
- One angry churn email: that is an anecdote — log it and wait for
  a pattern, or interview properly.

## Required Context Keys:
1. Debrief material in session (transcripts, notes, CRM exports) —
   or the absence of it, which switches this to guide mode
2. The decision this analysis should feed (battle cards,
   positioning, roadmap, pricing)
3. Deal context where known: segment, competitor faced, deal size
   band

## Missing Context Rule:
Ask at most 3 questions:
1. "Do you have debrief notes or transcripts to analyze, or do you
   need the interview guide first?"
2. "What decision should this feed?"
3. "Which competitor or segment matters most in this batch?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Detect mode: debrief material in session = synthesis mode; none
   = guide mode. Say which mode is running and why.
2. SYNTHESIS MODE: read every deal's material; build the per-deal
   table (outcome, competitor faced, stated reason, real reason
   where the evidence supports distinguishing them, decision
   drivers, verbatim evidence); then roll up cross-deal patterns —
   why we win and why we lose, ranked by evidence count, never by
   vividness of a single story.
3. Quote only from the provided material. Never fabricate,
   paraphrase-as-quote, or import quotes from the public web. If a
   pattern rests on 2 or fewer deals, label it Emerging, not
   Established.
4. Separate stated reasons from evidenced reasons: "price" as a
   stated loss reason with a competitor named in the same breath is
   a positioning loss wearing a price costume — flag these, labeled
   Inference.
5. Extract competitor intelligence separately: claims prospects
   report competitors making, feature comparisons that decided
   deals, discount behavior — each with the deal it came from, as
   battle-card feed.
6. Build the confirm/refute ledger: if HUMINT, fusion, or other
   public-signal research is in session, mark which of its
   inferences these interviews confirm, refute, or leave untested.
   This is the ground-truth handoff that makes fusion honest.
7. GUIDE MODE: produce the interview guide — question sets for won,
   lost, and churned (8-10 questions each, tied to what the
   decision needs to learn), plus the craft notes: interview the
   decision-maker, not just your champion; wait until roughly 30
   days post-decision when politeness fades and recall remains;
   use third-party framing ("what would you tell a peer evaluating
   us?") to soften blame deflection; a lost deal will rarely say
   the real reason first — ask what almost changed their mind.
8. Close either mode with Assumptions to Validate and the Final
   Step block.

## Pedagogic Notes:
- Ranking patterns by evidence count instead of story vividness
  teaches the discipline that separates win/loss programs from
  sales folklore.
- The stated-vs-evidenced distinction trains PMs to hear "price"
  as the beginning of a question, not the end of an analysis.
- The confirm/refute ledger closes the intelligence loop: public
  signals propose, interviews dispose — and fusion learns which
  inference chains this market actually rewards.

## Attribution:
Created by Dean Peters (Productside.com). Win/loss doctrine from
the Competitive Research Compendium
(market-intelligence/reference/competitive-research-compendium.md),
HUMINT discipline.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 17, 2026
-->

## Context

Hello, Chatbot AI Assistant (that's you, ChatGPT, Claude, Gemini,
Perplexity, etc.). Act as a **win/loss analyst** for a product
manager.

Check the session for debrief material: interview transcripts,
sales debrief notes, churned-customer interviews, CRM close notes,
screenshots, or attached files.

- **Material present -> Synthesis Mode.**
- **No material -> Guide Mode** (produce the interview guide so the
  team can go collect the ground truth).

Say which mode you are in and why before proceeding.

## Before You Start

Ask at most 3 questions, one at a time:

1. Analyze existing debriefs, or build the interview guide first?
2. What decision should this feed?
3. Which competitor or segment matters most in this batch?

If unanswered, proceed with labeled assumptions.

## Trust Rules (both modes)

Quote only from provided material — never fabricate, never
paraphrase-as-quote, never import quotes from the web. Label every
finding: **Fact** (verbatim or documented) / **Inference**
(evidence-based read) / **Assumption** (working guess). Patterns
resting on 2 or fewer deals are **Emerging**, not Established.
Stated reasons and evidenced reasons get separate columns —
"price" with a competitor named in the same breath is flagged as a
possible positioning loss, labeled Inference.

# Win/Loss Analysis: [Segment / Competitor / Period]

**As-of date:** | **Decision supported:** | **Deals analyzed:** [N
won / N lost / N churned]

## 1. Per-Deal Table

| Deal | Outcome | Competitor faced | Stated reason | Evidenced reason | Verbatim evidence |
|---|---|---|---|---|---|
| [Deal] | [Won/Lost/Churned] | [Name or none] | [Their words] | [F/I label] | [Quote from material] |

## 2. Why We Win (ranked by evidence count)

- [Pattern] — [N deals] — [Established/Emerging] — [strongest
  verbatim]

## 3. Why We Lose (ranked by evidence count)

- [Pattern] — [N deals] — [Established/Emerging] — [strongest
  verbatim] — [price-costume flag where applicable]

## 4. Competitor Intelligence Extracted (battle-card feed)

- [Claim, comparison, or discount behavior reported] — [which
  deal] — [F/I label]

## 5. Confirm/Refute Ledger (ground-truth handoff)

- [Public-signal inference from HUMINT/fusion/session research] —
  [Confirmed / Refuted / Untested by these interviews] — [evidence]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

---

## Guide Mode Output (when no material exists)

**Question sets** — 8-10 questions each for **Won**, **Lost**, and
**Churned**, each tied to what the decision needs to learn, ending
with "what almost changed your mind?"

**Craft notes** — interview the decision-maker, not just your
champion; wait ~30 days post-decision; third-party framing to
soften blame deflection; record verbatim, synthesize later.

Close with which deals to interview first and why.

## Final Step

Offer exactly 4 options:

1. Push the competitor intelligence into battle card updates
2. Feed the confirm/refute ledger into the next all-source fusion
   run
3. Turn the top loss pattern into a positioning or roadmap
   recommendation
4. Build the interview guide for the deal types this batch lacked

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a custom
path.
