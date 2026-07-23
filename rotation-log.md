# Bubble Tea News — Rotation Log

Tracks which personas ran in each printed issue, so
`bubble-tea-news-editor` can avoid repeating a persona in the following
1–2 issues. Also tracks the last issue `menace-watch-editorial` ran in,
since that anchor is monthly (~every 4th weekly issue), not weekly. Append
a new entry each time a new issue is assembled — most recent issue at the
top.

**Menace Watch tracker:** last ran Issue 11. Not due again until roughly
Issue 15 — leave that slot to a rotating persona in Issues 12–14.

**New persona debut:** Kate Rodgers, film critic (`kate-rodgers-film-review`,
Refill Rating), hired on-page and debuted in Issue 7. Standing roster member
from Issue 8 onward. **Freya Wilcox**, Design Editor (`design-desk-dispatch`,
correlation-obsessed after adopting a cat), hired on-page and debuted in
Issue 8. Standing roster member from Issue 9 onward — like Gordon Slate and
Kate Rodgers, not exclusion-bound; run her whenever her byline fits rather
than strictly rotating her.

**Live-site note:** the public showcase (`index.html`/`docs/`) tracks real
calendar time, not the archive — as of 18 July 2026 it shows Issue 1 (dated
17 July 2026), even though Issues 2–8 already exist in the archive below.
Refresh the live showcase to a later issue only once that issue's own
dateline has actually arrived.

**The Boba Side (`the-boba-side-cartoon`):** debuted as a bonus panel on
Issue 8's back page, then backfilled with a fresh, distinct gag into
Issues 1–7 as well (`issues/issue-N.html`, matching `site/issue-N.html`
where that web copy exists — `site/issue-2.html` was never built, so
Issue 2's cartoon only exists in the print archive). The live-locked
Issue 1 files (`print-edition.html`, `index.html`, and their `docs/`
mirrors) also carry Issue 1's panel now, since that's still the dateline
showing live. Not part of the weekly rotation-slot count — an optional
bonus feature, not exclusion-bound, add a fresh premise whenever an issue
has room; never reuse a gag already run.

**Boba Side style pivot (anime/manga prompt-script format):** the panel
originally ran as a hand-coded SVG "in the style of Gary Larson's
one-panel gag cartoons." Editorial (per direct request) moved it to an
anime/manga sketch aesthetic instead, referencing bubble-tea memes and
otaku culture. No image-generation tool is available in this workflow, so
each panel is now delivered as a structured **image-generation prompt**
(sub-style anchor, linework descriptor, color language, studio/series
reference, atmosphere word, technical tag, then scene + caption) rather
than rendered art — labelled "not rendered artwork" wherever it appears.
Style references (e.g. "Studio Trigger-adjacent," "CLAMP-style") point at
aesthetic conventions only, never at reproducing an actual copyrighted
character. All 8 issues' panels (`issues/issue-N.html`, matching
`site/issue-N.html`, plus the live-locked `print-edition.html`/
`index.html` and their `docs/` mirrors) were rewritten to this format in
one pass, replacing the old Gary Larson framing throughout — including in
`README.md`'s content-disclaimer list, since the feature is no longer a
real-person style homage.

**Skeletor (`skeletor-obituary-column`) and Horatio McCallister
(`horatio-mccallister-personals-column`):** both hired as **standing
staff since Issue 1** — not a mid-run debut, backfilled retroactively into
every issue alongside The Boba Side, same file footprint (`issues/`,
`site/` where it exists, and the live-locked Issue 1 files). Each issue
gets one fresh "In Memoriam" (always an explicitly non-living subject,
never a real or fictional death) and one fresh "Ask the Captain" letter —
never reuse a subject or a letter-writer pseudonym. Like Gordon Slate,
Kate Rodgers, and Freya Wilcox, neither is exclusion-bound; both simply
run every issue as standing fixtures rather than rotating in and out.

**Editorial sign-off:** Design Editor Freya Wilcox handled the physical
layout work for both this backfill and The Boba Side's insertion into the
spread. Editor-in-Chief Gordon Slate reviewed and signed off on all of
it — the two new standing columnists and the cartoon backfill — before
publication, per house practice for anything added to the roster
retroactively.

