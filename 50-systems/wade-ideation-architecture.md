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
