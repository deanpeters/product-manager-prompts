# market-sizing-loop.md
<!--
## Description:
Build a TAM/SAM/SOM model segment by segment under a seasoned /goal
+ /loop: index the segments first (Rule 3), size one segment per
turn bottom-up with its own cited inputs, gate each on
modify-or-continue, and only then roll up — so one bad assumption
stays in its segment instead of silently propagating through the
whole model. The segment sizing format is embedded at every level.

## Usage Note:
Bring the scope (product, geography, buyer) or accept labeled
defaults. Each segment follows the evidence contract of
market-intelligence/tam-sam-som-analysis-prompt.md (bottom-up, URL
per data point, ranges for uncertainty); this recipe adds the loop
controls around it. Feeds from market-landscape-scan-prompt.md when
its segment map is in session.

## When NOT to Use:
- One homogeneous segment: run the TAM/SAM/SOM prompt directly;
  there is nothing to loop over.
- Sizing to justify a decision already made: no loop fixes that.

## Instructions:
At every level: bottom-up per segment, never top-down percentages;
a clickable URL per major data point; ranges with reasons where
data is soft; every segment rendered in the Segment Sizing Format;
roll-up only after all segments settle; sensitivity (best / base /
worst) on the roll-up.

## Pedagogic Notes:
- Segment-by-segment sizing teaches that a market model is a sum of
  arguments, not a number — and each argument can be inspected,
  challenged, and re-run alone.
- The gate per segment catches the classic failure: an average
  price or adoption rate from segment one quietly reused on
  segments two through five.
- Roll-up-last is Rule 4: the total is downstream of every segment;
  computing it early anchors everyone on a number the evidence has
  not earned yet.

## Attribution:
Created by Dean Peters (Productside.com), from "Prompts Aren't Dead.
They Just Got a Bigger Vocabulary." Sizing rules per
market-intelligence/tam-sam-som-analysis-prompt.md. Loop discipline
after Leen Ammeraal, Programs and Data Structures in C (Wiley,
1987).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Segment Sizing Format (every segment, every level)

```markdown
### Segment [N]: [name — who, where, buying what]

- **Universe:** [count of potential customers] — [URL, date, label]
- **Bottom-up math:** [units x price x frequency, shown]
- **TAM contribution:** [currency + customer count]
- **SAM filter:** [what makes them serviceable by us — rate + why]
- **SOM logic:** [3-5 yr capture, benchmarked to comparable: name,
  URL]
- **Range:** [low - high, and what drives the spread]
- **Weakest input:** [the number most likely wrong, flagged]
- **Labels:** [each major input: Fact / Inference / Assumption]
```

## Level 0 — Unseasoned (works today)

```
/goal Build a TAM/SAM/SOM analysis for [product] in [geography], bottom-up, with citations for every major data point.
```

You'll get a model. You won't see which segment carries the weight,
which input is doing the most work, or where one assumption leaked
across all of them.

## Level 1 — Loop Lingo (the sizing contract)

```
/goal Build a defensible TAM/SAM/SOM for [product] in [geography] —
each segment sized bottom-up in the Segment Sizing Format, gated by
me, rolled up only when all segments settle.

Base camp (calculate once):
- Product/service and delivery model: [fill]
- Target buyer and secondary audience: [fill]
- Pricing anchor: [fill, or "benchmark it"]
- Governing criterion: speed and defensibility over perfection.

Index before you size (build once; this is the loop bound):
1. List the segments — distinct buyer x geography x need
  combinations, 3-6 of them, one line each. (If a market landscape
  scan is in session, use its segmentation.)
2. Note per segment: likely data sources, and whether a pricing
  anchor exists.
3. I approve the segment list before any sizing. The approved list
  is frozen — discoveries mid-loop go to a parking note.

/loop One segment per turn.

For each segment:
1. Cheap checks: is the segment distinct (no double-counting with a
   sibling)? Is there any anchor data at all? If not, flag and ask
   before burning research on it.
2. Size it bottom-up in the Segment Sizing Format — its OWN inputs,
   never reusing another segment's price or adoption rate without
   saying so.
3. Ask me: "Modify, or continue to [next segment]?" Wait.
4. On approval, compact: carry the segment's contribution and its
   weakest input forward.

Roll-up (only after all segments settle):
- TAM / SAM / SOM totals with the per-segment table
- Sensitivity: best / base / worst, and which segment's weakest
  input moves the total most
- Sources section with every URL
```

## Level 2 — Just Enough Jinja2 (the routine form)

```jinja2
{% set routine_version = "market-sizing-loop-v1.0" %}

{% for segment in approved_segments %}
## Size segment {{ loop.index }} of {{ approved_segments | length }}:
{{ segment.name }}

Cheap checks: distinct from siblings (no double-count)? anchor data
exists? If either fails, flag and ask before researching.

Render the Segment Sizing Format:

### Segment {{ loop.index }}: {{ segment.name }}
- **Universe:** [count] — [URL, date, label]
- **Bottom-up math:** [shown]
- **TAM contribution:** [amount + count]
- **SAM filter:** [rate + why]
- **SOM logic:** [capture + comparable, URL]
- **Range:** [low - high, driver]
- **Weakest input:** [flagged]
- **Labels:** [per input]

Ask "Modify, or continue?" and wait before the next segment.
{% else %}
STOP: no approved segment list. Build and approve the index first.
{% endfor %}

## Roll-up (all segments settled)
- TAM / SAM / SOM totals + per-segment table
- Best / base / worst, naming the input that moves the total most
- Sources: every URL used

Generated by {{ routine_version }} over
{{ approved_segments | length }} segments.
```

## Final Step

Offer exactly 4 next options:
1. Pressure-test the segment whose weakest input moves the total
   most (Recommended)
2. Re-run one segment with a different pricing anchor
3. Convert the roll-up into a one-slide executive summary
4. Feed the biggest segment into an Ansoff growth-options analysis

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a
custom path.
