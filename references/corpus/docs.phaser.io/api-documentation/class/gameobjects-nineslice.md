# NineSlice | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-nineslice

Phaser API Documentation
Class
NineSlice
Version: Phaser v3.90.0
On this page
NineSlice
A Nine Slice Game Object allows you to display a texture-based object that
can be stretched both horizontally and vertically, but that retains
fixed-sized corners. The dimensions of the corners are set via the
parameters to this class.
This is extremely useful for UI and button like elements, where you need
them to expand to accommodate the content without distorting the texture.
The texture you provide for this Game Object should be based on the
following layout structure:
A B
+---+----------------------+---+
C | 1 | 2 | 3 |
+---+----------------------+---+
| | | |
| 4 | 5 | 6 |
| | | |
+---+----------------------+---+
D | 7 | 8 | 9 |
+---+----------------------+---+
When changing this objects width and / or height:
areas 1, 3, 7 and 9 (the corners) will remain unscaled
areas 2 and 8 will be stretched horizontally only
areas 4 and 6 will be stretched vertically only
area 5 will be stretched both horizontally and vertically
You can also create a 3 slice Game Object:
This works in a similar way, except you can only stretch it horizontally.
Therefore, it requires less configuration:
A B
+---+----------------------+---+
| | | |
C | 1 | 2 | 3 |
| | | |
+---+----------------------+---+
When changing this objects width (you cannot change its height)
areas 1 and 3 will remain unscaled
area 2 will be stretched horizontally
The above configuration concept is adapted from the Pixi NineSlicePlane.
To specify a 3 slice object instead of a 9 slice you should only
provide the leftWidth and rightWidth parameters. To create a 9 slice
you must supply all parameters.
The minimum width this Game Object can be is the total of
leftWidth + rightWidth . The minimum height this Game Object
can be is the total of topHeight + bottomHeight .
If you need to display this object at a smaller size, you can scale it.
In terms of performance, using a 3 slice Game Object is the equivalent of
having 3 Sprites in a row. Using a 9 slice Game Object is the equivalent
of having 9 Sprites in a row. The vertices of this object are all batched
together and can co-exist with other Sprites and graphics on the display
list, without incurring any additional overhead.
As of Phaser 3.60 this Game Object is WebGL only.
As of Phaser 3.70 this Game Object can now populate its values automatically
if they have been set within Texture Packer 7.1.0 or above and exported with
the atlas json. If this is the case, you can just call this method without
specifying anything more than the texture key and frame and it will pull the
area data from the atlas.
Constructor
new NineSlice(scene, x, y, texture, [frame], [width], [height], [leftWidth], [rightWidth], [topHeight], [bottomHeight])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number No The horizontal position of the center of this Game Object in the world.
y number No The vertical position of the center of this Game Object in the world.
texture string | Phaser.Textures.Texture No The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
width number Yes 256 The width of the Nine Slice Game Object. You can adjust the width post-creation.
height number Yes 256 The height of the Nine Slice Game Object. If this is a 3 slice object the height will be fixed to the height of the texture and cannot be changed.
leftWidth number Yes 10 The size of the left vertical column (A).
rightWidth number Yes 10 The size of the right vertical column (B).
topHeight number Yes 0 The size of the top horizontal row (C). Set to zero or undefined to create a 3 slice object.
bottomHeight number Yes 0 The size of the bottom horizontal row (D). Set to zero or undefined to create a 3 slice object.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Texture
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/nineslice/NineSlice.js#L13
Since: 3.60.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
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
bottomHeight ​
bottomHeight: number ​
Description:
The size of the bottom horizontal bar (D).
If this is a 3 slice object this property will be set to zero.
Source: src/gameobjects/nineslice/NineSlice.js#L265
Since: 3.60.0
displayHeight ​
displayHeight: number ​
Description:
The displayed height of this Game Object.
This value takes into account the scale factor.
Setting this value will adjust the Game Object's scale property.
Source: src/gameobjects/nineslice/NineSlice.js#L792
Since: 3.60.0
displayWidth ​
displayWidth: number ​
Description:
The displayed width of this Game Object.
This value takes into account the scale factor.
Setting this value will adjust the Game Object's scale property.
Source: src/gameobjects/nineslice/NineSlice.js#L767
Since: 3.60.0
height ​
height: number ​
Description:
The displayed height of this Game Object.
Setting this value will adjust the way in which this Nine Slice
object scales vertically, if configured to do so.
The minimum height this Game Object can be is the total of
topHeight + bottomHeight . If you need to display this object
at a smaller size, you can also scale it.
If this is a 3-slice object, you can only stretch it horizontally
and changing the height will be ignored.
Source: src/gameobjects/nineslice/NineSlice.js#L731
Since: 3.60.0
is3Slice ​
is3Slice: boolean ​
Description:
This property is true if this Nine Slice Game Object was configured
with just leftWidth and rightWidth values, making it a 3-slice
instead of a 9-slice object.
Source: src/gameobjects/nineslice/NineSlice.js#L304
Since: 3.60.0
isTinted ​
isTinted: boolean ​
Description:
Does this Game Object have a tint applied?
It checks to see if the tint property is set to a value other than 0xffffff.
This indicates that a Game Object is tinted.
Tags:
webglOnly
Source: src/gameobjects/nineslice/NineSlice.js#L680
Since: 3.60.0
leftWidth ​
leftWidth: number ​
Description:
The size of the left vertical bar (A).
Source: src/gameobjects/nineslice/NineSlice.js#L232
Since: 3.60.0
originX ​
originX: number ​
Description:
The horizontal origin of this Game Object.
The origin maps the relationship between the size and position of the Game Object.
The default value is 0.5, meaning all Game Objects are positioned based on their center.
Setting the value to 0 means the position now relates to the left of the Game Object.
Overrides: Phaser.GameObjects.Components.Origin#originX
Source: src/gameobjects/nineslice/NineSlice.js#L877
Since: 3.60.0
originY ​
originY: number ​
Description:
The vertical origin of this Game Object.
The origin maps the relationship between the size and position of the Game Object.
The default value is 0.5, meaning all Game Objects are positioned based on their center.
Setting the value to 0 means the position now relates to the top of the Game Object.
Overrides: Phaser.GameObjects.Components.Origin#originY
Source: src/gameobjects/nineslice/NineSlice.js#L902
Since: 3.60.0
rightWidth ​
rightWidth: number ​
Description:
The size of the right vertical bar (B).
Source: src/gameobjects/nineslice/NineSlice.js#L242
Since: 3.60.0
tint ​
tint: number ​
Description:
The tint value being applied to the top-left vertice of the Game Object.
This value is interpolated from the corner to the center of the Game Object.
The value should be set as a hex number, i.e. 0xff0000 for red, or 0xff00ff for purple.
Source: src/gameobjects/nineslice/NineSlice.js#L277
Since: 3.60.0
tintFill ​
tintFill: boolean ​
Description:
The tint fill mode.
false = An additive tint (the default), where vertices colors are blended with the texture.
true = A fill tint, where the vertices colors replace the texture, but respects texture alpha.
Source: src/gameobjects/nineslice/NineSlice.js#L289
Since: 3.60.0
topHeight ​
topHeight: number ​
Description:
The size of the top horizontal bar (C).
If this is a 3 slice object this property will be set to the
height of the texture being used.
Source: src/gameobjects/nineslice/NineSlice.js#L252
Since: 3.60.0
vertices ​
vertices: Array.< Phaser.Geom.Mesh.Vertex > ​
Description:
An array of Vertex objects that correspond to the quads that make-up
this Nine Slice Game Object. They are stored in the following order:
Top Left - Indexes 0 - 5
Top Center - Indexes 6 - 11
Top Right - Indexes 12 - 17
Center Left - Indexes 18 - 23
Center - Indexes 24 - 29
Center Right - Indexes 30 - 35
Bottom Left - Indexes 36 - 41
Bottom Center - Indexes 42 - 47
Bottom Right - Indexes 48 - 53
Each quad is represented by 6 Vertex instances.
This array will contain 18 elements for a 3 slice object
and 54 for a nine slice object.
You should never modify this array once it has been populated.
Source: src/gameobjects/nineslice/NineSlice.js#L205
Since: 3.60.0
width ​
width: number ​
Description:
The displayed width of this Game Object.
Setting this value will adjust the way in which this Nine Slice
object scales horizontally, if configured to do so.
The minimum width this Game Object can be is the total of
leftWidth + rightWidth . If you need to display this object
at a smaller size, you can also scale it.
Source: src/gameobjects/nineslice/NineSlice.js#L701
Since: 3.60.0
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
clearTint ​
<instance> clearTint() ​
Description:
Clears all tint values associated with this Game Object.
Immediately sets the color values back to 0xffffff and the tint type to 'additive',
which results in no visible change to the texture.
Tags:
webglOnly
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L598
Since: 3.60.0
setDisplaySize ​
<instance> setDisplaySize(width, height) ​
Description:
Sets the display size of this Game Object.
Calling this will adjust the scale.
Parameters:
name type optional description
width number No The width of this Game Object.
height number No The height of this Game Object.
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L856
Since: 3.60.0
setOrigin ​
<instance> setOrigin([x], [y]) ​
Description:
Sets the origin of this Game Object.
The values are given in the range 0 to 1.
Parameters:
name type optional default description
x number Yes 0.5 The horizontal origin value.
y number Yes "x" The vertical origin value. If not defined it will be set to the value of x .
Overrides: Phaser.GameObjects.Components.Origin#setOrigin
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L927
Since: 3.60.0
setSize ​
<instance> setSize(width, height) ​
Description:
Sets the size of this Game Object.
For a Nine Slice Game Object this means it will be stretched (or shrunk) horizontally
and vertically depending on the dimensions given to this method, in accordance with
how it has been configured for the various corner sizes.
If this is a 3-slice object, you can only stretch it horizontally
and changing the height will be ignored.
If you have enabled this Game Object for input, changing the size will also change the
size of the hit area.
Parameters:
name type optional description
width number No The width of this Game Object.
height number No The height of this Game Object.
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L817
Since: 3.60.0
setSizeToFrame ​
<instance> setSizeToFrame() ​
Description:
This method is included but does nothing for the Nine Slice Game Object,
because the size of the object isn't based on the texture frame.
You should not call this method.
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L953
Since: 3.60.0
setSlices ​
<instance> setSlices([width], [height], [leftWidth], [rightWidth], [topHeight], [bottomHeight], [skipScale9]) ​
Description:
Resets the width, height and slices for this NineSlice Game Object.
This allows you to modify the texture being used by this object and then reset the slice configuration,
to avoid having to destroy this Game Object in order to use it for a different game element.
Please note that you cannot change a 9-slice to a 3-slice or vice versa.
Parameters:
name type optional default description
width number Yes 256 The width of the Nine Slice Game Object. You can adjust the width post-creation.
height number Yes 256 The height of the Nine Slice Game Object. If this is a 3 slice object the height will be fixed to the height of the texture and cannot be changed.
leftWidth number Yes 10 The size of the left vertical column (A).
rightWidth number Yes 10 The size of the right vertical column (B).
topHeight number Yes 0 The size of the top horizontal row (C). Set to zero or undefined to create a 3 slice object.
bottomHeight number Yes 0 The size of the bottom horizontal row (D). Set to zero or undefined to create a 3 slice object.
skipScale9 boolean Yes false If this Nine Slice was created from Texture Packer scale9 atlas data, set this property to use the given column sizes instead of those specified in the JSON.
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L340
Since: 3.60.0
setTint ​
<instance> setTint([color]) ​
Description:
Sets an additive tint on this Game Object.
The tint works by taking the pixel color values from the Game Objects texture, and then
multiplying it by the color value of the tint.
To modify the tint color once set, either call this method again with new values or use the
tint property.
To remove a tint call clearTint , or call this method with no parameters.
To swap this from being an additive tint to a fill based tint set the property tintFill to true .
Tags:
webglOnly
Parameters:
name type optional default description
color number Yes "0xffffff" The tint being applied to the entire Game Object.
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L617
Since: 3.60.0
setTintFill ​
<instance> setTintFill([color]) ​
Description:
Sets a fill-based tint on this Game Object.
Unlike an additive tint, a fill-tint literally replaces the pixel colors from the texture
with those in the tint. You can use this for effects such as making a player flash 'white'
if hit by something. The whole Game Object will be rendered in the given color.
To modify the tint color once set, either call this method again with new values or use the
tint property.
To remove a tint call clearTint , or call this method with no parameters.
To swap this from being a fill-tint to an additive tint set the property tintFill to false .
Tags:
webglOnly
Parameters:
name type optional default description
color number Yes "0xffffff" The tint being applied to the entire Game Object.
Returns: Phaser.GameObjects.NineSlice - This Game Object instance.
Source: src/gameobjects/nineslice/NineSlice.js#L649
Since: 3.60.0
updateQuad ​
<instance> updateQuad(offset, x1, y1, x2, y2) ​
Description:
Internally updates the position coordinates across all vertices of the
given quad offset.
You should not typically need to call this method directly, but it
is left public should an extended class require it.
Parameters:
name type optional description
offset number No The offset in the vertices array of the quad to update.
x1 number No The top-left quad coordinate.
y1 number No The top-left quad coordinate.
x2 number No The bottom-right quad coordinate.
y2 number No The bottom-right quad coordinate.
Source: src/gameobjects/nineslice/NineSlice.js#L512
Since: 3.60.0
updateQuadUVs ​
<instance> updateQuadUVs(offset, u1, v1, u2, v2) ​
Description:
Internally updates the UV coordinates across all vertices of the
given quad offset, based on the frame size.
You should not typically need to call this method directly, but it
is left public should an extended class require it.
Parameters:
name type optional description
offset number No The offset in the vertices array of the quad to update.
u1 number No The top-left UV coordinate.
v1 number No The top-left UV coordinate.
u2 number No The bottom-right UV coordinate.
v2 number No The bottom-right UV coordinate.
Source: src/gameobjects/nineslice/NineSlice.js#L545
Since: 3.60.0
updateUVs ​
<instance> updateUVs() ​
Description:
Updates all of the vertice UV coordinates. This is called automatically
when the NineSlice Game Object is created, or if the texture frame changes.
Unlike with the updateVertice method, you do not need to call this
method if the Nine Slice changes size. Only if it changes texture frame.
Source: src/gameobjects/nineslice/NineSlice.js#L437
Since: 3.60.0
updateVertices ​
<instance> updateVertices() ​
Description:
Recalculates all of the vertices in this Nine Slice Game Object
based on the leftWidth , rightWidth , topHeight and bottomHeight
properties, combined with the Game Object size.
This method is called automatically when this object is created
or if it's origin is changed.
You should not typically need to call this method directly, but it
is left public should you find a need to modify one of those properties
after creation.
Source: src/gameobjects/nineslice/NineSlice.js#L472
Since: 3.60.0
Previous
Mesh
Next
EmitterColorOp
Inherited Members
Public Members
bottomHeight
displayHeight
displayWidth
height
is3Slice
isTinted
leftWidth
originX
originY
rightWidth
tint
tintFill
topHeight
vertices
width
Inherited Methods
Public Methods
clearTint
setDisplaySize
setOrigin
setSize
setSizeToFrame
setSlices
setTint
setTintFill
updateQuad
updateQuadUVs
updateUVs
updateVertices