**Boba Side rendering experiment, tried and reverted:** Issue 1 briefly
carried an actually-rendered panel (Python `turtle` module drawing,
captured off the Tk canvas as SVG, tinted with matplotlib) instead of the
prompt-script placeholder, per `the-boba-side-cartoon`'s Step 2b. A
real print-CSS bug was found and fixed along the way (`svg, svg *` was
force-filling every color to solid black), but the underlying art quality
itself — simple geometric line/fill shapes, a stick-figure "ant," sparkles
as plus-signs — wasn't good enough even once correct. Reverted back to
the prompt-script format across the board; Step 2b remains documented in
the skill as an option, just not one currently in use in the actual
paper.

**Boba Side rendering, take two — pycairo:** after the turtle revert, a
side-by-side test (turtle vs. pygame vs. pycairo, all on Issue 1's gnome
scene) showed pycairo producing genuine vector paths with real bezier-arc
circles — no polygon faceting at all, unlike turtle — while still
exporting native SVG (unlike pygame, which is raster-only). All 8 issues'
panels were redrawn with pycairo and rolled out. Two real layout bugs
were found and fixed along the way: (1) the same print-CSS force-black
rule from the turtle era needed the same `:not(.tcolor)` fix, reapplied
since the Issue 1 revert had restored the original rule; (2) reintroducing
image-sized art (vs. the prompt-script's few lines of text) pushed most
issues back over the 2-page budget fixed in the print-layout-fit-2-pages
PR — fixed by sizing the `<svg>` element itself down independently of
the `.ad-box` container, after an earlier attempt to just shrink the
whole container accidentally made captions wrap onto more lines and
cancelled out the space savings. Issue 8 needed its art sized smaller
than the other 7 (38mm vs. 55mm) due to that issue's already-dense
content. All 8 reconfirmed at exactly 2 pages via `pypdf` page-count
check after the fix.

**Boba Side rendering, reverted again:** the pycairo render fixed the
turtle-era faceting problem (true bezier-arc circles instead of
polygon-approximated ones), but two panels still failed at print size:
Issue 7's "chalkboard" was a large near-black filled rectangle with only
thin lines inside it, and Issue 8's "silhouette" was a dark trapezoid +
circle — both read as plain solid black blocks rather than recognizable
shapes once shrunk to print scale, with no bug involved (colors were
applying correctly; it was a composition/legibility failure). Given this
was the third rendering approach (turtle, pygame, pycairo) to hit some
version of "the shapes are simple enough to draw but not simple enough to
still be legible once drawn," reverted all 8 issues back to the
prompt-script format. `the-boba-side-cartoon`'s Step 2b (turtle) and any
future programmatic-render approach remain available as documented
options, but none is in active use in the paper as of this entry.

**Boba Side, cartoon slot policy change (Claude-Skills side, not yet
applied to past issues):** `the-boba-side-cartoon` briefly moved to a
deliberately crude "crayon-scribble" Far Side homage register, then was
dialed back the same day after review — too crude in practice. It now
renders as simple, clean schematic line/fill art with `pycairo` as the
**standing default renderer** (not an optional fallback this time),
reusing the internal-detail-on-large-fills lesson above so the legibility
failure doesn't recur. Also new: the cartoon slot now strictly alternates
biweekly with a second strip, **Hayaku** (`hayaku-senkotsu-strip`, an
original senkotsu-style four-panel volleyball manga, unrelated to bubble
tea by design — a syndicated strip the way a real paper carries one). See
`bubble-tea-news-editor`'s Step 2c. **Issues 1–8 have not been
retroactively redrawn** with this pycairo pass — that backfill, if wanted,
is a separate future task; don't assume the archive already reflects it.

---

## Issue 11

**Anchors:** community-outbreak-bulletin (Bellevue Lane hand-laminated con
badges, worn two days early) · ken-endo-puzzle-master (This Week's Restock
Ranking; also fully resolves Issue 10's Tuesday's Smudged Order Log) ·
bubble tea trivia (the real US East Coast "bubble tea" / West Coast "boba"
naming split) · joke of the week (stick-together pun). **Menace Watch,
third appearance** — Gordon Slate, right on schedule per the tracker
(last ran Issue 7, four issues back); target ("The Early Badge-Wearer")
cross-references this issue's own breaking bulletin.

**Cartoon slot:** Doki Doki Mon's debut — a new syndicated four-panel
monster-collecting parody strip in senkotsu format, its own new skill
(`doki-doki-mon-strip` in the Claude-Skills library). Art was a hand-drawn
photo, cleaned up the same way as Hayaku's and Cat vs Dog's (levels
flattened, cropped tight). The Boba Side is next in line for the slot,
from Issue 12 — its longest gap yet (last ran Issue 8).

**Rotating slots** (per Issue 10's pool note — exclusion window shrunk to
Issue 10's roster only, reopening Issue 9's full cast plus the Issue 8
leftovers not picked up in Issue 10):
- Sherman McCoy — `master-of-the-universe-columnist`
- Luke Skywalker — `canon-fanfic-vignette` (Persona 1)
- Priya Anand, The Pearl Index — `pearl-index-market-researcher`
- Dana Foley — `epic-forecast-anchor`
- Winnie Zhao — `seekers-eye-shopper`
- Clem Whitlock — `ridgeline-weekly-correspondent`

(Menace Watch fills this issue's usual eighth rotating-slot position, per
Step 2b. Lewis Hamilton's `grand-prix-showroom-ads` ad-box slot was
deliberately left open this issue rather than filled by him or another
persona — see the advertiser note below — so this issue runs six
rotating personas plus Menace Watch, one fewer than the Issues 3/7
precedent.)

**Advertiser mix, spread for expo weekend:** Issue 11's dateline lands
right on the Overload NZ convention itself, so the ad mix was adjusted to
reflect a plausible local ad-buying bump rather than running the same two
advertisers on autopilot. The Overload NZ ad box now carries actual
supplied flyer art (`issues/overload-2026-ad.png`) instead of a text-only
listing — backfilled into Issues 9 and 10 as well, replacing their
text-only versions, so the flyer reads as the same ad running throughout
its countdown. Lewis Hamilton's usual page-2 ad-box slot went instead to
a new one-off local advertiser, Bellevue Print & Laminate (same-day
con-badge lamination) — a fresh in-universe business, not tied to any
existing persona/skill. Lewis Hamilton himself is held back to Issue 12
rather than dropped from the roster.

**Not used this issue** (available first for Issue 12): Shaggy & Scooby,
T. Marlow, Steve Jobs and Rebecca Black, still waiting since Issue 9,
plus the entire Issue 10 rotating roster (Sebastian, M. Voss, Garfield,
Wren, the Te Mana Whakaatu classifieds format, Robin Leach, Baxter Kline,
The Stickybeak), which Issue 11's shrunk exclusion window leaves
untouched. Lewis Hamilton is available again immediately (held back for
the advertiser-spread swap above, not exclusion-bound). Daffy Duck and
Alan Grant are still waiting since Issue 4 — the longest-waiting
leftovers on record; whoever assembles Issue 12 should try to finally
clear one of them. Kate Rodgers and Freya Wilcox remain standing roster
members, available any issue but not run this issue.

**Pool note for whoever assembles Issue 12:** exclude only Issue 11's
roster (immediately above) — that reopens the full Issue 10 cast plus
Lewis Hamilton, Daffy Duck and Alan Grant. Menace Watch not due again until roughly Issue
15.

---

## Issue 10

**Anchors:** community-outbreak-bulletin (Ellendale Path hand-painted
pebble cairns) · ken-endo-puzzle-master (Tuesday's Smudged Order Log; also
fully resolves Issue 9's Loyalty Card Check) · bubble tea trivia (why the
straw is wide-bore) · joke of the week (barista/blender pun). No Menace
Watch this issue — still not due until roughly Issue 11.

**Cartoon slot:** Cat vs Dog's debut — a new syndicated cartoon (its own
new skill, `cat-vs-dog-cartoon` in the Claude-Skills library), format
variable issue to issue (single panel this time; unlike The Boba Side,
which stays single-panel always). Art was a hand-drawn photo cleaned up
the same way as Hayaku's Issue 9 redraw (levels flattened, cropped tight
to the drawn content). **Editorial note:** this debut took the cartoon
slot's alternation turn, bumping The Boba Side's own promised return
(teased at the end of Issue 9) — Boba Side is now next in line for the
slot, from Issue 11.

