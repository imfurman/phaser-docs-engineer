# Vignette | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-vignette

Phaser API Documentation
Class
Vignette
Version: Phaser v3.90.0
On this page
Vignette
The Vignette FX Controller.
This FX controller manages the vignette effect for a Game Object.
The vignette effect is a visual technique where the edges of the screen, or a Game Object, gradually darken or blur,
creating a frame-like appearance. This effect is used to draw the player's focus towards the central action or subject,
enhance immersion, and provide a cinematic or artistic quality to the game's visuals.
A Vignette effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addVignette ( ) ;
sprite . postFX . addVignette ( ) ;
Constructor
new Vignette(gameObject, [x], [y], [radius], [strength])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
x number Yes 0.5 The horizontal offset of the vignette effect. This value is normalized to the range 0 to 1.
y number Yes 0.5 The vertical offset of the vignette effect. This value is normalized to the range 0 to 1.
radius number Yes 0.5 The radius of the vignette effect. This value is normalized to the range 0 to 1.
strength number Yes 0.5 The strength of the vignette effect.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Vignette.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
radius ​
radius: number ​
Description:
The radius of the vignette effect. This value is normalized to the range 0 to 1.
Source: src/fx/Vignette.js#L75
Since: 3.60.0
strength ​
strength: number ​
Description:
The strength of the vignette effect.
Source: src/fx/Vignette.js#L84
Since: 3.60.0
x ​
x: number ​
Description:
The horizontal offset of the vignette effect. This value is normalized to the range 0 to 1.
Source: src/fx/Vignette.js#L57
Since: 3.60.0
y ​
y: number ​
Description:
The vertical offset of the vignette effect. This value is normalized to the range 0 to 1.
Source: src/fx/Vignette.js#L66
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Shine
Next
Wipe
Inherited Members
Public Members
radius
strength
x
y
Inherited Methods
