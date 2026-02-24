# Phaser.Physics.Arcade.Components.Enable | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-components-enable

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.Components.Enable
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.Components.Enable
Scope: static
Source: src/physics/arcade/components/Enable.js#L7
Since: 3.0.0
Static functions ​
disableBody ​
<instance> disableBody([disableGameObject], [hideGameObject]) ​
Description:
Stops and disables this Game Object's Body.
Parameters:
name type optional default description
disableGameObject boolean Yes false Also set this Game Object's active to false.
hideGameObject boolean Yes false Also set this Game Object's visible to false.
Returns: Phaser.Physics.Arcade.Components.Enable - This Game Object.
Source: src/physics/arcade/components/Enable.js#L81
Since: 3.0.0
enableBody ​
<instance> enableBody([reset], [x], [y], [enableGameObject], [showGameObject]) ​
Description:
Enables this Game Object's Body.
If you reset the Body you must also pass x and y .
Parameters:
name type optional description
reset boolean Yes Also reset the Body and place the Game Object at (x, y).
x number Yes The horizontal position to place the Game Object, if reset is true.
y number Yes The horizontal position to place the Game Object, if reset is true.
enableGameObject boolean Yes Also set this Game Object's active to true.
showGameObject boolean Yes Also set this Game Object's visible to true.
Returns: Phaser.Physics.Arcade.Components.Enable - This Game Object.
Source: src/physics/arcade/components/Enable.js#L37
Since: 3.0.0
refreshBody ​
<instance> refreshBody() ​
Description:
Syncs the Body's position and size with its parent Game Object.
You don't need to call this for Dynamic Bodies, as it happens automatically.
But for Static bodies it's a useful way of modifying the position of a Static Body
in the Physics World, based on its Game Object.
Returns: Phaser.Physics.Arcade.Components.Enable - This Game Object.
Source: src/physics/arcade/components/Enable.js#L119
Since: 3.1.0
setDirectControl ​
<instance> setDirectControl([value]) ​
Description:
Sets whether this Body should calculate its velocity based on its change in
position every frame. The default, which is to not do this, means that you
make this Body move by setting the velocity directly. However, if you are
trying to move this Body via a Tween, or have it follow a Path, then you
should enable this instead. This will allow it to still collide with other
bodies, something that isn't possible if you're just changing its position directly.
Parameters:
name type optional default description
value boolean Yes true true if the Body calculate velocity based on changes in position, otherwise false .
Returns: Phaser.Physics.Arcade.Components.Enable - This Game Object.
Source: src/physics/arcade/components/Enable.js#L15
Since: 3.70.0
Previous
Phaser.Physics.Arcade.Components.Drag
Next
Phaser.Physics.Arcade.Components.Friction
Static functions
disableBody
enableBody
refreshBody
setDirectControl
