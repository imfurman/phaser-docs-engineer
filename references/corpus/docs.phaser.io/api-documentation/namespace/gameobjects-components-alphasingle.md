# Phaser.GameObjects.Components.AlphaSingle | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-alphasingle

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.AlphaSingle
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.AlphaSingle
Scope: static
Source: src/gameobjects/components/AlphaSingle.js#L12
Since: 3.22.0
Static functions ​
alpha ​
alpha: number ​
Description:
The alpha value of the Game Object.
This is a global value, impacting the entire Game Object, not just a region of it.
Source: src/gameobjects/components/AlphaSingle.js#L68
Since: 3.0.0
Static functions ​
clearAlpha ​
<instance> clearAlpha() ​
Description:
Clears all alpha values associated with this Game Object.
Immediately sets the alpha levels back to 1 (fully opaque).
Returns: Phaser.GameObjects.Components.AlphaSingle - This Game Object instance.
Source: src/gameobjects/components/AlphaSingle.js#L33
Since: 3.0.0
setAlpha ​
<instance> setAlpha([value]) ​
Description:
Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.
Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.
Parameters:
name type optional default description
value number Yes 1 The alpha value applied across the whole Game Object.
Returns: Phaser.GameObjects.Components.AlphaSingle - This Game Object instance.
Source: src/gameobjects/components/AlphaSingle.js#L48
Since: 3.0.0
Previous
Phaser.GameObjects.Components.Alpha
Next
Phaser.GameObjects.Components.BlendMode
Static functions
alpha
Static functions
clearAlpha
setAlpha
