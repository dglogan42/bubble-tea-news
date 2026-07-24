#!/usr/bin/env python3
"""Promote a staged (or archive-built) issue to the live showcase.

Live files:
  print-edition.html, index.html  (repo root)
  docs/print-edition.html, docs/index.html, docs/issues/*  (GitHub Pages)

By default this promotes Issue 13 from live-queue/issue-13/, rewriting image
paths so archive assets under issues/ resolve both at the repo root and under
docs/ on GitHub Pages.

Guards (all on by default for scheduled runs):
  --require-on-or-after YYYY-MM-DD   NZ calendar date must be on/after this
  --skip-if-live-at-least N         no-op if live already shows issue >= N

Usage examples:
  # Dry-run (writes nothing):
  python3 scripts/promote-live-issue.py --issue 13 --dry-run

  # Local promote (no commit):
  python3 scripts/promote-live-issue.py --issue 13 --force

  # CI promote + commit + push:
  python3 scripts/promote-live-issue.py --issue 13 \\
    --require-on-or-after 2026-10-09 --skip-if-live-at-least 13 \\
    --commit --push
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parent.parent
NZ = ZoneInfo("Pacific/Auckland")

IMG_SRC_RE = re.compile(r'''(?P<prefix>\bsrc\s*=\s*["'])(?P<path>[^"']+)(?P<suffix>["'])''')
ISSUE_NUM_RE = re.compile(
    r"""Issue\s+(\d+)\s*[·.]\s*\d+\s+\w+\s+\d{4}"""
    r"""|Edition\s+No\.\s*(\d+)"""
    r"""|Print Edition\s*[—-]\s*Issue\s+(\d+)"""
    r"""|This week's edition\s*&mdash;\s*Issue\s+(\d+)""",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--issue", type=int, default=13, help="Issue number to promote (default: 13)")
    p.add_argument(
        "--queue-dir",
        type=Path,
        default=None,
        help="Staged content dir (default: live-queue/issue-N). Must contain index.html; "
        "print-edition.html is optional (built from issues/issue-N.html if missing).",
    )
    p.add_argument(
        "--require-on-or-after",
        type=str,
        default=None,
        help="Pacific/Auckland calendar date YYYY-MM-DD that must have arrived (or --force).",
    )
    p.add_argument(
        "--skip-if-live-at-least",
        type=int,
        default=None,
        help="Exit 0 without writing if live already shows this issue number or higher.",
    )
    p.add_argument("--force", action="store_true", help="Bypass date and already-live guards.")
    p.add_argument("--dry-run", action="store_true", help="Print actions only; do not write files.")
    p.add_argument("--commit", action="store_true", help="git add + commit if there are changes.")
    p.add_argument("--push", action="store_true", help="git push origin HEAD after commit.")
    p.add_argument(
        "--update-rotation-log",
        action="store_true",
        default=True,
        help="Append a live-site note to rotation-log.md (default: on).",
    )
    p.add_argument("--no-update-rotation-log", action="store_false", dest="update_rotation_log")
    return p.parse_args()


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=REPO_ROOT, check=check, text=True, capture_output=True)


def detect_live_issue() -> int | None:
    pe = REPO_ROOT / "print-edition.html"
    if not pe.exists():
        return None
    text = pe.read_text(encoding="utf-8", errors="replace")
    for m in ISSUE_NUM_RE.finditer(text):
        for g in m.groups():
            if g:
                return int(g)
    title = re.search(r"<title>([^<]+)</title>", text, re.I)
    if title:
        m = re.search(r"Issue\s+(\d+)", title.group(1), re.I)
        if m:
            return int(m.group(1))
    return None


def nz_today() -> date:
    return datetime.now(tz=NZ).date()


def parse_ymd(s: str) -> date:
    return date.fromisoformat(s)


