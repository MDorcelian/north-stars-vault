---
name: Trello Access
type: credential-gap
status: open
grade: G1
updated: 2026-08-01
sources: [G1 - verified 2026-08-01]
related: [30-projects/ace-knows-a-guy.md, 60-assets/credential-locations.md]
---

# Trello Access — NOT actually available

Verified 2026-08-01: North Stars does NOT have Trello access, despite the genesis doc's Section 5 assuming Trello reads are already possible ("L2, reversible execution: ... Trello reads. Trello writes after his first confirmation that board access is correct").

Checked and confirmed blocked:
- Direct Trello API call to board 6a5319cca50910796e314d4f: "unauthorized permission requested"
- Direct board URL (trello.com/b/6a5319cca50910796e314d4f) via browser: "Sign up to see this board, requires a Trello account"
- No TRELLO_API_KEY or TRELLO_TOKEN anywhere in `~/.hermes/.env` or the vault

To fix: Marvens needs to generate a Trello API key + token (trello.com/power-ups/admin or trello.com/app-key) and add them to `.env` the same way the YouTube key was added. Until then, any task referencing "the Trello board" (candidate cards, the 12-topic ideas list, content rules) cannot be verified or read by North Stars, only what's already logged in the vault from prior manual reports is available.
