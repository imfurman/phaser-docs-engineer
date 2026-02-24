# Phaser.Physics.Arcade.Components.Angular | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-components-angular

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.Components.Angular
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.Components.Angular
Scope: static
Source: src/physics/arcade/components/Angular.js#L7
Since: 3.0.0
Static functions ​
setAngularAcceleration ​
<instance> setAngularAcceleration(value) ​
Description:
Sets the angular acceleration of the body.
In Arcade Physics, bodies cannot rotate. They are always axis-aligned.
However, they can have angular motion, which is passed on to the Game Object bound to the body,
causing them to visually rotate, even though the body remains axis-aligned.
Parameters:
name type optional description
value number No The amount of angular acceleration.
Returns: Phaser.Physics.Arcade.Components.Angular - This Game Object.
Source: src/physics/arcade/components/Angular.js#L36
Since: 3.0.0
setAngularDrag ​
<instance> setAngularDrag(value) ​
Description:
Sets the angular drag of the body. Drag is applied to the current velocity, providing a form of deceleration.
Parameters:
name type optional description
value number No The amount of drag.
Returns: Phaser.Physics.Arcade.Components.Angular - This Game Object.
Source: src/physics/arcade/components/Angular.js#L57
Since: 3.0.0
setAngularVelocity ​
<instance> setAngularVelocity(value) ​
Description:
Sets the angular velocity of the body.
In Arcade Physics, bodies cannot rotate. They are always axis-aligned.
However, they can have angular motion, which is passed on to the Game Object bound to the body,
causing them to visually rotate, even though the body remains axis-aligned.
Parameters:
name type optional description
value number No The amount of angular velocity.
Returns: Phaser.Physics.Arcade.Components.Angular - This Game Object.
Source: src/physics/arcade/components/Angular.js#L15
Since: 3.0.0
Previous
Phaser.Physics.Arcade.Components.Acceleration
Next
Phaser.Physics.Arcade.Components.Bounce
Static functions
setAngularAcceleration
setAngularDrag
setAngularVelocity
