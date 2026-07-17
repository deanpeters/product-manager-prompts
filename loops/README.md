# Loops

**Seasoned `/goal`, `/loop`, `/batch`, and `/routine` recipes for the
prompts you already run**

Prompts aren't dead. They just got a bigger vocabulary. You still
have to prompt the loop, prompt the goal, prompt the batch and the
routine — nobody skipped a step, they just renamed the step and put
a slash in front of it. And the second you're prompting a loop,
you're one bad instruction away from a runaway that won't stop, or a
batch that quietly burns your context window recomputing the same
thing forty times.

This directory recasts key prompts from the library as **command
recipes**: the plain version that works today, then the same workflow
seasoned with plain-English controls, then — only where it earns its
keep — Just Enough Jinja2.

(Companion reading: Dean Peters, *"Prompts Aren't Dead. They Just Got
a Bigger Vocabulary."* The four rules below come from Leen Ammeraal's
*Programs and Data Structures in C*, Wiley, 1987 — loop discipline
that predates every one of these platforms.)

## The Four Rules

1. **Calculate once, iterate often.** Don't recompute the same
   expensive judgment on every pass. Compact the stable context —
   persona, outcome, evidence, decisions made — into a base camp the
   loop carries forward.
2. **Order your checks by cost.** Cheap checks first (does the
   required element exist? does it contradict anything?), expensive
   reasoning only when the cheap check didn't already clear it.
   Don't send a sommelier to inspect an empty bottle.
3. **Index before you search.** Map the territory once — sections,
   themes, epics, dependencies, open questions — then work from the
   map instead of rescanning the whole corpus every pass.
4. **Know your critical path before you loop.** Some items block
   others. Don't loop on step seven while step three is still under
   negotiation.

## The Four Primitives and How They Fail

| Primitive | Defines | Failure mode | The control |
|---|---|---|---|
| `/goal` | The destination | Ambiguity — moving toward what merely *sounds* successful | State the outcome, the evidence of success, and when to stop |
| `/loop` | What repeats | Motion without progress | Pass ceiling, no-change exit, report-per-pass, ask after a survivor |
| `/batch` | Scope of repetition | Scale without visibility | Item cap, one at a time, per-item report, fail-stop |
| `/routine` | What's reusable | Drift in captivity | Name + version in every output; record sources and rubric |

## The Three Levels (every recipe here uses them)

- **Level 0 — Unseasoned.** The plain commands. They work today.
  You just can't see how many passes it took or what broke when
  story seventeen comes out wrong.
- **Level 1 — Loop lingo.** A plain-English operating contract:
  turn-taking, modify-or-continue gates, ceilings, stop conditions,
  compaction. Not programming — decomposition, which is the job.
- **Level 2 — Just Enough Jinja2 (JEJ).** Visible bounds, batch
  caps, and routine receipts. Markdown remains the meal; Jinja2 is
  the seasoning. Use a light hand. (Full notation guidance:
  [`jinja2-prompt-structures.md`](../jinja2-prompt-structures.md).)

## What's Available

| Recipe | Recasts | Primitives |
|--------|---------|------------|
| **[story-splitting-loop.md](story-splitting-loop.md)** | [user-story-splitting](../prompts/user-story-splitting-prompt-template.md) via the Lawrence rubric | `/goal` + `/loop` |
| **[prd-section-loop.md](prd-section-loop.md)** | [prd-workshop](../workshops/prd-workshop.md) / [prd-prompt-template](../prompts/prd-prompt-template.md) | `/goal` + `/loop` |
| **[epic-story-batch.md](epic-story-batch.md)** | [backlog-epic-hypothesis](../prompts/backlog-epic-hypothesis.md) + story generation at scale | `/batch` |
| **[research-synthesis-loop.md](research-synthesis-loop.md)** | Interview/VoC synthesis ([voice-of-customer-miner](../market-intelligence/voice-of-customer-miner-prompt.md) downstream) | `/goal` + `/loop` |
| **[competitive-watch-routine.md](competitive-watch-routine.md)** | [competitive-intel-watch](../market-intelligence/competitive-intel-watch-prompt.md) | `/routine` |
| **[swot-batch.md](swot-batch.md)** | [swot-analysis](../market-intelligence/swot-analysis-prompt.md) across a competitor set | `/batch` |
| **[market-sizing-loop.md](market-sizing-loop.md)** | [tam-sam-som-analysis](../market-intelligence/tam-sam-som-analysis-prompt.md) segment by segment | `/goal` + `/loop` |
| **[fusion-cadence-routine.md](fusion-cadence-routine.md)** | The seven [market-intelligence collection sweeps](../market-intelligence/README.md) + [all-source-fusion](../market-intelligence/all-source-fusion-prompt.md) on the compendium's tiered cadence | `/routine` |

## When NOT to Use This Directory

A casual one-off doesn't need a governed, versioned, multi-turn
routine. You do not need loop ceremony to rewrite a meeting invite.
The economics change when the prompt becomes **infrastructure** —
when other people depend on it, when a batch runs while you're
elsewhere, or when someone will eventually ask what version produced
the output. That's when scripted beats silent.
