# Frame | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/textures-frame

Phaser API Documentation
Class
Frame
Version: Phaser v3.90.0
On this page
Frame
A Frame is a section of a Texture.
Constructor
new Frame(texture, name, sourceIndex, x, y, width, height)
Parameters
name type optional description
texture Phaser.Textures.Texture No The Texture this Frame is a part of.
name number | string No The name of this Frame. The name is unique within the Texture.
sourceIndex number No The index of the TextureSource that this Frame is a part of.
x number No The x coordinate of the top-left of this Frame.
y number No The y coordinate of the top-left of this Frame.
width number No The width of this Frame.
height number No The height of this Frame.
Scope : static
Source: src/textures/Frame.js#L11
Since: 3.0.0
Public Members ​
autoRound ​
autoRound: number ​
Description:
Over-rides the Renderer setting.
-1 = use Renderer Setting
0 = No rounding
1 = Round
Source: src/textures/Frame.js#L227
Since: 3.0.0
canvasData ​
canvasData: object ​
Description:
The Canvas drawImage data object.
Source: src/textures/Frame.js#L952
Since: 3.0.0
centerX ​
centerX: number ​
Description:
The x center of this frame, floored.
Source: src/textures/Frame.js#L165
Since: 3.0.0
centerY ​
centerY: number ​
Description:
The y center of this frame, floored.
Source: src/textures/Frame.js#L174
Since: 3.0.0
customData ​
customData: object ​
Description:
Any Frame specific custom data can be stored here.
Source: src/textures/Frame.js#L240
Since: 3.0.0
customPivot ​
customPivot: boolean ​
Description:
Does this Frame have a custom pivot point?
Source: src/textures/Frame.js#L203
Since: 3.0.0
cutHeight ​
cutHeight: number ​
Description:
The height of the area in the source image to cut.
Source: src/textures/Frame.js#L98
Since: 3.0.0
cutWidth ​
cutWidth: number ​
Description:
The width of the area in the source image to cut.
Source: src/textures/Frame.js#L89
Since: 3.0.0
cutX ​
cutX: number ​
Description:
X position within the source image to cut from.
Source: src/textures/Frame.js#L71
Since: 3.0.0
cutY ​
cutY: number ​
Description:
Y position within the source image to cut from.
Source: src/textures/Frame.js#L80
Since: 3.0.0
glTexture ​
glTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper ​
Description:
A reference to the Texture Source WebGL Texture that this Frame is using.
Source: src/textures/Frame.js#L832
Since: 3.11.0
halfHeight ​
halfHeight: number ​
Description:
Half the height, floored.
Precalculated for the renderer.
Source: src/textures/Frame.js#L155
Since: 3.0.0
halfWidth ​
halfWidth: number ​
Description:
Half the width, floored.
Precalculated for the renderer.
Source: src/textures/Frame.js#L145
Since: 3.0.0
height ​
height: number ​
Description:
The rendering height of this Frame, taking trim into account.
Source: src/textures/Frame.js#L136
Since: 3.0.0
is3Slice ​
is3Slice: boolean ​
Description:
If the Frame has scale9 border data, is it 3-slice or 9-slice data?
Source: src/textures/Frame.js#L935
Since: 3.70.0
name ​
name: string ​
Description:
The name of this Frame.
The name is unique within the Texture.
Source: src/textures/Frame.js#L43
Since: 3.0.0
pivotX ​
pivotX: number ​
Description:
The horizontal pivot point of this Frame.
Source: src/textures/Frame.js#L183
Since: 3.0.0
pivotY ​
pivotY: number ​
Description:
The vertical pivot point of this Frame.
Source: src/textures/Frame.js#L193
Since: 3.0.0
radius ​
radius: number ​
Description:
The radius of the Frame (derived from sqrt(w * w + h * h) / 2)
Source: src/textures/Frame.js#L884
Since: 3.0.0
realHeight ​
realHeight: number ​
Description:
The height of the Frame in its un-trimmed, un-padded state, as prepared in the art package,
before being packed.
Source: src/textures/Frame.js#L866
Since: 3.0.0
realWidth ​
realWidth: number ​
Description:
The width of the Frame in its un-trimmed, un-padded state, as prepared in the art package,
before being packed.
Source: src/textures/Frame.js#L848
Since: 3.0.0
rotated ​
rotated: boolean ​
Description:
CURRENTLY UNSUPPORTED
Is this frame is rotated or not in the Texture?
Rotation allows you to use rotated frames in texture atlas packing.
It has nothing to do with Sprite rotation.
Source: src/textures/Frame.js#L213
Since: 3.0.0
scale9 ​
scale9: boolean ​
Description:
Does the Frame have scale9 border data?
Source: src/textures/Frame.js#L918
Since: 3.70.0
source ​
source: Phaser.Textures.TextureSource ​
Description:
The TextureSource this Frame is part of.
Source: src/textures/Frame.js#L53
Since: 3.0.0
sourceIndex ​
sourceIndex: number ​
Description:
The index of the TextureSource in the Texture sources array.
Source: src/textures/Frame.js#L62
Since: 3.0.0
texture ​
texture: Phaser.Textures.Texture ​
Description:
The Texture this Frame is a part of.
Source: src/textures/Frame.js#L34
Since: 3.0.0
trimmed ​
trimmed: boolean ​
Description:
Is the Frame trimmed or not?
Source: src/textures/Frame.js#L901
Since: 3.0.0
u0 ​
u0: number ​
Description:
WebGL UV u0 value.
Source: src/textures/Frame.js#L249
Since: 3.11.0
u1 ​
u1: number ​
Description:
WebGL UV u1 value.
Source: src/textures/Frame.js#L269
Since: 3.11.0
v0 ​
v0: number ​
Description:
WebGL UV v0 value.
Source: src/textures/Frame.js#L259
Since: 3.11.0
v1 ​
v1: number ​
Description:
WebGL UV v1 value.
Source: src/textures/Frame.js#L279
Since: 3.11.0
width ​
width: number ​
Description:
The rendering width of this Frame, taking trim into account.
Source: src/textures/Frame.js#L127
Since: 3.0.0
x ​
x: number ​
Description:
The X rendering offset of this Frame, taking trim into account.
Source: src/textures/Frame.js#L107
Since: 3.0.0
y ​
y: number ​
Description:
The Y rendering offset of this Frame, taking trim into account.
Source: src/textures/Frame.js#L117
Since: 3.0.0
Public Methods ​
clone ​
<instance> clone() ​
Description:
Clones this Frame into a new Frame object.
Returns: Phaser.Textures.Frame - A clone of this Frame.
Source: src/textures/Frame.js#L780
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Frame by nulling its reference to the parent Texture and and data objects.
Source: src/textures/Frame.js#L818
Since: 3.0.0
setCropUVs ​
<instance> setCropUVs(crop, x, y, width, height, flipX, flipY) ​
Description:
Takes a crop data object and, based on the rectangular region given, calculates the
required UV coordinates in order to crop this Frame for WebGL and Canvas rendering.
The crop size as well as coordinates can not exceed the the size of the frame.
This is called directly by the Game Object Texture Components setCrop method.
Please use that method to crop a Game Object.
Parameters:
name type optional description
crop object No The crop data object. This is the GameObject._crop property.
x number No The x coordinate to start the crop from. Cannot be negative or exceed the Frame width.
y number No The y coordinate to start the crop from. Cannot be negative or exceed the Frame height.
width number No The width of the crop rectangle. Cannot exceed the Frame width.
height number No The height of the crop rectangle. Cannot exceed the Frame height.
flipX boolean No Does the parent Game Object have flipX set?
flipY boolean No Does the parent Game Object have flipY set?
Returns: object - The updated crop data object.
Source: src/textures/Frame.js#L523
Since: 3.11.0
setCutPosition ​
<instance> setCutPosition([x], [y]) ​
Description:
Sets the x and y position within the source image to cut from.
Parameters:
name type optional default description
x number Yes 0 X position within the source image to cut from.
y number Yes 0 Y position within the source image to cut from.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L339
Since: 3.85.0
setCutSize ​
<instance> setCutSize(width, height) ​
Description:
Sets the width, and height of the area in the source image to cut.
Parameters:
name type optional description
width number No The width of the area in the source image to cut.
height number No The height of the area in the source image to cut.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L361
Since: 3.85.0
setScale9 ​
<instance> setScale9(x, y, width, height) ​
Description:
Sets the scale9 center rectangle values.
Scale9 is a feature of Texture Packer, allowing you to define a nine-slice scaling grid.
This is set automatically by the JSONArray and JSONHash parsers.
Parameters:
name type optional description
x number No The left coordinate of the center scale9 rectangle.
y number No The top coordinate of the center scale9 rectangle.
width number No The width of the center scale9 rectangle.
height number No The height coordinate of the center scale9 rectangle.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L491
Since: 3.70.0
setSize ​
<instance> setSize(width, height, [x], [y]) ​
Description:
Sets the width, height, x and y of this Frame.
This is called automatically by the constructor
and should rarely be changed on-the-fly.
Parameters:
name type optional default description
width number No The width of the frame before being trimmed.
height number No The height of the frame before being trimmed.
x number Yes 0 The x coordinate of the top-left of this Frame.
y number Yes 0 The y coordinate of the top-left of this Frame.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L380
Since: 3.7.0
setTrim ​
<instance> setTrim(actualWidth, actualHeight, destX, destY, destWidth, destHeight) ​
Description:
If the frame was trimmed when added to the Texture Atlas, this records the trim and source data.
Parameters:
name type optional description
actualWidth number No The width of the frame before being trimmed.
actualHeight number No The height of the frame before being trimmed.
destX number No The destination X position of the trimmed frame for display.
destY number No The destination Y position of the trimmed frame for display.
destWidth number No The destination width of the trimmed frame for display.
destHeight number No The destination height of the trimmed frame for display.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L441
Since: 3.0.0
setUVs ​
<instance> setUVs(width, height, u0, v0, u1, v1) ​
Description:
Directly sets the canvas and WebGL UV data for this frame.
Use this if you need to override the values that are generated automatically
when the Frame is created.
Parameters:
name type optional description
width number No Width of this frame for the Canvas data.
height number No Height of this frame for the Canvas data.
u0 number No UV u0 value.
v0 number No UV v0 value.
u1 number No UV u1 value.
v1 number No UV v1 value.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L684
Since: 3.50.0
updateCropUVs ​
<instance> updateCropUVs(crop, flipX, flipY) ​
Description:
Takes a crop data object and recalculates the UVs based on the dimensions inside the crop object.
Called automatically by setFrame .
Parameters:
name type optional description
crop object No The crop data object. This is the GameObject._crop property.
flipX boolean No Does the parent Game Object have flipX set?
flipY boolean No Does the parent Game Object have flipY set?
Returns: object - The updated crop data object.
Source: src/textures/Frame.js#L666
Since: 3.11.0
updateUVs ​
<instance> updateUVs() ​
Description:
Updates the internal WebGL UV cache and the drawImage cache.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L722
Since: 3.0.0
updateUVsInverted ​
<instance> updateUVsInverted() ​
Description:
Updates the internal WebGL UV cache.
Returns: Phaser.Textures.Frame - This Frame object.
Source: src/textures/Frame.js#L758
Since: 3.0.0
Previous
DynamicTexture
Next
Texture
Public Members
autoRound
canvasData
centerX
centerY
customData
customPivot
cutHeight
cutWidth
cutX
cutY
glTexture
halfHeight
halfWidth
height
is3Slice
name
pivotX
pivotY
radius
realHeight
realWidth
rotated
scale9
source
sourceIndex
texture
trimmed
u0
u1
v0
v1
width
x
y
Public Methods
clone
destroy
setCropUVs
setCutPosition
setCutSize
setScale9
setSize
setTrim
setUVs
updateCropUVs
updateUVs
updateUVsInverted
