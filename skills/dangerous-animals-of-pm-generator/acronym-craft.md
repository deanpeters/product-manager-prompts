# Writing Creature Acronyms That Work

Reference for the Dangerous Animals beast generator, covering the two rules that
decide whether a creature acronym is usable in a real room or just a joke that
dies on contact. Applies equally to the skill
(`skills/dangerous-animals-of-pm-generator/`) and the prompt it was adapted from
(`prompts/Dangerous Animals of Product Management Beast Generator.md`).

## Contents

- The failure this document exists to prevent
- Rule: one mechanism, not two traits
- The "which is why" test
- Rule: every word carries freight
- Worked pass/fail table
- Why WoLF and ZEbRA are compliant
- Checklist

## The failure this document exists to prevent

The original rule said **"sentence-like structure: the words should work
together like a sentence."** That rule taught the bug. A sentence is a subject
plus a predicate, so asking for one reliably produced expansions like:

> **MACAW** — Mentions AI Constantly, Accomplished Wrapper

Two complaints about the same person, joined by a comma, with nothing connecting
them. Being a thin wrapper does not cause the constant AI talk. The two traits
merely co-occur.

The rule also cited RHiNO as its example of a "sentence," when RHiNO is not a
sentence at all — it is a noun phrase. The rule contradicted its own exemplar.

**A beast that names a type instead of a mechanism cannot be used to argue.**
Nobody can point at a decision in a meeting and say "that's a MACAW," because
there is no cause to point at.

## Rule: one mechanism, not two traits

The expansion must hold together as a single idea. Exactly two shapes do that.

### Shape 1 — a single noun phrase

The behavior is **implied by the noun**, never narrated by a second clause.

> **RHiNO** — Really High-value, New Opportunity
> **HiPPO** — Highest Paid Person's Opinion

RHiNO never says what the salesperson does. It does not need to: "opportunity"
already carries the pursuit, the optimism, and the derailment. The comma here is
an adjective separator, not a clause boundary. Everything modifies one head
noun.

### Shape 2 — cause and effect

The first half **produces** the second.

> **ORCA** — Optimistic Reasoning, Catastrophic Action
> **DODO** — Demo Overpromised, Deployment Obliterated

Here the comma is a hinge. The optimistic reasoning is *why* the action is
catastrophic. The overpromised demo is *why* the deployment is obliterated.

### The failure is coordination

The problem was never the comma. It is **coordination** — two things that
merely sit next to each other. A list is not a mechanism.

## The "which is why" test

Say the expansion aloud with **"which is why"** in the comma's place.

| Expansion | With the test | Verdict |
|---|---|---|
| Demo Overpromised, Deployment Obliterated | Demo overpromised, **which is why** deployment obliterated | holds |
| Silent Handshake, Roadmap Knifed | Silent handshake, **which is why** roadmap knifed | holds |
| Mentions AI Constantly, Accomplished Wrapper | Mentions AI constantly, **which is why** accomplished wrapper | breaks |

If the only connector that fits is **"and also,"** you have written a list. Pick
the shape before you pick the words.

## Rule: every word carries freight

Intensity words are not evidence. *Escalates*, *Hemorrhages*, *Obliterated*,
*Destroys*, *Devastates* announce that something is bad without naming what or
how. A beast built from them describes any dysfunction at any company, which
means it names nobody's problem in particular. It is unfalsifiable, and an
unfalsifiable beast is unusable in a real room.

A word earns its slot by being **specific and checkable**. "Highest Paid" is
observable. "Demo Overpromised" names the exact act.

**Freight comes from binding, not from the word itself.** The same word passes
or fails depending on what it is attached to:

- *Deployment Obliterated* — works. The deployment is the thing obliterated.
- A bare *Obliterated* — melodrama. Nothing is named.

Attach the verb to a subject or cut it.

**Never add a word only to reach a letter.** The tell is a trailing adverb doing
no work:

> **REMORA** — Roadmap Edits Made Off-Record, ~~Always~~ → **Rarely Argued**

"Always" existed purely to supply the final A. "Rarely Argued" turns the
expansion into cause and effect: made off-record, *which is why* nobody argues.
If no honest word fits the letter, pick a different animal.

## Why WoLF and ZEbRA are compliant

Two of the five core Dangerous Animals are neither noun phrases nor cause and
effect, and they are still correct. This matters, because a stricter rule
("noun phrases only") would invalidate canon:

| Beast | Expansion | Why it holds |
|---|---|---|
| **WoLF** | Works on Latest Fire | A single predicate. There are no halves to coordinate. |
| **ZEbRA** | Zero Evidence But Really Arrogant | The halves are bound **concessively** by "but" — arrogance *despite* ignorance is one idea, not two. |

The governing principle is therefore **"one mechanism," not "one noun phrase."**
Halves are allowed when something binds them: causally, concessively, or by
subordination. Only bare coordination fails.

The five core Dangerous Animals — **HiPPO, RHiNO, ZEbRA, WoLF, Seagull
Manager** — are canon from *The Dangerous Animals of Product Management*. Cite
them; do not rewrite them. ORCA and DODO appear in the skill as shape
illustrations only.

## Checklist

Before shipping a creature:

- [ ] The acronym spells a real animal species noun (not a trait, sound, or action)
- [ ] 3–6 letters, stretching to 8 only for an unmistakably better metaphor
- [ ] The expansion is one noun phrase **or** cause and effect
- [ ] "Which is why" fits between the halves, if there are halves
- [ ] No bare intensity verb floats without a subject
- [ ] No word is present only to satisfy a letter
- [ ] Someone could point at a real decision and name this beast out loud
