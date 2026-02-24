# Phaser.Physics.Matter.Components.Transform | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-components-transform

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.Components.Transform
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.Components.Transform
Scope: static
Source: src/physics/matter-js/components/Transform.js#L17
Since: 3.0.0
Static functions ​
angle ​
angle: number ​
Description:
Use angle to set or get rotation of the physics body associated to this GameObject.
Unlike rotation, when using set the value can be in degrees, which will be converted to radians internally.
Source: src/physics/matter-js/components/Transform.js#L171
Since: 3.0.0
rotation ​
rotation: number ​
Description:
Use rotation to set or get the rotation of the physics body associated with this GameObject.
The value when set must be in radians.
Source: src/physics/matter-js/components/Transform.js#L193
Since: 3.0.0
scale ​
scale: number ​
Description:
This is a special setter that allows you to set both the horizontal and vertical scale of this Game Object
to the same value, at the same time. When reading this value the result returned is (scaleX + scaleY) / 2 .
Use of this property implies you wish the horizontal and vertical scales to be equal to each other. If this
isn't the case, use the scaleX or scaleY properties instead.
Source: src/physics/matter-js/components/Transform.js#L71
Since: 3.88.0
scaleX ​
scaleX: number ​
Description:
The horizontal scale of this Game Object.
Source: src/physics/matter-js/components/Transform.js#L96
Since: 3.0.0
scaleY ​
scaleY: number ​
Description:
The vertical scale of this Game Object.
Source: src/physics/matter-js/components/Transform.js#L134
Since: 3.0.0
x ​
x: number ​
Description:
The x position of this Game Object.
Source: src/physics/matter-js/components/Transform.js#L25
Since: 3.0.0
y ​
y: number ​
Description:
The y position of this Game Object.
Source: src/physics/matter-js/components/Transform.js#L48
Since: 3.0.0
Static functions ​
setAngle ​
<instance> setAngle([degrees]) ​
Description:
Immediately sets the angle of the Body.
Angular velocity, position, force etc. are unchanged.
Parameters:
name type optional default description
degrees number Yes 0 The angle to set, in degrees.
Returns: Phaser.Physics.Matter.Components.Transform - This Game Object instance.
Source: src/physics/matter-js/components/Transform.js#L280
Since: 3.0.0
setFixedRotation ​
<instance> setFixedRotation() ​
Description:
Setting fixed rotation sets the Body inertia to Infinity, which stops it
from being able to rotate when forces are applied to it.
Returns: Phaser.Physics.Matter.Components.Transform - This Game Object instance.
Source: src/physics/matter-js/components/Transform.js#L264
Since: 3.0.0
setPosition ​
<instance> setPosition([x], [y]) ​
Description:
Sets the position of the physics body along x and y axes.
Both the parameters to this function are optional and if not passed any they default to 0.
Velocity, angle, force etc. are unchanged.
Parameters:
name type optional default description
x number Yes 0 The horizontal position of the body.
y number Yes "x" The vertical position of the body.
Returns: Phaser.Physics.Matter.Components.Transform - This Game Object instance.
Source: src/physics/matter-js/components/Transform.js#L217
Since: 3.0.0
setRotation ​
<instance> setRotation([radians]) ​
Description:
Immediately sets the angle of the Body.
Angular velocity, position, force etc. are unchanged.
Parameters:
name type optional default description
radians number Yes 0 The angle of the body, in radians.
Returns: Phaser.Physics.Matter.Components.Transform - This Game Object instance.
Source: src/physics/matter-js/components/Transform.js#L242
Since: 3.0.0
setScale ​
<instance> setScale([x], [y], [point]) ​
Description:
Sets the scale of this Game Object.
Parameters:
name type optional default description
x number Yes 1 The horizontal scale of this Game Object.
y number Yes "x" The vertical scale of this Game Object. If not set it will use the x value.
point Phaser.Math.Vector2 Yes The point (Vector2) from which scaling will occur.
Returns: Phaser.Physics.Matter.Components.Transform - This Game Object instance.
Source: src/physics/matter-js/components/Transform.js#L302
Since: 3.0.0
Previous
Phaser.Physics.Matter.Components.Static
Next
Phaser.Physics.Matter.Components.Velocity
Static functions
angle
rotation
scale
scaleX
scaleY
x
y
Static functions
setAngle
setFixedRotation
setPosition
setRotation
setScale
