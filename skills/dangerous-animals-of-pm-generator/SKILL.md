---
name: dangerous-animals-of-pm-generator
description: Generate creature acronyms that name PM dysfunctions, blockers, or winning strategies. Use when you want to give your team shared vocabulary for the animals hiding in your product work.
license: CC-BY-NC-SA-4.0
metadata:
  intent: >-
    Guide product managers through a 5-question facilitation that maps their real jobs, pains, and frustrations onto creature acronyms — then outputs a session-starter prompt for a dedicated beast-naming exploration. Surfaces the "Dangerous Animals" (dysfunctions, anti-patterns, blockers) or "Beneficial Beasts" (strategies, behaviors, mindsets) lurking in daily PM work.
  type: interactive
  theme: creativity-reframing
  best_for:
    - "Making PM anti-patterns visible and memorable for teams and stakeholders"
    - "Building shared vocabulary for dysfunctions in retrospectives or team charters"
    - "Reframing obstacles with humor to reduce friction in sensitive conversations"
  scenarios:
    - "My team keeps building what the HiPPO wants instead of what customers need — I want to name this and the other creatures like it"
    - "I need a warm-up exercise for a retrospective about product dysfunctions"
    - "I want memorable metaphors to explain PM anti-patterns to non-PM stakeholders"
  estimated_time: "10-15 min"
---

<!--
## Description:
Runs a five-question facilitation over a product manager's real jobs,
pains, and obstacles, then names 4-9 creature acronyms that make those
hazards discussable -- the meeting that eats a day, the stakeholder who
circles, the requirement that molts overnight.

## Standalone: yes

## Usage Note:
Reach for this in a retro that has gone flat, a team offsite, or any
moment when people will describe a dysfunction as a monster long before
they will name it in a status report. Humor is the anesthetic; the
diagnosis is the point.

## When NOT to Use:
When the team is not safe enough to name dysfunctions honestly, when a
metaphor would substitute for direct feedback someone is owed, or when
the moment calls for a formal framework artifact rather than a naming
exercise.

## Instructions:
1. Ask the five questions one at a time; do not batch them.
2. Generate options 1-4 per question from what the user has already
   said -- the enumerated lists below are worked examples, not a script.
3. Let the user pick beast mode and animal category before naming
   anything.
4. Name the creatures directly. Unlike the source prompt, this skill
   does not emit a session starter for the user to run elsewhere.

## Pedagogic Notes:
- Metaphor lowers the cost of naming an uncomfortable truth, which is
  why satire belongs in a serious prompt library.
- The animal-noun-first rule teaches a general prompting lesson: bind
  the generator to a hard constraint it cannot satisfy by paraphrase,
  or it will drift to the nearest easy word.
- Building shared vocabulary for recurring hazards makes them
  discussable later without the metaphor.

## Attribution:
Created by Dean Peters (Productside.com), September 2024.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires
expressed written permission from Dean Peters.

Date: August 8, 2026
-->

## Purpose

Guide product managers through a 5-question facilitation that maps real jobs, pains, and frustrations onto creature acronyms — then outputs a session-starter prompt for a dedicated exploration. Use this to name the "Dangerous Animals" lurking in your product work (dysfunctions, anti-patterns, blockers) or the "Beneficial Beasts" worth cultivating (strategies, behaviors, mindsets).

This is not a framework document — it's a creative reframing tool. Naming a dysfunction gives your team shared vocabulary to talk about it without pointing fingers.

## Key Concepts

### The Creature Acronym Pattern

Creature names map PM realities onto animal imagery through acronyms.

**The five core Dangerous Animals.** These are canon from *The Dangerous
Animals of Product Management* and are not up for redefinition — cite them,
don't rewrite them:

| Creature | Acronym | What It Represents |
|---|---|---|
| HiPPO | Highest Paid Person's Opinion | Decisions driven by seniority, not evidence |
| RHiNO | Really High-value, New Opportunity | Shiny object that derails the roadmap |
| ZEbRA | Zero Evidence But Really Arrogant | Stakeholder with strong opinions and no data |
| WoLF | Works on Latest Fire | Reactive PM who abandons strategy for urgency |
| Seagull Manager | — | Flies in, makes noise, dumps on everything, leaves |

**Illustrations only**, used below to show the cause-and-effect shape. Generate
your own; these are not canon:

| Creature | Acronym | What It Represents |
|---|---|---|
| ORCA | Optimistic Reasoning, Catastrophic Action | Confident plan that breaks on contact |
| DODO | Demo Overpromised, Deployment Obliterated | The demo that wrote a cheque delivery couldn't cash |

