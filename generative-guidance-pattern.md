# Generative Guidance Pattern (v2)

A conversational facilitation technique used throughout this repository to
reduce cognitive load, accumulate context progressively, and produce
higher-quality AI-generated outputs without front-loading the user.

This is **v2** of the pattern. The v1 spec (five fixed menu slots) is
retained below in the changelog. New prompts follow v2. Existing v1
prompts are grandfathered and migrate when they are next edited.

---

## The Canonical Spec (v2)

When a prompt uses the Generative Guidance pattern, the AI should:

1. **Derive the question sequence from the deliverable.** List the inputs
   the deliverable requires, order questions from broadest context to most
   specific detail, and set a question budget of 3–5. When the budget is
   reached, close the loop with a stated-assumptions summary.
2. **Ask one question at a time.** Never stack questions. Never present
   the full list upfront.
3. **For each question, offer 4 choices:**
   - **Choices 1–3**: Thoughtful, context-aware recommendations derived
     from everything the user has shared so far. Each must contain at
     least one specific detail from prior answers — never a fixed list.
   - **Choice 4**: **Other** — type your own answer, or combine numbered
     options with commentary.
4. **Keep two standing bypasses available at every question** (announce
   them when the loop opens; honor them at any turn):
   - **Take your best guess.** The AI fills in the most reasonable answer
     given everything it knows, states the assumption explicitly, and
     advances. The user can correct it at any point.
   - **Bulk drop.** The user pastes a block of notes, shares a document,
     or points at session context. The AI reads it fully, extracts answers
     to all remaining questions, lists what was found, what was inferred,
     and what is still missing, then asks only about genuine gaps.
5. **Honor loop-control verbs at any turn:**
   - **Skip** ("skip this one") — mark the question skipped and move on.
   - **Go back** ("go back to question 2") — re-ask with updated
     recommendations.
   - **Stop early** ("that's enough, build it") — use what is captured,
     flag the gaps, and produce the deliverable.
6. **Acknowledge before advancing.** After each answer, give one sentence
   of acknowledgment — what was heard and why it matters — then ask the
   next question. Not a paragraph. Not a recap.
7. **Search when sparse.** If the recommendations for a question would be
   generic because context is too thin — domain facts, named companies,
   current market data — run a web search before presenting options.
   State that the search is happening and why. Never silently fabricate
   specific-sounding options.
8. **Sharpen with each answer.** Use every answer to make the next
   question and its options more specific. By question 3 or 4, the AI
   should be generating options it could not have offered at the start.
9. **Withhold the final output until the loop closes** — all questions
   answered, a bulk drop processed, or the user stops early. On close:
   present a brief context summary (what is known, what was assumed, what
   is still open), ask for confirmation or correction, then build.
10. **Collapse on arrival context.** If the user arrives with sufficient
    context — a brief, an attachment, an example, a context dump — reduce
    or skip the questions and proceed with the best available
    interpretation. The pattern is a scaffold for thin context, not a
    ritual.

---

## Why This Works

**Workload inversion.** The AI proposes; the human reacts. Users do not
need to pre-design the artifact the AI should help create. Starting from
three plausible options is far easier than starting from a blank field.

**Standing escape routes.** "Take your best guess" and "bulk drop" are
always available, not occasionally offered. Users are never trapped in
the interview. Best-guess delegates a single decision; bulk drop lets a
user who has already done their thinking exit the loop entirely —
mid-flight, not just at the start.

**Progressive context accumulation.** Each answer narrows the option
space. The facilitation earns the output.

**Evidence honesty.** Assumptions are named and marked, searches are
declared, and the found / inferred / missing accounting after a bulk drop
keeps the AI from asking about things it was already told — or quietly
inventing things it was not.

**Context-detection collapse.** When a user arrives with enough detail,
the questions compress or disappear. This prevents the facilitation from
feeling bureaucratic.

**Pacing control.** Withholding the final output until the loop closes
prevents premature generation that has to be unwound. The confirmation
summary at close gives the user one last cheap correction point before
the expensive artifact is built.

---

## Quick Reference: The v2 Question Shape

```
[Question N of B: short question title]

[One clear question about the next meaningful decision, with one
sentence on why it matters.]

1. [Context-aware recommendation] — [brief rationale]
2. [Context-aware alternative] — [brief rationale]
3. [Context-aware alternative] — [brief rationale]
4. Other — type your own, or combine numbers with commentary.

Or, at any point: say "take your best guess," or drop in your notes
to skip ahead. You can also skip, go back, or say "that's enough,
build it."
```

The loop opener states the contract once:

```
Before I build [deliverable], I need to capture a few things. I'll ask
[B] questions, one at a time. At any point you can pick an option, type
your own answer, say "take your best guess," or drop in a block of
notes to skip ahead.
```

---

## Authoring Rules

When writing or editing a prompt that uses this pattern:

1. **Choices 1–3 must be generated from context, not hardcoded.** If you
   find yourself writing fixed option text in the prompt template, the
   facilitation is not context-aware enough. Every option must contain at
   least one specific detail from prior answers.
