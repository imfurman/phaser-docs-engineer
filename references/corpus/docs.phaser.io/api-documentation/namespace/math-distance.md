# Phaser.Math.Distance | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/math-distance

Phaser API Documentation
Namespaces
Phaser.Math.Distance
Version: Phaser v3.90.0
On this page
Phaser.Math.Distance
Scope: static
Source: src/math/distance/index.js#L7
Static functions ​
Between ​
<static> Between(x1, y1, x2, y2) ​
Description:
Calculate the distance between two sets of coordinates (points).
Parameters:
name type optional description
x1 number No The x coordinate of the first point.
y1 number No The y coordinate of the first point.
x2 number No The x coordinate of the second point.
y2 number No The y coordinate of the second point.
Returns: number - The distance between each point.
Source: src/math/distance/DistanceBetween.js#L7
Since: 3.0.0
BetweenPoints ​
<static> BetweenPoints(a, b) ​
Description:
Calculate the distance between two points.
Parameters:
name type optional description
a Phaser.Types.Math.Vector2Like No The first point.
b Phaser.Types.Math.Vector2Like No The second point.
Returns: number - The distance between the points.
Source: src/math/distance/DistanceBetweenPoints.js#L7
Since: 3.22.0
BetweenPointsSquared ​
<static> BetweenPointsSquared(a, b) ​
Description:
Calculate the squared distance between two points.
Parameters:
name type optional description
a Phaser.Types.Math.Vector2Like No The first point.
b Phaser.Types.Math.Vector2Like No The second point.
Returns: number - The squared distance between the points.
Source: src/math/distance/DistanceBetweenPointsSquared.js#L7
Since: 3.22.0
Chebyshev ​
<static> Chebyshev(x1, y1, x2, y2) ​
Description:
Calculate the Chebyshev distance between two sets of coordinates (points).
Chebyshev distance (or chessboard distance) is the maximum of the horizontal and vertical distances.
It's the effective distance when movement can be horizontal, vertical, or diagonal.
Parameters:
name type optional description
x1 number No The x coordinate of the first point.
y1 number No The y coordinate of the first point.
x2 number No The x coordinate of the second point.
y2 number No The y coordinate of the second point.
Returns: number - The distance between each point.
Source: src/math/distance/DistanceChebyshev.js#L7
Since: 3.22.0
Power ​
<static> Power(x1, y1, x2, y2, pow) ​
Description:
Calculate the distance between two sets of coordinates (points) to the power of pow .
Parameters:
name type optional description
x1 number No The x coordinate of the first point.
y1 number No The y coordinate of the first point.
x2 number No The x coordinate of the second point.
y2 number No The y coordinate of the second point.
pow number No The exponent.
Returns: number - The distance between each point.
Source: src/math/distance/DistancePower.js#L7
Since: 3.0.0
Snake ​
<static> Snake(x1, y1, x2, y2) ​
Description:
Calculate the snake distance between two sets of coordinates (points).
Snake distance (rectilinear distance, Manhattan distance) is the sum of the horizontal and vertical distances.
It's the effective distance when movement is allowed only horizontally or vertically (but not both).
Parameters:
name type optional description
x1 number No The x coordinate of the first point.
y1 number No The y coordinate of the first point.
x2 number No The x coordinate of the second point.
y2 number No The y coordinate of the second point.
Returns: number - The distance between each point.
Source: src/math/distance/DistanceSnake.js#L7
Since: 3.22.0
Squared ​
<static> Squared(x1, y1, x2, y2) ​
Description:
Calculate the distance between two sets of coordinates (points), squared.
Parameters:
name type optional description
x1 number No The x coordinate of the first point.
y1 number No The y coordinate of the first point.
x2 number No The x coordinate of the second point.
y2 number No The y coordinate of the second point.
Returns: number - The distance between each point, squared.
Source: src/math/distance/DistanceSquared.js#L7
Since: 3.0.0
Previous
Phaser.Math.Angle
Next
Phaser.Math.Easing.Back
Static functions
Between
BetweenPoints
BetweenPointsSquared
Chebyshev
Power
Snake
Squared
