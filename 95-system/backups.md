---
name: backups
type: system
updated: 2026-08-10
---
# Backups & Recovery
The vault is a git repo (remote: github.com/MDorcelian/north-stars-vault.git), pushed on activity.
Local recovery: `git log` / `git checkout` for history. Portable copy: zip of ~/vault or clone of the
remote. NO secrets live in the vault (values in ~/.hermes/.env, referenced by path only), so the repo
is safe to back up without a secret-scan step beyond confirmation.