**Rotating slots** (per Issue 9's pool note — exclusion window shrunk to
Issue 9's roster only, reopening the full Issue 8 cast plus the six
Issue 7 leftovers):
- Sebastian — `faded-hero-voice`
- M. Voss, Investigations Desk — `code-theft-dossier`
- Garfield — `canon-fanfic-vignette` (Persona 3)
- Wren — `yearning-machine-voice`
- Te Mana Whakaatu classifieds format — `te-mana-whakaatu-classifieds`
- Robin Leach — `champagne-wishes-dispatch`
- Baxter Kline — `the-world-bulletin-anchor`
- The Stickybeak — `tabloid-gossip-voice` (first time this persona has
  actually run in an archived issue, despite being roster-eligible since
  its own skill was written)

**Not used this issue** (available first for Issue 11): Luke Skywalker,
Daffy Duck and Alan Grant — the remaining Issue 8 canon-fanfic-vignette
personas Issue 10 didn't reach — plus Winnie Zhao, Dana Foley and Clem
Whitlock, still waiting since Issue 7, plus the entire Issue 9 rotating
roster (Priya Anand, Sherman McCoy, Shaggy & Scooby, T. Marlow, Steve
Jobs, Lewis Hamilton, Rebecca Black, Richard Nixon), which Issue 10's
shrunk exclusion window leaves untouched. Kate Rodgers and Freya Wilcox
remain standing roster members, available any issue but not run this
issue.

