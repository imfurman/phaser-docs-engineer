# Spline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/curves-spline

Phaser API Documentation
Class
Spline
Version: Phaser v3.90.0
On this page
Spline
Create a smooth 2d spline curve from a series of points.
Constructor
new Spline([points])
Parameters
name type optional description
points Array.< Phaser.Math.Vector2 > | Array.<number> Array.<Array.<number>> Yes
Scope : static
Extends
Phaser.Curves.Curve
Source: src/curves/SplineCurve.js#L14
Since: 3.0.0
Inherited Members ​
From Phaser.Curves.Curve :
active
arcLengthDivisions
cacheArcLengths
defaultDivisions
needsUpdate
type
Public Members ​
points ​
points: Array.< Phaser.Math.Vector2 > ​
Description:
The Vector2 points that configure the curve.
Source: src/curves/SplineCurve.js#L38
Since: 3.0.0
Inherited Methods ​
From Phaser.Curves.Curve :
draw
getBounds
getDistancePoints
getEndPoint
getLength
getLengths
getPointAt
getPoints
getRandomPoint
getSpacedPoints
getTangent
getTangentAt
getTFromDistance
getUtoTmapping
updateArcLengths
Public Methods ​
addPoint ​
<instance> addPoint(x, y) ​
Description:
Add a point to the current list of Vector2 points of the curve.
Parameters:
name type optional description
x number No The x coordinate of this curve
y number No The y coordinate of this curve
Returns: Phaser.Math.Vector2 - The new Vector2 added to the curve
Source: src/curves/SplineCurve.js#L91
Since: 3.0.0
addPoints ​
<instance> addPoints(points) ​
Description:
Add a list of points to the current list of Vector2 points of the curve.
Parameters:
name type optional description
points Array.< Phaser.Math.Vector2 > | Array.<number> Array.<Array.<number>> No
Returns: Phaser.Curves.Spline - This curve object.
Source: src/curves/SplineCurve.js#L51
Since: 3.0.0
fromJSON ​
<static> fromJSON(data) ​
Description:
Imports a JSON object containing this curve data.
Parameters:
name type optional description
data Phaser.Types.Curves.JSONCurve No The JSON object containing this curve data.
Returns: Phaser.Curves.Spline - The spline curve created.
Source: src/curves/SplineCurve.js#L204
Since: 3.0.0
getPoint ​
<instance> getPoint(t, [out]) ​
Description:
Get point at relative position in curve according to length.
Tags:
generic
Parameters:
name type optional description
t number No The position along the curve to return. Where 0 is the start and 1 is the end.
out Phaser.Math.Vector2 Yes A Vector2 object to store the result in. If not given will be created.
Returns: Phaser.Math.Vector2 - The coordinates of the point on the curve. If an out object was given this will be returned.
Source: src/curves/SplineCurve.js#L145
Since: 3.0.0
getResolution ​
<instance> getResolution(divisions) ​
Description:
Get the resolution of the curve.
Parameters:
name type optional description
divisions number No Optional divisions value.
Returns: number - The curve resolution.
Source: src/curves/SplineCurve.js#L130
Since: 3.0.0
getStartPoint ​
<instance> getStartPoint([out]) ​
Description:
Gets the starting point on the curve.
Tags:
generic
Parameters:
name type optional description
out Phaser.Math.Vector2 Yes A Vector2 object to store the result in. If not given will be created.
Overrides: Phaser.Curves.Curve#getStartPoint
Returns: Phaser.Math.Vector2 - The coordinates of the point on the curve. If an out object was given this will be returned.
Source: src/curves/SplineCurve.js#L111
Since: 3.0.0
toJSON ​
<instance> toJSON() ​
Description:
Exports a JSON object containing this curve data.
Returns: Phaser.Types.Curves.JSONCurve - The JSON object containing this curve data.
Source: src/curves/SplineCurve.js#L178
Since: 3.0.0
Previous
QuadraticBezier
Next
RequestAnimationFrame
Inherited Members
Public Members
points
Inherited Methods
Public Methods
addPoint
addPoints
fromJSON
getPoint
getResolution
getStartPoint
toJSON
