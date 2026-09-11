# Farm-story format evidence (live YouTube Data API, pulled 2026-09-10/11)

Purpose: the evidence base for the Old Ground Script DNA v2. Every number here is a live API
snapshot on the date shown, not a stored or remembered figure. Multiplier = video views / channel
subscriber count at pull time.

## METHOD LIMIT (read this first)

Full transcripts were NOT obtained, and this is now a proven dead end, not a lack of effort.

Caption availability, checked via the YouTube Data API `contentDetails.caption` field on 2026-09-11:
- **Barnside Tales: 0 of 17 videos have captions.**
- **The Stubborn Farmwife: 0 of 25 sampled have captions.**
- **Burl Sizemore: 0 of 25 sampled have captions.**
- **Forgotten Home Engineering: 0 of 20 have captions.**
- Forgotten American Farm & Country Life and Earl's Old Farm Days: no captions on the checked videos.
- **Old Timber: 14 of 15 videos DO have captions** (the one exception being the 2026-09-05 upload).

So for three of the four supplied examples there is literally no transcript in existence to retrieve. For Old
Timber, where captions do exist, every retrieval path still returned an empty body:
- yt-dlp subtitle download: "Sign in to confirm you're not a bot" on all player clients (tv, web, web_embedded,
  mweb, ios, web_safari).
- youtube-transcript-api: RequestBlocked from this IP.
- YouTube timedtext caption track URL (both the asr and the uploaded en-US track, each tried with no format
  param, `fmt=json3` and `fmt=srv3`): HTTP 200 with a **zero-length body**, from this server AND via
  Firecrawl's cloud IP.
- YouTube's own on-page transcript panel, driven through Firecrawl's browser: the panel is present in the DOM
  but segment elements never populate.
- Third-party services: youtubetranscript.com reports "YouTube is currently blocking us from fetching
  subtitles"; youtube-transcript.io requires login; kome.ai API 522; tactiq 401.
- Firecrawl `/interact` in code mode (Node/Playwright) was inconsistent: it sometimes executed (output landing
  on stderr) and sometimes returned nothing.
- Firecrawl `/interact` in prompt mode refused to reproduce the transcript verbatim, but DID return a 390KB
  accessibility tree, which is where the comment and sidebar-title evidence below comes from.

Conclusion: the structural read below is built from titles, full video descriptions, published chapter lists,
channel catalogs, outlier maths, comment text and the live sidebar title ecosystem. Where a claim describes how
a script is built it is inference from those artefacts and is labelled as such. It is NOT a verbatim script
analysis, and no verbatim transcript was ever in hand.

## AI DISCLOSURE LABELS (new finding, 2026-09-11, Firecrawl page render)

YouTube renders a "How this was made / Made with AI / Sounds or visuals were altered or fully generated" notice
on two of the four supplied examples:
- **Barnside Tales, "Nobody Bid on 6 Quiet Cows" (273.5x): label present.**
- **Burl Sizemore, "25 Outlawed Tools" (44.4x): label present.**
- Old Timber "The County Came to Demolish His 100-Year-Old Barn": label NOT present.
- The Stubborn Farmwife "The Little Girl Paid a Nickel": label NOT present.

**This matters more than it looks.** The two highest-multiplier examples in the set are openly carrying
YouTube's synthetic-content disclosure and still pulling 273x and 44x. The disclosure is not a performance
penalty. It is also the compliance posture that protects monetisation. DNA v2 therefore mandates it rather
than treating it as a risk to be hidden.

## LIVE TITLE ECOSYSTEM (from the sidebar of the Old Timber video, 2026-09-11)

The related-video rail is a live census of what the lane is actually making right now. 52 candidate titles
captured. Recurring shapes:

1. **They Laughed / Nobody Wanted / Neighbors Called It Worthless + Until/Then.** Fully saturated. Includes
   near-duplicates of Old Timber's own video ("The County Came to Demolish His 100-Year-Old Barn - But He Moved
   the Whole Thing First" beside "- So He Moved the Whole Thing").
2. **Widow / single mom / teen / elderly underdog against an institution.** "A Widow Bought 50 Rusty Plows for
   $1,000 - They Laughed Until She Turned the Scrap Into a Fortune." "Nobody Wanted the Giant Redwood Log -
   Until a Single Mom Took One Look" (51 min).
3. **Refusal and legal escalation.** "The Flood Left a 60-Ton Locomotive Standing in Her Cornfield - She Refused
   Every Offer to Move It." "They Bulldozed a Little Girl's Orchard - Then Faced the Harvest That Cost Them
   Millions in Court."