### Five Acronym Rules

1. **Animal nouns only** — The acronym must spell an actual animal species noun from the chosen category. FROG, TOAD, NEWT, SALAMANDER, AXOLOTL are valid. CROAK, SLIME, LEAP, AGILE, STINKS are not. If it isn't a creature name, it isn't a creature.
2. **Short and punchy** — aim for 3–6 letters. Stretch to 8 only when the longer animal noun is unmistakably the better metaphor (AXOLOTL earns its length; PLATYPUS rarely does).
3. **One mechanism, not two traits** — the expansion has to hold together as a single idea. Two shapes work:
   - **One noun phrase**, where the behavior is *implied by the noun* rather than narrated. RHiNO — *Really High-value, New Opportunity* — never says what the salesperson does, because the noun already did it. Same with HiPPO — *Highest Paid Person's Opinion*.
   - **Cause and effect**, where the first half produces the second. ORCA — *Optimistic Reasoning, Catastrophic Action*. DODO — *Demo Overpromised, Deployment Obliterated*. Here the comma is a hinge, not a list separator.

   The failure is **coordination**: two traits that merely co-occur. MACAW — *Mentions AI Constantly, Accomplished Wrapper* — names two complaints about the same person and no mechanism joining them; being a thin wrapper doesn't cause the AI talk. **Test:** put "which is why" between the halves. If only "and also" fits, it's a list, not a beast.
4. **Every word carries freight** — intensity words are not evidence. *Escalates*, *Hemorrhages*, *Obliterated* announce that something is bad without naming what or how, and a beast built from them would fit any dysfunction at any company. A word earns its slot by being specific and checkable: "Highest Paid" is observable, "Demo Overpromised" names the exact act. The same word passes or fails depending on what it's bound to — *Deployment Obliterated* works because the deployment is the thing obliterated, while a bare *Obliterated* is melodrama. Attach it to a subject or cut it. Never add a word just to reach a letter.
5. **Emotional impact** — The name should create a vivid, memorable image. ZEbRA and WoLF work because they trigger an instant visual *and* a gut reaction.

### Pains, Gains, and Jobs Framing

The facilitation collects three lenses before generating beasts:
- **Jobs** — What PM tasks or outcomes are you trying to achieve?
- **Pains** — What makes those jobs hard?
- **Obstacles** — What specific behaviors, personalities, or dynamics block you?

These map directly onto which creatures get created and what they represent. Specific inputs produce specific beasts.

### Two Beast Modes

- **Dangerous Animals Enumeration** — Creatures representing dysfunctions, blockers, anti-patterns. Good for retrospectives, team charters, naming what's already happening.
- **Beneficial Beasts List** — Creatures representing strategies, mindsets, behaviors worth cultivating. Good for culture-building, onboarding, and making positive behaviors memorable.

### When to Use This
- Team retrospectives where you need a low-threat way to name dysfunctions
- Stakeholder conversations about PM culture and working agreements
- Personal reflection on what's blocking your best work
- Icebreakers for PM workshops or offsites
- Explaining PM anti-patterns to non-PM audiences with humor

### When NOT to Use This
- As a substitute for direct feedback in serious performance conversations
- When the team isn't psychologically safe enough to name dysfunctions honestly
- When the moment calls for a formal framework artifact — a positioning statement, a job story, a prioritization model — and a metaphor would read as deflection

---

## Application

This interactive skill asks **5 questions one at a time**, building a creature profile from your real PM context. Wait for the user's response to each question before moving on.

---

### Question 1: Your Jobs

**Agent asks:**
"What jobs or tasks are you, as a product manager, struggling to accomplish?"

**Offer 4 enumerated options:**

1. **Stakeholder alignment** — "Getting buy-in across exec, engineering, design, and sales when priorities conflict"
2. **Discovery and validation** — "Running research to find and validate real customer problems before building"
3. **Roadmap prioritization** — "Making defensible decisions about what gets built, cut, and deferred"
4. **Team delivery** — "Keeping cross-functional teams unblocked, coordinated, and shipping"

**Or describe your own job in your words.**

**User response:** [Selection or custom]

---

### Question 2: Your Pains

**Agent asks:**
"What are the main challenges or pains you face in accomplishing this job?"

**Offer 4 enumerated options (adapt based on Q1):**

**Example options (if Q1 = Stakeholder alignment):**
1. **HiPPO dynamics** — "Decisions driven by the highest-paid person's opinion, not evidence or customer insight"
2. **Misaligned incentives** — "Different departments optimizing for their own metrics, not shared outcomes"
3. **Death by committee** — "Too many stakeholders with veto power, too few with accountability"
4. **Invisible decisions** — "Strategic pivots made in hallways and offsites that surface as done deals"

