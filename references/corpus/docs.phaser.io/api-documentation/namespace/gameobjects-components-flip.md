# Phaser.GameObjects.Components.Flip | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-flip

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Flip
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Flip
Scope: static
Source: src/gameobjects/components/Flip.js#L7
Since: 3.0.0
Static functions ​
flipX ​
flipX: boolean ​
Description:
The horizontally flipped state of the Game Object.
A Game Object that is flipped horizontally will render inversed on the horizontal axis.
Flipping always takes place from the middle of the texture and does not impact the scale value.
If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.
Source: src/gameobjects/components/Flip.js#L17
Since: 3.0.0
flipY ​
flipY: boolean ​
Description:
The vertically flipped state of the Game Object.
A Game Object that is flipped vertically will render inversed on the vertical axis (i.e. upside down)
Flipping always takes place from the middle of the texture and does not impact the scale value.
If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.
Source: src/gameobjects/components/Flip.js#L31
Since: 3.0.0
Static functions ​
resetFlip ​
<instance> resetFlip() ​
Description:
Resets the horizontal and vertical flipped state of this Game Object back to their default un-flipped state.
Returns: Phaser.GameObjects.Components.Flip - This Game Object instance.
Source: src/gameobjects/components/Flip.js#L140
Since: 3.0.0
setFlip ​
<instance> setFlip(x, y) ​
Description:
Sets the horizontal and vertical flipped state of this Game Object.
A Game Object that is flipped will render inversed on the flipped axis.
Flipping always takes place from the middle of the texture and does not impact the scale value.
If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.
Parameters:
name type optional description
x boolean No The horizontal flipped state. false for no flip, or true to be flipped.
y boolean No The horizontal flipped state. false for no flip, or true to be flipped.
Returns: Phaser.GameObjects.Components.Flip - This Game Object instance.
Source: src/gameobjects/components/Flip.js#L117
Since: 3.0.0
setFlipX ​
<instance> setFlipX(value) ​
Description:
Sets the horizontal flipped state of this Game Object.
A Game Object that is flipped horizontally will render inversed on the horizontal axis.
Flipping always takes place from the middle of the texture and does not impact the scale value.
If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.
Parameters:
name type optional description
value boolean No The flipped state. false for no flip, or true to be flipped.
Returns: Phaser.GameObjects.Components.Flip - This Game Object instance.
Source: src/gameobjects/components/Flip.js#L79
Since: 3.0.0
setFlipY ​
<instance> setFlipY(value) ​
Description:
Sets the vertical flipped state of this Game Object.
Parameters:
name type optional description
value boolean No The flipped state. false for no flip, or true to be flipped.
Returns: Phaser.GameObjects.Components.Flip - This Game Object instance.
Source: src/gameobjects/components/Flip.js#L100
Since: 3.0.0
toggleFlipX ​
<instance> toggleFlipX() ​
Description:
Toggles the horizontal flipped state of this Game Object.
A Game Object that is flipped horizontally will render inversed on the horizontal axis.
Flipping always takes place from the middle of the texture and does not impact the scale value.
If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.
Returns: Phaser.GameObjects.Components.Flip - This Game Object instance.
Source: src/gameobjects/components/Flip.js#L45
Since: 3.0.0
toggleFlipY ​
<instance> toggleFlipY() ​
Description:
Toggles the vertical flipped state of this Game Object.
Returns: Phaser.GameObjects.Components.Flip - This Game Object instance.
Source: src/gameobjects/components/Flip.js#L64
Since: 3.0.0
Previous
Phaser.GameObjects.Components.Depth
Next
Phaser.GameObjects.Components.GetBounds
Static functions
flipX
flipY
Static functions
resetFlip
setFlip
setFlipX
setFlipY
toggleFlipX
toggleFlipY
