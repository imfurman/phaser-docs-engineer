# Phaser.Physics.Matter.Components.Mass | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-components-mass

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.Components.Mass
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.Components.Mass
Scope: static
Source: src/physics/matter-js/components/Mass.js#L10
Since: 3.0.0
Static functions ​
setDensity ​
<instance> setDensity(value) ​
Description:
Sets density of the body.
Parameters:
name type optional description
value number No The new density of the body.
Returns: Phaser.Physics.Matter.Components.Mass - This Game Object instance.
Source: src/physics/matter-js/components/Mass.js#L35
Since: 3.0.0
setMass ​
<instance> setMass(value) ​
Description:
Sets the mass of the Game Object's Matter Body.
Parameters:
name type optional description
value number No The new mass of the body.
Returns: Phaser.Physics.Matter.Components.Mass - This Game Object instance.
Source: src/physics/matter-js/components/Mass.js#L18
Since: 3.0.0
Static functions ​
centerOfMass ​
centerOfMass: Phaser.Math.Vector2 ​
Description:
The body's center of mass.
Calling this creates a new `Vector2 each time to avoid mutation.
If you only need to read the value and won't change it, you can get it from GameObject.body.centerOfMass .
Returns: Phaser.Math.Vector2 - The center of mass.
Source: src/physics/matter-js/components/Mass.js#L52
Since: 3.10.0
Previous
Phaser.Physics.Matter.Components.Gravity
Next
Phaser.Physics.Matter.Components.Sensor
Static functions
setDensity
setMass
Static functions
centerOfMass
