# BitmapMask | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/display-masks-bitmapmask

Phaser API Documentation
Class
BitmapMask
Version: Phaser v3.90.0
On this page
BitmapMask
A Bitmap Mask combines the alpha (opacity) of a masked pixel with the alpha of another pixel.
Unlike the Geometry Mask, which is a clipping path, a Bitmap Mask behaves like an alpha mask,
not a clipping path. It is only available when using the WebGL Renderer.
A Bitmap Mask can use any Game Object or Dynamic Texture to determine the alpha of each pixel of the masked Game Object(s).
For any given point of a masked Game Object's texture, the pixel's alpha will be multiplied by the alpha
of the pixel at the same position in the Bitmap Mask's Game Object. The color of the pixel from the
Bitmap Mask doesn't matter.
For example, if a pure blue pixel with an alpha of 0.95 is masked with a pure red pixel with an
alpha of 0.5, the resulting pixel will be pure blue with an alpha of 0.475. Naturally, this means
that a pixel in the mask with an alpha of 0 will hide the corresponding pixel in all masked Game Objects.
A pixel with an alpha of 1 in the masked Game Object will receive the same alpha as the
corresponding pixel in the mask.
Note: You cannot combine Bitmap Masks and Blend Modes on the same Game Object. You can, however,
combine Geometry Masks and Blend Modes together.
The Bitmap Mask's location matches the location of its Game Object, not the location of the
masked objects. Moving or transforming the underlying Game Object will change the mask
(and affect the visibility of any masked objects), whereas moving or transforming a masked object
will not affect the mask.
The Bitmap Mask will not render its Game Object by itself. If the Game Object is not in a
Scene's display list, it will only be used for the mask and its full texture will not be directly
visible. Adding the underlying Game Object to a Scene will not cause any problems - it will
render as a normal Game Object and will also serve as a mask.
Constructor
new BitmapMask(scene, [maskObject], [x], [y], [texture], [frame])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this mask is being added.
maskObject Phaser.GameObjects.GameObject | Phaser.Textures.DynamicTexture Yes The Game Object or Dynamic Texture that will be used as the mask. If null it will generate an Image Game Object using the rest of the arguments.
x number Yes If creating a Game Object, the horizontal position in the world.
y number Yes If creating a Game Object, the vertical position in the world.
texture string | Phaser.Textures.Texture Yes If creating a Game Object, the key, or instance of the Texture it will use to render with, as stored in the Texture Manager.
frame string | number Phaser.Textures.Frame Yes
Scope : static
Source: src/display/mask/BitmapMask.js#L10
Since: 3.0.0
Public Members ​
bitmapMask ​
bitmapMask: Phaser.GameObjects.GameObject , Phaser.Textures.DynamicTexture ​
Description:
The Game Object that is used as the mask. Must use a texture, such as a Sprite.
Source: src/display/mask/BitmapMask.js#L63
Since: 3.0.0
invertAlpha ​
invertAlpha: boolean ​
Description:
Whether to invert the masks alpha.
If true , the alpha of the masking pixel will be inverted before it's multiplied with the masked pixel.
Essentially, this means that a masked area will be visible only if the corresponding area in the mask is invisible.
Source: src/display/mask/BitmapMask.js#L72
Since: 3.1.2
isStencil ​
isStencil: boolean ​
Description:
Is this mask a stencil mask? This is false by default and should not be changed.
Source: src/display/mask/BitmapMask.js#L85
Since: 3.17.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this BitmapMask and nulls any references it holds.
Note that if a Game Object is currently using this mask it will not automatically detect you have destroyed it,
so be sure to call clearMask on any Game Object using it, before destroying it.
Source: src/display/mask/BitmapMask.js#L175
Since: 3.7.0
postRenderCanvas ​
<instance> postRenderCanvas(renderer) ​
Description:
This is a NOOP method. Bitmap Masks are not supported by the Canvas Renderer.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer | Phaser.Renderer.WebGL.WebGLRenderer No The Canvas Renderer which would be rendered to.
Source: src/display/mask/BitmapMask.js#L162
Since: 3.0.0
postRenderWebGL ​
<instance> postRenderWebGL(renderer, camera, [renderTarget]) ​
Description:
Finalizes rendering of a masked Game Object.
This resets the previously bound framebuffer and switches the WebGL Renderer to the Bitmap Mask Pipeline, which uses a special fragment shader to apply the masking effect.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer | Phaser.Renderer.WebGL.WebGLRenderer No The WebGL Renderer to clean up.
camera Phaser.Cameras.Scene2D.Camera No The Camera to render to.
renderTarget Phaser.Renderer.WebGL.RenderTarget Yes Optional WebGL RenderTarget.
Source: src/display/mask/BitmapMask.js#L130
Since: 3.0.0
preRenderCanvas ​
<instance> preRenderCanvas(renderer, mask, camera) ​
Description:
This is a NOOP method. Bitmap Masks are not supported by the Canvas Renderer.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer | Phaser.Renderer.WebGL.WebGLRenderer No The Canvas Renderer which would be rendered to.
mask Phaser.GameObjects.GameObject No The masked Game Object which would be rendered.
camera Phaser.Cameras.Scene2D.Camera No The Camera to render to.
Source: src/display/mask/BitmapMask.js#L147
Since: 3.0.0
preRenderWebGL ​
<instance> preRenderWebGL(renderer, maskedObject, camera) ​
Description:
Prepares the WebGL Renderer to render a Game Object with this mask applied.
This renders the masking Game Object to the mask framebuffer and switches to the main framebuffer so that the masked Game Object will be rendered to it instead of being rendered directly to the frame.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer | Phaser.Renderer.WebGL.WebGLRenderer No The WebGL Renderer to prepare.
maskedObject Phaser.GameObjects.GameObject No The masked Game Object which will be drawn.
camera Phaser.Cameras.Scene2D.Camera No The Camera to render to.
Source: src/display/mask/BitmapMask.js#L113
Since: 3.0.0
setBitmap ​
<instance> setBitmap(maskObject) ​
Description:
Sets a new Game Object or Dynamic Texture for this Bitmap Mask to use.
If a Game Object it must have a texture, such as a Sprite.
You can update the source of the mask as often as you like.
Parameters:
name type optional description
maskObject Phaser.GameObjects.GameObject | Phaser.Textures.DynamicTexture No The Game Object or Dynamic Texture that will be used as the mask. If a Game Object, it must have a texture, such as a Sprite.
Source: src/display/mask/BitmapMask.js#L96
Since: 3.0.0
Previous
ColorMatrix
Next
GeometryMask
Public Members
bitmapMask
invertAlpha
isStencil
Public Methods
destroy
postRenderCanvas
postRenderWebGL
preRenderCanvas
preRenderWebGL
setBitmap