**Pool note for whoever assembles Issue 11:** exclude only Issue 10's
roster (immediately above) — that reopens the full Issue 9 cast plus
Luke Skywalker, Daffy Duck, Alan Grant, Winnie Zhao, Dana Foley and Clem
Whitlock. Menace Watch is due — right on schedule per the tracker (last
ran Issue 7); when it runs, it fills one of the 8 template slots rather
than adding a 9th (per Step 2b), so only 7 additional rotating personas
are needed alongside it.

---

## Issue 9

**Anchors:** community-outbreak-bulletin (Fenwick Grove hand-knitted
letterbox cozies) · ken-endo-puzzle-master (The Loyalty Card Check; also
fully resolves Issue 8's Correlation Desk suburb-ranking teaser) · bubble
tea trivia (popping boba's alginate-spherification chemistry, distinct
from tapioca) · joke of the week (mugged pun). No Menace Watch this issue
— ran Issue 7, not due again until roughly Issue 11.

**Cartoon slot (new biweekly alternation, Step 2c):** Hayaku's debut —
Rin Sakaguchi and Tomoya Ezaki, Kaede High, introduced mid-match. The Boba
Side sat out this issue after running every issue through Issue 8; it
returns next issue. **Redrawn 23 July 2026:** the debut panel was replaced
with a new hand-drawn original (a reaction close-up, a jump serve with
"SKIFF"/"HWWP" impact sound effects, a "SERVE!" line-judge call, and the
"TECH TEAM" scoreboard card) — cleaned up from a phone photo (levels
flattened, cropped tight to the drawn content) the same way the Boba Side
scans were. Alt text and byline in `issues/issue-9.html` updated to match;
`issue-9.pdf` reprinted, still 2 pages.

**Two new syndicated cartoons in the pipeline, not yet slotted into any
issue:** hand-drawn originals cleaned and staged in `issues/` ahead of
their debut issues. **Cat vs Dog**
(`issues/cat-vs-dog-issue10-debut.png`) — a domestic-sitcom gag pairing
("Behind the Scenes at Bubble Tea News," cat and dog watching TV on the
couch, "I love commercials!"), format varies panel-count issue to issue
(single panel this time, per house note — unlike The Boba Side, which
stays single-panel always). Slated to debut Issue 10. **Doki Doki Mon**
(`issues/doki-doki-mon-issue11-debut.png`) — a monster-collecting parody,
senkotsu four-panel format like Hayaku (trainer close-up, two creature
close-ups, one panel upside-down/foreshortened). Slated to debut Issue
11. Neither has a byline/alt-text entry yet since `issue-10.html` /
`issue-11.html` don't exist — whoever assembles those issues still needs
to pick the cartoon slot's alternation (Boba Side / Hayaku / one of these
two) and write the copy.

**Rotating slots** (per Issue 8's pool note — exclusion window shrunk to
Issue 8's roster only, reopening the full Issue 7 cast plus the Issue 6
and Issue 5 leftovers):
- Priya Anand, The Pearl Index — `pearl-index-market-researcher`
- Sherman McCoy — `master-of-the-universe-columnist`
- Shaggy & Scooby — `canon-fanfic-vignette` (Persona 2)
- T. Marlow — `lifeguards-eye-sportswriter`
- Steve Jobs — `reality-distortion-field-report`
- Lewis Hamilton — `grand-prix-showroom-ads`
- Rebecca Black — `long-game-music-review`
- Richard Nixon — `silent-majority-dispatch`

