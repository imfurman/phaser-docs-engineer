# Types.GameObjects.Plane | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/types-gameobjects-plane

Phaser API Documentation
Typedefs
Types.GameObjects.Plane
Version: Phaser v3.90.0
On this page
Types.GameObjects.Plane
PlaneCheckerboardConfig ​
<static> PlaneCheckerboardConfig ​
name type optional default description
color1 number Yes "0xffffff" The odd cell color, specified as a hex value.
color2 number Yes "0x0000ff" The even cell color, specified as a hex value.
alpha1 number Yes 255 The odd cell alpha value, specified as a number between 0 and 255.
alpha2 number Yes 255 The even cell alpha value, specified as a number between 0 and 255.
height number Yes 128 The view height of the Plane after creation, in pixels.
Type : object
Member of : Phaser.Types.GameObjects.Plane
Source: src/gameobjects/plane/typedefs/PlaneCheckerboardConfig.js#L1
Since: 3.60.0
PlaneConfig ​
<static> PlaneConfig ​
name type optional default description
key string | Phaser.Textures.Texture Yes The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
width number Yes 8 The width of this Plane, in cells, not pixels.
height number Yes 8 The height of this Plane, in cells, not pixels.
tile boolean Yes false Is the texture tiled? I.e. repeated across each cell.
checkerboard Phaser.Types.GameObjects.Plane.PlaneCheckerboardConfig Yes Plane checkerboard configuration object.
Type : object
Member of : Phaser.Types.GameObjects.Plane
Source: src/gameobjects/plane/typedefs/PlaneConfig.js#L1
Since: 3.60.0
Previous
Types.GameObjects.PathFollower
Next
Types.GameObjects.RenderTexture
PlaneCheckerboardConfig
<static> PlaneCheckerboardConfig
PlaneConfig
<static> PlaneConfig
