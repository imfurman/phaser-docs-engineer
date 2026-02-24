# Glow | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-glow

Phaser API Documentation
Class
Glow
Version: Phaser v3.90.0
On this page
Glow
The Glow FX Controller.
This FX controller manages the glow effect for a Game Object.
The glow effect is a visual technique that creates a soft, luminous halo around game objects,
characters, or UI elements. This effect is used to emphasize importance, enhance visual appeal,
or convey a sense of energy, magic, or otherworldly presence. The effect can also be set on
the inside of the Game Object. The color and strength of the glow can be modified.
A Glow effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addGlow ( ) ;
sprite . postFX . addGlow ( ) ;
Constructor
new Glow(gameObject, [color], [outerStrength], [innerStrength], [knockout])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
color number Yes "0xffffff" The color of the glow effect as a number value.
outerStrength number Yes 4 The strength of the glow outward from the edge of the Sprite.
innerStrength number Yes 0 The strength of the glow inward from the edge of the Sprite.
knockout boolean Yes false If true only the glow is drawn, not the texture itself.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Glow.js#L11
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
The color of the glow as a number value.
Source: src/fx/Glow.js#L99
Since: 3.60.0
glcolor ​
glcolor: Array.<number> ​
Description:
A 4 element array of gl color values.
Source: src/fx/Glow.js#L84
Since: 3.60.0
innerStrength ​
innerStrength: number ​
Description:
The strength of the glow inward from the edge of the Sprite.
Source: src/fx/Glow.js#L66
Since: 3.60.0
knockout ​
knockout: number ​
Description:
If true only the glow is drawn, not the texture itself.
Source: src/fx/Glow.js#L75
Since: 3.60.0
outerStrength ​
outerStrength: number ​
Description:
The strength of the glow outward from the edge of the Sprite.
Source: src/fx/Glow.js#L57
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Displacement
Next
Gradient
Inherited Members
Public Members
color
glcolor
innerStrength
knockout
outerStrength
Inherited Methods