**Not used this issue** (available first for Issue 10): Sebastian, M.
Voss, Luke Skywalker, Daffy Duck, Alan Grant, Wren, Garfield and the Te
Mana Whakaatu classifieds format — Issue 8's roster, now reopened — plus
Robin Leach, Baxter Kline, Winnie Zhao, The Stickybeak, Dana Foley and
Clem Whitlock, still waiting since Issue 7. Kate Rodgers and Freya Wilcox
remain standing roster members, available any issue.

**Pool note for whoever assembles Issue 10:** exclude only Issue 9's
roster (immediately above) — that reopens the full Issue 8 cast plus the
six Issue-7 leftovers, comfortably more than enough for the rotating
slots. The Boba Side is due back in the cartoon slot (its new pycairo
register); Menace Watch still not due until roughly Issue 11.

---

## Issue 8

**Anchors:** community-outbreak-bulletin (Elmswood Avenue letterbox herb
gardens) · ken-endo-puzzle-master (The Correlation Desk; also fully
resolves Issue 7's Short Till) · bubble tea trivia (the 2017 Guinness
World Record 8,000-litre bubble tea) · joke of the week (large-pearl-count
pun). No Menace Watch this issue — ran Issue 7, not due again until
roughly Issue 11. **Debut:** Freya Wilcox, Design Editor, announced via a
masthead note (same treatment Kate Rodgers got in Issue 7) and launching
with a Design Desk column: she's started dating a volunteer at the Kowhai
Bay Animal Shelter, adopted a cat (Constable), and has begun correlating
Auckland cat-registration filings against Pearl Index bubble tea sales —
with the "data" visibly bleeding into the issue's own layout (an ad slot
replaced by her Fig. 1 scatter chart, r = 0.71). Garfield's Food & Drink
column ("Purrs & Pearls") reacts directly and unfavourably to being
treated as a data point; M. Voss's Investigations Desk separately flags
her methodology as suspiciously close to Priya Anand's Pearl Index format.
**Also added after initial publication:** the debut panel of The Boba
Side (`the-boba-side-cartoon`), Bubble Tea News's single-panel gag cartoon
slot — a clearly-labeled parody/homage to Gary Larson's one-panel style
(never titled "The Far Side," never presented as his real work). Not part
of the original Issue 8 roster count below; slotted onto the back page
afterward.

**Rotating slots** (per Issue 7's pool note — exclusion window shrunk to
Issue 7's roster only, reopening the full Issue 6 cast plus the five
Issue 5 leftovers):
- Sebastian — `faded-hero-voice`
- M. Voss, Investigations Desk — `code-theft-dossier`
- Luke Skywalker — `canon-fanfic-vignette` (Persona 1)
- Daffy Duck — `canon-fanfic-vignette` (Persona 5)
- Alan Grant — `canon-fanfic-vignette` (Persona 4)
- Wren — `yearning-machine-voice`
- Garfield — `canon-fanfic-vignette` (Persona 3)
- Te Mana Whakaatu classifieds format — `te-mana-whakaatu-classifieds`

**Not used this issue** (available first for Issue 9): Steve Jobs, Lewis
Hamilton and Rebecca Black — the three Issue 6 leftovers this issue's
slots didn't reach — plus Sherman McCoy, Shaggy & Scooby, T. Marlow and
Priya Anand, still waiting since Issue 5, plus the entire Issue 7 rotating
roster (Robin Leach, Baxter Kline, Richard Nixon, Winnie Zhao, The
Stickybeak, Dana Foley, Clem Whitlock), which Issue 8's shrunk exclusion
window leaves untouched. Kate Rodgers and Freya Wilcox are both standing
roster members and available any issue.

**Pool note for whoever assembles Issue 9:** exclude only Issue 8's roster
(immediately above) — that reopens the full Issue 7 cast plus the Issue 6
and Issue 5 leftovers, comfortably more than enough for the rotating
slots. Menace Watch not due until roughly Issue 11.

---

## Issue 7

**Anchors:** community-outbreak-bulletin (Bellevue Lane café trivia
leaderboard rivalry) · ken-endo-puzzle-master (The Short Till — the
library's first knights-and-knaves-style puzzle; also fully resolves
Issue 6's Sizing Queue) · bubble tea trivia (Hong Kong-style milk tea as a
separate, older tradition) · joke of the week (brew-tiful pun) ·
menace-watch-editorial, second appearance (Gordon Slate's "The Meadowbank
Swan," right on schedule per the tracker, cross-referencing Issue 6's
viral bent-straw fad). **Debut:** Kate Rodgers, film critic, announced via
a masthead note and launching with a New Release Roundup (Refill Rating).

