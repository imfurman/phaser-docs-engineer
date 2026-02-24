# Phaser.Display.Color.Interpolate | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/display-color-interpolate

Phaser API Documentation
Namespaces
Phaser.Display.Color.Interpolate
Version: Phaser v3.90.0
On this page
Phaser.Display.Color.Interpolate
Scope: static
Source: src/display/color/Interpolate.js#L10
Since: 3.0.0
Static functions ​
ColorWithColor ​
<static> ColorWithColor(color1, color2, [length], [index]) ​
Description:
Interpolates between the two given color objects over the length supplied.
Parameters:
name type optional default description
color1 Phaser.Display.Color No The first Color object.
color2 Phaser.Display.Color No The second Color object.
length number Yes 100 Distance to interpolate over.
index number Yes 0 Index to start from.
Returns: Phaser.Types.Display.ColorObject - An object containing the interpolated color values.
Source: src/display/color/Interpolate.js#L54
Since: 3.0.0
ColorWithRGB ​
<static> ColorWithRGB(color1, r, g, b, [length], [index]) ​
Description:
Interpolates between the Color object and color values over the length supplied.
Parameters:
name type optional default description
color1 Phaser.Display.Color No The first Color object.
r number No Red value.
g number No Blue value.
b number No Green value.
length number Yes 100 Distance to interpolate over.
index number Yes 0 Index to start from.
Returns: Phaser.Types.Display.ColorObject - An object containing the interpolated color values.
Source: src/display/color/Interpolate.js#L77
Since: 3.0.0
RGBWithRGB ​
<static> RGBWithRGB(r1, g1, b1, r2, g2, b2, [length], [index]) ​
Description:
Interpolates between the two given color ranges over the length supplied.
Parameters:
name type optional default description
r1 number No Red value.
g1 number No Blue value.
b1 number No Green value.
r2 number No Red value.
g2 number No Blue value.
b2 number No Green value.
length number Yes 100 Distance to interpolate over.
index number Yes 0 Index to start from.
Returns: Phaser.Types.Display.ColorObject - An object containing the interpolated color values.
Source: src/display/color/Interpolate.js#L16
Since: 3.0.0
Previous
Phaser.Display.Canvas
Next
Phaser.Display.Color
Static functions
ColorWithColor
ColorWithRGB
RGBWithRGB
