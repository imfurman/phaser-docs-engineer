# Phaser.Scale.ScaleModes | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/scale-scalemodes

Phaser API Documentation
Namespaces
Phaser.Scale.ScaleModes
Version: Phaser v3.90.0
On this page
Phaser.Scale.ScaleModes
Scope: static
Source: src/scale/const/SCALE_MODE_CONST.js#L7
Since: 3.16.0
Static functions ​
ENVELOP ​
ENVELOP: number ​
Description:
The width and height are automatically adjusted to make the size cover the entire target
area while keeping the aspect ratio. This may extend further out than the target size.
Source: src/scale/const/SCALE_MODE_CONST.js#L71
Since: 3.16.0
EXPAND ​
EXPAND: number ​
Description:
The Canvas's visible area is resized to fit all available parent space like RESIZE mode,
and scale canvas size to fit inside the visible area like FIT mode.
Source: src/scale/const/SCALE_MODE_CONST.js#L92
Since: 3.80.0
FIT ​
FIT: number ​
Description:
The width and height are automatically adjusted to fit inside the given target area,
while keeping the aspect ratio. Depending on the aspect ratio there may be some space
inside the area which is not covered.
Source: src/scale/const/SCALE_MODE_CONST.js#L59
Since: 3.16.0
HEIGHT_CONTROLS_WIDTH ​
HEIGHT_CONTROLS_WIDTH: number ​
Description:
The width is automatically adjusted based on the height.
Source: src/scale/const/SCALE_MODE_CONST.js#L49
Since: 3.16.0
NONE ​
NONE: number ​
Description:
No scaling happens at all. The canvas is set to the size given in the game config and Phaser doesn't change it
again from that point on. If you change the canvas size, either via CSS, or directly via code, then you need
to call the Scale Managers resize method to give the new dimensions, or input events will stop working.
Source: src/scale/const/SCALE_MODE_CONST.js#L27
Since: 3.16.0
RESIZE ​
RESIZE: number ​
Description:
The Canvas is resized to fit all available parent space, regardless of aspect ratio.
Source: src/scale/const/SCALE_MODE_CONST.js#L82
Since: 3.16.0
WIDTH_CONTROLS_HEIGHT ​
WIDTH_CONTROLS_HEIGHT: number ​
Description:
The height is automatically adjusted based on the width.
Source: src/scale/const/SCALE_MODE_CONST.js#L39
Since: 3.16.0
Previous
Phaser.Scale.Orientation
Next
Phaser.Scale.Zoom
Static functions
ENVELOP
EXPAND
FIT
HEIGHT_CONTROLS_WIDTH
NONE
RESIZE
WIDTH_CONTROLS_HEIGHT
