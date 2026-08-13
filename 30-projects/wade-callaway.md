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

## Scripts
- ~/.hermes/scripts/wade_viral_ref.py — attach viral ref to a card (link in title), attachment-only.
- ~/.hermes/scripts/wade_curate.py — lists High Priority queue with PROOF STATUS per card + ranking rule.
- Cron "Wade High-Priority Idea Curator" (45 10 * * *) re-orders the list by proof daily + attaches refs
  to no-ref cards. Owner boundaries: only High Priority Ideas list; never Diana's workflow lists.
