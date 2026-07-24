# Live-site promotion queue

Staged web-showcase files for future issues, promoted onto the public
site (`index.html`, `print-edition.html`, and their `docs/` mirrors) only
when that issue's dateline arrives.

| Queue dir | Issue | Dateline (NZ) | How it goes live |
|---|---|---|---|
| `issue-13/` | 13 | 9 October 2026 | `.github/workflows/promote-issue-13.yml` + `scripts/promote-live-issue.py` |

## Layout of a queue entry

```
live-queue/issue-N/
  index.html           # required — web showcase (hand-built teasers)
  print-edition.html   # optional — if missing, built from issues/issue-N.html
```

`print-edition.html` image paths should either already use `issues/...`
or be bare filenames that exist under `issues/`; the promote script
rewrites them and copies the assets into `docs/issues/` for GitHub Pages.

## Manual promote (local)

```bash
# Dry-run
python3 scripts/promote-live-issue.py --issue 13 --dry-run --force

# Write files only (no commit)
python3 scripts/promote-live-issue.py --issue 13 --force

# Write + commit + push (same as CI)
python3 scripts/promote-live-issue.py --issue 13 \
  --require-on-or-after 2026-10-09 \
  --skip-if-live-at-least 13 \
  --commit --push
```

## CI

The scheduled workflow fires at **20:00 UTC on 8 October** (09:00 NZDT
on 9 October). Because GitHub cron cannot encode a year, the script
guards on the NZ calendar date and on "already live ≥ 13", so later
years and re-runs are no-ops. You can also trigger it from the Actions
tab (`workflow_dispatch`); set `force_promote` only if you intend to
publish early.
