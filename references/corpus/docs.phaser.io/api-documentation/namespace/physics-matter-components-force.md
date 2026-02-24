# Phaser.Physics.Matter.Components.Force | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-components-force

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.Components.Force
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.Components.Force
Scope: static
Source: src/physics/matter-js/components/Force.js#L9
Since: 3.0.0
Static functions ​
applyForce ​
<instance> applyForce(force) ​
Description:
Applies a force to a body.
Parameters:
name type optional description
force Phaser.Math.Vector2 No A Vector that specifies the force to apply.
Returns: Phaser.Physics.Matter.Components.Force - This Game Object instance.
Source: src/physics/matter-js/components/Force.js#L19
Since: 3.0.0
applyForceFrom ​
<instance> applyForceFrom(position, force) ​
Description:
Applies a force to a body from a given position.
Parameters:
name type optional description
position Phaser.Math.Vector2 No The position in which the force comes from.
force Phaser.Math.Vector2 No A Vector that specifies the force to apply.
Returns: Phaser.Physics.Matter.Components.Force - This Game Object instance.
Source: src/physics/matter-js/components/Force.js#L38
Since: 3.0.0
thrust ​
<instance> thrust(speed) ​
Description:
Apply thrust to the forward position of the body.
Use very small values, such as 0.1, depending on the mass and required speed.
Parameters:
name type optional description
speed number No A speed value to be applied to a directional force.
Returns: Phaser.Physics.Matter.Components.Force - This Game Object instance.
Source: src/physics/matter-js/components/Force.js#L56
Since: 3.0.0
thrustBack ​
<instance> thrustBack(speed) ​
Description:
Apply thrust to the back position of the body.
Use very small values, such as 0.1, depending on the mass and required speed.
Parameters:
name type optional description
speed number No A speed value to be applied to a directional force.
Returns: Phaser.Physics.Matter.Components.Force - This Game Object instance.
Source: src/physics/matter-js/components/Force.js#L125
Since: 3.0.0
thrustLeft ​
<instance> thrustLeft(speed) ​
Description:
Apply thrust to the left position of the body.
Use very small values, such as 0.1, depending on the mass and required speed.
Parameters:
name type optional description
speed number No A speed value to be applied to a directional force.
Returns: Phaser.Physics.Matter.Components.Force - This Game Object instance.
Source: src/physics/matter-js/components/Force.js#L79
Since: 3.0.0
thrustRight ​
<instance> thrustRight(speed) ​
Description:
Apply thrust to the right position of the body.
Use very small values, such as 0.1, depending on the mass and required speed.
Parameters:
name type optional description
speed number No A speed value to be applied to a directional force.
Returns: Phaser.Physics.Matter.Components.Force - This Game Object instance.
Source: src/physics/matter-js/components/Force.js#L102
Since: 3.0.0
Previous
Phaser.Physics.Matter.Components.Collision
Next
Phaser.Physics.Matter.Components.Friction
Static functions
applyForce
applyForceFrom
thrust
thrustBack
thrustLeft
thrustRight
