# Phaser.Physics.Matter.PhysicsEditorParser | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-physicseditorparser

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.PhysicsEditorParser
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.PhysicsEditorParser
Scope: static
Source: src/physics/matter-js/PhysicsEditorParser.js#L15
Since: 3.10.0
Static functions ​
parseBody ​
<static> parseBody(x, y, config, [options]) ​
Description:
Parses a body element exported by PhysicsEditor.
Parameters:
name type optional description
x number No The horizontal world location of the body.
y number No The vertical world location of the body.
config object No The body configuration and fixture (child body) definitions, as exported by PhysicsEditor.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: MatterJS.BodyType - A compound Matter JS Body.
Source: src/physics/matter-js/PhysicsEditorParser.js#L24
Since: 3.10.0
parseFixture ​
<static> parseFixture(fixtureConfig) ​
Description:
Parses an element of the "fixtures" list exported by PhysicsEditor
Parameters:
name type optional description
fixtureConfig object No The fixture object to parse.
Returns: Array.<MatterJS.BodyType> - - An array of Matter JS Bodies.
Source: src/physics/matter-js/PhysicsEditorParser.js#L70
Since: 3.10.0
parseVertices ​
<static> parseVertices(vertexSets, [options]) ​
Description:
Parses the "vertices" lists exported by PhysicsEditor.
Parameters:
name type optional description
vertexSets array No The vertex lists to parse.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: Array.<MatterJS.BodyType> - - An array of Matter JS Bodies.
Source: src/physics/matter-js/PhysicsEditorParser.js#L104
Since: 3.10.0
Previous
Phaser.Physics.Matter.Matter
Next
Phaser.Physics.Matter.PhysicsJSONParser
Static functions
parseBody
parseFixture
parseVertices
