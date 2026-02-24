# Ellipse | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-ellipse

Phaser API Documentation
Class
Ellipse
Version: Phaser v3.90.0
On this page
Ellipse
The Ellipse Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports both fill and stroke colors.
When it renders it displays an ellipse shape. You can control the width and height of the ellipse.
If the width and height match it will render as a circle. If the width is less than the height,
it will look more like an egg shape.
The Ellipse shape also has a smoothness property and corresponding setSmoothness method.
This allows you to control how smooth the shape renders in WebGL, by controlling the number of iterations
that take place during construction. Increase and decrease the default value for smoother, or more
jagged, shapes.
Constructor
new Ellipse(scene, [x], [y], [width], [height], [fillColor], [fillAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
width number Yes 128 The width of the ellipse. An ellipse with equal width and height renders as a circle.
height number Yes 128 The height of the ellipse. An ellipse with equal width and height renders as a circle.
fillColor number Yes The color the ellipse will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes The alpha the ellipse will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/ellipse/Ellipse.js#L13
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
smoothness ​
smoothness: number ​
Description:
The smoothness of the ellipse. The number of points used when rendering it.
Increase this value for a smoother ellipse, at the cost of more polygons being rendered.
Source: src/gameobjects/shape/ellipse/Ellipse.js#L89
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
setSize ​
<instance> setSize(width, height) ​
Description:
Sets the size of the ellipse by changing the underlying geometry data, rather than scaling the object.
This call can be chained.
Parameters:
name type optional description
width number No The width of the ellipse.
height number No The height of the ellipse.
Overrides: Phaser.GameObjects.Shape#setSize
Returns: Phaser.GameObjects.Ellipse - This Game Object instance.
Source: src/gameobjects/shape/ellipse/Ellipse.js#L114
Since: 3.13.0
setSmoothness ​
<instance> setSmoothness(value) ​
Description:
Sets the smoothness of the ellipse. The number of points used when rendering it.
Increase this value for a smoother ellipse, at the cost of more polygons being rendered.
This call can be chained.
Parameters:
name type optional description
value number No The value to set the smoothness to.
Returns: Phaser.GameObjects.Ellipse - This Game Object instance.
Source: src/gameobjects/shape/ellipse/Ellipse.js#L138
Since: 3.13.0
Previous
DynamicBitmapText
Next
Extern
Inherited Members
Public Members
smoothness
Inherited Methods
Public Methods
setSize
setSmoothness
