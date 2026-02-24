---
name: phaser-docs-engineer
description: Comprehensive Phaser implementation skill grounded in a local parsed documentation corpus. Use when building, debugging, refactoring, optimizing, testing, or explaining Phaser code across scenes, game objects, rendering, input, physics, loader, audio, tweens, time, scale, events, and types. Use whenever the agent must base decisions on documentation evidence and cite exact local doc file paths.
---

# Phaser Docs Engineer

Use documentation evidence first and memory second.

## Runbook

1. Resolve the corpus root with `scripts/phaser_docs_tool.py find-root`.
2. Verify corpus coverage with `scripts/phaser_docs_tool.py section-report`.
3. If needed, compare links vs parsed files with `scripts/phaser_docs_tool.py coverage`.
4. Search relevant docs with `scripts/phaser_docs_tool.py search --query "..."`.
5. Read the most relevant files before writing code.
6. Implement and test changes.
7. Cite local documentation paths in the response.

## Required Guardrails

- Ground every non-trivial Phaser decision in local docs.
- Prefer at least one conceptual doc and one API doc for runtime behavior changes.
- If coverage check reports missing docs, state this explicitly and request corpus refresh before high-confidence claims.
- Never invent APIs, events, or config fields.

## Coverage Discipline

Use [topic-map.md](references/topic-map.md) to ensure relevant areas are checked.
Use [coverage-checklist.md](references/coverage-checklist.md) before finalizing large features.
Use [query-patterns.md](references/query-patterns.md) for fast targeted retrieval.
Use [corpus-index.tsv](references/corpus-index.tsv) for exhaustive path discovery.

## Resources

- `scripts/phaser_docs_tool.py`: root detection, search, section report, links-vs-files coverage audit.
- `scripts/rebuild_corpus_index.py`: regenerate full file index after corpus refresh.
- `references/corpus/docs.phaser.io`: bundled автономный корпус Phaser docs (`.md`).
- `references/documentation_links.txt`: bundled URL list for coverage checks.
- `references/topic-map.md`: full domain map and where each topic lives.
- `references/coverage-checklist.md`: completeness checklist for implementation/debug/perf tasks.
- `references/query-patterns.md`: proven search queries and retrieval patterns.
- `references/corpus-index.tsv`: full parsed-file index (generated from corpus paths).
