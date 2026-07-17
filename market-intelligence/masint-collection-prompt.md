# masint-collection-prompt.md
<!--
## Description:
Runs a MASINT (Measurement and Signature Intelligence) collection
sweep on a target company: import/export records, facility and
project signals (permits, land, utility approvals, EPC awards),
operational capacity indicators (support response times, status-
page incident patterns), and certification pipelines. Every signal
lands in a fusion-ready inventory with a source URL, date,
evidence label, and the inference chain it supports. The satellite
photo discipline: measure the physical and operational exhaust —
abnormal resource allocation never lies.

## Usage Note:
One of seven discipline collection prompts feeding
all-source-fusion-prompt.md; doctrine in
reference/competitive-research-compendium.md (MASINT discipline).
Strongest for hardware and industrial players; for pure software
targets this sweep runs the software equivalent — ops capacity,
status-page patterns, certification registries, and
infrastructure-scale language in job postings. For MENA facility
and project sources (industrial zones, environmental permits,
utility approvals, EPC awards), load
reference/regional-source-overlays-eu-mena.md. Primary feed for
threat assessment and launch prediction.

## When NOT to Use:
- The target is a small pure-software company: expect a thin run;
  the ops-capacity section may be all there is — say so rather
  than padding.
- You need financial corroboration for a volume anomaly: that
  disambiguation is FININT's job; flag the handoff.
- You want people signals behind an ops strain: HUMINT owns
  hiring-freeze and sentiment reads.

## Required Context Keys:
1. The [TARGET] company and whether it ships physical product
2. The [DECISION] this collection will feed
3. The [GEOGRAPHY] of its operations (drives permit, customs, and
   registry sources)

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company — and does it ship hardware, run infrastructure,
   or sell pure software?"
2. "What decision should this collection feed?"
3. "Where does it operate — which countries' permits, customs, and
   registries apply?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show a 3-bullet search plan first: supply-chain sources,
   facility/project sources for the [GEOGRAPHY], ops and
   certification sources. Continue unless revised.
2. Sweep in this order: import/export and customs records,
   facility and project signals (permits, land allocation, utility
   approvals, zone tenancy, EPC awards), operational capacity
   (support response patterns, status-page incident frequency),
   certification and safety registries (in-process listings,
   notified-body selections, recalls).
3. For software targets, run the software equivalent explicitly:
   status-page incident patterns, support responsiveness,
   infrastructure-scale language in job postings, compliance
   certifications in process.
4. Log every signal in the Signal Inventory: what was observed,
   source URL with date, Fact / Inference / Assumption label, the
   inference chain it supports, and the artifact it feeds.
5. Run the compendium's MASINT inference chains explicitly: a
   20%+ volume change in critical inputs = pre-launch or demand
   collapse — flag FININT to disambiguate; new supplier
   geographies or origin shifts = market entry, tariff hedging, or
   resilience play; certification in process or a notified-body
   selection = 12-36 month runway into a regulated segment,
   visible to anyone who checks the registry; recalls or repeated
   safety alerts = quality strain with a public citation; land,
   power/water reservations, or design contracts before equipment
   = facility buildout 6-36 months ahead of any announcement;
   support strain plus a support hiring freeze = cash constraint
   or overwhelmed growth — flag HUMINT to disambiguate; office
   consolidations = cost compression, expect pricing aggression.
6. MASINT signals are ambiguous alone by nature — every chain in
   this sweep must name its disambiguating discipline, because a
   volume spike reads identically for a launch and a fire sale.
7. Keep the schema stable so run N and N+1 are diffable; if a
   prior sweep is in session, lead with the delta.

## Pedagogic Notes:
- Reading resource allocation instead of announcements teaches the
  hardest intelligence lesson: watch what they spend, not what
  they say.
- The mandatory disambiguation flag builds fusion instincts — a
  MASINT anomaly is a question addressed to another discipline,
  not an answer.
- Checking certification registries teaches that regulated-market
  entries are publicly telegraphed years out, for anyone who
  bothers to look.

## Attribution:
Created by Dean Peters (Productside.com). Collection doctrine from
the Competitive Research Compendium in this directory's reference/
shelf, MASINT discipline.

## Licensing:
MIT License

Date: July 16, 2026
-->

## Purpose

Measure one company's physical and operational exhaust and land
every signal in a fusion-ready inventory.
Workflow: **search plan -> supply chain, facilities, ops,
certifications -> signal inventory -> chains with disambiguation
flags -> gaps and handoffs.**

## Mode

**Just Enough Mode**: strongest signals only, max 5 inference
chains, one-line watch items. **Verbose Mode** only if asked.

This is a collection prompt: it gathers and labels; it does not
verdict. Confidence rating across disciplines belongs to
[all-source-fusion-prompt.md](all-source-fusion-prompt.md).

## Before You Start

Ask at most 3 questions:

1. Which company — hardware, infrastructure, or pure software?
2. What decision should this collection feed?
3. Which countries' permits, customs, and registries apply?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: supply-chain sources, facility/project
sources for the [GEOGRAPHY] (for MENA, per the regional overlay),
ops and certification sources. Continue unless revised.

## Source + Trust Rules

Real, checkable URLs with dates on every signal. Do not invent
**shipment volumes, customs records, permit filings, certification
statuses, incident counts, or response-time measurements.** Label
every signal: **Fact** / **Inference** / **Assumption**. Every
anomaly names its disambiguating discipline — a MASINT signal
without a disambiguation path is a Rorschach test, not
intelligence. Thin runs are valid: for software targets, a short
ops-capacity read beats padded supply-chain speculation.

# MASINT Collection: [TARGET]

**As-of date:** | **Decision supported:** | **Prior sweep:** [date
or "first run"]

## 1. Signal Inventory (fusion-ready)

| Signal | Source (URL, date) | Label | Inference chain | Disambiguate via | Feeds |
|---|---|---|---|---|---|
| [What was measured] | [URL, date] | [F/I/A] | [What it could mean] | [FININT / HUMINT / ...] | [Threat assessment / Launch prediction / ...] |

## 2. Strongest Inference Chains (max 5, ranked)

- [Anomaly] -> [competing explanations, labeled] -> [which
  discipline settles it] -> [what to do under each reading]

## 3. Capacity and Commitment Read

- **Physical commitments visible:** [land, permits, capacity
  reservations, EPC awards — with lead-time estimates]
- **Certification runway:** [in-process listings and what segment
  they telegraph]
- **Ops strain indicators:** [support/status patterns, labeled]

## 4. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 5. Collection Gaps and Handoffs

- [Source type out of reach this run] — [why]
- Disambiguations owed: [anomaly -> finint-collection or
  humint-collection]; regional facility sources -> reference
  overlay

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Feed this inventory into all-source fusion with the other
   disciplines
2. Run the FININT or HUMINT disambiguation on the top anomaly
3. Turn the capacity-strain signals into battle card objection
   ammo
4. Schedule-ready version: save as the baseline event-driven
   alerts diff against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
