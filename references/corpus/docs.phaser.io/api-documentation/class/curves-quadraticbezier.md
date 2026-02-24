# QuadraticBezier | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/curves-quadraticbezier

Phaser API Documentation
Class
QuadraticBezier
Version: Phaser v3.90.0
On this page
QuadraticBezier
A quadratic Bézier curve constructed from two control points.
Constructor
new QuadraticBezier(p0, p1, p2)
Parameters
name type optional description
p0 Phaser.Math.Vector2 | Array.<number> No Start point, or an array of point pairs.
p1 Phaser.Math.Vector2 No Control Point 1.
p2 Phaser.Math.Vector2 No Control Point 2.
Scope : static
Extends
Phaser.Curves.Curve
Source: src/curves/QuadraticBezierCurve.js#L12
Since: 3.2.0
Inherited Members ​
From Phaser.Curves.Curve :
active
arcLengthDivisions
cacheArcLengths
defaultDivisions
needsUpdate
type
Public Members ​
p0 ​
p0: Phaser.Math.Vector2 ​
Description:
The start point.
Source: src/curves/QuadraticBezierCurve.js#L43
Since: 3.2.0
p1 ​
p1: Phaser.Math.Vector2 ​
Description:
The first control point.
Source: src/curves/QuadraticBezierCurve.js#L52
Since: 3.2.0
p2 ​
p2: Phaser.Math.Vector2 ​
Description:
The second control point.
Source: src/curves/QuadraticBezierCurve.js#L61
Since: 3.2.0
Inherited Methods ​
From Phaser.Curves.Curve :
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
draw ​
<instance> draw(graphics, [pointsTotal]) ​
Description:
Draws this curve on the given Graphics object.
The curve is drawn using Graphics.strokePoints so will be drawn at whatever the present Graphics stroke color is.
The Graphics object is not cleared before the draw, so the curve will appear on-top of anything else already rendered to it.
Tags:
generic
Parameters:
name type optional default description
graphics Phaser.GameObjects.Graphics No Graphics object to draw onto.
pointsTotal number Yes 32 Number of points to be used for drawing the curve. Higher numbers result in smoother curve but require more processing.
Overrides: Phaser.Curves.Curve#draw
Returns: Phaser.GameObjects.Graphics - Graphics object that was drawn to.
Source: src/curves/QuadraticBezierCurve.js#L132
Since: 3.2.0
fromJSON ​
<static> fromJSON(data) ​
Description:
Creates a curve from a JSON object, e. g. created by toJSON .
Parameters:
name type optional description
data Phaser.Types.Curves.JSONCurve No The JSON object containing this curve data.
Returns: Phaser.Curves.QuadraticBezier - The created curve instance.
Source: src/curves/QuadraticBezierCurve.js#L190
Since: 3.2.0
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
Source: src/curves/QuadraticBezierCurve.js#L105
Since: 3.2.0
getResolution ​
<instance> getResolution(divisions) ​
Description:
Get the resolution of the curve.
Parameters:
name type optional description
divisions number No Optional divisions value.
Returns: number - The curve resolution.
Source: src/curves/QuadraticBezierCurve.js#L90
Since: 3.2.0
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
Source: src/curves/QuadraticBezierCurve.js#L71
Since: 3.2.0
toJSON ​
<instance> toJSON() ​
Description:
Converts the curve into a JSON compatible object.
Returns: Phaser.Types.Curves.JSONCurve - The JSON object containing this curve data.
Source: src/curves/QuadraticBezierCurve.js#L168
Since: 3.2.0
Previous
Path
Next
Spline
Inherited Members
Public Members
p0
p1
p2
Inherited Methods
Public Methods
draw
fromJSON
getPoint
getResolution
getStartPoint
toJSON
