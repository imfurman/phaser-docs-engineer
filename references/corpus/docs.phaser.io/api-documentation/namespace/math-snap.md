# Phaser.Math.Snap | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/math-snap

Phaser API Documentation
Namespaces
Phaser.Math.Snap
Version: Phaser v3.90.0
On this page
Phaser.Math.Snap
Scope: static
Source: src/math/snap/index.js#L7
Static functions ​
Ceil ​
<static> Ceil(value, gap, [start], [divide]) ​
Description:
Snap a value to nearest grid slice, using ceil.
Example: if you have an interval gap of 5 and a position of 12 ... you will snap to 15 .
As will 14 snap to 15 ... but 16 will snap to 20 .
Parameters:
name type optional default description
value number No The value to snap.
gap number No The interval gap of the grid.
start number Yes 0 Optional starting offset for gap.
divide boolean Yes false If true it will divide the snapped value by the gap before returning.
Returns: number - The snapped value.
Source: src/math/snap/SnapCeil.js#L7
Since: 3.0.0
Floor ​
<static> Floor(value, gap, [start], [divide]) ​
Description:
Snap a value to nearest grid slice, using floor.
Example: if you have an interval gap of 5 and a position of 12 ... you will snap to 10 .
As will 14 snap to 10 ... but 16 will snap to 15 .
Parameters:
name type optional default description
value number No The value to snap.
gap number No The interval gap of the grid.
start number Yes 0 Optional starting offset for gap.
divide boolean Yes false If true it will divide the snapped value by the gap before returning.
Returns: number - The snapped value.
Source: src/math/snap/SnapFloor.js#L7
Since: 3.0.0
To ​
<static> To(value, gap, [start], [divide]) ​
Description:
Snap a value to nearest grid slice, using rounding.
Example: if you have an interval gap of 5 and a position of 12 ... you will snap to 10 whereas 14 will snap to 15 .
Parameters:
name type optional default description
value number No The value to snap.
gap number No The interval gap of the grid.
start number Yes 0 Optional starting offset for gap.
divide boolean Yes false If true it will divide the snapped value by the gap before returning.
Returns: number - The snapped value.
Source: src/math/snap/SnapTo.js#L7
Since: 3.0.0
Previous
Phaser.Math.Pow2
Next
Phaser.Math
Static functions
Ceil
Floor
To
