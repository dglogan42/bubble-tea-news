# Bubble Tea News

A fictional weekly print-and-digital freesheet for Auckland's bubble tea
scene — Coffee-News-style: a rotating cast of satirical columnists, a
real-feeling market-research section, a standing "Menace Watch" editorial
bit, a single-panel gag cartoon, and a new issue every week.

This repo holds the actual published product — every issue, the live
website, and print-ready PDFs. The content is generated using a companion
library of reusable writing "skills" at
[`dglogan42/Claude-Skills`](https://github.com/dglogan42/Claude-Skills)
(see `bubble-tea-news-editor` there for how a new issue gets assembled).
The two repos are kept separate so the published newspaper and the skills
that write it can be versioned and released independently.

## Layout

- **`issues/`** — the full archive (`issue-1.html` … `issue-N.html`, each
  with a matching `.pdf`), one weekly issue per file, dated 17 July 2026
  plus 7 days per issue. Print-ready via the browser Print dialog (A4, no
  margins, flip on the long edge for double-sided).
- **`rotation-log.md`** — tracks which personas ran in each issue (so the
  roster doesn't repeat week to week), the monthly "Menace Watch" cadence,
  and persona-debut history. Read this before assembling the next issue.
- **`site/`** — the fuller bubbletea.nz website build: archive, the
  current issue, The Desk (columnist directory), Pearl Index, Puzzle
  Corner, pickup locations, subscribe, advertise, about. See
  `site/README.md` for that build's own status and open items.
- **`print-edition.html`** / **`index.html`** — the live showcase.
  **Calendar-locked**: these only ever show whichever issue's in-fiction
  dateline matches today's real date, so future issues already sitting in
  `issues/` aren't spoiled early. Check `rotation-log.md`'s live-site note
  for which issue is currently pinned here.
- **`docs/`** — mirrors `print-edition.html` and `index.html` for GitHub
  Pages. Re-copy both files into `docs/` after any future edit to the
  top-level copies — not auto-synced.
- **`business-card.html`** / **`.pdf`** — print-ready business card.
- **`gongcha-pitch.html`** / **`.pdf`** — a draft partnership-pitch
  one-pager for a retail distribution partner.

## Live site

Deployed via GitHub Pages from `docs/` on `main`, with `bubbletea.nz` as
the custom domain (DNS pointed at GitHub Pages' four A records:
`185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
`185.199.111.153`).

## Content disclaimer

All content is satire/character-voice fiction. Original personas
(Gordon Slate, Freya Wilcox, Sebastian, Wren, and others) are wholly
invented. Pieces built around real people or existing franchises — Richard
Nixon, Steve Jobs, Lewis Hamilton, Robin Leach, Rebecca Black, Kate
Rodgers's Refill Rating, Luke Skywalker, Shaggy & Scooby-Doo, Daffy Duck,
Te Mana Whakaatu — are
clearly labeled parody/homage with a non-affiliation and non-endorsement
disclaimer, per that persona's originating skill in
`dglogan42/Claude-Skills`. All headlines, quotes, market-research figures,
and business names are illustrative examples, not real news, real survey
data, or real endorsements (Overload NZ 2026 excepted — a real, named
convention run as this paper's first actual paid ad placement).

## License

MIT for the code, layout, and original written content — see `LICENSE`.
Does not cover the third-party names/trademarks referenced above.
