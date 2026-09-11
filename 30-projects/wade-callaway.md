---
name: wade-callaway
type: project
status: active
channel: Wade Callaway (AI-avatar farm channel)
updated: 2026-08-13
related: [16-people/diana-wade.md, 30-projects/ace-knows-a-guy.md]
---

# Wade Callaway — Proof-First Thumbnail System (logged 08-11)

## The system (established 08-11)
- Cards on the High Priority Ideas list carry a **[VIRAL REF Nx]** thumbnail attachment = the proven
  viral thumbnail template in that exact topic for Diana to copy/adapt, with the outlier multiplier in the
  name so its strength is visible.
- **Proof-first ranking (Marvens rule, 08-11):** an idea WITH a genuinely viral thumbnail reference
  (outlier >= 2x in the correct niche) is more likely to succeed than one without. PROVEN (>=2x) =
  high priority, top of list by outlier strength. NO-REF and WEAK/BAD-ref (<2x or wrong-niche) = no
  proof = bottom of list. Never ship a no-proof idea while proven ideas remain. Refresh daily means few
  ideas are needed, so only ship what has proof.

## Hard filters (wade_viral_ref.py, v2)
- NEVER use Shorts (drops videos under ~200s).
- Outlier floor: views/subs >= 2.0 (0.1x/0.43x/1.09x are NOT viral, rejected).
- Topic relevance gate: title/channel must contain a known farm/animal term (drops wrong-niche picks
  like a personal-development video landing on a hay card).
- Attachment-only (cover cleared, NO color banner). Re-run replaces old refs.
- Search is NON-DETERMINISTIC/rate-limited: some topics return no clean ref on a given run; a no-find
  card stays no-proof and sinks. Manually clean stale bad refs when detected.

## Universal Thumbnail Combiner Prompt (delivered 08-11)
- Purpose: Diana formerly made thumbnails from only Wade's portrait + title. New method = take the
  viral REFERENCE + the Wade AI AVATAR, combine them via prompt. Keeps reference's proven layout/
  contrast/hook, places Wade as the channel face (identical glasses/plaid/weathered look), applies
  truthful 3-6 word dollar hook + barn-red/khaki/cream palette. Outputs 6-point written design spec.
- DOC: https://docs.google.com/document/d/1q65Tr_9H0UZDEBW0Ar8TsuybKZvI_DLBYn5ipQaXDMc/edit (definitive v2)

## How Diana uses it (simple)
1. Open the card's [VIRAL REF] attachment (the reference).
2. Take that reference + Wade's avatar image into the combiner prompt.
3. It gives back one thumbnail (and a design spec).

