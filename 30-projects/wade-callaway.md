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
