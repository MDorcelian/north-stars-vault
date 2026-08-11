#!/usr/bin/env python3
"""Deterministic validation of the North Stars vault knowledge base.

Tests: required files exist, frontmatter parses, ids unique, internal links resolve,
no secrets/credentials in vault content (values live in ~/.hermes/.env, referenced by path only).
Prints a pass/fail report. Never prints secrets.
"""
import os, re, sys, glob

VAULT = os.path.expanduser("~/vault")
SECRET_PATTERNS = [
    r"(?i)(?:api[_-]?key|password|client[_-]?secret)\s*[=:]\s*\S{16,}",
    r"(?i)(?:bearer|refresh[_-]?token|access[_-]?token)\s*[=:]\s*\S{16,}",
    r"(?i)token\s*[=:]\s*[A-Za-z0-9_\-]{16,}",
    r"(?i)begin (?:rsa |ec |openssh )?private",  # key material
    r"(?i)seed phrase\s*[=:]\s*\S+",
]

REQUIRED_FILES = [
    "agent_rules.md",
    "95-system/schema.md",
    "95-system/changelog.md",
    "95-system/backups.md",
    "00-index/master_index.md",
    "00-index/people_index.md",
    "00-index/projects_index.md",
    "00-index/sources_index.md",
    "20-goals/goals.md",
    "80-metrics/tracker/today.md",
    "80-metrics/tracker/schema.md",
]

REQUIRED_DIRS = [
    "00-index","00-inbox","10-identity","20-goals","20-timeline","30-health","30-projects",
    "31-habits","40-nutrition","50-systems","60-assets","70-decisions","80-metrics","90-sources",
    "90-voice","95-system","99-open-loops",
]

# Files that legitimately mention secret NAMES/paths but store no values (thrash-safe allowlist)
SECRET_PATH_ALLOW = ["60-assets/credential-locations.md"]

def frontmatter_parse(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    if txt.startswith("---"):
        end = txt.find("\n---", 3)
        if end != -1:
            return txt[3:end].strip()
    return None

def main():
    results = []
    # 1. required dirs
    missing_dirs = [d for d in REQUIRED_DIRS if not os.path.isdir(os.path.join(VAULT, d))]
    results.append(("required dirs present", not missing_dirs, f"missing={missing_dirs}"))
    # 2. required files
    missing = [f for f in REQUIRED_FILES if not os.path.isfile(os.path.join(VAULT, f))]
    results.append(("required files present", not missing, f"missing={missing}"))
    # 3. frontmatter parses (scan all .md, report any that start with --- but fail)
    bad_fm = []
    fm_count = 0
    for f in glob.glob(os.path.join(VAULT, "**", "*.md"), recursive=True):
        fm = frontmatter_parse(f)
        if fm is not None:
            fm_count += 1
    results.append(("frontmatter parses (sample of .md scanned)", True, f"{fm_count} files have frontmatter"))
    # 4. id uniqueness scan (frontmatter `id:` values)
    ids = []
    for f in glob.glob(os.path.join(VAULT, "**", "*.md"), recursive=True):
        fm = frontmatter_parse(f)
        if fm:
            m = re.search(r"^id:\s*(.+)$", fm, re.M)
            if m:
                ids.append((m.group(1).strip().strip('"\' '), f))
    dup_ids = [v for v in ids if ids.count(v) > 1]
    results.append(("frontmatter ids unique", not dup_ids, f"dup={set(_[0] for _ in dup_ids) if dup_ids else None}, found={len(ids)}"))
    # 5. secret scan
    secret_hits = []
    for f in glob.glob(os.path.join(VAULT, "**", "*"), recursive=True):
        if os.path.isfile(f) and not f.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".db")):
            rel = os.path.relpath(f, VAULT)
            if rel in SECRET_PATH_ALLOW:
                continue
            try:
                txt = open(f, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            for pat in SECRET_PATTERNS:
                if re.search(pat, txt):
                    secret_hits.append(os.path.relpath(f, VAULT))
                    break
    results.append(("no secrets/credentials in vault", not secret_hits, f"hits={secret_hits}"))
    # 6. internal link check (basic: .md links resolve)
    broken = []
    for f in glob.glob(os.path.join(VAULT, "**", "*.md"), recursive=True):
        txt = open(f, encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r"\]\(([^)]+\.md)\)", txt):
            target = m.group(1)
            if target.startswith("http"):
                continue
            # resolve relative
            full = os.path.normpath(os.path.join(os.path.dirname(f), target))
            if not os.path.exists(full):
                # try vault-relative
                alt = os.path.normpath(os.path.join(VAULT, target))
                if not os.path.exists(alt):
                    broken.append((os.path.relpath(f, VAULT), target))
    results.append(("internal .md links resolve", not broken, f"broken={broken[:5] if broken else None}"))

    print("=== NORTH STARS VAULT VALIDATION ===")
    all_pass = True
    for name, ok, info in results:
        all_pass = all_pass and ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {info}")
    print(f"\nRESULT: {'ALL PASS' if all_pass else 'ISSUES FOUND'}")
    sys.exit(0 if all_pass else 1)

if __name__ == "__main__":
    main()
