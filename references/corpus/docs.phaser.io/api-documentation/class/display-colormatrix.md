# ColorMatrix | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/display-colormatrix

Phaser API Documentation
Class
ColorMatrix
Version: Phaser v3.90.0
On this page
ColorMatrix
The ColorMatrix class creates a 5x4 matrix that can be used in shaders and graphics
operations. It provides methods required to modify the color values, such as adjusting
the brightness, setting a sepia tone, hue rotation and more.
Use the method getData to return a Float32Array containing the current color values.
Scope : static
Source: src/display/ColorMatrix.js#L11
Since: 3.50.0
Public Members ​
alpha ​
alpha: number ​
Description:
The value that determines how much of the original color is used
when mixing the colors. A value between 0 (all original) and 1 (all final)
Source: src/display/ColorMatrix.js#L40
Since: 3.50.0
Public Methods ​
blackWhite ​
<instance> blackWhite([multiply]) ​
Description:
Sets this ColorMatrix to be black and white.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L271
Since: 3.50.0
brightness ​
<instance> brightness([value], [multiply]) ​
Description:
Changes the brightness of this ColorMatrix by the given amount.
Parameters:
name type optional default description
value number Yes 0 The amount of brightness to apply to this ColorMatrix. Between 0 (black) and 1.
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L150
Since: 3.50.0
brown ​
<instance> brown([multiply]) ​
Description:
Applies a brown tone to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L407
Since: 3.50.0
contrast ​
<instance> contrast([value], [multiply]) ​
Description:
Change the contrast of this ColorMatrix by the amount given.
Parameters:
name type optional default description
value number Yes 0 The amount of contrast to apply to this ColorMatrix.
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L288
Since: 3.50.0
desaturateLuminance ​
<instance> desaturateLuminance([multiply]) ​
Description:
Apply a desaturated luminance to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L332
Since: 3.50.0
getData ​
<instance> getData() ​
Description:
Gets the ColorMatrix as a Float32Array.
Can be used directly as a 1fv shader uniform value.
Returns: Float32Array - The ColorMatrix as a Float32Array.
Source: src/display/ColorMatrix.js#L121
Since: 3.50.0
grayscale ​
<instance> grayscale([value], [multiply]) ​
Description:
Sets this ColorMatrix to be grayscale.
Parameters:
name type optional default description
value number Yes 1 The grayscale scale (0 is black).
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L252
Since: 3.50.0
hue ​
<instance> hue([rotation], [multiply]) ​
Description:
Rotates the hues of this ColorMatrix by the value given.
Parameters:
name type optional default description
rotation number Yes 0 The amount of hue rotation to apply to this ColorMatrix, in degrees.
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L220
Since: 3.50.0
kodachrome ​
<instance> kodachrome([multiply]) ​
Description:
Applies a kodachrome color effect to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L441
Since: 3.50.0
lsd ​
<instance> lsd([multiply]) ​
Description:
Applies a trippy color tone to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L390
Since: 3.50.0
multiply ​
<instance> multiply(a, [multiply]) ​
Description:
Multiplies the two given matrices.
Parameters:
name type optional default description
a Array.<number> No The 5x4 array to multiply with ColorMatrix._matrix.
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L509
Since: 3.50.0
negative ​
<instance> negative([multiply]) ​
Description:
Converts this ColorMatrix to have negative values.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L315
Since: 3.50.0
night ​
<instance> night([intensity], [multiply]) ​
Description:
Applies a night vision tone to this ColorMatrix.
Parameters:
name type optional default description
intensity number Yes 0.1 The intensity of this effect.
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L366
Since: 3.50.0
polaroid ​
<instance> polaroid([multiply]) ​
Description:
Applies a polaroid color effect to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L475
Since: 3.50.0
reset ​
<instance> reset() ​
Description:
Resets the ColorMatrix to default values and also resets
the alpha property back to 1.
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L94
Since: 3.50.0
saturate ​
<instance> saturate([value], [multiply]) ​
Description:
Changes the saturation of this ColorMatrix by the given amount.
Parameters:
name type optional default description
value number Yes 0 The amount of saturation to apply to this ColorMatrix.
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L176
Since: 3.50.0
saturation ​
<instance> saturation([multiply]) ​
Description:
Desaturates this ColorMatrix (removes color from it).
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L203
Since: 3.50.0
sepia ​
<instance> sepia([multiply]) ​
Description:
Applies a sepia tone to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L349
Since: 3.50.0
set ​
<instance> set(value) ​
Description:
Sets this ColorMatrix from the given array of color values.
Parameters:
name type optional description
value Array.<number> | Float32Array No The ColorMatrix values to set. Must have 20 elements.
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L75
Since: 3.50.0
shiftToBGR ​
<instance> shiftToBGR([multiply]) ​
Description:
Shifts the values of this ColorMatrix into BGR order.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L492
Since: 3.50.0
technicolor ​
<instance> technicolor([multiply]) ​
Description:
Applies a technicolor color effect to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L458
Since: 3.50.0
vintagePinhole ​
<instance> vintagePinhole([multiply]) ​
Description:
Applies a vintage pinhole color effect to this ColorMatrix.
Parameters:
name type optional default description
multiply boolean Yes false Multiply the resulting ColorMatrix ( true ), or set it ( false ) ?
Returns: Phaser.Display.ColorMatrix - This ColorMatrix instance.
Source: src/display/ColorMatrix.js#L424
Since: 3.50.0
Constants: ​
Public Members ​
BLACK_WHITE ​
BLACK_WHITE: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for black_white operations.
Source: src/display/ColorMatrix.js#L575
Since: 3.60.0
BROWN ​
BROWN: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for brown operations.
Source: src/display/ColorMatrix.js#L625
Since: 3.60.0
DESATURATE_LUMINANCE ​
DESATURATE_LUMINANCE: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for desatured luminance operations.
Source: src/display/ColorMatrix.js#L595
Since: 3.60.0
KODACHROME ​
KODACHROME: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for kodachrome operations.
Source: src/display/ColorMatrix.js#L645
Since: 3.60.0
LSD ​
LSD: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for lsd operations.
Source: src/display/ColorMatrix.js#L615
Since: 3.60.0
NEGATIVE ​
NEGATIVE: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for negative operations.
Source: src/display/ColorMatrix.js#L585
Since: 3.60.0
POLAROID ​
POLAROID: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for polaroid shift operations.
Source: src/display/ColorMatrix.js#L665
Since: 3.60.0
SEPIA ​
SEPIA: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for sepia operations.
Source: src/display/ColorMatrix.js#L605
Since: 3.60.0
SHIFT_BGR ​
SHIFT_BGR: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for shift BGR operations.
Source: src/display/ColorMatrix.js#L675
Since: 3.60.0
TECHNICOLOR ​
TECHNICOLOR: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for technicolor operations.
Source: src/display/ColorMatrix.js#L655
Since: 3.60.0
VINTAGE ​
VINTAGE: Array.<number> ​
Description:
A constant array used by the ColorMatrix class for vintage pinhole operations.
Source: src/display/ColorMatrix.js#L635
Since: 3.60.0
Previous
Color
Next
BitmapMask
Public Members
alpha
Public Methods
blackWhite
brightness
brown
contrast
desaturateLuminance
getData
grayscale
hue
kodachrome
lsd
multiply
negative
night
polaroid
reset
saturate
saturation
sepia
set
shiftToBGR
technicolor
vintagePinhole
Constants:
Public Members
BLACK_WHITE
BROWN
DESATURATE_LUMINANCE
KODACHROME
LSD
NEGATIVE
POLAROID
SEPIA
SHIFT_BGR
TECHNICOLOR
VINTAGE
