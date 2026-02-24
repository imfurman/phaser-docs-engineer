# Barrel | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-barrel

Phaser API Documentation
Class
Barrel
Version: Phaser v3.90.0
On this page
Barrel
The Barrel FX Controller.
This FX controller manages the barrel distortion effect for a Game Object.
A barrel effect allows you to apply either a 'pinch' or 'expand' distortion to
a Game Object. The amount of the effect can be modified in real-time.
A Barrel effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addBarrel ( ) ;
sprite . postFX . addBarrel ( ) ;
Constructor
new Barrel(gameObject, [amount])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
amount number Yes 1 The amount of distortion applied to the barrel effect. A value of 1 is no distortion. Typically keep this within +- 1.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Barrel.js#L11
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
The amount of distortion applied to the barrel effect.
Typically keep this within the range 1 (no distortion) to +- 1.
Source: src/fx/Barrel.js#L50
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
EventEmitter
Next
Bloom
Inherited Members
Public Members
amount
Inherited Methods
