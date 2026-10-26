---
name: bubble-tea-news
description: "Data folder for the Bubble Tea News paper itself (issue archive, print template, rotation log, website, print PDFs). Not a writing skill. Use only to locate or read published issues, the rotation log or the site files; to make a new issue, use bubble-tea-news-editor."
---
# Bubble Tea News (paper repo, data only)

This folder is the checked-out `dglogan42/bubble-tea-news` repo. `bubble-tea-news-editor` treats it as `PAPER_DIR` (its default is the sibling folder `../bubble-tea-news/`). This file only exists so the skills loader stops seeing the folder as broken.

## What's here
- `issues/`: issue-1 to issue-21 (HTML and PDF) plus the comic-strip and ad art.
- `rotation-log.md`: which personas ran in each issue. Read it before assembling a new issue.
- `print-edition.html` and `index.html`: the print template and web showcase. `docs/` mirrors them for GitHub Pages and has to be re-copied by hand after edits.
- `site/`: the fuller bubbletea.nz site build and its page copy.
- `live-queue/`, `scripts/promote-live-issue.py` and `.github/workflows/promote-issue-13.yml`: the auto-promotion of staged issues.
- `business-card.*`, `gongcha-pitch.*`, `Overload.html`, `ad-overload-expo.html`: print collateral and a draft partnership pitch.
- `Horoscope.md`, `Lewis Hamilton Commentary.txt`, `WordBounds.txt`, `namespace.txt` (a PowerShell word-cloud script for the Pearl Index), `senkotsu.YAML`: working notes and assets.

## Rules
- Reading is fine. To write a new issue, follow `bubble-tea-news-editor`.
- Don't commit, push, edit the Pages workflow or change DNS without David's OK. A push to `main` publishes to bubbletea.nz.
- Everything in the paper is satire or character fiction. Keep the non-affiliation disclaimers on any piece about a real person or brand.
