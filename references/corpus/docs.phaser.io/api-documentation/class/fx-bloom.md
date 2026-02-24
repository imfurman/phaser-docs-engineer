# Bloom | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-bloom

Phaser API Documentation
Class
Bloom
Version: Phaser v3.90.0
On this page
Bloom
The Bloom FX Controller.
This FX controller manages the bloom effect for a Game Object.
Bloom is an effect used to reproduce an imaging artifact of real-world cameras.
The effect produces fringes of light extending from the borders of bright areas in an image,
contributing to the illusion of an extremely bright light overwhelming the
camera or eye capturing the scene.
A Bloom effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addBloom ( ) ;
sprite . postFX . addBloom ( ) ;
Constructor
new Bloom(gameObject, [color], [offsetX], [offsetY], [blurStrength], [strength], [steps])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
color number Yes "0xffffff" The color of the Bloom, as a hex value.
offsetX number Yes 1 The horizontal offset of the bloom effect.
offsetY number Yes 1 The vertical offset of the bloom effect.
blurStrength number Yes 1 The strength of the blur process of the bloom effect.
strength number Yes 1 The strength of the blend process of the bloom effect.
steps number Yes 4 The number of steps to run the Bloom effect for. This value should always be an integer.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Bloom.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
blurStrength ​
blurStrength: number ​
Description:
The strength of the blur process of the bloom effect.
Source: src/fx/Bloom.js#L96
Since: 3.60.0
color ​
color: number ​
Description:
The color of the bloom as a number value.
Source: src/fx/Bloom.js#L129
Since: 3.60.0
glcolor ​
glcolor: Array.<number> ​
Description:
The internal gl color array.
Source: src/fx/Bloom.js#L114
Since: 3.60.0
offsetX ​
offsetX: number ​
Description:
The horizontal offset of the bloom effect.
Source: src/fx/Bloom.js#L78
Since: 3.60.0
offsetY ​
offsetY: number ​
Description:
The vertical offset of the bloom effect.
Source: src/fx/Bloom.js#L87
Since: 3.60.0
steps ​
steps: number ​
Description:
The number of steps to run the Bloom effect for.
This value should always be an integer.
It defaults to 4. The higher the value, the smoother the Bloom,
but at the cost of exponentially more gl operations.
Keep this to the lowest possible number you can have it, while
still looking correct for your game.
Source: src/fx/Bloom.js#L61
Since: 3.60.0
strength ​
strength: number ​
Description:
The strength of the blend process of the bloom effect.
Source: src/fx/Bloom.js#L105
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Barrel
Next
Blur
Inherited Members
Public Members
blurStrength
color
glcolor
offsetX
offsetY
steps
strength
Inherited Methods
