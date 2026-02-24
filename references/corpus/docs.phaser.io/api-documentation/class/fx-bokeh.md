# Bokeh | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-bokeh

Phaser API Documentation
Class
Bokeh
Version: Phaser v3.90.0
On this page
Bokeh
The Bokeh FX Controller.
This FX controller manages the bokeh effect for a Game Object.
Bokeh refers to a visual effect that mimics the photographic technique of creating a shallow depth of field.
This effect is used to emphasize the game's main subject or action, by blurring the background or foreground
elements, resulting in a more immersive and visually appealing experience. It is achieved through rendering
techniques that simulate the out-of-focus areas, giving a sense of depth and realism to the game's graphics.
This effect can also be used to generate a Tilt Shift effect, which is a technique used to create a miniature
effect by blurring everything except a small area of the image. This effect is achieved by blurring the
top and bottom elements, while keeping the center area in focus.
A Bokeh effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addBokeh ( ) ;
sprite . postFX . addBokeh ( ) ;
Constructor
new Bokeh(gameObject, [radius], [amount], [contrast], [isTiltShift], [blurX], [blurY], [strength])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
radius number Yes 0.5 The radius of the bokeh effect.
amount number Yes 1 The amount of the bokeh effect.
contrast number Yes 0.2 The color contrast of the bokeh effect.
isTiltShift boolean Yes false Is this a bokeh or Tile Shift effect?
blurX number Yes 1 If Tilt Shift, the amount of horizontal blur.
blurY number Yes 1 If Tilt Shift, the amount of vertical blur.
strength number Yes 1 If Tilt Shift, the strength of the blur.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Bokeh.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
amount ​
amount: number ​
Description:
The amount, or strength, of the bokeh effect. Defaults to 1.
Source: src/fx/Bokeh.js#L81
Since: 3.60.0
blurX ​
blurX: number ​
Description:
If a Tilt Shift effect this controls the amount of horizontal blur.
Setting this value on a non-Tilt Shift effect will have no effect.
Source: src/fx/Bokeh.js#L119
Since: 3.60.0
blurY ​
blurY: number ​
Description:
If a Tilt Shift effect this controls the amount of vertical blur.
Setting this value on a non-Tilt Shift effect will have no effect.
Source: src/fx/Bokeh.js#L130
Since: 3.60.0
contrast ​
contrast: number ​
Description:
The color contrast, or brightness, of the bokeh effect. Defaults to 0.2.
Source: src/fx/Bokeh.js#L90
Since: 3.60.0
isTiltShift ​
isTiltShift: boolean ​
Description:
Is this a Tilt Shift effect or a standard bokeh effect?
Source: src/fx/Bokeh.js#L99
Since: 3.60.0
radius ​
radius: number ​
Description:
The radius of the bokeh effect.
This is a float value, where a radius of 0 will result in no effect being applied,
and a radius of 1 will result in a strong bokeh. However, you can exceed this value
for even stronger effects.
Source: src/fx/Bokeh.js#L68
Since: 3.60.0
strength ​
strength: number ​
Description:
If a Tilt Shift effect this controls the strength of the blur.
Setting this value on a non-Tilt Shift effect will have no effect.
Source: src/fx/Bokeh.js#L108
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Blur
Next
Circle
Inherited Members
Public Members
amount
blurX
blurY
contrast
isTiltShift
radius
strength
Inherited Methods
