# Phaser.Math | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/math

Phaser API Documentation
Namespaces
Phaser.Math
Version: Phaser v3.90.0
On this page
Phaser.Math
Scope: static
Source: src/math/index.js#L10
Static functions ​
Euler
Matrix3
Matrix4
Quaternion
RandomDataGenerator
Vector2
Vector3
Vector4
Static functions ​
Average ​
<static> Average(values) ​
Description:
Calculate the mean average of the given values.
Parameters:
name type optional description
values Array.<number> No The values to average.
Returns: number - The average value.
Source: src/math/Average.js#L7
Since: 3.0.0
Bernstein ​
<static> Bernstein(n, i) ​
Description:
Calculates the Bernstein basis from the three factorial coefficients.
Parameters:
name type optional description
n number No The first value.
i number No The second value.
Returns: number - The Bernstein basis of Factorial(n) / Factorial(i) / Factorial(n - i)
Source: src/math/Bernstein.js#L9
Since: 3.0.0
Between ​
<static> Between(min, max) ​
Description:
Compute a random integer between the min and max values, inclusive.
Parameters:
name type optional description
min number No The minimum value.
max number No The maximum value.
Returns: number - The random integer.
Source: src/math/Between.js#L7
Since: 3.0.0
CatmullRom ​
<static> CatmullRom(t, p0, p1, p2, p3) ​
Description:
Calculates a Catmull-Rom value from the given points, based on an alpha of 0.5.
Parameters:
name type optional description
t number No The amount to interpolate by.
p0 number No The first control point.
p1 number No The second control point.
p2 number No The third control point.
p3 number No The fourth control point.
Returns: number - The Catmull-Rom value.
Source: src/math/CatmullRom.js#L7
Since: 3.0.0
CeilTo ​
<static> CeilTo(value, [place], [base]) ​
Description:
Ceils to some place comparative to a base , default is 10 for decimal place.
The place is represented by the power applied to base to get that place.
Parameters:
name type optional default description
value number No The value to round.
place number Yes 0 The place to round to.
base number Yes 10 The base to round in. Default is 10 for decimal.
Returns: number - The rounded value.
Source: src/math/CeilTo.js#L7
Since: 3.0.0
Clamp ​
<static> Clamp(value, min, max) ​
Description:
Force a value within the boundaries by clamping it to the range min , max .
Parameters:
name type optional description
value number No The value to be clamped.
min number No The minimum bounds.
max number No The maximum bounds.
Returns: number - The clamped value.
Source: src/math/Clamp.js#L7
Since: 3.0.0
DegToRad ​
<static> DegToRad(degrees) ​
Description:
Convert the given angle from degrees, to the equivalent angle in radians.
Parameters:
name type optional description
degrees number No The angle (in degrees) to convert to radians.
Returns: number - The given angle converted to radians.
Source: src/math/DegToRad.js#L9
Since: 3.0.0
Difference ​
<static> Difference(a, b) ​
Description:
Calculates the positive difference of two given numbers.
Parameters:
name type optional description
a number No The first number in the calculation.
b number No The second number in the calculation.
Returns: number - The positive difference of the two given numbers.
Source: src/math/Difference.js#L7
Since: 3.0.0
Factorial ​
<static> Factorial(value) ​
Description:
Calculates the factorial of a given number for integer values greater than 0.
Parameters:
name type optional description
value number No A positive integer to calculate the factorial of.
Returns: number - The factorial of the given number.
Source: src/math/Factorial.js#L7
Since: 3.0.0
FloatBetween ​
<static> FloatBetween(min, max) ​
Description:
Generate a random floating point number between the two given bounds, minimum inclusive, maximum exclusive.
Parameters:
name type optional description
min number No The lower bound for the float, inclusive.
max number No The upper bound for the float exclusive.
Returns: number - A random float within the given range.
Source: src/math/FloatBetween.js#L7
Since: 3.0.0
FloorTo ​
<static> FloorTo(value, [place], [base]) ​
Description:
Floors to some place comparative to a base , default is 10 for decimal place.
The place is represented by the power applied to base to get that place.
Parameters:
name type optional default description
value number No The value to round.
place number Yes 0 The place to round to.
base number Yes 10 The base to round in. Default is 10 for decimal.
Returns: number - The rounded value.
Source: src/math/FloorTo.js#L7
Since: 3.0.0
FromPercent ​
<static> FromPercent(percent, min, [max]) ​
Description:
Return a value based on the range between min and max and the percentage given.
Parameters:
name type optional description
percent number No A value between 0 and 1 representing the percentage.
min number No The minimum value.
max number Yes The maximum value.
Returns: number - The value that is percent percent between min and max .
Source: src/math/FromPercent.js#L9
Since: 3.0.0
GetSpeed ​
<static> GetSpeed(distance, time) ​
Description:
Calculate a per-ms speed from a distance and time (given in seconds).
Parameters:
name type optional description
distance number No The distance.
time number No The time, in seconds.
Returns: number - The speed, in distance per ms.
Source: src/math/GetSpeed.js#L7
Since: 3.0.0
IsEven ​
<static> IsEven(value) ​
Description:
Check if a given value is an even number.
Parameters:
name type optional description
value number No The number to perform the check with.
Returns: boolean - Whether the number is even or not.
Source: src/math/IsEven.js#L7
Since: 3.0.0
IsEvenStrict ​
<static> IsEvenStrict(value) ​
Description:
Check if a given value is an even number using a strict type check.
Parameters:
name type optional description
value number No The number to perform the check with.
Returns: boolean - Whether the number is even or not.
Source: src/math/IsEvenStrict.js#L7
Since: 3.0.0
Linear ​
<static> Linear(p0, p1, t) ​
Description:
Calculates a linear (interpolation) value over t.
Parameters:
name type optional description
p0 number No The first point.
p1 number No The second point.
t number No The percentage between p0 and p1 to return, represented as a number between 0 and 1.
Returns: number - The step t% of the way between p0 and p1.
Source: src/math/Linear.js#L7
Since: 3.0.0
LinearXY ​
<static> LinearXY(vector1, vector2, [t]) ​
Description:
Interpolates two given Vectors and returns a new Vector between them.
Does not modify either of the passed Vectors.
Parameters:
name type optional default description
vector1 Phaser.Math.Vector2 No Starting vector
vector2 Phaser.Math.Vector2 No Ending vector
t number Yes 0 The percentage between vector1 and vector2 to return, represented as a number between 0 and 1.
Returns: Phaser.Math.Vector2 - The step t% of the way between vector1 and vector2.
Source: src/math/LinearXY.js#L7
Since: 3.60.0
MaxAdd ​
<static> MaxAdd(value, amount, max) ​
Description:
Add an amount to a value , limiting the maximum result to max .
Parameters:
name type optional description
value number No The value to add to.
amount number No The amount to add.
max number No The maximum value to return.
Returns: number - The resulting value.
Source: src/math/MaxAdd.js#L7
Since: 3.0.0
Median ​
<static> Median(values) ​
Description:
Calculate the median of the given values. The values are sorted and the middle value is returned.
In case of an even number of values, the average of the two middle values is returned.
Parameters:
name type optional description
values Array.<number> No The values to average.
Returns: number - The median value.
Source: src/math/Median.js#L7
Since: 3.54.0
MinSub ​
<static> MinSub(value, amount, min) ​
Description:
Subtract an amount from value , limiting the minimum result to min .
Parameters:
name type optional description
value number No The value to subtract from.
amount number No The amount to subtract.
min number No The minimum value to return.
Returns: number - The resulting value.
Source: src/math/MinSub.js#L7
Since: 3.0.0
Percent ​
<static> Percent(value, min, [max], [upperMax]) ​
Description:
Work out what percentage value is of the range between min and max .
If max isn't given then it will return the percentage of value to min .
You can optionally specify an upperMax value, which is a mid-way point in the range that represents 100%, after which the % starts to go down to zero again.
Parameters:
name type optional description
value number No The value to determine the percentage of.
min number No The minimum value.
max number Yes The maximum value.
upperMax number Yes The mid-way point in the range that represents 100%.
Returns: number - A value between 0 and 1 representing the percentage.
Source: src/math/Percent.js#L7
Since: 3.0.0
RadToDeg ​
<static> RadToDeg(radians) ​
Description:
Convert the given angle in radians, to the equivalent angle in degrees.
Parameters:
name type optional description
radians number No The angle in radians to convert ot degrees.
Returns: number - The given angle converted to degrees.
Source: src/math/RadToDeg.js#L9
Since: 3.0.0
RandomXY ​
<static> RandomXY(vector, [scale]) ​
Description:
Compute a random unit vector.
Computes random values for the given vector between -1 and 1 that can be used to represent a direction.
Optionally accepts a scale value to scale the resulting vector by.
Parameters:
name type optional default description
vector Phaser.Math.Vector2 No The Vector to compute random values for.
scale number Yes 1 The scale of the random values.
Returns: Phaser.Math.Vector2 - The given Vector.
Source: src/math/RandomXY.js#L7
Since: 3.0.0
RandomXYZ ​
<static> RandomXYZ(vec3, [radius]) ​
Description:
Compute a random position vector in a spherical area, optionally defined by the given radius.
Parameters:
name type optional default description
vec3 Phaser.Math.Vector3 No The Vector to compute random values for.
radius number Yes 1 The radius.
Returns: Phaser.Math.Vector3 - The given Vector.
Source: src/math/RandomXYZ.js#L7
Since: 3.0.0
RandomXYZW ​
<static> RandomXYZW(vec4, [scale]) ​
Description:
Compute a random four-dimensional vector.
Parameters:
name type optional default description
vec4 Phaser.Math.Vector4 No The Vector to compute random values for.
scale number Yes 1 The scale of the random values.
Returns: Phaser.Math.Vector4 - The given Vector.
Source: src/math/RandomXYZW.js#L7
Since: 3.0.0
Rotate ​
<static> Rotate(point, angle) ​
Description:
Rotate a given point by a given angle around the origin (0, 0), in an anti-clockwise direction.
Parameters:
name type optional description
point Phaser.Geom.Point | object No The point to be rotated.
angle number No The angle to be rotated by in an anticlockwise direction.
Returns: Phaser.Geom.Point - The given point, rotated by the given angle in an anticlockwise direction.
Source: src/math/Rotate.js#L7
Since: 3.0.0
RotateAround ​
<static> RotateAround(point, x, y, angle) ​
Description:
Rotate a point around x and y to the given angle , at the same distance.
In polar notation, this maps a point from (r, t) to (r, angle), vs. the origin (x, y).
Tags:
generic
Parameters:
name type optional description
point Phaser.Geom.Point | object No The point to be rotated.
x number No The horizontal coordinate to rotate around.
y number No The vertical coordinate to rotate around.
angle number No The angle of rotation in radians.
Returns: Phaser.Types.Math.Vector2Like - The given point.
Source: src/math/RotateAround.js#L7
Since: 3.0.0
RotateAroundDistance ​
<static> RotateAroundDistance(point, x, y, angle, distance) ​
Description:
Rotate a point around x and y by the given angle and distance .
In polar notation, this maps a point from (r, t) to (distance, t + angle), vs. the origin (x, y).
Tags:
generic
Parameters:
name type optional description
point Phaser.Geom.Point | object No The point to be rotated.
x number No The horizontal coordinate to rotate around.
y number No The vertical coordinate to rotate around.
angle number No The angle of rotation in radians.
distance number No The distance from (x, y) to place the point at.
Returns: Phaser.Types.Math.Vector2Like - The given point.
Source: src/math/RotateAroundDistance.js#L7
Since: 3.0.0
RotateTo ​
<static> RotateTo(point, x, y, angle, distance) ​
Description:
Position a point at the given angle and distance to ( x , y ).
Tags:
generic
Parameters:
name type optional description
point Phaser.Types.Math.Vector2Like No The point to be positioned.
x number No The horizontal coordinate to position from.
y number No The vertical coordinate to position from.
angle number No The angle of rotation in radians.
distance number No The distance from (x, y) to place the point at.
Returns: Phaser.Types.Math.Vector2Like - The given point.
Source: src/math/RotateTo.js#L7
Since: 3.24.0
RotateVec3 ​
<static> RotateVec3(vec, axis, radians) ​
Description:
Rotates a vector in place by axis angle.
This is the same as transforming a point by an
axis-angle quaternion, but it has higher precision.
Parameters:
name type optional description
vec Phaser.Math.Vector3 No The vector to be rotated.
axis Phaser.Math.Vector3 No The axis to rotate around.
radians number No The angle of rotation in radians.
Returns: Phaser.Math.Vector3 - The given vector.
Source: src/math/RotateVec3.js#L15
Since: 3.0.0
RoundAwayFromZero ​
<static> RoundAwayFromZero(value) ​
Description:
Round a given number so it is further away from zero. That is, positive numbers are rounded up, and negative numbers are rounded down.
Parameters:
name type optional description
value number No The number to round.
Returns: number - The rounded number, rounded away from zero.
Source: src/math/RoundAwayFromZero.js#L7
Since: 3.0.0
RoundTo ​
<static> RoundTo(value, [place], [base]) ​
Description:
Round a value to the given precision.
For example:
RoundTo ( 123.456 , 0 ) = 123
RoundTo ( 123.456 , 1 ) = 120
RoundTo ( 123.456 , 2 ) = 100
To round the decimal, i.e. to round to precision, pass in a negative place :
RoundTo ( 123.456789 , 0 ) = 123
RoundTo ( 123.456789 , - 1 ) = 123.5
RoundTo ( 123.456789 , - 2 ) = 123.46
RoundTo ( 123.456789 , - 3 ) = 123.457
Parameters:
name type optional default description
value number No The value to round.
place number Yes 0 The place to round to. Positive to round the units, negative to round the decimal.
base number Yes 10 The base to round in. Default is 10 for decimal.
Returns: number - The rounded value.
Source: src/math/RoundTo.js#L7
Since: 3.0.0
SinCosTableGenerator ​
<static> SinCosTableGenerator(length, [sinAmp], [cosAmp], [frequency]) ​
Description:
Generate a series of sine and cosine values.
Parameters:
name type optional default description
length number No The number of values to generate.
sinAmp number Yes 1 The sine value amplitude.
cosAmp number Yes 1 The cosine value amplitude.
frequency number Yes 1 The frequency of the values.
Returns: Phaser.Types.Math.SinCosTable - The generated values.
Source: src/math/SinCosTableGenerator.js#L7
Since: 3.0.0
SmootherStep ​
<static> SmootherStep(x, min, max) ​
Description:
Calculate a smoother interpolation percentage of x between min and max .
The function receives the number x as an argument and returns 0 if x is less than or equal to the left edge,
1 if x is greater than or equal to the right edge, and smoothly interpolates, using a Hermite polynomial,
between 0 and 1 otherwise.
Produces an even smoother interpolation than Phaser.Math.SmoothStep .
Parameters:
name type optional description
x number No The input value.
min number No The minimum value, also known as the 'left edge', assumed smaller than the 'right edge'.
max number No The maximum value, also known as the 'right edge', assumed greater than the 'left edge'.
Returns: number - The percentage of interpolation, between 0 and 1.
Source: src/math/SmootherStep.js#L7
Since: 3.0.0
SmoothStep ​
<static> SmoothStep(x, min, max) ​
Description:
Calculate a smooth interpolation percentage of x between min and max .
The function receives the number x as an argument and returns 0 if x is less than or equal to the left edge,
1 if x is greater than or equal to the right edge, and smoothly interpolates, using a Hermite polynomial,
between 0 and 1 otherwise.
Parameters:
name type optional description
x number No The input value.
min number No The minimum value, also known as the 'left edge', assumed smaller than the 'right edge'.
max number No The maximum value, also known as the 'right edge', assumed greater than the 'left edge'.
Returns: number - The percentage of interpolation, between 0 and 1.
Source: src/math/SmoothStep.js#L7
Since: 3.0.0
ToXY ​
<static> ToXY(index, width, height, [out]) ​
Description:
Returns a Vector2 containing the x and y position of the given index in a width x height sized grid.
For example, in a 6 x 4 grid, index 16 would equal x: 4 y: 2.
If the given index is out of range an empty Vector2 is returned.
Parameters:
name type optional description
index number No The position within the grid to get the x/y value for.
width number No The width of the grid.
height number No The height of the grid.
out Phaser.Math.Vector2 Yes An optional Vector2 to store the result in. If not given, a new Vector2 instance will be created.
Returns: Phaser.Math.Vector2 - A Vector2 where the x and y properties contain the given grid index.
Source: src/math/ToXY.js#L9
Since: 3.19.0
TransformXY ​
<static> TransformXY(x, y, positionX, positionY, rotation, scaleX, scaleY, [output]) ​
Description:
Takes the x and y coordinates and transforms them into the same space as
defined by the position, rotation and scale values.
Parameters:
name type optional description
x number No The x coordinate to be transformed.
y number No The y coordinate to be transformed.
positionX number No Horizontal position of the transform point.
positionY number No Vertical position of the transform point.
rotation number No Rotation of the transform point, in radians.
scaleX number No Horizontal scale of the transform point.
scaleY number No Vertical scale of the transform point.
output Phaser.Math.Vector2 | Phaser.Geom.Point object Yes
Returns: Phaser.Math.Vector2 , Phaser.Geom.Point , object - The translated point.
Source: src/math/TransformXY.js#L9
Since: 3.0.0
Within ​
<static> Within(a, b, tolerance) ​
Description:
Checks if the two values are within the given tolerance of each other.
Parameters:
name type optional description
a number No The first value to use in the calculation.
b number No The second value to use in the calculation.
tolerance number No The tolerance. Anything equal to or less than this value is considered as being within range.
Returns: boolean - Returns true if a is less than or equal to the tolerance of b .
Source: src/math/Within.js#L7
Since: 3.0.0
Wrap ​
<static> Wrap(value, min, max) ​
Description:
Wrap the given value between min and max .
Parameters:
name type optional description
value number No The value to wrap.
min number No The minimum value.
max number No The maximum value.
Returns: number - The wrapped value.
Source: src/math/Wrap.js#L7
Since: 3.0.0
Static functions ​
Angle
Distance
Easing
Fuzzy
Interpolation
Pow2
Snap
Static functions ​
DEG_TO_RAD ​
DEG_TO_RAD: number ​
Description:
For converting degrees to radians (PI / 180)
Source: src/math/const.js#L40
Since: 3.0.0
EPSILON ​
EPSILON: number ​
Description:
An epsilon value (1.0e-6)
Source: src/math/const.js#L31
Since: 3.0.0
MAX_SAFE_INTEGER ​
MAX_SAFE_INTEGER: number ​
Description:
The maximum safe integer this browser supports.
We use a const for backward compatibility with Internet Explorer.
Source: src/math/const.js#L78
Since: 3.21.0
MIN_SAFE_INTEGER ​
MIN_SAFE_INTEGER: number ​
Description:
The minimum safe integer this browser supports.
We use a const for backward compatibility with Internet Explorer.
Source: src/math/const.js#L68
Since: 3.21.0
PI2 ​
PI2: number ​
Description:
The value of PI * 2.
Source: src/math/const.js#L9
Since: 3.0.0
RAD_TO_DEG ​
RAD_TO_DEG: number ​
Description:
For converting radians to degrees (180 / PI)
Source: src/math/const.js#L49
Since: 3.0.0
RND ​
RND: Phaser.Math.RandomDataGenerator ​
Description:
An instance of the Random Number Generator.
This is not set until the Game boots.
Source: src/math/const.js#L58
Since: 3.0.0
TAU ​
TAU: number ​
Description:
The value of PI * 0.5.
Yes, we understand that this should actually be PI * 2, but
it has been like this for so long we can't change it now.
If you need PI * 2, use the PI2 constant instead.
Source: src/math/const.js#L18
Since: 3.0.0
Previous
Phaser.Math.Snap
Next
Phaser.Physics.Arcade.Components.Acceleration
Static functions
Static functions
Average
Bernstein
Between
CatmullRom
CeilTo
Clamp
DegToRad
Difference
Factorial
FloatBetween
FloorTo
FromPercent
GetSpeed
IsEven
IsEvenStrict
Linear
LinearXY
MaxAdd
Median
MinSub
Percent
RadToDeg
RandomXY
RandomXYZ
RandomXYZW
Rotate
RotateAround
RotateAroundDistance
RotateTo
RotateVec3
RoundAwayFromZero
RoundTo
SinCosTableGenerator
SmootherStep
SmoothStep
ToXY
TransformXY
Within
Wrap
Static functions
Static functions
DEG_TO_RAD
EPSILON
MAX_SAFE_INTEGER
MIN_SAFE_INTEGER
PI2
RAD_TO_DEG
RND
TAU
