# Triangle | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-triangle

Phaser API Documentation
Class
Triangle
Version: Phaser v3.90.0
On this page
Triangle
The Triangle Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports both fill and stroke colors.
The Triangle consists of 3 lines, joining up to form a triangular shape. You can control the
position of each point of these lines. The triangle is always closed and cannot have an open
face. If you require that, consider using a Polygon instead.
Constructor
new Triangle(scene, [x], [y], [x1], [y1], [x2], [y2], [x3], [y3], [fillColor], [fillAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
x1 number Yes 0 The horizontal position of the first point in the triangle.
y1 number Yes 128 The vertical position of the first point in the triangle.
x2 number Yes 64 The horizontal position of the second point in the triangle.
y2 number Yes 0 The vertical position of the second point in the triangle.
x3 number Yes 128 The horizontal position of the third point in the triangle.
y3 number Yes 128 The vertical position of the third point in the triangle.
fillColor number Yes The color the triangle will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes The alpha the triangle will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/triangle/Triangle.js#L12
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
setTo ​
<instance> setTo([x1], [y1], [x2], [y2], [x3], [y3]) ​
Description:
Sets the data for the lines that make up this Triangle shape.
Parameters:
name type optional default description
x1 number Yes 0 The horizontal position of the first point in the triangle.
y1 number Yes 0 The vertical position of the first point in the triangle.
x2 number Yes 0 The horizontal position of the second point in the triangle.
y2 number Yes 0 The vertical position of the second point in the triangle.
x3 number Yes 0 The horizontal position of the third point in the triangle.
y3 number Yes 0 The vertical position of the third point in the triangle.
Returns: Phaser.GameObjects.Triangle - This Game Object instance.
Source: src/gameobjects/shape/triangle/Triangle.js#L81
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
Previous
TileSprite
Next
UpdateList
Inherited Methods
Public Methods
setTo
Inherited Members
