# Interaction Modes

This repository's prompts follow one of three interaction modes. The
modes differ on a single axis: **where the context comes from.** Pick the
mode by asking whose knowledge the deliverable depends on.

| Mode | Context source | Human's role | Exemplar |
|---|---|---|---|
| **Facilitation** (Generative Guidance) | The human | Answers narrowing questions | `workshops/battle-card-workshop.md` |
| **Checkpointed co-construction** | An artifact (template, case study, session material) | Gates each section | `workshops/prd-workshop.md` |
| **Autonomous investigation** | The world (search, data, published sources) | Optional; sets defaults, then reviews | `market-intelligence/tam-sam-som-analysis-prompt.md` |

A single prompt may blend modes — a facilitation that searches when its
options would be generic is borrowing from investigation; an
investigation that pauses at a confirmation gate is borrowing from
co-construction. But every prompt should declare one primary mode,
because the mode determines the defaults: who asks, who waits, and what
happens when nobody answers.

---

## Mode 1: Facilitation (Generative Guidance)

The human holds the context; the AI's job is to extract it with the
least burden. One question at a time, 3 context-aware recommendations
plus "Other," standing bypasses (best guess, bulk drop), loop control
(skip, go back, stop early), output withheld until the loop closes.

Full spec: `generative-guidance-pattern.md` (v2).

**Use when:** the deliverable depends on situational knowledge only the
user has — their product, their stakeholders, their constraints.

**Do not use when:** the user has already handed over the context (use
the collapse rule, or co-construction against their artifact), or the
answers are discoverable by search (use investigation — asking the user
to recite public facts is burden-shifting).

---

## Mode 2: Checkpointed Co-Construction

An artifact drives the structure; the human paces the build. The
defining moves:

1. **Artifact precondition.** Check whether the driving artifact (a
   template, outline, case study, or prior output) is already in the
   session or attached. If it is missing, ask for it before doing
   anything else.
2. **The artifact's sections are the iterator.** The multi-turn
   structure comes from the artifact, not from a hardcoded question
   list. Work one section at a time.
3. **Checkpoint gate.** After completing each section, stop and ask:
   *"Want to refine this section, or move on to [next section name]?"*
   Wait for the response. Naming the next section keeps the user
   oriented without a progress recap.
4. **Fill gaps honestly.** Use session context first, then web search.
   Label every gap explicitly as **Assumption** or **Open Question**.
   Never invent facts, data, approvals, or commitments.
5. **Assemble on request.** After the final section, offer to assemble
   the full artifact into a single document.
6. **Closing self-critique.** Append: strongest section, weakest
   section, top assumptions to validate, recommended next step.

**Use when:** the deliverable has a known structure (a template the
team already uses) and the value is in building it well section by
section, with the human steering quality at each gate.

**Do not use when:** there is no driving artifact (facilitate one into
existence first), or the human will not be present to gate sections
(use investigation mode with a default-assumption fallback).

---

## Mode 3: Autonomous Investigation

The world holds the context; the AI does the fieldwork. The human sets
direction and defaults, then reviews evidence. The defining moves:

1. **Autonomy-first posture.** "Do the heavy lifting yourself. Only ask
   if absolutely necessary — and default to strong, evidence-based
   assumptions if the user does not respond." This is what makes the
   prompt runnable by an agent, in a loop, or on a schedule, where
   nobody answers questions.
2. **Question budget.** A hard cap (e.g., "ask no more than 4 total
   questions"), not a facilitation arc.
3. **Default positioning block.** The prompt states its assumptions
   upfront (target buyer, product type, scope) as overridable defaults,
   so a non-response still produces a defensible result.
4. **Search plan gate.** Before researching, show a short plan (what
   will be searched, which source types, how facts will be separated
   from inferences) and continue unless the user revises it. This is
   the mode's one cheap checkpoint: reviewing a 3-bullet plan costs
   seconds; reviewing a wrong report costs the whole run.
5. **Evidence contract.** A clickable, checkable source URL for every
   major data point, from mixed credible source classes (government
   data, industry reports, filings, pricing pages, workforce data,
   credible news). Show ranges and explain the uncertainty when data
   is soft.
6. **Three-level evidence labels.** Mark key points **Fact**
   (source-supported), **Inference** (evidence-based interpretation),
   or **Assumption** (working guess). Keep labels short. Where the
   output is tabular, include an evidence-quality dimension.
7. **Do-not-invent list.** Name the domain's specific fabrication
   risks explicitly (for competitive work: competitors, features,
   pricing, market share, customer wins, roadmap items). Generic
   "don't fabricate" is weaker than naming where this domain's
   hallucinations live.
8. **Method constraint.** Specify the analytical method so the AI cannot
   take the lazy path (e.g., "bottom-up calculations, not just top-down
   percentages").
9. **Governing criterion and output mode.** One line that resolves
   tradeoffs (e.g., "prioritize speed and defensibility over
   perfection," or "report only material shifts"), plus an output-size
   governor: **Just Enough Mode** by default (short bullets, strongest
   findings only, no giant report), Verbose Mode only on request.
10. **Structured uncertainty.** Sensitivity analysis (best / base /
    worst) or confidence labels, so uncertainty is exposed structurally,
    not hidden in hedge-words.
11. **Stable output schema.** A fixed section order, so run N and run
    N+1 are diffable. For scheduled or looped prompts, add a **delta
    rule**: given the previous snapshot, report only what materially
    changed.

Exemplars: `market-intelligence/tam-sam-som-analysis-prompt.md` (sizing) and
`market-intelligence/competitive-research-snapshot-prompt.md` (landscape,
with the search plan gate and three-level labels in full form).

**Use when:** the deliverable depends on public, discoverable evidence —
market sizing, competitive intelligence, company research, trend
monitoring — and especially when the prompt should be schedulable.

**Do not use when:** the deliverable depends on private context only the
user holds (facilitate instead), or when the user's judgment is the
product and evidence is secondary.

---

## Shared Conventions (All Modes)

Whatever the mode, prompts in this repository:

- **Name every assumption.** The user always knows what was guessed,
  inferred, or defaulted. Artifacts close with "Assumptions to Validate."
- **Declare searches.** Say that a search is happening and why. Never
  silently fabricate specifics.
- **State a governing criterion** when tradeoffs are likely, so the AI
  resolves them the way the author would.
- **Keep humans as decision owners.** The AI proposes, drafts, and
  investigates; it does not approve, commit, or decide.
- **Close with a Final Step block** — exactly 4 numbered next options,
  recommended option first (see `SUBMISSIONS-GUIDE.md`).
- **Preserve template stability.** Output schemas are contracts; version
  structural changes explicitly.

---

## Choosing a Mode: Quick Test

1. Could the AI answer the intake questions itself with a web search?
   → **Investigation.** Asking the user is burden-shifting.
2. Is there a template or artifact that already defines the structure,
   and will the human be present to steer? → **Co-construction.**
3. Otherwise → **Facilitation**, with the collapse rule ready for users
   who arrive prepared.
