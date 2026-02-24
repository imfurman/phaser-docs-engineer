# Blur | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-blur

Phaser API Documentation
Class
Blur
Version: Phaser v3.90.0
On this page
Blur
The Blur FX Controller.
This FX controller manages the blur effect for a Game Object.
A Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect,
typically to reduce image noise and reduce detail. The visual effect of this blurring technique is a
smooth blur resembling that of viewing the image through a translucent screen, distinctly different
from the bokeh effect produced by an out-of-focus lens or the shadow of an object under usual illumination.
A Blur effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addBlur ( ) ;
sprite . postFX . addBlur ( ) ;
Constructor
new Blur(gameObject, [quality], [x], [y], [strength], [color], [steps])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
quality number Yes 0 The quality of the blur effect. Can be either 0 for Low Quality, 1 for Medium Quality or 2 for High Quality.
x number Yes 2 The horizontal offset of the blur effect.
y number Yes 2 The vertical offset of the blur effect.
strength number Yes 1 The strength of the blur effect.
color number Yes "0xffffff" The color of the blur, as a hex value.
steps number Yes 4 The number of steps to run the blur effect for. This value should always be an integer.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Blur.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
color ​
color: number ​
Description:
The color of the blur as a number value.
Source: src/fx/Blur.js#L143
Since: 3.60.0
glcolor ​
glcolor: Array.<number> ​
Description:
The internal gl color array.
Source: src/fx/Blur.js#L128
Since: 3.60.0
quality ​
quality: number ​
Description:
The quality of the blur effect.
This can be:
0 for Low Quality
1 for Medium Quality
2 for High Quality
The higher the quality, the more complex shader is used
and the more processing time is spent on the GPU calculating
the final blur. This value is used in conjunction with the
steps value, as one has a direct impact on the other.
Keep this value as low as you can, while still achieving the
desired effect you need for your game.
Source: src/fx/Blur.js#L61
Since: 3.60.0
steps ​
steps: number ​
Description:
The number of steps to run the Blur effect for.
This value should always be an integer.
It defaults to 4. The higher the value, the smoother the blur,
but at the cost of exponentially more gl operations.
Keep this to the lowest possible number you can have it, while
still looking correct for your game.
Source: src/fx/Blur.js#L102
Since: 3.60.0
strength ​
strength: number ​
Description:
The strength of the blur effect.
Source: src/fx/Blur.js#L119
Since: 3.60.0
x ​
x: number ​
Description:
The horizontal offset of the blur effect.
Source: src/fx/Blur.js#L84
Since: 3.60.0
y ​
y: number ​
Description:
The vertical offset of the blur effect.
Source: src/fx/Blur.js#L93
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Bloom
Next
Bokeh
Inherited Members
Public Members
color
glcolor
quality
steps
strength
x
y
Inherited Methods
