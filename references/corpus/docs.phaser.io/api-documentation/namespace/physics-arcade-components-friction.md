# Phaser.Physics.Arcade.Components.Friction | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-components-friction

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.Components.Friction
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.Components.Friction
Scope: static
Source: src/physics/arcade/components/Friction.js#L7
Since: 3.0.0
Static functions ​
setFriction ​
<instance> setFriction(x, [y]) ​
Description:
Sets the friction of this game object's physics body.
In Arcade Physics, friction is a special case of motion transfer from an "immovable" body to a riding body.
Parameters:
name type optional default description
x number No The amount of horizontal friction to apply, [0, 1].
y number Yes "x" The amount of vertical friction to apply, [0, 1].
Returns: Phaser.Physics.Arcade.Components.Friction - This Game Object.
Source: src/physics/arcade/components/Friction.js#L19
Since: 3.0.0
setFrictionX ​
<instance> setFrictionX(x) ​
Description:
Sets the horizontal friction of this game object's physics body.
This can move a riding body horizontally when it collides with this one on the vertical axis.
Parameters:
name type optional description
x number No The amount of friction to apply, [0, 1].
Returns: Phaser.Physics.Arcade.Components.Friction - This Game Object.
Source: src/physics/arcade/components/Friction.js#L40
Since: 3.0.0
setFrictionY ​
<instance> setFrictionY(y) ​
Description:
Sets the vertical friction of this game object's physics body.
This can move a riding body vertically when it collides with this one on the horizontal axis.
Parameters:
name type optional description
y number No The amount of friction to apply, [0, 1].
Returns: Phaser.Physics.Arcade.Components.Friction - This Game Object.
Source: src/physics/arcade/components/Friction.js#L60
Since: 3.0.0
Previous
Phaser.Physics.Arcade.Components.Enable
Next
Phaser.Physics.Arcade.Components.Gravity
Static functions
setFriction
setFrictionX
setFrictionY
