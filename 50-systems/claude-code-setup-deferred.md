---
name: Claude Code setup (future work)
type: system
status: deferred (do later)
created: 2026-08-04
updated: 2026-08-04
related: [50-systems/claude-ideation-engine-port.md, brains/north_stars_brain.py]
---

# Claude Code setup on the servers — RESOLVED 2026-08-04

## STATUS: WORKING
Claude Code is authenticated and running on this box as of 08-04. FIX USED: Option 1 (root's OAuth
creds copied to the hermes user), verified via `claude -p` returning real output. AuthMethod
firstParty (Claude Pro, OAuth). The per-user scoping (root vs hermes) was the original blocker,
NOT a broken install.

## How auth was fixed (for reference / if it needs redoing)
- Login was done as `root@agents-...nyc1` via `claude auth login` (claude.ai OAuth, Pro).
- North Stars runs as the `hermes` user, whose ~/.claude did not see root's credentials.
- Fix: `mkdir -p /home/hermes/.claude && cp -r /root/.claude/.credentials.json /home/hermes/.claude/ && chown -R hermes:hermes /home/hermes/.claude`

## Provider/cost note for this box
- ANTHROPIC_API_KEY in ~/.hermes/.env is STILL blank (length 0), but Claude Code uses the OAuth login,
  so it works without a key.
- North Stars itself still runs on OpenRouter (deepseek) for MY normal turns. Claude Code is a SEPARATE
  CLI I can drive via terminal for delegated coding tasks, and it bills to the Claude Pro account.

## What Claude Code gives North Stars now (agent-level capability)
- Ability to run `claude -p "task"` / interactive sessions for delegated coding, automation, and
  agentic work (see claude-code skill + wiki-backed-ops-agent skill).
- Full parity with Marvens' engine (torque: Opus models + vision thumbnail pass + retained web search)
  is now POSSIBLE, since Claude Code can make those calls, but it bills Pro tokens. The native
  evidence brain (brains/north_stars_brain.py) still handles the accumulation cheaply.

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
