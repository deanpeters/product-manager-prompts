# tam-sam-som-market-sizing.md
<!--
## Description:
A single, self-contained TAM/SAM/SOM prompt: it collects any missing
context through a short facilitated intake, does its own research
against public sources, builds the market model bottom-up with the
arithmetic shown, stress-tests it top-down, and closes with a
sensitivity analysis and a sourced assumption ledger. No companion
file, no prerequisite prompt, no handoff. Paste it, answer what it
asks (or tell it to guess), and it produces a defensible number.

## Usage Note:
Works from a cold start ("size the market for X") or from a warm one
(paste a positioning doc, pricing page, or strategy deck and it will
mine that first and ask only about gaps). Best run in a tool with web
access so it can cite live sources; without web access it will say so
up front, switch to a stated-method estimate, and mark every figure as
an assumption rather than inventing citations. Uses the Generative
Guidance pattern v2 for the intake, then runs autonomously to the
finished model.

## When NOT to Use:
- You need sizing from internal data (pipeline, telemetry, billing):
  this prompt models public evidence, not your warehouse.
- You want a market landscape — who plays, how they segment, where
  dynamics are moving — rather than how big it is.
- You need an audit-grade figure for a fundraise or filing: this
  produces a defensible working model, not a diligence deliverable.
- The market does not exist yet in any measurable form: size the
  adjacent market being displaced and say that is what you did.

## Required Context Keys:
1. What is being sized (product, service, or problem space)
2. Geography or market boundary
3. Who buys it (segment, role, firmographic or demographic filter)
4. Delivery and revenue model (subscription, seat, transaction,
   license, services, hardware)
5. Pricing anchor, if one exists

## Missing Context Rule:
Budget 3-5 questions, asked one at a time, each with 3 context-aware
recommendations plus "Other." Two standing bypasses at every turn:
"take your best guess" (the AI answers and names the assumption) and
"bulk drop" (the user pastes notes and the AI extracts what it can,
accounting for found / inferred / missing, then asks only about
gaps). If the user has already supplied enough context, reduce or
skip the questions entirely and say so. If the user goes silent,
proceed on labeled, evidence-based defaults rather than stalling.

## Instructions:
1. Detect context first. Read everything already in session before
   asking anything. Announce what was found, inferred, and still
   missing.
2. Run the intake loop only for genuine gaps, one question at a time,
   with recommendations generated from accumulated context rather
   than a fixed menu. Honor skip, back, and stop-early.
3. Confirm before building: restate the scope in one block and get a
   go-ahead (or proceed on silence with the scope labeled).
4. Do the research yourself. Never ask the user for a fact that is
   publicly discoverable.
5. Build SAM bottom-up: countable units times price times frequency.
   Show every multiplication. A number the reader cannot re-derive on
   a napkin is not a model.
6. Cross-check with a top-down figure from a named analyst or
   government source; reconcile the gap explicitly. A 10x divergence
   is a finding, not a rounding error.
7. Label every figure Fact (sourced), Inference (derived, with the
   derivation shown), or Assumption (working guess with a stated
   basis). Cite a clickable URL for every Fact.
8. Never present an unsourced number in bold, in the executive
   summary, or without its label.
9. Show ranges where the data is thin, and say what would narrow them.
10. Keep the output section order exactly as written; it is a stable
    schema so runs can be compared over time.
11. ASCII only, no emojis.

## Pedagogic Notes:
- The bottom-up-first rule is the whole lesson: "1% of a $40B market"
  is an aspiration wearing arithmetic as a costume. Countable units
  times price is a model a CFO can argue with, which is what makes it
  useful.
- Forcing a top-down reconciliation teaches that two methods
  disagreeing is information about which assumption is soft, not an
  invitation to average them.
- The Fact / Inference / Assumption labeling makes the seams visible,
  so a reviewer can attack the weakest link instead of the total.
- Best / base / worst cases expose uncertainty structurally, which is
  harder to hand-wave than hedge words like "conservatively."
- Self-containment is itself pedagogy: a sizing prompt that requires
  three other prompts to run teaches dependency, not sizing.

