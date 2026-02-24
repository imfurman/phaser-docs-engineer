# Phaser.Math.Angle | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/math-angle

Phaser API Documentation
Namespaces
Phaser.Math.Angle
Version: Phaser v3.90.0
On this page
Phaser.Math.Angle
Scope: static
Source: src/math/angle/index.js#L7
Static functions ​
Between ​
<static> Between(x1, y1, x2, y2) ​
Description:
Find the angle of a segment from (x1, y1) -> (x2, y2).
Parameters:
name type optional description
x1 number No The x coordinate of the first point.
y1 number No The y coordinate of the first point.
x2 number No The x coordinate of the second point.
y2 number No The y coordinate of the second point.
Returns: number - The angle in radians.
Source: src/math/angle/Between.js#L7
Since: 3.0.0
BetweenPoints ​
<static> BetweenPoints(point1, point2) ​
Description:
Find the angle of a segment from (point1.x, point1.y) -> (point2.x, point2.y).
Calculates the angle of the vector from the first point to the second point.
Parameters:
name type optional description
point1 Phaser.Types.Math.Vector2Like No The first point.
point2 Phaser.Types.Math.Vector2Like No The second point.
Returns: number - The angle in radians.
Source: src/math/angle/BetweenPoints.js#L7
Since: 3.0.0
BetweenPointsY ​
<static> BetweenPointsY(point1, point2) ​
Description:
Find the angle of a segment from (point1.x, point1.y) -> (point2.x, point2.y).
The difference between this method and Phaser.Math.Angle.BetweenPoints is that this assumes the y coordinate
travels down the screen.
Parameters:
name type optional description
point1 Phaser.Types.Math.Vector2Like No The first point.
point2 Phaser.Types.Math.Vector2Like No The second point.
Returns: number - The angle in radians.
Source: src/math/angle/BetweenPointsY.js#L7
Since: 3.0.0
BetweenY ​
<static> BetweenY(x1, y1, x2, y2) ​
Description:
Find the angle of a segment from (x1, y1) -> (x2, y2).
The difference between this method and Phaser.Math.Angle.Between is that this assumes the y coordinate
travels down the screen.
Parameters:
name type optional description
x1 number No The x coordinate of the first point.
y1 number No The y coordinate of the first point.
x2 number No The x coordinate of the second point.
y2 number No The y coordinate of the second point.
Returns: number - The angle in radians.
Source: src/math/angle/BetweenY.js#L7
Since: 3.0.0
CounterClockwise ​
<static> CounterClockwise(angle) ​
Description:
Takes an angle in Phasers default clockwise format and converts it so that
0 is North, 90 is West, 180 is South and 270 is East,
therefore running counter-clockwise instead of clockwise.
You can pass in the angle from a Game Object using:
var converted = CounterClockwise ( gameobject . rotation ) ;
All values for this function are in radians.
Parameters:
name type optional description
angle number No The angle to convert, in radians.
Returns: number - The converted angle, in radians.
Source: src/math/angle/CounterClockwise.js#L9
Since: 3.16.0
GetClockwiseDistance ​
<static> GetClockwiseDistance(angle1, angle2) ​
Description:
Gets the shortest nonnegative angular distance from angle1 to angle2.
Parameters:
name type optional description
angle1 number No The starting angle in radians.
angle2 number No The target angle in radians.
Returns: number - The distance in radians, in the range [0, 2pi).
Source: src/math/angle/GetClockwiseDistance.js#L9
Since: 4.0.0
GetCounterClockwiseDistance ​
<static> GetCounterClockwiseDistance(angle1, angle2) ​
Description:
Gets the shortest nonpositive angular distance from angle1 to angle2.
Parameters:
name type optional description
angle1 number No The starting angle in radians.
angle2 number No The target angle in radians.
Returns: number - The distance in radians, in the range (-2pi, 0].
Source: src/math/angle/GetCounterClockwiseDistance.js#L11
Since: 4.0.0
GetShortestDistance ​
<static> GetShortestDistance(angle1, angle2) ​
Description:
Gets the shortest signed angular distance from angle1 to angle2.
A positive distance is a clockwise rotation.
A negative distance is a counter-clockwise rotation.
For calculation in degrees use Phaser.Math.Angle.ShortestBetween instead.
Parameters:
name type optional description
angle1 number No The first angle in radians.
angle2 number No The second angle in radians.
Returns: number - The distance in radians, in the range [-pi, pi).
Source: src/math/angle/GetShortestDistance.js#L9
Since: 4.0.0
Normalize ​
<static> Normalize(angle) ​
Description:
Normalize an angle to the [0, 2pi] range.
Parameters:
name type optional description
angle number No The angle to normalize, in radians.
Returns: number - The normalized angle, in radians.
Source: src/math/angle/Normalize.js#L7
Since: 3.0.0
Random ​
<static> Random() ​
Description:
Returns a random angle in the range [-pi, pi].
Returns: number - The angle, in radians.
Source: src/math/angle/Random.js#L10
Since: 3.23.0
RandomDegrees ​
<static> RandomDegrees() ​
Description:
Returns a random angle in the range [-180, 180].
Returns: number - The angle, in degrees.
Source: src/math/angle/RandomDegrees.js#L10
Since: 3.23.0
Reverse ​
<static> Reverse(angle) ​
Description:
Reverse the given angle.
Parameters:
name type optional description
angle number No The angle to reverse, in radians.
Returns: number - The reversed angle, in radians.
Source: src/math/angle/Reverse.js#L9
Since: 3.0.0
RotateTo ​
<static> RotateTo(currentAngle, targetAngle, [lerp]) ​
Description:
Rotates currentAngle towards targetAngle , taking the shortest rotation distance. The lerp argument is the amount to rotate by in this call.
Parameters:
name type optional default description
currentAngle number No The current angle, in radians.
targetAngle number No The target angle to rotate to, in radians.
lerp number Yes 0.05 The lerp value to add to the current angle.
Returns: number - The adjusted angle.
Source: src/math/angle/RotateTo.js#L9
Since: 3.0.0
ShortestBetween ​
<static> ShortestBetween(angle1, angle2) ​
Description:
Gets the shortest angle between angle1 and angle2 .
Both angles must be in the range -180 to 180, which is the same clamped
range that sprite.angle uses, so you can pass in two sprite angles to
this method and get the shortest angle back between the two of them.
The angle returned will be in the same range. If the returned angle is
greater than 0 then it's a counter-clockwise rotation, if < 0 then it's
a clockwise rotation.
For calculation in radians use Phaser.Math.Angle.GetShortestDistance instead.
Parameters:
name type optional description
angle1 number No The first angle in the range -180 to 180.
angle2 number No The second angle in the range -180 to 180.
Returns: number - The shortest angle, in degrees. If greater than zero it's a counter-clockwise rotation.
Source: src/math/angle/ShortestBetween.js#L7
Since: 3.0.0
Wrap ​
<static> Wrap(angle) ​
Description:
Wrap an angle.
Wraps the angle to a value in the range of -PI to PI.
Parameters:
name type optional description
angle number No The angle to wrap, in radians.
Returns: number - The wrapped angle, in radians.
Source: src/math/angle/Wrap.js#L9
Since: 3.0.0
WrapDegrees ​
<static> WrapDegrees(angle) ​
Description:
Wrap an angle in degrees.
Wraps the angle to a value in the range of -180 to 180.
Parameters:
name type optional description
angle number No The angle to wrap, in degrees.
Returns: number - The wrapped angle, in degrees.
Source: src/math/angle/WrapDegrees.js#L9
Since: 3.0.0
Previous
Phaser.Loader
Next
Phaser.Math.Distance
Static functions
Between
BetweenPoints
BetweenPointsY
BetweenY
CounterClockwise
GetClockwiseDistance
GetCounterClockwiseDistance
GetShortestDistance
Normalize
Random
RandomDegrees
Reverse
RotateTo
ShortestBetween
Wrap
WrapDegrees