4. **HOA / easement confrontation (an adjacent lane running hot).** "HOA Installed A Gate On My Private Bridge -
   So I Removed The Entire Bridge Overnight!" "HOA Built Houses Around My Airstrip - Then the FAA Inspector
   Arrived." "HOA Booted My Tractor Inside My Own Barn - So I Revoked Every Easement They Held."
5. **Genre drift.** Some rail entries are not farm content at all, e.g. a 48-minute "The Girls Choose the Deadly
   Chained Alien" story. Same template machinery, different genre, which is a strong sign of template farming
   at scale.

Observed durations in the lane: 12 to 51 minutes. Our 10 to 15 minute target sits at the low end, which is
where Old Timber's repeatable 13.8x median lives.

## Audience reaction (from the Old Timber comment block, 2026-09-11)

Comments on the barn video show the emotional payload landing and, importantly, viewers fact-checking cost
figures: "I know that the barn was 100 yrs old but you'd think he would have built a brand new better one for
$185,000." Also "Made me hold my breath for the farmer." and a viewer revealing their own barn loss to a
county. That is the credibility pressure our DNA's real-mechanism and sources rule exists to survive.


## The four examples (as supplied)

| Video | Channel | Subs | Views | Mult | Dur |
|---|---|---|---|---|---|
| Nobody Bid on 6 Quiet Cows - No One Knew They Were the Last | Barnside Tales | 265 | 72,468 | 273.5x | 27.3 min |
| The County Came to Demolish His 100-Year-Old Barn - So He Moved the Whole Thing | Old Timber | 1,290 | 40,086 | 31.1x | 11.6 min |
| The Little Girl Paid a Nickel for Every Printed Feed Sack - Then the Quilt Collectors Found Her Barn | The Stubborn Farmwife | 3,030 | 22,376 | 7.4x | 37.3 min |
| 25 "Outlawed" Tools Every Appalachian Grandfather Hid in His Barn Loft (I Quit Using 9) | Burl Sizemore | 1,810 | 80,360 | 44.4x | 25.3 min |

All four are long-form (11 to 37 min), all four are single-narrative or narrative-framed, none is a
modular "system documentary".

## Channel catalogs (the real signal: is the format repeatable?)

### Old Timber - UCNxBYhgZD47M776dylkkXIA
Created 2025-04-20. 1,290 subs. 15 videos. 606,919 total views.
Outlier: max 112.9x. **median 13.8x. 8 of 15 above 10x. 13 of 15 above 3x.**
Runtime: 10 to 15 min. Channel line: "Old Timber - where quiet folks stand their ground, and powerful
men learn the hard way. Stories of land, pride, family, and justice."
Top: Dairy Dumped Thousands of Gallons at Her Farm Weekly (145,688 / 112.9x, 12.0 min); They Laughed
When She Took 300 Old Windows - Then Her Greenhouse Earned $180,000 (141,016 / 109.3x, 14.6 min); The
Pecan Mill Dumped Mountains of Shells on Her Farm - She Built a Six-Figure BBQ Pellet Business
(76,372 / 59.2x); They Laughed When She Took 500 Rusty Oilfield Pipes (50,985 / 39.5x); She Paid $800
for 40 Tons of Rejected Wool - Then Made $1.8 Million (47,663 / 36.9x).
**This is the only one of the four with a consistently repeatable formula rather than a single hit.**

### Burl Sizemore - UCXO5xjzNQzkPqVqBhMLgMiw
Created 2022-03-30. 1,810 subs. 37 videos. 363,492 total views.
Outlier: max 44.4x. median 2.1x. 6 of 37 above 10x. 16 of 37 above 3x. Runtime 10 to 40 min.
First-person elder narrator. Titles carry a parenthetical personal proof tag: "(I Quit Using 9)",
"(I Own 3)", "(I Still Carry 3)", "(Four Are Still With Me)", "(Four Were Smarter Than Ours)".
Direct product funnel at the persona: https://burlsizemore.com (an Appalachian "pocket-fix" guide).
Description of "My Grandfather Carried Three Things" ends: "Everything here is real history: the
Federal Switchblade Act of 1958, the state laws on blackjacks that go back to the 1800s, company
scrip, and untaxed liquor... The man is mine. The world was real." That is a fiction disclaimer
bolted to real statutes: real law as credibility scaffolding for an invented man.

### The Stubborn Farmwife - UCzMsmR_aJBEA53FjuWez0oQ
Created 2007-06-10. 3,030 subs. 91 videos. 1,157,009 total views.
Outlier: max 50.9x. median 1.0x. 12 of 91 above 10x. 25 of 91 above 3x. Runtime 30 to 44 min.
Volume play: same title shape repeated at scale, most videos land near 1x, the hits go big.
Descriptions are empty (title only), so no script scaffolding is available here.

