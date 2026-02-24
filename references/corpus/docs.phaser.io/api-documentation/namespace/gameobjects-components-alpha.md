# Phaser.GameObjects.Components.Alpha | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-alpha

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Alpha
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Alpha
Scope: static
Source: src/gameobjects/components/Alpha.js#L12
Since: 3.0.0
Static functions ​
alpha ​
alpha: number ​
Description:
The alpha value of the Game Object.
This is a global value, impacting the entire Game Object, not just a region of it.
Source: src/gameobjects/components/Alpha.js#L129
Since: 3.0.0
alphaBottomLeft ​
alphaBottomLeft: number ​
Description:
The alpha value starting from the bottom-left of the Game Object.
This value is interpolated from the corner to the center of the Game Object.
Tags:
webglOnly
Source: src/gameobjects/components/Alpha.js#L227
Since: 3.0.0
alphaBottomRight ​
alphaBottomRight: number ​
Description:
The alpha value starting from the bottom-right of the Game Object.
This value is interpolated from the corner to the center of the Game Object.
Tags:
webglOnly
Source: src/gameobjects/components/Alpha.js#L257
Since: 3.0.0
alphaTopLeft ​
alphaTopLeft: number ​
Description:
The alpha value starting from the top-left of the Game Object.
This value is interpolated from the corner to the center of the Game Object.
Tags:
webglOnly
Source: src/gameobjects/components/Alpha.js#L167
Since: 3.0.0
alphaTopRight ​
alphaTopRight: number ​
Description:
The alpha value starting from the top-right of the Game Object.
This value is interpolated from the corner to the center of the Game Object.
Tags:
webglOnly
Source: src/gameobjects/components/Alpha.js#L197
Since: 3.0.0
Static functions ​
clearAlpha ​
<instance> clearAlpha() ​
Description:
Clears all alpha values associated with this Game Object.
Immediately sets the alpha levels back to 1 (fully opaque).
Returns: Phaser.GameObjects.Components.Alpha - This Game Object instance.
Source: src/gameobjects/components/Alpha.js#L77
Since: 3.0.0
setAlpha ​
<instance> setAlpha([topLeft], [topRight], [bottomLeft], [bottomRight]) ​
Description:
Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.
Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.
If your game is running under WebGL you can optionally specify four different alpha values, each of which
correspond to the four corners of the Game Object. Under Canvas only the topLeft value given is used.
Parameters:
name type optional default description
topLeft number Yes 1 The alpha value used for the top-left of the Game Object. If this is the only value given it's applied across the whole Game Object.
topRight number Yes The alpha value used for the top-right of the Game Object. WebGL only.
bottomLeft number Yes The alpha value used for the bottom-left of the Game Object. WebGL only.
bottomRight number Yes The alpha value used for the bottom-right of the Game Object. WebGL only.
Returns: Phaser.GameObjects.Components.Alpha - This Game Object instance.
Source: src/gameobjects/components/Alpha.js#L92
Since: 3.0.0
Previous
Phaser.FX
Next
Phaser.GameObjects.Components.AlphaSingle
Static functions
alpha
alphaBottomLeft
alphaBottomRight
alphaTopLeft
alphaTopRight
Static functions
clearAlpha
setAlpha
