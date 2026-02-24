# Phaser.Physics.Matter.PhysicsJSONParser | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-physicsjsonparser

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.PhysicsJSONParser
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.PhysicsJSONParser
Scope: static
Source: src/physics/matter-js/PhysicsJSONParser.js#L10
Since: 3.22.0
Static functions ​
parseBody ​
<static> parseBody(x, y, config, [options]) ​
Description:
Parses a body element from the given JSON data.
Parameters:
name type optional description
x number No The horizontal world location of the body.
y number No The vertical world location of the body.
config object No The body configuration data.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: MatterJS.BodyType - A Matter JS Body.
Source: src/physics/matter-js/PhysicsJSONParser.js#L53
Since: 3.22.0
Previous
Phaser.Physics.Matter.PhysicsEditorParser
Next
Phaser.Physics.Matter
Static functions
parseBody
