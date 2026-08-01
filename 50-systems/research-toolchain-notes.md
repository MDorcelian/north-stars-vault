---
name: Research Toolchain Notes
type: system
status: active
grade: G1
updated: 2026-08-01
sources: [G1 - verified working 2026-08-01]
related: [40-people/coaching-and-advisors.md]
---

# Research Toolchain Notes

State as of 2026-08-01. These are tools/methods North Stars can now use for real research, not just the standard web_search/web_extract tools (which are limited to Brave-free, search-snippets only, no page rendering).

## YouTube channel/video listing: yt-dlp (WORKING)
Installed via `pip install yt-dlp`. Works for channel stats and video listing without auth:
```
yt-dlp --flat-playlist --playlist-end N -J "https://www.youtube.com/@handle/videos"
```
Returns subscriber count, video titles, view counts, durations, thumbnails URLs, video IDs. Reliable, no bot-check triggered for channel-level listing.

Blocked: fetching individual video pages, transcripts/subtitles, or full-res thumbnails triggers YouTube's "sign in to confirm you're not a bot" wall. Needs authenticated cookies from a real logged-in browser session to go further (Marvens' suggestion: install Firefox, browse YouTube normally, export cookies). Not yet done as of 2026-08-01, still an open item if deep transcript-level research is needed on specific videos.

## General page extraction: Playwright + Chromium (WORKING, workaround)
Installed via `pip install playwright && python3 -m playwright install chromium` (works without root, browser binary installs to `~/.cache/ms-playwright/`, no `install-deps` needed despite the warning, missing OS deps didn't block basic page rendering in practice).

Minimal working pattern:
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(user_agent="Mozilla/5.0 ...")
    page.goto(url, timeout=45000, wait_until="networkidle")
    text = page.inner_text("body")
    browser.close()
```
Confirmed working on ytjobs.co (full profile data). Does NOT reliably work on canvas-rendered apps like Google Docs' live editor (returns only the outline/UI chrome, not document body text).

## Google Docs specifically: direct export endpoint (WORKING, simplest)
No browser needed. For any Google Doc with link-sharing enabled:
```
https://docs.google.com/document/d/<DOC_ID>/export?format=txt
```
(swap `txt` for `pdf`/`docx` as needed). Simple `curl` or `web_extract` against this URL works directly, this is the fastest path for Google Docs, try it before reaching for Playwright.

## Recommended fix still pending
Marvens flagged that Google Docs extraction "used to work" and these tools will be needed often. The proper long-term fix is reconfiguring `web.extract_backend` away from `brave-free` to a real extraction provider (firecrawl/tavily/exa/parallel), which needs an API key in `.env`. Attempted `hermes config set web.extract_backend firecrawl` on 2026-08-01, but no `FIRECRAWL_API_KEY` is present in `.env` yet (only commented-out placeholders for firecrawl/tavily/exa/parallel), so it's not actually functional until a key is added. Until then, the workarounds above (yt-dlp, Playwright, direct Google Docs export) cover the immediate need.
