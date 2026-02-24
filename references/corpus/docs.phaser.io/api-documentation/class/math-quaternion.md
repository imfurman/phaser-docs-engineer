# Quaternion | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/math-quaternion

Phaser API Documentation
Class
Quaternion
Version: Phaser v3.90.0
On this page
Quaternion
A quaternion.
Constructor
new Quaternion([x], [y], [z], [w])
Parameters
name type optional default description
x number Yes 0 The x component.
y number Yes 0 The y component.
z number Yes 0 The z component.
w number Yes 1 The w component.
Scope : static
Source: src/math/Quaternion.js#L27
Since: 3.0.0
Public Members ​
onChangeCallback ​
onChangeCallback: function ​
Description:
This callback is invoked, if set, each time a value in this quaternion is changed.
The callback is passed one argument, a reference to this quaternion.
Source: src/math/Quaternion.js#L87
Since: 3.50.0
w ​
w: number ​
Description:
The w component of this Quaternion.
Source: src/math/Quaternion.js#L166
Since: 3.0.0
x ​
x: number ​
Description:
The x component of this Quaternion.
Source: src/math/Quaternion.js#L100
Since: 3.0.0
y ​
y: number ​
Description:
The y component of this Quaternion.
Source: src/math/Quaternion.js#L122
Since: 3.0.0
z ​
z: number ​
Description:
The z component of this Quaternion.
Source: src/math/Quaternion.js#L144
Since: 3.0.0
Public Methods ​
add ​
<instance> add(v) ​
Description:
Add a given Quaternion or Vector to this Quaternion. Addition is component-wise.
Parameters:
name type optional description
v Phaser.Math.Quaternion | Phaser.Math.Vector4 No The Quaternion or Vector to add to this Quaternion.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L244
Since: 3.0.0
calculateW ​
<instance> calculateW() ​
Description:
Create a unit (or rotation) Quaternion from its x, y, and z components.
Sets the w component.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L763
Since: 3.0.0
conjugate ​
<instance> conjugate() ​
Description:
Convert this Quaternion into its conjugate.
Sets the x, y and z components.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L652
Since: 3.0.0
copy ​
<instance> copy(src) ​
Description:
Copy the components of a given Quaternion or Vector into this Quaternion.
Parameters:
name type optional description
src Phaser.Math.Quaternion | Phaser.Math.Vector4 No The Quaternion or Vector to copy the components from.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L188
Since: 3.0.0
dot ​
<instance> dot(v) ​
Description:
Calculate the dot product of this Quaternion and the given Quaternion or Vector.
Parameters:
name type optional description
v Phaser.Math.Quaternion | Phaser.Math.Vector4 No The Quaternion or Vector to dot product with this Quaternion.
Returns: number - The dot product of this Quaternion and the given Quaternion or Vector.
Source: src/math/Quaternion.js#L377
Since: 3.0.0
fromMat3 ​
<instance> fromMat3(mat) ​
Description:
Convert the given Matrix into this Quaternion.
Parameters:
name type optional description
mat Phaser.Math.Matrix3 No The Matrix to convert from.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L968
Since: 3.0.0
identity ​
<instance> identity() ​
Description:
Reset this Matrix to an identity (default) Quaternion.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L495
Since: 3.0.0
invert ​
<instance> invert() ​
Description:
Invert this Quaternion.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L626
Since: 3.0.0
length ​
<instance> length() ​
Description:
Calculate the length of this Quaternion.
Returns: number - The length of this Quaternion.
Source: src/math/Quaternion.js#L310
Since: 3.0.0
lengthSq ​
<instance> lengthSq() ​
Description:
Calculate the length of this Quaternion squared.
Returns: number - The length of this Quaternion, squared.
Source: src/math/Quaternion.js#L328
Since: 3.0.0
lerp ​
<instance> lerp(v, [t]) ​
Description:
Linearly interpolate this Quaternion towards the given Quaternion or Vector.
Parameters:
name type optional default description
v Phaser.Math.Quaternion | Phaser.Math.Vector4 No The Quaternion or Vector to interpolate towards.
t number Yes 0 The percentage of interpolation.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L392
Since: 3.0.0
multiply ​
<instance> multiply(b) ​
Description:
Multiply this Quaternion by the given Quaternion or Vector.
Parameters:
name type optional description
b Phaser.Math.Quaternion | Phaser.Math.Vector4 No The Quaternion or Vector to multiply this Quaternion by.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L533
Since: 3.0.0
normalize ​
<instance> normalize() ​
Description:
Normalize this Quaternion.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L346
Since: 3.0.0
rotateX ​
<instance> rotateX(rad) ​
Description:
Rotate this Quaternion on the X axis.
Parameters:
name type optional description
rad number No The rotation angle in radians.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L673
Since: 3.0.0
rotateY ​
<instance> rotateY(rad) ​
Description:
Rotate this Quaternion on the Y axis.
Parameters:
name type optional description
rad number No The rotation angle in radians.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L703
Since: 3.0.0
rotateZ ​
<instance> rotateZ(rad) ​
Description:
Rotate this Quaternion on the Z axis.
Parameters:
name type optional description
rad number No The rotation angle in radians.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L733
Since: 3.0.0
rotationTo ​
<instance> rotationTo(a, b) ​
Description:
Rotates this Quaternion based on the two given vectors.
Parameters:
name type optional description
a Phaser.Math.Vector3 No The transform rotation vector.
b Phaser.Math.Vector3 No The target rotation vector.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L420
Since: 3.0.0
scale ​
<instance> scale(scale) ​
Description:
Scale this Quaternion by the given value.
Parameters:
name type optional description
scale number No The value to scale this Quaternion by.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L288
Since: 3.0.0
set ​
<instance> set([x], [y], [z], [w], [update]) ​
Description:
Set the components of this Quaternion and optionally call the onChangeCallback .
Parameters:
name type optional default description
x number | object Yes 0 The x component, or an object containing x, y, z, and w components.
y number Yes 0 The y component.
z number Yes 0 The z component.
w number Yes 0 The w component.
update boolean Yes true Call the onChangeCallback ?
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L203
Since: 3.0.0
setAxes ​
<instance> setAxes(view, right, up) ​
Description:
Set the axes of this Quaternion.
Parameters:
name type optional description
view Phaser.Math.Vector3 No The view axis.
right Phaser.Math.Vector3 No The right axis.
up Phaser.Math.Vector3 No The upwards axis.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L464
Since: 3.0.0
setAxisAngle ​
<instance> setAxisAngle(axis, rad) ​
Description:
Set the axis angle of this Quaternion.
Parameters:
name type optional description
axis Phaser.Math.Vector3 No The axis.
rad number No The angle in radians.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L508
Since: 3.0.0
setFromEuler ​
<instance> setFromEuler(euler, [update]) ​
Description:
Set this Quaternion from the given Euler, based on Euler order.
Parameters:
name type optional default description
euler Phaser.Math.Euler No The Euler to convert from.
update boolean Yes true Run the onChangeCallback ?
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L784
Since: 3.50.0
setFromRotationMatrix ​
<instance> setFromRotationMatrix(mat4) ​
Description:
Sets the rotation of this Quaternion from the given Matrix4.
Parameters:
name type optional description
mat4 Phaser.Math.Matrix4 No The Matrix4 to set the rotation from.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L893
Since: 3.50.0
slerp ​
<instance> slerp(b, t) ​
Description:
Smoothly linearly interpolate this Quaternion towards the given Quaternion or Vector.
Parameters:
name type optional description
b Phaser.Math.Quaternion | Phaser.Math.Vector4 No The Quaternion or Vector to interpolate towards.
t number No The percentage of interpolation.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L563
Since: 3.0.0
subtract ​
<instance> subtract(v) ​
Description:
Subtract a given Quaternion or Vector from this Quaternion. Subtraction is component-wise.
Parameters:
name type optional description
v Phaser.Math.Quaternion | Phaser.Math.Vector4 No The Quaternion or Vector to subtract from this Quaternion.
Returns: Phaser.Math.Quaternion - This Quaternion.
Source: src/math/Quaternion.js#L266
Since: 3.0.0
Previous
Matrix4
Next
RandomDataGenerator
Public Members
onChangeCallback
w
x
y
z
Public Methods
add
calculateW
conjugate
copy
dot
fromMat3
identity
invert
length
lengthSq
lerp
multiply
normalize
rotateX
rotateY
rotateZ
rotationTo
scale
set
setAxes
setAxisAngle
setFromEuler
setFromRotationMatrix
slerp
subtract
