# TileBody | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-matter-tilebody

Phaser API Documentation
Class
TileBody
Version: Phaser v3.90.0
On this page
TileBody
A wrapper around a Tile that provides access to a corresponding Matter body. A tile can only
have one Matter body associated with it. You can either pass in an existing Matter body for
the tile or allow the constructor to create the corresponding body for you. If the Tile has a
collision group (defined in Tiled), those shapes will be used to create the body. If not, the
tile's rectangle bounding box will be used.
The corresponding body will be accessible on the Tile itself via Tile.physics.matterBody.
Note: not all Tiled collision shapes are supported. See
Phaser.Physics.Matter.TileBody#setFromTileCollision for more information.
Constructor
new TileBody(world, tile, [options])
Parameters
name type optional description
world Phaser.Physics.Matter.World No The Matter world instance this body belongs to.
tile Phaser.Tilemaps.Tile No The target tile that should have a Matter body.
options Phaser.Types.Physics.Matter.MatterTileOptions Yes Options to be used when creating the Matter body.
Scope : static
Extends
Phaser.Events.EventEmitter
Phaser.Physics.Matter.Components.Bounce
Phaser.Physics.Matter.Components.Collision
Phaser.Physics.Matter.Components.Friction
Phaser.Physics.Matter.Components.Gravity
Phaser.Physics.Matter.Components.Mass
Phaser.Physics.Matter.Components.Sensor
Phaser.Physics.Matter.Components.Sleep
Phaser.Physics.Matter.Components.Static
Source: src/physics/matter-js/MatterTileBody.js#L17
Since: 3.0.0
Inherited Members ​
From Phaser.Physics.Matter.Components.Mass :
centerOfMass
Public Members ​
tile ​
tile: Phaser.Tilemaps.Tile ​
Description:
The tile object the body is associated with.
Source: src/physics/matter-js/MatterTileBody.js#L70
Since: 3.0.0
world ​
world: Phaser.Physics.Matter.World ​
Description:
The Matter world the body exists within.
Source: src/physics/matter-js/MatterTileBody.js#L79
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
From Phaser.Physics.Matter.Components.Bounce :
setBounce
From Phaser.Physics.Matter.Components.Collision :
setCollidesWith
setCollisionCategory
setCollisionGroup
setOnCollide
setOnCollideActive
setOnCollideEnd
setOnCollideWith
From Phaser.Physics.Matter.Components.Friction :
setFriction
setFrictionAir
setFrictionStatic
From Phaser.Physics.Matter.Components.Gravity :
setIgnoreGravity
From Phaser.Physics.Matter.Components.Mass :
setDensity
setMass
From Phaser.Physics.Matter.Components.Sensor :
isSensor
setSensor
From Phaser.Physics.Matter.Components.Sleep :
setAwake
setSleepEndEvent
setSleepEvents
setSleepStartEvent
setSleepThreshold
setToSleep
From Phaser.Physics.Matter.Components.Static :
isStatic
setStatic
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Removes the current body from the tile and the world.
Overrides: Phaser.Events.EventEmitter#destroy
Returns: Phaser.Physics.Matter.TileBody - This TileBody object.
Source: src/physics/matter-js/MatterTileBody.js#L310
Since: 3.0.0
removeBody ​
<instance> removeBody() ​
Description:
Removes the current body from the TileBody and from the Matter world
Returns: Phaser.Physics.Matter.TileBody - This TileBody object.
Source: src/physics/matter-js/MatterTileBody.js#L290
Since: 3.0.0
setBody ​
<instance> setBody(body, [addToWorld]) ​
Description:
Sets the current body to the given body. This will remove the previous body, if one already
exists.
Parameters:
name type optional default description
body MatterJS.BodyType No The new Matter body to use.
addToWorld boolean Yes true Whether or not to add the body to the Matter world.
Returns: Phaser.Physics.Matter.TileBody - This TileBody object.
Source: src/physics/matter-js/MatterTileBody.js#L258
Since: 3.0.0
setFromTileCollision ​
<instance> setFromTileCollision([options]) ​
Description:
Sets the current body from the collision group associated with the Tile. This is typically
set up in Tiled's collision editor.
Note: Matter doesn't support all shapes from Tiled. Rectangles and polygons are directly
supported. Ellipses are converted into circle bodies. Polylines are treated as if they are
closed polygons. If a tile has multiple shapes, a multi-part body will be created. Concave
shapes are supported if poly-decomp library is included. Decomposition is not guaranteed to
work for complex shapes (e.g. holes), so it's often best to manually decompose a concave
polygon into multiple convex polygons yourself.
Parameters:
name type optional description
options Phaser.Types.Physics.Matter.MatterBodyTileOptions Yes Options to be used when creating the Matter body. See MatterJS.Body for a list of what Matter accepts.
Returns: Phaser.Physics.Matter.TileBody - This TileBody object.
Source: src/physics/matter-js/MatterTileBody.js#L158
Since: 3.0.0
setFromTileRectangle ​
<instance> setFromTileRectangle([options]) ​
Description:
Sets the current body to a rectangle that matches the bounds of the tile.
Parameters:
name type optional description
options Phaser.Types.Physics.Matter.MatterBodyTileOptions Yes Options to be used when creating the Matter body. See MatterJS.Body for a list of what Matter accepts.
Returns: Phaser.Physics.Matter.TileBody - This TileBody object.
Source: src/physics/matter-js/MatterTileBody.js#L132
Since: 3.0.0
Previous
Sprite
Next
World
Inherited Members
Public Members
tile
world
Inherited Methods
Public Methods
destroy
removeBody
setBody
setFromTileCollision
setFromTileRectangle
