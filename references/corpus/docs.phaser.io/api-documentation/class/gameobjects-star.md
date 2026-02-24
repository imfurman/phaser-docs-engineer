# Star | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-star

Phaser API Documentation
Class
Star
Version: Phaser v3.90.0
On this page
Star
The Star Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports both fill and stroke colors.
As the name implies, the Star shape will display a star in your game. You can control several
aspects of it including the number of points that constitute the star. The default is 5. If
you change it to 4 it will render as a diamond. If you increase them, you'll get a more spiky
star shape.
You can also control the inner and outer radius, which is how 'long' each point of the star is.
Modify these values to create more interesting shapes.
Constructor
new Star(scene, [x], [y], [points], [innerRadius], [outerRadius], [fillColor], [fillAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
points number Yes 5 The number of points on the star.
innerRadius number Yes 32 The inner radius of the star.
outerRadius number Yes 64 The outer radius of the star.
fillColor number Yes The color the star will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes The alpha the star will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/star/Star.js#L12
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
innerRadius ​
innerRadius: number ​
Description:
The inner radius of the Star shape.
Source: src/gameobjects/shape/star/Star.js#L187
Since: 3.13.0
outerRadius ​
outerRadius: number ​
Description:
The outer radius of the Star shape.
Source: src/gameobjects/shape/star/Star.js#L211
Since: 3.13.0
points ​
points: number ​
Description:
The number of points that make up the Star shape.
Source: src/gameobjects/shape/star/Star.js#L163
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
setInnerRadius ​
<instance> setInnerRadius(value) ​
Description:
Sets the inner radius of the Star shape.
This call can be chained.
Parameters:
name type optional description
value number No The amount to set the inner radius to.
Returns: Phaser.GameObjects.Star - This Game Object instance.
Source: src/gameobjects/shape/star/Star.js#L127
Since: 3.13.0
setOuterRadius ​
<instance> setOuterRadius(value) ​
Description:
Sets the outer radius of the Star shape.
This call can be chained.
Parameters:
name type optional description
value number No The amount to set the outer radius to.
Returns: Phaser.GameObjects.Star - This Game Object instance.
Source: src/gameobjects/shape/star/Star.js#L145
Since: 3.13.0
setPoints ​
<instance> setPoints(value) ​
Description:
Sets the number of points that make up the Star shape.
This call can be chained.
Parameters:
name type optional description
value number No The amount of points the Star will have.
Returns: Phaser.GameObjects.Star - This Game Object instance.
Source: src/gameobjects/shape/star/Star.js#L109
Since: 3.13.0
Previous
Sprite
Next
Text
Inherited Members
Public Members
innerRadius
outerRadius
points
Inherited Methods
Public Methods
setInnerRadius
setOuterRadius
setPoints
