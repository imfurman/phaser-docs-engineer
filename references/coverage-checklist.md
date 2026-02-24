# Coverage Checklist

Use this checklist before finalizing any substantial Phaser task.

## 1) Scope Fit
- Confirm the target runtime subsystem and expected behavior.
- Confirm task type: new feature, bug fix, refactor, optimization, architecture, or migration.

## 2) Documentation Retrieval
- Resolve corpus root with `scripts/phaser_docs_tool.py find-root`.
- Run targeted search with `scripts/phaser_docs_tool.py search --query "..."`.
- Read at least one conceptual guide and one API reference page.

## 3) Runtime Correctness
- Validate lifecycle hooks (`preload/create/update`, scene events, plugin lifecycle).
- Validate object ownership and cleanup (destroy, shutdown, event listener removal).
- Validate configuration contracts (constructor args, config objects, typedefs).

## 4) Systems Review (mark relevant)
- Scenes/state orchestration.
- Game objects/render pipeline.
- Input mapping and pointer/keyboard/gamepad handling.
- Physics setup and collision semantics.
- Loader/cache/asset keys.
- Animation/tween/time usage.
- Audio playback and manager behavior.
- Scale/camera/responsiveness.
- Event flow and data/state propagation.

## 5) Quality Gates
- Add/adjust tests when feasible.
- Run available lint/type/test commands.
- Re-check docs if behavior diverges from expected API contracts.

## 6) Response Quality
- Cite local doc file paths used for key decisions.
- Call out assumptions explicitly.
- State any corpus gaps or ambiguities.
