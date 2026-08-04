---
name: Google Workspace access (Docs/Drive/Sheets)
type: system
status: LIVE 2026-08-04
grade: G1 (verified, working)
updated: 2026-08-04
related: [40-people/joshua-a.md, 30-projects/ace-knows-a-guy.md]
---

# Google Workspace Access (North Stars)

## Status: WORKING
North Stars can now create, read, append, and share Google Docs / Drive files / Sheets for Marvens,
authenticated as the workspace account gprestigue@gmail.com. Verified end-to-end 08-04 (created a
doc, read it back, trashed a test doc, confirmed the real brief doc).

## Deliberately MINIMAL scope grant (least privilege)
Authorized scopes: Google Drive, Google Docs, Google Sheets ONLY.
Intentionally NOT granted: gmail, calendar, contacts. The setup script warns "missing 5 scopes" on
every check-live because it expects the full set; that warning is EXPECTED and correct (we narrowed
the grant on purpose). Do not "fix" it by re-authorizing full scope — keep least-privilege.

## Account decision (Marvens 08-04)
Docs owned by gprestigue@gmail.com (his main workspace). AceKnowsAGuy@gmail.com is deliberately an
ISOLATED, separate environment for the ACE channel, kept clean, NOT used for North Stars doc tooling.
Do not cross them.

## Tooling
- Setup: ~/.hermes/skills/productivity/google-workspace/scripts/setup.py
- API: GAPI="python3 ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/google_api.py"
- Creds: ~/.hermes/google_client_secret.json + ~/.hermes/google_token.json (auto-refresh)
- Commands: $GAPI docs create/get/append; $GAPI drive search/share/upload/delete; $GAPI sheets create/get/update
- Share: $GAPI drive share FILE_ID --email person@ --role writer/reader [--notify]

## Deliverable convention (Marvens 08-04)
- Docs must be NICELY FORMATTED, not plain-text blobs. Use the gdoc_format.py method: headings (HEADING_2 for sections), bold on key labels/rules, clean structure, no raw `**` or `[UNCONFIRMED]` artifacts in the doc body.
- Docs are shared INSTANTLY as anyone-with-the-link, and the shareable link is given to Marvens. Default role = writer (editable by the recipient/self). Set via Drive permissions {role: writer, type: anyone}.
- Formatter tool: /tmp/gdoc_format.py (builds via Docs batchUpdate + Drive share). Reusable pattern for ALL deliverables.

## FIRST DELIVERABLE (08-04, FORMATTED + SHARED)
Document: "ACE KNOWS A GUY — First Video Scope: Every GTA 6 Gang Explained" (v2, formatted)
Docs ID: 1QAnu5Q8s90wjatEdfFiCuGgmdp38cD5vYADzTAGCd6Y
Shareable link: https://docs.google.com/document/d/1QAnu5Q8s90wjatEdfFiCuGgmdp38cD5vYADzTAGCd6Y/edit
Share: anyone-with-link, WRITER. Owned by gprestigue@gmail.com. Verified clean (no ** artifacts, sections present).
The earlier plain-text brief doc (1vdtx5l_89twKKeHix1na2W9dDBHf28ZjwoLym_T0S0Y) was trashed as superseded.
Test doc (1zymow-KWTRds_ocRR-1_AD4VYVrc7_zu_l7AVH9ewTM) also trashed during verification.

## Notes
- NEVER create/share/delete docs or send without confirming with Marvens first (show recipients/content).
- The brief is owned by gprestigue@gmail.com; sharing it with Joshua is a separate explicit action.