- Niche Watch list created on the board (08-11) for competitor-format models.
  - Gould Dunlap (https://www.youtube.com/@goulddunlap9864, UC_kTpc6yrFRz6JFleB8r8xQ): sibling
    "hidden value" format in antiques niche. 4,090 subs, 5 videos in one week, 320K views, top outlier
    49.64x (rusty cast iron pans). Thumbnail formula logged in skill. Transferable mechanics only, not topic.
- Scripts
- ~/.hermes/scripts/wade_viral_ref.py — attach viral ref to a card (link in title), attachment-only.
- ~/.hermes/scripts/wade_curate.py — lists High Priority queue with PROOF STATUS per card + ranking rule.
- Cron "Wade High-Priority Idea Curator" (45 10 * * *) re-orders the list by proof daily + attaches refs
  to no-ref cards. Owner boundaries: only High Priority Ideas list; never Diana's workflow lists.


## Daily Evidence + Reasoning Sweep (built 08-11)
- Cron "Wade Evidence + Reasoning Sweep" (30 8 * * *) -> runs wade_evidence_sweep.py, writes channels/
  videos/view-snapshots to ~/.hermes/brains/north_stars_brain.db, emits conclusion-form reasoning notes.
  Fires BEFORE the 11:00 daily brief so the brief sees fresh evidence. Watchlist FIXED for clean velocity.
- Watchlist (6 competitors): Gould Dunlap, Down On The Farm, Rational Ranchers, Harvest Machine,
  Substructure, Farm Secrets.
- Niche Watch list on board: Gould Dunlap, Harvest Machine, Substructure, Farm Secrets cards added (08-11).

## BRAIN RECOVERY (08-11) — caution flag
The brain DB (~/.hermes/brains/north_stars_brain.db) was accidentally DELETED at ~21:01 during a sweep
test (careless rm). Rebuilt via seed_brain.py (schema + live channels restored; Free App master 33.87x
intact) + re-added hand-banked Web Browser P1 (671K) + farm sweep. LESSON: NEVER rm the brain; it is NOT
in git and is not recoverable from a backup. Seed then re-sweep is the rebuild path.


## PRODUCTION STATUS (08-14) — pipeline snapshot
- Video 3 ($40k Cattle): footages redone, APPROVED, SCHEDULED for upload (Diana 1:02 AM).
- Video 4: RENDER FAILURE (Diana can't render, 2:08 AM). Jiggy advised refresh / paste error to AI
  support bot. OPEN — needs follow-up; a stalled render is a pipeline blocker.
- Video 5: script APPROVED + thumbnail chosen (go with the picked one).
- Video 6: script delivered (1:04 AM) — pending Jiggy review.
- Video 7: script + thumbnails delivered (1:14 AM) — pending Jiggy review.
- Diana cadence is strong: scripts/thumbnails/render all moving, only video 4 render is blocked.
- Next: Jiggy review video 6 + video 7 scripts; resolve video 4 render.


## Niche Watch additions (08-15)
- The Deed Report: cheap rural farmhouse/property 'why cheap' format sibling. 23 subs, 106x/58x
  search-discovery outliers. Curiosity-hook transfer only.
- Backyard Bankroll: 'animals that pay X/mo, zero land' — DIRECT sibling to Wade's animal-profit lane.
  18K subs, 4 videos, 533K/29.66x launch outlier.
- Amish Frugal Life: Amish self-sufficiency, 21K subs, 462K/21.6x top, multiple 12-21x outliers. Adjacent.
- Seeds of Time: survival-gardening, one-hit (9.65x) then decay (0.05-0.10x). Warning pattern.
- Evidence sweep watchlist now 10 competitors: Gould, DownOnTheFarm, RationalRanchers, HarvestMachine,
  Substructure, FarmSecrets, DeedReport, BackyardBankroll, AmishFrugalLife, SeedsOfTime.


## PROVEN OUTLIER PROOF-TILES (08-15) — banked to brain
Cross-channel demand proof for Wade ideation engine (from 4 outlier videos):
- chicken_feed_free: '5 Plants Replace ALL Chicken Feed' 56.70x (106K, Self Reliance Hub 1.8K subs)
- feed_family_trees: '10 Trees feed family 300 yrs' 43.25x (480K, Backyard Garden Life 11K)
- quit_9to5_livestock: 'Quit 9-5 with livestock, how many animals' 6.00x (260K, Rational Ranchers)
- infinite_chicken_feed: 'Infinite FREE Chicken Feed' 1.90x (985K, Alt Ordo 520K - topic at scale)
=> 'free/infinite chicken feed' + 'salary-replacement' are proven high-demand sub-lanes for Wade.
TheLostNatureVault channel itself = decaying clone, NOT tracked (noise).


## CHANNEL FRESHNESS SYSTEM (08-15)
Lesson from the "gold" video dump: nearly all farm/self-sufficiency channels are spike-then-decay or
one-hit-wonder; a video's outlier is NOT proof the channel is viable. Durable value = proof-tiles.
- New daily cron "Wade channel discovery + decay scan" (15 16 * * *) -> wade_discovery.py. Finds NEW
  growing small channels + flags STALE watched ones. Database stays fresh, not frozen competitors.
- Kept-when-stale (historical/warning models on purpose): Down On The Farm (brag-hype decays),
  Rational Ranchers (face-led farm-profit benchmark, valued for catalog not recent velocity).
- Skill updated: ALWAYS check channel context (subs/new/top+recent) before logging a video as gold.


## CROSS-NICHE PLATFORM (Marvens 08-15 directive)
The end goal is NOT owning niche research — it's owning sister and brother niches, and ultimately
understanding what works across ALL of YouTube. Because outlier research gets arbitraged away (everyone
runs the same faceless playbook), the durable edge is transferable FORMATS + PSYCHOLOGICAL TRIGGERS.
- Implemented: brain `format_patterns` table seeded with 6 proven cross-niche patterns
  (hidden_real_numbers, free_input_hack, x_vs_y_which_profits, every_x_explained, salary_replace_count,
  forgotten_banned_hidden), each with niche-Evidence + top multipliers.
- Ideation engine skill updated: cross-niche layer is now a first-class step — query patterns first,
  transplant into any new niche cold, pattern-proven-in-4+-niches beats no-in-niche-outlier.
- Compounds across sessions as each niche confirms a pattern (ADD back on new proof).


## ANGUS DOUGLAS — VERIFIED FORMAT-PEER PROOF (08-17, live API)
@AngusDouglasUS (Angus Douglas, UCqmJMtkMyz9F2XCKm5quXoA). 11.3K subs, 18 videos, ~426K views.
Fictional Scottish-shepherd AI authority + REAL chicken info + $47 ebook. Same skeleton as Wade
(authority persona + real info + product funnel), but leads with PAIN/EMERGENCY hooks and pushes the
ebook early.
VERIFIED outliers (live): 'Heal a Dying Chicken in 5 Minutes' 131K/11.62x; 'Never Pay for Chicken Feed
Again (Plant This Tree)' 75K/6.65x; 'NEVER Pay For Chicken Feed Again - Old Scottish Method' 54K/4.80x;
'365 EGGS/Year chicken' 52K/4.63x; 'Your Hen Stopped Laying? Scottish Method' 48K/4.28x. Durations mostly
16-24 min. (Tweet numbers were a few days stale: it said 14 vids/313K/9.1K subs; now 18/426K/11.3K.)
TRANSFERABLE LESSONS for Wade: (1) lead with urgent pain/emergency topics ('your hen stopped laying',
'never pay for feed again', 'your chicken is dying') for the Google-it-now clicks; (2) push the shop
offer EARLY (soft first-3-min CTA = the same play); (3) 2/wk cadence, ride first 5x outlier, repeat
formula; (4) keep Wade's honest-real-numbers framing (safer vs YouTube authenticity than a fake culture),
borrow only the topic-energy + early-shop monetization, do NOT copy the fake-Scottish-authority gimmick.

## NICHE WATCH ADD (08-19): Lillie Ahlers (LIVE launch-phase, NOT decay)
UCZgnDg-w6VqHLJB8Qwpwabg | @LillieAhlers | 8.18K subs, 14 vids, 416K views, started 2026-07-20 (1 month old).
Live now (not decayed): top 17.86x '25 BANNED Appalachian Cooking Tricks', 9.02x grandma-never-wrote, 7.56x cast-iron; recent week still 2.6-7.6x.
FORMAT: Heritage Hidden-Knowledge (BANNED/never-wrote + rotate item = cornbread/skillet/potato/meat). HIGHEST-OUTLIER TRANSFERABLE to Wade (old-farmer authority fits).
Watch because it is a launch-phase channel actively ripping the hidden-knowledge pattern, not a spike-then-decay case. Pattern + thumb banked in brain (heritage_hidden_knowledge).

## FORMAT-PROOF REINFORCEMENT (08-20)
- Cow Calculator (GB, 400 subs, 12 vids, started 2026-06): '$10,000 in Sheep vs Goats vs Rabbits vs Quail' 52.91x + 'Start With $300 Make $61,000/yr 8 most profitable' 22.86x. Reinforces x_vs_y_which_profits (52.9) + salary_replace_count (22.9) money-threshold animal-comparison lane. Spike-then-taper (top = weeks 1-2, decayed since) -> bank evidence only, do NOT track channel.
- BalKony Chillz (UG AI podcast, 64 subs): 45.3x on one farm video among 20 non-farm podcasts = stray search fluke, NO format signal. Ignored.

## TUBELAB $120K THREAD (08-21) — product model validation + Wade actions
Thread shares ~7 money channels (NOTE: images show MOST are real-person 50+ presenters, not AI avatars; so it validates the elder-trust + product model, not AI-avatar specifically).
VERIFIED PATTERNS (from reading images + thread):
- Beat the Contractor: 25.9K subs, $11.5K/mo ads (1.14M views), PLUS a $29.99 58-page manual (40 numbered fixes, materials/prices/steps) at 0.025% conv ~ +$8.5K/mo.
- Garden Problem-Solving: 25.4K subs $7K/mo. Title format 'The One Crop I Plant in [MONTH] That Feeds Me Until [MONTH]'. Suggested product: $47 calendar w/ frost dates by zone.
- Senior Money: 22.6K $7.5K/mo ads; comments ask 'do I qualify?' = product signal; suggested $37 eligibility guide = +$25K/mo they leave on the table.
TAKEAWAYS FOR WADE:
1. VALIDATES Wade's exact monetization: elder-trust honest-real-numbers persona + cheap ultra-specific manual/calendar ($29-47) at 0.025% conversion = meaningful monthly revenue on top of ads.
2. NEW PRODUCT IDEA: a Wade farm monthly calendar (month-month: plant/feed/breed + frost dates by zone) at $29-47. Mirror of Garden's $47 calendar.
3. TITLE FORMULA to borrow: date/month-anchored ('The One Crop I Plant in [MONTH]...', 'Stop Paying These [N] Bills After 65') + number-anchored.
4. PRODUCT SIGNAL: when Wade comments ask qualify questions ('can I afford', 'should I'), that's the product.
Status: banked in brain (elder_trust_product) + hidden_real_numbers evidence updated. Wade monthly-calendar product card NOT yet created.

## V18 Amish Machinery Ledger — APPROVED (08-25)
- Script approved (strongest sourcing yet: Randall James OSU Geauga 2002 study, $126/acre Amish wheat vs $10 conventional; honest machinery dual-ledger; $15-20K Amish toolkit vs $94K+30K tractors / $340-420K combine / $850-950K flagship; custom hire $35-45/acre; Purdue cost benchmarks; honest ceiling).
- Thumbnail: 3-way tie-break via 3 models. My Haiku-side + Fable = B ($15K OUTWORKS $340K); Opus = D (AMISH $15K SETUP). Fable tiebreak rationale: zero-audience channel wins on CTR first, B legible at 120px, title already carries 'Amish Machinery Ledger', D is best for traction stage not #1. PICK = B, ship it. D = documented variant for A/B later at scale.
- Important practice: thumbnail review used manual Opus call (Marvens asked) + Fable tiebreak — routed per model-routing (Opus = high-leverage review, Fable = manual-trigger ideation/tiebreak only).

## Beef-wave validation + thumbnail log (08-26)
- Logged reference thumbnail: 60-references/amos_hale_beef_197x.jpg (saved 08-26).
- OUTLIER COMPARISON (which beef reference is the biggest outlier):
  - Amos Hale 'America's Beef Supply Just Hit a New Warning Sign' -> 40,896 views on 207 subs = 197.6x. GENUINE real outlier (not rounding artifact). Channel created 08-04, only 3 weeks old. 789 likes. ~15 min. Published 08-21. THE biggest, most current outlier.
  - CNBC 'Why Beef Prices Keep Rising' (n1bF_8yC8QM) -> this is the card-22 attached ref by FORMAT family (hidden_real_numbers), but as a massive-multiplier REFERENCE it's a big-channel news explainer, NOT the outlier to copy for packaging. Amos is the outlier for PACKAGING (warning/person-first); CNBC is the data source.
- VERDICT on card 22: ship FIRST, use AMOS's packaging recipe (person-first + warning/urgency + concerned face + institutional cue) because Amos is the true packaging outlier (197x vs CNBC's normal news format). CNBC remains the number/research source.
- Card 22 updated accordingly (title 'Beef Is $9 a Pound. Here's the Real Problem.', thumb recipe = Amos-derived, ship first).

## 10-VIDEO FARM-HISTORY PIVOT BATCH MATERIALIZED (09-10)
Card 27 ("30 Things Every American Farmhouse Had Before Electricity", uploaded 09-10) carried a research plan
buried in its DESC that was never turned into board cards. Materialized it: 10 cards created in the
**Scripting** list, numbered **28-37**, one per planned video.
Script: `~/.hermes/scripts/wade_pivot_batch.py` (reusable, `--dry-run` supported; gates every ref).
- Cards: 28 farm well | 29 farmhouse kitchen | 30 farm buildings | 31 farm child skills | 32 tech replaced by
  electricity | 33 barn 1950s | 34 farm tractor | 35 machines built to repair | 36 prairie winter | 37 workshop tools.
- Every proof reference RE-VERIFIED live 09-10 (never trust the 09-04 snapshot): all long-form 24-38 min
  (no Shorts), all developed-market English channels, outlier range 8.4x-55.7x. Two ref channels:
  Forgotten American Farm & Country Life (5,060 subs) and Earl's Old Farm Days (2,900 subs).
- Each card desc is self-contained: title, angle, modules, thumbnail hook, refreshed proof numbers,
  outline-first workflow, hard research rules, deliverables list + link to DNA.
- Each card carries its verified ref thumbnail as a `[VIRAL REF Nx]` attachment (attachment-only, cover cleared).
- Card #28's ref (jXz_PuC5IuQ, 55.7x) is the flagship format outlier but its topic is the farmhouse itself, not
  water. Added an ALT REF line on that card: Two Hands Restorations "Red Jacket Hand Water Pump Restoration"
  (373,228v / 55,600 subs = 6.7x, 28.2 min) = exact object match. Left the choice to Jiggy rather than
  silently substituting.
- Card 27 desc updated to point at cards 28-37.

### NICHE WATCH ADD (09-10): Forgotten Home Engineering — live launch-phase format peer
@forgottenhomeengineering | UCE3DzKfdkEEf3kwQYPqcJFA | created 2026-08-03 (5 weeks old) | 20 vids | 7,100 subs |
1,176,259 total views. NOT decaying: 09-07 upload still at 82,446v.
Top outliers (live 09-10): "20 Forgotten Home Designs That Stayed Cool Before Air Conditioning" 336,329v/47.4x
(29.9 min); "20 Old-House Ventilation Tricks Modern Builders Quietly Abandoned" 184,980v/26.1x;
"25 Old-School Basement Tricks That Kept Homes Dry Without a Sump Pump" 161,517v/22.7x;
"20 Old-House Drainage Tricks..." 110,092v/15.5x.
TWO title shapes: "N Forgotten/Old-House [system] Tricks ... Before Modern [X]" and "Old-House [system] Tricks
Modern Builders Quietly Abandoned" — all 25-30 min. Strongest live proof the "forgotten old-home system"
framing carries 300K+ views on a brand-new channel. TRANSFERABLE: framing + "Quietly Abandoned" angle +
25-30 min catalog length. Do NOT copy topics verbatim.
Logged in the board under Niche Watch. Ownership UNCONFIRMED: Jiggy called it "another channel for Wade
Callaway"; channel description reads as an independently owned property (nostalgiaoperations@gmail.com), so it
is logged as an external peer. Ask Jiggy if it is actually ours before treating it as a competitor again.

### OPEN ITEM for Jiggy
Whether the 10 pivot videos continue the existing upload numbering (28-37 on the WadeCallaway board, where
card 27 already sits) or start fresh on a new channel. Numbered 28-37 on the assumption the pivot continues the
same sequence, since card 27 is itself a farm-history video in that sequence. One command to renumber.
NOTE (09-11): Jiggy moved the 10 cards from `Scripting` to `High Priority Ideas (next in line)`. Treat High
Priority Ideas as the intake list for new idea cards on this board; do not drop new cards straight into Scripting.

## SCRIPT DNA v2 + FARM-STORY SYNTHESIS (09-11) — primary format changed
Jiggy challenged the DNA against four farm-story example videos and asked for the right DNA / product-market fit.
Verdict: **the winners are stories, and the story format is stronger than our modular list documentary.**
- v1 DNA archived to `50-systems/dennis-taylor-script-dna-v1-ARCHIVED-2026-09-04.md`.
- New master: `50-systems/dennis-taylor-script-dna.md` (v2, 09-11). Evidence file:
  `50-systems/farm-story-format-evidence.md` (all figures live-API snapshots 09-10/11).

### The decisive evidence
- **Old Timber** (1,290 subs, 15 vids, created 2025-04-20): **median outlier 13.8x, 8/15 above 10x, 13/15 above
  3x**, on 10-15 min videos. Top 145,688 / 112.9x. This is a REPEATABLE formula, not a one-hit. Primary
  architecture source for v2.
- **Burl Sizemore** (1,810 subs, 37 vids): top 80,360 / 44.4x, 6/37 above 10x. First-person 72-year-old
  Appalachian narrator + product funnel (burlsizemore.com). Live independent confirmation of our banked
  `elder_trust_product` model.
- **The Stubborn Farmwife** (3,030 subs, 91 vids): top 154,353 / 50.9x, but median 1.0x with 25/91 above 3x.
  Volume lane, 30-44 min. Hit machine, not a floor.
- **Barnside Tales** (265 subs, 17 vids, created 2026-08-06): top 72,468 / **273.5x** but median 1.2x, only
  2/17 above 10x. A single breakout on a tiny channel, NOT channel proof.

### The formula distilled (now the v2 beat sheet)
One person vs one institution. A discarded/rejected object at the centre. The protagonist is methodical
(weighs, tests, records) which makes vindication feel earned. A mid-story technical FAILURE. One mentor with one
specific fix. Institutional BACKLASH before payoff. A hard number payoff ($180,000 / $1.8M / $294,000). Then one
theme line, stated once. Titles: "The [institution] Dumped/Wrote Off [thing] - Then [number payoff]" and "They
Laughed/Mocked When She [did the odd thing] - Then/Until [reveal]". Published chapter timestamps = the beat
template. 10-15 min launch length, not 30-44.

### The tradeoff v2 had to resolve (documented honestly)
v1 forbade invented people; the top outliers invent them (Old Timber / Barnside use fabricated named people; Burl
sells a product on an invented first-person memoir). v2 keeps the story ENGINE and refuses the specific act with
real authenticity/monetisation risk: Dennis stays a third-person narrator/guide with NO claimed personal memory,
the mechanism layer must be real + sourced, protagonists are explicitly labelled dramatised composites in the
description, and no product is ever attached to a claimed memory. Flagged to Jiggy as a deliberate decision.

### BLOCKER: transcripts unavailable
Full transcripts could NOT be obtained on 09-10/11. yt-dlp blocked on every player client ("sign in to confirm
you're not a bot"); youtube-transcript-api RequestBlocked; YouTube timedtext caption track returns HTTP 200 with
ZERO-length body, both from our server AND from inside a Browserbase cloud session; the on-page transcript panel
opens but segments never load; youtubetranscript.com reports YouTube blocking it; youtube-transcript.io needs
login; kome.ai 522; tactiq 401. So the structural read is from titles, full DESCRIPTIONS (rich: Barnside and Burl
paste script openings), published CHAPTER LISTS, catalogs and outlier maths. Labelled as such in the evidence
file; NOT claimed as verbatim script analysis.

### Card state
Cards 28-37 were flagged with a prominent `FORMAT HOLD` note at the top of each description pointing at DNA v2,
so Diana does not start scripting a superseded list-format brief. Each card is explicitly awaiting Jiggy's call on
keep-as-secondary-list vs recast-as-story.

### INFERENCE FLAG (unconfirmed)
Barnside Tales and Old Timber share title grammar AND repeatedly name the protagonist **Ruth** (Ruth Alder, Ruth
Ackerman, Ruth Merrick, Ruth Keller), plus the same "On a Tuesday morning in [month], outside [town]..." opening.
Consistent with a shared production template/operator behind both. If so, they are ONE validation, not two.

### FIRECRAWL PASS (09-11) — transcript dead end CONFIRMED, two new findings banked
Jiggy supplied a Firecrawl API key to unblock scraping. Result:
- **Transcripts are a proven dead end, not a lack of effort.** YouTube API `contentDetails.caption`: Barnside
  Tales 0/17, Stubborn Farmwife 0/25, Burl Sizemore 0/25, Forgotten Home Engineering 0/20 have captions at all.
  Only **Old Timber has captions (14/15)**. Even there, every path returns an empty body: timedtext (both the
  asr and uploaded en-US track, no-param + fmt=json3 + fmt=srv3) = HTTP 200 zero-length from our IP AND via
  Firecrawl's cloud IP; the on-page panel populates no segments; Firecrawl interact in code mode is unreliable.
  Three of the four examples have no transcript in existence. Stop retrying transcript extraction on this lane.
- **NEW FINDING 1, AI disclosure labels.** YouTube renders "How this was made / Made with AI / Sounds or visuals
  were altered or fully generated" on **Barnside Tales (273.5x)** and **Burl Sizemore (44.4x)**; NOT on Old Timber
  or Stubborn Farmwife. The two highest multipliers openly carry the synthetic-content label and still perform.
  => The disclosure is NOT a performance penalty. DNA v2 now MANDATES ticking it (rule 7) as the monetisation-safe
  posture. This materially de-risks the earlier "disclosure will hurt us" assumption.
- **NEW FINDING 2, live title census (52 titles from the Old Timber sidebar).** Confirms the "They Laughed /
  Nobody Wanted / Until" template is SATURATED (near-duplicate titles on the reference channels themselves) and
  adds two live lanes: Shape 4 = refusal + legal escalation ("She Refused Every Offer to Move It"; "Cost Them
  Millions in Court"), Shape 5 = HOA/easement confrontation ("HOA Installed A Gate On My Private Bridge - So I
  Removed The Entire Bridge Overnight!"). Also saw template drift into non-farm genres = template farming at
  scale. Lane durations run 12-51 min.
- Audience comments fact-check cost figures ("you'd think he would have built a new one for $185,000"), which is
  exactly the pressure the real-mechanism + sources rule exists to survive.
- Firecrawl API notes for reuse: max 2 concurrent browser jobs (429 otherwise); free stuck slots with
  `GET /v2/interact?status=active` then `DELETE /v2/interact/{sessionId}`; v2 `/scrape` supports `actions`
  (click / wait / executeJavascript) and `/scrape/{id}/interact` takes `prompt` or `code` (node/python/bash).
  Key left INLINE only: `~/.hermes/.env` is write-protected, so FIRECRAWL_API_KEY is still a commented
  placeholder there. Add it manually if we want Firecrawl available next session.

### YOUTUBE-TRANSCRIPT-API TEST (09-11) — library fine, wall is YouTube-side. DO NOT RETRY.
Jiggy suggested https://github.com/jdepoix/youtube-transcript-api. Ran it properly (v1.2.4, in the hermes venv):
- **The library works.** Control video `dQw4w9WgXcQ` returned 61 segments, repeatedly, between every failing
  attempt. So the tool, our IP and the install are all fine.
- **Every target video returns `RequestBlocked`**, consistently: all 7 top Old Timber videos, all 7 top Barnside
  Tales videos, 7 Stubborn Farmwife videos, 7 Burl Sizemore videos, the 1950s farmhouse/kitchen references, the
  Earl's tractor/barn/workshop references, and Forgotten Home Engineering's two biggest (336K / 184K). Even
  `api.list(vid)` is blocked, and requesting the transcript in es/fr/de is blocked too.
- Diagnosed as per-video, NOT per-IP: the control succeeded immediately before AND after each blocked fetch.
- **Root cause evidence:** fetching the caption track from INSIDE a real browser session already sitting on the
  youtube.com watch page (same origin, same session) returns HTTP 200 with `Content-Length: 0` and
  `Server: video-timedtext`, for BOTH the asr track and the uploaded en-US track, on a video that the API says
  has captions. YouTube now gates caption delivery behind a PoToken / signed-in session. The caption URL is
  present in `ytInitialPlayerResponse.captions` but serves an empty body to anonymous requests.
- Combined with the caption-availability data above: **3 of the 4 supplied example videos have no captions in
  existence at all**, and the 4th is PoToken-gated. Verbatim transcripts for this lane are not obtainable from
  this environment by any method tried (yt-dlp x6 clients, youtube-transcript-api direct/list/translated,
  timedtext x3 formats x2 IPs, on-page panel x2 browsers, 4 third-party services, Firecrawl actions + interact
  prompt + interact code).
- **Local ASR is not a viable fallback in this environment:** ffmpeg present and faster-whisper installed, but
  the box has 2 CPUs / 3 GB RAM, no whisper model cached, and there is no way to obtain the audio (yt-dlp
  download blocked; signed googlevideo URLs are IP-bound to the browser that requested them).
- **THE PATH THAT WOULD WORK:** a residential IP. Jiggy runs one yt-dlp subtitle command on his own machine and
  drops the .vtt into the vault, or opens the video, clicks Show transcript and pastes it. That takes about a
  minute and closes the gap permanently for any video we care about.

### NET EFFECT ON THE DNA
None. DNA v2 does not depend on transcripts. The transcript would let us verify pacing and exact CTA placement
inside Old Timber's script; it would not change the architecture, the beat sheet, the honesty rules or the
primary/secondary lane split, all of which are already evidenced from descriptions, published chapter lists,
catalogs, outlier maths and the live title census.
