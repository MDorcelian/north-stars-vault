# Farm-story format evidence (live YouTube Data API, pulled 2026-09-10/11)

Purpose: the evidence base for the Dennis Taylor Script DNA v2. Every number here is a live API
snapshot on the date shown, not a stored or remembered figure. Multiplier = video views / channel
subscriber count at pull time.

## METHOD LIMIT (read this first)

Full transcripts were NOT obtained. Every transcript route failed on 2026-09-10/11:
- yt-dlp subtitle download: "Sign in to confirm you're not a bot" on all player clients (tv, web,
  web_embedded, mweb, ios, web_safari).
- youtube-transcript-api: RequestBlocked from this IP.
- YouTube timedtext caption track URL, fetched both from this server and from inside a Browserbase
  cloud browser session: HTTP 200 with a zero-length body.
- YouTube's own on-page transcript panel: panel opens, segments never load.
- Third-party transcript services: youtubetranscript.com returns "YouTube is currently blocking us
  from fetching subtitles"; youtube-transcript.io requires login; kome.ai API 522; tactiq 401.
So the structural read below is built from titles, full video descriptions, published chapter lists,
channel catalogs and outlier maths. Where a specific claim describes how a script is built, it is
inference from those artefacts and is labelled as such. It is NOT a verbatim script analysis.

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
