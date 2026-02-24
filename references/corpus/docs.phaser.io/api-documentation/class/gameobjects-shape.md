# Shape | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-shape

Phaser API Documentation
Class
Shape
Version: Phaser v3.90.0
On this page
Shape
The Shape Game Object is a base class for the various different shapes, such as the Arc, Star or Polygon.
You cannot add a Shape directly to your Scene, it is meant as a base for your own custom Shape classes.
Constructor
new Shape(scene, [type], [data])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
type string Yes The internal type of the Shape.
data any Yes The data of the source shape geometry, if any.
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
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/shape/Shape.js#L12
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
Public Methods ​
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/shape/Shape.js#L353
Since: 3.13.0
setClosePath ​
<instance> setClosePath(value) ​
Description:
Sets if this Shape path is closed during rendering when stroked.
Note that some Shapes are always closed when stroked (such as Ellipse shapes)
This call can be chained.
Parameters:
name type optional description
value boolean No Set to true if the Shape should be closed when stroked, otherwise false .
Returns: Phaser.GameObjects.Shape - This Game Object instance.
Source: src/gameobjects/shape/Shape.js#L284
Since: 3.13.0
setDisplaySize ​
<instance> setDisplaySize(width, height) ​
Description:
Sets the display size of this Shape.
Calling this will adjust the scale.
Parameters:
name type optional description
width number No The display width of this Shape.
height number No The display height of this Shape.
Returns: Phaser.GameObjects.Shape - This Shape instance.
Source: src/gameobjects/shape/Shape.js#L332
Since: 3.53.0
setFillStyle ​
<instance> setFillStyle([color], [alpha]) ​
Description:
Sets the fill color and alpha for this Shape.
If you wish for the Shape to not be filled then call this method with no arguments, or just set isFilled to false .
Note that some Shapes do not support fill colors, such as the Line shape.
This call can be chained.
Parameters:
name type optional default description
color number Yes The color used to fill this shape. If not provided the Shape will not be filled.
alpha number Yes 1 The alpha value used when filling this shape, if a fill color is given.
Returns: Phaser.GameObjects.Shape - This Game Object instance.
Source: src/gameobjects/shape/Shape.js#L212
Since: 3.13.0
setStrokeStyle ​
<instance> setStrokeStyle([lineWidth], [color], [alpha]) ​
Description:
Sets the stroke color and alpha for this Shape.
If you wish for the Shape to not be stroked then call this method with no arguments, or just set isStroked to false .
Note that some Shapes do not support being stroked, such as the Iso Box shape.
This call can be chained.
Parameters:
name type optional default description
lineWidth number Yes The width of line to stroke with. If not provided or undefined the Shape will not be stroked.
color number Yes The color used to stroke this shape. If not provided the Shape will not be stroked.
alpha number Yes 1 The alpha value used when stroking this shape, if a stroke color is given.
Returns: Phaser.GameObjects.Shape - This Game Object instance.
Source: src/gameobjects/shape/Shape.js#L247
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
Public Members ​
closePath ​
closePath: boolean ​
Description:
Controls if this Shape path is closed during rendering when stroked.
Note that some Shapes are always closed when stroked (such as Ellipse shapes)
Source: src/gameobjects/shape/Shape.js#L161
Since: 3.13.0
displayHeight ​
displayHeight: number ​
Description:
The displayed height of this Game Object.
This value takes into account the scale factor.
Setting this value will adjust the Game Object's scale property.
Source: src/gameobjects/shape/Shape.js#L393
Since: 3.13.0
displayWidth ​
displayWidth: number ​
Description:
The displayed width of this Game Object.
This value takes into account the scale factor.
Setting this value will adjust the Game Object's scale property.
Source: src/gameobjects/shape/Shape.js#L368
Since: 3.13.0
fillAlpha ​
fillAlpha: number ​
Description:
The fill alpha value used by this Shape.
Source: src/gameobjects/shape/Shape.js#L105
Since: 3.13.0
fillColor ​
fillColor: number ​
Description:
The fill color used by this Shape.
Source: src/gameobjects/shape/Shape.js#L96
Since: 3.13.0
geom ​
geom: any ​
Description:
The source Shape data. Typically a geometry object.
You should not manipulate this directly.
Source: src/gameobjects/shape/Shape.js#L65
Since: 3.13.0
height ​
height: number ​
Description:
The native (un-scaled) height of this Game Object.
Changing this value will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or use
the displayHeight property.
Source: src/gameobjects/shape/Shape.js#L195
Since: 3.0.0
isFilled ​
isFilled: boolean ​
Description:
Controls if this Shape is filled or not.
Note that some Shapes do not support being filled (such as Line shapes)
Source: src/gameobjects/shape/Shape.js#L141
Since: 3.13.0
isRounded ​
isRounded: boolean ​
Description:
Does this Rectangle have rounded corners?
Do not modify this property. Instead, call the method setRounded to set the
radius state of this rectangle.
Source: src/gameobjects/shape/rectangle/Rectangle.js#L70
Since: 3.90.0
isStroked ​
isStroked: boolean ​
Description:
Controls if this Shape is stroked or not.
Note that some Shapes do not support being stroked (such as Iso Box shapes)
Source: src/gameobjects/shape/Shape.js#L151
Since: 3.13.0
lineWidth ​
lineWidth: number ​
Description:
The stroke line width used by this Shape.
Source: src/gameobjects/shape/Shape.js#L132
Since: 3.13.0
pathData ​
pathData: Array.<number> ​
Description:
Holds the polygon path data for filled rendering.
Source: src/gameobjects/shape/Shape.js#L76
Since: 3.13.0
pathIndexes ​
pathIndexes: Array.<number> ​
Description:
Holds the earcut polygon path index data for filled rendering.
Source: src/gameobjects/shape/Shape.js#L86
Since: 3.13.0
radius ​
radius: number ​
Description:
The radius of the rectangle if this is set to use rounded corners.
Do not modify this property. Instead, call the method setRounded to set the
radius of the rounded corners.
Source: src/gameobjects/shape/rectangle/Rectangle.js#L57
Since: 3.90.0
strokeAlpha ​
strokeAlpha: number ​
Description:
The stroke alpha value used by this Shape.
Source: src/gameobjects/shape/Shape.js#L123
Since: 3.13.0
strokeColor ​
strokeColor: number ​
Description:
The stroke color used by this Shape.
Source: src/gameobjects/shape/Shape.js#L114
Since: 3.13.0
width ​
width: number ​
Description:
The native (un-scaled) width of this Game Object.
Changing this value will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or use
the displayWidth property.
Source: src/gameobjects/shape/Shape.js#L182
Since: 3.13.0
Previous
Shader
Next
Sprite
Inherited Methods
Public Methods
preDestroy
setClosePath
setDisplaySize
setFillStyle
setStrokeStyle
Inherited Members
Public Members
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