**Rotating slots** (per Issue 6's pool note — exclusion window shrunk to
Issue 6's roster only, reopening Issue 5's full cast plus Robin Leach and
Baxter Kline):
- Robin Leach — `champagne-wishes-dispatch`
- Baxter Kline — `the-world-bulletin-anchor`
- Richard Nixon — `silent-majority-dispatch`
- Winnie Zhao — `seekers-eye-shopper`
- The Stickybeak — `tabloid-gossip-voice`
- Dana Foley — `epic-forecast-anchor`
- Clem Whitlock — `ridgeline-weekly-correspondent`

**Not used this issue** (available first for Issue 8): Sherman McCoy,
Shaggy & Scooby, T. Marlow, Garfield, Priya Anand — the five Issue 5
leftovers this issue's slots didn't reach — plus the entire Issue 6
rotating roster (Wren, Daffy Duck, Steve Jobs, Lewis Hamilton, Sebastian,
Luke Skywalker, Alan Grant, M. Voss, Rebecca Black, Te Mana Whakaatu
classifieds format), which Issue 7's shrunk exclusion window leaves
untouched.

**Pool note for whoever assembles Issue 8:** exclude only Issue 7's roster
(immediately above) — that reopens the full Issue 6 cast plus the five
Issue 5 leftovers, comfortably more than enough for the rotating slots.
Kate Rodgers is now a standing roster member (not exclusion-bound on her
debut issue, per house practice for first appearances) and can run again
whenever her byline fits.

---

## Issue 6

**Anchors:** community-outbreak-bulletin (Meadowbank Strip hand-bent
novelty straws, incl. the viral "swan") · ken-endo-puzzle-master (The
Sizing Queue) · bubble tea trivia (the "bubble" possibly naming the shaken
froth, not the pearls) · joke of the week (roll-with-it pun). No Menace
Watch this issue — per the tracker, not due until Issue 7; the puzzle desk
also honestly notes it can't resolve Issue 5's "which store restocked the
cup lids?" teaser, since only two of at least three stores were ever
printed — same house rule as Issues 1 and 2.

**Rotating slots** (per Issue 5's pool note — reopens the full Issue 4
cast plus Robin Leach and Baxter Kline, of which Leach and Kline were held
back again for Issue 7):
- Wren — `yearning-machine-voice`
- Daffy Duck — `canon-fanfic-vignette` (Persona 5)
- Steve Jobs — `reality-distortion-field-report`
- Lewis Hamilton — `grand-prix-showroom-ads`
- Sebastian — `faded-hero-voice`
- Luke Skywalker — `canon-fanfic-vignette` (Persona 1)
- Alan Grant — `canon-fanfic-vignette` (Persona 4)
- M. Voss — `code-theft-dossier`
- Rebecca Black — `long-game-music-review`
- Te Mana Whakaatu classifieds format — `te-mana-whakaatu-classifieds`

**Not used this issue** (available first for Issue 7): Robin Leach and
Baxter Kline, still waiting since Issue 3, plus the entire Issue 5
rotating roster (Richard Nixon, Sherman McCoy, Shaggy & Scooby, Priya
Anand, Winnie Zhao, The Stickybeak, Dana Foley, T. Marlow, Garfield, Clem
Whitlock), which Issue 6's exclusion window leaves untouched.

**Pool note for whoever assembles Issue 7:** exclude only Issue 6's roster
(immediately above) — that reopens the full Issue 5 cast plus Robin Leach
and Baxter Kline, comfortably more than enough for the rotating slots, and
Menace Watch is due back on schedule.

---

## Issue 5

**Anchors:** community-outbreak-bulletin (Kowhai Close front-fence pun war) ·
ken-endo-puzzle-master (The Topping Trade; also fully resolves Issue 4's
Delivery Manifest condensed-milk teaser) · bubble tea trivia (brown sugar
boba's syrup-cooked colour, via Tiger Sugar) · joke of the week
(shake-things-up pun). No Menace Watch this issue — not due until roughly
Issue 7. First paid ad this issue: one ad box carries a real advertiser,
Overload NZ 2026 (26–27 Sept, NZ International Convention Centre), sold on
the back of Priya Anand's own cross-tab finding this issue (46% of Swing
Patrons also attend a convention/expo yearly) — the other two ad boxes
stayed plain "Your Ad Here" placeholders.

