# Phaser.Renderer.Snapshot | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/renderer-snapshot

Phaser API Documentation
Namespaces
Phaser.Renderer.Snapshot
Version: Phaser v3.90.0
On this page
Phaser.Renderer.Snapshot
Scope: static
Source: src/renderer/snapshot/index.js#L7
Static functions ​
Canvas ​
<static> Canvas(sourceCanvas, config) ​
Description:
Takes a snapshot of an area from the current frame displayed by a canvas.
This is then copied to an Image object. When this loads, the results are sent
to the callback provided in the Snapshot Configuration object.
Parameters:
name type optional description
sourceCanvas HTMLCanvasElement No The canvas to take a snapshot of.
config Phaser.Types.Renderer.Snapshot.SnapshotState No The snapshot configuration object.
Source: src/renderer/snapshot/CanvasSnapshot.js#L11
Since: 3.0.0
WebGL ​
<static> WebGL(sourceContext, config) ​
Description:
Takes a snapshot of an area from the current frame displayed by a WebGL canvas.
This is then copied to an Image object. When this loads, the results are sent
to the callback provided in the Snapshot Configuration object.
Parameters:
name type optional description
sourceContext WebGLRenderingContext No The WebGL context to take a snapshot of.
config Phaser.Types.Renderer.Snapshot.SnapshotState No The snapshot configuration object.
Source: src/renderer/snapshot/WebGLSnapshot.js#L11
Since: 3.0.0
Previous
Phaser.Renderer.Events
Next
Phaser.Renderer.WebGL.Pipelines.Events
Static functions
Canvas
WebGL
