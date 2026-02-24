# Rectangle | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-rectangle

Phaser API Documentation
Class
Rectangle
Version: Phaser v3.90.0
On this page
Rectangle
The Rectangle Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports both fill and stroke colors.
You can change the size of the rectangle by changing the width and height properties.
Constructor
new Rectangle(scene, x, y, [width], [height], [fillColor], [fillAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
width number Yes 128 The width of the rectangle.
height number Yes 128 The height of the rectangle.
fillColor number Yes The color the rectangle will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes The alpha the rectangle will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/rectangle/Rectangle.js#L13
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
setRounded ​
<instance> setRounded([radius]) ​
Description:
Sets this rectangle to have rounded corners by specifying the radius of the corner.
The radius of the rounded corners is limited by the smallest dimension of the rectangle.
To disable rounded corners, set the radius parameter to 0.
Parameters:
name type optional default description
radius number Yes 16 The radius of all four rounded corners.
Returns: Phaser.GameObjects.Rectangle - This Game Object instance.
Source: src/gameobjects/shape/rectangle/Rectangle.js#L95
Since: 3.90.0
setSize ​
<instance> setSize(width, height) ​
Description:
Sets the internal size of this Rectangle, as used for frame or physics body creation.
If you have assigned a custom input hit area for this Rectangle, changing the Rectangle size will not change the
size of the hit area. To do this you should adjust the input.hitArea object directly.
Parameters:
name type optional description
width number No The width of this Game Object.
height number No The height of this Game Object.
Overrides: Phaser.GameObjects.Shape#setSize
Returns: Phaser.GameObjects.Rectangle - This Game Object instance.
Source: src/gameobjects/shape/rectangle/Rectangle.js#L119
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
Polygon
Next
RenderTexture
Inherited Methods
Public Methods
setRounded
setSize
Inherited Members
