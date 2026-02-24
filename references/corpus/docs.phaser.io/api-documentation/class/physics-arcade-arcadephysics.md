# ArcadePhysics | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-arcade-arcadephysics

Phaser API Documentation
Class
ArcadePhysics
Version: Phaser v3.90.0
On this page
ArcadePhysics
The Arcade Physics Plugin belongs to a Scene and sets up and manages the Scene's physics simulation.
It also holds some useful methods for moving and rotating Arcade Physics Bodies.
You can access it from within a Scene using this.physics .
Arcade Physics uses the Projection Method of collision resolution and separation. While it's fast and suitable
for 'arcade' style games it lacks stability when multiple objects are in close proximity or resting upon each other.
The separation that stops two objects penetrating may create a new penetration against a different object. If you
require a high level of stability please consider using an alternative physics system, such as Matter.js.
Constructor
new ArcadePhysics(scene)
Parameters
name type optional description
scene Phaser.Scene No The Scene that this Plugin belongs to.
Scope : static
Source: src/physics/arcade/ArcadePhysics.js#L21
Since: 3.0.0
Public Members ​
add ​
add: Phaser.Physics.Arcade.Factory ​
Description:
An object holding the Arcade Physics factory methods.
Source: src/physics/arcade/ArcadePhysics.js#L82
Since: 3.0.0
config ​
config: Phaser.Types.Physics.Arcade.ArcadeWorldConfig ​
Description:
A configuration object. Union of the physics.arcade.* properties of the GameConfig and SceneConfig objects.
Source: src/physics/arcade/ArcadePhysics.js#L64
Since: 3.0.0
scene ​
scene: Phaser.Scene ​
Description:
The Scene that this Plugin belongs to.
Source: src/physics/arcade/ArcadePhysics.js#L46
Since: 3.0.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
The Scene's Systems.
Source: src/physics/arcade/ArcadePhysics.js#L55
Since: 3.0.0
world ​
world: Phaser.Physics.Arcade.World ​
Description:
The physics simulation.
Source: src/physics/arcade/ArcadePhysics.js#L73
Since: 3.0.0
Public Methods ​
accelerateTo ​
<instance> accelerateTo(gameObject, x, y, [speed], [xSpeedMax], [ySpeedMax]) ​
Description:
Sets the acceleration.x/y property on the game object so it will move towards the x/y coordinates at the given rate (in pixels per second squared)
You must give a maximum speed value, beyond which the game object won't go any faster.
Note: The game object does not continuously track the target. If the target changes location during transit the game object will not modify its course.
Note: The game object doesn't stop moving once it reaches the destination coordinates.
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No Any Game Object with an Arcade Physics body.
x number No The x coordinate to accelerate towards.
y number No The y coordinate to accelerate towards.
speed number Yes 60 The acceleration (change in speed) in pixels per second squared.
xSpeedMax number Yes 500 The maximum x velocity the game object can reach.
ySpeedMax number Yes 500 The maximum y velocity the game object can reach.
Returns: number - The angle (in radians) that the object should be visually set to in order to match its new velocity.
Source: src/physics/arcade/ArcadePhysics.js#L378
Since: 3.0.0
accelerateToObject ​
<instance> accelerateToObject(gameObject, destination, [speed], [xSpeedMax], [ySpeedMax]) ​
Description:
Sets the acceleration.x/y property on the game object so it will move towards the x/y coordinates at the given rate (in pixels per second squared)
You must give a maximum speed value, beyond which the game object won't go any faster.
Note: The game object does not continuously track the target. If the target changes location during transit the game object will not modify its course.
Note: The game object doesn't stop moving once it reaches the destination coordinates.
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No Any Game Object with an Arcade Physics body.
destination Phaser.GameObjects.GameObject No The Game Object to move towards. Can be any object but must have visible x/y properties.
speed number Yes 60 The acceleration (change in speed) in pixels per second squared.
xSpeedMax number Yes 500 The maximum x velocity the game object can reach.
ySpeedMax number Yes 500 The maximum y velocity the game object can reach.
Returns: number - The angle (in radians) that the object should be visually set to in order to match its new velocity.
Source: src/physics/arcade/ArcadePhysics.js#L414
Since: 3.0.0
closest ​
<instance> closest(source, [targets]) ​
Description:
Finds the Body or Game Object closest to a source point or object.
If a targets argument is passed, this method finds the closest of those.
The targets can be Arcade Physics Game Objects, Dynamic Bodies, or Static Bodies.
If no targets argument is passed, this method finds the closest Dynamic Body.
If two or more targets are the exact same distance from the source point, only the first target
is returned.
Tags:
generic
Parameters:
name type optional description
source Phaser.Types.Math.Vector2Like No Any object with public x and y properties, such as a Game Object or Geometry object.
targets Array.<Target> Yes The targets.
Returns: Target, null - The target closest to the given source point.
Source: src/physics/arcade/ArcadePhysics.js#L438
Since: 3.0.0
collide ​
<instance> collide(object1, [object2], [collideCallback], [processCallback], [callbackContext]) ​
Description:
Performs a collision check and separation between the two physics enabled objects given, which can be single
Game Objects, arrays of Game Objects, Physics Groups, arrays of Physics Groups or normal Groups.
If you don't require separation then use #overlap instead.
If two Groups or arrays are passed, each member of one will be tested against each member of the other.
If only one Group is passed (as object1 ), each member of the Group will be collided against the other members.
If only one Array is passed, the array is iterated and every element in it is tested against the others.
Two callbacks can be provided. The collideCallback is invoked if a collision occurs and the two colliding
objects are passed to it.
Arcade Physics uses the Projection Method of collision resolution and separation. While it's fast and suitable
for 'arcade' style games it lacks stability when multiple objects are in close proximity or resting upon each other.
The separation that stops two objects penetrating may create a new penetration against a different object. If you
require a high level of stability please consider using an alternative physics system, such as Matter.js.
Parameters:
name type optional description
object1 Phaser.Types.Physics.Arcade.ArcadeColliderType No The first object or array of objects to check.
object2 Phaser.Types.Physics.Arcade.ArcadeColliderType Yes The second object or array of objects to check, or undefined .
collideCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects collide.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then collideCallback will only be called if this callback returns true .
callbackContext * Yes The context in which to run the callbacks.
Returns: boolean - True if any overlapping Game Objects were separated, otherwise false.
Source: src/physics/arcade/ArcadePhysics.js#L249
Since: 3.0.0
collideTiles ​
<instance> collideTiles(sprite, tiles, [collideCallback], [processCallback], [callbackContext]) ​
Description:
This advanced method is specifically for testing for collision between a single Sprite and an array of Tile objects.
You should generally use the collide method instead, with a Sprite vs. a Tilemap Layer, as that will perform
tile filtering and culling for you, as well as handle the interesting face collision automatically.
This method is offered for those who would like to check for collision with specific Tiles in a layer, without
having to set any collision attributes on the tiles in question. This allows you to perform quick dynamic collisions
on small sets of Tiles. As such, no culling or checks are made to the array of Tiles given to this method,
you should filter them before passing them to this method.
Important: Use of this method skips the interesting faces system that Tilemap Layers use. This means if you have
say a row or column of tiles, and you jump into, or walk over them, it's possible to get stuck on the edges of the
tiles as the interesting face calculations are skipped. However, for quick-fire small collision set tests on
dynamic maps, this method can prove very useful.
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No The first object to check for collision.
tiles Array.< Phaser.Tilemaps.Tile > No An array of Tiles to check for collision against.
collideCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects collide.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then collideCallback will only be called if this callback returns true .
callbackContext any Yes The context in which to run the callbacks.
Returns: boolean - True if any objects overlap (with overlapOnly ); or true if any overlapping objects were separated.
Fires: Phaser.Physics.Arcade.Events#event:TILE_COLLIDE
Source: src/physics/arcade/ArcadePhysics.js#L291
Since: 3.17.0
destroy ​
<instance> destroy() ​
Description:
The Scene that owns this plugin is being destroyed.
We need to shutdown and then kill off all external references.
Source: src/physics/arcade/ArcadePhysics.js#L732
Since: 3.0.0
disableUpdate ​
<instance> disableUpdate() ​
Description:
Causes World.update to not be automatically called each time the Scene
emits and UPDATE event.
If you wish to run the World update at your own rate, or from your own
component, then you should call this method to disable the built-in link,
and then call World.update(time, delta) accordingly.
Note that World.postUpdate is always automatically called when the Scene
emits a POST_UPDATE event, regardless of this setting.
Source: src/physics/arcade/ArcadePhysics.js#L162
Since: 3.50.0
enableUpdate ​
<instance> enableUpdate() ​
Description:
Causes World.update to be automatically called each time the Scene
emits and UPDATE event. This is the default setting, so only needs
calling if you have specifically disabled it.
Source: src/physics/arcade/ArcadePhysics.js#L149
Since: 3.50.0
furthest ​
<instance> furthest(source, [targets]) ​
Description:
Finds the Body or Game Object farthest from a source point or object.
If a targets argument is passed, this method finds the farthest of those.
The targets can be Arcade Physics Game Objects, Dynamic Bodies, or Static Bodies.
If no targets argument is passed, this method finds the farthest Dynamic Body.
If two or more targets are the exact same distance from the source point, only the first target
is returned.
Parameters:
name type optional description
source any No Any object with public x and y properties, such as a Game Object or Geometry object.
targets Array.< Phaser.Physics.Arcade.Body > | Array.< Phaser.Physics.Arcade.StaticBody > Array.< Phaser.GameObjects.GameObject > Yes
Returns: Phaser.Physics.Arcade.Body , Phaser.Physics.Arcade.StaticBody , Phaser.GameObjects.GameObject - The target farthest from the given source point.
Source: src/physics/arcade/ArcadePhysics.js#L493
Since: 3.0.0
getConfig ​
<instance> getConfig() ​
Description:
Creates the physics configuration for the current Scene.
Returns: Phaser.Types.Physics.Arcade.ArcadeWorldConfig - The physics configuration.
Source: src/physics/arcade/ArcadePhysics.js#L181
Since: 3.0.0
moveTo ​
<instance> moveTo(gameObject, x, y, [speed], [maxTime]) ​
Description:
Move the given display object towards the x/y coordinates at a steady velocity.
If you specify a maxTime then it will adjust the speed (over-writing what you set) so it arrives at the destination in that number of seconds.
Timings are approximate due to the way browser timers work. Allow for a variance of +- 50ms.
Note: The display object does not continuously track the target. If the target changes location during transit the display object will not modify its course.
Note: The display object doesn't stop moving once it reaches the destination coordinates.
Note: Doesn't take into account acceleration, maxVelocity or drag (if you've set drag or acceleration too high this object may not move at all)
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No Any Game Object with an Arcade Physics body.
x number No The x coordinate to move towards.
y number No The y coordinate to move towards.
speed number Yes 60 The speed it will move, in pixels per second (default is 60 pixels/sec)
maxTime number Yes 0 Time given in milliseconds (1000 = 1 sec). If set the speed is adjusted so the object will arrive at destination in the given number of ms.
Returns: number - The angle (in radians) that the object should be visually set to in order to match its new velocity.
Source: src/physics/arcade/ArcadePhysics.js#L548
Since: 3.0.0
moveToObject ​
<instance> moveToObject(gameObject, destination, [speed], [maxTime]) ​
Description:
Move the given display object towards the destination object at a steady velocity.
If you specify a maxTime then it will adjust the speed (overwriting what you set) so it arrives at the destination in that number of seconds.
Timings are approximate due to the way browser timers work. Allow for a variance of +- 50ms.
Note: The display object does not continuously track the target. If the target changes location during transit the display object will not modify its course.
Note: The display object doesn't stop moving once it reaches the destination coordinates.
Note: Doesn't take into account acceleration, maxVelocity or drag (if you've set drag or acceleration too high this object may not move at all)
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No Any Game Object with an Arcade Physics body.
destination object No Any object with public x and y properties, such as a Game Object or Geometry object.
speed number Yes 60 The speed it will move, in pixels per second (default is 60 pixels/sec)
maxTime number Yes 0 Time given in milliseconds (1000 = 1 sec). If set the speed is adjusted so the object will arrive at destination in the given number of ms.
Returns: number - The angle (in radians) that the object should be visually set to in order to match its new velocity.
Source: src/physics/arcade/ArcadePhysics.js#L585
Since: 3.0.0
nextCategory ​
<instance> nextCategory() ​
Description:
Returns the next available collision category.
You can have a maximum of 32 categories.
By default all bodies collide with all other bodies.
Use the Body.setCollisionCategory() and
Body.setCollidesWith() methods to change this.
Returns: number - The next collision category.
Source: src/physics/arcade/ArcadePhysics.js#L202
Since: 3.70.0
overlap ​
<instance> overlap(object1, [object2], [overlapCallback], [processCallback], [callbackContext]) ​
Description:
Tests if Game Objects overlap. See Phaser.Physics.Arcade.World#overlap
Parameters:
name type optional description
object1 Phaser.Types.Physics.Arcade.ArcadeColliderType No The first object or array of objects to check.
object2 Phaser.Types.Physics.Arcade.ArcadeColliderType Yes The second object or array of objects to check, or undefined .
overlapCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects overlap.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they overlap. If this is set then overlapCallback will only be called if this callback returns true .
callbackContext * Yes The context in which to run the callbacks.
Returns: boolean - True if at least one Game Object overlaps another.
Source: src/physics/arcade/ArcadePhysics.js#L224
Since: 3.0.0
overlapCirc ​
<instance> overlapCirc(x, y, radius, [includeDynamic], [includeStatic]) ​
Description:
This method will search the given circular area and return an array of all physics bodies that
overlap with it. It can return either Dynamic, Static bodies or a mixture of both.
A body only has to intersect with the search area to be considered, it doesn't have to be fully
contained within it.
If Arcade Physics is set to use the RTree (which it is by default) then the search is rather fast,
otherwise the search is O(N) for Dynamic Bodies.
Parameters:
name type optional default description
x number No The x coordinate of the center of the area to search within.
y number No The y coordinate of the center of the area to search within.
radius number No The radius of the area to search within.
includeDynamic boolean Yes true Should the search include Dynamic Bodies?
includeStatic boolean Yes false Should the search include Static Bodies?
Returns: Array.< Phaser.Physics.Arcade.Body >, Array.< Phaser.Physics.Arcade.StaticBody > - An array of bodies that overlap with the given area.
Source: src/physics/arcade/ArcadePhysics.js#L677
Since: 3.21.0
overlapRect ​
<instance> overlapRect(x, y, width, height, [includeDynamic], [includeStatic]) ​
Description:
This method will search the given rectangular area and return an array of all physics bodies that
overlap with it. It can return either Dynamic, Static bodies or a mixture of both.
A body only has to intersect with the search area to be considered, it doesn't have to be fully
contained within it.
If Arcade Physics is set to use the RTree (which it is by default) then the search for is extremely fast,
otherwise the search is O(N) for Dynamic Bodies.
Parameters:
name type optional default description
x number No The top-left x coordinate of the area to search within.
y number No The top-left y coordinate of the area to search within.
width number No The width of the area to search within.
height number No The height of the area to search within.
includeDynamic boolean Yes true Should the search include Dynamic Bodies?
includeStatic boolean Yes false Should the search include Static Bodies?
Returns: Array.< Phaser.Physics.Arcade.Body >, Array.< Phaser.Physics.Arcade.StaticBody > - An array of bodies that overlap with the given area.
Source: src/physics/arcade/ArcadePhysics.js#L650
Since: 3.17.0
overlapTiles ​
<instance> overlapTiles(sprite, tiles, [overlapCallback], [processCallback], [callbackContext]) ​
Description:
This advanced method is specifically for testing for overlaps between a single Sprite and an array of Tile objects.
You should generally use the overlap method instead, with a Sprite vs. a Tilemap Layer, as that will perform
tile filtering and culling for you, as well as handle the interesting face collision automatically.
This method is offered for those who would like to check for overlaps with specific Tiles in a layer, without
having to set any collision attributes on the tiles in question. This allows you to perform quick dynamic overlap
tests on small sets of Tiles. As such, no culling or checks are made to the array of Tiles given to this method,
you should filter them before passing them to this method.
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No The first object to check for collision.
tiles Array.< Phaser.Tilemaps.Tile > No An array of Tiles to check for collision against.
overlapCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects overlap.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then overlapCallback will only be called if this callback returns true .
callbackContext any Yes The context in which to run the callbacks.
Returns: boolean - True if any objects overlap (with overlapOnly ); or true if any overlapping objects were separated.
Fires: Phaser.Physics.Arcade.Events#event:TILE_OVERLAP
Source: src/physics/arcade/ArcadePhysics.js#L324
Since: 3.17.0
pause ​
<instance> pause() ​
Description:
Pauses the simulation.
Returns: Phaser.Physics.Arcade.World - The simulation.
Source: src/physics/arcade/ArcadePhysics.js#L352
Since: 3.0.0
resume ​
<instance> resume() ​
Description:
Resumes the simulation (if paused).
Returns: Phaser.Physics.Arcade.World - The simulation.
Source: src/physics/arcade/ArcadePhysics.js#L365
Since: 3.0.0
shutdown ​
<instance> shutdown() ​
Description:
The Scene that owns this plugin is shutting down.
We need to kill and reset all internal properties as well as stop listening to Scene events.
Source: src/physics/arcade/ArcadePhysics.js#L703
Since: 3.0.0
velocityFromAngle ​
<instance> velocityFromAngle(angle, [speed], [vec2]) ​
Description:
Given the angle (in degrees) and speed calculate the velocity and return it as a vector, or set it to the given vector object.
One way to use this is: velocityFromAngle(angle, 200, sprite.body.velocity) which will set the values directly to the sprite's velocity and not create a new vector object.
Parameters:
name type optional default description
angle number No The angle in degrees calculated in clockwise positive direction (down = 90 degrees positive, right = 0 degrees positive, up = 90 degrees negative)
speed number Yes 60 The speed it will move, in pixels per second squared.
vec2 Phaser.Math.Vector2 Yes The Vector2 in which the x and y properties will be set to the calculated velocity.
Returns: Phaser.Math.Vector2 - The Vector2 that stores the velocity.
Source: src/physics/arcade/ArcadePhysics.js#L608
Since: 3.0.0
velocityFromRotation ​
<instance> velocityFromRotation(rotation, [speed], [vec2]) ​
Description:
Given the rotation (in radians) and speed calculate the velocity and return it as a vector, or set it to the given vector object.
One way to use this is: velocityFromRotation(rotation, 200, sprite.body.velocity) which will set the values directly to the sprite's velocity and not create a new vector object.
Parameters:
name type optional default description
rotation number No The angle in radians.
speed number Yes 60 The speed it will move, in pixels per second squared
vec2 Phaser.Math.Vector2 Yes The Vector2 in which the x and y properties will be set to the calculated velocity.
Returns: Phaser.Math.Vector2 - The Vector2 that stores the velocity.
Source: src/physics/arcade/ArcadePhysics.js#L629
Since: 3.0.0
Previous
Vector4
Next
Body
Public Members
add
config
scene
systems
world
Public Methods
accelerateTo
accelerateToObject
closest
collide
collideTiles
destroy
disableUpdate
enableUpdate
furthest
getConfig
moveTo
moveToObject
nextCategory
overlap
overlapCirc
overlapRect
overlapTiles
pause
resume
shutdown
velocityFromAngle
velocityFromRotation
