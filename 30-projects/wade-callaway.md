---
name: wade-callaway
type: project
status: active
channel: Wade Callaway (AI-avatar farm channel)
updated: 2026-08-13
related: [16-people/diana-wade.md, 30-projects/ace-knows-a-guy.md]
---

# Wade Callaway — Proof-First Thumbnail System (logged 08-11)

## The system (established 08-11)
- Cards on the High Priority Ideas list carry a **[VIRAL REF Nx]** thumbnail attachment = the proven
  viral thumbnail template in that exact topic for Diana to copy/adapt, with the outlier multiplier in the
  name so its strength is visible.
- **Proof-first ranking (Marvens rule, 08-11):** an idea WITH a genuinely viral thumbnail reference
  (outlier >= 2x in the correct niche) is more likely to succeed than one without. PROVEN (>=2x) =
  high priority, top of list by outlier strength. NO-REF and WEAK/BAD-ref (<2x or wrong-niche) = no
  proof = bottom of list. Never ship a no-proof idea while proven ideas remain. Refresh daily means few
  ideas are needed, so only ship what has proof.

## Hard filters (wade_viral_ref.py, v2)
- NEVER use Shorts (drops videos under ~200s).
- Outlier floor: views/subs >= 2.0 (0.1x/0.43x/1.09x are NOT viral, rejected).
- Topic relevance gate: title/channel must contain a known farm/animal term (drops wrong-niche picks
  like a personal-development video landing on a hay card).
- Attachment-only (cover cleared, NO color banner). Re-run replaces old refs.
- Search is NON-DETERMINISTIC/rate-limited: some topics return no clean ref on a given run; a no-find
  card stays no-proof and sinks. Manually clean stale bad refs when detected.

## Universal Thumbnail Combiner Prompt (delivered 08-11)
- Purpose: Diana formerly made thumbnails from only Wade's portrait + title. New method = take the
  viral REFERENCE + the Wade AI AVATAR, combine them via prompt. Keeps reference's proven layout/
  contrast/hook, places Wade as the channel face (identical glasses/plaid/weathered look), applies
  truthful 3-6 word dollar hook + barn-red/khaki/cream palette. Outputs 6-point written design spec.
- DOC: https://docs.google.com/document/d/1q65Tr_9H0UZDEBW0Ar8TsuybKZvI_DLBYn5ipQaXDMc/edit (definitive v2)

## How Diana uses it (simple)
1. Open the card's [VIRAL REF] attachment (the reference).
2. Take that reference + Wade's avatar image into the combiner prompt.
3. It gives back one thumbnail (and a design spec).

- Niche Watch list created on the board (08-11) for competitor-format models.
  - Gould Dunlap (https://www.youtube.com/@goulddunlap9864, UC_kTpc6yrFRz6JFleB8r8xQ): sibling
    "hidden value" format in antiques niche. 4,090 subs, 5 videos in one week, 320K views, top outlier
    49.64x (rusty cast iron pans). Thumbnail formula logged in skill. Transferable mechanics only, not topic.
- Scripts
- ~/.hermes/scripts/wade_viral_ref.py — attach viral ref to a card (link in title), attachment-only.
- ~/.hermes/scripts/wade_curate.py — lists High Priority queue with PROOF STATUS per card + ranking rule.
- Cron "Wade High-Priority Idea Curator" (45 10 * * *) re-orders the list by proof daily + attaches refs
  to no-ref cards. Owner boundaries: only High Priority Ideas list; never Diana's workflow lists.


## Daily Evidence + Reasoning Sweep (built 08-11)
- Cron "Wade Evidence + Reasoning Sweep" (30 8 * * *) -> runs wade_evidence_sweep.py, writes channels/
  videos/view-snapshots to ~/.hermes/brains/north_stars_brain.db, emits conclusion-form reasoning notes.
  Fires BEFORE the 11:00 daily brief so the brief sees fresh evidence. Watchlist FIXED for clean velocity.
- Watchlist (6 competitors): Gould Dunlap, Down On The Farm, Rational Ranchers, Harvest Machine,
  Substructure, Farm Secrets.
- Niche Watch list on board: Gould Dunlap, Harvest Machine, Substructure, Farm Secrets cards added (08-11).

## BRAIN RECOVERY (08-11) — caution flag
The brain DB (~/.hermes/brains/north_stars_brain.db) was accidentally DELETED at ~21:01 during a sweep
test (careless rm). Rebuilt via seed_brain.py (schema + live channels restored; Free App master 33.87x
intact) + re-added hand-banked Web Browser P1 (671K) + farm sweep. LESSON: NEVER rm the brain; it is NOT
in git and is not recoverable from a backup. Seed then re-sweep is the rebuild path.
