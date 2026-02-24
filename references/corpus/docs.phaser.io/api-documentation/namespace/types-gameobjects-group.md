# Phaser.Types.GameObjects.Group | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/types-gameobjects-group

Phaser API Documentation
Namespaces
Phaser.Types.GameObjects.Group
Version: Phaser v3.90.0
On this page
Phaser.Types.GameObjects.Group
Scope: static
Source: src/gameobjects/group/typedefs/index.js#L7
Static functions ​
GroupCallback ​
GroupCallback ​
Parameters:
name type optional description
item Phaser.GameObjects.GameObject No A group member
Source: src/gameobjects/group/typedefs/GroupCallback.js#L1
Since: 3.0.0
GroupClassTypeConstructor ​
GroupClassTypeConstructor ​
Parameters:
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
texture string | Phaser.Textures.Texture No The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
Source: src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1
Since: 3.0.0
GroupConfig ​
GroupConfig ​
Source: src/gameobjects/group/typedefs/GroupConfig.js#L1
Since: 3.0.0
GroupCreateConfig ​
GroupCreateConfig ​
Description:
The total number of objects created will be
key.length * frame.length * frameQuantity * (yoyo ? 2 : 1) * (1 + repeat)
If max is nonzero, then the total created will not exceed max .
key is required. Phaser.GameObjects.Group#defaultKey is not used.
Source: src/gameobjects/group/typedefs/GroupCreateConfig.js#L1
Since: 3.0.0
GroupMultipleCreateCallback ​
GroupMultipleCreateCallback ​
Parameters:
name type optional description
items Array.< Phaser.GameObjects.GameObject > No The newly created group members
Source: src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1
Since: 3.0.0
Previous
Phaser.Types.GameObjects.Graphics
Next
Phaser.Types.GameObjects.Mesh
Static functions
GroupCallback
GroupClassTypeConstructor
GroupConfig
GroupCreateConfig
GroupMultipleCreateCallback
