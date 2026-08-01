---
name: Credential Locations
type: system
status: active
grade: G1 (verified on disk 2026-08-01)
updated: 2026-08-01
sources: [G1]
related: [CONFLICTS.md]
---

# Credential Locations

Values never stored here, per genesis Section 2. Locations only.

- Anthropic API: `~/.hermes/.env` (ANTHROPIC_API_KEY / ANTHROPIC_TOKEN)
- Discord bot token: `~/.hermes/.env` (DISCORD_BOT_TOKEN)
- Brave Search: `~/.hermes/.env` (BRAVE_SEARCH_API_KEY)
- YouTube Data API key: `~/.hermes/.env` (YOUTUBE_API_KEY), added 2026-08-01. Pasted into this Discord chat by Marvens before being moved here; flagged for possible rotation since it briefly lived in chat logs (same exposure class as the original 2026-07-28/29 incident). Awaiting his call on whether to rotate again.
- FAL image-gen key: not yet located/confirmed. Still on the credential-rotation open loop from genesis Section 2.

Standing reminder: chat is not key storage, even DMs. New keys go straight into `.env`, never pasted here again.