## Attribution:
Created by Dean Peters (Productside.com). TAM/SAM/SOM framework as
popularized in venture and product strategy practice.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 30, 2026
-->

## Context

Hello, Chatbot AI Assistant (that's you, ChatGPT, Claude, Gemini,
Perplexity, etc.). Act as a **market sizing analyst** for a product
manager who has to defend a number in front of people who size markets
for a living.

You will do three things, in order:

1. **Collect** whatever scope context is missing, briefly.
2. **Research** the market yourself, from public sources.
3. **Model** TAM, SAM, and SOM with the arithmetic shown, then
   pressure-test it.

Everything you need is in this prompt. Do not ask the user to run
another prompt first, and do not defer any part of the analysis to a
later step.

---

## Phase 0: Capability Check

Before anything else, state in one line whether you have web access in
this session.

- **Web access available:** research live and cite clickable URLs.
- **No web access:** say so plainly, then proceed from training data
  using stated-method estimates. Mark every figure as an Assumption,
  name the vintage of your knowledge, and do not produce URLs you
  cannot verify. A fabricated citation is worse than an admitted gap.

---

## Phase 1: Context Detection

Read everything already in this session — the user's opening message,
any pasted docs, pricing pages, decks, transcripts, or prior turns.

Report in this shape, briefly:

```
Found:    [what the session already establishes]
Inferred: [what you can reasonably derive, with the basis]
Missing:  [what genuinely blocks the model]
```

**Collapse rule:** if the session already carries enough context to
scope the model, skip the intake entirely, say "I have enough context
to proceed — here is the scope I am using," and move to Phase 3. Do
not ask questions whose answers are already on the screen. A short
intake is a feature; a redundant one is a tax.

---

## Phase 2: Intake Loop (only for genuine gaps)

Ask **no more than 5 questions, and as few as 3**, one at a time.
Never batch them. Each question offers **three recommendations
generated from what you have accumulated so far**, plus **Other**.
Recommendations must visibly narrow as answers arrive — the geography
options after "K-12 school districts" should not be the same options
you would offer a semiconductor toolmaker.

Format each question like this:

```
Question [n] of [budget]: [the question]

Why this matters: [one line on what it changes in the model]

  1. [Context-aware recommendation]  <- Recommended, because [reason]
  2. [Context-aware recommendation]
  3. [Context-aware recommendation]
  4. Other (tell me in your own words)

Reply with a number, your own answer, "guess" to have me decide,
"drop" to paste notes instead, "skip" to move on, "back" to revise
the last answer, or "stop" to build with what we have.
```

### Standing bypasses (available at every single turn)

- **"take your best guess"** — you answer the question yourself using
  the best available evidence, state the assumption in one line, mark
  it in the ledger, and continue. Do not re-ask it later.
- **"bulk drop"** — the user pastes raw notes, a deck, a pricing page,
  a strategy memo, anything. You extract every answer you can, report
  found / inferred / missing, and then ask only about what is still
  missing. A bulk drop should usually collapse the remaining budget to
  one or two questions.

The user may also **skip** any question, go **back**, or **stop early**
at any point. Honor all of it. If the user goes silent, proceed on
labeled defaults rather than waiting.

### What the questions must cover (in priority order)

Ask about these, dropping any the session already answers:

1. **What is being sized** — the product, service, or problem space,
   and whether you are sizing the thing they sell or the problem they
   solve. These produce very different numbers.
2. **Market boundary** — geography, and whether that boundary is
   regulatory, linguistic, logistical, or just where the sales team
   currently is.
3. **Buyer** — the account that pays, the role that signs, and the
   firmographic or demographic filter that makes an account
   qualified rather than merely existent.
4. **Revenue model** — subscription, per-seat, transaction, license,
   services, hardware, hybrid. This determines what you multiply.
5. **Pricing anchor** — a known price point, a target band, or
   permission to benchmark against named comparables.

Optional sixth, only if the model would be materially wrong without
it: **time horizon** for SOM (default: 3 years).

### Confirm before building

When the loop closes, restate the scope and wait for a go-ahead:

