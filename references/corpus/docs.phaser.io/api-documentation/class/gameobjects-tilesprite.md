# TileSprite | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-tilesprite

Phaser API Documentation
Class
TileSprite
Version: Phaser v3.90.0
On this page
TileSprite
A TileSprite is a Sprite that has a repeating texture.
The texture can be scrolled and scaled independently of the TileSprite itself. Textures will automatically wrap and
are designed so that you can create game backdrops using seamless textures as a source.
You shouldn't ever create a TileSprite any larger than your actual canvas size. If you want to create a large repeating background
that scrolls across the whole map of your game, then you create a TileSprite that fits the canvas size and then use the tilePosition
property to scroll the texture as the player moves. If you create a TileSprite that is thousands of pixels in size then it will
consume huge amounts of memory and cause performance issues. Remember: use tilePosition to scroll your texture and tileScale to
adjust the scale of the texture - don't resize the sprite itself or make it larger than it needs.
An important note about Tile Sprites and NPOT textures: Internally, TileSprite textures use GL_REPEAT to provide
seamless repeating of the textures. This, combined with the way in which the textures are handled in WebGL, means
they need to be POT (power-of-two) sizes in order to wrap. If you provide a NPOT (non power-of-two) texture to a
TileSprite it will generate a POT sized canvas and draw your texture to it, scaled up to the POT size. It's then
scaled back down again during rendering to the original dimensions. While this works, in that it allows you to use
any size texture for a Tile Sprite, it does mean that NPOT textures are going to appear anti-aliased when rendered,
due to the interpolation that took place when it was resized into a POT texture. This is especially visible in
pixel art graphics. If you notice it and it becomes an issue, the only way to avoid it is to ensure that you
provide POT textures for Tile Sprites.
Constructor
new TileSprite(scene, x, y, width, height, textureKey, [frameKey])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
width number No The width of the Game Object. If zero it will use the size of the texture frame.
height number No The height of the Game Object. If zero it will use the size of the texture frame.
textureKey string No The key of the Texture this Game Object will use to render with, as stored in the Texture Manager. Cannot be a DynamicTexture.
frameKey string | number Yes An optional frame from the Texture this Game Object is rendering with.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Alpha
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.ComputedSize
Phaser.GameObjects.Components.Crop
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Flip
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Tint
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/tilesprite/TileSprite.js#L20
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Components.Alpha :
alpha
alphaBottomLeft
alphaBottomRight
alphaTopLeft
alphaTopRight
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.ComputedSize :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.Crop :
isCropped
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Flip :
flipX
flipY
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
From Phaser.GameObjects.Components.Pipeline :
defaultPipeline
pipeline
pipelineData
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
From Phaser.GameObjects.Components.Tint :
isTinted
tint
tintBottomLeft
tintBottomRight
tintFill
tintTopLeft
tintTopRight
From Phaser.GameObjects.Components.Transform :
angle
hasTransformComponent
rotation
scale
scaleX
scaleY
w
x
y
z
From Phaser.GameObjects.Components.Visible :
visible
From Phaser.GameObjects.GameObject :
active
body
cameraFilter
data
displayList
ignoreDestroy
input
name
parentContainer
renderFlags
scene
state
tabIndex
type
Public Members ​
canvas ​
canvas: HTMLCanvasElement ​
Description:
The Canvas element that the TileSprite renders its fill pattern in to.
Only used in Canvas mode.
Source: src/gameobjects/tilesprite/TileSprite.js#L173
Since: 3.12.0
context ​
context: CanvasRenderingContext2D ​
Description:
The Context of the Canvas element that the TileSprite renders its fill pattern in to.
Only used in Canvas mode.
Source: src/gameobjects/tilesprite/TileSprite.js#L183
Since: 3.12.0
dirty ​
dirty: boolean ​
Description:
Whether the Tile Sprite has changed in some way, requiring an re-render of its tile texture.
Such changes include the texture frame and scroll position of the Tile Sprite.
Source: src/gameobjects/tilesprite/TileSprite.js#L152
Since: 3.0.0
fillCanvas ​
fillCanvas: HTMLCanvasElement ​
Description:
The Canvas that the TileSprites texture is rendered to.
This is used to create a WebGL texture from.
Source: src/gameobjects/tilesprite/TileSprite.js#L269
Since: 3.12.0
fillContext ​
fillContext: CanvasRenderingContext2D ​
Description:
The Canvas Context used to render the TileSprites texture.
Source: src/gameobjects/tilesprite/TileSprite.js#L279
Since: 3.12.0
fillPattern ​
fillPattern: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper , CanvasPattern ​
Description:
The texture that the Tile Sprite is rendered to, which is then rendered to a Scene.
In WebGL this is a WebGLTextureWrapper. In Canvas it's a Canvas Fill Pattern.
Source: src/gameobjects/tilesprite/TileSprite.js#L288
Since: 3.12.0
frame ​
frame: Phaser.Textures.Frame ​
Description:
The Texture Frame this Game Object is using to render with.
Overrides: Phaser.GameObjects.Components.Crop#frame
Source: src/gameobjects/tilesprite/TileSprite.js#L242
Since: 3.0.0
potHeight ​
potHeight: number ​
Description:
The next power of two value from the height of the Fill Pattern frame.
Source: src/gameobjects/tilesprite/TileSprite.js#L260
Since: 3.0.0
potWidth ​
potWidth: number ​
Description:
The next power of two value from the width of the Fill Pattern frame.
Source: src/gameobjects/tilesprite/TileSprite.js#L251
Since: 3.0.0
renderer ​
renderer: Phaser.Renderer.Canvas.CanvasRenderer , Phaser.Renderer.WebGL.WebGLRenderer ​
Description:
The renderer in use by this Tile Sprite.
Source: src/gameobjects/tilesprite/TileSprite.js#L164
Since: 3.0.0
texture ​
texture: Phaser.Textures.Texture , Phaser.Textures.CanvasTexture ​
Description:
The Texture this Game Object is using to render with.
Overrides: Phaser.GameObjects.Components.Crop#texture
Source: src/gameobjects/tilesprite/TileSprite.js#L233
Since: 3.0.0
tilePositionX ​
tilePositionX: number ​
Description:
The horizontal scroll position of the Tile Sprite.
Source: src/gameobjects/tilesprite/TileSprite.js#L579
Since: 3.0.0
tilePositionY ​
tilePositionY: number ​
Description:
The vertical scroll position of the Tile Sprite.
Source: src/gameobjects/tilesprite/TileSprite.js#L602
Since: 3.0.0
tileScaleX ​
tileScaleX: number ​
Description:
The horizontal scale of the Tile Sprite texture.
Source: src/gameobjects/tilesprite/TileSprite.js#L625
Since: 3.11.0
tileScaleY ​
tileScaleY: number ​
Description:
The vertical scale of the Tile Sprite texture.
Source: src/gameobjects/tilesprite/TileSprite.js#L648
Since: 3.11.0
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
From Phaser.GameObjects.Components.Alpha :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.ComputedSize :
setDisplaySize
setSize
From Phaser.GameObjects.Components.Crop :
setCrop
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Flip :
resetFlip
setFlip
setFlipX
setFlipY
toggleFlipX
toggleFlipY
From Phaser.GameObjects.Components.GetBounds :
getBottomCenter
getBottomLeft
getBottomRight
getBounds
getCenter
getLeftCenter
getRightCenter
getTopCenter
getTopLeft
getTopRight
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
From Phaser.GameObjects.Components.Pipeline :
getPipelineName
initPipeline
resetPipeline
setPipeline
setPipelineData
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
From Phaser.GameObjects.Components.Tint :
clearTint
setTint
setTintFill
From Phaser.GameObjects.Components.Transform :
copyPosition
getLocalPoint
getLocalTransformMatrix
getParentRotation
getWorldPoint
getWorldTransformMatrix
setAngle
setPosition
setRandomPosition
setRotation
setScale
setW
setX
setY
setZ
From Phaser.GameObjects.Components.Visible :
setVisible
From Phaser.GameObjects.GameObject :
addedToScene
addToDisplayList
addToUpdateList
destroy
disableInteractive
getData
getDisplayList
getIndexList
incData
removedFromScene
removeFromDisplayList
removeFromUpdateList
removeInteractive
setActive
setData
setDataEnabled
setInteractive
setName
setState
toggleData
toJSON
update
willRender
Public Methods ​
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/tilesprite/TileSprite.js#L545
Since: 3.9.0
setFrame ​
<instance> setFrame(frame) ​
Description:
Sets the frame this Game Object will use to render with.
The Frame has to belong to the current Texture being used.
It can be either a string or an index.
Parameters:
name type optional description
frame string | number No The name or index of the frame within the Texture.
Returns: Phaser.GameObjects.TileSprite - This Game Object instance.
Source: src/gameobjects/tilesprite/TileSprite.js#L326
Since: 3.0.0
setTexture ​
<instance> setTexture(key, [frame]) ​
Description:
Sets the texture and frame this Game Object will use to render with.
Textures are referenced by their string-based keys, as stored in the Texture Manager.
Parameters:
name type optional description
key string No The key of the texture to be used, as stored in the Texture Manager.
frame string | number Yes The name or index of the frame within the Texture.
Returns: Phaser.GameObjects.TileSprite - This Game Object instance.
Source: src/gameobjects/tilesprite/TileSprite.js#L306
Since: 3.0.0
setTilePosition ​
<instance> setTilePosition([x], [y]) ​
Description:
Sets Phaser.GameObjects.TileSprite#tilePositionX and Phaser.GameObjects.TileSprite#tilePositionY .
Parameters:
name type optional description
x number Yes The x position of this sprite's tiling texture.
y number Yes The y position of this sprite's tiling texture.
Returns: Phaser.GameObjects.TileSprite - This Tile Sprite instance.
Source: src/gameobjects/tilesprite/TileSprite.js#L368
Since: 3.3.0
setTileScale ​
<instance> setTileScale([x], [y]) ​
Description:
Sets Phaser.GameObjects.TileSprite#tileScaleX and Phaser.GameObjects.TileSprite#tileScaleY .
Parameters:
name type optional default description
x number Yes The horizontal scale of the tiling texture. If not given it will use the current tileScaleX value.
y number Yes "x" The vertical scale of the tiling texture. If not given it will use the x value.
Returns: Phaser.GameObjects.TileSprite - This Tile Sprite instance.
Source: src/gameobjects/tilesprite/TileSprite.js#L394
Since: 3.12.0
Previous
TextStyle
Next
Triangle
Inherited Members
Public Members
canvas
context
dirty
fillCanvas
fillContext
fillPattern
frame
potHeight
potWidth
renderer
texture
tilePositionX
tilePositionY
tileScaleX
tileScaleY
Inherited Methods
Public Methods
preDestroy
setFrame
setTexture
setTilePosition
setTileScale
