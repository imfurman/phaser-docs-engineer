# 🎮 phaser-docs-engineer

> An AI agent skill that grounds every Phaser.js decision in locally parsed documentation — no hallucinated APIs, no guesswork.

---

## What This Is

**phaser-docs-engineer** is a skill (instruction set + tooling + documentation corpus) for AI coding agents. Built primarily for **OpenAI Codex**, but compatible with any agent that supports skill/instruction files — including Claude Projects, Cursor, and similar tools.

The skill turns an AI agent into a reliable Phaser.js implementation engineer by requiring it to search and cite a **local corpus of parsed Phaser documentation** before writing or modifying any non-trivial code.

### Why it exists

LLMs frequently invent Phaser APIs, config fields, and event names that don't exist — especially for less common subsystems like `Scale`, `Loader`, or `Time`. This skill enforces a docs-first workflow to eliminate that problem.

---

## Compatibility

| Agent | Status |
|---|---|
| OpenAI Codex | ✅ Primary target |
| Claude (Projects / claude.ai) | ✅ Compatible |
| Cursor (Rules) | ✅ Compatible |
| Other agents with instruction files | ⚠️ Should work, untested |

The skill's runbook uses standard CLI calls and file reads — nothing agent-specific.

---

## Features

- 📚 **Documentation-grounded** — every non-trivial decision cites a local doc file path
- 🔍 **Searchable corpus** — fast targeted retrieval via `phaser_docs_tool.py`
- 🗺️ **Full domain coverage** — scenes, game objects, physics, input, audio, tweens, loader, scale, events, types, and more
- ✅ **Coverage discipline** — checklists and topic maps prevent blind spots
- 🚫 **No invented APIs** — guardrails explicitly forbid hallucinated methods, events, or config fields

---

## Repository Structure

```
.
├── SKILL.md                        # Skill definition (loaded by the agent)
├── scripts/
│   ├── phaser_docs_tool.py         # Main CLI: search, find-root, section-report, coverage
│   └── rebuild_corpus_index.py     # Regenerate corpus-index.tsv after corpus refresh
└── references/
    ├── corpus/
    │   └── docs.phaser.io/         # Parsed Phaser docs corpus (.md files)
    ├── documentation_links.txt     # Full URL list for coverage audits
    ├── topic-map.md                # Domain map — where each topic lives in corpus
    ├── coverage-checklist.md       # Completeness checklist for large features
    ├── query-patterns.md           # Proven search queries and retrieval patterns
    └── corpus-index.tsv            # Full file index (auto-generated)
```

---

## How It Works

When an agent uses this skill, it follows a strict runbook before writing any code:

1. **Resolve corpus root** — `scripts/phaser_docs_tool.py find-root`
2. **Verify coverage** — `scripts/phaser_docs_tool.py section-report`
3. **Audit if needed** — `scripts/phaser_docs_tool.py coverage`
4. **Search relevant docs** — `scripts/phaser_docs_tool.py search --query "..."`
5. **Read before writing** — opens the most relevant `.md` files
6. **Implement changes** — writes code grounded in documentation
7. **Cite sources** — includes local doc paths in the response

---

## Setup

### OpenAI Codex

1. Clone this repo into your project or as a standalone skill repo
2. Point Codex to `SKILL.md` as the skill instruction file
3. Ensure `references/corpus/` is accessible at runtime

### Claude Projects

1. Upload `SKILL.md` to your Claude Project's instructions
2. Make `references/` available in the project file context

### Cursor

Add the contents of `SKILL.md` to your `.cursor/rules` file or project rules.

---

## CLI Tool

```bash
# Find the corpus root
python scripts/phaser_docs_tool.py find-root

# Check which Phaser sections are covered
python scripts/phaser_docs_tool.py section-report

# Search the corpus
python scripts/phaser_docs_tool.py search --query "arcade physics body velocity"

# Audit parsed files vs documentation links
python scripts/phaser_docs_tool.py coverage

# Rebuild the corpus index after a refresh
python scripts/rebuild_corpus_index.py
```

---

## Covered Phaser Domains

| Domain | Examples |
|---|---|
| Scenes | lifecycle, SceneManager, transitions |
| Game Objects | Sprites, Groups, Containers, Text |
| Physics | Arcade, Matter.js bodies, colliders |
| Input | Keyboard, Pointer, GamePad, events |
| Rendering | Camera, pipeline, layers, blend modes |
| Loader | file types, load events, pack files |
| Audio | WebAudioSound, markers, spatial |
| Tweens | TweenManager, timeline, callbacks |
| Time | TimerEvent, Clock, delayedCall |
| Scale | ScaleManager, resize, orientation |
| Events | EventEmitter, listener patterns |
| Types | TypeScript-compatible config shapes |

---

## Guardrails

The skill enforces the following hard rules:

- **Ground every non-trivial decision** in at least one local doc file
- **Prefer two sources** for runtime behavior changes: one conceptual, one API reference
- **Never invent** APIs, events, or config fields
- **Explicitly flag** any missing documentation before making high-confidence claims
- **Request corpus refresh** when coverage checks reveal gaps

---

## Refreshing the Corpus

If the Phaser docs are updated or you want to expand coverage:

1. Re-parse the docs into `references/corpus/docs.phaser.io/` as `.md` files
2. Run `python scripts/rebuild_corpus_index.py` to regenerate `corpus-index.tsv`
3. Update `references/documentation_links.txt` with any new URLs
4. Run `python scripts/phaser_docs_tool.py coverage` to audit completeness

---

## Requirements

- Python 3.8+
- An AI coding agent with skill/instruction file support (Codex, Claude, Cursor, etc.)

---

## License

MIT — see [LICENSE](LICENSE)

---

## Contributing

PRs welcome for:
- Expanding corpus coverage (more Phaser subsystems)
- Improving `query-patterns.md` with battle-tested search queries
- Adding entries to `topic-map.md` for undocumented areas
- Better `coverage-checklist.md` items for common feature patterns
- Testing and reporting compatibility with other agents