# Phaser.Physics.Arcade.Components.Size | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-components-size

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.Components.Size
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.Components.Size
Scope: static
Source: src/physics/arcade/components/Size.js#L7
Since: 3.0.0
Static functions ​
setBodySize ​
<instance> setBodySize(width, height, [center]) ​
Description:
Sets the size of this physics body. Setting the size does not adjust the dimensions of the parent Game Object.
Parameters:
name type optional default description
width number No The new width of the physics body, in pixels.
height number No The new height of the physics body, in pixels.
center boolean Yes true Should the body be re-positioned so its center aligns with the parent Game Object?
Returns: Phaser.Physics.Arcade.Components.Size - This Game Object.
Source: src/physics/arcade/components/Size.js#L57
Since: 3.24.0
setCircle ​
<instance> setCircle(radius, [offsetX], [offsetY]) ​
Description:
Sets this physics body to use a circle for collision instead of a rectangle.
Parameters:
name type optional description
radius number No The radius of the physics body, in pixels.
offsetX number Yes The amount to offset the body from the parent Game Object along the x-axis.
offsetY number Yes The amount to offset the body from the parent Game Object along the y-axis.
Returns: Phaser.Physics.Arcade.Components.Size - This Game Object.
Source: src/physics/arcade/components/Size.js#L76
Since: 3.0.0
setOffset ​
<instance> setOffset(x, [y]) ​
Description:
Sets the body offset. This allows you to adjust the difference between the center of the body
and the x and y coordinates of the parent Game Object.
Parameters:
name type optional default description
x number No The amount to offset the body from the parent Game Object along the x-axis.
y number Yes "x" The amount to offset the body from the parent Game Object along the y-axis. Defaults to the value given for the x-axis.
Returns: Phaser.Physics.Arcade.Components.Size - This Game Object.
Source: src/physics/arcade/components/Size.js#L16
Since: 3.0.0
setSize ​
<instance> setSize(width, height, [center]) ​
Description:
DEPRECATED : Please use setBodySize instead.
Sets the size of this physics body. Setting the size does not adjust the dimensions of the parent Game Object.
Parameters:
name type optional default description
width number No The new width of the physics body, in pixels.
height number No The new height of the physics body, in pixels.
center boolean Yes true Should the body be re-positioned so its center aligns with the parent Game Object?
Returns: Phaser.Physics.Arcade.Components.Size - This Game Object.
Source: src/physics/arcade/components/Size.js#L35
Since: 3.0.0
Previous
Phaser.Physics.Arcade.Components.Pushable
Next
Phaser.Physics.Arcade.Components.Velocity
Static functions
setBodySize
setCircle
setOffset
setSize
