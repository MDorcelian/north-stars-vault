---
name: Claude Code setup (future work)
type: system
status: deferred (do later)
created: 2026-08-04
updated: 2026-08-04
related: [50-systems/claude-ideation-engine-port.md, brains/north_stars_brain.py]
---

# Claude Code setup on the servers — deferred pre-work notes

## Context
Marvens wants North Stars "on Claude Code" for full engine parity (Opus + vision + retained web
sources) with its own database. The native SQLite evidence brain (brains/north_stars_brain.py + .db)
already gives North Stars its own accumulating database TODAY with no Claude Code dependency. Full
Claude Code parity is a LATER enhancement; the database is done now.

## Blocker on the DIGITALOCEAN droplet (root@agents-...nyc1)
Error observed on that droplet:
- `claude: command not found`
- `pip3 install claude` → PEP 668 externally-managed-environment error.
Cause: claude-code is an npm package, NOT a pip package, and the droplet's pip is system/PEP-668-locked.

## Correct install path (do NOT use pip)
```bash
# Node is required; install claude-code globally via npm
npm install -g @anthropic-ai/claude-code
# then authenticate (needs a valid ANTHROPIC_API_KEY or browser login)
claude auth login        # or: export ANTHROPIC_API_KEY=... ; claude
```
Alternative on a PEP-668 host without node: use a venv or pipx, but npm global is the canonical path
for claude-code specifically.

## Current machine (this one, /home/hermes)
- claude-code IS installed (v2.1.220) via npm at ~/.local/bin/claude.
- BUT auth fails: ANTHROPIC_API_KEY in ~/.hermes/.env is BLANK (zero-length), and no claude auth login
  has been done. So claude -p returns "Not logged in · Please run /login".
- This machine runs on OpenRouter (deepseek-v4), which claude-code won't use without a valid Anthropic
  key.

## To enable Claude Code parity later (checklist)
1. Provide a valid ANTHROPIC_API_KEY (or run `claude auth login`) on the target machine.
2. Install claude-code via `npm install -g @anthropic-ai/claude-code` (not pip).
3. Port the actual engine source from Marvens' PC (C:\Users\MarvensD\Desktop\YouTube Comment
   Checker\claude_code_ideator\) if we want the app itself; otherwise North Stars' native brain +
   youtube-ideation-engine skill already capture the METHODOLOGY.
4. Cost note: full parity uses Opus tokens + a vision pass; the native approach burns no Claude budget.

## Decision
Proceed with the native evidence brain (DONE 08-04). Claude Code parity is optional future work;
revisit only if the native brain + skills prove insufficient.
