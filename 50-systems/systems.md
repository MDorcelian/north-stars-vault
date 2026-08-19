---
name: Systems and SOPs
type: system
status: active
grade: mixed (see inline tags)
updated: 2026-07-29
sources: [C, A, T]
related: [90-voice/voice.md, CONFLICTS.md]
---

# Systems (essentials; full SOPs in /seed/ files)

## Script revision SOP
Fact-check volatile claims BEFORE notes; categorized revision notes; ranked cuts in the scissors sandwich format with word savings quantified; per-item approve/reject, "Keep" is permanent; 2 to 4 passes; never remove or combine sections; never re-propose a rejected item [C].

## Word-count reality
2,300 ceiling is aspiration; the working floor for 10-section scripts is 2,800 to 3,000 at 130 wpm; never trust a script footer count, always recount [C]. See CONFLICTS.md #16 on which number the standing brief should state.

## Outro chain-link
Rank by outlier score AND topical adjacency; never the top outlier if it is a topical cold start; published targets only [C].

## Idea modes
proven_rerun or untapped_cross, nothing in between; at most half a report may be reruns; reject phrase swaps that push title similarity to >= 0.7 Dice [A].

## Niche validation (5 gates)
New channels getting traction, multi-video consistency, < 10 dominant exact-format players, copycat validation, plausible $5K to $10K/mo path. YouTube search demand: 2 to 3 views/hour healthy, < 0.1 move on [T].

## Freelancer hiring heuristics (education material, G3)
Editors $3 to $5/min, scripts ~$20, thumbs $10 to $15, VO $20 to $30; attention-check line in every job post [T].

## Nexlev hard-won settings
search_videos with channelId + sortBy viewCount for catalogs; isExactMatch true; empty outlier query at 1.5x threshold means consistency, not failure [C].

## Quota discipline
Uploads playlist trick (1 unit) instead of search (100 units); 10K daily units global across workspaces [A].


## STRATEGY UPDATE (08-11) — SHORT-FIRST, THEN EXTEND, ALL CHANNELS
CHANNEL STRATEGY CHANGED (applies to ALL channels: Explainer Chris, Wade, Ace, etc.):
Start SHORT to gain an audience first (like the Ace 8-10min scripts Joshua delivers), then increase
video length over time as the audience grows. Modern/pre-launch phase = shorter videos to build
audience + algorithmic discoverability; lengthen later to keep the audience.
RATIONALE: WizofYT + multiple strategists recommend short-first for audience growth, then increase.
Honest tension: RedSignal thesis (longer + faster = dominance) was REAL but earned on an already-
established channel WITH an audience. Short-first is the audience-BUILDING phase; length is the
audience-KEEPING phase. Not conflicting, sequenced.
CAVEAT/ACTION: define the "we've built an audience" switch trigger deliberately (subs threshold,
retention bar, or cadence held N weeks), so lengthen-time is data-driven not vibes. Voice/integrity
standard stays constant across short and long.


## X (TWITTER) API CONNECTED — READ-ONLY (08-19, verified live)
xurl installed at /usr/local/bin. App `n0rthstar` registered + default (client id QnV4clJq...). Working bot credentials in ~/.hermes/.env (X_CONSUMER_KEY/SECRET, X_BEARER_TOKEN, X_CLIENT_ID, X_APP, X_HANDLE). Handle @jiggywastaken.
VERIFIED LIVE: `xurl --app n0rthstar --auth app '/2/users/by/username/jiggywastaken'` returns profile (7,454 followers); `xurl search` returns real posts. App-only bearer auth works; no OAuth browser freeze needed for reads.
READ-ONLY ONLY. OAuth2 user-context (posting/reply/timeline/like) NOT configured — needs interactive browser login on a machine with a browser. Deferred until Jiggy wants to post from X.
PITFALL (hit this session): `xurl auth oauth2 --app n0rthstar jiggywastaken` FREEZES on the headless VPS (no browser, waits for localhost:8080 callback). Do NOT run it on the server. Use `xurl auth app-only '*bearer*'` for reads. Also: a 401 persisted with the FIRST app because its access tier never let it read; a fresh bot worked immediately. If reads 401, the app access tier (not the token transcription) is usually the cause.
