# Polygon | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-polygon

Phaser API Documentation
Class
Polygon
Version: Phaser v3.90.0
On this page
Polygon
The Polygon Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports both fill and stroke colors.
The Polygon Shape is created by providing a list of points, which are then used to create an
internal Polygon geometry object. The points can be set from a variety of formats:
A string containing paired values separated by a single space: '40 0 40 20 100 20 100 80 40 80 40 100 0 50'
An array of Point or Vector2 objects: [new Phaser.Math.Vector2(x1, y1), ...]
An array of objects with public x/y properties: [obj1, obj2, ...]
An array of paired numbers that represent point coordinates: [x1,y1, x2,y2, ...]
An array of arrays with two elements representing x/y coordinates: [[x1, y1], [x2, y2], ...]
By default the x and y coordinates of this Shape refer to the center of it. However, depending
on the coordinates of the points provided, the final shape may be rendered offset from its origin.
Note: The method getBounds will return incorrect bounds if any of the points in the Polygon are negative.
If this is the case, please use the function Phaser.Geom.Polygon.GetAABB(polygon.geom) instead and then
adjust the returned Rectangle position accordingly.
Constructor
new Polygon(scene, [x], [y], [points], [fillColor], [fillAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
points any Yes The points that make up the polygon.
fillColor number Yes The color the polygon will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes The alpha the polygon will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/polygon/Polygon.js#L15
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
<instance> setTo([points]) ​
Description:
Sets this Polygon to the given points.
The points can be set from a variety of formats:
A string containing paired values separated by a single space: '40 0 40 20 100 20 100 80 40 80 40 100 0 50'
An array of Point objects: [new Phaser.Point(x1, y1), ...]
An array of objects with public x/y properties: [obj1, obj2, ...]
An array of paired numbers that represent point coordinates: [x1,y1, x2,y2, ...]
An array of arrays with two elements representing x/y coordinates: [[x1, y1], [x2, y2], ...]
Calling this method will reset the size (width, height) and display origin of this Shape.
It also runs both GetAABB and EarCut on the given points, so please be careful not to do this
at a high frequency, or with too many points.
Parameters:
name type optional description
points string | Array.<number> Array.< Phaser.Types.Math.Vector2Like > Yes
Returns: Phaser.GameObjects.Polygon - This Game Object instance.
Source: src/gameobjects/shape/polygon/Polygon.js#L108
Since: 3.60.0
smooth ​
<instance> smooth([iterations]) ​
Description:
Smooths the polygon over the number of iterations specified.
The base polygon data will be updated and replaced with the smoothed values.
This call can be chained.
Parameters:
name type optional default description
iterations number Yes 1 The number of times to apply the polygon smoothing.
Returns: Phaser.GameObjects.Polygon - This Game Object instance.
Source: src/gameobjects/shape/polygon/Polygon.js#L84
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
PointLight
Next
Rectangle
Inherited Methods
Public Methods
setTo
smooth
Inherited Members