**Example options (if Q1 = Roadmap prioritization):**
1. **Scope creep** — "Features growing beyond original intent, quietly consuming time and quality"
2. **Shiny object syndrome** — "Executives chasing competitor features instead of customer jobs"
3. **Resource illusions** — "Commitments made without checking engineering capacity"
4. **Technical debt blindness** — "Pressure to ship new things while old things quietly break"

**Or describe your own pain in your words.**

**User response:** [Selection or custom]

---

### Question 3: Specific Obstacles

**Agent asks:**
"Are there specific obstacles, frustrations, or frustrating personalities you encounter that you'd like to name?"

**Offer 4 enumerated options:**

1. **Personality archetypes** — "The scope-creeper, the HiPPO, the seagull manager, the ZEbRA"
2. **Process bureaucracy** — "Approval chains, committee decisions, change management overhead that buries momentum"
3. **Engineering-PM friction** — "Technical debt blockers, sprint overload, misaligned definition of done"
4. **Market and competitive pressure** — "External forces constantly reshaping priorities mid-quarter"

**Or describe your specific obstacle, frustration, or personality — the more specific, the better the creature.**

**User response:** [Selection or custom]

---

### Question 4: Beast Mode

**Agent asks:**
"Would you like to explore a Dangerous Animals Enumeration or a Beneficial Beasts List?"

**Offer 2 options:**

1. **Dangerous Animals Enumeration** — "Creatures that name dysfunctions, blockers, and anti-patterns you're navigating right now"
2. **Beneficial Beasts List** — "Creatures that represent strategies, mindsets, or behaviors worth cultivating in yourself or your team"

**User response:** [1 or 2]

---

### Question 5: Animal Kingdom

**Agent asks:**
"What category of living thing would you like to explore?"

**Offer 4 enumerated options:**

1. **Jungle animals** — Lions, gorillas, crocodiles, pythons (power, predation, patience, constriction)
2. **Ocean creatures** — Sharks, octopus, anglerfish, remora (depth, camouflage, lure, parasitism)
3. **Birds** — Eagles, seagulls, ostriches, peacocks (vision, noise, avoidance, display)
4. **Insects** — Ants, bees, wasps, fireflies (swarms, hierarchy, stings, misdirection)

**Or name your own category (zoo, deep sea, Arctic, mythological, etc.).**

**User response:** [Selection or custom]

---

### Output: Generate the Creatures

After collecting all five responses, generate 4–9 creatures directly using the user's jobs, pains, and obstacles as source material. Do not output a prompt to run elsewhere — name the beasts now.

For each creature, use `template.md` format:

```
## [Animal Name] — [ACRONYM expansion]
*[Animal type] | [Beast mode]*

[One sentence describing what this creature represents and what makes it dangerous or beneficial.]
[One sentence describing the specific trigger — when does this creature appear in the PM's world?]
```

**Acronym rules (apply to every creature):**
- **The acronym must spell an actual animal species noun** from the chosen category. Start here — pick the animal, then build the acronym. Never work backwards from a characteristic or action.
  - **Valid** (real animals): FROG, TOAD, NEWT, SIREN, AXOLOTL, AMPHIUMA
  - **Invalid** (actions, sounds, traits): CROAK, SLIME, LEAP, AGILE, STINKS, SPAWN
- **The expansion names one mechanism, not two traits.** Either a single noun phrase where the behavior is implied by the noun (RHiNO — *Really High-value, New Opportunity*), or cause and effect where the first half produces the second (DODO — *Demo Overpromised, Deployment Obliterated*). Never two co-occurring traits joined by a comma (MACAW — *Mentions AI Constantly, Accomplished Wrapper*). Test each expansion by putting "which is why" between the halves; if only "and also" fits, rewrite it.
- **Every word is specific and checkable.** No bare intensity verbs (*Escalates*, *Hemorrhages*, *Obliterated*) floating without a subject, and no word added only to reach a letter.
- Name should trigger a vivid, gut-level reaction.

**After the creatures:** Offer 3 next options:
1. Name more creatures from the same session context
2. Flip to Beneficial Beasts — name the creatures that counter these dangers
3. Export a one-pager naming all creatures (suitable for a team retro or charter)

---

## Examples

See `examples/sample.md` for a full worked conversation and creature output.

Mini excerpt — a creature generated from a stakeholder alignment / ocean creatures session:

