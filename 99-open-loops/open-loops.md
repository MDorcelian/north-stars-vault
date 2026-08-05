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
- TikTok rename @ace.explainer -> @AceKnowsAGuy: window opens 2026-08-15, hard deadline ~2026-08-28 [D][G2]. Dedicated one-shot reminder cron set for 2026-08-15 7am (job "TikTok Rename Reminder (Aug 15 window)").
- Vincent Bekong delivery ($510 expressions milestone active, nudge sent 08-02) [H][D]. Ace banner is NOT Vincent's scope, Marvens creates it himself (corrected 08-02).
- Upwork CM post deploy decision after 24-48h of Discord monitoring [H][D].
- Subscriptions-management video (teased, never made) [C].
- TikTok appeals from June, outcome unknown [C]. Nudge drafted, awaiting approval: 99-open-loops/tiktok-appeals-outcome.md.
- S-corp election: CLOSED/parked 2026-08-02, Marvens confirmed not necessary yet. No action until revenue justifies it.
- Old-droplet stale Discord channel ID 404s [C].
- Daily reports stopped 06-23, cause unknown [A].
- FAL image-gen key location not yet confirmed (rotation flag still open).
- YouTube API key: added to .env 2026-08-01, briefly pasted in this Discord chat before being moved; awaiting his call on whether to rotate once more.
- Emanuele Fathom session transcript: RECEIVED and processed 2026-08-01. Full SOP in 50-systems/hiring-and-team-management.md, source outline doc in 50-systems/group-coaching-agenda-07-31.md (Google Doc, extracted via direct export endpoint).
- WizofYT/Andrew $9k coaching: INTEREST is real, but Marvens is WAITING ON A STRONG MONTH (enough to pay Andrew + bills + invest + implement his ideas comfortably) before committing. Not a yes/no now; track as waiting-on-good-month, do not push for a decision until that clears. See 40-people/coaching-and-advisors.md (channel data + context there).
- Aditya Mittal ("Strange Mindset") CM candidate: test brief SENT 2026-08-02, topic "Every GTA 6 Gang Explained," Ace voice with approved card-flip cold open. Awaiting his sample outline. See 40-people/aditya-mittal-strange-mindset.md and 99-open-loops/aditya-mittal-test-brief.md.
- Trello board access: RESOLVED 2026-08-02, key + token added to .env, board "AceKnowsAGuy" confirmed readable via API. Live board contents synced in 30-projects/trello-board-sync.md. Writes to the board are possible but gated per genesis L2 rule (writes only after Marvens confirms board access is correct). See 60-assets/trello-access-gap.md (now a historical record).
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


## [PRIORITY] Hire a Channel Manager for Explainer Chris (Marvens 08-04, ASAP)
Marvens made this an explicit priority: get a channel manager for Explainer Chris, not necessarily right now but ASAP.
CONTEXT: Explainer Chris is the active, monetized income channel (52K subs, Free App franchise 1.7M). Unlike Ace's CM (Joshua, Option C per-deliverable), EC's main channel runs mostly OUTSIDE North Stars (Trello-visible, Discord/Upwork-elsewhere; GetPoppy pipeline with Maryam scriptwriter, Izi thumbs, etc). A CM here would own the EC production loop end to end.
HONEST TAKE (North Stars): Yes, this is the highest-leverage untapped hire. EC already generates revenue and has a real team + pipeline; a CM who owns it end to end (idea to upload, keeps cadence, drives the franchise lean + Free App plan) directly grows the $/month, and this is the channel whose performance feeds the $10k combined coaching bar. It's a bigger deal than Ace's pre-launch CM because the money is already flowing there.
OPEN ITEMS to decide when pursued (ASAP but not tonight):
- Same CM as Ace (Joshua) vs a separate EC CM? Earlier noted: if Joshua also does EC, clarify retainer stacking.
- Budget / structure: EC has revenue, could justify a management retainer more than Ace's pre-launch could.
- Who: source candidates fresh, or consider Joshua / existing EC team member (Maryam, Joshua Galadima)?
STATUS: priority logged 08-04, not urgent-aggressive, plan to actively pursue soon.


## [DONE] Separate Wise for Royalty Media (created 08-05)
Marvens created a separate/dedicated Wise account for ROYALTY MEDIA, isolated from the Main Wise used
for contractor payments (Joshua's $ was paid via Main Wise). Clean business money separation. If not
yet done, note which email/entity owns the Royalty Media Wise for the record.
