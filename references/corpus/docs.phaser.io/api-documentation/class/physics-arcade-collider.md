# Collider | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-arcade-collider

Phaser API Documentation
Class
Collider
Version: Phaser v3.90.0
On this page
Collider
An Arcade Physics Collider will automatically check for collision, or overlaps, between two objects
every step. If a collision, or overlap, occurs it will invoke the given callbacks.
Note, if setting overlapOnly to true , and one of the objects is a TilemapLayer , every tile in the layer, regardless of tile ID, will be checked for collision.
Even if the layer has had only a subset of tile IDs enabled for collision, all tiles will still be checked for overlap.
Constructor
new Collider(world, overlapOnly, object1, object2, collideCallback, processCallback, callbackContext)
Parameters
name type optional description
world Phaser.Physics.Arcade.World No The Arcade physics World that will manage the collisions.
overlapOnly boolean No Whether to check for collisions or overlaps.
object1 Phaser.Types.Physics.Arcade.ArcadeColliderType No The first object to check for collision.
object2 Phaser.Types.Physics.Arcade.ArcadeColliderType No The second object to check for collision.
collideCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback No The callback to invoke when the two objects collide.
processCallback Phaser.Types.Physics.Arcade.ArcadePhysicsCallback No The callback to invoke when the two objects collide. Must return a boolean.
callbackContext any No The scope in which to call the callbacks.
Scope : static
Source: src/physics/arcade/Collider.js#L9
Since: 3.0.0
Public Members ​
active ​
active: boolean ​
Description:
Whether the collider is active.
Source: src/physics/arcade/Collider.js#L54
Since: 3.0.0
callbackContext ​
callbackContext: object ​
Description:
The context the collideCallback and processCallback will run in.
Source: src/physics/arcade/Collider.js#L109
Since: 3.0.0
collideCallback ​
collideCallback: Phaser.Types.Physics.Arcade.ArcadePhysicsCallback ​
Description:
The callback to invoke when the two objects collide.
Source: src/physics/arcade/Collider.js#L91
Since: 3.0.0
name ​
name: string ​
Description:
The name of the collider (unused by Phaser).
Source: src/physics/arcade/Collider.js#L45
Since: 3.1.0
object1 ​
object1: Phaser.Types.Physics.Arcade.ArcadeColliderType ​
Description:
The first object to check for collision.
Source: src/physics/arcade/Collider.js#L73
Since: 3.0.0
object2 ​
object2: Phaser.Types.Physics.Arcade.ArcadeColliderType ​
Description:
The second object to check for collision.
Source: src/physics/arcade/Collider.js#L82
Since: 3.0.0
overlapOnly ​
overlapOnly: boolean ​
Description:
Whether to check for collisions or overlaps.
Source: src/physics/arcade/Collider.js#L64
Since: 3.0.0
processCallback ​
processCallback: Phaser.Types.Physics.Arcade.ArcadePhysicsCallback ​
Description:
If a processCallback exists it must return true or collision checking will be skipped.
Source: src/physics/arcade/Collider.js#L100
Since: 3.0.0
world ​
world: Phaser.Physics.Arcade.World ​
Description:
The world in which the bodies will collide.
Source: src/physics/arcade/Collider.js#L36
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Removes Collider from World and disposes of its resources.
Source: src/physics/arcade/Collider.js#L156
Since: 3.0.0
setName ​
<instance> setName(name) ​
Description:
A name for the Collider.
Phaser does not use this value, it's for your own reference.
Parameters:
name type optional description
name string No The name to assign to the Collider.
Returns: Phaser.Physics.Arcade.Collider - This Collider instance.
Source: src/physics/arcade/Collider.js#L119
Since: 3.1.0
update ​
<instance> update() ​
Description:
Called by World as part of its step processing, initial operation of collision checking.
Source: src/physics/arcade/Collider.js#L138
Since: 3.0.0
Previous
Body
Next
Factory
Public Members
active
callbackContext
collideCallback
name
object1
object2
overlapOnly
processCallback
world
Public Methods
destroy
setName
update
