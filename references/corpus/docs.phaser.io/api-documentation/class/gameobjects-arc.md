# Arc | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-arc

Phaser API Documentation
Class
Arc
Version: Phaser v3.90.0
On this page
Arc
The Arc Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports both fill and stroke colors.
When it renders it displays an arc shape. You can control the start and end angles of the arc,
as well as if the angles are winding clockwise or anti-clockwise. With the default settings
it renders as a complete circle. By changing the angles you can create other arc shapes,
such as half-circles.
Arcs also have an iterations property and corresponding setIterations method. This allows
you to control how smooth the shape renders in WebGL, by controlling the number of iterations
that take place during construction.
Constructor
new Arc(scene, [x], [y], [radius], [startAngle], [endAngle], [anticlockwise], [fillColor], [fillAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
radius number Yes 128 The radius of the arc.
startAngle number Yes 0 The start angle of the arc, in degrees.
endAngle number Yes 360 The end angle of the arc, in degrees.
anticlockwise boolean Yes false The winding order of the start and end angles.
fillColor number Yes The color the arc will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes The alpha the arc will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/arc/Arc.js#L15
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
strokeAlpha
strokeColor
width
Public Members ​
anticlockwise ​
anticlockwise: boolean ​
Description:
The winding order of the start and end angles.
Source: src/gameobjects/shape/arc/Arc.js#L223
Since: 3.13.0
endAngle ​
endAngle: number ​
Description:
The end angle of the arc, in degrees.
Source: src/gameobjects/shape/arc/Arc.js#L200
Since: 3.13.0
iterations ​
iterations: number ​
Description:
The number of iterations used when drawing the arc.
Increase this value for smoother arcs, at the cost of more polygons being rendered.
Modify this value by small amounts, such as 0.01.
Source: src/gameobjects/shape/arc/Arc.js#L125
Since: 3.13.0
radius ​
radius: number ​
Description:
The radius of the arc.
Overrides: Phaser.GameObjects.Shape#radius
Source: src/gameobjects/shape/arc/Arc.js#L151
Since: 3.13.0
startAngle ​
startAngle: number ​
Description:
The start angle of the arc, in degrees.
Source: src/gameobjects/shape/arc/Arc.js#L177
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
setEndAngle ​
<instance> setEndAngle(value) ​
Description:
Sets the ending angle of the arc, in degrees.
This call can be chained.
Parameters:
name type optional description
value number No The value to set the ending angle to.
Returns: Phaser.GameObjects.Arc - This Game Object instance.
Source: src/gameobjects/shape/arc/Arc.js#L309
Since: 3.13.0
setIterations ​
<instance> setIterations(value) ​
Description:
Sets the number of iterations used when drawing the arc.
Increase this value for smoother arcs, at the cost of more polygons being rendered.
Modify this value by small amounts, such as 0.01.
This call can be chained.
Parameters:
name type optional description
value number No The value to set the iterations to.
Returns: Phaser.GameObjects.Arc - This Game Object instance.
Source: src/gameobjects/shape/arc/Arc.js#L264
Since: 3.13.0
setRadius ​
<instance> setRadius(value) ​
Description:
Sets the radius of the arc.
This call can be chained.
Parameters:
name type optional description
value number No The value to set the radius to.
Returns: Phaser.GameObjects.Arc - This Game Object instance.
Source: src/gameobjects/shape/arc/Arc.js#L246
Since: 3.13.0
setStartAngle ​
<instance> setStartAngle(value) ​
Description:
Sets the starting angle of the arc, in degrees.
This call can be chained.
Parameters:
name type optional description
value number No The value to set the starting angle to.
Returns: Phaser.GameObjects.Arc - This Game Object instance.
Source: src/gameobjects/shape/arc/Arc.js#L286
Since: 3.13.0
Previous
Game
Next
BitmapText
Inherited Members
Public Members
anticlockwise
endAngle
iterations
radius
startAngle
Inherited Methods
Public Methods
setEndAngle
setIterations
setRadius
setStartAngle
