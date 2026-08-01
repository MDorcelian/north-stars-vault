---
name: Open Loops
type: tracker
status: active
grade: mixed
updated: 2026-08-01
sources: [H, D, G2]
related: [CONFLICTS.md, 30-projects/, 40-people/coaching-and-advisors.md]
---

# Open Loops (state as of 2026-08-01)

## OPEN
- TikTok rename @ace.explainer -> @AceKnowsAGuy: window opens 2026-08-15, hard deadline ~2026-08-28 [D][G2].
- Vincent Bekong delivery ($510 expressions milestone active) [H][D]. Nudge drafted, awaiting approval: 99-open-loops/vincent-delivery.md.
- Upwork CM post deploy decision after 24-48h of Discord monitoring [H][D].
- Subscriptions-management video (teased, never made) [C].
- TikTok appeals from June, outcome unknown [C]. Nudge drafted, awaiting approval: 99-open-loops/tiktok-appeals-outcome.md.
- S-corp election exploration, no CPA engaged [C].
- Old-droplet stale Discord channel ID 404s [C].
- Daily reports stopped 06-23, cause unknown [A].
- FAL image-gen key location not yet confirmed (rotation flag still open).
- YouTube API key: added to .env 2026-08-01, briefly pasted in this Discord chat before being moved; awaiting his call on whether to rotate once more.
- Emanuele Fathom session transcript: RECEIVED 2026-08-01, this loop is closed. Full SOP extracted into 50-systems/hiring-and-team-management.md. Still needed: the reference Google Doc from the call (extraction blocked, see below).
- WizofYT/@wizofYT channel: PARTIALLY DONE 2026-08-01 via yt-dlp (installed fresh). Got channel stats + 13 recent video titles/views/durations, all real data, see 40-people/coaching-and-advisors.md. BLOCKED on transcripts and thumbnails: YouTube's bot-check wall stopped yt-dlp from fetching individual video pages/subtitles. Needs either browser cookies or another method if deeper research is wanted.
- Web tool backend limitation: Brave-free cannot extract general page content (Google Docs, most web pages) or run web_search reliably as of 2026-08-01. YouTube specifically is now workable via yt-dlp (installed), but the Google Doc from the coaching call and general web research still need `web.extract_backend` reconfigured to firecrawl/tavily/exa/parallel. Marvens flagged real-content access (channels, transcripts, thumbnails) as important; YouTube channel-level access is now solved, transcript/thumbnail-level access and general page extraction are not.

## CLOSED / CORRECTED 2026-08-01
- "Trevor" CM candidate: discarded, not a real identity, gave a fake name during GTA 6 screening. Not an open loop, not a real person to track. See 40-people/cm-candidates.md.
- "WizofYT/Andrew session" as a scheduled meeting: does not exist. Andrew's coaching is a paid $4,500/2mo ($9K total) program, not a 1-on-1 call. Old-agent confusion with the Friday WannerCashCow group call. See 40-people/coaching-and-advisors.md.
- "Emanuele hiring session, date TBD": WRONG, the session already happened (Fathom recording exists). Removed as a scheduling loop; see the Fathom-extraction loop above instead.
- All 15 CONFLICTS.md items (see CONFLICTS.md for full list, entity map, income target, explainerguy01 role/subs, funnel truth, Ace persona, VideoVault, etc).
- Gateway verified running as system-level systemd service.
- Vault git remote confirmed in sync (GitHub push working).

## SUPERSEDED
- "GTA 6 Explained launch ~07-25" [A] replaced by the CM-first decision on 07-26 [H]; launch now blocked on the CM hire.