2. **The standing bypasses are non-negotiable fixtures.** "Take your best
   guess" and "bulk drop" must be announced at loop open and honored at
   every question. Do not omit them to shorten the prompt. They are
   load-bearing UX elements.
3. **Each question must be informed by prior answers.** If the questions
   could run in any order without changing the options, the pattern is
   not being applied correctly.
4. **The context-detection rule must be explicit.** Include a line in the
   prompt instructing the AI to reduce or skip questions when sufficient
   context is already present.
5. **Assumptions are always named.** Any gap the AI fills — via best
   guess, bulk-drop inference, or early stop — is labeled as an
   assumption the user can correct.
6. **Set the question budget in the prompt.** Derive it from the
   deliverable's required inputs; do not let the loop grow open-ended.
7. **Persona language first.** Options should be phrased from the user's
   point of view before adding any business or stakeholder translation.

---

## Pitfalls

**Stacking questions.** Symptom: the AI asks three things at once.
Fix: one question per turn, always.

**Generic recommendations.** Symptom: options that would fit any project.
Fix: every option must contain at least one specific detail from prior
answers; search first if context is too thin to be specific.

**Ignoring the bulk drop.** Symptom: the AI asks follow-up questions
about things already in the pasted content. Fix: read the full drop
before generating any questions; ask only about genuine gaps.

**Endless loops.** Symptom: the loop never closes because the AI keeps
finding more to ask. Fix: enforce the question budget; close with a
stated-assumptions summary when it is reached.

**Silent assumptions.** Symptom: the AI fills in gaps without telling the
user. Fix: every assumption is named and marked; the user always knows
what the AI guessed.

---

## Changelog: v1 to v2

The v1 spec used a five-slot menu: choices 1–3 were context-aware
recommendations, choice 4 was always "Go ahead and take your best
guess," and choice 5 was always "Something else: I'll provide my own
idea."

v2 changes, and why:

| Change | v1 | v2 | Why |
|---|---|---|---|
| Menu shape | 5 slots; guess and open-floor occupy slots 4–5 | 3 recommendations + "Other"; guess and bulk drop are standing bypasses | Escape routes belong to the whole loop, not to each menu; frees the menu for substance |
| Bulk drop | Only recognized at arrival (context collapse) | Available mid-loop, with found / inferred / missing accounting | Users finish their thinking at unpredictable moments |
| Loop control | Not specified | Skip, go back, stop early | Users need to steer, not just answer |
| Search | Not specified | Search-when-sparse, declared aloud | Prevents fabricated "specific" options |
| Acknowledgment | Not specified | One sentence before advancing | Confirms hearing without recap bloat |
| Question count | "3–5 questions" | Budget derived from the deliverable's inputs, enforced | Prevents endless loops |
| Loop close | Generate output after last question | Context summary + confirmation, then build | One last cheap correction point |

The permanent-exit intent behind v1's choices 4 and 5 is unchanged —
it is strengthened, not removed. What changed is where the exits live.

**Migration stance:** new prompts follow v2. Existing v1 prompts remain
valid and are migrated to v2 when they are next edited for any other
reason. Do not mass-rewrite the library.

---

## Relationship to Earlier Patterns

The Generative Guidance pattern evolved through several generations in
this repository:

| Stage | File | What it established |
|---|---|---|
| Origin (May 2024) | `a-generative-AI-prompt-builder-for-product-professionals.md` | Sequential Q&A → generated prompt → modification offer |
| Structured domain | `tam-sam-som-prompt-generator.md` | Domain-specific questions, filled template output |
| Decision forks | `proto-persona-prompt-generator.md`, `customer-journey-mapping-prompt-generator.md` | 3 context-aware options per fork, workload inversion, recommended choice, business translation |
| Full form (v1) | `storyline-to-prompt-generator-prompt.md` | Conditional entry, two-phase facilitation, context-aware option generation, portable artifact output |
| Engine form (v2) | `guided-context-capture` skill (Product-Manager-Skills repo) | Standing bypasses, bulk drop with gap accounting, loop-control verbs, search-when-sparse, question budgets |

Generative Guidance is one of three interaction modes used in this
repository. When the context source is an artifact (a template driving
section-by-section co-construction) or the world (autonomous
investigation with citations), see `interaction-modes.md`.

---

## Where This Pattern Is Used

**Most prompts in `/prompt-generators/`** use the Generative Guidance
pattern as their primary facilitation model. Files that exemplify it
most clearly:

- `storyline-to-prompt-generator-prompt.md` — most complete v1
  expression; conditional entry, two-phase facilitation, context-aware
  option generation per phase
- `proto-persona-prompt-generator.md` — clean three-decision-point
  structure with business translation
- `customer-journey-mapping-prompt-generator.md` — same structure,
  journey-mapping domain

**A portion of generators in `/storytelling/`** also use this pattern,
particularly those that involve facilitated narrative construction before
rendering a visual or structural output.
