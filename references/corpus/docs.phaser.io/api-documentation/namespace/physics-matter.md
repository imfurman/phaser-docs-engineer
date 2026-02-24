# Phaser.Physics.Matter | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter

Phaser API Documentation
Namespaces
Phaser.Physics.Matter
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter
Scope: static
Source: src/physics/matter-js/index.js#L7
Static functions ​
BodyBounds
Factory
Image
MatterPhysics
PointerConstraint
Sprite
TileBody
World
Static functions ​
Components
Events
Matter
PhysicsEditorParser
PhysicsJSONParser
Static functions ​
MatterGameObject ​
<static> MatterGameObject(world, gameObject, [options], [addToWorld]) ​
Description:
A Matter Game Object is a generic object that allows you to combine any Phaser Game Object,
including those you have extended or created yourself, with all of the Matter Components.
This enables you to use component methods such as setVelocity or isSensor directly from
this Game Object.
Parameters:
name type optional default description
world Phaser.Physics.Matter.World No The Matter world to add the body to.
gameObject Phaser.GameObjects.GameObject No The Game Object that will have the Matter body applied to it.
options Phaser.Types.Physics.Matter.MatterBodyConfig | MatterJS.Body Yes A Matter Body configuration object, or an instance of a Matter Body.
addToWorld boolean Yes true Should the newly created body be immediately added to the World?
Returns: Phaser.GameObjects.GameObject - The Game Object that was created with the Matter body.
Source: src/physics/matter-js/MatterGameObject.js#L26
Since: 3.3.0
Previous
Phaser.Physics.Matter.PhysicsJSONParser
Next
Phaser.Physics
Static functions
Static functions
Static functions
MatterGameObject
