#!/usr/bin/env python3
"""Utilities for searching and auditing the local Phaser docs corpus."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlparse

INVALID_SEGMENT_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def safe_segment(segment: str) -> str:
    text = unquote(segment).strip().lower()
    text = INVALID_SEGMENT_RE.sub("-", text).strip("-")
    return text or "index"


def url_to_relpath(url: str) -> Path:
    parsed = urlparse(url)
    host = safe_segment(parsed.netloc or "unknown-host")
    pieces = [safe_segment(piece) for piece in parsed.path.split("/") if piece]
    if not pieces:
        pieces = ["index"]
    if parsed.path.endswith("/"):
        pieces.append("index")
    if "." not in pieces[-1]:
        pieces[-1] = f"{pieces[-1]}.md"
    else:
        pieces[-1] = f"{Path(pieces[-1]).stem}.md"
    return Path(host, *pieces)


def root_candidates() -> list[Path]:
    candidates: list[Path] = []

    env_root = os.environ.get("PHASER_DOCS_PARSED_ROOT", "").strip()
    if env_root:
        candidates.append(Path(env_root))

    candidates.append(skill_root() / "references/corpus/docs.phaser.io")

    cwd = Path.cwd()
    for base in [cwd, *cwd.parents]:
        candidates.append(base / "docs/pages/parsed/docs.phaser.io")

    seen: set[str] = set()
    unique: list[Path] = []
    for item in candidates:
        key = str(item.resolve()) if item.exists() else str(item)
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def detect_root(explicit: str | None = None) -> Path:
    if explicit:
        root = Path(explicit)
        if root.exists():
            return root.resolve()
        raise FileNotFoundError(f"Docs root does not exist: {root}")

    for candidate in root_candidates():
        if candidate.exists() and candidate.is_dir():
            return candidate.resolve()

    lines = ["Could not locate docs root. Checked:"]
    for candidate in root_candidates():
        lines.append(f"- {candidate}")
    raise FileNotFoundError("\n".join(lines))


def detect_links_file(explicit: str | None, docs_root: Path) -> Path:
    if explicit:
        path = Path(explicit)
        if path.exists():
            return path.resolve()
        raise FileNotFoundError(f"Links file not found: {path}")

    links_env = os.environ.get("PHASER_DOCS_LINKS_FILE", "").strip()
    if links_env:
        path = Path(links_env)
        if path.exists():
            return path.resolve()

    cwd = Path.cwd()
    for base in [skill_root() / "references", cwd, *cwd.parents, docs_root.parent]:
        candidate = base / "documentation_links.txt"
        if candidate.exists():
            return candidate.resolve()

    raise FileNotFoundError(
        "Could not locate documentation_links.txt. Pass --links-file explicitly."
    )


def cmd_find_root(args: argparse.Namespace) -> int:
    root = detect_root(args.root)
    print(root)
    return 0


def cmd_section_report(args: argparse.Namespace) -> int:
    root = detect_root(args.root)
    files = sorted(root.rglob("*.md"))

    print(f"Root: {root}")
    print(f"Markdown files: {len(files)}")

    top = Counter()
    for path in files:
        rel = path.relative_to(root)
        top[rel.parts[0]] += 1

    print("\nTop-level sections:")
    for name, count in sorted(top.items()):
        print(f"- {name}: {count}")

    for section in ["api-documentation", "phaser"]:
        base = root / section
        if not base.exists():
            continue
        counter = Counter()
        for path in base.rglob("*.md"):
            rel = path.relative_to(base)
            counter[rel.parts[0]] += 1
        print(f"\n{section} subsections:")
        for name, count in sorted(counter.items()):
            print(f"- {name}: {count}")

    return 0


def run_rg(query: str, root: Path, smart_case: bool) -> str:
    cmd = ["rg", "-n", "--no-heading"]
    if smart_case:
        cmd.append("--smart-case")
    else:
        cmd.append("-i")
    cmd.extend([query, str(root)])

    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr.strip() or "rg failed")
    return proc.stdout


def cmd_search(args: argparse.Namespace) -> int:
    root = detect_root(args.root)
    query = args.query.strip()
    if not query:
        raise ValueError("--query cannot be empty")

    output = run_rg(query=query, root=root, smart_case=args.smart_case)
    if not output.strip():
        print("No matches")
        return 0

    file_hits: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for line in output.splitlines():
        parts = line.split(":", 2)
        if len(parts) != 3:
            continue
        file_path, line_no, snippet = parts
        try:
            n = int(line_no)
        except ValueError:
            continue
        file_hits[file_path].append((n, snippet.strip()))

    ranked = sorted(file_hits.items(), key=lambda item: len(item[1]), reverse=True)
    print(f"Root: {root}")
    print(f"Query: {query}")
    print(f"Matched files: {len(ranked)}")
    print("")

    for file_path, hits in ranked[: args.limit_files]:
        rel = Path(file_path).resolve().relative_to(root)
        print(f"{rel} (hits: {len(hits)})")
        for line_no, snippet in hits[: args.limit_snippets]:
            print(f"  L{line_no}: {snippet}")
        print("")

    return 0


def cmd_coverage(args: argparse.Namespace) -> int:
    root = detect_root(args.root)
    links_file = detect_links_file(args.links_file, root)

    urls: list[str] = []
    for raw in links_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not line.startswith(("http://", "https://")):
            continue
        urls.append(line)

    missing: list[tuple[str, Path]] = []
    for url in urls:
        rel = url_to_relpath(url)
        expected = root.parent / rel
        if not expected.exists():
            missing.append((url, expected))

    print(f"Docs root: {root}")
    print(f"Links file: {links_file}")
    print(f"URL rows: {len(urls)}")
    print(f"Missing parsed files: {len(missing)}")

    if missing:
        print("\nFirst missing entries:")
        for url, expected in missing[: args.limit_missing]:
            print(f"- {url}")
            print(f"  expected: {expected}")
        return 2

    print("Coverage OK")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Phaser docs corpus helper")
    sub = parser.add_subparsers(dest="command", required=True)

    p_find = sub.add_parser("find-root", help="Print resolved corpus root")
    p_find.add_argument("--root", help="Explicit corpus root")
    p_find.set_defaults(func=cmd_find_root)

    p_report = sub.add_parser("section-report", help="Show corpus section counts")
    p_report.add_argument("--root", help="Explicit corpus root")
    p_report.set_defaults(func=cmd_section_report)

    p_search = sub.add_parser("search", help="Full-text search in docs corpus")
    p_search.add_argument("--root", help="Explicit corpus root")
    p_search.add_argument("--query", required=True, help="Search query")
    p_search.add_argument("--limit-files", type=int, default=15)
    p_search.add_argument("--limit-snippets", type=int, default=3)
    p_search.add_argument(
        "--smart-case",
        action="store_true",
        help="Enable smart-case matching (default is case-insensitive)",
    )
    p_search.set_defaults(func=cmd_search)

    p_cov = sub.add_parser(
        "coverage",
        help="Compare documentation_links.txt URLs with parsed markdown files",
    )
    p_cov.add_argument("--root", help="Explicit corpus root")
    p_cov.add_argument("--links-file", help="Path to documentation_links.txt")
    p_cov.add_argument("--limit-missing", type=int, default=20)
    p_cov.set_defaults(func=cmd_coverage)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
