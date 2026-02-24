# CubicBezier | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/curves-cubicbezier

Phaser API Documentation
Class
CubicBezier
Version: Phaser v3.90.0
On this page
CubicBezier
A higher-order Bézier curve constructed of four points.
Constructor
new CubicBezier(p0, p1, p2, p3)
Parameters
name type optional description
p0 Phaser.Math.Vector2 | Array.< Phaser.Math.Vector2 > No Start point, or an array of point pairs.
p1 Phaser.Math.Vector2 No Control Point 1.
p2 Phaser.Math.Vector2 No Control Point 2.
p3 Phaser.Math.Vector2 No End Point.
Scope : static
Extends
Phaser.Curves.Curve
Source: src/curves/CubicBezierCurve.js#L14
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
p0 ​
p0: Phaser.Math.Vector2 ​
Description:
The start point of this curve.
Source: src/curves/CubicBezierCurve.js#L47
Since: 3.0.0
p1 ​
p1: Phaser.Math.Vector2 ​
Description:
The first control point of this curve.
Source: src/curves/CubicBezierCurve.js#L56
Since: 3.0.0
p2 ​
p2: Phaser.Math.Vector2 ​
Description:
The second control point of this curve.
Source: src/curves/CubicBezierCurve.js#L65
Since: 3.0.0
p3 ​
p3: Phaser.Math.Vector2 ​
Description:
The end point of this curve.
Source: src/curves/CubicBezierCurve.js#L74
Since: 3.0.0
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
Draws this curve to the specified graphics object.
Tags:
generic
Parameters:
name type optional default description
graphics Phaser.GameObjects.Graphics No The graphics object this curve should be drawn to.
pointsTotal number Yes 32 The number of intermediary points that make up this curve. A higher number of points will result in a smoother curve.
Overrides: Phaser.Curves.Curve#draw
Returns: Phaser.GameObjects.Graphics - The graphics object this curve was drawn to. Useful for method chaining.
Source: src/curves/CubicBezierCurve.js#L143
Since: 3.0.0
fromJSON ​
<static> fromJSON(data) ​
Description:
Generates a curve from a JSON object.
Parameters:
name type optional description
data Phaser.Types.Curves.JSONCurve No The JSON object containing this curve data.
Returns: Phaser.Curves.CubicBezier - The curve generated from the JSON object.
Source: src/curves/CubicBezierCurve.js#L199
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
Source: src/curves/CubicBezierCurve.js#L118
Since: 3.0.0
getResolution ​
<instance> getResolution(divisions) ​
Description:
Returns the resolution of this curve.
Parameters:
name type optional description
divisions number No The amount of divisions used by this curve.
Returns: number - The resolution of the curve.
Source: src/curves/CubicBezierCurve.js#L103
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
Source: src/curves/CubicBezierCurve.js#L84
Since: 3.0.0
toJSON ​
<instance> toJSON() ​
Description:
Returns a JSON object that describes this curve.
Returns: Phaser.Types.Curves.JSONCurve - The JSON object containing this curve data.
Source: src/curves/CubicBezierCurve.js#L176
Since: 3.0.0
Previous
TimeStep
Next
Curve
Inherited Members
Public Members
p0
p1
p2
p3
Inherited Methods
Public Methods
draw
fromJSON
getPoint
getResolution
getStartPoint
toJSON
