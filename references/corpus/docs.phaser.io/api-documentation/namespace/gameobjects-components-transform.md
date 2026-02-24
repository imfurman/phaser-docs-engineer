# Phaser.GameObjects.Components.Transform | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-transform

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Transform
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Transform
Scope: static
Source: src/gameobjects/components/Transform.js#L17
Since: 3.0.0
Static functions ​
angle ​
angle: number ​
Description:
The angle of this Game Object as expressed in degrees.
Phaser uses a right-hand clockwise rotation system, where 0 is right, 90 is down, 180/-180 is left
and -90 is up.
If you prefer to work in radians, see the rotation property instead.
Source: src/gameobjects/components/Transform.js#L211
Since: 3.0.0
hasTransformComponent ​
hasTransformComponent: boolean ​
Description:
A property indicating that a Game Object has this component.
Source: src/gameobjects/components/Transform.js#L26
Since: 3.60.0
rotation ​
rotation: number ​
Description:
The angle of this Game Object in radians.
Phaser uses a right-hand clockwise rotation system, where 0 is right, PI/2 is down, +-PI is left
and -PI/2 is up.
If you prefer to work in degrees, see the angle property instead.
Source: src/gameobjects/components/Transform.js#L238
Since: 3.0.0
scale ​
scale: number ​
Description:
This is a special setter that allows you to set both the horizontal and vertical scale of this Game Object
to the same value, at the same time. When reading this value the result returned is (scaleX + scaleY) / 2 .
Use of this property implies you wish the horizontal and vertical scales to be equal to each other. If this
isn't the case, use the scaleX or scaleY properties instead.
Source: src/gameobjects/components/Transform.js#L113
Since: 3.18.0
scaleX ​
scaleX: number ​
Description:
The horizontal scale of this Game Object.
Source: src/gameobjects/components/Transform.js#L149
Since: 3.0.0
scaleY ​
scaleY: number ​
Description:
The vertical scale of this Game Object.
Source: src/gameobjects/components/Transform.js#L180
Since: 3.0.0
w ​
w: number ​
Description:
The w position of this Game Object.
Source: src/gameobjects/components/Transform.js#L103
Since: 3.0.0
x ​
x: number ​
Description:
The x position of this Game Object.
Source: src/gameobjects/components/Transform.js#L70
Since: 3.0.0
y ​
y: number ​
Description:
The y position of this Game Object.
Source: src/gameobjects/components/Transform.js#L80
Since: 3.0.0
z ​
z: number ​
Description:
The z position of this Game Object.
Note: The z position does not control the rendering order of 2D Game Objects. Use
Phaser.GameObjects.Components.Depth#depth instead.
Source: src/gameobjects/components/Transform.js#L90
Since: 3.0.0
Static functions ​
copyPosition ​
<instance> copyPosition(source) ​
Description:
Copies an object's coordinates to this Game Object's position.
Parameters:
name type optional description
source Phaser.Types.Math.Vector2Like | Phaser.Types.Math.Vector3Like Phaser.Types.Math.Vector4Like No
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L293
Since: 3.50.0
getLocalPoint ​
<instance> getLocalPoint(x, y, [point], [camera]) ​
Description:
Takes the given x and y coordinates and converts them into local space for this
Game Object, taking into account parent and local transforms, and the Display Origin.
The returned Vector2 contains the translated point in its properties.
A Camera needs to be provided in order to handle modified scroll factors. If no
camera is specified, it will use the main camera from the Scene to which this
Game Object belongs.
Parameters:
name type optional description
x number No The x position to translate.
y number No The y position to translate.
point Phaser.Math.Vector2 Yes A Vector2, or point-like object, to store the results in.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera which is being tested against. If not given will use the Scene default camera.
Returns: Phaser.Math.Vector2 - The translated point.
Source: src/gameobjects/components/Transform.js#L551
Since: 3.50.0
getLocalTransformMatrix ​
<instance> getLocalTransformMatrix([tempMatrix]) ​
Description:
Gets the local transform matrix for this Game Object.
Parameters:
name type optional description
tempMatrix Phaser.GameObjects.Components.TransformMatrix Yes The matrix to populate with the values from this Game Object.
Returns: Phaser.GameObjects.Components.TransformMatrix - The populated Transform Matrix.
Source: src/gameobjects/components/Transform.js#L484
Since: 3.4.0
getParentRotation ​
<instance> getParentRotation() ​
Description:
Gets the sum total rotation of all of this Game Objects parent Containers.
The returned value is in radians and will be zero if this Game Object has no parent container.
Returns: number - The sum total rotation, in radians, of all parent containers of this Game Object.
Source: src/gameobjects/components/Transform.js#L635
Since: 3.18.0
getWorldPoint ​
<instance> getWorldPoint([point], [tempMatrix], [parentMatrix]) ​
Description:
Gets the world position of this Game Object, factoring in any parent Containers.
Parameters:
name type optional description
point Phaser.Math.Vector2 Yes A Vector2, or point-like object, to store the result in.
tempMatrix Phaser.GameObjects.Components.TransformMatrix Yes A temporary matrix to hold the Game Object's values.
parentMatrix Phaser.GameObjects.Components.TransformMatrix Yes A temporary matrix to hold parent values.
Returns: Phaser.Math.Vector2 - The world position of this Game Object.
Source: src/gameobjects/components/Transform.js#L601
Since: 3.88.0
getWorldTransformMatrix ​
<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix]) ​
Description:
Gets the world transform matrix for this Game Object, factoring in any parent Containers.
Parameters:
name type optional description
tempMatrix Phaser.GameObjects.Components.TransformMatrix Yes The matrix to populate with the values from this Game Object.
parentMatrix Phaser.GameObjects.Components.TransformMatrix Yes A temporary matrix to hold parent values during the calculations.
Returns: Phaser.GameObjects.Components.TransformMatrix - The populated Transform Matrix.
Source: src/gameobjects/components/Transform.js#L501
Since: 3.4.0
setAngle ​
<instance> setAngle([degrees]) ​
Description:
Sets the angle of this Game Object.
Parameters:
name type optional default description
degrees number Yes 0 The rotation of this Game Object, in degrees.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L364
Since: 3.0.0
setPosition ​
<instance> setPosition([x], [y], [z], [w]) ​
Description:
Sets the position of this Game Object.
Parameters:
name type optional default description
x number Yes 0 The x position of this Game Object.
y number Yes "x" The y position of this Game Object. If not set it will use the x value.
z number Yes 0 The z position of this Game Object.
w number Yes 0 The w position of this Game Object.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L265
Since: 3.0.0
setRandomPosition ​
<instance> setRandomPosition([x], [y], [width], [height]) ​
Description:
Sets the position of this Game Object to be a random position within the confines of
the given area.
If no area is specified a random position between 0 x 0 and the game width x height is used instead.
The position does not factor in the size of this Game Object, meaning that only the origin is
guaranteed to be within the area.
Parameters:
name type optional default description
x number Yes 0 The x position of the top-left of the random area.
y number Yes 0 The y position of the top-left of the random area.
width number Yes The width of the random area.
height number Yes The height of the random area.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L313
Since: 3.8.0
setRotation ​
<instance> setRotation([radians]) ​
Description:
Sets the rotation of this Game Object.
Parameters:
name type optional default description
radians number Yes 0 The rotation of this Game Object, in radians.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L345
Since: 3.0.0
setScale ​
<instance> setScale([x], [y]) ​
Description:
Sets the scale of this Game Object.
Parameters:
name type optional default description
x number Yes 1 The horizontal scale of this Game Object.
y number Yes "x" The vertical scale of this Game Object. If not set it will use the x value.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L383
Since: 3.0.0
setW ​
<instance> setW([value]) ​
Description:
Sets the w position of this Game Object.
Parameters:
name type optional default description
value number Yes 0 The w position of this Game Object.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L465
Since: 3.0.0
setX ​
<instance> setX([value]) ​
Description:
Sets the x position of this Game Object.
Parameters:
name type optional default description
value number Yes 0 The x position of this Game Object.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L405
Since: 3.0.0
setY ​
<instance> setY([value]) ​
Description:
Sets the y position of this Game Object.
Parameters:
name type optional default description
value number Yes 0 The y position of this Game Object.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L424
Since: 3.0.0
setZ ​
<instance> setZ([value]) ​
Description:
Sets the z position of this Game Object.
Note: The z position does not control the rendering order of 2D Game Objects. Use
Phaser.GameObjects.Components.Depth#setDepth instead.
Parameters:
name type optional default description
value number Yes 0 The z position of this Game Object.
Returns: Phaser.GameObjects.Components.Transform - This Game Object instance.
Source: src/gameobjects/components/Transform.js#L443
Since: 3.0.0
Previous
Phaser.GameObjects.Components.Tint
Next
Phaser.GameObjects.Components.Visible
Static functions
angle
hasTransformComponent
rotation
scale
scaleX
scaleY
w
x
y
z
Static functions
copyPosition
getLocalPoint
getLocalTransformMatrix
getParentRotation
getWorldPoint
getWorldTransformMatrix
setAngle
setPosition
setRandomPosition
setRotation
setScale
setW
setX
setY
setZ
