# Phaser.Physics.Arcade | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade
Scope: static
Source: src/physics/arcade/index.js#L10
Static functions ​
ArcadePhysics
Body
Collider
Factory
Group
Image
Sprite
StaticBody
StaticGroup
World
Static functions ​
GetCollidesWith ​
<static> GetCollidesWith(categories) ​
Description:
Calculates and returns the bitmask needed to determine if the given
categories will collide with each other or not.
Parameters:
name type optional description
categories number | Array.<number> No A unique category bitfield, or an array of them.
Returns: number - The collision mask.
Source: src/physics/arcade/GetCollidesWith.js#L7
Since: 3.70.0
GetOverlapX ​
<static> GetOverlapX(body1, body2, overlapOnly, bias) ​
Description:
Calculates and returns the horizontal overlap between two arcade physics bodies and sets their properties
accordingly, including: touching.left , touching.right , touching.none and `overlapX'.
Parameters:
name type optional description
body1 Phaser.Physics.Arcade.Body No The first Body to separate.
body2 Phaser.Physics.Arcade.Body No The second Body to separate.
overlapOnly boolean No Is this an overlap only check, or part of separation?
bias number No A value added to the delta values during collision checks. Increase it to prevent sprite tunneling(sprites passing through another instead of colliding).
Returns: number - The amount of overlap.
Source: src/physics/arcade/GetOverlapX.js#L9
Since: 3.0.0
GetOverlapY ​
<static> GetOverlapY(body1, body2, overlapOnly, bias) ​
Description:
Calculates and returns the vertical overlap between two arcade physics bodies and sets their properties
accordingly, including: touching.up , touching.down , touching.none and `overlapY'.
Parameters:
name type optional description
body1 Phaser.Physics.Arcade.Body No The first Body to separate.
body2 Phaser.Physics.Arcade.Body No The second Body to separate.
overlapOnly boolean No Is this an overlap only check, or part of separation?
bias number No A value added to the delta values during collision checks. Increase it to prevent sprite tunneling(sprites passing through another instead of colliding).
Returns: number - The amount of overlap.
Source: src/physics/arcade/GetOverlapY.js#L9
Since: 3.0.0
SeparateX ​
<static> SeparateX(body1, body2, overlapOnly, bias, [overlap]) ​
Description:
Separates two overlapping bodies on the X-axis (horizontally).
Separation involves moving two overlapping bodies so they don't overlap anymore and adjusting their velocities based on their mass. This is a core part of collision detection.
The bodies won't be separated if there is no horizontal overlap between them, if they are static, or if either one uses custom logic for its separation.
Parameters:
name type optional description
body1 Phaser.Physics.Arcade.Body No The first Body to separate.
body2 Phaser.Physics.Arcade.Body No The second Body to separate.
overlapOnly boolean No If true , the bodies will only have their overlap data set and no separation will take place.
bias number No A value to add to the delta value during overlap checking. Used to prevent sprite tunneling.
overlap number Yes If given then this value will be used as the overlap and no check will be run.
Returns: boolean - true if the two bodies overlap vertically, otherwise false .
Source: src/physics/arcade/SeparateX.js#L10
Since: 3.0.0
SeparateY ​
<static> SeparateY(body1, body2, overlapOnly, bias, [overlap]) ​
Description:
Separates two overlapping bodies on the Y-axis (vertically).
Separation involves moving two overlapping bodies so they don't overlap anymore and adjusting their velocities based on their mass. This is a core part of collision detection.
The bodies won't be separated if there is no vertical overlap between them, if they are static, or if either one uses custom logic for its separation.
Parameters:
name type optional description
body1 Phaser.Physics.Arcade.Body No The first Body to separate.
body2 Phaser.Physics.Arcade.Body No The second Body to separate.
overlapOnly boolean No If true , the bodies will only have their overlap data set and no separation will take place.
bias number No A value to add to the delta value during overlap checking. Used to prevent sprite tunneling.
overlap number Yes If given then this value will be used as the overlap and no check will be run.
Returns: boolean - true if the two bodies overlap vertically, otherwise false .
Source: src/physics/arcade/SeparateY.js#L10
Since: 3.0.0
SetCollisionObject ​
<static> SetCollisionObject(noneFlip, [data]) ​
Description:
Either sets or creates the Arcade Body Collision object.
Mostly only used internally.
Parameters:
name type optional description
noneFlip boolean No Is none true or false?
data Phaser.Types.Physics.Arcade.ArcadeBodyCollision Yes The collision data object to populate, or create if not given.
Returns: Phaser.Types.Physics.Arcade.ArcadeBodyCollision - The collision data.
Source: src/physics/arcade/SetCollisionObject.js#L7
Since: 3.70.0
Static functions ​
Components
Events
ProcessX
ProcessY
Tilemap
Static functions ​
DYNAMIC_BODY ​
DYNAMIC_BODY: number ​
Description:
Dynamic Body.
Source: src/physics/arcade/const.js#L15
Since: 3.0.0
FACING_DOWN ​
FACING_DOWN: number ​
Description:
Facing down.
Source: src/physics/arcade/const.js#L85
Since: 3.0.0
FACING_LEFT ​
FACING_LEFT: number ​
Description:
Facing left.
Source: src/physics/arcade/const.js#L97
Since: 3.0.0
FACING_NONE ​
FACING_NONE: number ​
Description:
Facing no direction (initial value).
Source: src/physics/arcade/const.js#L61
Since: 3.0.0
FACING_RIGHT ​
FACING_RIGHT: number ​
Description:
Facing right.
Source: src/physics/arcade/const.js#L109
Since: 3.0.0
FACING_UP ​
FACING_UP: number ​
Description:
Facing up.
Source: src/physics/arcade/const.js#L73
Since: 3.0.0
GROUP ​
GROUP: number ​
Description:
Arcade Physics Group containing Dynamic Bodies.
Source: src/physics/arcade/const.js#L41
Since: 3.0.0
STATIC_BODY ​
STATIC_BODY: number ​
Description:
Static Body.
Source: src/physics/arcade/const.js#L28
Since: 3.0.0
TILEMAPLAYER ​
TILEMAPLAYER: number ​
Description:
A Tilemap Layer.
Source: src/physics/arcade/const.js#L51
Since: 3.0.0
Previous
Phaser.Physics.Arcade.Tilemap
Next
Phaser.Physics.Matter.Components.Bounce
Static functions
Static functions
GetCollidesWith
GetOverlapX
GetOverlapY
SeparateX
SeparateY
SetCollisionObject
Static functions
Static functions
DYNAMIC_BODY
FACING_DOWN
FACING_LEFT
FACING_NONE
FACING_RIGHT
FACING_UP
GROUP
STATIC_BODY
TILEMAPLAYER
