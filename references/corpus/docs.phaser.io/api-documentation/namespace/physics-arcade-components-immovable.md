# Phaser.Physics.Arcade.Components.Immovable | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-components-immovable

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.Components.Immovable
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.Components.Immovable
Scope: static
Source: src/physics/arcade/components/Immovable.js#L7
Since: 3.0.0
Static functions ​
setImmovable ​
<instance> setImmovable([value]) ​
Description:
Sets if this Body can be separated during collisions with other bodies.
When a body is immovable it means it won't move at all, not even to separate it from collision
overlap. If you just wish to prevent a body from being knocked around by other bodies, see
the setPushable method instead.
Parameters:
name type optional default description
value boolean Yes true Sets if this body will be separated during collisions with other bodies.
Returns: Phaser.Physics.Arcade.Components.Immovable - This Game Object.
Source: src/physics/arcade/components/Immovable.js#L15
Since: 3.0.0
Previous
Phaser.Physics.Arcade.Components.Gravity
Next
Phaser.Physics.Arcade.Components.Mass
Static functions
setImmovable
