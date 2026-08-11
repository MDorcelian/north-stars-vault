---
name: schema
type: system
status: active
updated: 2026-08-10
---

# Vault Schema & Provenance

Frontmatter YAML where it improves retrieval. Only include applicable fields.

```yaml
---
type: event | note | source | entity | metric | habit | checklist | decision | project | goal | idea | resource
subtype: health | nutrition | finance | project | personal | business | fitness | sleep | weight | habit | etc
record_status: current | historical | resolved | uncertain | superseded
epistemic: fact | self_report | observation | hypothesis | preference
occurred_at: yyyy-mm-dd        # when it happened
valid_from: yyyy-mm-dd
valid_to: null
recorded_at: yyyy-mm-dd         # when we wrote it
created: yyyy-mm-dd
updated: yyyy-mm-dd
people: []
projects: []
source_ids: []
confidence: high | medium | low
verification: verified | user_reported | unverified
needs_verification: false
supersedes: []
aliases: []
tags: []
---
```

## ID prefixes (stable)
`evt-` event / `src-` source / `sym-` symptom / `cond-` condition / `med-` medication / `sup-` supplement
/ `lab-` lab result / `per-` person / `org-` org / `prj-` project / `dec-` decision / `goal-` goal
/ `idea-` idea / `res-` resource / `cmp-` metric / `hbt-` habit / `chk-` checklist

## Record body pattern
```markdown
# human-readable title
## summary
## details
## evidence and provenance
## connections
## uncertainty and follow-up
```

## Epistemic labels (what is true vs what is said)
- `fact` – verified against a traceable source
- `self_report` – user stated it (trusted but not independently verified)
- `observation` – drawn from data/logs/records
- `hypothesis` – an interpretation, not established
- `preference` – a stable user preference (highest-trust for guiding behavior)

## Source records
A source record includes: origin, author/provider, document or event date, date received, path/url,
extraction status, reliability. Sources live in `90-sources/records/`, originals in `90-sources/files/`.

## Date precision
- Exact date when known: `2026-08-10`
- Approximate: `~2026-08`, `2026`, `~2026-08-0X`. Always say when a date is approximate.

## Correction & supersession
- Never delete superseded claims. Mark old record `record_status: superseded` + `supersedes`/`superseded_by`.
- User correction overrides the summary; the OLD claim stays traceable in the dated note.
