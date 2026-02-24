# Point | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/geom-point

Phaser API Documentation
Class
Point
Version: Phaser v3.90.0
On this page
Point
Defines a Point in 2D space, with an x and y component.
Constructor
new Point([x], [y])
Parameters
name type optional default description
x number Yes 0 The x coordinate of this Point.
y number Yes "x" The y coordinate of this Point.
Scope : static
Source: src/geom/point/Point.js#L10
Since: 3.0.0
Public Methods ​
Ceil ​
<static> Ceil(point) ​
Description:
Apply Math.ceil() to each coordinate of the given Point.
Tags:
generic
Parameters:
name type optional description
point Phaser.Geom.Point No The Point to ceil.
Returns: Phaser.Geom.Point - The Point with Math.ceil() applied to its coordinates.
Source: src/geom/point/Ceil.js#L7
Since: 3.0.0
Clone ​
<static> Clone(source) ​
Description:
Clone the given Point.
Parameters:
name type optional description
source Phaser.Geom.Point No The source Point to clone.
Returns: Phaser.Geom.Point - The cloned Point.
Source: src/geom/point/Clone.js#L9
Since: 3.0.0
CopyFrom ​
<static> CopyFrom(source, dest) ​
Description:
Copy the values of one Point to a destination Point.
Tags:
generic
Parameters:
name type optional description
source Phaser.Geom.Point No The source Point to copy the values from.
dest Phaser.Geom.Point No The destination Point to copy the values to.
Returns: Phaser.Geom.Point - The destination Point.
Source: src/geom/point/CopyFrom.js#L7
Since: 3.0.0
Equals ​
<static> Equals(point, toCompare) ​
Description:
A comparison of two Point objects to see if they are equal.
Parameters:
name type optional description
point Phaser.Geom.Point No The original Point to compare against.
toCompare Phaser.Geom.Point No The second Point to compare.
Returns: boolean - Returns true if the both Point objects are equal.
Source: src/geom/point/Equals.js#L7
Since: 3.0.0
Floor ​
<static> Floor(point) ​
Description:
Apply Math.ceil() to each coordinate of the given Point.
Tags:
generic
Parameters:
name type optional description
point Phaser.Geom.Point No The Point to floor.
Returns: Phaser.Geom.Point - The Point with Math.floor() applied to its coordinates.
Source: src/geom/point/Floor.js#L7
Since: 3.0.0
GetCentroid ​
<static> GetCentroid(points, [out]) ​
Description:
Get the centroid or geometric center of a plane figure (the arithmetic mean position of all the points in the figure).
Informally, it is the point at which a cutout of the shape could be perfectly balanced on the tip of a pin.
Tags:
generic
Parameters:
name type optional description
points Array.< Phaser.Types.Math.Vector2Like > No An array of Vector2Like objects to get the geometric center of.
out Phaser.Geom.Point Yes A Point object to store the output coordinates in. If not given, a new Point instance is created.
Returns: Phaser.Geom.Point - A Point object representing the geometric center of the given points.
Source: src/geom/point/GetCentroid.js#L9
Since: 3.0.0
GetMagnitude ​
<static> GetMagnitude(point) ​
Description:
Calculate the magnitude of the point, which equivalent to the length of the line from the origin to this point.
Parameters:
name type optional description
point Phaser.Geom.Point No The point to calculate the magnitude for
Returns: number - The resulting magnitude
Source: src/geom/point/GetMagnitude.js#L7
Since: 3.0.0
GetMagnitudeSq ​
<static> GetMagnitudeSq(point) ​
Description:
Calculates the square of magnitude of given point.(Can be used for fast magnitude calculation of point)
Parameters:
name type optional description
point Phaser.Geom.Point No Returns square of the magnitude/length of given point.
Returns: number - Returns square of the magnitude of given point.
Source: src/geom/point/GetMagnitudeSq.js#L7
Since: 3.0.0
GetRectangleFromPoints ​
<static> GetRectangleFromPoints(points, [out]) ​
Description:
Calculates the Axis Aligned Bounding Box (or aabb) from an array of points.
Tags:
generic
Parameters:
name type optional description
points Array.< Phaser.Types.Math.Vector2Like > No An array of Vector2Like objects to get the AABB from.
out Phaser.Geom.Rectangle Yes A Rectangle object to store the results in. If not given, a new Rectangle instance is created.
Returns: Phaser.Geom.Rectangle - A Rectangle object holding the AABB values for the given points.
Source: src/geom/point/GetRectangleFromPoints.js#L9
Since: 3.0.0
Interpolate ​
<static> Interpolate(pointA, pointB, [t], [out]) ​
Description:
Returns the linear interpolation point between the two given points, based on t .
Tags:
generic
Parameters:
name type optional default description
pointA Phaser.Geom.Point No The starting Point for the interpolation.
pointB Phaser.Geom.Point No The target Point for the interpolation.
t number Yes 0 The amount to interpolate between the two points. Generally, a value between 0 (returns the starting Point ) and 1 (returns the target Point ). If omitted, 0 is used.
out Phaser.Geom.Point | object Yes An optional Point object whose x and y values will be set to the result of the interpolation (can also be any object with x and y properties). If omitted, a new Point created and returned.
Returns: Phaser.Geom.Point , object - Either the object from the out argument with the properties x and y set to the result of the interpolation or a newly created Point object.
Source: src/geom/point/Interpolate.js#L9
Since: 3.0.0
Invert ​
<static> Invert(point) ​
Description:
Swaps the X and the Y coordinate of a point.
Tags:
generic
Parameters:
name type optional description
point Phaser.Geom.Point No The Point to modify.
Returns: Phaser.Geom.Point - The modified point .
Source: src/geom/point/Invert.js#L7
Since: 3.0.0
Negative ​
<static> Negative(point, [out]) ​
Description:
Inverts a Point's coordinates.
Tags:
generic
Parameters:
name type optional description
point Phaser.Geom.Point No The Point to invert.
out Phaser.Geom.Point Yes The Point to return the inverted coordinates in.
Returns: Phaser.Geom.Point - The modified out Point, or a new Point if none was provided.
Source: src/geom/point/Negative.js#L9
Since: 3.0.0
Project ​
<static> Project(pointA, pointB, [out]) ​
Description:
Calculates the vector projection of pointA onto the nonzero pointB . This is the
orthogonal projection of pointA onto a straight line parallel to pointB .
Tags:
generic
Parameters:
name type optional description
pointA Phaser.Geom.Point No Point A, to be projected onto Point B.
pointB Phaser.Geom.Point No Point B, to have Point A projected upon it.
out Phaser.Geom.Point Yes The Point object to store the position in. If not given, a new Point instance is created.
Returns: Phaser.Geom.Point - A Point object holding the coordinates of the vector projection of pointA onto pointB .
Source: src/geom/point/Project.js#L10
Since: 3.0.0
ProjectUnit ​
<static> ProjectUnit(pointA, pointB, [out]) ​
Description:
Calculates the vector projection of pointA onto the nonzero pointB . This is the
orthogonal projection of pointA onto a straight line paralle to pointB .
Tags:
generic
Parameters:
name type optional description
pointA Phaser.Geom.Point No Point A, to be projected onto Point B. Must be a normalized point with a magnitude of 1.
pointB Phaser.Geom.Point No Point B, to have Point A projected upon it.
out Phaser.Geom.Point Yes The Point object to store the position in. If not given, a new Point instance is created.
Returns: Phaser.Geom.Point - A unit Point object holding the coordinates of the vector projection of pointA onto pointB .
Source: src/geom/point/ProjectUnit.js#L9
Since: 3.0.0
SetMagnitude ​
<static> SetMagnitude(point, magnitude) ​
Description:
Changes the magnitude (length) of a two-dimensional vector without changing its direction.
Tags:
generic
Parameters:
name type optional description
point Phaser.Geom.Point No The Point to treat as the end point of the vector.
magnitude number No The new magnitude of the vector.
Returns: Phaser.Geom.Point - The modified Point.
Source: src/geom/point/SetMagnitude.js#L9
Since: 3.0.0
setTo ​
<instance> setTo([x], [y]) ​
Description:
Set the x and y coordinates of the point to the given values.
Parameters:
name type optional default description
x number Yes 0 The x coordinate of this Point.
y number Yes "x" The y coordinate of this Point.
Returns: Phaser.Geom.Point - This Point object.
Source: src/geom/point/Point.js#L63
Since: 3.0.0
Public Members ​
type ​
type: number ​
Description:
The geometry constant type of this object: GEOM_CONST.POINT .
Used for fast type comparisons.
Source: src/geom/point/Point.js#L31
Since: 3.19.0
x ​
x: number ​
Description:
The x coordinate of this Point.
Source: src/geom/point/Point.js#L42
Since: 3.0.0
y ​
y: number ​
Description:
The y coordinate of this Point.
Source: src/geom/point/Point.js#L52
Since: 3.0.0
Previous
Vertex
Next
Polygon
Public Methods
Ceil
Clone
CopyFrom
Equals
Floor
GetCentroid
GetMagnitude
GetMagnitudeSq
GetRectangleFromPoints
Interpolate
Invert
Negative
Project
ProjectUnit
SetMagnitude
setTo
Public Members
type
x
y
