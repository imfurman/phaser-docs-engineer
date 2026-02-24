# Zone | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-zone

Phaser API Documentation
Class
Zone
Version: Phaser v3.90.0
On this page
Zone
A Zone Game Object.
A Zone is a non-rendering rectangular Game Object that has a position and size.
It has no texture and never displays, but does live on the display list and
can be moved, scaled and rotated like any other Game Object.
Its primary use is for creating Drop Zones and Input Hit Areas and it has a couple of helper methods
specifically for this. It is also useful for object overlap checks, or as a base for your own
non-displaying Game Objects.
The default origin is 0.5, the center of the Zone, the same as with Game Objects.
Constructor
new Zone(scene, x, y, [width], [height])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
width number Yes 1 The width of the Game Object.
height number Yes 1 The height of the Game Object.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/zone/Zone.js#L16
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
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
blendMode ​
blendMode: number ​
Description:
The Blend Mode of the Game Object.
Although a Zone never renders, it still has a blend mode to allow it to fit seamlessly into
display lists without causing a batch flush.
Source: src/gameobjects/zone/Zone.js#L91
Since: 3.0.0
displayHeight ​
displayHeight: number ​
Description:
The displayed height of this Game Object.
This value takes into account the scale factor.
Source: src/gameobjects/zone/Zone.js#L127
Since: 3.0.0
displayWidth ​
displayWidth: number ​
Description:
The displayed width of this Game Object.
This value takes into account the scale factor.
Source: src/gameobjects/zone/Zone.js#L105
Since: 3.0.0
height ​
height: number ​
Description:
The native (un-scaled) height of this Game Object.
Source: src/gameobjects/zone/Zone.js#L82
Since: 3.0.0
width ​
width: number ​
Description:
The native (un-scaled) width of this Game Object.
Source: src/gameobjects/zone/Zone.js#L73
Since: 3.0.0
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
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
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
setCircleDropZone ​
<instance> setCircleDropZone(radius) ​
Description:
Sets this Zone to be a Circular Drop Zone.
The circle is centered on this Zones x and y coordinates.
Parameters:
name type optional description
radius number No The radius of the Circle that will form the Drop Zone.
Returns: Phaser.GameObjects.Zone - This Game Object.
Source: src/gameobjects/zone/Zone.js#L201
Since: 3.0.0
setDisplaySize ​
<instance> setDisplaySize(width, height) ​
Description:
Sets the display size of this Game Object.
Calling this will adjust the scale.
Parameters:
name type optional description
width number No The width of this Game Object.
height number No The height of this Game Object.
Returns: Phaser.GameObjects.Zone - This Game Object.
Source: src/gameobjects/zone/Zone.js#L181
Since: 3.0.0
setDropZone ​
<instance> setDropZone([hitArea], [hitAreaCallback]) ​
Description:
Allows you to define your own Geometry shape to be used as a Drop Zone.
Parameters:
name type optional description
hitArea object Yes A Geometry shape instance, such as Phaser.Geom.Ellipse, or your own custom shape. If not given it will try to create a Rectangle based on the size of this zone.
hitAreaCallback Phaser.Types.Input.HitAreaCallback Yes A function that will return true if the given x/y coords it is sent are within the shape. If you provide a shape you must also provide a callback.
Returns: Phaser.GameObjects.Zone - This Game Object.
Source: src/gameobjects/zone/Zone.js#L234
Since: 3.0.0
setRectangleDropZone ​
<instance> setRectangleDropZone(width, height) ​
Description:
Sets this Zone to be a Rectangle Drop Zone.
The rectangle is centered on this Zones x and y coordinates.
Parameters:
name type optional description
width number No The width of the rectangle drop zone.
height number No The height of the rectangle drop zone.
Returns: Phaser.GameObjects.Zone - This Game Object.
Source: src/gameobjects/zone/Zone.js#L217
Since: 3.0.0
setSize ​
<instance> setSize(width, height, [resizeInput]) ​
Description:
Sets the size of this Game Object.
Parameters:
name type optional default description
width number No The width of this Game Object.
height number No The height of this Game Object.
resizeInput boolean Yes true If this Zone has a Rectangle for a hit area this argument will resize the hit area as well.
Returns: Phaser.GameObjects.Zone - This Game Object.
Source: src/gameobjects/zone/Zone.js#L149
Since: 3.0.0
Previous
Video
Next
Circle
Inherited Members
Public Members
blendMode
displayHeight
displayWidth
height
width
Inherited Methods
Public Methods
setCircleDropZone
setDisplaySize
setDropZone
setRectangleDropZone
setSize
