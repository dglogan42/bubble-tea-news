# bubbletea.nz site build

This is the working build of the real **bubbletea.nz** marketing site — distinct
from `../index.html` (the all-personas skill showcase) and `../gongcha-pitch.html`
(the standalone Gong Cha partnership proposal).

## Status

All ten sitemap pages are built and fully cross-linked (no dead internal links):

- `index.html` — Home
- `latest-issue.html` — Full web rendition of the current issue (Issue 2),
  front/back-page two-tone layout mirroring the print edition. Treat this as
  a template: its body should be replaced wholesale each new issue.
- `issue-1.html` — Frozen snapshot of Issue 1, same layout as `latest-issue.html`,
  for archive purposes now that Issue 1 is no longer current.
- `archive.html` — Back-issue index (Issue 1 + Issue 2 so far)
- `the-desk.html` — Columnist directory, all 21 bylines grouped by beat, with
  a "This Week" badge on whoever's in the current issue
- `puzzle-corner.html` — Ken Endo's open puzzle + solved archive
- `pearl-index.html` — The market-research page behind every sponsor stat
- `advertise.html` — Retailer ad-slot pitch (Sponsor Box / Classifieds Line)
- `pickup-locations.html` — Where to find a print copy (Gong Cha Botany
  confirmed; chain-wide Gong Cha Auckland rollout as the target — see
  `../gongcha-pitch.html` for the outreach piece)
- `about.html` — What the paper is, satire/non-affiliation disclaimer, contact
- `subscribe.html` — Email capture (markup only, no backend wired up)
- `page-copy-*.md` — The original written-copy drafts each HTML page was built from

## Open items before this goes live

- **Ad rates are a first-draft proposal, not confirmed** — `advertise.html` has
  introductory rates (Sponsor Box: $35/issue, $120/4-issue, $324/12-issue;
  Classifieds Line: $12/issue, $40/4-issue), sized to current single-store
  circulation, added 2026-07-18. Review before actually taking payment —
  these were drafted, not sourced from real market research or David's
  explicit pricing decision. Rate is framed as locked-in-once-booked, rising
  as distribution grows (e.g. once the Gong Cha partnership lands).
- **Contact form is live but routes to a personal inbox** — `about.html` has a
  working form (Name/Email/Reason/Message) via FormSubmit.co, posting to
  David's personal email (david_logan_nz@outlook.com). No backend needed,
  but swap the destination to a dedicated address (e.g. hello@bubbletea.nz)
  once the domain and a real mailbox exist. Also: FormSubmit.co requires a
  one-time confirmation click on the first real submission before it starts
  forwarding — untested end-to-end as of 2026-07-18.
- **Subscribe has no backend** — the email form on `subscribe.html` posts to
  `#`. Needs a real email service (Mailchimp/Buttondown/etc.) before launch.
- **`latest-issue.html` needs a real update process** — right now it's Issue 2's
  content hardcoded. When Issue 3 ships, this page's body should be replaced,
  the old Issue 2 content should become a frozen `issue-2.html` (same pattern
  as `issue-1.html`), and `archive.html` should get a third card.
- Both issues' Sponsor Boxes (Milkwood Tea Co., Nine Cups Tea Bar) currently
  show identical stats across Issue 1 and Issue 2 — that matches what
  actually ran in both print PDFs, so it was kept consistent rather than
  invented differently per issue. Worth deciding whether that's an
  intentional recurring ad slot or should refresh per issue going forward.

## Design system

Same taro-purple / brown-sugar duotone as `../business-card.html`
(`--taro-bg: #E4D9EC`, `--taro-ink: #4A2E63`, `--sugar-bg: #F0DCC0`,
`--sugar-ink: #6B4419`), extended into a full type/spacing scale for the
web. `latest-issue.html` and `issue-1.html` reuse the print edition's
front-page/back-page split as full-bleed color zones rather than a
card-based layout, so they read as the online twin of the actual print
object. The other pages use a lighter card-based layout on a shared cream
paper background (`--paper: #E9E3D6`).
