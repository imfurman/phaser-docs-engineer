# Rope | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-rope

Phaser API Documentation
Class
Rope
Version: Phaser v3.90.0
On this page
Rope
A Rope Game Object.
The Rope object is WebGL only and does not have a Canvas counterpart.
A Rope is a special kind of Game Object that has a texture is stretched along its entire length.
Unlike a Sprite, it isn't restricted to using just a quad and can have as many vertices as you define
when creating it. The vertices can be arranged in a horizontal or vertical strip and have their own
color and alpha values as well.
A Ropes origin is always 0.5 x 0.5 and cannot be changed.
Constructor
new Rope(scene, [x], [y], [texture], [frame], [points], [horizontal], [colors], [alphas])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
texture string Yes The key of the Texture this Game Object will use to render with, as stored in the Texture Manager. If not given, __DEFAULT is used.
frame string | number null Yes
points number | Array.< Phaser.Types.Math.Vector2Like > Yes 2 An array containing the vertices data for this Rope, or a number that indicates how many segments to split the texture frame into. If none is provided a simple quad is created. See setPoints to set this post-creation.
horizontal boolean Yes true Should the vertices of this Rope be aligned horizontally ( true ), or vertically ( false )?
colors Array.<number> Yes An optional array containing the color data for this Rope. You should provide one color value per pair of vertices.
alphas Array.<number> Yes An optional array containing the alpha data for this Rope. You should provide one alpha value per pair of vertices.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Flip
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.Size
Phaser.GameObjects.Components.Texture
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Phaser.GameObjects.Components.ScrollFactor
Source: src/gameobjects/rope/Rope.js#L15
Since: 3.23.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
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
From Phaser.GameObjects.Components.Size :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.Texture :
frame
texture
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
alphas ​
alphas: Float32Array ​
Description:
An array containing the alpha data for this Rope.
Alphas should be given as float values, such as 0.5.
You should provide two alpha values for every point in the Rope, one for the top and one for the bottom of each quad.
You can modify the contents of this array directly in real-time, however, should you need to change the size
of the array, then you should use the setAlphas method instead.
Source: src/gameobjects/rope/Rope.js#L154
Since: 3.23.0
anims ​
anims: Phaser.Animations.AnimationState ​
Description:
The Animation State of this Rope.
Source: src/gameobjects/rope/Rope.js#L89
Since: 3.23.0
colors ​
colors: Uint32Array ​
Description:
An array containing the color data for this Rope.
Colors should be given as numeric RGB values, such as 0xff0000.
You should provide two color values for every point in the Rope, one for the top and one for the bottom of each quad.
You can modify the contents of this array directly in real-time, however, should you need to change the size
of the array, then you should use the setColors method instead.
Source: src/gameobjects/rope/Rope.js#L139
Since: 3.23.0
debugCallback ​
debugCallback: function ​
Description:
You can optionally choose to render the vertices of this Rope to a Graphics instance.
Achieve this by setting the debugCallback and the debugGraphic properties.
You can do this in a single call via the Rope.setDebug method, which will use the
built-in debug function. You can also set it to your own callback. The callback
will be invoked once per render and sent the following parameters:
debugCallback(src, meshLength, verts)
src is the Rope instance being debugged.
meshLength is the number of mesh vertices in total.
verts is an array of the translated vertex coordinates.
To disable rendering, set this property back to null .
Source: src/gameobjects/rope/Rope.js#L244
Since: 3.23.0
debugGraphic ​
debugGraphic: Phaser.GameObjects.Graphics ​
Description:
The Graphics instance that the debug vertices will be drawn to, if setDebug has
been called.
Source: src/gameobjects/rope/Rope.js#L267
Since: 3.23.0
dirty ​
dirty: boolean ​
Description:
If the Rope is marked as dirty it will automatically recalculate its vertices
the next time it renders. You can also force this by calling updateVertices .
Source: src/gameobjects/rope/Rope.js#L181
Since: 3.23.0
flipX ​
flipX: boolean ​
Description:
The horizontally flipped state of the Game Object.
A Game Object that is flipped horizontally will render inversed on the horizontal axis.
Flipping always takes place from the middle of the texture and does not impact the scale value.
If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.
Overrides: Phaser.GameObjects.Components.Flip#flipX
Source: src/gameobjects/rope/Rope.js#L1067
Since: 3.23.0
flipY ​
flipY: boolean ​
Description:
The vertically flipped state of the Game Object.
A Game Object that is flipped vertically will render inversed on the vertical axis (i.e. upside down)
Flipping always takes place from the middle of the texture and does not impact the scale value.
If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.
Overrides: Phaser.GameObjects.Components.Flip#flipY
Source: src/gameobjects/rope/Rope.js#L1095
Since: 3.23.0
horizontal ​
horizontal: boolean ​
Description:
Are the Rope vertices aligned horizontally, in a strip, or vertically, in a column?
This property is set during instantiation and cannot be changed directly.
See the setVertical and setHorizontal methods.
Source: src/gameobjects/rope/Rope.js#L191
Since: 3.23.0
points ​
points: Array.< Phaser.Types.Math.Vector2Like > ​
Description:
An array containing the points data for this Rope.
Each point should be given as a Vector2Like object (i.e. a Vector2, Geom.Point or object with public x/y properties).
The point coordinates are given in local space, where 0 x 0 is the start of the Rope strip.
You can modify the contents of this array directly in real-time to create interesting effects.
If you do so, be sure to call setDirty after modifying this array, so that the vertices data is
updated before the next render. Alternatively, you can use the setPoints method instead.
Should you need to change the size of this array, then you should always use the setPoints method.
Source: src/gameobjects/rope/Rope.js#L98
Since: 3.23.0
tintFill ​
tintFill: boolean ​
Description:
The tint fill mode.
false = An additive tint (the default), where vertices colors are blended with the texture.
true = A fill tint, where the vertices colors replace the texture, but respects texture alpha.
Source: src/gameobjects/rope/Rope.js#L169
Since: 3.23.0
uv ​
uv: Float32Array ​
Description:
An array containing the uv data for this Rope.
This data is calculated automatically in the setPoints method, based on the points provided.
Source: src/gameobjects/rope/Rope.js#L128
Since: 3.23.0
vertices ​
vertices: Float32Array ​
Description:
An array containing the vertices data for this Rope.
This data is calculated automatically in the updateVertices method, based on the points provided.
Source: src/gameobjects/rope/Rope.js#L117
Since: 3.23.0
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
From Phaser.GameObjects.Components.AlphaSingle :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
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
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
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
From Phaser.GameObjects.Components.Size :
setDisplaySize
setSize
setSizeToFrame
From Phaser.GameObjects.Components.Texture :
setFrame
setTexture
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
play ​
<instance> play(key, [ignoreIfPlaying], [startFrame]) ​
Description:
Start playing the given animation.
Parameters:
name type optional default description
key string No The string-based key of the animation to play.
ignoreIfPlaying boolean Yes false If an animation is already playing then ignore this call.
startFrame number Yes 0 Optionally start the animation playing from this frame index.
Returns: Phaser.GameObjects.Rope - This Game Object.
Source: src/gameobjects/rope/Rope.js#L328
Since: 3.23.0
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
The Rope update loop.
Access: protected
Parameters:
name type optional description
time number No The current timestamp.
delta number No The delta time, in ms, elapsed since the last frame.
Source: src/gameobjects/rope/Rope.js#L305
Since: 3.23.0
renderDebugVerts ​
<instance> renderDebugVerts(src, meshLength, verts) ​
Description:
The built-in Rope vertices debug rendering method.
See Rope.setDebug for more details.
Parameters:
name type optional description
src Phaser.GameObjects.Rope No The Rope object being rendered.
meshLength number No The number of vertices in the mesh.
verts Array.<number> No An array of translated vertex coordinates.
Source: src/gameobjects/rope/Rope.js#L1002
Since: 3.23.0
resizeArrays ​
<instance> resizeArrays(newSize) ​
Description:
Resizes all of the internal arrays: vertices , uv , colors and alphas to the new
given Rope segment total.
Parameters:
name type optional description
newSize number No The amount of segments to split the Rope in to.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L845
Since: 3.23.0
setAlphas ​
<instance> setAlphas([alphas], [bottomAlpha]) ​
Description:
Set the alpha values used by the Rope during rendering.
You can provide the values in a number of ways:
One single numeric value: setAlphas(0.5) - This will set a single alpha for the whole Rope.
Two numeric value: setAlphas(1, 0.5) - This will set a 'top' and 'bottom' alpha value across the whole Rope.
An array of values: setAlphas([ 1, 0.5, 0.2 ])
If you provide an array of values and the array has exactly the same number of values as points in the Rope, it
will use each alpha value per rope segment.
If the provided array has a different number of values than points then it will use the values in order, from
the first Rope segment and on, until it runs out of values. This allows you to control the alpha values at all
vertices in the Rope.
Note this method is called setAlphas (plural) and not setAlpha .
Parameters:
name type optional description
alphas number | Array.<number> Yes Either a single alpha value, or an array of values. If nothing is provided alpha is reset to 1.
bottomAlpha number Yes An optional bottom alpha value. See the method description for details.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L451
Since: 3.23.0
setColors ​
<instance> setColors([colors]) ​
Description:
Set the color values used by the Rope during rendering.
Colors are used to control the level of tint applied across the Rope texture.
You can provide the values in a number of ways:
One single numeric value: setColors(0xff0000) - This will set a single color tint for the whole Rope.
An array of values: setColors([ 0xff0000, 0x00ff00, 0x0000ff ])
If you provide an array of values and the array has exactly the same number of values as points in the Rope, it
will use each color per rope segment.
If the provided array has a different number of values than points then it will use the values in order, from
the first Rope segment and on, until it runs out of values. This allows you to control the color values at all
vertices in the Rope.
Parameters:
name type optional description
colors number | Array.<number> Yes Either a single color value, or an array of values. If nothing is provided color is reset to 0xffffff.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L550
Since: 3.23.0
setDebug ​
<instance> setDebug([graphic], [callback]) ​
Description:
This method enables rendering of the Rope vertices to the given Graphics instance.
If you enable this feature, you must call Graphics.clear() in your Scene update ,
otherwise the Graphics instance you provide to debug will fill-up with draw calls,
eventually crashing the browser. This is not done automatically to allow you to debug
draw multiple Rope objects to a single Graphics instance.
The Rope class has a built-in debug rendering callback Rope.renderDebugVerts , however
you can also provide your own callback to be used instead. Do this by setting the callback parameter.
The callback is invoked once per render and sent the following parameters:
callback(src, meshLength, verts)
src is the Rope instance being debugged.
meshLength is the number of mesh vertices in total.
verts is an array of the translated vertex coordinates.
If using your own callback you do not have to provide a Graphics instance to this method.
To disable debug rendering, to either your own callback or the built-in one, call this method
with no arguments.
Parameters:
name type optional description
graphic Phaser.GameObjects.Graphics Yes The Graphic instance to render to if using the built-in callback.
callback function Yes The callback to invoke during debug render. Leave as undefined to use the built-in callback.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L950
Since: 3.23.0
setDirty ​
<instance> setDirty() ​
Description:
Flags this Rope as being dirty. A dirty rope will recalculate all of its vertices data
the next time it renders. You should set this rope as dirty if you update the points
array directly.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L347
Since: 3.23.0
setHorizontal ​
<instance> setHorizontal([points], [colors], [alphas]) ​
Description:
Sets the alignment of the points in this Rope to be horizontal, in a strip format.
Calling this method will reset this Rope. The current points, vertices, colors and alpha
values will be reset to thoes values given as parameters.
Parameters:
name type optional description
points number | Array.< Phaser.Types.Math.Vector2Like > Yes An array containing the vertices data for this Rope, or a number that indicates how many segments to split the texture frame into. If none is provided the current points length is used.
colors number | Array.<number> Yes Either a single color value, or an array of values.
alphas number | Array.<number> Yes Either a single alpha value, or an array of values.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L364
Since: 3.23.0
setPoints ​
<instance> setPoints([points], [colors], [alphas]) ​
Description:
Sets the points used by this Rope.
The points should be provided as an array of Vector2, or vector2-like objects (i.e. those with public x/y properties).
Each point corresponds to one segment of the Rope. The more points in the array, the more segments the rope has.
Point coordinates are given in local-space, not world-space, and are directly related to the size of the texture
this Rope object is using.
For example, a Rope using a 512 px wide texture, split into 4 segments (128px each) would use the following points:
rope . setPoints ( [
{ x : 0 , y : 0 } ,
{ x : 128 , y : 0 } ,
{ x : 256 , y : 0 } ,
{ x : 384 , y : 0 }
] ) ;
Or, you can provide an integer to do the same thing:
rope . setPoints ( 4 ) ;
Which will divide the Rope into 4 equally sized segments based on the frame width.
Note that calling this method with a different number of points than the Rope has currently will
reset the color and alpha values, unless you provide them as arguments to this method.
Parameters:
name type optional default description
points number | Array.< Phaser.Types.Math.Vector2Like > Yes 2 An array containing the vertices data for this Rope, or a number that indicates how many segments to split the texture frame into. If none is provided a simple quad is created.
colors number | Array.<number> Yes Either a single color value, or an array of values.
alphas number | Array.<number> Yes Either a single alpha value, or an array of values.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L635
Since: 3.23.0
setTintFill ​
<instance> setTintFill([value]) ​
Description:
Sets the tint fill mode.
Mode 0 ( false ) is an additive tint, the default, which blends the vertices colors with the texture.
This mode respects the texture alpha.
Mode 1 ( true ) is a fill tint. Unlike an additive tint, a fill-tint literally replaces the pixel colors
from the texture with those in the tint. You can use this for effects such as making a player flash 'white'
if hit by something. This mode respects the texture alpha.
See the setColors method for details of how to color each of the vertices.
Tags:
webglOnly
Parameters:
name type optional default description
value boolean Yes false Set to false for an Additive tint or true fill tint with alpha.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L422
Since: 3.23.0
setVertical ​
<instance> setVertical([points], [colors], [alphas]) ​
Description:
Sets the alignment of the points in this Rope to be vertical, in a column format.
Calling this method will reset this Rope. The current points, vertices, colors and alpha
values will be reset to thoes values given as parameters.
Parameters:
name type optional description
points number | Array.< Phaser.Types.Math.Vector2Like > Yes An array containing the vertices data for this Rope, or a number that indicates how many segments to split the texture frame into. If none is provided the current points length is used.
colors number | Array.<number> Yes Either a single color value, or an array of values.
alphas number | Array.<number> Yes Either a single alpha value, or an array of values.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L393
Since: 3.23.0
updateUVs ​
<instance> updateUVs() ​
Description:
Updates all of the UVs based on the Rope.points and flipX and flipY settings.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L757
Since: 3.23.0
updateVertices ​
<instance> updateVertices() ​
Description:
Updates the vertices based on the Rope points.
This method is called automatically during rendering if Rope.dirty is true , which is set
by the setPoints and setDirty methods. You should flag the Rope as being dirty if you modify
the Rope points directly.
Returns: Phaser.GameObjects.Rope - This Game Object instance.
Source: src/gameobjects/rope/Rope.js#L882
Since: 3.23.0
Previous
RenderTexture
Next
Shader
Inherited Members
Public Members
alphas
anims
colors
debugCallback
debugGraphic
dirty
flipX
flipY
horizontal
points
tintFill
uv
vertices
Inherited Methods
Public Methods
play
preUpdate
renderDebugVerts
resizeArrays
setAlphas
setColors
setDebug
setDirty
setHorizontal
setPoints
setTintFill
setVertical
updateUVs
updateVertices
