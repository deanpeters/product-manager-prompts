# Market Intelligence

**Autonomous research prompts: the AI does the fieldwork, you review
the evidence**

Prompts in this directory follow the **autonomous investigation**
interaction mode (see [`interaction-modes.md`](../interaction-modes.md)).
Where `/prompts/` assumes you hold the context and `/prompt-generators/`
facilitates it out of you, investigations point the AI at the world:
web search, published data, credible sources — with citations, labeled
inference, and defaults that let the prompt run without you.

That last property matters: because these prompts proceed on
best-available evidence when nobody answers questions, they are
suitable for agents, loops, and scheduled runs — a competitive scan
that refreshes quarterly, a market snapshot that diffs against last
month's.

## The contract every investigation honors

- **Question budget** — a hard cap (usually 3), then proceed with
  labeled assumptions
- **Search plan gate** — a 3-bullet plan shown before researching;
  it continues unless you revise it
- **Evidence labels** — every key point marked **Fact** (source-
  supported), **Inference** (evidence-based interpretation), or
  **Assumption** (working guess)
- **Real, checkable URLs** — and a do-not-invent list naming the
  domain's specific fabrication risks
- **Just Enough Mode by default** — strongest findings, short
  bullets; Verbose only on request
- **Stable output schema** — so run N and run N+1 are diffable, which
  is what makes scheduled re-runs and delta reports possible
- **Final Step block** — exactly 4 numbered next options

## What's Available

| Prompt | Best For |
|--------|----------|
| **[competitive-research-snapshot-prompt.md](competitive-research-snapshot-prompt.md)** | Just-enough competitive landscape research with cited snapshots, a comparison matrix, and "so what" implications |
| **[competitive-intel-watch-prompt.md](competitive-intel-watch-prompt.md)** | Scheduled delta monitoring against a prior snapshot: material shifts only, with battle-card update flags |
| **[market-landscape-scan-prompt.md](market-landscape-scan-prompt.md)** | Mapping a market's segments, players, substitutes, and whitespace before sizing or positioning |
| **[voice-of-customer-miner-prompt.md](voice-of-customer-miner-prompt.md)** | Mining reviews, app stores, and forums for unmet needs and competitor weaknesses, with quoted evidence |
| **[earnings-executive-signal-refresh-prompt.md](earnings-executive-signal-refresh-prompt.md)** | Quarterly diff of one company's executive and strategy signals against a prior profile |
| **[pricing-packaging-tracker-prompt.md](pricing-packaging-tracker-prompt.md)** | Tracking competitor pricing and packaging as a diffable time series |
| **[pestel-delta-monitor-prompt.md](pestel-delta-monitor-prompt.md)** | Quarterly re-scan of macro factors: what moved, what broke, what entered the frame |
| **[tam-sam-som-analysis-prompt.md](tam-sam-som-analysis-prompt.md)** | Citation-backed market sizing, bottom-up, with best/base/worst sensitivity |
| **[battle-card-builder-prompt.md](battle-card-builder-prompt.md)** | Evidence-cited battle card from public sources: per-claim labels, field-action format |
| **[swot-analysis-prompt.md](swot-analysis-prompt.md)** | SWOT with sources, quadrant discipline, and the S-O / W-T crossings |
| **[porters-five-forces-prompt.md](porters-five-forces-prompt.md)** | Industry structure read: five rated forces with documented signals, profit-pool implication |
| **[ansoff-matrix-prompt.md](ansoff-matrix-prompt.md)** | Growth options with evidence per quadrant, risk gradient respected, recommended sequence |
| **[all-source-fusion-prompt.md](all-source-fusion-prompt.md)** | The situation room: fuses signals from the other investigations into confidence-rated stories with artifact-mapped responses |

## The tradecraft shelf

The prompts above are the runnable layer. The doctrine behind them —
what to collect, where, and which signal → inference chains to run —
lives in [`reference/`](reference/):

- **[competitive-research-compendium.md](reference/competitive-research-compendium.md)**
  — the eight intelligence-community collection disciplines (OSINT,
  FININT, GEOINT/DEMOINT, TECHINT, HUMINT, SIGINT, MASINT, All-Source
  Fusion) mapped to PM artifacts, with sources, signal chains,
  confidence stacking, and a fusion cadence
- **[regional-source-overlays-eu-mena.md](reference/regional-source-overlays-eu-mena.md)**
  — EU and MENA source overlays: procurement platforms, registries,
  statistics bureaus, and the regional guardrails (the disciplines
  don't change across markets; the sources and evidentiary burden do)

Files in `reference/` are doctrine, not prompts — they carry no
comment block and are excluded from the catalog and validator.

### Discipline coverage

How this directory's prompts map onto the compendium's disciplines —
and where the gaps are:

| Discipline | Covered by |
|---|---|
| OSINT | market-landscape-scan, competitive-research-snapshot, voice-of-customer-miner |
| FININT | earnings-executive-signal-refresh *(procurement/government-spend angle uncovered)* |
| GEOINT/DEMOINT | tam-sam-som-analysis, pestel-delta-monitor (macro terrain deltas) |
| TECHINT | *gap — patents, trademarks, technographics, changelog diffs* |
| HUMINT | *gap — hiring signals, talent moves, employee sentiment* |
| SIGINT | competitive-intel-watch, pricing-packaging-tracker |
| MASINT | *gap — supply chain and ops exhaust; strongest for hardware/industrial* |
| All-Source Fusion | all-source-fusion (confidence stacking, conflict digs, artifact-mapped responses); swot-analysis, porters-five-forces, ansoff-matrix, and battle-card-builder consume the fused evidence |

**Typical flow:** landscape scan → snapshot the players that matter →
watch on a cadence, with the pricing tracker, executive refresh, and
PESTEL delta as deeper lenses. The strategy frameworks then build on
that evidence: **five forces** reads the industry's structure, **SWOT**
reads one player's position, **Ansoff** maps the growth options,
**TAM/SAM/SOM** sizes them, and the **battle-card builder** arms the
field. When several investigations have run, **all-source fusion**
stacks their signals into confidence-rated stories — the situation
room over the collection floor. To build a custom investigation, use
[prompt-generators/research-agent-prompt-generator.md](../prompt-generators/research-agent-prompt-generator.md).
To turn any output here into a stakeholder story, use
[storytelling/Generator - Research-to-Narrative Bridge.md](../storytelling/Generator%20-%20Research-to-Narrative%20Bridge.md).
For loop, batch, and routine recipes over these prompts, see
[loops/](../loops/) — swot-batch, market-sizing-loop, and
competitive-watch-routine run this directory's frameworks under
governed repetition.