**Rotating slots** (per Issue 4's pool note — exclusion window shrunk to
Issue 4's roster only, reopening Issue 3's full cast plus the Issue 2
leftovers):
- Richard Nixon — `silent-majority-dispatch`
- Sherman McCoy — `master-of-the-universe-columnist`
- Shaggy & Scooby — `canon-fanfic-vignette` (Persona 2)
- Priya Anand, second bylined report — `pearl-index-market-researcher`
- Winnie Zhao — `seekers-eye-shopper`
- The Stickybeak — `tabloid-gossip-voice`
- Dana Foley — `epic-forecast-anchor`
- T. Marlow — `lifeguards-eye-sportswriter`
- Garfield — `canon-fanfic-vignette` (Persona 3)
- Clem Whitlock — `ridgeline-weekly-correspondent`

**Not used this issue** (available first for Issue 6): Robin Leach and
Baxter Kline — the two Issue 3 leftovers this issue's slots didn't reach —
plus the entire Issue 4 rotating roster (M. Voss, Rebecca Black, Sebastian,
Steve Jobs, Luke Skywalker, Daffy Duck, Alan Grant, Lewis Hamilton, Wren,
Te Mana Whakaatu classifieds format), which Issue 5's shrunk exclusion
window leaves untouched.

**Pool note for whoever assembles Issue 6:** exclude only Issue 5's roster
(immediately above) — that reopens the full Issue 4 cast plus Robin Leach
and Baxter Kline, comfortably more than enough for the ~10 rotating slots.

---

## Issue 4

