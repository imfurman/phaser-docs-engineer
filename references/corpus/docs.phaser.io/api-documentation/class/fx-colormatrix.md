# ColorMatrix | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-colormatrix

Phaser API Documentation
Class
ColorMatrix
Version: Phaser v3.90.0
On this page
ColorMatrix
The ColorMatrix FX Controller.
This FX controller manages the color matrix effect for a Game Object.
The color matrix effect is a visual technique that involves manipulating the colors of an image
or scene using a mathematical matrix. This process can adjust hue, saturation, brightness, and contrast,
allowing developers to create various stylistic appearances or mood settings within the game.
Common applications include simulating different lighting conditions, applying color filters,
or achieving a specific visual style.
A ColorMatrix effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addColorMatrix ( ) ;
sprite . postFX . addColorMatrix ( ) ;
Constructor
new ColorMatrix(gameObject)
Parameters
name type optional description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
Scope : static
Extends
Phaser.Display.ColorMatrix
Source: src/fx/ColorMatrix.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.Display.ColorMatrix :
alpha
Public Members ​
active ​
active: boolean ​
Description:
Toggle this boolean to enable or disable this effect,
without removing and adding it from the Game Object.
Source: src/fx/ColorMatrix.js#L68
Since: 3.60.0
gameObject ​
gameObject: Phaser.GameObjects.GameObject ​
Description:
A reference to the Game Object that owns this effect.
Source: src/fx/ColorMatrix.js#L59
Since: 3.60.0
type ​
type: number ​
Description:
The FX_CONST type of this effect.
Source: src/fx/ColorMatrix.js#L50
Since: 3.60.0
Inherited Methods ​
From Phaser.Display.ColorMatrix :
blackWhite
brightness
brown
contrast
desaturateLuminance
getData
grayscale
hue
kodachrome
lsd
multiply
negative
night
polaroid
reset
saturate
saturation
sepia
set
shiftToBGR
technicolor
vintagePinhole
Previous
Circle
Next
Controller
Inherited Members
Public Members
active
gameObject
type
Inherited Methods
