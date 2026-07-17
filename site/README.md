# bubbletea.nz site build

This is the working build of the real **bubbletea.nz** marketing site — distinct
from `../index.html` (the all-personas skill showcase) and `../gongcha-pitch.html`
(the standalone Gong Cha partnership proposal).

## Status

- `index.html` — Home page. Built and functional.
- `latest-issue.html` — Full web rendition of the current issue (Issue 2),
  front/back-page two-tone layout mirroring the print edition. Built and functional.
- `page-copy-*.md` — Written copy for every other page in the sitemap
  (Archive, The Desk, Puzzle Corner, Pearl Index, Advertise, Pickup Locations,
  About, Subscribe). Not yet built as HTML.
- `pickup-locations.md` — Data file tracking confirmed and prospective
  pickup stores (currently: Gong Cha Botany Town Centre, both Issue 1 and
  Issue 2 in stock; chain-wide Gong Cha Auckland rollout is the target —
  see `../gongcha-pitch.html` for the outreach piece).

## Open items before this goes live

- Ad rates are unset (`page-copy-advertise.md` has placeholders only).
- No public contact address exists yet (`page-copy-about.md` flags this).
- Internal links between pages (`the-desk.html`, `archive.html`, etc.)
  point to filenames that don't exist until those pages are built.
- No email service wired up for Subscribe.

## Design system

Same taro-purple / brown-sugar duotone as `../business-card.html`
(`--taro-bg: #E4D9EC`, `--taro-ink: #4A2E63`, `--sugar-bg: #F0DCC0`,
`--sugar-ink: #6B4419`), extended into a full type/spacing scale for the
web. `latest-issue.html` reuses the print edition's front-page/back-page
split as full-bleed color zones rather than a card-based layout, so it
reads as the online twin of the actual print object.