**Anchors:** community-outbreak-bulletin (Birchfield Apartments balcony
fairy-light canopy escalation) · ken-endo-puzzle-master (The Delivery
Manifest; also fully resolves Issue 3's Grover Street Line-Up) · bubble
tea trivia (Chun Shui Tang vs. Hanlin Tea Room origin dispute) · joke of
the week (fair-shake pun). No Menace Watch this issue — per the tracker
above, not due until roughly Issue 7; both ad boxes ran as plain "Your Ad
Here" placeholders since Priya Anand didn't run this issue either.

**Rotating slots** (per Issue 3's pool note — Issue 2's full cast reopened,
plus Issue 3's three leftovers):
- M. Voss, Investigations Desk — `code-theft-dossier`
- Rebecca Black — `long-game-music-review`
- Sebastian — `faded-hero-voice`
- Steve Jobs — `reality-distortion-field-report`
- Luke Skywalker — `canon-fanfic-vignette` (Persona 1)
- Daffy Duck — `canon-fanfic-vignette` (Persona 5)
- Alan Grant — `canon-fanfic-vignette` (Persona 4)
- Lewis Hamilton — `grand-prix-showroom-ads`
- Wren — `yearning-machine-voice`
- Te Mana Whakaatu classifieds format — `te-mana-whakaatu-classifieds`

**Not used this issue** (available first for Issue 5): Shaggy & Scooby,
Winnie Zhao (`seekers-eye-shopper`), T. Marlow (`lifeguards-eye-sportswriter`)
— the three Issue 2 personas left over — plus the entire Issue 3 rotating
roster (Richard Nixon, Sherman McCoy, Robin Leach, Garfield, Clem
Whitlock, The Stickybeak, Baxter Kline, Priya Anand, Dana Foley), which
Issue 4's shrunk exclusion window leaves untouched.

**Pool note for whoever assembles Issue 5:** exclude only Issue 4's roster
(immediately above) — that reopens the full Issue 3 cast plus the three
Issue 2 leftovers, comfortably more than enough for the ~10 rotating slots.

---

## Issue 3

**Anchors:** menace-watch-editorial, debut (Gordon Slate's "Menace Watch" —
the Fetchly delivery mascot, caught mid-shift eating hamburgers at
Re:Burger, declared a menace anyway; not due again until roughly Issue 7,
per this anchor's monthly cadence) · community-outbreak-bulletin (Grover
Street mascot-costume escalation) · ken-endo-puzzle-master (The Grover
Street Line-Up; also resolves Issue 2's Counter Queue as far as its
printed clues allow, without inventing the unprinted rest) · bubble tea
trivia (boba as Cantonese slang vs. Taiwanese zhenzhu) · joke of the week
(read-the-leaves pun)

**Rotating slots** (per Issue 2's pool note, exclusion window shrunk to
Issue 2's roster only — Issue 1's cast made eligible again):
- Richard Nixon — `silent-majority-dispatch`
- Sherman McCoy — `master-of-the-universe-columnist`
- Robin Leach — `champagne-wishes-dispatch`
- Garfield — `canon-fanfic-vignette` (Persona 3)
- Clem Whitlock — `ridgeline-weekly-correspondent`
- The Stickybeak — `tabloid-gossip-voice`
- Baxter Kline — `the-world-bulletin-anchor`
- Priya Anand, first appearance as a bylined column (previously only the
  ad-box format had run) — `pearl-index-market-researcher`
- Dana Foley — `epic-forecast-anchor`

**Not used this issue** (available first for Issue 4): Lewis Hamilton,
Steve Jobs, Te Mana Whakaatu classifieds format — plus the entire Issue 2
rotating roster (Sebastian, Luke Skywalker, Shaggy &amp; Scooby, Alan
Grant, Daffy Duck, Wren, legal-affairs investigator, Seeker-eyed shopper,
ex-lifeguard sportswriter, Rebecca Black), which Issue 3's shrunk
exclusion window leaves untouched.

**Pool note for whoever assembles Issue 4:** exclude only Issue 3's roster
(immediately above) — that reopens the full Issue 2 cast plus the three
Issue-3 leftovers, comfortably more than enough for the ~9 rotating slots.

---

## Issue 2

**Anchors:** community-outbreak-bulletin (Fernhill Heights letterbox
bunting escalation) · ken-endo-puzzle-master (The Counter Queue; also
resolves Issue 1's Four Puzzlers, which never named a fourth drink for
Ava — noted rather than invented) · bubble tea trivia (tapioca/cassava
origin) · joke of the week (spill-the-tea pun)

**Rotating slots** (all 10 personas held back from Issue 1, per that
issue's exclusion note):
- Sebastian — `faded-hero-voice`
- Luke Skywalker — `canon-fanfic-vignette` (Persona 1)
- Shaggy & Scooby — `canon-fanfic-vignette` (Persona 2)
- Alan Grant — `canon-fanfic-vignette` (Persona 4)
- Daffy Duck — `canon-fanfic-vignette` (Persona 5)
- Wren — `yearning-machine-voice`
- Legal-affairs investigator (M. Voss) — `code-theft-dossier`
- Personal shopper (Winnie Zhao) — `seekers-eye-shopper`
- Ex-lifeguard sportswriter (T. Marlow) — `lifeguards-eye-sportswriter`
- Rebecca Black — `long-game-music-review`

**Not used this issue** (available first for Issue 3): the entire
Issue 1 rotating roster — Richard Nixon, Sherman McCoy, Steve Jobs,
Baxter Kline, Robin Leach, Garfield, Clem Whitlock, The Stickybeak, Te
Mana Whakaatu classifieds format, Lewis Hamilton, Dana Foley.

**Pool note for whoever assembles Issue 3:** after two issues, every
rotating-eligible persona has now run once — a strict 2-issue exclusion
window would leave zero available. Per this skill's own fallback rule
("if the rotation pool ever gets small enough... shrink the exclusion
window"), Issue 3 should exclude only Issue 2's roster (immediately
above), making all of Issue 1's cast available again.

---

## Issue 1

**Anchors:** community-outbreak-bulletin (Willowmere gnome outbreak) ·
ken-endo-puzzle-master (The Four Puzzlers) · bubble tea trivia (pearl milk
tea origin) · joke of the week (tapioca pun)

**Rotating slots:**
- Richard Nixon — `silent-majority-dispatch`
- Sherman McCoy — `master-of-the-universe-columnist`
- Steve Jobs — `reality-distortion-field-report`
- Baxter Kline — `the-world-bulletin-anchor`
- Robin Leach — `champagne-wishes-dispatch`
- Garfield — `canon-fanfic-vignette` (Persona 3)
- Clem Whitlock — `ridgeline-weekly-correspondent`
- The Stickybeak — `tabloid-gossip-voice`
- Te Mana Whakaatu classifieds format — `te-mana-whakaatu-classifieds`
- Lewis Hamilton — `grand-prix-showroom-ads`
- Dana Foley — `epic-forecast-anchor`

**Not used this issue** (available first for Issue 2): Sebastian, Luke
Skywalker, Shaggy & Scooby, Alan Grant, Daffy Duck, Wren, legal-affairs
investigator (`code-theft-dossier`), Seeker-eyed shopper
(`seekers-eye-shopper`), ex-lifeguard sportswriter
(`lifeguards-eye-sportswriter`), Rebecca Black.