def rewrite_print_html(src_html: str, issue: int) -> tuple[str, list[str]]:
    """Rewrite archive issue HTML for live root / docs/ placement.

    Returns (html, asset basenames that must be copied into docs/issues/).
    """
    assets: list[str] = []

    def repl(m: re.Match) -> str:
        path = m.group("path")
        # Already correct live path
        if path.startswith("issues/"):
            assets.append(Path(path).name)
            return m.group(0)
        # Skip absolute / data / external
        if path.startswith(("http://", "https://", "data:", "/", "#")):
            return m.group(0)
        name = Path(path).name
        candidate = REPO_ROOT / "issues" / name
        if candidate.is_file():
            assets.append(name)
            return f'{m.group("prefix")}issues/{name}{m.group("suffix")}'
        return m.group(0)

    html = IMG_SRC_RE.sub(repl, src_html)

    # Normalize <title>
    html = re.sub(
        r"<title>[^<]*</title>",
        f"<title>Bubble Tea News — Print Edition — Issue {issue}</title>",
        html,
        count=1,
        flags=re.I,
    )

    # Prefer a short print-setup line over the long assembly blurb if present
    html = re.sub(
        r"(This week's edition\s*&mdash;\s*Issue\s+)\d+",
        rf"\g<1>{issue}",
        html,
        count=1,
        flags=re.I,
    )

    # Drop stale "text-only placeholder" claim if real art is wired
    if f"hayaku-issue-{issue}.png" in html or "hayaku-issue-13.png" in html:
        html = html.replace(
            "but no new source photo was available this round &mdash; it runs as a labelled\n"
            "    text-only placeholder rather than reusing Issue 9's debut art. ",
            "with actual source art (`issues/hayaku-issue-13.png`) rather than reusing Issue 9's debut. ",
        )
        # single-line variant
        html = re.sub(
            r"but no new source photo was available this round[^.]+\.\s*",
            "with actual source art rather than reusing Issue 9's debut. ",
            html,
            count=1,
        )

    # Dedupe asset list preserving order
    seen: set[str] = set()
    ordered: list[str] = []
    for a in assets:
        if a not in seen:
            seen.add(a)
            ordered.append(a)
    return html, ordered


def load_print_edition(issue: int, queue_dir: Path) -> tuple[str, list[str]]:
    staged = queue_dir / "print-edition.html"
    if staged.is_file():
        html = staged.read_text(encoding="utf-8")
        # Still collect assets via rewrite pass (idempotent if already rewritten)
        return rewrite_print_html(html, issue)

    archive = REPO_ROOT / "issues" / f"issue-{issue}.html"
    if not archive.is_file():
        raise SystemExit(f"Missing archive issue HTML: {archive} (and no staged print-edition.html)")
    return rewrite_print_html(archive.read_text(encoding="utf-8"), issue)


def load_index(issue: int, queue_dir: Path) -> str:
    staged = queue_dir / "index.html"
    if not staged.is_file():
        raise SystemExit(
            f"Missing staged web showcase: {staged}\n"
            f"Hand-build index.html for Issue {issue} under live-queue/issue-{issue}/ before promoting."
        )
    return staged.read_text(encoding="utf-8")


def write_file(path: Path, content: str, dry_run: bool) -> None:
    print(f"  write {path.relative_to(REPO_ROOT)} ({len(content)} bytes)")
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def copy_asset(name: str, dry_run: bool) -> None:
    src = REPO_ROOT / "issues" / name
    dest = REPO_ROOT / "docs" / "issues" / name
    if not src.is_file():
        raise SystemExit(f"Required asset missing: {src}")
    print(f"  copy  issues/{name} -> docs/issues/{name} ({src.stat().st_size} bytes)")
    if not dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


def patch_rotation_log(issue: int, dateline_note: str, dry_run: bool) -> None:
    path = REPO_ROOT / "rotation-log.md"
    text = path.read_text(encoding="utf-8")
    marker = f"**Issue {issue} refresh pushed live"
    if marker in text:
        print("  rotation-log.md already notes this refresh; leaving as-is")
        return

    stamp = datetime.now(tz=NZ).strftime("%-d %B %Y")
    insertion = (
        f"**Live-site note:** the public showcase (`index.html`/`docs/`) tracks real\n"
        f"calendar time, not the archive. **Issue {issue} refresh pushed live {stamp}** "
        f"({dateline_note}): `print-edition.html`, `index.html`, and their `docs/` mirrors "
        f"now show Issue {issue} (matching `issues/issue-{issue}.html`), via the scheduled "
        f"`promote-live-issue` workflow / `scripts/promote-live-issue.py`.\n\n"
    )

    # Prefer replacing the existing Live-site note block's first paragraph if present
    live_re = re.compile(
        r"\*\*Live-site note:\*\*.*?(?=\n\n\*\*|\n\n## |\Z)",
        re.DOTALL,
    )
    if live_re.search(text):
        # Prepend a short addendum after the existing note's first sentence block
        # by inserting right after the live-site paragraph.
        new_text, n = live_re.subn(
            lambda m: m.group(0).rstrip()
            + f"\n\n**Issue {issue} refresh pushed live {stamp}** ({dateline_note}): "
            f"`print-edition.html`, `index.html`, and their `docs/` mirrors now show Issue {issue} "
            f"(matching `issues/issue-{issue}.html`), via `scripts/promote-live-issue.py` / "
            f"`.github/workflows/promote-issue-13.yml`.",
            text,
            count=1,
        )
        if n:
            print("  patch rotation-log.md (append to Live-site note)")
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
            return

    # Fallback: insert near top after the intro paragraph
    print("  patch rotation-log.md (insert live-site note)")
    if not dry_run:
        path.write_text(insertion + text, encoding="utf-8")


