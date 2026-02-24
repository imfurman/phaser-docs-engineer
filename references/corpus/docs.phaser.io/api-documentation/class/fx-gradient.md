# Gradient | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-gradient

Phaser API Documentation
Class
Gradient
Version: Phaser v3.90.0
On this page
Gradient
The Gradient FX Controller.
This FX controller manages the gradient effect for a Game Object.
The gradient overlay effect is a visual technique where a smooth color transition is applied over Game Objects,
such as sprites or UI components. This effect is used to enhance visual appeal, emphasize depth, or create
stylistic and atmospheric variations. It can also be utilized to convey information, such as representing
progress or health status through color changes.
A Gradient effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addGradient ( ) ;
sprite . postFX . addGradient ( ) ;
Constructor
new Gradient(gameObject, [color1], [color2], [alpha], [fromX], [fromY], [toX], [toY], [size])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
color1 number Yes "0xff0000" The first gradient color, given as a number value.
color2 number Yes "0x00ff00" The second gradient color, given as a number value.
alpha number Yes 0.2 The alpha value of the gradient effect.
fromX number Yes 0 The horizontal position the gradient will start from. This value is normalized, between 0 and 1, and is not in pixels.
fromY number Yes 0 The vertical position the gradient will start from. This value is normalized, between 0 and 1, and is not in pixels.
toX number Yes 0 The horizontal position the gradient will end at. This value is normalized, between 0 and 1, and is not in pixels.
toY number Yes 1 The vertical position the gradient will end at. This value is normalized, between 0 and 1, and is not in pixels.
size number Yes 0 How many 'chunks' the gradient is divided in to, as spread over the entire height of the texture. Leave this at zero for a smooth gradient, or set higher for a more retro chunky effect.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Gradient.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
alpha ​
alpha: number ​
Description:
The alpha value of the gradient effect.
Source: src/fx/Gradient.js#L64
Since: 3.60.0
color1 ​
color1: number ​
Description:
The first gradient color, given as a number value.
Source: src/fx/Gradient.js#L150
Since: 3.60.0
color2 ​
color2: number ​
Description:
The second gradient color, given as a number value.
Source: src/fx/Gradient.js#L177
Since: 3.60.0
fromX ​
fromX: number ​
Description:
The horizontal position the gradient will start from. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/fx/Gradient.js#L85
Since: 3.60.0
fromY ​
fromY: number ​
Description:
The vertical position the gradient will start from. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/fx/Gradient.js#L94
Since: 3.60.0
glcolor1 ​
glcolor1: Array.<number> ​
Description:
The internal gl color array for the starting color.
Source: src/fx/Gradient.js#L121
Since: 3.60.0
glcolor2 ​
glcolor2: Array.<number> ​
Description:
The internal gl color array for the ending color.
Source: src/fx/Gradient.js#L130
Since: 3.60.0
size ​
size: number ​
Description:
Sets how many 'chunks' the gradient is divided in to, as spread over the
entire height of the texture. Leave this at zero for a smooth gradient,
or set to a higher number to split the gradient into that many sections, giving
a more banded 'retro' effect.
Source: src/fx/Gradient.js#L73
Since: 3.60.0
toX ​
toX: number ​
Description:
The horizontal position the gradient will end. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/fx/Gradient.js#L103
Since: 3.60.0
toY ​
toY: number ​
Description:
The vertical position the gradient will end. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/fx/Gradient.js#L112
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Glow
Next
Pixelate
Inherited Members
Public Members
alpha
color1
color2
fromX
fromY
glcolor1
glcolor2
size
toX
toY
Inherited Methods
