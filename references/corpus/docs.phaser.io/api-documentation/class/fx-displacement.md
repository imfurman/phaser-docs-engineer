# Displacement | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-displacement

Phaser API Documentation
Class
Displacement
Version: Phaser v3.90.0
On this page
Displacement
The Displacement FX Controller.
This FX controller manages the displacement effect for a Game Object.
The displacement effect is a visual technique that alters the position of pixels in an image
or texture based on the values of a displacement map. This effect is used to create the illusion
of depth, surface irregularities, or distortion in otherwise flat elements. It can be applied to
characters, objects, or backgrounds to enhance realism, convey movement, or achieve various
stylistic appearances.
A Displacement effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addDisplacement ( ) ;
sprite . postFX . addDisplacement ( ) ;
Constructor
new Displacement(gameObject, [texture], [x], [y])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
texture string Yes "'__WHITE'" The unique string-based key of the texture to use for displacement, which must exist in the Texture Manager.
x number Yes 0.005 The amount of horizontal displacement to apply. A very small float number, such as 0.005.
y number Yes 0.005 The amount of vertical displacement to apply. A very small float number, such as 0.005.
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Displacement.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
glTexture ​
glTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper ​
Description:
The underlying texture used for displacement.
Source: src/fx/Displacement.js#L75
Since: 3.60.0
x ​
x: number ​
Description:
The amount of horizontal displacement to apply.
Source: src/fx/Displacement.js#L57
Since: 3.60.0
y ​
y: number ​
Description:
The amount of vertical displacement to apply.
Source: src/fx/Displacement.js#L66
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Public Methods ​
setTexture ​
<instance> setTexture([texture]) ​
Description:
Sets the Texture to be used for the displacement effect.
You can only use a whole texture, not a frame from a texture atlas or sprite sheet.
Parameters:
name type optional default description
texture string Yes "'__WHITE'" The unique string-based key of the texture to use for displacement, which must exist in the Texture Manager.
Returns: Phaser.FX.Displacement - This FX Controller.
Source: src/fx/Displacement.js#L87
Since: 3.60.0
Previous
Controller
Next
Glow
Inherited Members
Public Members
glTexture
x
y
Inherited Methods
Public Methods
setTexture