def git_commit_and_push(issue: int, do_commit: bool, do_push: bool, dry_run: bool) -> None:
    if not do_commit:
        return
    status = run(["git", "status", "--porcelain"])
    if not status.stdout.strip():
        print("No git changes to commit.")
        return
    files = [
        "print-edition.html",
        "index.html",
        "docs/print-edition.html",
        "docs/index.html",
        "docs/issues",
        "rotation-log.md",
    ]
    print("  git add", " ".join(files))
    if not dry_run:
        run(["git", "add", "--"] + files)
        msg = (
            f"Refresh the live site to Issue {issue}\n\n"
            f"print-edition.html, index.html, and their docs/ mirrors now show Issue {issue}'s\n"
            f"content (matching issues/issue-{issue}.html). Assets required by the print\n"
            f"edition were copied into docs/issues/ for GitHub Pages.\n\n"
            f"Promoted by scripts/promote-live-issue.py on the Issue {issue} dateline.\n"
        )
        run(["git", "commit", "-m", msg])
        print("  committed")
    if do_push:
        print("  git push origin HEAD")
        if not dry_run:
            # Prefer authenticated remote; GITHUB_TOKEN is set in Actions
            env = os.environ.copy()
            result = subprocess.run(
                ["git", "push", "origin", "HEAD"],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                env=env,
            )
            if result.returncode != 0:
                print(result.stdout)
                print(result.stderr, file=sys.stderr)
                raise SystemExit(f"git push failed ({result.returncode})")
            print("  pushed")


def main() -> int:
    args = parse_args()
    issue = args.issue
    queue_dir = (args.queue_dir or (REPO_ROOT / "live-queue" / f"issue-{issue}")).resolve()

    print(f"promote-live-issue: issue={issue} queue={queue_dir.relative_to(REPO_ROOT)}")
    print(f"  NZ today: {nz_today().isoformat()}  UTC now: {datetime.now(timezone.utc).isoformat()}")

    live = detect_live_issue()
    print(f"  currently live: Issue {live if live is not None else 'unknown'}")

    if not args.force and args.skip_if_live_at_least is not None and live is not None:
        if live >= args.skip_if_live_at_least:
            print(
                f"Skip: live already at Issue {live} (>= {args.skip_if_live_at_least}). "
                "Nothing to do."
            )
            return 0

    if not args.force and args.require_on_or_after:
        threshold = parse_ymd(args.require_on_or_after)
        today = nz_today()
        if today < threshold:
            print(
                f"Skip: NZ date {today.isoformat()} is before required "
                f"{threshold.isoformat()}. Use --force to override."
            )
            return 0

    if not queue_dir.is_dir():
        raise SystemExit(f"Queue dir missing: {queue_dir}")

    print_html, assets = load_print_edition(issue, queue_dir)
    index_html = load_index(issue, queue_dir)

    print("Actions:")
    write_file(REPO_ROOT / "print-edition.html", print_html, args.dry_run)
    write_file(REPO_ROOT / "docs" / "print-edition.html", print_html, args.dry_run)
    write_file(REPO_ROOT / "index.html", index_html, args.dry_run)
    write_file(REPO_ROOT / "docs" / "index.html", index_html, args.dry_run)
    for name in assets:
        copy_asset(name, args.dry_run)

    if args.update_rotation_log:
        dateline = f"on/after Issue {issue} dateline"
        if args.require_on_or_after:
            dateline = f"dateline {args.require_on_or_after} NZ"
        patch_rotation_log(issue, dateline, args.dry_run)

    git_commit_and_push(issue, args.commit, args.push, args.dry_run)
    print("Done." + (" (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