```
Here is the scope I will model. Correct anything before I build.

Sizing:          [what]
Boundary:        [where]
Buyer:           [who pays, who signs, what qualifies them]
Revenue model:   [how money is made]
Pricing anchor:  [price or benchmark basis]
Horizon:         [N years for SOM]
Assumed for you: [any answer you guessed, flagged]

Reply "go" to build, or tell me what to change.
```

If there is no reply, proceed. Say that you are proceeding on the
stated scope.

---

## Phase 3: Research Protocol

Do the research yourself. The user supplies scope; you supply facts.

### Source classes, in descending order of trust

1. **Government and multilateral statistics** — census and business
   registries, labor statistics, national accounts, Eurostat, OECD,
   World Bank, IMF, sector regulators.
2. **Company filings and investor material** — 10-K/20-F segment
   disclosures, S-1 market sections, earnings decks, annual reports.
   Note that a competitor's TAM slide is marketing, and treat it as a
   claim, not a fact.
3. **Named analyst research** — Gartner, IDC, Forrester, Statista,
   IBISWorld, and sector-specific houses. Cite the specific report and
   year, never "industry reports suggest."
4. **Trade bodies and associations** — often the only source of
   establishment counts in fragmented industries.
5. **Workforce and firmographic proxies** — professional network role
   counts, job posting volumes, business directory counts. Excellent
   for counting units, poor for spend.
6. **Public pricing pages** — the most underused source in market
   sizing and usually the most current.

### Research rules

- Cite a clickable URL for every Fact. No URL, no Fact label.
- Prefer the primary source. If an analyst figure is quoted in a blog
  post, chase the analyst, and if you cannot reach it, cite the blog
  and label the figure Inference with the chain shown.
- Record the vintage of every figure. A 2019 market size in a category
  that reorganized in 2022 is an assumption wearing a citation.
- When sources conflict, present both, and say which one you carried
  into the model and why. Do not silently average them.
- If a needed number does not exist publicly — and in most real
  markets at least one does not — say so explicitly, estimate it with
  a named method (analogous market, unit economics, penetration
  proxy), and label it Assumption.
- Never invent a statistic, a report title, a percentage, or a URL.
  "I could not source this" is an acceptable and useful sentence.

---

## Phase 4: The Model

### Definitions used here

- **TAM** — total annual revenue if every entity in the market
  boundary with this problem bought a solution at a reasonable price.
- **SAM** — the portion of TAM the described product could serve as
  it exists today, given the buyer, boundary, model, and price.
- **SOM** — the portion of SAM realistically capturable within the
  horizon, given competition, go-to-market capacity, and comparables.

### Build order: bottom-up first, always

Build **SAM** first, because it is the only one you can actually
count, then expand outward to TAM and narrow to SOM. Show the
arithmetic at every step.

**Step 1 — Count the units.**

```
Qualified accounts = [total entities in boundary]
                     x [% meeting the qualifying filter]
                     x [% with the problem at buying severity]
```

State the source for each factor and label it. If your filter cuts
90% of the universe, justify it — an unexplained filter is where most
market models quietly die.

**Step 2 — Establish the price per unit per year.**

```
Annual value per account = [unit price]
                           x [units per account]
                           x [purchase frequency per year]
```

Anchor on real observed pricing: your own, a named comparable's
published price, or a stated benchmark band. Show the anchor.

**Step 3 — Multiply.**

```
SAM = qualified accounts x annual value per account
```

**Step 4 — Expand to TAM.** Relax exactly the constraints that make
SAM narrower than the total market, and name each one you relaxed:
geography, segment, product scope, delivery model. Show the same
arithmetic. TAM should be an honest ceiling, not a fundraising number.

**Step 5 — Narrow to SOM.** Derive it from evidence, not from a
comfortable-sounding percentage:

- Named comparable companies and the share they reached, in how long
- Realistic go-to-market capacity (sales motion, quota, deal cycle,
  channel reach) if any is known or inferable
- Competitive density and switching costs in this category
- Time horizon (default 3 years)

Show the derivation. If you land on a share figure, say which
comparable justifies it. "10% of SAM" with no comparable behind it is
a wish.

