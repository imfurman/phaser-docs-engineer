# IsoBox | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-isobox

Phaser API Documentation
Class
IsoBox
Version: Phaser v3.90.0
On this page
IsoBox
The IsoBox Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports only fill colors and cannot be stroked.
An IsoBox is an 'isometric' rectangle. Each face of it has a different fill color. You can set
the color of the top, left and right faces of the rectangle respectively. You can also choose
which of the faces are rendered via the showTop , showLeft and showRight properties.
You cannot view an IsoBox from under-neath, however you can change the 'angle' by setting
the projection property.
Constructor
new IsoBox(scene, [x], [y], [size], [height], [fillTop], [fillLeft], [fillRight])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
size number Yes 48 The width of the iso box in pixels. The left and right faces will be exactly half this value.
height number Yes 32 The height of the iso box. The left and right faces will be this tall. The overall height of the isobox will be this value plus half the size value.
fillTop number Yes "0xeeeeee" The fill color of the top face of the iso box.
fillLeft number Yes "0x999999" The fill color of the left face of the iso box.
fillRight number Yes "0xcccccc" The fill color of the right face of the iso box.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/isobox/IsoBox.js#L11
Since: 3.13.0
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
From Phaser.GameObjects.Shape :
closePath
displayHeight
displayWidth
fillAlpha
fillColor
geom
height
isFilled
isRounded
isStroked
lineWidth
pathData
pathIndexes
radius
strokeAlpha
strokeColor
width
Public Members ​
fillLeft ​
fillLeft: number ​
Description:
The color used to fill in the left-facing side of the iso box.
Source: src/gameobjects/shape/isobox/IsoBox.js#L83
Since: 3.13.0
fillRight ​
fillRight: number ​
Description:
The color used to fill in the right-facing side of the iso box.
Source: src/gameobjects/shape/isobox/IsoBox.js#L92
Since: 3.13.0
fillTop ​
fillTop: number ​
Description:
The color used to fill in the top of the iso box.
Source: src/gameobjects/shape/isobox/IsoBox.js#L74
Since: 3.13.0
projection ​
projection: number ​
Description:
The projection level of the iso box. Change this to change the 'angle' at which you are looking at the box.
Source: src/gameobjects/shape/isobox/IsoBox.js#L64
Since: 3.13.0
showLeft ​
showLeft: boolean ​
Description:
Controls if the left-face of the iso box be rendered.
Source: src/gameobjects/shape/isobox/IsoBox.js#L111
Since: 3.13.0
showRight ​
showRight: boolean ​
Description:
Controls if the right-face of the iso box be rendered.
Source: src/gameobjects/shape/isobox/IsoBox.js#L121
Since: 3.13.0
showTop ​
showTop: boolean ​
Description:
Controls if the top-face of the iso box be rendered.
Source: src/gameobjects/shape/isobox/IsoBox.js#L101
Since: 3.13.0
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
From Phaser.GameObjects.Shape :
preDestroy
setClosePath
setDisplaySize
setStrokeStyle
Public Methods ​
setFaces ​
<instance> setFaces([showTop], [showLeft], [showRight]) ​
Description:
Sets which faces of the iso box will be rendered.
This call can be chained.
Parameters:
name type optional default description
showTop boolean Yes true Show the top-face of the iso box.
showLeft boolean Yes true Show the left-face of the iso box.
showRight boolean Yes true Show the right-face of the iso box.
Returns: Phaser.GameObjects.IsoBox - This Game Object instance.
Source: src/gameobjects/shape/isobox/IsoBox.js#L157
Since: 3.13.0
setFillStyle ​
<instance> setFillStyle([fillTop], [fillLeft], [fillRight]) ​
Description:
Sets the fill colors for each face of the iso box.
This call can be chained.
Parameters:
name type optional description
fillTop number Yes The color used to fill the top of the iso box.
fillLeft number Yes The color used to fill in the left-facing side of the iso box.
fillRight number Yes The color used to fill in the right-facing side of the iso box.
Overrides: Phaser.GameObjects.Shape#setFillStyle
Returns: Phaser.GameObjects.IsoBox - This Game Object instance.
Source: src/gameobjects/shape/isobox/IsoBox.js#L183
Since: 3.13.0
setProjection ​
<instance> setProjection(value) ​
Description:
Sets the projection level of the iso box. Change this to change the 'angle' at which you are looking at the box.
This call can be chained.
Parameters:
name type optional description
value number No The value to set the projection to.
Returns: Phaser.GameObjects.IsoBox - This Game Object instance.
Source: src/gameobjects/shape/isobox/IsoBox.js#L139
Since: 3.13.0
Previous
Image
Next
IsoTriangle
Inherited Members
Public Members
fillLeft
fillRight
fillTop
projection
showLeft
showRight
showTop
Inherited Methods
Public Methods
setFaces
setFillStyle
setProjection
