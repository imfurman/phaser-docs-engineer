# Phaser.GameObjects.Components.ScrollFactor | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-scrollfactor

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.ScrollFactor
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.ScrollFactor
Scope: static
Source: src/gameobjects/components/ScrollFactor.js#L7
Since: 3.0.0
Static functions ​
scrollFactorX ​
scrollFactorX: number ​
Description:
The horizontal scroll factor of this Game Object.
The scroll factor controls the influence of the movement of a Camera upon this Game Object.
When a camera scrolls it will change the location at which this Game Object is rendered on-screen.
It does not change the Game Objects actual position values.
A value of 1 means it will move exactly in sync with a camera.
A value of 0 means it will not move at all, even if the camera moves.
Other values control the degree to which the camera movement is mapped to this Game Object.
Please be aware that scroll factor values other than 1 are not taken in to consideration when
calculating physics collisions. Bodies always collide based on their world position, but changing
the scroll factor is a visual adjustment to where the textures are rendered, which can offset
them from physics bodies if not accounted for in your code.
Source: src/gameobjects/components/ScrollFactor.js#L16
Since: 3.0.0
scrollFactorY ​
scrollFactorY: number ​
Description:
The vertical scroll factor of this Game Object.
The scroll factor controls the influence of the movement of a Camera upon this Game Object.
When a camera scrolls it will change the location at which this Game Object is rendered on-screen.
It does not change the Game Objects actual position values.
A value of 1 means it will move exactly in sync with a camera.
A value of 0 means it will not move at all, even if the camera moves.
Other values control the degree to which the camera movement is mapped to this Game Object.
Please be aware that scroll factor values other than 1 are not taken in to consideration when
calculating physics collisions. Bodies always collide based on their world position, but changing
the scroll factor is a visual adjustment to where the textures are rendered, which can offset
them from physics bodies if not accounted for in your code.
Source: src/gameobjects/components/ScrollFactor.js#L40
Since: 3.0.0
Static functions ​
setScrollFactor ​
<instance> setScrollFactor(x, [y]) ​
Description:
Sets the scroll factor of this Game Object.
The scroll factor controls the influence of the movement of a Camera upon this Game Object.
When a camera scrolls it will change the location at which this Game Object is rendered on-screen.
It does not change the Game Objects actual position values.
A value of 1 means it will move exactly in sync with a camera.
A value of 0 means it will not move at all, even if the camera moves.
Other values control the degree to which the camera movement is mapped to this Game Object.
Please be aware that scroll factor values other than 1 are not taken in to consideration when
calculating physics collisions. Bodies always collide based on their world position, but changing
the scroll factor is a visual adjustment to where the textures are rendered, which can offset
them from physics bodies if not accounted for in your code.
Parameters:
name type optional default description
x number No The horizontal scroll factor of this Game Object.
y number Yes "x" The vertical scroll factor of this Game Object. If not set it will use the x value.
Returns: Phaser.GameObjects.Components.ScrollFactor - This Game Object instance.
Source: src/gameobjects/components/ScrollFactor.js#L64
Since: 3.0.0
Previous
Phaser.GameObjects.Components.PostPipeline
Next
Phaser.GameObjects.Components.Size
Static functions
scrollFactorX
scrollFactorY
Static functions
setScrollFactor
