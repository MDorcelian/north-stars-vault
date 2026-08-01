---
name: Assets (where things live)
type: system
status: active
grade: mixed (see inline tags)
updated: 2026-07-29
sources: [A, H, C]
related: [99-open-loops, CONFLICTS.md]
---

# Assets (where things live; locations only, never credential values)

## Windows desktop
C:\Users\MarvensD\Desktop\YouTube Comment Checker: the ideator app + its SQLite system of record (2,911 videos, 7,405 comments, 131 keyword-bank terms, 18 ideation reports), the comment ranker, clipper, scraper, ~30 comment exports, Claude Code memory.

No backup exists beyond one local pre-migration DB copy. This machine is a single point of failure. Raise a backup plan in week one [A]. See onboarding interview: approve a backup plan.

## Old droplet
/home/hermes/vault (61 notes, now in 00-inbox/legacy-vault/), ~/.hermes/memory, session exports via `hermes sessions export --format md` [H].

## Claude account
24+ project conversations, project files, full archive export via Settings -> Privacy -> Export data [C]. Two derived assets possibly lost to ephemeral session folders: MASTER_REVISION_GUIDE.md and the nurture sequence file. Verify with him (open loop).

## Nexlev
FREE plan; personal analytics tools return ACCESS DENIED; public-data tools work [A]. No tool anywhere reaches YouTube Studio analytics (RPM, retention, traffic sources). That is the operation's biggest data blind spot [A][C].

## Keyword bank top proofs (2026-07-29)
"is michael worse than trevor gta 5" 6.9M; "gta vice city unsolved mysteries" 5.3M; "most disturbing deaths in gta" 4.2M; "what happened to vic vance" 2.7M [A].

## Credential flags (see genesis Section 2, act on first message)
YouTube Data API key was pasted in plaintext into old Discord DMs on 2026-07-28/29, exposed in exported logs. Recommend rotation at console.cloud.google.com. Same check for the FAL image-gen key pasted earlier.
