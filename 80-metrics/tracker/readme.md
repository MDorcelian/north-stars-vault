---
name: tracker
type: system
updated: 2026-08-10
---
# Life Tracker (file-based scaffold)
Private life tracker for checklists, habits, goals, projects, reviews, and read-only life data.
The AGENT is the write interface (natural language + knowledge-base rules); this dir holds the data.

## Structure
- `today.md` — the live "today" checklist
- `habits/` — habit definitions (yaml) + completion logs
- `metrics/` — custom metric definitions + dated observations
- `goals/`, `projects/` — advance refs to 20-goals / 30-projects (no duplication)
- `schema.md` — tracker data semantics + ids
