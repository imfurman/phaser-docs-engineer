# Ellipse | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/curves-ellipse

Phaser API Documentation
Class
Ellipse
Version: Phaser v3.90.0
On this page
Ellipse
An Elliptical Curve derived from the Base Curve class.
See https://en.wikipedia.org/wiki/Elliptic_curve for more details.
Constructor
new Ellipse([x], [y], [xRadius], [yRadius], [startAngle], [endAngle], [clockwise], [rotation])
Parameters
name type optional default description
x number | Phaser.Types.Curves.EllipseCurveConfig Yes 0 The x coordinate of the ellipse, or an Ellipse Curve configuration object.
y number Yes 0 The y coordinate of the ellipse.
xRadius number Yes 0 The horizontal radius of ellipse.
yRadius number Yes 0 The vertical radius of ellipse.
startAngle number Yes 0 The start angle of the ellipse, in degrees.
endAngle number Yes 360 The end angle of the ellipse, in degrees.
clockwise boolean Yes false Whether the ellipse angles are given as clockwise ( true ) or counter-clockwise ( false ).
rotation number Yes 0 The rotation of the ellipse, in degrees.
Scope : static
Extends
Phaser.Curves.Curve
Source: src/curves/EllipseCurve.js#L16
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
angle ​
angle: number ​
Description:
The rotation of the ellipse, relative to the center, in degrees.
Source: src/curves/EllipseCurve.js#L536
Since: 3.14.0
clockwise ​
clockwise: boolean ​
Description:
true if the ellipse rotation is clockwise or false if anti-clockwise.
Source: src/curves/EllipseCurve.js#L515
Since: 3.0.0
endAngle ​
endAngle: number ​
Description:
The end angle of the ellipse in degrees.
Source: src/curves/EllipseCurve.js#L494
Since: 3.0.0
p0 ​
p0: Phaser.Math.Vector2 ​
Description:
The center point of the ellipse. Used for calculating rotation.
Source: src/curves/EllipseCurve.js#L71
Since: 3.0.0
rotation ​
rotation: number ​
Description:
The rotation of the ellipse, relative to the center, in radians.
Source: src/curves/EllipseCurve.js#L557
Since: 3.0.0
startAngle ​
startAngle: number ​
Description:
The start angle of the ellipse in degrees.
Source: src/curves/EllipseCurve.js#L473
Since: 3.0.0
x ​
x: number ​
Description:
The x coordinate of the center of the ellipse.
Source: src/curves/EllipseCurve.js#L389
Since: 3.0.0
xRadius ​
xRadius: number ​
Description:
The horizontal radius of the ellipse.
Source: src/curves/EllipseCurve.js#L431
Since: 3.0.0
y ​
y: number ​
Description:
The y coordinate of the center of the ellipse.
Source: src/curves/EllipseCurve.js#L410
Since: 3.0.0
yRadius ​
yRadius: number ​
Description:
The vertical radius of the ellipse.
Source: src/curves/EllipseCurve.js#L452
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
fromJSON ​
<static> fromJSON(data) ​
Description:
Creates a curve from the provided Ellipse Curve Configuration object.
Parameters:
name type optional description
data Phaser.Types.Curves.JSONEllipseCurve No The JSON object containing this curve data.
Returns: Phaser.Curves.Ellipse - The ellipse curve constructed from the configuration object.
Source: src/curves/EllipseCurve.js#L603
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
Source: src/curves/EllipseCurve.js#L177
Since: 3.0.0
getResolution ​
<instance> getResolution(divisions) ​
Description:
Get the resolution of the curve.
Parameters:
name type optional description
divisions number No Optional divisions value.
Returns: number - The curve resolution.
Source: src/curves/EllipseCurve.js#L162
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
Source: src/curves/EllipseCurve.js#L143
Since: 3.0.0
setClockwise ​
<instance> setClockwise(value) ​
Description:
Sets if this curve extends clockwise or anti-clockwise.
Parameters:
name type optional description
value boolean No The clockwise state of this curve.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L355
Since: 3.0.0
setEndAngle ​
<instance> setEndAngle(value) ​
Description:
Sets the end angle of this curve.
Parameters:
name type optional description
value number No The end angle of this curve, in radians.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L338
Since: 3.0.0
setHeight ​
<instance> setHeight(value) ​
Description:
Sets the height of this curve.
Parameters:
name type optional description
value number No The height of this curve.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L304
Since: 3.0.0
setRotation ​
<instance> setRotation(value) ​
Description:
Sets the rotation of this curve.
Parameters:
name type optional description
value number No The rotation of this curve, in radians.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L372
Since: 3.0.0
setStartAngle ​
<instance> setStartAngle(value) ​
Description:
Sets the start angle of this curve.
Parameters:
name type optional description
value number No The start angle of this curve, in radians.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L321
Since: 3.0.0
setWidth ​
<instance> setWidth(value) ​
Description:
Sets the width of this curve.
Parameters:
name type optional description
value number No The width of this curve.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L287
Since: 3.0.0
setXRadius ​
<instance> setXRadius(value) ​
Description:
Sets the horizontal radius of this curve.
Parameters:
name type optional description
value number No The horizontal radius of this curve.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L253
Since: 3.0.0
setYRadius ​
<instance> setYRadius(value) ​
Description:
Sets the vertical radius of this curve.
Parameters:
name type optional description
value number No The vertical radius of this curve.
Returns: Phaser.Curves.Ellipse - This curve object.
Source: src/curves/EllipseCurve.js#L270
Since: 3.0.0
toJSON ​
<instance> toJSON() ​
Description:
JSON serialization of the curve.
Returns: Phaser.Types.Curves.JSONEllipseCurve - The JSON object containing this curve data.
Source: src/curves/EllipseCurve.js#L578
Since: 3.0.0
Previous
Curve
Next
Line
Inherited Members
Public Members
angle
clockwise
endAngle
p0
rotation
startAngle
x
xRadius
y
yRadius
Inherited Methods
Public Methods
fromJSON
getPoint
getResolution
getStartPoint
setClockwise
setEndAngle
setHeight
setRotation
setStartAngle
setWidth
setXRadius
setYRadius
toJSON
