# Types.GameObjects.NineSlice | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/types-gameobjects-nineslice

Phaser API Documentation
Typedefs
Types.GameObjects.NineSlice
Version: Phaser v3.90.0
On this page
Types.GameObjects.NineSlice
NineSliceConfig ​
<static> NineSliceConfig ​
name type optional default description
key string | Phaser.Textures.Texture Yes The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
width number Yes 256 The width of the Nine Slice Game Object. You can adjust the width post-creation.
height number Yes 256 The height of the Nine Slice Game Object. If this is a 3 slice object the height will be fixed to the height of the texture and cannot be changed.
leftWidth number Yes 10 The size of the left vertical column (A).
rightWidth number Yes 10 The size of the right vertical column (B).
topHeight number Yes 0 The size of the top horiztonal row (C). Set to zero or undefined to create a 3 slice object.
bottomHeight number Yes 0 The size of the bottom horiztonal row (D). Set to zero or undefined to create a 3 slice object.
Type : object
Member of : Phaser.Types.GameObjects.NineSlice
Source: src/gameobjects/nineslice/typedefs/NineSliceConfig.js#L1
Since: 3.60.0
Previous
Types.GameObjects.Mesh
Next
Types.GameObjects.Particles
NineSliceConfig
<static> NineSliceConfig
