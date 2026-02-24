# RenderTexture | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-rendertexture

Phaser API Documentation
Class
RenderTexture
Version: Phaser v3.90.0
On this page
RenderTexture
A Render Texture is a combination of Dynamic Texture and an Image Game Object, that uses the
Dynamic Texture to display itself with.
A Dynamic Texture is a special texture that allows you to draw textures, frames and most kind of
Game Objects directly to it.
You can take many complex objects and draw them to this one texture, which can then be used as the
base texture for other Game Objects, such as Sprites. Should you then update this texture, all
Game Objects using it will instantly be updated as well, reflecting the changes immediately.
It's a powerful way to generate dynamic textures at run-time that are WebGL friendly and don't invoke
expensive GPU uploads on each change.
In versions of Phaser before 3.60 a Render Texture was the only way you could create a texture
like this, that had the ability to be drawn on. But in 3.60 we split the core functions out to
the Dynamic Texture class as it made a lot more sense for them to reside in there. As a result,
the Render Texture is now a light-weight shim that sits on-top of an Image Game Object and offers
proxy methods to the features available from a Dynamic Texture.
When should you use a Render Texture vs. a Dynamic Texture?
You should use a Dynamic Texture if the texture is going to be used by multiple Game Objects,
or you want to use it across multiple Scenes, because textures are globally stored.
You should use a Dynamic Texture if the texture isn't going to be displayed in-game, but is
instead going to be used for something like a mask or shader.
You should use a Render Texture if you need to display the texture in-game on a single Game Object,
as it provides the convenience of wrapping an Image and Dynamic Texture together for you.
Under WebGL1, a FrameBuffer, which is what this Dynamic Texture uses internally, cannot be anti-aliased.
This means that when drawing objects such as Shapes or Graphics instances to this texture, they may appear
to be drawn with no aliasing around the edges. This is a technical limitation of WebGL1. To get around it,
create your shape as a texture in an art package, then draw that to this texture.
Constructor
new RenderTexture(scene, [x], [y], [width], [height], [forceEven])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
width number Yes 32 The width of the Render Texture.
height number Yes 32 The height of the Render Texture.
forceEven boolean Yes true Force the given width and height to be rounded to even values. This significantly improves the rendering quality. Set to false if you know you need an odd sized texture.
Scope : static
Extends
Phaser.GameObjects.Image
Source: src/gameobjects/rendertexture/RenderTexture.js#L11
Since: 3.2.0
Inherited Members ​
From Phaser.GameObjects.Components.Alpha :
alpha
alphaBottomLeft
alphaBottomRight
alphaTopLeft
alphaTopRight
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Flip :
flipX
flipY
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
From Phaser.GameObjects.Components.Pipeline :
defaultPipeline
pipeline
pipelineData
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
From Phaser.GameObjects.Components.Size :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.TextureCrop :
frame
isCropped
texture
From Phaser.GameObjects.Components.Tint :
isTinted
tint
tintBottomLeft
tintBottomRight
tintFill
tintTopLeft
tintTopRight
From Phaser.GameObjects.Components.Transform :
angle
hasTransformComponent
rotation
scale
scaleX
scaleY
w
x
y
z
From Phaser.GameObjects.Components.Visible :
visible
From Phaser.GameObjects.GameObject :
active
body
cameraFilter
data
displayList
ignoreDestroy
input
name
parentContainer
renderFlags
scene
state
tabIndex
type
Public Members ​
camera ​
camera: Phaser.Cameras.Scene2D.BaseCamera ​
Description:
An internal Camera that can be used to move around this Render Texture.
Control it just like you would any Scene Camera. The difference is that it only impacts
the placement of Game Objects that you then draw to this texture.
You can scroll, zoom and rotate this Camera.
This property is a reference to RenderTexture.texture.camera .
Source: src/gameobjects/rendertexture/RenderTexture.js#L81
Since: 3.12.0
Inherited Methods ​
From Phaser.Events.EventEmitter :
addListener
emit
eventNames
listenerCount
listeners
off
on
once
removeAllListeners
removeListener
shutdown
From Phaser.GameObjects.Components.Alpha :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Flip :
resetFlip
setFlip
setFlipX
setFlipY
toggleFlipX
toggleFlipY
From Phaser.GameObjects.Components.GetBounds :
getBottomCenter
getBottomLeft
getBottomRight
getBounds
getCenter
getLeftCenter
getRightCenter
getTopCenter
getTopLeft
getTopRight
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
From Phaser.GameObjects.Components.Pipeline :
getPipelineName
initPipeline
resetPipeline
setPipeline
setPipelineData
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
From Phaser.GameObjects.Components.Size :
setDisplaySize
setSizeToFrame
From Phaser.GameObjects.Components.TextureCrop :
setCrop
setFrame
setTexture
From Phaser.GameObjects.Components.Tint :
clearTint
setTint
setTintFill
From Phaser.GameObjects.Components.Transform :
copyPosition
getLocalPoint
getLocalTransformMatrix
getParentRotation
getWorldPoint
getWorldTransformMatrix
setAngle
setPosition
setRandomPosition
setRotation
setScale
setW
setX
setY
setZ
From Phaser.GameObjects.Components.Visible :
setVisible
From Phaser.GameObjects.GameObject :
addedToScene
addToDisplayList
addToUpdateList
destroy
disableInteractive
getData
getDisplayList
getIndexList
incData
removedFromScene
removeFromDisplayList
removeFromUpdateList
removeInteractive
setActive
setData
setDataEnabled
setInteractive
setName
setState
toggleData
toJSON
update
willRender
Public Methods ​
batchDraw ​
<instance> batchDraw(entries, [x], [y], [alpha], [tint]) ​
Description:
Use this method if you have already called beginDraw and need to batch
draw a large number of objects to this Render Texture.
This method batches the drawing of the given objects to this texture,
without causing a WebGL bind or batch flush for each one.
It is faster than calling draw , but you must be careful to manage the
flow of code and remember to call endDraw() . If you don't need to draw large
numbers of objects it's much safer and easier to use the draw method instead.
The flow should be:
// Call once:
RenderTexture . beginDraw ( ) ;
// repeat n times:
RenderTexture . batchDraw ( ) ;
// or
RenderTexture . batchDrawFrame ( ) ;
// Call once:
RenderTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Render Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the RenderTexture.texture.isDrawing boolean property to tell if a batch is
currently open, or not.
This method can accept any of the following:
Any renderable Game Object, such as a Sprite, Text, Graphics or TileSprite.
Tilemap Layers.
A Group. The contents of which will be iterated and drawn in turn.
A Container. The contents of which will be iterated fully, and drawn in turn.
A Scene's Display List. Pass in Scene.children to draw the whole list.
Another Dynamic Texture or Render Texture.
A Texture Frame instance.
A string. This is used to look-up a texture from the Texture Manager.
Note: You cannot draw a Render Texture to itself.
If passing in a Group or Container it will only draw children that return true
when their willRender() method is called. I.e. a Container with 10 children,
5 of which have visible=false will only draw the 5 visible ones.
If passing in an array of Game Objects it will draw them all, regardless if
they pass a willRender check or not.
You can pass in a string in which case it will look for a texture in the Texture
Manager matching that string, and draw the base frame. If you need to specify
exactly which frame to draw then use the method drawFrame instead.
You can pass in the x and y coordinates to draw the objects at. The use of
the coordinates differ based on what objects are being drawn. If the object is
a Group, Container or Display List, the coordinates are added to the positions
of the children. For all other types of object, the coordinates are exact.
The alpha and tint values are only used by Texture Frames.
Game Objects use their own alpha and tint values when being drawn.
Parameters:
name type optional default description
entries any No Any renderable Game Object, or Group, Container, Display List, other Dynamic or Texture, Texture Frame or an array of any of these.
x number Yes 0 The x position to draw the Frame at, or the offset applied to the object.
y number Yes 0 The y position to draw the Frame at, or the offset applied to the object.
alpha number Yes 1 The alpha value. Only used when drawing Texture Frames to this texture. Game Objects use their own alpha.
tint number Yes "0xffffff" The tint color value. Only used when drawing Texture Frames to this texture. Game Objects use their own tint. WebGL only.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L536
Since: 3.50.0
batchDrawFrame ​
<instance> batchDrawFrame(key, [frame], [x], [y], [alpha], [tint]) ​
Description:
Use this method if you have already called beginDraw and need to batch
draw a large number of texture frames to this Render Texture.
This method batches the drawing of the given frames to this Render Texture,
without causing a WebGL bind or batch flush for each one.
It is faster than calling drawFrame , but you must be careful to manage the
flow of code and remember to call endDraw() . If you don't need to draw large
numbers of frames it's much safer and easier to use the drawFrame method instead.
The flow should be:
// Call once:
RenderTexture . beginDraw ( ) ;
// repeat n times:
RenderTexture . batchDraw ( ) ;
// or
RenderTexture . batchDrawFrame ( ) ;
// Call once:
RenderTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Render Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the RenderTexture.texture.isDrawing boolean property to tell if a batch is
currently open, or not.
Textures are referenced by their string-based keys, as stored in the Texture Manager.
You can optionally provide a position, alpha and tint value to apply to the frame
before it is drawn.
Parameters:
name type optional default description
key string No The key of the texture to be used, as stored in the Texture Manager.
frame string | number Yes The name or index of the frame within the Texture.
x number Yes 0 The x position to draw the frame at.
y number Yes 0 The y position to draw the frame at.
alpha number Yes 1 The alpha value. Only used when drawing Texture Frames to this texture. Game Objects use their own alpha.
tint number Yes "0xffffff" The tint color value. Only used when drawing Texture Frames to this texture. Game Objects use their own tint. WebGL only.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L619
Since: 3.50.0
beginDraw ​
<instance> beginDraw() ​
Description:
Use this method if you need to batch draw a large number of Game Objects to
this Render Texture in a single pass, or on a frequent basis. This is especially
useful under WebGL, however, if your game is using Canvas only, it will not make
any speed difference in that situation.
This method starts the beginning of a batched draw, unless one is already open.
Batched drawing is faster than calling draw in loop, but you must be careful
to manage the flow of code and remember to call endDraw() when you're finished.
If you don't need to draw large numbers of objects it's much safer and easier
to use the draw method instead.
The flow should be:
// Call once:
RenderTexture . beginDraw ( ) ;
// repeat n times:
RenderTexture . batchDraw ( ) ;
// or
RenderTexture . batchDrawFrame ( ) ;
// Call once:
RenderTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Render Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the RenderTexture.texture.isDrawing boolean property to tell if a batch is
currently open, or not.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L488
Since: 3.50.0
clear ​
<instance> clear() ​
Description:
Fully clears this Render Texture, erasing everything from it and resetting it back to
a blank, transparent, texture.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L253
Since: 3.2.0
draw ​
<instance> draw(entries, [x], [y], [alpha], [tint]) ​
Description:
Draws the given object, or an array of objects, to this Render Texture.
It can accept any of the following:
Any renderable Game Object, such as a Sprite, Text, Graphics or TileSprite.
Tilemap Layers.
A Group. The contents of which will be iterated and drawn in turn.
A Container. The contents of which will be iterated fully, and drawn in turn.
A Scene Display List. Pass in Scene.children to draw the whole list.
Another Dynamic Texture, or a Render Texture.
A Texture Frame instance.
A string. This is used to look-up the texture from the Texture Manager.
Note 1: You cannot draw a Render Texture to itself.
Note 2: For Game Objects that have Post FX Pipelines, the pipeline cannot be
used when drawn to this texture.
If passing in a Group or Container it will only draw children that return true
when their willRender() method is called. I.e. a Container with 10 children,
5 of which have visible=false will only draw the 5 visible ones.
If passing in an array of Game Objects it will draw them all, regardless if
they pass a willRender check or not.
You can pass in a string in which case it will look for a texture in the Texture
Manager matching that string, and draw the base frame. If you need to specify
exactly which frame to draw then use the method drawFrame instead.
You can pass in the x and y coordinates to draw the objects at. The use of
the coordinates differ based on what objects are being drawn. If the object is
a Group, Container or Display List, the coordinates are added to the positions
of the children. For all other types of object, the coordinates are exact.
The alpha and tint values are only used by Texture Frames.
Game Objects use their own alpha and tint values when being drawn.
Calling this method causes the WebGL batch to flush, so it can write the texture
data to the framebuffer being used internally. The batch is flushed at the end,
after the entries have been iterated. So if you've a bunch of objects to draw,
try and pass them in an array in one single call, rather than making lots of
separate calls.
Parameters:
name type optional default description
entries any No Any renderable Game Object, or Group, Container, Display List, other Render Texture, Texture Frame or an array of any of these.
x number Yes 0 The x position to draw the Frame at, or the offset applied to the object.
y number Yes 0 The y position to draw the Frame at, or the offset applied to the object.
alpha number Yes 1 The alpha value. Only used when drawing Texture Frames to this texture. Game Objects use their own alpha.
tint number Yes "0xffffff" The tint color value. Only used when drawing Texture Frames to this texture. Game Objects use their own tint. WebGL only.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L352
Since: 3.2.0
drawFrame ​
<instance> drawFrame(key, [frame], [x], [y], [alpha], [tint]) ​
Description:
Draws the Texture Frame to the Render Texture at the given position.
Textures are referenced by their string-based keys, as stored in the Texture Manager.
var rt = this . add . renderTexture ( 0 , 0 , 800 , 600 ) ;
rt . drawFrame ( key , frame ) ;
You can optionally provide a position, alpha and tint value to apply to the frame
before it is drawn.
Calling this method will cause a batch flush, so if you've got a stack of things to draw
in a tight loop, try using the draw method instead.
If you need to draw a Sprite to this Render Texture, use the draw method instead.
Parameters:
name type optional default description
key string No The key of the texture to be used, as stored in the Texture Manager.
frame string | number Yes The name or index of the frame within the Texture. Set to null to skip this argument if not required.
x number Yes 0 The x position to draw the frame at.
y number Yes 0 The y position to draw the frame at.
alpha number Yes 1 The alpha value. Only used when drawing Texture Frames to this texture.
tint number Yes "0xffffff" The tint color value. Only used when drawing Texture Frames to this texture. WebGL only.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L414
Since: 3.12.0
endDraw ​
<instance> endDraw([erase]) ​
Description:
Use this method to finish batch drawing to this Render Texture.
Doing so will stop the WebGL Renderer from capturing draws and then blit the
framebuffer to the Render Target owned by this texture.
Calling this method without first calling beginDraw will have no effect.
Batch drawing is faster than calling draw , but you must be careful to manage the
flow of code and remember to call endDraw() when you're finished.
If you don't need to draw large numbers of objects it's much safer and easier
to use the draw method instead.
The flow should be:
// Call once:
RenderTexture . beginDraw ( ) ;
// repeat n times:
RenderTexture . batchDraw ( ) ;
// or
RenderTexture . batchDrawFrame ( ) ;
// Call once:
RenderTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Render Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the RenderTexture.texture.isDrawing boolean property to tell if a batch is
currently open, or not.
Parameters:
name type optional default description
erase boolean Yes false Draws all objects in this batch using a blend mode of ERASE. This has the effect of erasing any filled pixels in the objects being drawn.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L676
Since: 3.50.0
erase ​
<instance> erase(entries, [x], [y]) ​
Description:
Draws the given object, or an array of objects, to this Render Texture using a blend mode of ERASE.
This has the effect of erasing any filled pixels present in the objects from this texture.
It can accept any of the following:
Any renderable Game Object, such as a Sprite, Text, Graphics or TileSprite.
Tilemap Layers.
A Group. The contents of which will be iterated and drawn in turn.
A Container. The contents of which will be iterated fully, and drawn in turn.
A Scene Display List. Pass in Scene.children to draw the whole list.
Another Dynamic Texture, or a Render Texture.
A Texture Frame instance.
A string. This is used to look-up the texture from the Texture Manager.
Note: You cannot erase a Render Texture from itself.
If passing in a Group or Container it will only draw children that return true
when their willRender() method is called. I.e. a Container with 10 children,
5 of which have visible=false will only draw the 5 visible ones.
If passing in an array of Game Objects it will draw them all, regardless if
they pass a willRender check or not.
You can pass in a string in which case it will look for a texture in the Texture
Manager matching that string, and draw the base frame.
You can pass in the x and y coordinates to draw the objects at. The use of
the coordinates differ based on what objects are being drawn. If the object is
a Group, Container or Display List, the coordinates are added to the positions
of the children. For all other types of object, the coordinates are exact.
Calling this method causes the WebGL batch to flush, so it can write the texture
data to the framebuffer being used internally. The batch is flushed at the end,
after the entries have been iterated. So if you've a bunch of objects to draw,
try and pass them in an array in one single call, rather than making lots of
separate calls.
Parameters:
name type optional default description
entries any No Any renderable Game Object, or Group, Container, Display List, Render Texture, Texture Frame, or an array of any of these.
x number Yes 0 The x position to draw the Frame at, or the offset applied to the object.
y number Yes 0 The y position to draw the Frame at, or the offset applied to the object.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L298
Since: 3.16.0
fill ​
<instance> fill(rgb, [alpha], [x], [y], [width], [height]) ​
Description:
Fills this Render Texture with the given color.
By default it will fill the entire texture, however you can set it to fill a specific
rectangular area by using the x, y, width and height arguments.
The color should be given in hex format, i.e. 0xff0000 for red, 0x00ff00 for green, etc.
Parameters:
name type optional default description
rgb number No The color to fill this Render Texture with, such as 0xff0000 for red.
alpha number Yes 1 The alpha value used by the fill.
x number Yes 0 The left coordinate of the fill rectangle.
y number Yes 0 The top coordinate of the fill rectangle.
width number Yes "this.width" The width of the fill rectangle.
height number Yes "this.height" The height of the fill rectangle.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L226
Since: 3.2.0
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/rendertexture/RenderTexture.js#L816
Since: 3.9.0
repeat ​
<instance> repeat(key, [frame], [x], [y], [width], [height], [alpha], [tint], [skipBatch]) ​
Description:
Takes the given Texture Frame and draws it to this Render Texture as a fill pattern,
i.e. in a grid-layout based on the frame dimensions.
Textures are referenced by their string-based keys, as stored in the Texture Manager.
You can optionally provide a position, width, height, alpha and tint value to apply to
the frames before they are drawn. The position controls the top-left where the repeating
fill will start from. The width and height control the size of the filled area.
The position can be negative if required, but the dimensions cannot.
Calling this method will cause a batch flush by default. Use the skipBatch argument
to disable this if this call is part of a larger batch draw.
Parameters:
name type optional default description
key string No The key of the texture to be used, as stored in the Texture Manager.
frame string | number Yes The name or index of the frame within the Texture. Set to null to skip this argument if not required.
x number Yes 0 The x position to start drawing the frames from (can be negative to offset).
y number Yes 0 The y position to start drawing the frames from (can be negative to offset).
width number Yes "this.width" The width of the area to repeat the frame within. Defaults to the width of this Dynamic Texture.
height number Yes "this.height" The height of the area to repeat the frame within. Defaults to the height of this Dynamic Texture.
alpha number Yes 1 The alpha to use. Defaults to 1, no alpha.
tint number Yes "0xffffff" WebGL only. The tint color to use. Leave as undefined, or 0xffffff to have no tint.
skipBatch boolean Yes false Skip beginning and ending a batch with this call. Use if this is part of a bigger batched draw.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L451
Since: 3.60.0
resize ​
<instance> resize(width, [height], [forceEven]) ​
Description:
Resizes the Render Texture to the new dimensions given.
In WebGL it will destroy and then re-create the frame buffer being used by the Render Texture.
In Canvas it will resize the underlying canvas element.
Both approaches will erase everything currently drawn to the Render Texture.
Calling this will then invoke the setSize method, setting the internal size of this Game Object
to the values given to this method.
If the dimensions given are the same as those already being used, calling this method will do nothing.
Parameters:
name type optional default description
width number No The new width of the Render Texture.
height number Yes "width" The new height of the Render Texture. If not specified, will be set the same as the width .
forceEven boolean Yes true Force the given width and height to be rounded to even values. This significantly improves the rendering quality. Set to false if you know you need an odd sized texture.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture.
Source: src/gameobjects/rendertexture/RenderTexture.js#L146
Since: 3.10.0
saveTexture ​
<instance> saveTexture(key) ​
Description:
Stores a copy of this Render Texture in the Texture Manager using the given key.
After doing this, any texture based Game Object, such as a Sprite, can use the contents of this
Render Texture by using the texture key:
var rt = this . add . renderTexture ( 0 , 0 , 128 , 128 ) ;
// Draw something to the Render Texture
rt . saveTexture ( 'doodle' ) ;
this . add . image ( 400 , 300 , 'doodle' ) ;
Updating the contents of this Render Texture will automatically update any Game Object
that is using it as a texture. Calling saveTexture again will not save another copy
of the same texture, it will just rename the key of the existing copy.
By default it will create a single base texture. You can add frames to the texture
by using the Texture.add method. After doing this, you can then allow Game Objects
to use a specific frame from a Render Texture.
If you destroy this Render Texture, any Game Object using it via the Texture Manager will
stop rendering. Ensure you remove the texture from the Texture Manager and any Game Objects
using it first, before destroying this Render Texture.
Parameters:
name type optional description
key string No The unique key to store the texture as within the global Texture Manager.
Returns: Phaser.Textures.DynamicTexture - The Texture that was saved.
Source: src/gameobjects/rendertexture/RenderTexture.js#L177
Since: 3.12.0
setSize ​
<instance> setSize(width, height) ​
Description:
Sets the internal size of this Render Texture, as used for frame or physics body creation.
This will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or call the
setDisplaySize method, which is the same thing as changing the scale but allows you
to do so by giving pixel values. You could also call the resize method, as that
will resize the underlying texture.
If you have enabled this Game Object for input, changing the size will also change the
size of the hit area, unless you have defined a custom hit area.
Parameters:
name type optional description
width number No The width of this Game Object.
height number No The height of this Game Object.
Overrides: Phaser.GameObjects.Image#setSize
Returns: Phaser.GameObjects.RenderTexture - This Game Object instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L108
Since: 3.0.0
snapshot ​
<instance> snapshot(callback, [type], [encoderOptions]) ​
Description:
Takes a snapshot of the whole of this Render Texture.
The snapshot is taken immediately, but the results are returned via the given callback.
To capture a portion of this Render Texture see the snapshotArea method.
To capture just a specific pixel, see the snapshotPixel method.
Snapshots work by using the WebGL readPixels feature to grab every pixel from the frame buffer
into an ArrayBufferView. It then parses this, copying the contents to a temporary Canvas and finally
creating an Image object from it, which is the image returned to the callback provided.
All in all, this is a computationally expensive and blocking process, which gets more expensive
the larger the resolution this Render Texture has, so please be careful how you employ this in your game.
Parameters:
name type optional default description
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot image is created.
type string Yes "'image/png'" The format of the image to create, usually image/png or image/jpeg .
encoderOptions number Yes 0.92 The image quality, between 0 and 1. Used for image formats with lossy compression, such as image/jpeg .
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L761
Since: 3.19.0
snapshotArea ​
<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions]) ​
Description:
Takes a snapshot of the given area of this Render Texture.
The snapshot is taken immediately, but the results are returned via the given callback.
To capture the whole Render Texture see the snapshot method.
To capture just a specific pixel, see the snapshotPixel method.
Snapshots work by using the WebGL readPixels feature to grab every pixel from the frame buffer
into an ArrayBufferView. It then parses this, copying the contents to a temporary Canvas and finally
creating an Image object from it, which is the image returned to the callback provided.
All in all, this is a computationally expensive and blocking process, which gets more expensive
the larger the resolution this Render Texture has, so please be careful how you employ this in your game.
Parameters:
name type optional default description
x number No The x coordinate to grab from.
y number No The y coordinate to grab from.
width number No The width of the area to grab.
height number No The height of the area to grab.
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot image is created.
type string Yes "'image/png'" The format of the image to create, usually image/png or image/jpeg .
encoderOptions number Yes 0.92 The image quality, between 0 and 1. Used for image formats with lossy compression, such as image/jpeg .
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L726
Since: 3.19.0
snapshotPixel ​
<instance> snapshotPixel(x, y, callback) ​
Description:
Takes a snapshot of the given pixel from this Render Texture.
The snapshot is taken immediately, but the results are returned via the given callback.
To capture the whole Render Texture see the snapshot method.
To capture a portion of this Render Texture see the snapshotArea method.
Unlike the two other snapshot methods, this one will send your callback a Color object
containing the color data for the requested pixel. It doesn't need to create an internal
Canvas or Image object, so is a lot faster to execute, using less memory than the other snapshot methods.
Parameters:
name type optional description
x number No The x coordinate of the pixel to get.
y number No The y coordinate of the pixel to get.
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot pixel data is extracted.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L790
Since: 3.19.0
stamp ​
<instance> stamp(key, [frame], [x], [y], [config]) ​
Description:
Takes the given texture key and frame and then stamps it at the given
x and y coordinates. You can use the optional 'config' argument to provide
lots more options about how the stamp is applied, including the alpha,
tint, angle, scale and origin.
By default, the frame will stamp on the x/y coordinates based on its center.
If you wish to stamp from the top-left, set the config originX and
originY properties both to zero.
Parameters:
name type optional default description
key string No The key of the texture to be used, as stored in the Texture Manager.
frame string | number Yes The name or index of the frame within the Texture. Set to null to skip this argument if not required.
x number Yes 0 The x position to draw the frame at.
y number Yes 0 The y position to draw the frame at.
config Phaser.Types.Textures.StampConfig Yes The stamp configuration object, allowing you to set the alpha, tint, angle, scale and origin of the stamp.
Returns: Phaser.GameObjects.RenderTexture - This Render Texture instance.
Source: src/gameobjects/rendertexture/RenderTexture.js#L269
Since: 3.60.0
Previous
Rectangle
Next
Rope
Inherited Members
Public Members
camera
Inherited Methods
Public Methods
batchDraw
batchDrawFrame
beginDraw
clear
draw
drawFrame
endDraw
erase
fill
preDestroy
repeat
resize
saveTexture
setSize
snapshot
snapshotArea
snapshotPixel
stamp
