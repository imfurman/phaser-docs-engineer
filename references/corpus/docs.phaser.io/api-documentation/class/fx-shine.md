# Shine | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-shine

Phaser API Documentation
Class
Shine
Version: Phaser v3.90.0
On this page
Shine
The Shine FX Controller.
This FX controller manages the shift effect for a Game Object.
The shine effect is a visual technique that simulates the appearance of reflective
or glossy surfaces by passing a light beam across a Game Object. This effect is used to
enhance visual appeal, emphasize certain features, and create a sense of depth or
material properties.
A Shine effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addShine ( ) ;
sprite . postFX . addShine ( ) ;
Constructor
new Shine(gameObject, [speed], [lineWidth], [gradient], [reveal])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
speed number Yes 0.5 The speed of the Shine effect.
lineWidth number Yes 0.5 The line width of the Shine effect.
gradient number Yes 3 The gradient of the Shine effect.
reveal boolean Yes false Does this Shine effect reveal or get added to its target?
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Shine.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
gradient ​
gradient: number ​
Description:
The gradient of the Shine effect.
Source: src/fx/Shine.js#L76
Since: 3.60.0
lineWidth ​
lineWidth: number ​
Description:
The line width of the Shine effect.
Source: src/fx/Shine.js#L67
Since: 3.60.0
reveal ​
reveal: boolean ​
Description:
Does this Shine effect reveal or get added to its target?
Source: src/fx/Shine.js#L85
Since: 3.60.0
speed ​
speed: number ​
Description:
The speed of the Shine effect.
Source: src/fx/Shine.js#L58
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Shadow
Next
Vignette
Inherited Members
Public Members
gradient
lineWidth
reveal
speed
Inherited Methods
