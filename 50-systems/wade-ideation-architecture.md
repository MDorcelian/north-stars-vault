# Wade Callaway — Ideation Backend Architecture (authoritative, 08-21)

Four-layer evidence-driven ideation engine. An idea is not shipped unless it is proof-backed AND
thumbnail-backed; noise is trashed daily.

## Layer 1 — Evidence Brain (north_stars_brain.db)
- format_patterns: cross-niche proven formats. Each = trigger (psych why it clicks), structure (how to build),
  cross_niche_evidence, proof_multipliers, THUMBNAIL recipe. Top: hidden_real_numbers(106x), free_input_hack(56.7x),
  x_vs_y(52.9x), things_trade_dont_tell(51.7x), salary_replace(34.9x), every_x_explained, economics_of_owning,
  heritage_hidden_knowledge, elder_trust_product.
- proof_tiles: per-topic proof videos (views + multiplier) used to gate idea momentum.

## Layer 2 — Daily automated sweeps (cron stack, all before 11:00 UTC daily brief)
- 08:30 Evidence + Reasoning Sweep (deep-think: format proof vs noise)
- 09:45 Channel Discovery + Decay scan (find NEW growing channels, flag stale ones = 'find it 60 days earlier' edge)
- 10:00 Niche + Channel Daily Awareness
- 10:30 Comment Demand Signal ('am I too late / should I rip it out' = product signal)
- 10:45 High-Priority Idea Curator
- 10:50 Clean-handle reminder

## Layer 3 — Ideation gates (an idea is eligible ONLY if ALL pass)
1. Has a proof tile (real viral video >=100K w/ multiplier; NEVER Shorts)
2. Reference origin verified developed/non-3rd-world (rule: no India/Nigeria/etc.) — a 3rd-world ref distorts the
   real-numbers baseline for a US/developed audience, pass regardless of multiplier.
3. Maps to a proven format_pattern WITH a real THUMBNAIL REFERENCE (an actual image attached to the card, not a
   text comment).
4. No proper thumbnail reference => the card is ARCHIVED (Marvens rule 08-21). Never attach unverified refs.

## PREFERENCE RULE — low-duration-viral-expansion (Marvens strategy, 08-21)
A proof video that is LOW-SUB channel + LOW DURATION (2-7 min, NOT a Short) + HIGH OUTLIER is a strong signal
that the TOPIC is bubbling on its own, independent of a big channel's length. These are prime candidates to be
made into a LONGER video (the short hit proves the topic; we expand it to our 8-15 min format).
- Duration is now recorded on every proof_tile (duration_s column, seconds).
- USE: when ranking idea candidates, a proof that is low-sub + low-duration (<=420s, >=120s so not a Short) +
  high-outlier gets a PRIORITY BOOST over a comparable idea whose proof is long/high-sub.
- OVERRIDE RULE: "These can take priority over best ideas if already best idea AND original timestamp is low
  duration. Otherwise these are limited to the videos available to us." => A low-duration low-sub outlier ONLY
  jumps the queue when the idea is ALREADY a best/top idea AND its proof is low-duration. It does not displace
  a clearly stronger best-idea that lacks a low-duration proof; it is limited to the pool of videos we already
  have access to (no forced category to find new low-duration proofs).

## Layer 4 — Trello pipeline (output)
High Priority Ideas -> Scripting -> Scripts Need Approval -> Scripts Approved -> Video Generated -> Uploaded.
Only proof+thumb backed cards survive; weak/ref-less cards archived.

## The loop
daily sweeps feed new evidence -> brain banks format proofs / discards noise -> proven formats become idea cards
-> cards only move if real proof + real thumbnail -> once channel has views, its own data picks the format to
double down on (Lillie/Every model: one format pops, then you rotate the subject within it).

## Product/monetization layer (added 08-21, TubeLab validation)
Elder-trust persona + honest real-numbers + cheap ultra-specific manual/calendar ($29-47) at ~0.025% conversion =
meaningful monthly revenue ON TOP of ads. Wade product candidate: evergreen zone-based farm monthly calendar
(plant/feed/breed + frost dates), NO year-date (keeps it near-zero-maintenance). Comment qualify-questions = product signal.

## MARKET STRATEGY LAYER (added 08-21 — Jake Trinder's Views-to-Clients method, source of the CSVs)
These frameworks upgrade how we JUDGE ideas and set strategy, sourced from the client-strategy methodology
that produced the reverse-engineering research dumps. Marvens logs this as his foundational strategy doctrine.

### 1. God Mode = foundational YouTube research FIRST
Do broad cross-niche YouTube research BEFORE niche research (avoids confirmation bias + conventional thinking).
Continuously: collect outliers + patterns-between-outliers (formats) + trends, and study WHY each won/lost
(the "why did that work / why did that make it work" drill). Our daily sweeps ARE this. God Mode wanted-state =
an omniscient, always-fresh sense of what works across all of YouTube.

### 2. Market Sophistication Theory (Eugene Schwartz, 5 levels)
The ladder of increasing audience awareness/saturation:
 L1 introduce a new mechanism (iPhone touchscreen) -> L2 enhance it -> L3 add benefits -> L4 bolder claims/story
 -> L5 innovate past saturation (Tesla). OUT-SOPHISTICATE the current level of your niche to break through.
 Application to Wade: farm real-numbers content is low-maturity in this market (few creators, big demand), so
 we often sit at L1-L3 (educate on the real mechanism = the real cost / the real income). As the niche catches
 up, keep out-sophisticating (claims, storytelling, vaulting gaps).

### 3. View Ceiling vs View Floor + 75/25 split for small/new channels
- View ceiling = max of your target market the packaging can attract. View floor = min you'd expect.
- Goal: raise floor toward ceiling AND raise ceiling; idea with high floor + high ceiling = "banger."
- For a NEW/SMALL channel: go 75% prioritizing VIEW FLOOR (high-certainty) + 25% VIEW CEILING (risky upside).
- This formalizes Wade's queue: most cards should be high-floor (proven formats), a few high-ceiling risks.

### 4. Demon Mode — kill your ideas before you ship
After ideating (God Mode = see green), switch to Demon Mode (see red): poke holes, find points of failure,
build each idea back stronger, or abandon it. Our archive-on-no-ref gate is a crude version; the full loop is
"identify cracks -> fix -> repeat -> unbreakable or dead". Apply at every card before it ships.

### 5. Stacking Rocks framework
A "rock" = any element (title format, thumbnail, topic, trend, length, style) that pushes a video toward
success (positive rock, left) or failure (negative rock, right). Rocks have different weights. A video wins
when positive weight > negative weight. Note: a rock that worked elsewhere can be weightless or negative here,
and a heavyweight topic alone can outweight everything else. Use as a per-card checklist: stack positive rocks,
eliminate negatives, honesty on the weight.

### 6. Content gap = demand with no supply
An audience wants a type of video that isn't being supplied. Biggest B2B/product-gap: youtube education is
growing (1.3B learners, 27% YoY) but supply is thin (5-10% serious creators). Content gaps in Wade's farm lane =
the "underserved angle not topic" we identified. Find = study top performers, spot what they're NOT doing
(underrepresented topics, underused formats, underserved segments), then win the gap.

### Research-collection standard (how to log analysis)
Per data point (video), record via the multi-lens breakdown seen in the CSVs: Format (why it worked),
Topic (why the topic won/lost), Thumbnail (why it worked/failed), Execution traits (why retained/missed).
Record the WHY at each level, not just the WHAT. Log into Trello cards with the video link + screenshot +
analysis in the notes (matches existing WR directive).
