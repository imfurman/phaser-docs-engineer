#!/usr/bin/env python3
"""Rebuild references/corpus-index.tsv from the parsed docs corpus."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="",
        help="Path to parsed docs root (default: bundled references/corpus/docs.phaser.io)",
    )
    parser.add_argument(
        "--out",
        default="",
        help="Output TSV path (defaults to references/corpus-index.tsv in this skill)",
    )
    return parser.parse_args()


def resolve_root(explicit: str) -> Path:
    if explicit:
        p = Path(explicit)
        if p.exists():
            return p.resolve()
        raise FileNotFoundError(f"Root does not exist: {p}")

    bundled = Path(__file__).resolve().parents[1] / "references/corpus/docs.phaser.io"
    if bundled.exists():
        return bundled.resolve()

    cwd = Path.cwd()
    for base in [cwd, *cwd.parents]:
        candidate = base / "docs/pages/parsed/docs.phaser.io"
        if candidate.exists():
            return candidate.resolve()

    raise FileNotFoundError("Cannot find docs/pages/parsed/docs.phaser.io")


def main() -> int:
    args = parse_args()
    root = resolve_root(args.root)

    if args.out:
        out = Path(args.out)
    else:
        out = Path(__file__).resolve().parents[1] / "references/corpus-index.tsv"

    rows = sorted(root.rglob("*.md"))
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8") as fp:
        fp.write("section\tsubsection\tpath\n")
        for path in rows:
            rel = path.relative_to(root)
            parts = rel.parts
            section = parts[0] if len(parts) > 0 else ""
            subsection = parts[1] if len(parts) > 1 else ""
            fp.write(f"{section}\t{subsection}\t{rel.as_posix()}\n")

    print(f"Root: {root}")
    print(f"Rows: {len(rows)}")
    print(f"Out:  {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