### Barnside Tales - UCBdsf1T1WLVU1Eb_5hPHqfQ
Created 2026-08-06. 265 subs. 17 videos. 81,009 total views.
Outlier: max 273.5x. median 1.2x. 2 of 17 above 10x.
**One breakout, not a proven formula.** On a 265-sub channel a single 72K video produces a 273x
multiplier mechanically. Treat the 273x as a topic/hook signal, not as channel proof.

## What the artefacts show about the winning construction

1. **A named protagonist with a nameable antagonist.** "Ruth Keller" vs Vanderveld Dairy. "Patty" vs
   the pecan mill. "Walt Kessler" vs the county. "Marian Ellison" vs the commercial cattlemen. The
   story is a person versus an institution, not an inventory of objects.
2. **Rejected material at the centre.** Rejected milk, rejected wool, 300 old windows, 500 rusty
   pipes, 40 tons of shells, cows nobody bid on, a barn the county wants gone. The subject is always
   something the world priced at zero.
3. **Recording and measurement as the credibility move.** Ruth "tested every load, demanded disposal
   records". Patty "weighed every delivery, saved samples, sorted by hand". The protagonist is
   methodical and literate, which is what makes the vindication feel earned rather than lucky.
4. **A mid-story failure beat.** The greenhouse overheated, a batch ruined a Saturday of brisket, the
   cattle gate sagged once loaded. The failure is what forces the discovery.
5. **One mentor or expert fix.** "She took the sagging gate to a rancher who had been building gates
   for years." Advice from a commercial grower. The turn is external and specific.
6. **Institutional backlash before resolution.** The mill stops delivery without warning once it
   realises the waste is worth money. This is the tension spike near the end.
7. **A hard number as the payoff.** $180,000. $1.8 million. A six-figure business. $294,000 at
   auction. The number is the proof the story was worth telling.
8. **A stated theme on the way out.** "Sometimes the difference between trash and opportunity is
   simply knowing what you're looking at." "seeing value where everyone else saw garbage."
9. **Published chapter lists.** Old Timber and the Wool video both publish timestamps, which means the
   beat structure is a fixed template the writer fills each time.
10. **Open loops at title level and mid-title tension.** "Nobody bid on 6 quiet cows - no one knew
    they were the last." "The County Came to Demolish His Barn - So He Moved the Whole Thing." The
    title poses a problem and withholds the resolution.

### Template-level observations (inference, flagged as such)
Barnside Tales opens multiple videos with the same construction: "On a Tuesday morning in [month],
outside [town], in [county], [state], [name] stood..." Across Barnside Tales and Old Timber the
protagonist is repeatedly named **Ruth** (Ruth Alder, Ruth Ackerman, Ruth Merrick, Ruth Keller).
Shared protagonist naming plus shared title grammar is consistent with a common production template
or operator behind both channels. Not confirmed, but it means the two channels should not be counted
as two independent validations of the same formula.

## Alignment assessment against our own banked patterns

Our brain (`~/.hermes/brains/north_stars_brain.db`, `format_patterns`) already carries:
- **Underdog Animal/Farm Redemption Story** (multipliers 47.7, 8.9, 7.8; triggers empathy,
  emotional-resolution, justice/redemption, nostalgia).
- **Elder/50+ trust persona + ultra-targeted cheap manual/calendar product** (25.9K-sub channel
  $11.5K/mo ads plus a $29.99 manual; 25.4K and 22.6K examples at $7K to $7.5K/mo ad revenue).
- **The [Forgotten/Banned/Hidden] [X]: Why Did They Do This?** (17.9, 9.0, 7.6).
- **Heritage Hidden-Knowledge** (BANNED/never-written-down, rotate the item) (17.9, 9.0, 7.6).
So the story lane is not new to us; it was banked but never promoted to the primary script format.
Burl Sizemore is a live, independent confirmation of the elder-trust-persona-plus-product model.

## The tradeoff that has to be decided (not resolved by data)

The highest outliers here are **dramatised third-person case narratives about people who do not
appear to exist** (Old Timber, Barnside Tales), and in Burl Sizemore's case a **first-person invented
memoir** sold alongside a product. Our v1 DNA explicitly banned exactly that ("not AI farm fiction,
fake personal reminiscence").

The data says the story architecture is the viral engine. The risk is authenticity and monetisation:
invented first-person testimony attached to a product is the highest-liability version of that
architecture, and the pivot's whole purpose is to get paid. DNA v2 therefore keeps the story engine
and grounds it in verifiable mechanism plus an explicit dramatisation disclosure, and keeps the
narrator out of fake personal memory. See the DNA's Honesty and disclosure section.
