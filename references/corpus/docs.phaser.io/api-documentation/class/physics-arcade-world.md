# World | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-arcade-world

Phaser API Documentation
Class
World
Version: Phaser v3.90.0
On this page
World
The Arcade Physics World.
The World is responsible for creating, managing, colliding and updating all of the bodies within it.
An instance of the World belongs to a Phaser.Scene and is accessed via the property physics.world .
Constructor
new World(scene, config)
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this World instance belongs.
config Phaser.Types.Physics.Arcade.ArcadeWorldConfig No An Arcade Physics Configuration object.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/physics/arcade/World.js#L39
Since: 3.0.0
Public Members ​
bodies ​
bodies: Phaser.Structs.Set.<Phaser.Physics.Arcade.Body> ​
Description:
Dynamic Bodies in this simulation.
Source: src/physics/arcade/World.js#L75
Since: 3.0.0
bounds ​
bounds: Phaser.Geom.Rectangle ​
Description:
A boundary constraining Bodies.
Source: src/physics/arcade/World.js#L120
Since: 3.0.0
checkCollision ​
checkCollision: Phaser.Types.Physics.Arcade.CheckCollisionObject ​
Description:
The boundary edges that Bodies can collide with.
Source: src/physics/arcade/World.js#L134
Since: 3.0.0
colliders ​
colliders: Phaser.Structs.ProcessQueue.<Phaser.Physics.Arcade.Collider> ​
Description:
This simulation's collision processors.
Source: src/physics/arcade/World.js#L102
Since: 3.0.0
debugGraphic ​
debugGraphic: Phaser.GameObjects.Graphics ​
Description:
The graphics object drawing the debug display.
Source: src/physics/arcade/World.js#L293
Since: 3.0.0
defaults ​
defaults: Phaser.Types.Physics.Arcade.ArcadeWorldDefaults ​
Description:
Default debug display settings for new Bodies.
Source: src/physics/arcade/World.js#L302
Since: 3.0.0
drawDebug ​
drawDebug: boolean ​
Description:
Enables the debug display.
Source: src/physics/arcade/World.js#L283
Since: 3.0.0
fixedStep ​
fixedStep: boolean ​
Description:
Should Physics use a fixed update time-step (true) or sync to the render fps (false)?.
False value of this property disables fps and timeScale properties.
Source: src/physics/arcade/World.js#L161
Since: 3.23.0
forceX ​
forceX: boolean ​
Description:
Always separate overlapping Bodies horizontally before vertically.
False (the default) means Bodies are first separated on the axis of greater gravity, or the vertical axis if neither is greater.
Source: src/physics/arcade/World.js#L251
Since: 3.0.0
fps ​
fps: number ​
Description:
The number of physics steps to be taken per second.
This property is read-only. Use the setFPS method to modify it at run-time.
Source: src/physics/arcade/World.js#L148
Since: 3.10.0
gravity ​
gravity: Phaser.Math.Vector2 ​
Description:
Acceleration of Bodies due to gravity, in pixels per second.
Source: src/physics/arcade/World.js#L111
Since: 3.0.0
isPaused ​
isPaused: boolean ​
Description:
Whether the simulation advances with the game loop.
Source: src/physics/arcade/World.js#L262
Since: 3.0.0
maxEntries ​
maxEntries: number ​
Description:
The maximum number of items per node on the RTree.
This is ignored if useTree is false . If you have a large number of bodies in
your world then you may find search performance improves by increasing this value,
to allow more items per node and less node division.
Source: src/physics/arcade/World.js#L318
Since: 3.0.0
OVERLAP_BIAS ​
OVERLAP_BIAS: number ​
Description:
The maximum absolute difference of a Body's per-step velocity and its overlap with another Body that will result in separation on each axis .
Larger values favor separation.
Smaller values favor no separation.
Source: src/physics/arcade/World.js#L226
Since: 3.0.0
pendingDestroy ​
pendingDestroy: Phaser.Structs.Set.<(Phaser.Physics.Arcade.Body | Phaser.Physics.Arcade.StaticBody )> ​
Description:
Static Bodies marked for deletion.
Source: src/physics/arcade/World.js#L93
Since: 3.1.0
scene ​
scene: Phaser.Scene ​
Description:
The Scene this simulation belongs to.
Source: src/physics/arcade/World.js#L66
Since: 3.0.0
staticBodies ​
staticBodies: Phaser.Structs.Set.<Phaser.Physics.Arcade.StaticBody> ​
Description:
Static Bodies in this simulation.
Source: src/physics/arcade/World.js#L84
Since: 3.0.0
staticTree ​
staticTree: Phaser.Structs.RTree ​
Description:
The spatial index of Static Bodies.
Source: src/physics/arcade/World.js#L365
Since: 3.0.0
stepsLastFrame ​
stepsLastFrame: number ​
Description:
The number of steps that took place in the last frame.
Source: src/physics/arcade/World.js#L202
Since: 3.10.0
TILE_BIAS ​
TILE_BIAS: number ​
Description:
The maximum absolute value of a Body's overlap with a tile that will result in separation on each axis .
Larger values favor separation.
Smaller values favor no separation.
The optimum value may be similar to the tile size.
Source: src/physics/arcade/World.js#L238
Since: 3.0.0
tileFilterOptions ​
tileFilterOptions: Phaser.Types.Tilemaps.FilteringOptions ​
Description:
The Filtering Options passed to GetTilesWithinWorldXY as part of the collideSpriteVsTilemapLayer check.
Source: src/physics/arcade/World.js#L403
Since: 3.60.0
timeScale ​
timeScale: number ​
Description:
Scaling factor applied to the frame rate.
1.0 = normal speed
2.0 = half speed
0.5 = double speed
Source: src/physics/arcade/World.js#L212
Since: 3.10.0
tree ​
tree: Phaser.Structs.RTree ​
Description:
The spatial index of Dynamic Bodies.
Source: src/physics/arcade/World.js#L356
Since: 3.0.0
treeMinMax ​
treeMinMax: Phaser.Types.Physics.Arcade.ArcadeWorldTreeMinMax ​
Description:
Recycled input for tree searches.
Source: src/physics/arcade/World.js#L374
Since: 3.0.0
useTree ​
useTree: boolean ​
Description:
Should this Arcade Physics World use an RTree for Dynamic bodies?
An RTree is a fast way of spatially sorting of all the bodies in the world.
However, at certain limits, the cost of clearing and inserting the bodies into the
tree every frame becomes more expensive than the search speed gains it provides.
If you have a large number of dynamic bodies in your world then it may be best to
disable the use of the RTree by setting this property to false in the physics config.
The number it can cope with depends on browser and device, but a conservative estimate
of around 5,000 bodies should be considered the max before disabling it.
This only applies to dynamic bodies. Static bodies are always kept in an RTree,
because they don't have to be cleared every frame, so you benefit from the
massive search speeds all the time.
Source: src/physics/arcade/World.js#L332
Since: 3.10.0
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
Public Methods ​
add ​
<instance> add(body) ​
Description:
Adds an existing Arcade Physics Body or StaticBody to the simulation.
The body is enabled and added to the local search trees.
Parameters:
name type optional description
body Phaser.Physics.Arcade.Body | Phaser.Physics.Arcade.StaticBody No The Body to be added to the simulation.
Returns: Phaser.Physics.Arcade.Body , Phaser.Physics.Arcade.StaticBody - The Body that was added to the simulation.
Source: src/physics/arcade/World.js#L540
Since: 3.10.0
addCollider ​
<instance> addCollider(object1, object2, [collideCallback], [processCallback], [callbackContext]) ​
Description:
Creates a new Collider object and adds it to the simulation.
A Collider is a way to automatically perform collision checks between two objects,
calling the collide and process callbacks if they occur.
Colliders are run as part of the World update, after all of the Bodies have updated.
By creating a Collider you don't need then call World.collide in your update loop,
as it will be handled for you automatically.
Parameters:
name type optional description
object1 Phaser.Types.Physics.Arcade.ArcadeColliderType No The first object to check for collision.
object2 Phaser.Types.Physics.Arcade.ArcadeColliderType No The second object to check for collision.
collideCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes The callback to invoke when the two objects collide.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes The callback to invoke when the two objects collide. Must return a boolean.
callbackContext * Yes The scope in which to call the callbacks.
Returns: Phaser.Physics.Arcade.Collider - The Collider that was created.
Source: src/physics/arcade/World.js#L801
Since: 3.0.0
addOverlap ​
<instance> addOverlap(object1, object2, [collideCallback], [processCallback], [callbackContext]) ​
Description:
Creates a new Overlap Collider object and adds it to the simulation.
A Collider is a way to automatically perform overlap checks between two objects,
calling the collide and process callbacks if they occur.
Colliders are run as part of the World update, after all of the Bodies have updated.
By creating a Collider you don't need then call World.overlap in your update loop,
as it will be handled for you automatically.
Parameters:
name type optional description
object1 Phaser.Types.Physics.Arcade.ArcadeColliderType No The first object to check for overlap.
object2 Phaser.Types.Physics.Arcade.ArcadeColliderType No The second object to check for overlap.
collideCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes The callback to invoke when the two objects overlap.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes The callback to invoke when the two objects overlap. Must return a boolean.
callbackContext * Yes The scope in which to call the callbacks.
Returns: Phaser.Physics.Arcade.Collider - The Collider that was created.
Source: src/physics/arcade/World.js#L837
Since: 3.0.0
canCollide ​
<instance> canCollide(body1, body2) ​
Description:
Checks if the two given Arcade Physics bodies will collide, or not,
based on their collision mask and collision categories.
Parameters:
name type optional description
body1 Phaser.Types.Physics.Arcade.ArcadeCollider No The first body to check.
body2 Phaser.Types.Physics.Arcade.ArcadeCollider No The second body to check.
Returns: boolean - True if the two bodies will collide, otherwise false.
Source: src/physics/arcade/World.js#L1997
Since: 3.70.0
circleBodyIntersects ​
<instance> circleBodyIntersects(circle, body) ​
Description:
Tests if a circular Body intersects with another Body.
Parameters:
name type optional description
circle Phaser.Physics.Arcade.Body No The circular body to test.
body Phaser.Physics.Arcade.Body No The rectangular body to test.
Returns: boolean - True if the two bodies intersect, otherwise false.
Source: src/physics/arcade/World.js#L1735
Since: 3.0.0
collide ​
<instance> collide(object1, [object2], [collideCallback], [processCallback], [callbackContext]) ​
Description:
Performs a collision check and separation between the two physics enabled objects given, which can be single
Game Objects, arrays of Game Objects, Physics Groups, arrays of Physics Groups or normal Groups.
If you don't require separation then use Phaser.Physics.Arcade.World#overlap instead.
If two Groups or arrays are passed, each member of one will be tested against each member of the other.
If only one Group is passed (as object1 ), each member of the Group will be collided against the other members.
If only one Array is passed, the array is iterated and every element in it is tested against the others.
Two callbacks can be provided; they receive the colliding game objects as arguments.
If an overlap is detected, the processCallback is called first. It can cancel the collision by returning false.
Next the objects are separated and collideCallback is invoked.
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
callbackContext any Yes The context in which to run the callbacks.
Returns: boolean - true if any overlapping Game Objects were separated, otherwise false .
Source: src/physics/arcade/World.js#L1784
Since: 3.0.0
collideSpriteVsTilemapLayer ​
<instance> collideSpriteVsTilemapLayer(sprite, tilemapLayer, [collideCallback], [processCallback], [callbackContext], [overlapOnly]) ​
Description:
Internal handler for Sprite vs. Tilemap collisions.
Please use Phaser.Physics.Arcade.World#collide instead.
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No The first object to check for collision.
tilemapLayer Phaser.Tilemaps.TilemapLayer No The second object to check for collision.
collideCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects collide.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then collideCallback will only be called if this callback returns true .
callbackContext any Yes The context in which to run the callbacks.
overlapOnly boolean Yes Whether this is a collision or overlap check.
Returns: boolean - True if any objects overlap (with overlapOnly ); or true if any overlapping objects were separated.
Fires: Phaser.Physics.Arcade.Events#event:TILE_COLLIDE , Phaser.Physics.Arcade.Events#event:TILE_OVERLAP
Source: src/physics/arcade/World.js#L2277
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
This method does not factor in the Collision Mask or Category.
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No The first object to check for collision.
tiles Array.< Phaser.Tilemaps.Tile > No An array of Tiles to check for collision against.
collideCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects collide.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then collideCallback will only be called if this callback returns true .
callbackContext any Yes The context in which to run the callbacks.
Returns: boolean - True if any objects overlap (with overlapOnly ); or true if any overlapping objects were separated.
Fires: Phaser.Physics.Arcade.Events#event:TILE_COLLIDE
Source: src/physics/arcade/World.js#L2198
Since: 3.17.0
computeAngularVelocity ​
<instance> computeAngularVelocity(body, delta) ​
Description:
Calculates a Body's angular velocity.
Parameters:
name type optional description
body Phaser.Physics.Arcade.Body No The Body to compute the velocity for.
delta number No The delta value to be used in the calculation, in seconds.
Source: src/physics/arcade/World.js#L1191
Since: 3.10.0
computeVelocity ​
<instance> computeVelocity(body, delta) ​
Description:
Calculates a Body's per-axis velocity.
Parameters:
name type optional description
body Phaser.Physics.Arcade.Body No The Body to compute the velocity for.
delta number No The delta value to be used in the calculation, in seconds.
Source: src/physics/arcade/World.js#L1237
Since: 3.0.0
createDebugGraphic ​
<instance> createDebugGraphic() ​
Description:
Creates a Graphics Game Object that the world will use to render the debug display to.
This is called automatically when the World is instantiated if the debug config property
was set to true . However, you can call it at any point should you need to display the
debug Graphic from a fixed point.
You can control which objects are drawn to the Graphics object, and the colors they use,
by setting the debug properties in the physics config.
You should not typically use this in a production game. Use it to aid during debugging.
Returns: Phaser.GameObjects.Graphics - The Graphics object that was created for use by the World.
Source: src/physics/arcade/World.js#L668
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Shuts down the simulation and disconnects it from the current scene.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/physics/arcade/World.js#L2514
Since: 3.0.0
disable ​
<instance> disable(object) ​
Description:
Disables the Arcade Physics Body of a Game Object, an array of Game Objects, or the children of a Group.
The difference between this and the disableBody method is that you can pass arrays or Groups
to this method.
The body itself is not deleted, it just has its enable property set to false, which
means you can re-enable it again at any point by passing it to enable World.enable or World.add .
Parameters:
name type optional description
object Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > Phaser.GameObjects.Group Array.< Phaser.GameObjects.Group >
Source: src/physics/arcade/World.js#L570
Since: 3.0.0
disableBody ​
<instance> disableBody(body) ​
Description:
Disables an existing Arcade Physics Body or StaticBody and removes it from the simulation.
The body is disabled and removed from the local search trees.
The body itself is not deleted, it just has its enable property set to false, which
means you can re-enable it again at any point by passing it to enable World.enable or World.add .
Parameters:
name type optional description
body Phaser.Physics.Arcade.Body | Phaser.Physics.Arcade.StaticBody No The Body to be disabled.
Source: src/physics/arcade/World.js#L621
Since: 3.0.0
enable ​
<instance> enable(object, [bodyType]) ​
Description:
Adds an Arcade Physics Body to a Game Object, an array of Game Objects, or the children of a Group.
The difference between this and the enableBody method is that you can pass arrays or Groups
to this method.
You can specify if the bodies are to be Dynamic or Static. A dynamic body can move via velocity and
acceleration. A static body remains fixed in place and as such is able to use an optimized search
tree, making it ideal for static elements such as level objects. You can still collide and overlap
with static bodies.
Normally, rather than calling this method directly, you'd use the helper methods available in the
Arcade Physics Factory, such as:
this . physics . add . image ( x , y , textureKey ) ;
this . physics . add . sprite ( x , y , textureKey ) ;
Calling factory methods encapsulates the creation of a Game Object and the creation of its
body at the same time. If you are creating custom classes then you can pass them to this
method to have their bodies created.
Parameters:
name type optional description
object Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > Phaser.GameObjects.Group Array.< Phaser.GameObjects.Group >
bodyType number Yes The type of Body to create. Either DYNAMIC_BODY or STATIC_BODY .
Source: src/physics/arcade/World.js#L418
Since: 3.0.0
enableBody ​
<instance> enableBody(object, [bodyType]) ​
Description:
Creates an Arcade Physics Body on a single Game Object.
If the Game Object already has a body, this method will simply add it back into the simulation.
You can specify if the body is Dynamic or Static. A dynamic body can move via velocity and
acceleration. A static body remains fixed in place and as such is able to use an optimized search
tree, making it ideal for static elements such as level objects. You can still collide and overlap
with static bodies.
Normally, rather than calling this method directly, you'd use the helper methods available in the
Arcade Physics Factory, such as:
this . physics . add . image ( x , y , textureKey ) ;
this . physics . add . sprite ( x , y , textureKey ) ;
Calling factory methods encapsulates the creation of a Game Object and the creation of its
body at the same time. If you are creating custom classes then you can pass them to this
method to have their bodies created.
Parameters:
name type optional description
object Phaser.GameObjects.GameObject No The Game Object on which to create the body.
bodyType number Yes The type of Body to create. Either DYNAMIC_BODY or STATIC_BODY .
Returns: Phaser.GameObjects.GameObject - The Game Object on which the body was created.
Source: src/physics/arcade/World.js#L486
Since: 3.0.0
intersects ​
<instance> intersects(body1, body2) ​
Description:
Checks to see if two Bodies intersect at all.
Parameters:
name type optional description
body1 Phaser.Physics.Arcade.Body No The first body to check.
body2 Phaser.Physics.Arcade.Body No The second body to check.
Returns: boolean - True if the two bodies intersect, otherwise false.
Source: src/physics/arcade/World.js#L1687
Since: 3.0.0
overlap ​
<instance> overlap(object1, [object2], [overlapCallback], [processCallback], [callbackContext]) ​
Description:
Tests if Game Objects overlap.
See details in Phaser.Physics.Arcade.World#collide .
Parameters:
name type optional description
object1 Phaser.Types.Physics.Arcade.ArcadeColliderType No The first object or array of objects to check.
object2 Phaser.Types.Physics.Arcade.ArcadeColliderType Yes The second object or array of objects to check, or undefined .
overlapCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects overlap.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they overlap. If this is set then overlapCallback will only be called if this callback returns true .
callbackContext * Yes The context in which to run the callbacks.
Returns: boolean - True if at least one Game Object overlaps another.
Source: src/physics/arcade/World.js#L1757
Since: 3.0.0
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
This method does not factor in the Collision Mask or Category.
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No The first object to check for collision.
tiles Array.< Phaser.Tilemaps.Tile > No An array of Tiles to check for collision against.
overlapCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that is called if the objects overlap.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes An optional callback function that lets you perform additional checks against the two objects if they collide. If this is set then overlapCallback will only be called if this callback returns true .
callbackContext any Yes The context in which to run the callbacks.
Returns: boolean - True if any objects overlap (with overlapOnly ); or true if any overlapping objects were separated.
Fires: Phaser.Physics.Arcade.Events#event:TILE_OVERLAP
Source: src/physics/arcade/World.js#L2240
Since: 3.17.0
pause ​
<instance> pause() ​
Description:
Pauses the simulation.
A paused simulation does not update any existing bodies, or run any Colliders.
However, you can still enable and disable bodies within it, or manually run collide or overlap
checks.
Returns: Phaser.Physics.Arcade.World - This World object.
Fires: Phaser.Physics.Arcade.Events#event:PAUSE
Source: src/physics/arcade/World.js#L760
Since: 3.0.0
postUpdate ​
<instance> postUpdate() ​
Description:
Updates bodies, draws the debug display, and handles pending queue operations.
Source: src/physics/arcade/World.js#L1077
Since: 3.0.0
remove ​
<instance> remove(body) ​
Description:
Removes an existing Arcade Physics Body or StaticBody from the simulation.
The body is disabled and removed from the local search trees.
The body itself is not deleted, it just has its enabled property set to false, which
means you can re-enable it again at any point by passing it to enable enable or add .
Parameters:
name type optional description
body Phaser.Physics.Arcade.Body | Phaser.Physics.Arcade.StaticBody No The body to be removed from the simulation.
Source: src/physics/arcade/World.js#L641
Since: 3.0.0
removeCollider ​
<instance> removeCollider(collider) ​
Description:
Removes a Collider from the simulation so it is no longer processed.
This method does not destroy the Collider. If you wish to add it back at a later stage you can call
World.colliders.add(Collider) .
If you no longer need the Collider you can call the Collider.destroy method instead, which will
automatically clear all of its references and then remove it from the World. If you call destroy on
a Collider you don't need to pass it to this method too.
Parameters:
name type optional description
collider Phaser.Physics.Arcade.Collider No The Collider to remove from the simulation.
Returns: Phaser.Physics.Arcade.World - This World object.
Source: src/physics/arcade/World.js#L872
Since: 3.0.0
resume ​
<instance> resume() ​
Description:
Resumes the simulation, if paused.
Returns: Phaser.Physics.Arcade.World - This World object.
Fires: Phaser.Physics.Arcade.Events#event:RESUME
Source: src/physics/arcade/World.js#L783
Since: 3.0.0
separate ​
<instance> separate(body1, body2, [processCallback], [callbackContext], [overlapOnly]) ​
Description:
Separates two Bodies.
Parameters:
name type optional description
body1 Phaser.Physics.Arcade.Body No The first Body to be separated.
body2 Phaser.Physics.Arcade.Body No The second Body to be separated.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback Yes The process callback.
callbackContext * Yes The context in which to invoke the callback.
overlapOnly boolean Yes If this a collide or overlap check?
Returns: boolean - True if separation occurred, otherwise false.
Fires: Phaser.Physics.Arcade.Events#event:COLLIDE , Phaser.Physics.Arcade.Events#event:OVERLAP
Source: src/physics/arcade/World.js#L1363
Since: 3.0.0
separateCircle ​
<instance> separateCircle(body1, body2, [overlapOnly]) ​
Description:
Separates two Bodies, when both are circular.
Parameters:
name type optional description
body1 Phaser.Physics.Arcade.Body No The first Body to be separated.
body2 Phaser.Physics.Arcade.Body No The second Body to be separated.
overlapOnly boolean Yes If this a collide or overlap check?
Returns: boolean - True if separation occurred, otherwise false.
Fires: Phaser.Physics.Arcade.Events#event:COLLIDE , Phaser.Physics.Arcade.Events#event:OVERLAP
Source: src/physics/arcade/World.js#L1480
Since: 3.0.0
setBounds ​
<instance> setBounds(x, y, width, height, [checkLeft], [checkRight], [checkUp], [checkDown]) ​
Description:
Sets the position, size and properties of the World boundary.
The World boundary is an invisible rectangle that defines the edges of the World.
If a Body is set to collide with the world bounds then it will automatically stop
when it reaches any of the edges. You can optionally set which edges of the boundary
should be checked against.
Parameters:
name type optional description
x number No The top-left x coordinate of the boundary.
y number No The top-left y coordinate of the boundary.
width number No The width of the boundary.
height number No The height of the boundary.
checkLeft boolean Yes Should bodies check against the left edge of the boundary?
checkRight boolean Yes Should bodies check against the right edge of the boundary?
checkUp boolean Yes Should bodies check against the top edge of the boundary?
checkDown boolean Yes Should bodies check against the bottom edge of the boundary?
Returns: Phaser.Physics.Arcade.World - This World object.
Source: src/physics/arcade/World.js#L698
Since: 3.0.0
setBoundsCollision ​
<instance> setBoundsCollision([left], [right], [up], [down]) ​
Description:
Enables or disables collisions on each edge of the World boundary.
Parameters:
name type optional default description
left boolean Yes true Should bodies check against the left edge of the boundary?
right boolean Yes true Should bodies check against the right edge of the boundary?
up boolean Yes true Should bodies check against the top edge of the boundary?
down boolean Yes true Should bodies check against the bottom edge of the boundary?
Returns: Phaser.Physics.Arcade.World - This World object.
Source: src/physics/arcade/World.js#L732
Since: 3.0.0
setFPS ​
<instance> setFPS(framerate) ​
Description:
Sets the frame rate to run the simulation at.
The frame rate value is used to simulate a fixed update time step. This fixed
time step allows for a straightforward implementation of a deterministic game state.
This frame rate is independent of the frequency at which the game is rendering. The
higher you set the fps, the more physics simulation steps will occur per game step.
Conversely, the lower you set it, the less will take place.
You can optionally advance the simulation directly yourself by calling the step method.
Parameters:
name type optional description
framerate number No The frame rate to advance the simulation at.
Returns: Phaser.Physics.Arcade.World - This World object.
Source: src/physics/arcade/World.js#L896
Since: 3.10.0
shutdown ​
<instance> shutdown() ​
Description:
Shuts down the simulation, clearing physics data and removing listeners.
Overrides: Phaser.Events.EventEmitter#shutdown
Source: src/physics/arcade/World.js#L2497
Since: 3.0.0
singleStep ​
<instance> singleStep() ​
Description:
Advances the simulation by a single step.
Fires: Phaser.Physics.Arcade.Events#event:WORLD_STEP
Source: src/physics/arcade/World.js#L1063
Since: 3.70.0
step ​
<instance> step(delta) ​
Description:
Advances the simulation by a time increment.
Parameters:
name type optional description
delta number No The delta time amount, in seconds, by which to advance the simulation.
Fires: Phaser.Physics.Arcade.Events#event:WORLD_STEP
Source: src/physics/arcade/World.js#L1011
Since: 3.10.0
update ​
<instance> update(time, delta) ​
Description:
Advances the simulation based on the elapsed time and fps rate.
This is called automatically by your Scene and does not need to be invoked directly.
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time, in ms, elapsed since the last frame.
Fires: Phaser.Physics.Arcade.Events#event:WORLD_STEP
Source: src/physics/arcade/World.js#L924
Since: 3.0.0
updateMotion ​
<instance> updateMotion(body, delta) ​
Description:
Calculates a Body's velocity and updates its position.
Parameters:
name type optional description
body Phaser.Physics.Arcade.Body No The Body to be updated.
delta number No The delta value to be used in the motion calculations, in seconds.
Source: src/physics/arcade/World.js#L1172
Since: 3.0.0
wrap ​
<instance> wrap(object, [padding]) ​
Description:
Wrap an object's coordinates (or several objects' coordinates) within Phaser.Physics.Arcade.World#bounds .
If the object is outside any boundary edge (left, top, right, bottom), it will be moved to the same offset from the opposite edge (the interior).
Parameters:
name type optional default description
object any No A Game Object, a Group, an object with x and y coordinates, or an array of such objects.
padding number Yes 0 An amount added to each boundary edge during the operation.
Source: src/physics/arcade/World.js#L2432
Since: 3.3.0
wrapArray ​
<instance> wrapArray(objects, [padding]) ​
Description:
Wrap each object's coordinates within Phaser.Physics.Arcade.World#bounds .
Parameters:
name type optional default description
objects Array.<*> No An array of objects to be wrapped.
padding number Yes 0 An amount added to the boundary.
Source: src/physics/arcade/World.js#L2463
Since: 3.3.0
wrapObject ​
<instance> wrapObject(object, [padding]) ​
Description:
Wrap an object's coordinates within Phaser.Physics.Arcade.World#bounds .
Parameters:
name type optional default description
object * No A Game Object, a Physics Body, or any object with x and y coordinates
padding number Yes 0 An amount added to the boundary.
Source: src/physics/arcade/World.js#L2480
Since: 3.3.0
Previous
StaticGroup
Next
BodyBounds
Public Members
bodies
bounds
checkCollision
colliders
debugGraphic
defaults
drawDebug
fixedStep
forceX
fps
gravity
isPaused
maxEntries
OVERLAP_BIAS
pendingDestroy
scene
staticBodies
staticTree
stepsLastFrame
TILE_BIAS
tileFilterOptions
timeScale
tree
treeMinMax
useTree
Inherited Methods
Public Methods
add
addCollider
addOverlap
canCollide
circleBodyIntersects
collide
collideSpriteVsTilemapLayer
collideTiles
computeAngularVelocity
computeVelocity
createDebugGraphic
destroy
disable
disableBody
enable
enableBody
intersects
overlap
overlapTiles
pause
postUpdate
remove
removeCollider
resume
separate
separateCircle
setBounds
setBoundsCollision
setFPS
shutdown
singleStep
step
update
updateMotion
wrap
wrapArray
wrapObject
