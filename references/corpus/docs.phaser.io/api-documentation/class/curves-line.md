# Line | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/curves-line

Phaser API Documentation
Class
Line
Version: Phaser v3.90.0
On this page
Line
A LineCurve is a "curve" comprising exactly two points (a line segment).
Constructor
new Line(p0, [p1])
Parameters
name type optional description
p0 Phaser.Math.Vector2 | Array.<number> No The first endpoint.
p1 Phaser.Math.Vector2 Yes The second endpoint.
Scope : static
Extends
Phaser.Curves.Curve
Source: src/curves/LineCurve.js#L15
Since: 3.0.0
Inherited Members ​
From Phaser.Curves.Curve :
active
cacheArcLengths
defaultDivisions
needsUpdate
type
Public Members ​
arcLengthDivisions ​
arcLengthDivisions: number ​
Description:
The quantity of arc length divisions within the curve.
Overrides: Phaser.Curves.Curve#arcLengthDivisions
Source: src/curves/LineCurve.js#L65
Since: 3.0.0
p0 ​
p0: Phaser.Math.Vector2 ​
Description:
The first endpoint.
Source: src/curves/LineCurve.js#L45
Since: 3.0.0
p1 ​
p1: Phaser.Math.Vector2 ​
Description:
The second endpoint.
Source: src/curves/LineCurve.js#L54
Since: 3.0.0
Inherited Methods ​
From Phaser.Curves.Curve :
getDistancePoints
getEndPoint
getLength
getLengths
getPoints
getRandomPoint
getSpacedPoints
getTangentAt
getTFromDistance
updateArcLengths
Public Methods ​
draw ​
<instance> draw(graphics) ​
Description:
Draws this curve on the given Graphics object.
The curve is drawn using Graphics.lineBetween so will be drawn at whatever the present Graphics line color is.
The Graphics object is not cleared before the draw, so the curve will appear on-top of anything else already rendered to it.
Tags:
generic
Parameters:
name type optional description
graphics Phaser.GameObjects.Graphics No The Graphics instance onto which this curve will be drawn.
Overrides: Phaser.Curves.Curve#draw
Returns: Phaser.GameObjects.Graphics - The Graphics object to which the curve was drawn.
Source: src/curves/LineCurve.js#L236
Since: 3.0.0
fromJSON ​
<static> fromJSON(data) ​
Description:
Configures this line from a JSON representation.
Parameters:
name type optional description
data Phaser.Types.Curves.JSONCurve No The JSON object containing this curve data.
Returns: Phaser.Curves.Line - A new LineCurve object.
Source: src/curves/LineCurve.js#L280
Since: 3.0.0
getBounds ​
<instance> getBounds([out]) ​
Description:
Returns a Rectangle where the position and dimensions match the bounds of this Curve.
Tags:
generic
Parameters:
name type optional description
out Phaser.Geom.Rectangle Yes A Rectangle object to store the bounds in. If not given a new Rectangle will be created.
Overrides: Phaser.Curves.Curve#getBounds
Returns: Phaser.Geom.Rectangle - A Rectangle object holding the bounds of this curve. If out was given it will be this object.
Source: src/curves/LineCurve.js#L76
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
Source: src/curves/LineCurve.js#L131
Since: 3.0.0
getPointAt ​
<instance> getPointAt(u, [out]) ​
Description:
Gets a point at a given position on the line.
Tags:
generic
Parameters:
name type optional description
u number No The position along the curve to return. Where 0 is the start and 1 is the end.
out Phaser.Math.Vector2 Yes A Vector2 object to store the result in. If not given will be created.
Overrides: Phaser.Curves.Curve#getPointAt
Returns: Phaser.Math.Vector2 - The coordinates of the point on the curve. If an out object was given this will be returned.
Source: src/curves/LineCurve.js#L160
Since: 3.0.0
getResolution ​
<instance> getResolution([divisions]) ​
Description:
Gets the resolution of the line.
Parameters:
name type optional default description
divisions number Yes 1 The number of divisions to consider.
Returns: number - The resolution. Equal to the number of divisions.
Source: src/curves/LineCurve.js#L114
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
Source: src/curves/LineCurve.js#L95
Since: 3.0.0
getTangent ​
<instance> getTangent([t], [out]) ​
Description:
Gets the slope of the line as a unit vector.
Tags:
generic
Parameters:
name type optional description
t number Yes The relative position on the line, [0..1].
out Phaser.Math.Vector2 Yes A vector to store the result in.
Overrides: Phaser.Curves.Curve#getTangent
Returns: Phaser.Math.Vector2 - The tangent vector.
Source: src/curves/LineCurve.js#L178
Since: 3.0.0
getUtoTmapping ​
<instance> getUtoTmapping(u, distance, [divisions]) ​
Description:
Given u ( 0 .. 1 ), get a t to find p. This gives you points which are equidistant.
Parameters:
name type optional description
u number No A float between 0 and 1.
distance number No The distance, in pixels.
divisions number Yes Optional amount of divisions.
Overrides: Phaser.Curves.Curve#getUtoTmapping
Returns: number - The equidistant value.
Source: src/curves/LineCurve.js#L200
Since: 3.0.0
toJSON ​
<instance> toJSON() ​
Description:
Gets a JSON representation of the line.
Returns: Phaser.Types.Curves.JSONCurve - The JSON object containing this curve data.
Source: src/curves/LineCurve.js#L259
Since: 3.0.0
Previous
Ellipse
Next
MoveTo
Inherited Members
Public Members
arcLengthDivisions
p0
p1
Inherited Methods
Public Methods
draw
fromJSON
getBounds
getPoint
getPointAt
getResolution
getStartPoint
getTangent
getUtoTmapping
toJSON
