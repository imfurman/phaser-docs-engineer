# CanvasRenderer | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-canvas-canvasrenderer

Phaser API Documentation
Class
CanvasRenderer
Version: Phaser v3.90.0
On this page
CanvasRenderer
The Canvas Renderer is responsible for managing 2D canvas rendering contexts,
including the one used by the Games canvas. It tracks the internal state of a
given context and can renderer textured Game Objects to it, taking into
account alpha, blending, and scaling.
Constructor
new CanvasRenderer(game)
Parameters
name type optional description
game Phaser.Game No The Phaser Game instance that owns this renderer.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/renderer/canvas/CanvasRenderer.js#L20
Since: 3.0.0
Public Members ​
antialias ​
antialias: boolean ​
Description:
Should the Canvas use Image Smoothing or not when drawing Sprites?
Source: src/renderer/canvas/CanvasRenderer.js#L141
Since: 3.20.0
blendModes ​
blendModes: array ​
Description:
The blend modes supported by the Canvas Renderer.
This object maps the Phaser.BlendModes to canvas compositing operations.
Source: src/renderer/canvas/CanvasRenderer.js#L150
Since: 3.0.0
config ​
config: object ​
Description:
The local configuration settings of the CanvasRenderer.
Source: src/renderer/canvas/CanvasRenderer.js#L47
Since: 3.0.0
currentContext ​
currentContext: CanvasRenderingContext2D ​
Description:
The canvas context currently used by the CanvasRenderer for all rendering operations.
Source: src/renderer/canvas/CanvasRenderer.js#L132
Since: 3.0.0
drawCount ​
drawCount: number ​
Description:
The total number of Game Objects which were rendered in a frame.
Source: src/renderer/canvas/CanvasRenderer.js#L80
Since: 3.0.0
game ​
game: Phaser.Game ​
Description:
The Phaser Game instance that owns this renderer.
Source: src/renderer/canvas/CanvasRenderer.js#L62
Since: 3.0.0
gameCanvas ​
gameCanvas: HTMLCanvasElement ​
Description:
The canvas element which the Game uses.
Source: src/renderer/canvas/CanvasRenderer.js#L108
Since: 3.0.0
gameContext ​
gameContext: CanvasRenderingContext2D ​
Description:
The canvas context used to render all Cameras in all Scenes during the game loop.
Source: src/renderer/canvas/CanvasRenderer.js#L123
Since: 3.0.0
height ​
height: number ​
Description:
The height of the canvas being rendered to.
Source: src/renderer/canvas/CanvasRenderer.js#L99
Since: 3.0.0
isBooted ​
isBooted: boolean ​
Description:
Has this renderer fully booted yet?
Source: src/renderer/canvas/CanvasRenderer.js#L211
Since: 3.50.0
snapshotState ​
snapshotState: Phaser.Types.Renderer.Snapshot.SnapshotState ​
Description:
Details about the currently scheduled snapshot.
If a non-null callback is set in this object, a snapshot of the canvas will be taken after the current frame is fully rendered.
Source: src/renderer/canvas/CanvasRenderer.js#L161
Since: 3.16.0
type ​
type: number ​
Description:
A constant which allows the renderer to be easily identified as a Canvas Renderer.
Source: src/renderer/canvas/CanvasRenderer.js#L71
Since: 3.0.0
width ​
width: number ​
Description:
The width of the canvas being rendered to.
Source: src/renderer/canvas/CanvasRenderer.js#L90
Since: 3.0.0
Inherited Methods ​
From Phaser.Events.EventEmitter :
addListener
emit
eventNames
listenerCount
listeners
off
on
once
removeAllListeners
removeListener
shutdown
Public Methods ​
batchSprite ​
<instance> batchSprite(sprite, frame, camera, [parentTransformMatrix]) ​
Description:
Takes a Sprite Game Object, or any object that extends it, and draws it to the current context.
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No The texture based Game Object to draw.
frame Phaser.Textures.Frame No The frame to draw, doesn't have to be that owned by the Game Object.
camera Phaser.Cameras.Scene2D.Camera No The Camera to use for the rendering transform.
parentTransformMatrix Phaser.GameObjects.Components.TransformMatrix Yes The transform matrix of the parent container, if set.
Source: src/renderer/canvas/CanvasRenderer.js#L692
Since: 3.12.0
destroy ​
<instance> destroy() ​
Description:
Destroys all object references in the Canvas Renderer.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/renderer/canvas/CanvasRenderer.js#L883
Since: 3.0.0
init ​
<instance> init() ​
Description:
Prepares the game canvas for rendering.
Source: src/renderer/canvas/CanvasRenderer.js#L223
Since: 3.0.0
onResize ​
<instance> onResize(gameSize, baseSize) ​
Description:
The event handler that manages the resize event dispatched by the Scale Manager.
Parameters:
name type optional description
gameSize Phaser.Structs.Size No The default Game Size object. This is the un-modified game dimensions.
baseSize Phaser.Structs.Size No The base Size object. The game dimensions multiplied by the resolution. The canvas width / height values match this.
Source: src/renderer/canvas/CanvasRenderer.js#L274
Since: 3.16.0
postRender ​
<instance> postRender() ​
Description:
Restores the game context's global settings and takes a snapshot if one is scheduled.
The post-render step happens after all Cameras in all Scenes have been rendered.
Fires: Phaser.Renderer.Events#event:POST_RENDER
Source: src/renderer/canvas/CanvasRenderer.js#L530
Since: 3.0.0
preRender ​
<instance> preRender() ​
Description:
Called at the start of the render loop.
Fires: Phaser.Renderer.Events#event:PRE_RENDER_CLEAR , Phaser.Renderer.Events#event:PRE_RENDER
Source: src/renderer/canvas/CanvasRenderer.js#L372
Since: 3.0.0
render ​
<instance> render(scene, children, camera) ​
Description:
The core render step for a Scene Camera.
Iterates through the given array of Game Objects and renders them with the given Camera.
This is called by the CameraManager.render method. The Camera Manager instance belongs to a Scene, and is invoked
by the Scene Systems.render method.
This method is not called if Camera.visible is false , or Camera.alpha is zero.
Parameters:
name type optional description
scene Phaser.Scene No The Scene to render.
children Array.< Phaser.GameObjects.GameObject > No An array of filtered Game Objects that can be rendered by the given Camera.
camera Phaser.Cameras.Scene2D.Camera No The Scene Camera to render with.
Fires: Phaser.Renderer.Events#event:RENDER
Source: src/renderer/canvas/CanvasRenderer.js#L412
Since: 3.0.0
resetTransform ​
<instance> resetTransform() ​
Description:
Resets the transformation matrix of the current context to the identity matrix, thus resetting any transformation.
Source: src/renderer/canvas/CanvasRenderer.js#L310
Since: 3.0.0
resize ​
<instance> resize([width], [height]) ​
Description:
Resize the main game canvas.
Parameters:
name type optional description
width number Yes The new width of the renderer.
height number Yes The new height of the renderer.
Fires: Phaser.Renderer.Events#event:RESIZE
Source: src/renderer/canvas/CanvasRenderer.js#L292
Since: 3.0.0
setAlpha ​
<instance> setAlpha(alpha) ​
Description:
Sets the global alpha of the current context.
Parameters:
name type optional description
alpha number No The new alpha to use, where 0 is fully transparent and 1 is fully opaque.
Returns: Phaser.Renderer.Canvas.CanvasRenderer - This CanvasRenderer object.
Source: src/renderer/canvas/CanvasRenderer.js#L355
Since: 3.0.0
setBlendMode ​
<instance> setBlendMode(blendMode) ​
Description:
Sets the blend mode (compositing operation) of the current context.
Parameters:
name type optional description
blendMode string No The new blend mode which should be used.
Returns: Phaser.Renderer.Canvas.CanvasRenderer - This CanvasRenderer object.
Source: src/renderer/canvas/CanvasRenderer.js#L321
Since: 3.0.0
setContext ​
<instance> setContext([ctx]) ​
Description:
Changes the Canvas Rendering Context that all draw operations are performed against.
Parameters:
name type optional description
ctx CanvasRenderingContext2D Yes The new Canvas Rendering Context to draw everything to. Leave empty to reset to the Game Canvas.
Returns: Phaser.Renderer.Canvas.CanvasRenderer - The Canvas Renderer instance.
Source: src/renderer/canvas/CanvasRenderer.js#L338
Since: 3.12.0
snapshot ​
<instance> snapshot(callback, [type], [encoderOptions]) ​
Description:
Schedules a snapshot of the entire game viewport to be taken after the current frame is rendered.
To capture a specific area see the snapshotArea method. To capture a specific pixel, see snapshotPixel .
Only one snapshot can be active per frame . If you have already called snapshotPixel , for example, then
calling this method will override it.
Snapshots work by creating an Image object from the canvas data, this is a blocking process, which gets
more expensive the larger the canvas size gets, so please be careful how you employ this in your game.
Parameters:
name type optional default description
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot image is created.
type string Yes "'image/png'" The format of the image to create, usually image/png or image/jpeg .
encoderOptions number Yes 0.92 The image quality, between 0 and 1. Used for image formats with lossy compression, such as image/jpeg .
Returns: Phaser.Renderer.Canvas.CanvasRenderer - This WebGL Renderer.
Source: src/renderer/canvas/CanvasRenderer.js#L597
Since: 3.0.0
snapshotArea ​
<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions]) ​
Description:
Schedules a snapshot of the given area of the game viewport to be taken after the current frame is rendered.
To capture the whole game viewport see the snapshot method. To capture a specific pixel, see snapshotPixel .
Only one snapshot can be active per frame . If you have already called snapshotPixel , for example, then
calling this method will override it.
Snapshots work by creating an Image object from the canvas data, this is a blocking process, which gets
more expensive the larger the canvas size gets, so please be careful how you employ this in your game.
Parameters:
name type optional default description
x number No The x coordinate to grab from.
y number No The y coordinate to grab from.
width number No The width of the area to grab.
height number No The height of the area to grab.
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot image is created.
type string Yes "'image/png'" The format of the image to create, usually image/png or image/jpeg .
encoderOptions number Yes 0.92 The image quality, between 0 and 1. Used for image formats with lossy compression, such as image/jpeg .
Returns: Phaser.Renderer.Canvas.CanvasRenderer - This WebGL Renderer.
Source: src/renderer/canvas/CanvasRenderer.js#L622
Since: 3.16.0
snapshotCanvas ​
<instance> snapshotCanvas(canvas, callback, [getPixel], [x], [y], [width], [height], [type], [encoderOptions]) ​
Description:
Takes a snapshot of the given area of the given canvas.
Unlike the other snapshot methods, this one is processed immediately and doesn't wait for the next render.
Snapshots work by creating an Image object from the canvas data, this is a blocking process, which gets
more expensive the larger the canvas size gets, so please be careful how you employ this in your game.
Parameters:
name type optional default description
canvas HTMLCanvasElement No The canvas to grab from.
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot image is created.
getPixel boolean Yes false Grab a single pixel as a Color object, or an area as an Image object?
x number Yes 0 The x coordinate to grab from.
y number Yes 0 The y coordinate to grab from.
width number Yes "canvas.width" The width of the area to grab.
height number Yes "canvas.height" The height of the area to grab.
type string Yes "'image/png'" The format of the image to create, usually image/png or image/jpeg .
encoderOptions number Yes 0.92 The image quality, between 0 and 1. Used for image formats with lossy compression, such as image/jpeg .
Returns: Phaser.Renderer.Canvas.CanvasRenderer - This Canvas Renderer.
Source: src/renderer/canvas/CanvasRenderer.js#L557
Since: 3.19.0
snapshotPixel ​
<instance> snapshotPixel(x, y, callback) ​
Description:
Schedules a snapshot of the given pixel from the game viewport to be taken after the current frame is rendered.
To capture the whole game viewport see the snapshot method. To capture a specific area, see snapshotArea .
Only one snapshot can be active per frame . If you have already called snapshotArea , for example, then
calling this method will override it.
Unlike the other two snapshot methods, this one will return a Color object containing the color data for
the requested pixel. It doesn't need to create an internal Canvas or Image object, so is a lot faster to execute,
using less memory.
Parameters:
name type optional description
x number No The x coordinate of the pixel to get.
y number No The y coordinate of the pixel to get.
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot pixel data is extracted.
Returns: Phaser.Renderer.Canvas.CanvasRenderer - This WebGL Renderer.
Source: src/renderer/canvas/CanvasRenderer.js#L662
Since: 3.16.0
Previous
ScenePlugin
Next
PipelineManager
Public Members
antialias
blendModes
config
currentContext
drawCount
game
gameCanvas
gameContext
height
isBooted
snapshotState
type
width
Inherited Methods
Public Methods
batchSprite
destroy
init
onResize
postRender
preRender
render
resetTransform
resize
setAlpha
setBlendMode
setContext
snapshot
snapshotArea
snapshotCanvas
snapshotPixel