```
## SHaRK — Silent Handshake, Roadmap Knifed
*Ocean creatures | Dangerous Animals*

The agreement made in the room you weren't in, which arrives already settled.
Surfaces the Monday after a QBR, when a commitment you never scoped is read
back to you as a decision.
```

---

## Common Pitfalls

### Pitfall 1: Using Characteristics Instead of Animal Nouns
**Symptom:** CROAK, SLIME, LEAP, AGILE, STINKS, SPAWN — words that describe what an animal does, sounds like, or looks like, rather than what it *is*.

**Consequence:** The creature loses its identity. The whole point is that the animal name carries the metaphor — a TOAD already conjures something puffed-up and warty before you read a single letter of the acronym.

**Fix:** Start with the animal noun, then build the acronym. Ask "what real animal from this category fits this dysfunction?" first. Then make the letters work. Never start from the dysfunction and hunt for matching initials.

---

### Pitfall 2: Acronyms That Are Too Forced
**Symptom:** "PLATYPUS — Product Leader Always Talking About Your Poorly Uncertain Solutions"

**Consequence:** The creature doesn't stick. Humor requires economy. Longer = forgettable.

**Fix:** Aim for 3–6 letters. Cut until the acronym reads like a real phrase, not a scrabble rack.

---

### Pitfall 3: Two Traits Wearing One Acronym
**Symptom:** "MACAW — Mentions AI Constantly, Accomplished Wrapper." The comma joins two separate complaints about the same person.

**Consequence:** The beast describes a *type* instead of naming a *mechanism*, so it can't be used to argue. Nobody can point at a decision and say "that's a MACAW," because there's no cause to point at — only two adjectives that happened to land on the same person.

**Fix:** Pick the shape before you pick the words. Either the behavior is implied by a noun (RHiNO), or the first half causes the second (ORCA, DODO). Say the expansion aloud with "which is why" in the comma's place: *Demo Overpromised, **which is why** Deployment Obliterated* holds. *Mentions AI Constantly, **which is why** Accomplished Wrapper* does not.

---

### Pitfall 4: Melodrama Standing In for Evidence
**Symptom:** Expansions leaning on *Escalates*, *Hemorrhages*, *Obliterated*, *Destroys*, *Devastates* — words that shout without specifying.

**Consequence:** The beast is unfalsifiable and therefore unusable in a real room. "Hemorrhages" fits every failing team on earth, so it names nobody's problem in particular.

**Fix:** Bind the verb to a subject or cut it. *Obliterated* alone is melodrama; *Deployment Obliterated* names what died. If a word is there only because the acronym needed that letter, pick a different animal.

---

### Pitfall 5: Generic Inputs, Generic Beasts
**Symptom:** Q2 answer is "things are hard" or "we have communication issues"

**Consequence:** The creature prompt generates vague, universally applicable beasts that don't name *your* situation.

**Fix:** Push for specificity in Questions 1–3. "Our CPO reshuffles the roadmap after every board meeting" produces a far more vivid creature than "leadership misalignment."

---

### Pitfall 6: Choosing the Wrong Mode
**Symptom:** Selecting Dangerous Animals when the team needs encouragement; selecting Beneficial Beasts when the team needs to name dysfunction honestly.

**Consequence:** The output doesn't match the moment.

**Fix:** Dangerous Animals = naming what's happening now. Beneficial Beasts = building toward what should happen. When in doubt, name the danger first — you can't fix what you can't see.

---

### Pitfall 7: Using Creature Names to Avoid Real Conversations
**Symptom:** Calling someone "the WoLF" in a 1:1 instead of addressing the behavior directly.

**Consequence:** Humor creates distance. Sometimes distance helps open a conversation; sometimes it replaces one.

**Fix:** Use creature vocabulary to open conversations, not close them. "We seem to have a WoLF pattern right now — can we talk about what's driving it?"

---

## References

### External Frameworks
- Clayton Christensen, *Competing Against Luck* — Jobs-to-be-Done; the jobs/pains framing behind Questions 1–2
- Alexander Osterwalder, *Value Proposition Design* — The pains / gains / jobs triad the intake borrows directly
- Avinash Kaushik — Popularized HiPPO (Highest Paid Person's Opinion), the term of art this skill generalizes from

### Provenance
- Adapted from `prompts/Dangerous Animals of Product Management Beast Generator.md` in `https://github.com/deanpeters/product-manager-prompts`
- Created by Dean Peters, September 2024. CC BY-NC-SA 4.0 (see repo LICENSE and LICENSING.md); commercial use requires expressed written permission from Dean Peters.

---

**Skill type:** Interactive
**Folder:** `skills/dangerous-animals-of-pm-generator/`
**Dependencies:** Standalone — no required skill dependencies
