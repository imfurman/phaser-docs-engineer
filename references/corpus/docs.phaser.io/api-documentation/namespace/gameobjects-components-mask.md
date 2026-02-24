# Phaser.GameObjects.Components.Mask | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-mask

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Mask
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Mask
Scope: static
Source: src/gameobjects/components/Mask.js#L10
Since: 3.0.0
Static functions ​
mask ​
mask: Phaser.Display.Masks.BitmapMask , Phaser.Display.Masks.GeometryMask ​
Description:
The Mask this Game Object is using during render.
Source: src/gameobjects/components/Mask.js#L19
Since: 3.0.0
Static functions ​
clearMask ​
<instance> clearMask([destroyMask]) ​
Description:
Clears the mask that this Game Object was using.
Parameters:
name type optional default description
destroyMask boolean Yes false Destroy the mask before clearing it?
Returns: Phaser.GameObjects.Components.Mask - This Game Object instance.
Source: src/gameobjects/components/Mask.js#L56
Since: 3.6.2
createBitmapMask ​
<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame]) ​
Description:
Creates and returns a Bitmap Mask. This mask can be used by any Game Object,
including this one, or a Dynamic Texture.
Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.
To create the mask you need to pass in a reference to a renderable Game Object.
A renderable Game Object is one that uses a texture to render with, such as an
Image, Sprite, Render Texture or BitmapText.
If you do not provide a renderable object, and this Game Object has a texture,
it will use itself as the object. This means you can call this method to create
a Bitmap Mask from any renderable texture-based Game Object.
Tags:
generic
generic
genericUse
Parameters:
name type optional description
maskObject Phaser.GameObjects.GameObject | Phaser.Textures.DynamicTexture Yes The Game Object or Dynamic Texture that will be used as the mask. If null it will generate an Image Game Object using the rest of the arguments.
x number Yes If creating a Game Object, the horizontal position in the world.
y number Yes If creating a Game Object, the vertical position in the world.
texture string | Phaser.Textures.Texture Yes If creating a Game Object, the key, or instance of the Texture it will use to render with, as stored in the Texture Manager.
frame string | number Phaser.Textures.Frame Yes
Returns: Phaser.Display.Masks.BitmapMask - This Bitmap Mask that was created.
Source: src/gameobjects/components/Mask.js#L80
Since: 3.6.2
createGeometryMask ​
<instance> createGeometryMask([graphics]) ​
Description:
Creates and returns a Geometry Mask. This mask can be used by any Game Object,
including this one.
To create the mask you need to pass in a reference to a Graphics Game Object.
If you do not provide a graphics object, and this Game Object is an instance
of a Graphics object, then it will use itself to create the mask.
This means you can call this method to create a Geometry Mask from any Graphics Game Object.
Tags:
generic
generic
genericUse
Parameters:
name type optional description
graphics Phaser.GameObjects.Graphics | Phaser.GameObjects.Shape Yes A Graphics Game Object, or any kind of Shape Game Object. The geometry within it will be used as the mask.
Returns: Phaser.Display.Masks.GeometryMask - This Geometry Mask that was created.
Source: src/gameobjects/components/Mask.js#L120
Since: 3.6.2
setMask ​
<instance> setMask(mask) ​
Description:
Sets the mask that this Game Object will use to render with.
The mask must have been previously created and can be either a GeometryMask or a BitmapMask.
Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.
If a mask is already set on this Game Object it will be immediately replaced.
Masks are positioned in global space and are not relative to the Game Object to which they
are applied. The reason for this is that multiple Game Objects can all share the same mask.
Masks have no impact on physics or input detection. They are purely a rendering component
that allows you to limit what is visible during the render pass.
Parameters:
name type optional description
mask Phaser.Display.Masks.BitmapMask | Phaser.Display.Masks.GeometryMask No The mask this Game Object will use when rendering.
Returns: Phaser.GameObjects.Components.Mask - This Game Object instance.
Source: src/gameobjects/components/Mask.js#L28
Since: 3.6.2
Previous
Phaser.GameObjects.Components.GetBounds
Next
Phaser.GameObjects.Components.Origin
Static functions
mask
Static functions
clearMask
createBitmapMask
createGeometryMask
setMask
