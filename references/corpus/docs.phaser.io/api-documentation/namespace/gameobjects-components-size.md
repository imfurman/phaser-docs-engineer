# Phaser.GameObjects.Components.Size | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-size

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Size
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Size
Scope: static
Source: src/gameobjects/components/Size.js#L7
Since: 3.0.0
Static functions ​
displayHeight ​
displayHeight: number ​
Description:
The displayed height of this Game Object.
This value takes into account the scale factor.
Setting this value will adjust the Game Object's scale property.
Source: src/gameobjects/components/Size.js#L78
Since: 3.0.0
displayWidth ​
displayWidth: number ​
Description:
The displayed width of this Game Object.
This value takes into account the scale factor.
Setting this value will adjust the Game Object's scale property.
Source: src/gameobjects/components/Size.js#L53
Since: 3.0.0
height ​
height: number ​
Description:
The native (un-scaled) height of this Game Object.
Changing this value will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or use
the displayHeight property.
Source: src/gameobjects/components/Size.js#L40
Since: 3.0.0
width ​
width: number ​
Description:
The native (un-scaled) width of this Game Object.
Changing this value will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or use
the displayWidth property.
Source: src/gameobjects/components/Size.js#L27
Since: 3.0.0
Static functions ​
setDisplaySize ​
<instance> setDisplaySize(width, height) ​
Description:
Sets the display size of this Game Object.
Calling this will adjust the scale.
Parameters:
name type optional description
width number No The width of this Game Object.
height number No The height of this Game Object.
Returns: Phaser.GameObjects.Components.Size - This Game Object instance.
Source: src/gameobjects/components/Size.js#L166
Since: 3.0.0
setSize ​
<instance> setSize(width, height) ​
Description:
Sets the internal size of this Game Object, as used for frame or physics body creation.
This will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or call the
setDisplaySize method, which is the same thing as changing the scale but allows you
to do so by giving pixel values.
If you have enabled this Game Object for input, changing the size will not change the
size of the hit area. To do this you should adjust the input.hitArea object directly.
Parameters:
name type optional description
width number No The width of this Game Object.
height number No The height of this Game Object.
Returns: Phaser.GameObjects.Components.Size - This Game Object instance.
Source: src/gameobjects/components/Size.js#L139
Since: 3.0.0
setSizeToFrame ​
<instance> setSizeToFrame([frame]) ​
Description:
Sets the size of this Game Object to be that of the given Frame.
This will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or call the
setDisplaySize method, which is the same thing as changing the scale but allows you
to do so by giving pixel values.
If you have enabled this Game Object for input, changing the size will not change the
size of the hit area. To do this you should adjust the input.hitArea object directly.
Parameters:
name type optional description
frame Phaser.Textures.Frame | boolean Yes The frame to base the size of this Game Object on.
Returns: Phaser.GameObjects.Components.Size - This Game Object instance.
Source: src/gameobjects/components/Size.js#L103
Since: 3.0.0
Previous
Phaser.GameObjects.Components.ScrollFactor
Next
Phaser.GameObjects.Components.Texture
Static functions
displayHeight
displayWidth
height
width
Static functions
setDisplaySize
setSize
setSizeToFrame