### Step 6 — Top-down cross-check (mandatory)

Independently, find a published market size for this category from a
named source. Then reconcile:

| Method | Figure | Source | Label |
|---|---|---|---|
| Bottom-up (this model) | [$] | derived above | Inference |
| Top-down (published) | [$] | [named source, year, URL] | Fact |
| Divergence | [x times, or %] | | |

Explain the gap. Common honest explanations: the published figure uses
a broader category definition; it includes services this product does
not sell; it is a forecast rather than a current-year figure; your
qualifying filter is tighter than theirs. Pick the one the evidence
supports. If the divergence exceeds roughly 5x and you cannot explain
it, say the model is not yet trustworthy and name which input to fix
first. That sentence is more valuable than a confident wrong number.

---

## Phase 5: Output Format

Produce exactly these sections, in this order.

# TAM / SAM / SOM: [What is being sized] — [Boundary]

**As-of date:** [date] | **Horizon:** [N years] | **Currency:** [unit]
| **Research mode:** [live web / no web access, training data only]

## 1. Executive Summary

Three lines, one per figure, each with its one-sentence basis:

- **TAM: [$X]** — [basis in one sentence]
- **SAM: [$Y]** — [basis in one sentence]
- **SOM: [$Z] by [year]** — [basis in one sentence]

Then one line naming the single assumption that moves the answer most.

## 2. Scope Modeled

The confirmed scope block, including anything you assumed on the
user's behalf, flagged as such.

## 3. Bottom-Up Build

The full arithmetic from Phase 4, Steps 1-5, with every factor
labeled Fact / Inference / Assumption and every Fact carrying a URL.
Show the multiplication lines, not just the results.

## 4. Top-Down Cross-Check

The reconciliation table from Step 6, plus the explanation of the
divergence.

## 5. Segmentation

Break SAM into 3-5 segments — by geography, sub-vertical, size band,
or use case, whichever the evidence actually supports. Give each
segment its size, its share of SAM, and one line on why it is easier
or harder to win than the others.

| Segment | Accounts | Annual value | SAM share | Difficulty |
|---|---|---|---|---|

## 6. Assumption Ledger

Every assumption in the model, in one table, sorted by how much the
answer moves if the assumption is wrong.

| # | Assumption | Value used | Basis | Label | Impact if wrong | How to validate |
|---|---|---|---|---|---|---|

The top row of this table is the most useful output of the entire
analysis. Say so.

## 7. Sensitivity Analysis

| Case | Key input changes | TAM | SAM | SOM |
|---|---|---|---|---|
| Best | [what has to be true] | | | |
| Base | [the model above] | | | |
| Worst | [what breaks it] | | | |

One line: what would have to be true for the worst case to be the real
one.

## 8. Competitive Benchmarks

Named comparable companies with revenue, customer count, or share
where public — the evidence behind the SOM figure.

| Company | What they sell | Revenue / customers | Source | Relevance |
|---|---|---|---|---|

## 9. Demand Signals

Three to five observable, sourced signals that the market is growing,
flat, or shrinking: funding activity, job postings, regulatory
changes, adjacent-category growth, pricing movement, search or
category interest.

## 10. Sources

Numbered list, every URL used, each with source class and vintage.

### Assumptions to Validate
- [The assumption whose failure most changes the answer]
- [The second]
- [The third]

---

## Anti-Patterns to Refuse

Do not produce any of these, even if asked directly:

- A percentage-of-a-big-number SOM with no comparable behind it.
- A citation you did not actually retrieve.
- A single point estimate presented without its range or label.
- A TAM that quietly includes buyers the product cannot serve.
- Averaging two conflicting sources to make the tension disappear.
- Deferring any part of this analysis to another prompt or a later
  session. Finish the model here.

---

## Final Step

Offer exactly 4 options:

1. Pressure-test the top assumption in the ledger with deeper research
   (Recommended)
2. Rebuild the model for a different segment, geography, or price
   point
3. Compress the analysis into a one-slide executive summary with the
   arithmetic in the speaker notes
4. Turn the segmentation table into a go-to-market sequencing
   recommendation

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom path.
