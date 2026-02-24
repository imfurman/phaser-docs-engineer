# Query Patterns

Use `scripts/phaser_docs_tool.py search` first, then open matching files.

## Global
```bash
python3 scripts/phaser_docs_tool.py section-report
python3 scripts/phaser_docs_tool.py search --query "ScenePlugin"
python3 scripts/phaser_docs_tool.py search --query "Arcade Physics collider"
```

## Gameplay / Scene Architecture
```bash
python3 scripts/phaser_docs_tool.py search --query "scene lifecycle"
python3 scripts/phaser_docs_tool.py search --query "cross scene communication"
python3 scripts/phaser_docs_tool.py search --query "Scenes.Events"
```

## Rendering / Game Objects / FX
```bash
python3 scripts/phaser_docs_tool.py search --query "GameObjects.Image"
python3 scripts/phaser_docs_tool.py search --query "render texture"
python3 scripts/phaser_docs_tool.py search --query "postfx pipeline"
```

## Input
```bash
python3 scripts/phaser_docs_tool.py search --query "InputPlugin pointerdown"
python3 scripts/phaser_docs_tool.py search --query "keyboard key combo"
python3 scripts/phaser_docs_tool.py search --query "gamepad plugin"
```

## Physics
```bash
python3 scripts/phaser_docs_tool.py search --query "ArcadePhysics body velocity"
python3 scripts/phaser_docs_tool.py search --query "Matter Physics collision"
python3 scripts/phaser_docs_tool.py search --query "StaticGroup"
```

## Assets / Loader / Textures
```bash
python3 scripts/phaser_docs_tool.py search --query "LoaderPlugin atlas"
python3 scripts/phaser_docs_tool.py search --query "cache manager"
python3 scripts/phaser_docs_tool.py search --query "TextureManager"
```

## Audio / Time / Tweens
```bash
python3 scripts/phaser_docs_tool.py search --query "WebAudioSoundManager"
python3 scripts/phaser_docs_tool.py search --query "TimeEvent"
python3 scripts/phaser_docs_tool.py search --query "TweenChain"
```

## Coverage Audit
```bash
python3 scripts/phaser_docs_tool.py coverage
python3 scripts/phaser_docs_tool.py coverage --links-file documentation_links.txt --limit-missing 50
```
