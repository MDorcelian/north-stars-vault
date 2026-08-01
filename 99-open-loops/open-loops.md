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
- Emanuele Fathom session transcript: RECEIVED and processed 2026-08-01. Full SOP in 50-systems/hiring-and-team-management.md, source outline doc in 50-systems/group-coaching-agenda-07-31.md (Google Doc, extracted via direct export endpoint).
- WizofYT/@wizofYT channel: PARTIALLY DONE 2026-08-01 via yt-dlp. Channel stats + 13 recent video titles/views/durations pulled, see 40-people/coaching-and-advisors.md. STILL BLOCKED on transcripts/thumbnails (YouTube bot-check wall); needs authenticated browser cookies, Marvens' suggestion to install Firefox and export real cookies not yet done.
- Aditya Mittal ("Strange Mindset") CM candidate: NEW 2026-08-01, portfolio verified via Playwright (30 verified clients, 402M views, strong reviews). Awaiting Marvens' decision on next step (recommend: GTA-specific writing sample test). See 40-people/aditya-mittal-strange-mindset.md.
- Research toolchain: yt-dlp (channel/video listing), Playwright+Chromium (general page rendering), and the Google Docs direct-export endpoint are now working workarounds, documented in 50-systems/research-toolchain-notes.md. Attempted `web.extract_backend` -> firecrawl but no FIRECRAWL_API_KEY exists in .env yet, so it's not actually active; the workarounds cover real usage in the meantime. If a proper extract backend key becomes available, this should be revisited.

## CLOSED / CORRECTED 2026-08-01
- "Trevor" CM candidate: discarded, not a real identity, gave a fake name during GTA 6 screening. Not an open loop, not a real person to track. See 40-people/cm-candidates.md.
- "WizofYT/Andrew session" as a scheduled meeting: does not exist. Andrew's coaching is a paid $4,500/2mo ($9K total) program, not a 1-on-1 call. Old-agent confusion with the Friday WannerCashCow group call. See 40-people/coaching-and-advisors.md.
- "Emanuele hiring session, date TBD": WRONG, the session already happened (Fathom recording exists). Removed as a scheduling loop; see the Fathom-extraction loop above instead.
- All 15 CONFLICTS.md items (see CONFLICTS.md for full list, entity map, income target, explainerguy01 role/subs, funnel truth, Ace persona, VideoVault, etc).
- Gateway verified running as system-level systemd service.
- Vault git remote confirmed in sync (GitHub push working).

## SUPERSEDED
- "GTA 6 Explained launch ~07-25" [A] replaced by the CM-first decision on 07-26 [H]; launch now blocked on the CM hire.
