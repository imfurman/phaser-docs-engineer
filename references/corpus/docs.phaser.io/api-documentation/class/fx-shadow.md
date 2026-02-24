# Shadow | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-shadow

Phaser API Documentation
Class
Shadow
Version: Phaser v3.90.0
On this page
Shadow
The Shadow FX Controller.
This FX controller manages the shadow effect for a Game Object.
The shadow effect is a visual technique used to create the illusion of depth and realism by adding darker,
offset silhouettes or shapes beneath game objects, characters, or environments. These simulated shadows
help to enhance the visual appeal and immersion, making the 2D game world appear more dynamic and three-dimensional.
A Shadow effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addShadow ( ) ;
sprite . postFX . addShadow ( ) ;
Constructor
new Shadow(gameObject, [x], [y], [decay], [power], [color], [samples], [intensity])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
x number Yes 0 The horizontal offset of the shadow effect.
y number Yes 0 The vertical offset of the shadow effect.
decay number Yes 0.1 The amount of decay for shadow effect.
power number Yes 1 The power of the shadow effect.
color number Yes "0x000000" The color of the shadow.
samples number Yes 6 The number of samples that the shadow effect will run for. An integer between 1 and 12.
intensity number Yes 1 The intensity of the shadow effect.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Shadow.js#L11
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
The color of the shadow.
Source: src/fx/Shadow.js#L133
Since: 3.60.0
decay ​
decay: number ​
Description:
The amount of decay for the shadow effect.
Source: src/fx/Shadow.js#L80
Since: 3.60.0
glcolor ​
glcolor: Array.<number> ​
Description:
The internal gl color array.
Source: src/fx/Shadow.js#L98
Since: 3.60.0
intensity ​
intensity: number ​
Description:
The intensity of the shadow effect.
Source: src/fx/Shadow.js#L118
Since: 3.60.0
power ​
power: number ​
Description:
The power of the shadow effect.
Source: src/fx/Shadow.js#L89
Since: 3.60.0
samples ​
samples: number ​
Description:
The number of samples that the shadow effect will run for.
This should be an integer with a minimum value of 1 and a maximum of 12.
Source: src/fx/Shadow.js#L107
Since: 3.60.0
x ​
x: number ​
Description:
The horizontal offset of the shadow effect.
Source: src/fx/Shadow.js#L62
Since: 3.60.0
y ​
y: number ​
Description:
The vertical offset of the shadow effect.
Source: src/fx/Shadow.js#L71
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Pixelate
Next
Shine
Inherited Members
Public Members
color
decay
glcolor
intensity
power
samples
x
y
Inherited Methods
