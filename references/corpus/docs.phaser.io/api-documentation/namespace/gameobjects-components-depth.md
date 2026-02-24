# Phaser.GameObjects.Components.Depth | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-depth

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Depth
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Depth
Scope: static
Source: src/gameobjects/components/Depth.js#L7
Since: 3.0.0
Static functions ​
depth ​
depth: number ​
Description:
The depth of this Game Object within the Scene. Ensure this value is only ever set to a number data-type.
The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order
of Game Objects, without actually moving their position in the display list.
The default depth is zero. A Game Object with a higher depth
value will always render in front of one with a lower value.
Setting the depth will queue a depth sort event within the Scene.
Source: src/gameobjects/components/Depth.js#L30
Since: 3.0.0
Static functions ​
setAbove ​
<instance> setAbove(gameObject) ​
Description:
Move this Game Object so that it appears above the given Game Object.
This means it will render immediately after the other object in the display list.
Both objects must belong to the same display list, or parent container.
This method does not change this Game Objects depth value, it simply alters its list position.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that this Game Object will be moved to be above.
Returns: Phaser.GameObjects.Components.Depth - This Game Object instance.
Source: src/gameobjects/components/Depth.js#L139
Since: 3.85.0
setBelow ​
<instance> setBelow(gameObject) ​
Description:
Move this Game Object so that it appears below the given Game Object.
This means it will render immediately under the other object in the display list.
Both objects must belong to the same display list, or parent container.
This method does not change this Game Objects depth value, it simply alters its list position.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that this Game Object will be moved to be below.
Returns: Phaser.GameObjects.Components.Depth - This Game Object instance.
Source: src/gameobjects/components/Depth.js#L167
Since: 3.85.0
setDepth ​
<instance> setDepth(value) ​
Description:
The depth of this Game Object within the Scene.
The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order
of Game Objects, without actually moving their position in the display list.
The default depth is zero. A Game Object with a higher depth
value will always render in front of one with a lower value.
Setting the depth will queue a depth sort event within the Scene.
Parameters:
name type optional description
value number No The depth of this Game Object. Ensure this value is only ever a number data-type.
Returns: Phaser.GameObjects.Components.Depth - This Game Object instance.
Source: src/gameobjects/components/Depth.js#L64
Since: 3.0.0
setToBack ​
<instance> setToBack() ​
Description:
Sets this Game Object to the back of the display list, or the back of its parent container.
Being at the back means it will render below everything else.
This method does not change this Game Objects depth value, it simply alters its list position.
Returns: Phaser.GameObjects.Components.Depth - This Game Object instance.
Source: src/gameobjects/components/Depth.js#L115
Since: 3.85.0
setToTop ​
<instance> setToTop() ​
Description:
Sets this Game Object to be at the top of the display list, or the top of its parent container.
Being at the top means it will render on-top of everything else.
This method does not change this Game Objects depth value, it simply alters its list position.
Returns: Phaser.GameObjects.Components.Depth - This Game Object instance.
Source: src/gameobjects/components/Depth.js#L91
Since: 3.85.0
Previous
Phaser.GameObjects.Components.Crop
Next
Phaser.GameObjects.Components.Flip
Static functions
depth
Static functions
setAbove
setBelow
setDepth
setToBack
setToTop
