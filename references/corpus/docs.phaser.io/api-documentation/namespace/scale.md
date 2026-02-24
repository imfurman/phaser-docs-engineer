# Phaser.Scale | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/scale

Phaser API Documentation
Namespaces
Phaser.Scale
Version: Phaser v3.90.0
On this page
Phaser.Scale
Scope: static
Source: src/scale/index.js#L10
Static functions ​
ScaleManager
Static functions ​
Center
Events
Orientation
ScaleModes
Zoom
Static functions ​
CenterType ​
CenterType ​
Description:
Phaser Scale Manager constants for centering the game canvas.
To find out what each mode does please see Phaser.Scale.Center .
Source: src/scale/const/CENTER_CONST.js#L15
Since: 3.16.0
OrientationType ​
OrientationType ​
Description:
Phaser Scale Manager constants for orientation.
To find out what each mode does please see Phaser.Scale.Orientation .
Source: src/scale/const/ORIENTATION_CONST.js#L15
Since: 3.16.0
ScaleModeType ​
ScaleModeType ​
Description:
Phaser Scale Manager constants for the different scale modes available.
To find out what each mode does please see Phaser.Scale.ScaleModes .
Source: src/scale/const/SCALE_MODE_CONST.js#L15
Since: 3.16.0
ZoomType ​
ZoomType ​
Description:
Phaser Scale Manager constants for zoom modes.
To find out what each mode does please see Phaser.Scale.Zoom .
Source: src/scale/const/ZOOM_CONST.js#L15
Since: 3.16.0
Static functions ​
CENTER_BOTH ​
CENTER_BOTH: number ​
Description:
The game canvas is centered both horizontally and vertically within the parent.
To do this, the parent has to have a bounds that can be calculated and not be empty.
Centering is achieved by setting the margin left and top properties of the
game canvas, and does not factor in any other CSS styles you may have applied.
Source: src/scale/const/CENTER_CONST.js#L38
Since: 3.16.0
CENTER_HORIZONTALLY ​
CENTER_HORIZONTALLY: number ​
Description:
The game canvas is centered horizontally within the parent.
To do this, the parent has to have a bounds that can be calculated and not be empty.
Centering is achieved by setting the margin left and top properties of the
game canvas, and does not factor in any other CSS styles you may have applied.
Source: src/scale/const/CENTER_CONST.js#L52
Since: 3.16.0
CENTER_VERTICALLY ​
CENTER_VERTICALLY: number ​
Description:
The game canvas is centered both vertically within the parent.
To do this, the parent has to have a bounds that can be calculated and not be empty.
Centering is achieved by setting the margin left and top properties of the
game canvas, and does not factor in any other CSS styles you may have applied.
Source: src/scale/const/CENTER_CONST.js#L66
Since: 3.16.0
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
LANDSCAPE ​
LANDSCAPE: string ​
Description:
The primary landscape orientation.
Source: src/scale/const/ORIENTATION_CONST.js#L27
Since: 3.16.0
MAX_ZOOM ​
MAX_ZOOM: number ​
Description:
Calculate the zoom value based on the maximum multiplied game size that will
fit into the parent, or browser window if no parent is set.
Source: src/scale/const/ZOOM_CONST.js#L57
Since: 3.16.0
NO_CENTER ​
NO_CENTER: number ​
Description:
The game canvas is not centered within the parent by Phaser.
You can still center it yourself via CSS.
Source: src/scale/const/CENTER_CONST.js#L27
Since: 3.16.0
NO_ZOOM ​
NO_ZOOM: number ​
Description:
The game canvas will not be zoomed by Phaser.
Source: src/scale/const/ZOOM_CONST.js#L27
Since: 3.16.0
NONE ​
NONE: number ​
Description:
No scaling happens at all. The canvas is set to the size given in the game config and Phaser doesn't change it
again from that point on. If you change the canvas size, either via CSS, or directly via code, then you need
to call the Scale Managers resize method to give the new dimensions, or input events will stop working.
Source: src/scale/const/SCALE_MODE_CONST.js#L27
Since: 3.16.0
PORTRAIT ​
PORTRAIT: string ​
Description:
The primary portrait orientation.
Source: src/scale/const/ORIENTATION_CONST.js#L47
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
ZOOM_2X ​
ZOOM_2X: number ​
Description:
The game canvas will be 2x zoomed by Phaser.
Source: src/scale/const/ZOOM_CONST.js#L37
Since: 3.16.0
ZOOM_4X ​
ZOOM_4X: number ​
Description:
The game canvas will be 4x zoomed by Phaser.
Source: src/scale/const/ZOOM_CONST.js#L47
Since: 3.16.0
Previous
Phaser.Scale.Zoom
Next
Phaser.ScaleModes
Static functions
Static functions
Static functions
CenterType
OrientationType
ScaleModeType
ZoomType
Static functions
CENTER_BOTH
CENTER_HORIZONTALLY
CENTER_VERTICALLY
ENVELOP
EXPAND
FIT
HEIGHT_CONTROLS_WIDTH
LANDSCAPE
MAX_ZOOM
NO_CENTER
NO_ZOOM
NONE
PORTRAIT
RESIZE
WIDTH_CONTROLS_HEIGHT
ZOOM_2X
ZOOM_4X
