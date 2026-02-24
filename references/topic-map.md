# Phaser Docs Topic Map

## Corpus Scope
- Root: `references/corpus/docs.phaser.io`
- Total markdown files: `693`
- Top-level sections:
  - `api-documentation`: `636`
  - `phaser`: `57`

## API Documentation Coverage
- `api-documentation/class` (`281`): classes, managers, plugins, core runtime entities.
- `api-documentation/namespace` (`242`): static modules, utils, sub-systems, type namespaces.
- `api-documentation/typedef` (`51`): structured config and type contracts.
- `api-documentation/event` (`23`): event emitters and payload/event channels.
- `api-documentation/function` (`21`): helper and utility functions.
- `api-documentation/constant` (`15`): constants/enums-like values.
- `api-documentation/api-documentation.md`, `gameobjects/index.md`, `physics/index.md`: section roots.

## Phaser Runtime Guides (`phaser/*`)
- `phaser/getting-started/*` (`5`): installation, first game, templates, setup.
- `phaser/concepts/*` (`52`): conceptual guides and subsystem overviews.
- Key concept subareas:
  - `concepts/scenes*`
  - `concepts/gameobjects/*`
  - `concepts/physics/*`
  - `concepts/loader*`
  - `concepts/input*`
  - `concepts/cameras*`
  - `concepts/tweens*`
  - `concepts/textures*`
  - `concepts/audio*`
  - `concepts/scale-manager*`

## Development Aspect Routing

Use this mapping to avoid missing relevant docs.

- Project bootstrap/setup
  - `phaser/getting-started/*`
  - `phaser/concepts/game.md`
- Scene lifecycle and architecture
  - `phaser/concepts/scenes*`
  - `api-documentation/class/scene*`
  - `api-documentation/class/scenes-*`
  - `api-documentation/event/scenes-events.md`
- Game objects/UI/renderables
  - `phaser/concepts/gameobjects/*`
  - `api-documentation/class/gameobjects-*`
  - `api-documentation/namespace/gameobjects*`
- Rendering/WebGL/FX
  - `phaser/concepts/display*`
  - `phaser/concepts/fx.md`
  - `api-documentation/class/renderer-*`
  - `api-documentation/class/fx-*`
- Input/controls
  - `phaser/concepts/input.md`
  - `api-documentation/class/input-*`
  - `api-documentation/event/input-*`
- Physics (Arcade/Matter)
  - `phaser/concepts/physics/*`
  - `api-documentation/class/physics-arcade-*`
  - `api-documentation/class/physics-matter-*`
  - `api-documentation/event/physics-*`
- Loading/assets/textures
  - `phaser/concepts/loader*`
  - `phaser/concepts/textures.md`
  - `api-documentation/class/loader-*`
  - `api-documentation/class/textures-*`
- Audio
  - `phaser/concepts/audio.md`
  - `api-documentation/class/sound-*`
  - `api-documentation/event/sound-events.md`
- Timing/animation/tweens
  - `phaser/concepts/animations.md`
  - `phaser/concepts/tweens.md`
  - `phaser/concepts/time.md`
  - `api-documentation/class/time-*`
  - `api-documentation/class/tweens-*`
- Events/data/state
  - `phaser/concepts/events.md`
  - `phaser/concepts/data-manager.md`
  - `api-documentation/class/events-eventemitter.md`
  - `api-documentation/class/data-*`
- Scale/responsive/device
  - `phaser/concepts/scale-manager.md`
  - `phaser/concepts/device.md`
  - `api-documentation/class/scale-scalemanager.md`

## Minimum Evidence Policy

For non-trivial coding tasks, read and cite:
- At least one `phaser/concepts/*` guide page.
- At least one `api-documentation/*` page relevant to used classes/functions/events.
