# Pixelate | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-pixelate

Phaser API Documentation
Class
Pixelate
Version: Phaser v3.90.0
On this page
Pixelate
The Pixelate FX Controller.
This FX controller manages the pixelate effect for a Game Object.
The pixelate effect is a visual technique that deliberately reduces the resolution or detail of an image,
creating a blocky or mosaic appearance composed of large, visible pixels. This effect can be used for stylistic
purposes, as a homage to retro gaming, or as a means to obscure certain elements within the game, such as
during a transition or to censor specific content.
A Pixelate effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addPixelate ( ) ;
sprite . postFX . addPixelate ( ) ;
Constructor
new Pixelate(gameObject, [amount])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
amount number Yes 1 The amount of pixelation to apply.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Pixelate.js#L11
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
The amount of pixelation to apply.
Source: src/fx/Pixelate.js#L52
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Gradient
Next
Shadow
Inherited Members
Public Members
amount
Inherited Methods
