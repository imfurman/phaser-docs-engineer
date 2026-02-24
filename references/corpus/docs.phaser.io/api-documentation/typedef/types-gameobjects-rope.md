# Types.GameObjects.Rope | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/types-gameobjects-rope

Phaser API Documentation
Typedefs
Types.GameObjects.Rope
Version: Phaser v3.90.0
On this page
Types.GameObjects.Rope
RopeConfig ​
<static> RopeConfig ​
name type optional default description
key string Yes The key of the Texture this Game Object will use to render with, as stored in the Texture Manager. If not given, __DEFAULT is used.
frame string | integer null Yes
points integer | Array.< Phaser.Types.Math.Vector2Like > Yes 2 An array containing the vertices data for this Rope, or a number that indicates how many segments to split the texture frame into. If none is provided a simple quad is created. See setPoints to set this post-creation.
horizontal boolean Yes true Should the vertices of this Rope be aligned horizontally ( true ), or vertically ( false )?
colors Array.<number> Yes An optional array containing the color data for this Rope. You should provide one color value per pair of vertices.
alphas Array.<number> Yes An optional array containing the alpha data for this Rope. You should provide one alpha value per pair of vertices.
Type : object
Member of : Phaser.Types.GameObjects.Rope
Source: src/gameobjects/rope/typedefs/RopeConfig.js#L1
Since: 3.50.0
Previous
Types.GameObjects.RenderTexture
Next
Types.GameObjects.Shader
RopeConfig
<static> RopeConfig
