# Phaser.Renderer.Canvas | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/renderer-canvas

Phaser API Documentation
Namespaces
Phaser.Renderer.Canvas
Version: Phaser v3.90.0
On this page
Phaser.Renderer.Canvas
Scope: static
Source: src/renderer/canvas/index.js#L7
Static functions ​
CanvasRenderer
Static functions ​
GetBlendModes ​
<static> GetBlendModes() ​
Description:
Returns an array which maps the default blend modes to supported Canvas blend modes.
If the browser doesn't support a blend mode, it will default to the normal source-over blend mode.
Returns: array - Which Canvas blend mode corresponds to which default Phaser blend mode.
Source: src/renderer/canvas/utils/GetBlendModes.js#L10
Since: 3.0.0
SetTransform ​
<static> SetTransform(renderer, ctx, src, camera, [parentMatrix]) ​
Description:
Takes a reference to the Canvas Renderer, a Canvas Rendering Context, a Game Object, a Camera and a parent matrix
and then performs the following steps:
Checks the alpha of the source combined with the Camera alpha. If 0 or less it aborts.
Takes the Camera and Game Object matrix and multiplies them, combined with the parent matrix if given.
Sets the blend mode of the context to be that used by the Game Object.
Sets the alpha value of the context to be that used by the Game Object combined with the Camera.
Saves the context state.
Sets the final matrix values into the context via setTransform.
If the Game Object has a texture frame, imageSmoothingEnabled is set based on frame.source.scaleMode.
If the Game Object does not have a texture frame, imageSmoothingEnabled is set based on Renderer.antialias.
This function is only meant to be used internally. Most of the Canvas Renderer classes use it.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer No A reference to the current active Canvas renderer.
ctx CanvasRenderingContext2D No The canvas context to set the transform on.
src Phaser.GameObjects.GameObject No The Game Object being rendered. Can be any type that extends the base class.
camera Phaser.Cameras.Scene2D.Camera No The Camera that is rendering the Game Object.
parentMatrix Phaser.GameObjects.Components.TransformMatrix Yes A parent transform matrix to apply to the Game Object before rendering.
Returns: boolean - true if the Game Object context was set, otherwise false .
Source: src/renderer/canvas/utils/SetTransform.js#L9
Since: 3.12.0
Previous
Phaser.Plugins
Next
Phaser.Renderer.Events
Static functions
Static functions
GetBlendModes
SetTransform
