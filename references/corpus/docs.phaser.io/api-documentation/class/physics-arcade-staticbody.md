# StaticBody | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-arcade-staticbody

Phaser API Documentation
Class
StaticBody
Version: Phaser v3.90.0
On this page
StaticBody
A Static Arcade Physics Body.
A Static Body never moves, and isn't automatically synchronized with its parent Game Object.
That means if you make any change to the parent's origin, position, or scale after creating or adding the body, you'll need to update the Static Body manually.
A Static Body can collide with other Bodies, but is never moved by collisions.
Its dynamic counterpart is Phaser.Physics.Arcade.Body .
Constructor
new StaticBody(world, [gameObject])
Parameters
name type optional description
world Phaser.Physics.Arcade.World No The Arcade Physics simulation this Static Body belongs to.
gameObject Phaser.GameObjects.GameObject Yes The Game Object this Body belongs to. As of Phaser 3.60 this is now optional.
Scope : static
Extends
Phaser.Physics.Arcade.Components.Collision
Source: src/physics/arcade/StaticBody.js#L15
Since: 3.0.0
Public Members ​
allowGravity ​
allowGravity: boolean ​
Description:
A constant false value expected by the Arcade Physics simulation.
Source: src/physics/arcade/StaticBody.js#L233
Since: 3.0.0
blocked ​
blocked: Phaser.Types.Physics.Arcade.ArcadeBodyCollision ​
Description:
This property is kept for compatibility with Dynamic Bodies.
Avoid using it.
Source: src/physics/arcade/StaticBody.js#L439
Since: 3.0.0
bottom ​
bottom: number ​
Description:
The lowest y coordinate of the area of the StaticBody. (y + height)
Source: src/physics/arcade/StaticBody.js#L1091
Since: 3.0.0
bounce ​
bounce: Phaser.Math.Vector2 ​
Description:
Rebound, or restitution, following a collision, relative to 1. Always zero for a Static Body.
Source: src/physics/arcade/StaticBody.js#L254
Since: 3.0.0
center ​
center: Phaser.Math.Vector2 ​
Description:
The center of the Static Body's boundary.
This is the midpoint of its position (top-left corner) and its bottom-right corner.
Source: src/physics/arcade/StaticBody.js#L213
Since: 3.0.0
checkCollision ​
checkCollision: Phaser.Types.Physics.Arcade.ArcadeBodyCollision ​
Description:
Whether this StaticBody is checked for collisions and for which directions. You can set checkCollision.none = false to disable collision checks.
Source: src/physics/arcade/StaticBody.js#L409
Since: 3.0.0
collideWorldBounds ​
collideWorldBounds: boolean ​
Description:
Whether this StaticBody interacts with the world boundary.
Always false for a Static Body. (Static Bodies never collide with the world boundary.)
Source: src/physics/arcade/StaticBody.js#L397
Since: 3.0.0
collisionCategory ​
collisionCategory: number ​
Description:
The Arcade Physics Body Collision Category.
This can be set to any valid collision bitfield value.
See the setCollisionCategory method for more details.
Source: src/physics/arcade/StaticBody.js#L459
Since: 3.70.0
collisionMask ​
collisionMask: number ​
Description:
The Arcade Physics Body Collision Mask.
See the setCollidesWith method for more details.
Source: src/physics/arcade/StaticBody.js#L472
Since: 3.70.0
customSeparateX ​
customSeparateX: boolean ​
Description:
A flag disabling the default horizontal separation of colliding bodies. Pass your own collideHandler to the collider.
Source: src/physics/arcade/StaticBody.js#L337
Since: 3.0.0
customSeparateY ​
customSeparateY: boolean ​
Description:
A flag disabling the default vertical separation of colliding bodies. Pass your own collideHandler to the collider.
Source: src/physics/arcade/StaticBody.js#L347
Since: 3.0.0
debugBodyColor ​
debugBodyColor: number ​
Description:
The color of this Static Body on the debug display.
Source: src/physics/arcade/StaticBody.js#L112
Since: 3.0.0
debugShowBody ​
debugShowBody: boolean ​
Description:
Whether the Static Body's boundary is drawn to the debug display.
Source: src/physics/arcade/StaticBody.js#L103
Since: 3.0.0
embedded ​
embedded: boolean ​
Description:
Whether this StaticBody has ever overlapped with another while both were not moving.
Source: src/physics/arcade/StaticBody.js#L387
Since: 3.0.0
enable ​
enable: boolean ​
Description:
Whether this Static Body is updated by the physics simulation.
Source: src/physics/arcade/StaticBody.js#L121
Since: 3.0.0
gameObject ​
gameObject: Phaser.GameObjects.GameObject ​
Description:
The Game Object this Static Body belongs to.
As of Phaser 3.60 this is now optional and can be undefined.
Source: src/physics/arcade/StaticBody.js#L82
Since: 3.0.0
gravity ​
gravity: Phaser.Math.Vector2 ​
Description:
Gravitational force applied specifically to this Body. Values are in pixels per second squared. Always zero for a Static Body.
Source: src/physics/arcade/StaticBody.js#L244
Since: 3.0.0
halfHeight ​
halfHeight: number ​
Description:
Half the Static Body's height, in pixels.
If the Static Body is circular, this is also the Static Body's radius.
Source: src/physics/arcade/StaticBody.js#L203
Since: 3.0.0
halfWidth ​
halfWidth: number ​
Description:
Half the Static Body's width, in pixels.
If the Static Body is circular, this is also the Static Body's radius.
Source: src/physics/arcade/StaticBody.js#L193
Since: 3.0.0
height ​
height: number ​
Description:
The height of the Static Body's boundary, in pixels.
If the Static Body is circular, this is also the Static Body's diameter.
Source: src/physics/arcade/StaticBody.js#L183
Since: 3.0.0
immovable ​
immovable: boolean ​
Description:
Whether this object can be moved by collisions with another body.
Source: src/physics/arcade/StaticBody.js#L308
Since: 3.0.0
isBody ​
isBody: boolean ​
Description:
A quick-test flag that signifies this is a Body, used in the World collision handler.
Source: src/physics/arcade/StaticBody.js#L93
Since: 3.60.0
isCircle ​
isCircle: boolean ​
Description:
Whether this Static Body's boundary is circular ( true ) or rectangular ( false ).
Source: src/physics/arcade/StaticBody.js#L131
Since: 3.0.0
left ​
left: number ​
Description:
Returns the left-most x coordinate of the area of the StaticBody.
Source: src/physics/arcade/StaticBody.js#L1040
Since: 3.0.0
mass ​
mass: number ​
Description:
The StaticBody's inertia, relative to a default unit (1). With bounce , this affects the exchange of momentum (velocities) during collisions.
Source: src/physics/arcade/StaticBody.js#L298
Since: 3.0.0
offset ​
offset: Phaser.Math.Vector2 ​
Description:
The offset set by Phaser.Physics.Arcade.StaticBody#setCircle or Phaser.Physics.Arcade.StaticBody#setSize .
This doesn't affect the Static Body's position, because a Static Body does not follow its Game Object.
Source: src/physics/arcade/StaticBody.js#L152
Since: 3.0.0
onCollide ​
onCollide: boolean ​
Description:
Whether the simulation emits a collide event when this StaticBody collides with another.
Source: src/physics/arcade/StaticBody.js#L278
Since: 3.0.0
onOverlap ​
onOverlap: boolean ​
Description:
Whether the simulation emits an overlap event when this StaticBody overlaps with another.
Source: src/physics/arcade/StaticBody.js#L288
Since: 3.0.0
onWorldBounds ​
onWorldBounds: boolean ​
Description:
Whether the simulation emits a worldbounds event when this StaticBody collides with the world boundary.
Always false for a Static Body. (Static Bodies never collide with the world boundary and never trigger a worldbounds event.)
Source: src/physics/arcade/StaticBody.js#L266
Since: 3.0.0
overlapR ​
overlapR: number ​
Description:
The amount of overlap (before separation), if this StaticBody is circular and colliding with another circular body.
Source: src/physics/arcade/StaticBody.js#L377
Since: 3.0.0
overlapX ​
overlapX: number ​
Description:
The amount of horizontal overlap (before separation), if this Body is colliding with another.
Source: src/physics/arcade/StaticBody.js#L357
Since: 3.0.0
overlapY ​
overlapY: number ​
Description:
The amount of vertical overlap (before separation), if this Body is colliding with another.
Source: src/physics/arcade/StaticBody.js#L367
Since: 3.0.0
physicsType ​
physicsType: number ​
Description:
The StaticBody's physics type (static by default).
Source: src/physics/arcade/StaticBody.js#L449
Since: 3.0.0
position ​
position: Phaser.Math.Vector2 ​
Description:
The position of this Static Body within the simulation.
Source: src/physics/arcade/StaticBody.js#L164
Since: 3.0.0
pushable ​
pushable: boolean ​
Description:
Sets if this Body can be pushed by another Body.
A body that cannot be pushed will reflect back all of the velocity it is given to the
colliding body. If that body is also not pushable, then the separation will be split
between them evenly.
If you want your body to never move or seperate at all, see the setImmovable method.
By default, Static Bodies are not pushable.
Source: src/physics/arcade/StaticBody.js#L318
Since: 3.50.0
radius ​
radius: number ​
Description:
If this Static Body is circular, this is the radius of the boundary, as set by Phaser.Physics.Arcade.StaticBody#setCircle , in pixels.
Equal to halfWidth .
Source: src/physics/arcade/StaticBody.js#L141
Since: 3.0.0
right ​
right: number ​
Description:
The right-most x coordinate of the area of the StaticBody.
Source: src/physics/arcade/StaticBody.js#L1057
Since: 3.0.0
top ​
top: number ​
Description:
The highest y coordinate of the area of the StaticBody.
Source: src/physics/arcade/StaticBody.js#L1074
Since: 3.0.0
touching ​
touching: Phaser.Types.Physics.Arcade.ArcadeBodyCollision ​
Description:
This property is kept for compatibility with Dynamic Bodies.
Avoid using it.
Source: src/physics/arcade/StaticBody.js#L418
Since: 3.0.0
velocity ​
velocity: Phaser.Math.Vector2 ​
Description:
A constant zero velocity used by the Arcade Physics simulation for calculations.
Source: src/physics/arcade/StaticBody.js#L223
Since: 3.0.0
wasTouching ​
wasTouching: Phaser.Types.Physics.Arcade.ArcadeBodyCollision ​
Description:
This property is kept for compatibility with Dynamic Bodies.
Avoid using it.
The values are always false for a Static Body.
Source: src/physics/arcade/StaticBody.js#L428
Since: 3.0.0
width ​
width: number ​
Description:
The width of the Static Body's boundary, in pixels.
If the Static Body is circular, this is also the Static Body's diameter.
Source: src/physics/arcade/StaticBody.js#L173
Since: 3.0.0
world ​
world: Phaser.Physics.Arcade.World ​
Description:
The Arcade Physics simulation this Static Body belongs to.
Source: src/physics/arcade/StaticBody.js#L73
Since: 3.0.0
x ​
x: number ​
Description:
The x coordinate of the StaticBody.
Source: src/physics/arcade/StaticBody.js#L990
Since: 3.0.0
y ​
y: number ​
Description:
The y coordinate of the StaticBody.
Source: src/physics/arcade/StaticBody.js#L1015
Since: 3.0.0
Inherited Methods ​
From Phaser.Physics.Arcade.Components.Collision :
addCollidesWith
removeCollidesWith
resetCollisionCategory
setCollidesWith
setCollisionCategory
willCollideWith
Public Methods ​
deltaAbsX ​
<instance> deltaAbsX() ​
Description:
The absolute (non-negative) change in this StaticBody's horizontal position from the previous step. Always zero.
Returns: number - Always zero for a Static Body.
Source: src/physics/arcade/StaticBody.js#L845
Since: 3.0.0
deltaAbsY ​
<instance> deltaAbsY() ​
Description:
The absolute (non-negative) change in this StaticBody's vertical position from the previous step. Always zero.
Returns: number - Always zero for a Static Body.
Source: src/physics/arcade/StaticBody.js#L858
Since: 3.0.0
deltaX ​
<instance> deltaX() ​
Description:
The change in this StaticBody's horizontal position from the previous step. Always zero.
Returns: number - The change in this StaticBody's velocity from the previous step. Always zero.
Source: src/physics/arcade/StaticBody.js#L871
Since: 3.0.0
deltaY ​
<instance> deltaY() ​
Description:
The change in this StaticBody's vertical position from the previous step. Always zero.
Returns: number - The change in this StaticBody's velocity from the previous step. Always zero.
Source: src/physics/arcade/StaticBody.js#L884
Since: 3.0.0
deltaZ ​
<instance> deltaZ() ​
Description:
The change in this StaticBody's rotation from the previous step. Always zero.
Returns: number - The change in this StaticBody's rotation from the previous step. Always zero.
Source: src/physics/arcade/StaticBody.js#L897
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Disables this Body and marks it for destruction during the next step.
Source: src/physics/arcade/StaticBody.js#L910
Since: 3.0.0
drawDebug ​
<instance> drawDebug(graphic) ​
Description:
Draws a graphical representation of the StaticBody for visual debugging purposes.
Parameters:
name type optional description
graphic Phaser.GameObjects.Graphics No The Graphics object to use for the debug drawing of the StaticBody.
Source: src/physics/arcade/StaticBody.js#L923
Since: 3.0.0
getBounds ​
<instance> getBounds(obj) ​
Description:
Returns the x and y coordinates of the top left and bottom right points of the StaticBody.
Parameters:
name type optional description
obj Phaser.Types.Physics.Arcade.ArcadeBodyBounds No The object which will hold the coordinates of the bounds.
Returns: Phaser.Types.Physics.Arcade.ArcadeBodyBounds - The same object that was passed with x , y , right and bottom values matching the respective values of the StaticBody.
Source: src/physics/arcade/StaticBody.js#L799
Since: 3.0.0
hitTest ​
<instance> hitTest(x, y) ​
Description:
Checks to see if a given x,y coordinate is colliding with this Static Body.
Parameters:
name type optional description
x number No The x coordinate to check against this body.
y number No The y coordinate to check against this body.
Returns: boolean - true if the given coordinate lies within this body, otherwise false .
Source: src/physics/arcade/StaticBody.js#L819
Since: 3.0.0
postUpdate ​
<instance> postUpdate() ​
Description:
NOOP
Source: src/physics/arcade/StaticBody.js#L835
Since: 3.12.0
reset ​
<instance> reset([x], [y]) ​
Description:
Resets this Static Body to its parent Game Object's position.
If x and y are given, the parent Game Object is placed there and this Static Body is centered on it.
Otherwise this Static Body is centered on the Game Object's current position.
Parameters:
name type optional description
x number Yes The x coordinate to reset the body to. If not given will use the parent Game Object's coordinate.
y number Yes The y coordinate to reset the body to. If not given will use the parent Game Object's coordinate.
Source: src/physics/arcade/StaticBody.js#L753
Since: 3.0.0
setCircle ​
<instance> setCircle(radius, [offsetX], [offsetY]) ​
Description:
Sets this Static Body to have a circular body and sets its size and position.
Parameters:
name type optional description
radius number No The radius of the StaticBody, in pixels.
offsetX number Yes The horizontal offset of the StaticBody from its Game Object, in pixels.
offsetY number Yes The vertical offset of the StaticBody from its Game Object, in pixels.
Returns: Phaser.Physics.Arcade.StaticBody - This Static Body object.
Source: src/physics/arcade/StaticBody.js#L697
Since: 3.0.0
setGameObject ​
<instance> setGameObject(gameObject, [update], [enable]) ​
Description:
Changes the Game Object this Body is bound to.
First it removes its reference from the old Game Object, then sets the new one.
This body will be resized to match the frame dimensions of the given Game Object, if it has a texture frame.
You can optionally update the position and dimensions of this Body to reflect that of the new Game Object.
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No The Game Object to assign this Body to.
update boolean Yes true Reposition and resize this Body to match the new Game Object?
enable boolean Yes true Automatically enable this Body for physics.
Returns: Phaser.Physics.Arcade.StaticBody - This Static Body object.
Source: src/physics/arcade/StaticBody.js#L508
Since: 3.1.0
setMass ​
<instance> setMass(value) ​
Description:
Sets the Mass of the StaticBody. Will set the Mass to 0.1 if the value passed is less than or equal to zero.
Parameters:
name type optional description
value number No The value to set the Mass to. Values of zero or less are changed to 0.1.
Returns: Phaser.Physics.Arcade.StaticBody - This Static Body object.
Source: src/physics/arcade/StaticBody.js#L967
Since: 3.0.0
setOffset ​
<instance> setOffset(x, y) ​
Description:
Positions the Static Body at an offset from its Game Object.
Parameters:
name type optional description
x number No The horizontal offset of the Static Body from the Game Object's x .
y number No The vertical offset of the Static Body from the Game Object's y .
Returns: Phaser.Physics.Arcade.StaticBody - This Static Body object.
Source: src/physics/arcade/StaticBody.js#L600
Since: 3.4.0
setSize ​
<instance> setSize([width], [height], [center]) ​
Description:
Sets the size of the Static Body.
When center is true, also repositions it.
Resets the width and height to match current frame, if no width and height provided and a frame is found.
Parameters:
name type optional default description
width number Yes The width of the Static Body in pixels. Cannot be zero. If not given, and the parent Game Object has a frame, it will use the frame width.
height number Yes The height of the Static Body in pixels. Cannot be zero. If not given, and the parent Game Object has a frame, it will use the frame height.
center boolean Yes true Place the Static Body's center on its Game Object's center. Only works if the Game Object has the getCenter method.
Returns: Phaser.Physics.Arcade.StaticBody - This Static Body object.
Source: src/physics/arcade/StaticBody.js#L632
Since: 3.0.0
stop ​
<instance> stop() ​
Description:
NOOP function. A Static Body cannot be stopped.
Returns: Phaser.Physics.Arcade.StaticBody - This Static Body object.
Source: src/physics/arcade/StaticBody.js#L786
Since: 3.0.0
updateCenter ​
<instance> updateCenter() ​
Description:
Updates the StaticBody's center from its position and dimensions.
Source: src/physics/arcade/StaticBody.js#L742
Since: 3.0.0
updateFromGameObject ​
<instance> updateFromGameObject() ​
Description:
Syncs the Static Body's position and size with its parent Game Object.
Returns: Phaser.Physics.Arcade.StaticBody - This Static Body object.
Source: src/physics/arcade/StaticBody.js#L571
Since: 3.1.0
willDrawDebug ​
<instance> willDrawDebug() ​
Description:
Indicates whether the StaticBody is going to be showing a debug visualization during postUpdate.
Returns: boolean - Whether or not the StaticBody is going to show the debug visualization during postUpdate.
Source: src/physics/arcade/StaticBody.js#L954
Since: 3.0.0
Previous
Sprite
Next
StaticGroup
Public Members
allowGravity
blocked
bottom
bounce
center
checkCollision
collideWorldBounds
collisionCategory
collisionMask
customSeparateX
customSeparateY
debugBodyColor
debugShowBody
embedded
enable
gameObject
gravity
halfHeight
halfWidth
height
immovable
isBody
isCircle
left
mass
offset
onCollide
onOverlap
onWorldBounds
overlapR
overlapX
overlapY
physicsType
position
pushable
radius
right
top
touching
velocity
wasTouching
width
world
x
y
Inherited Methods
Public Methods
deltaAbsX
deltaAbsY
deltaX
deltaY
deltaZ
destroy
drawDebug
getBounds
hitTest
postUpdate
reset
setCircle
setGameObject
setMass
setOffset
setSize
stop
updateCenter
updateFromGameObject
willDrawDebug
