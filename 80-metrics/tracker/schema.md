---
name: tracker_schema
type: system
updated: 2026-08-10
---
# Tracker Data Semantics

## Missing-value semantics (per metric)
- `unknown` (not recorded), `zero` (measured 0), `not_applicable`, `not_scheduled`, `not_completed`
  are DIFFERENT states. Never conflate them.

## Aggregation
- Averages use only valid observations unless the metric definition says otherwise.
- Intermittent metrics: use only recorded measurements; missing days ignored.
- Habit completion: use only SCHEDULED habit days; unscheduled days are not failures.
- Goal progress: derived from success criteria / completed milestones, NOT task volume or elapsed time.
- Project progress: derived from explicit milestones/scope, never fabricated from elapsed time.

## Correlations
- NEVER claim habit/metric/goal correlations prove causation.

## IDs (tracker)
- `hbt-` habit, `cmp-` metric, `chk-` checklist, `obs-yyyymmdd-nnn` observation.

## Completion rule
- Record completion ONLY from explicit user action or reliable evidence. A reminder firing or time
  passing never counts as completion.

## Habits
- Daily, weekly, selected-weekday, interval, and minimum-frequency habits supported.
- Parent habit can contain checkable subtasks.
- Distinguish habit vs temporary checklist vs project task.

## Correction
- Preserve observations/completions/events/status changes for correction without rewriting history.
- After corrections or batches, READ BACK from the data before declaring done.
