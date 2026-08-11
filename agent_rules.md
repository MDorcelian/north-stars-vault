---
name: agent_rules
type: system
status: active
updated: 2026-08-10
purpose: Unify conventions for the North Stars vault as Marvens' durable file-based source of truth
---

# North Stars Vault — Agent Rules (unified knowledge base + life tracker)

This vault is Marvens' authoritative, file-based source of truth. It is a LIVE system (git-backed,
activity daily). Read this file before answering personal questions, storing substantial context, or
updating the tracker.

## Core principles (non-negotiable)
1. FILES are the authoritative detailed record. Model memory is only a router, never the database.
2. Persistent memory stores ONLY the vault path, stable preferences, and retrieval routing.
3. Conversation history is secondary context, never proof of current state.
4. NEVER invent facts to fill empty fields. Use `unknown` / `insufficient data`, never fabricate.
5. Distinguish: fact, self_report, observation, hypothesis, preference.
6. Preserve uncertainty and conflicts instead of silently resolving them.
7. User corrections override summaries; superseded claims stay traceable (never delete, mark superseded).
8. Exact dates when known; explicitly mark date precision (e.g. `~2026-08`, `2026`).
9. `current` summaries answer "what is true now"; dated records answer "what happened and when".
10. Markdown is authoritative. CSV/SQLite/charts/indexes are rebuildable derivatives.
11. Fast capture: one targeted write + one concise ack for routine updates. No over-engineering casual notes.
12. Default to ONE writable copy of any fact (canonical note + links, not multiple editable copies).
13. Lexical search, ids, aliases, tags, dates, one-hop links BEFORE embeddings.
14. NEVER store credentials, passwords, keys, seeds, cookies, recovery codes, payment auth, portal creds.
15. Do not send vault content to third parties without explicit approval.

## Locations & hierarchy
- `00-inbox/` unprocessed material (triage then clear/link)
- `10-identity/` profile, entity map, who's who
- `20-goals/` canonical goals
- `30-projects/` one file per durable project (business + personal)
- `40-people/` one file per durable person
- `50-systems/` process/SOP/tooling/skills references
- `51-email/` email/product operations
- `60-assets/` credential LOCATIONS (paths only, never values), urls, repos
- `70-decisions/` decisions, rationale, resolution archive
- `80-metrics/` life/business metric data + tracker
- `90-voice/` writing voice / copy style
- `99-open-loops/` open items + daily/weekly logs
- `95-system/` (new) schema, changelog, backups, templates
- `20-timeline/` (new) life/event timeline
- `30-health/` `40-nutrition/` `31-habits/` (new) private life domains, kept in clearly marked subdirs

## Personal-life data note (privacy)
Health, nutrition, sleep, weight, and habits are PRIVATE life data. They live in clearly-named
subdirs (30-health, 40-nutrition, 31-habits, 20-timeline). This vault pushes to a git remote, so:
- never commit secrets/credentials anywhere (they live in ~/.hermes/.env, referenced by path only)
- keep personally-sensitive health detail proportionate; note sensitivity in frontmatter
- follow the same capture/retrieval rules as all other domains

## ID prefixes (stable)
`evt-` event / `src-` source / `sym-` symptom / `cond-` condition / `med-` medication / `sup-` supplement
/ `lab-` lab result / `per-` person / `org-` org / `prj-` project / `dec-` decision / `goal-` goal
/ `idea-` idea / `res-` resource / `cmp-` metric / `hbt-` habit / `chk-` checklist

## Retrieval workflow
1. Read this file. 2. Search original files. 3. Read canonical summary. 4. Read newer dated events.
5. Follow source links for consequential claims. 6. Distinguish current/historical/resolved/uncertain/
superseded. 7. State uncertainty + conflicts. 8. Cite note paths + source ids + dates when accuracy
matters. 9. Obey user's requested scope/exclusions literally.
