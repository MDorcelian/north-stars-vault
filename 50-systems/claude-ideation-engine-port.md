---
name: Claude Ideation Engine Port Spec (claude_ideation_hermes)
type: reference
status: incorporated 2026-08-04
grade: G1 (extracted from live codebase on Marvens' PC)
updated: 2026-08-04
sources: [claude_ideation_hermes.md from Marvens' machine, extracted by Claude Code]
related: [research/youtube-niche-research skill, 30-projects/august-production-shortlist, research/toolchain]
---

# The Ideation Engine — what it is and what's portable into North Stars

FULL PORT SPEC preserved at: ~/.hermes/cache/documents/doc_250d908196d8_claude_ideation_hermes.txt (2552 lines).
This file is the DURABLE INDEX + the decision on what to incorporate.

## What the engine is (one paragraph)
A Node/Express + React app + one SQLite brain that answers "what should this channel make next, with
exact title/thumbnail/script." Core: track competitor channels, compute OUTLIERS (views ÷ subs ≥ 2x),
mine comments + Reddit for demand, bank every view-backed term into a keyword brain, and when asked,
propose ideas crossing a PROVEN LANE with PROVEN EXTERNAL DEMAND, then verify EVERY candidate with a
real YouTube Data API search, OVERWRITE every model-written number with the real API number (the
"truth pass"), drop any idea with no proof video ≥ 100K views, and render a ranked report where every
title word carries a clickable receipt (a real title, a verbatim comment, or a banked keyword).
Anything without a receipt shows as an honest amber "style choice, no data" flag.

## The six hard gates (VERBATIM constants, the non-negotiable quality bars)
- GATE 1 SHORTS_MIN_SECONDS=180 (API proof); 240s SQL SHORTS_EXCLUDE for DB. Shorts never data.
- GATE 2 MIN_LANE_VIEWS=30,000 — a competitor "proven in niche" lane must clear this.
- GATE 3 PROOF_FLOOR=100,000 — an idea with no proof video ≥100K is DROPPED (enforced server-side).
- GATE 4 STRONG_PROOF=500,000 — ≥500K = High/Strong pick; else Medium/Solid bet. "Low" never emitted.
- GATE 5 OUTLIER_MULTIPLIER=2 — views ≥ 2× channel subs = a genuine outlier (the LEAD signal).
- GATE 6 DERIVATIVE_SIMILARITY=0.7 — Sørensen-Dice ≥0.7 vs a proof title = derivative "re-make not remix".
- Plus PHRASE_PROBE_MAX=6 budget gate (≤6 extra phrase searches/report).

## The two-mode framing (the only two acceptable plays)
- proven_rerun — running a proven title/format near-verbatim. FIRST-CLASS wanted output.
- untapped_cross — a proven format on a subject nobody crossed. Newness in the SUBJECT.
- FAILURE MODE = invented phrasing neither re-run nor proven-cross. A straight re-make BEATS an invented title.
- ≤50% of ideas may be proven_rerun; the rest must be untapped_cross (equally evidence-backed).

## opportunity_score (final ranking, deterministic)
```
log10(best_proof_views) + 0.8*log2(1+min(best_proof_multiplier,12)) + 0.3*log2(1+min(lane_multiplier,8))
```
Intent: a 500K outlier beats a 5M mega-channel norm video. The topic earned the views, not the channel.

## Title rules (operator-mandated)
MAIN CLAUSE (before any paren/bracket/dash suffix) ≤ 60 chars (home page rule; parens may overflow).
Summary data: ≤20:3.97M · 21-30:3.26M(-18%) · 31-40:2.75M(-31%) · 41-50:2.08M(-48%) · 51-60:1.70M(-57%)
61-70:1.63M(-59%) · 71-80:1.55M(-61%) · 81-100:1.20M(-70%). Shortest main clause that lands the hook.

## The truth pass (THE single most important thing)
Every model-supplied stat is OVERWRITTEN by video_id from the real API. Unverifiable ids/comments/citations
are stripped. Without this, the system is just a confident-sounding LLM. This is #1 in "what a faithful
reimplementation MUST keep."
Other must-keeps (ranked): outlier multiplier as lead signal; 100K proof floor enforced server-side;
honest unproven flag (never dressed as proven); the phrase probe (topic search proves SUBJECT, never
WORDING); anti-plagiarism guard on swaps; judge title on support AND overlap together; two-mode framing;
stripNumericClaims (numbers only via verified pills); keyword-brain invariant (only view-backed terms bank);
verification REWRITES not tags (VidRush); accounting funnel visibility.

## What is NOT in this engine (facts worth recording so I don't build the wrong thing)
- There is NO file named Ideation_Points anywhere reachable. The "six gates" are the hard-coded constants
  above (ideationReportService.ts). NO vidIQ (only in an unrelated affiliate-links doc). NO separate bot/
  repo — one app + one SQLite brain.
- The SQLite brain (keyword bank, comments, transcripts, feedback history) is the hardest thing to port —
  quality compounds from accumulated data. A fresh North Stars starts cold and must re-accumulate.

## NORTH STARS DECISION (2026-08-04)
Non-negotiable behaviors to adopt in ALL channel ideation/research I do:
1. TRUTH PASS — never present a stat I didn't verify via the YouTube Data API as a fact; overwrite numbers
   with real API values; say when I couldn't verify (G1 vs G3).
2. OUTLIER-FIRST ranking — lead with views÷subs ≥2x, not raw views.
3. 100K proof floor — an idea with no verified proof ≥100K is dropped or clearly flagged as unproven.
4. HONEST 'unproven' flag — flag any title/phrase with no evidence visibly; never dress it up.
5. 60-char main-clause title rule with the length↔views data.
6. Two-mode framing (proven_rerun / untapped_cross) + ≤50% re-runs.
7. Phrase-probe mindset — a topic proof ≠ wording proof; cross-niche phrasing hits are legitimate.
8. Anti-plagiarism guard — never let a "fix the wording" produce a near-verbatim copy of an existing title.
9. Keyword brain invariant — only bank terms a real video's views put there; Reddit trends never banked.
10. Report length discipline: ideation briefs concise; every claim cites a receipt or is flagged honest.

Constraint honesty: I run on deepseek-v4 (openrouter), not Opus; I have the YouTube Data API key + yt-dlp
(sub counts via channels.list are available = Gate 5 works). Web search needs the DuckDuckGo/crawl4ai
fallbacks. Vision thumbnail pass needs a multimodal path or is approximated. Full engine parity would need
the SQLite brain + Opus + a retained-source web tool; the METHODOLOGY is portable now.
