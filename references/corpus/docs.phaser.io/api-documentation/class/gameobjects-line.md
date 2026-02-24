# Line | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-line

Phaser API Documentation
Class
Line
Version: Phaser v3.90.0
On this page
Line
The Line Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports only stroke colors and cannot be filled.
A Line Shape allows you to draw a line between two points in your game. You can control the
stroke color and thickness of the line. In WebGL only you can also specify a different
thickness for the start and end of the line, allowing you to render lines that taper-off.
If you need to draw multiple lines in a sequence you may wish to use the Polygon Shape instead.
Be aware that as with all Game Objects the default origin is 0.5. If you need to draw a Line
between two points and want the x1/y1 values to match the x/y values, then set the origin to 0.
Constructor
new Line(scene, [x], [y], [x1], [y1], [x2], [y2], [strokeColor], [strokeAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
x1 number Yes 0 The horizontal position of the start of the line.
y1 number Yes 0 The vertical position of the start of the line.
x2 number Yes 128 The horizontal position of the end of the line.
y2 number Yes 0 The vertical position of the end of the line.
strokeColor number Yes The color the line will be drawn in, i.e. 0xff0000 for red.
strokeAlpha number Yes The alpha the line will be drawn in. You can also set the alpha of the overall Shape using its alpha property.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/line/Line.js#L12
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
pathData
pathIndexes
radius
strokeAlpha
strokeColor
width
Public Members ​
lineWidth ​
lineWidth: number ​
Description:
The width (or thickness) of the line.
See the setLineWidth method for extra details on changing this on WebGL.
Overrides: Phaser.GameObjects.Shape#lineWidth
Source: src/gameobjects/shape/line/Line.js#L70
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
setFillStyle
setStrokeStyle
Public Methods ​
setLineWidth ​
<instance> setLineWidth(startWidth, [endWidth]) ​
Description:
Sets the width of the line.
When using the WebGL renderer you can have different start and end widths.
When using the Canvas renderer only the startWidth value is used. The endWidth is ignored.
This call can be chained.
Parameters:
name type optional description
startWidth number No The start width of the line.
endWidth number Yes The end width of the line. Only used in WebGL.
Returns: Phaser.GameObjects.Line - This Game Object instance.
Source: src/gameobjects/shape/line/Line.js#L111
Since: 3.13.0
setTo ​
<instance> setTo([x1], [y1], [x2], [y2]) ​
Description:
Sets the start and end coordinates of this Line.
Parameters:
name type optional default description
x1 number Yes 0 The horizontal position of the start of the line.
y1 number Yes 0 The vertical position of the start of the line.
x2 number Yes 0 The horizontal position of the end of the line.
y2 number Yes 0 The vertical position of the end of the line.
Returns: Phaser.GameObjects.Line - This Line object.
Source: src/gameobjects/shape/line/Line.js#L139
Since: 3.13.0
Previous
LightsPlugin
Next
Mesh
Inherited Members
Public Members
lineWidth
Inherited Methods
Public Methods
setLineWidth
setTo
