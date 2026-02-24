# GeometryMask | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/display-masks-geometrymask

Phaser API Documentation
Class
GeometryMask
Version: Phaser v3.90.0
On this page
GeometryMask
A Geometry Mask can be applied to a Game Object to hide any pixels of it which don't intersect
a visible pixel from the geometry mask. The mask is essentially a clipping path which can only
make a masked pixel fully visible or fully invisible without changing its alpha (opacity).
A Geometry Mask uses a Graphics Game Object to determine which pixels of the masked Game Object(s)
should be clipped. For any given point of a masked Game Object's texture, the pixel will only be displayed
if the Graphics Game Object of the Geometry Mask has a visible pixel at the same position. The color and
alpha of the pixel from the Geometry Mask do not matter.
The Geometry Mask's location matches the location of its Graphics object, not the location of the masked objects.
Moving or transforming the underlying Graphics object will change the mask (and affect the visibility
of any masked objects), whereas moving or transforming a masked object will not affect the mask.
You can think of the Geometry Mask (or rather, of its Graphics object) as an invisible curtain placed
in front of all masked objects which has its own visual properties and, naturally, respects the camera's
visual properties, but isn't affected by and doesn't follow the masked objects by itself.
Constructor
new GeometryMask(scene, graphicsGeometry)
Parameters
name type optional description
scene Phaser.Scene No This parameter is not used.
graphicsGeometry Phaser.GameObjects.Graphics No The Graphics Game Object to use for the Geometry Mask. Doesn't have to be in the Display List.
Scope : static
Source: src/display/mask/GeometryMask.js#L9
Since: 3.0.0
Public Members ​
geometryMask ​
geometryMask: Phaser.GameObjects.Graphics ​
Description:
The Graphics object which describes the Geometry Mask.
Source: src/display/mask/GeometryMask.js#L41
Since: 3.0.0
invertAlpha ​
invertAlpha: boolean ​
Description:
Similar to the BitmapMasks invertAlpha setting this to true will then hide all pixels
drawn to the Geometry Mask.
This is a WebGL only feature.
Source: src/display/mask/GeometryMask.js#L50
Since: 3.16.0
isStencil ​
isStencil: boolean ​
Description:
Is this mask a stencil mask?
Source: src/display/mask/GeometryMask.js#L62
Since: 3.17.0
level ​
level: boolean ​
Description:
The current stencil level. This can change dynamically at runtime
and is set in the applyStencil method.
Source: src/display/mask/GeometryMask.js#L72
Since: 3.17.0
Public Methods ​
applyStencil ​
<instance> applyStencil(renderer, camera, inc) ​
Description:
Applies the current stencil mask to the renderer.
Parameters:
name type optional description
renderer Phaser.Renderer.WebGL.WebGLRenderer No The WebGL Renderer instance to draw to.
camera Phaser.Cameras.Scene2D.Camera No The camera the Game Object is being rendered through.
inc boolean No Is this an INCR stencil or a DECR stencil?
Source: src/display/mask/GeometryMask.js#L160
Since: 3.17.0
destroy ​
<instance> destroy() ​
Description:
Destroys this GeometryMask and nulls any references it holds.
Note that if a Game Object is currently using this mask it will not automatically detect you have destroyed it,
so be sure to call clearMask on any Game Object using it, before destroying it.
Source: src/display/mask/GeometryMask.js#L293
Since: 3.7.0
postRenderCanvas ​
<instance> postRenderCanvas(renderer) ​
Description:
Restore the canvas context's previous clipping path, thus turning off the mask for it.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer No The Canvas Renderer instance being restored.
Source: src/display/mask/GeometryMask.js#L280
Since: 3.0.0
postRenderWebGL ​
<instance> postRenderWebGL(renderer) ​
Description:
Flushes all rendered pixels and disables the stencil test of a WebGL context, thus disabling the mask for it.
Parameters:
name type optional description
renderer Phaser.Renderer.WebGL.WebGLRenderer No The WebGL Renderer instance to draw flush.
Source: src/display/mask/GeometryMask.js#L213
Since: 3.0.0
preRenderCanvas ​
<instance> preRenderCanvas(renderer, mask, camera) ​
Description:
Sets the clipping path of a 2D canvas context to the Geometry Mask's underlying Graphics object.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer No The Canvas Renderer instance to set the clipping path on.
mask Phaser.GameObjects.GameObject No The Game Object being rendered.
camera Phaser.Cameras.Scene2D.Camera No The camera the Game Object is being rendered through.
Source: src/display/mask/GeometryMask.js#L259
Since: 3.0.0
preRenderWebGL ​
<instance> preRenderWebGL(renderer, child, camera) ​
Description:
Renders the Geometry Mask's underlying Graphics object to the OpenGL stencil buffer and enables the stencil test, which clips rendered pixels according to the mask.
Parameters:
name type optional description
renderer Phaser.Renderer.WebGL.WebGLRenderer No The WebGL Renderer instance to draw to.
child Phaser.GameObjects.GameObject No The Game Object being rendered.
camera Phaser.Cameras.Scene2D.Camera No The camera the Game Object is being rendered through.
Source: src/display/mask/GeometryMask.js#L123
Since: 3.0.0
setInvertAlpha ​
<instance> setInvertAlpha([value]) ​
Description:
Sets the invertAlpha property of this Geometry Mask.
Inverting the alpha essentially flips the way the mask works.
This is a WebGL only feature.
Parameters:
name type optional default description
value boolean Yes true Invert the alpha of this mask?
Returns: Phaser.Display.Masks.GeometryMask - This Geometry Mask
Source: src/display/mask/GeometryMask.js#L100
Since: 3.17.0
setShape ​
<instance> setShape(graphicsGeometry) ​
Description:
Sets a new Graphics object for the Geometry Mask.
Parameters:
name type optional description
graphicsGeometry Phaser.GameObjects.Graphics No The Graphics object which will be used for the Geometry Mask.
Returns: Phaser.Display.Masks.GeometryMask - This Geometry Mask
Source: src/display/mask/GeometryMask.js#L83
Since: 3.0.0
Previous
BitmapMask
Next
RGB
Public Members
geometryMask
invertAlpha
isStencil
level
Public Methods
applyStencil
destroy
postRenderCanvas
postRenderWebGL
preRenderCanvas
preRenderWebGL
setInvertAlpha
setShape
