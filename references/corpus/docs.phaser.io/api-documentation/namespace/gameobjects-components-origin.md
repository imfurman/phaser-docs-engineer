# Phaser.GameObjects.Components.Origin | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-origin

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Origin
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Origin
Scope: static
Source: src/gameobjects/components/Origin.js#L7
Since: 3.0.0
Static functions ​
displayOriginX ​
displayOriginX: number ​
Description:
The horizontal display origin of this Game Object.
The origin is a normalized value between 0 and 1.
The displayOrigin is a pixel value, based on the size of the Game Object combined with the origin.
Source: src/gameobjects/components/Origin.js#L64
Since: 3.0.0
displayOriginY ​
displayOriginY: number ​
Description:
The vertical display origin of this Game Object.
The origin is a normalized value between 0 and 1.
The displayOrigin is a pixel value, based on the size of the Game Object combined with the origin.
Source: src/gameobjects/components/Origin.js#L88
Since: 3.0.0
originX ​
originX: number ​
Description:
The horizontal origin of this Game Object.
The origin maps the relationship between the size and position of the Game Object.
The default value is 0.5, meaning all Game Objects are positioned based on their center.
Setting the value to 0 means the position now relates to the left of the Game Object.
Set this value with setOrigin() .
Source: src/gameobjects/components/Origin.js#L30
Since: 3.0.0
originY ​
originY: number ​
Description:
The vertical origin of this Game Object.
The origin maps the relationship between the size and position of the Game Object.
The default value is 0.5, meaning all Game Objects are positioned based on their center.
Setting the value to 0 means the position now relates to the top of the Game Object.
Set this value with setOrigin() .
Source: src/gameobjects/components/Origin.js#L45
Since: 3.0.0
Static functions ​
setDisplayOrigin ​
<instance> setDisplayOrigin([x], [y]) ​
Description:
Sets the display origin of this Game Object.
The difference between this and setting the origin is that you can use pixel values for setting the display origin.
Parameters:
name type optional default description
x number Yes 0 The horizontal display origin value.
y number Yes "x" The vertical display origin value. If not defined it will be set to the value of x .
Returns: Phaser.GameObjects.Components.Origin - This Game Object instance.
Source: src/gameobjects/components/Origin.js#L159
Since: 3.0.0
setOrigin ​
<instance> setOrigin([x], [y]) ​
Description:
Sets the origin of this Game Object.
The values are given in the range 0 to 1.
Parameters:
name type optional default description
x number Yes 0.5 The horizontal origin value.
y number Yes "x" The vertical origin value. If not defined it will be set to the value of x .
Returns: Phaser.GameObjects.Components.Origin - This Game Object instance.
Source: src/gameobjects/components/Origin.js#L112
Since: 3.0.0
setOriginFromFrame ​
<instance> setOriginFromFrame() ​
Description:
Sets the origin of this Game Object based on the Pivot values in its Frame.
Returns: Phaser.GameObjects.Components.Origin - This Game Object instance.
Source: src/gameobjects/components/Origin.js#L136
Since: 3.0.0
updateDisplayOrigin ​
<instance> updateDisplayOrigin() ​
Description:
Updates the Display Origin cached values internally stored on this Game Object.
You don't usually call this directly, but it is exposed for edge-cases where you may.
Returns: Phaser.GameObjects.Components.Origin - This Game Object instance.
Source: src/gameobjects/components/Origin.js#L182
Since: 3.0.0
Previous
Phaser.GameObjects.Components.Mask
Next
Phaser.GameObjects.Components.PathFollower
Static functions
displayOriginX
displayOriginY
originX
originY
Static functions
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
