# earnings-executive-signal-refresh-prompt.md
<!--
## Description:
Quarterly refresh of a company's executive and strategy signals:
parses the latest earnings call, filings, executive interviews, and
announcements, then diffs against a prior Executive Insights Company
Profile — reporting what shifted in strategy, product direction, and
leadership narrative. The schedulable sibling of the executive
insights profile.

## Usage Note:
Run prompts/company-profile-executive-insights-research.md once to
create the baseline profile, then run this each quarter (or after a
major event) with the prior profile in session. Works for public
companies (earnings calls, filings) and, with reduced signal, for
private companies (interviews, blogs, announcements).
Companion: market-intelligence/competitive-intel-watch-prompt.md covers
the whole competitor set at lower depth; this goes deep on one
company.

## When NOT to Use:
- No baseline profile exists: create one first (or this run becomes
  the baseline).
- You need the full landscape, not one company: use the competitive
  watch or landscape scan.

## Required Context Keys:
1. The company being tracked
2. Prior Executive Insights profile (pasted or attached)
3. The decision this tracking supports

## Missing Context Rule:
Ask at most 2 questions:
1. "Do you have the prior profile to paste, or should I create the
   baseline?"
2. "What decision does tracking this company support?"
If unanswered, proceed: baseline mode without a profile, labeled
assumptions otherwise.

## Instructions:
1. Read the prior profile fully; diff against it, do not regenerate
   it.
2. Show the search plan (3 bullets) before researching; continue
   unless revised.
3. Prioritize primary sources: earnings transcripts, filings, direct
   executive quotes with dates. Quote exactly; never fabricate
   quotes, numbers, or guidance.
4. Report shifts, not state: new strategic language, dropped
   initiatives, changed metrics emphasis, leadership moves, product
   signals. "No material shift" is a valid result.
5. Label key points Fact, Inference, or Assumption; URL and date per
   signal.
6. Just Enough Mode by default.

## Pedagogic Notes:
- Diffing executive language quarter over quarter teaches that what
  leaders STOP saying is often the strongest signal.
- Separating narrative shifts from metric shifts trains PMs to read
  earnings materials as strategy documents, not finance rituals.

## Attribution:
Created by Dean Peters (Productside.com). Extends the Executive
Insights Company Profile.

## Licensing:
MIT License

Date: July 3, 2026
-->

## Purpose

Refresh executive and strategy intelligence on one company by
diffing the latest quarter's signals against the prior profile.
Workflow: **search plan -> primary-source sweep -> diff -> shifted
signals -> so what -> next-step options.**

## Mode

Baseline mode: no prior profile provided — produce the Executive
Insights Company Profile and stop; delta value begins next run.
Delta mode (default with a profile): diff and report shifts only.

## Before You Start

Ask at most 2 questions:

1. Prior profile to paste, or create the baseline?
2. What decision does tracking this company support?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: which primary sources (earnings call,
filings, interviews, announcements), the period covered, and how
facts will be separated from inference. Continue unless revised.

## Source + Trust Rules

Primary sources first: earnings transcripts, 10-K/10-Q or local
equivalents, investor days, direct executive interviews, official
announcements. Real URLs and dates. Quote executives exactly.
Do not invent **quotes, financial figures, guidance, product claims,
or org changes.**
Label: **Fact**, **Inference**, **Assumption**.

# Executive Signal Refresh

## 1. Run Header

**Company:**
**Prior profile date:**
**Period covered this run:**
**Decision supported:**

## 2. Shifted Signals

For each material shift:

### [4 to 8 word shift summary]
- **Then:** [what the prior profile recorded]
- **Now:** ["exact quote or signal" — source, date, URL]
- **Reading:** [Inference — what this suggests for strategy or
  product]
- **Confidence:** [high / medium / low]

Cover, where evidence exists: strategic narrative; product and
portfolio emphasis; metrics leadership highlights; transformation
initiatives; leadership and org moves; competitive posture.

If nothing shifted materially: say so, and note the quiet as its
own signal if sustained.

## 3. Dropped Language

- [Initiatives, phrases, or metrics the company stopped mentioning —
  often the strongest tell; labeled Inference]

## 4. So What?

- **3** product or competitive implications for the supported
  decision
- **2** signals to watch next quarter
- **3** assumptions to validate

Each bullet: label, confidence, URL where relevant.

## Final Step

Offer exactly 4 options:

1. Update the full Executive Insights profile (new baseline)
2. Deep-dive the most significant shift
3. Feed the shifts into the competitive watch or battle card
4. Draft a one-paragraph briefing for leadership

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
