# DynamicTexture | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/textures-dynamictexture

Phaser API Documentation
Class
DynamicTexture
Version: Phaser v3.90.0
On this page
DynamicTexture
A Dynamic Texture is a special texture that allows you to draw textures, frames and most kind of
Game Objects directly to it.
You can take many complex objects and draw them to this one texture, which can then be used as the
base texture for other Game Objects, such as Sprites. Should you then update this texture, all
Game Objects using it will instantly be updated as well, reflecting the changes immediately.
It's a powerful way to generate dynamic textures at run-time that are WebGL friendly and don't invoke
expensive GPU uploads on each change.
const t = this . textures . addDynamicTexture ( 'player' , 64 , 128 ) ;
// draw objects to t
this . add . sprite ( x , y , 'player' ) ;
Because this is a standard Texture within Phaser, you can add frames to it, meaning you can use it
to generate sprite sheets, texture atlases or tile sets.
Under WebGL1, a FrameBuffer, which is what this Dynamic Texture uses internally, cannot be anti-aliased.
This means that when drawing objects such as Shapes or Graphics instances to this texture, they may appear
to be drawn with no aliasing around the edges. This is a technical limitation of WebGL1. To get around it,
create your shape as a texture in an art package, then draw that to this texture.
Based on the assumption that you will be using this Dynamic Texture as a source for Sprites, it will
automatically invert any drawing done to it on the y axis. If you do not require this, please call the
setIsSpriteTexture() method and pass it false as its parameter. Do this before you start drawing
to this texture, otherwise you will get vertically inverted frames under WebGL. This isn't required
for Canvas.
Constructor
new DynamicTexture(manager, key, [width], [height], [forceEven])
Parameters
name type optional default description
manager Phaser.Textures.TextureManager No A reference to the Texture Manager this Texture belongs to.
key string No The unique string-based key of this Texture.
width number Yes 256 The width of this Dymamic Texture in pixels. Defaults to 256 x 256.
height number Yes 256 The height of this Dymamic Texture in pixels. Defaults to 256 x 256.
forceEven boolean Yes true Force the given width and height to be rounded to even values. This significantly improves the rendering quality. Set to false if you know you need an odd sized texture.
Scope : static
Extends
Phaser.Textures.Texture
Source: src/textures/DynamicTexture.js#L19
Since: 3.60.0
Inherited Members ​
From Phaser.Textures.Texture :
customData
dataSource
firstFrame
frames
frameTotal
key
manager
source
Public Members ​
camera ​
camera: Phaser.Cameras.Scene2D.Camera ​
Description:
An internal Camera that can be used to move around this Dynamic Texture.
Control it just like you would any Scene Camera. The difference is that it only impacts
the placement of Game Objects (not textures) that you then draw to this texture.
You can scroll, zoom and rotate this Camera.
Source: src/textures/DynamicTexture.js#L193
Since: 3.12.0
canvas ​
canvas: HTMLCanvasElement ​
Description:
A reference to the Rendering Context belonging to the Canvas Element this Dynamic Texture is drawing to.
Source: src/textures/DynamicTexture.js#L137
Since: 3.2.0
context ​
context: CanvasRenderingContext2D ​
Description:
The 2D Canvas Rendering Context.
Source: src/textures/DynamicTexture.js#L146
Since: 3.7.0
dirty ​
dirty: boolean ​
Description:
Is this Dynamic Texture dirty or not? If not it won't spend time clearing or filling itself.
Source: src/textures/DynamicTexture.js#L156
Since: 3.12.0
height ​
height: number ​
Description:
The height of this Dynamic Texture.
Treat this property as read-only. Use the setSize method to change the size.
Source: src/textures/DynamicTexture.js#L115
Since: 3.60.0
isDrawing ​
isDrawing: boolean ​
Description:
This flag is set to 'true' during beginDraw and reset to 'false in endDraw`,
allowing you to determine if this Dynamic Texture is batch drawing, or not.
Source: src/textures/DynamicTexture.js#L126
Since: 3.60.0
isSpriteTexture ​
isSpriteTexture: boolean ​
Description:
Is this Dynamic Texture being used as the base texture for a Sprite Game Object?
This is enabled by default, as we expect that will be the core use for Dynamic Textures.
However, to disable it, call RenderTexture.setIsSpriteTexture(false) .
You should do this before drawing to this texture, so that it correctly
inverses the frames for WebGL rendering. Not doing so will result in vertically flipped frames.
This property is used in the endDraw method.
Source: src/textures/DynamicTexture.js#L165
Since: 3.60.0
pipeline ​
pipeline: Phaser.Renderer.WebGL.Pipelines.SinglePipeline ​
Description:
A reference to the WebGL Single Pipeline.
This property remains null under Canvas.
Source: src/textures/DynamicTexture.js#L220
Since: 3.60.0
renderer ​
renderer: Phaser.Renderer.Canvas.CanvasRenderer , Phaser.Renderer.WebGL.WebGLRenderer ​
Description:
A reference to either the Canvas or WebGL Renderer that the Game instance is using.
Source: src/textures/DynamicTexture.js#L95
Since: 3.2.0
renderTarget ​
renderTarget: Phaser.Renderer.WebGL.RenderTarget ​
Description:
The Render Target that belongs to this Dynamic Texture.
A Render Target encapsulates a framebuffer and texture for the WebGL Renderer.
This property remains null under Canvas.
Source: src/textures/DynamicTexture.js#L207
Since: 3.60.0
type ​
type: string ​
Description:
The internal data type of this object.
Source: src/textures/DynamicTexture.js#L75
Since: 3.60.0
width ​
width: number ​
Description:
The width of this Dynamic Texture.
Treat this property as read-only. Use the setSize method to change the size.
Source: src/textures/DynamicTexture.js#L104
Since: 3.60.0
Inherited Methods ​
From Phaser.Textures.Texture :
add
get
getDataSourceImage
getFrameBounds
getFrameNames
getFramesFromTextureSource
getSourceImage
getTextureSourceIndex
has
remove
setDataSource
setFilter
Public Methods ​
batchDraw ​
<instance> batchDraw(entries, [x], [y], [alpha], [tint]) ​
Description:
Use this method if you have already called beginDraw and need to batch
draw a large number of objects to this Dynamic Texture.
This method batches the drawing of the given objects to this texture,
without causing a WebGL bind or batch flush for each one.
It is faster than calling draw , but you must be careful to manage the
flow of code and remember to call endDraw() . If you don't need to draw large
numbers of objects it's much safer and easier to use the draw method instead.
The flow should be:
// Call once:
DynamicTexture . beginDraw ( ) ;
// repeat n times:
DynamicTexture . batchDraw ( ) ;
// or
DynamicTexture . batchDrawFrame ( ) ;
// Call once:
DynamicTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Dynamic Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the DynamicTexture.isDrawing boolean property to tell if a batch is
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
Note: You cannot draw a Dynamic Texture to itself.
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
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L1007
Since: 3.50.0
batchDrawFrame ​
<instance> batchDrawFrame(key, [frame], [x], [y], [alpha], [tint]) ​
Description:
Use this method if you have already called beginDraw and need to batch
draw a large number of texture frames to this Dynamic Texture.
This method batches the drawing of the given frames to this Dynamic Texture,
without causing a WebGL bind or batch flush for each one.
It is faster than calling drawFrame , but you must be careful to manage the
flow of code and remember to call endDraw() . If you don't need to draw large
numbers of frames it's much safer and easier to use the drawFrame method instead.
The flow should be:
// Call once:
DynamicTexture . beginDraw ( ) ;
// repeat n times:
DynamicTexture . batchDraw ( ) ;
// or
DynamicTexture . batchDrawFrame ( ) ;
// Call once:
DynamicTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Dynamic Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the DynamicTexture.isDrawing boolean property to tell if a batch is
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
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L1095
Since: 3.50.0
beginDraw ​
<instance> beginDraw() ​
Description:
Use this method if you need to batch draw a large number of Game Objects to
this Dynamic Texture in a single pass, or on a frequent basis. This is especially
useful under WebGL, however, if your game is using Canvas only, it will not make
any speed difference in that situation.
This method starts the beginning of a batched draw, unless one is already open.
Batched drawing is faster than calling draw in loop, but you must be careful
to manage the flow of code and remember to call endDraw() when you're finished.
If you don't need to draw large numbers of objects it's much safer and easier
to use the draw method instead.
The flow should be:
// Call once:
DynamicTexture . beginDraw ( ) ;
// repeat n times:
DynamicTexture . batchDraw ( ) ;
// or
DynamicTexture . batchDrawFrame ( ) ;
// Call once:
DynamicTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Dynamic Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the DynamicTexture.isDrawing boolean property to tell if a batch is
currently open, or not.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L941
Since: 3.50.0
clear ​
<instance> clear([x], [y], [width], [height]) ​
Description:
Clears a portion or everything from this Dynamic Texture by erasing it and resetting it back to
a blank, transparent, texture. To clear an area, specify the x , y , width and height .
Parameters:
name type optional default description
x number Yes 0 The left coordinate of the fill rectangle.
y number Yes 0 The top coordinate of the fill rectangle.
width number Yes "this.width" The width of the fill rectangle.
height number Yes "this.height" The height of the fill rectangle.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L453
Since: 3.2.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Texture and releases references to its sources and frames.
Overrides: Phaser.Textures.Texture#destroy
Source: src/textures/DynamicTexture.js#L1630
Since: 3.60.0
draw ​
<instance> draw(entries, [x], [y], [alpha], [tint]) ​
Description:
Draws the given object, or an array of objects, to this Dynamic Texture.
It can accept any of the following:
Any renderable Game Object, such as a Sprite, Text, Graphics or TileSprite.
Tilemap Layers.
A Group. The contents of which will be iterated and drawn in turn.
A Container. The contents of which will be iterated fully, and drawn in turn.
A Scene Display List. Pass in Scene.children to draw the whole list.
Another Dynamic Texture, or a Render Texture.
A Texture Frame instance.
A string. This is used to look-up the texture from the Texture Manager.
Note 1: You cannot draw a Dynamic Texture to itself.
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
If you are not planning on using this Dynamic Texture as a base texture for Sprite
Game Objects, then you should set DynamicTexture.isSpriteTexture = false before
calling this method, otherwise you will get vertically inverted frames in WebGL.
Parameters:
name type optional default description
entries any No Any renderable Game Object, or Group, Container, Display List, other Render Texture, Texture Frame or an array of any of these.
x number Yes 0 The x position to draw the Frame at, or the offset applied to the object.
y number Yes 0 The y position to draw the Frame at, or the offset applied to the object.
alpha number Yes 1 The alpha value. Only used when drawing Texture Frames to this texture. Game Objects use their own alpha.
tint number Yes "0xffffff" The tint color value. Only used when drawing Texture Frames to this texture. Game Objects use their own tint. WebGL only.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L641
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
If you are not planning on using this Dynamic Texture as a base texture for Sprite
Game Objects, then you should set DynamicTexture.isSpriteTexture = false before
calling this method, otherwise you will get vertically inverted frames in WebGL.
Parameters:
name type optional default description
key string No The key of the texture to be used, as stored in the Texture Manager.
frame string | number Yes The name or index of the frame within the Texture. Set to null to skip this argument if not required.
x number Yes 0 The x position to draw the frame at.
y number Yes 0 The y position to draw the frame at.
alpha number Yes 1 The alpha value. Only used when drawing Texture Frames to this texture.
tint number Yes "0xffffff" The tint color value. Only used when drawing Texture Frames to this texture. WebGL only.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L709
Since: 3.12.0
endDraw ​
<instance> endDraw([erase]) ​
Description:
Use this method to finish batch drawing to this Dynamic Texture.
Doing so will stop the WebGL Renderer from capturing draws and then blit the
framebuffer to the Render Target owned by this texture.
Calling this method without first calling beginDraw will have no effect.
Batch drawing is faster than calling draw , but you must be careful to manage the
flow of code and remember to call endDraw() when you're finished.
If you don't need to draw large numbers of objects it's much safer and easier
to use the draw method instead.
The flow should be:
// Call once:
DynamicTexture . beginDraw ( ) ;
// repeat n times:
DynamicTexture . batchDraw ( ) ;
// or
DynamicTexture . batchDrawFrame ( ) ;
// Call once:
DynamicTexture . endDraw ( ) ;
Do not call any methods other than batchDraw , batchDrawFrame , or endDraw once you
have started a batch. Also, be very careful not to destroy this Dynamic Texture while the
batch is still open. Doing so will cause a run-time error in the WebGL Renderer.
You can use the DynamicTexture.isDrawing boolean property to tell if a batch is
currently open, or not.
Parameters:
name type optional default description
erase boolean Yes false Draws all objects in this batch using a blend mode of ERASE. This has the effect of erasing any filled pixels in the objects being drawn.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L1169
Since: 3.50.0
erase ​
<instance> erase(entries, [x], [y]) ​
Description:
Draws the given object, or an array of objects, to this Dynamic Texture using a blend mode of ERASE.
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
Note: You cannot erase a Dynamic Texture from itself.
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
If you are not planning on using this Dynamic Texture as a base texture for Sprite
Game Objects, then you should set DynamicTexture.isSpriteTexture = false before
calling this method, otherwise you will get vertically inverted frames in WebGL.
Parameters:
name type optional default description
entries any No Any renderable Game Object, or Group, Container, Display List, Render Texture, Texture Frame, or an array of any of these.
x number Yes 0 The x position to draw the Frame at, or the offset applied to the object.
y number Yes 0 The y position to draw the Frame at, or the offset applied to the object.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L579
Since: 3.16.0
fill ​
<instance> fill(rgb, [alpha], [x], [y], [width], [height]) ​
Description:
Fills this Dynamic Texture with the given color.
By default it will fill the entire texture, however you can set it to fill a specific
rectangular area by using the x, y, width and height arguments.
The color should be given in hex format, i.e. 0xff0000 for red, 0x00ff00 for green, etc.
Parameters:
name type optional default description
rgb number No The color to fill this Dynamic Texture with, such as 0xff0000 for red.
alpha number Yes 1 The alpha value used by the fill.
x number Yes 0 The left coordinate of the fill rectangle.
y number Yes 0 The top coordinate of the fill rectangle.
width number Yes "this.width" The width of the fill rectangle.
height number Yes "this.height" The height of the fill rectangle.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L378
Since: 3.2.0
getWebGLTexture ​
<instance> getWebGLTexture() ​
Description:
Returns the underlying WebGLTextureWrapper, if not running in Canvas mode.
Returns: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper - The underlying WebGLTextureWrapper, if not running in Canvas mode.
Source: src/textures/DynamicTexture.js#L1578
Since: 3.60.0
renderCanvas ​
<instance> renderCanvas(renderer, mask, camera) ​
Description:
This is a NOOP method. Bitmap Masks are not supported by the Canvas Renderer.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer | Phaser.Renderer.WebGL.WebGLRenderer No The Canvas Renderer which would be rendered to.
mask Phaser.GameObjects.GameObject No The masked Game Object which would be rendered.
camera Phaser.Cameras.Scene2D.Camera No The Camera to render to.
Source: src/textures/DynamicTexture.js#L1615
Since: 3.60.0
renderWebGL ​
<instance> renderWebGL(renderer, src, camera, parentMatrix) ​
Description:
Renders this Dynamic Texture onto the Stamp Game Object as a BitmapMask.
Parameters:
name type optional description
renderer Phaser.Renderer.WebGL.WebGLRenderer No A reference to the current active WebGL renderer.
src Phaser.GameObjects.Image No The Game Object being rendered in this call.
camera Phaser.Cameras.Scene2D.Camera No The Camera that is rendering the Game Object.
parentMatrix Phaser.GameObjects.Components.TransformMatrix No This transform matrix is defined if the game object is nested
Source: src/textures/DynamicTexture.js#L1594
Since: 3.60.0
repeat ​
<instance> repeat(key, [frame], [x], [y], [width], [height], [alpha], [tint], [skipBatch]) ​
Description:
Takes the given Texture Frame and draws it to this Dynamic Texture as a fill pattern,
i.e. in a grid-layout based on the frame dimensions.
Textures are referenced by their string-based keys, as stored in the Texture Manager.
You can optionally provide a position, width, height, alpha and tint value to apply to
the frames before they are drawn. The position controls the top-left where the repeating
fill will start from. The width and height control the size of the filled area.
The position can be negative if required, but the dimensions cannot.
Calling this method will cause a batch flush by default. Use the skipBatch argument
to disable this if this call is part of a larger batch draw.
If you are not planning on using this Dynamic Texture as a base texture for Sprite
Game Objects, then you should set DynamicTexture.isSpriteTexture = false before
calling this method, otherwise you will get vertically inverted frames in WebGL.
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
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L752
Since: 3.60.0
setFromRenderTarget ​
<instance> setFromRenderTarget() ​
Description:
Links the WebGL Textures used by this Dynamic Texture to its Render Target.
This method is called internally by the Dynamic Texture when it is first created,
or if you change its size.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L334
Since: 3.70.0
setIsSpriteTexture ​
<instance> setIsSpriteTexture(value) ​
Description:
If you are planning on using this Render Texture as a base texture for Sprite
Game Objects, then you should call this method with a value of true before
drawing anything to it, otherwise you will get inverted frames in WebGL.
Parameters:
name type optional description
value boolean No Is this Render Target being used as a Sprite Texture, or not?
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L359
Since: 3.60.0
setSize ​
<instance> setSize(width, [height], [forceEven]) ​
Description:
Resizes this Dynamic Texture to the new dimensions given.
In WebGL it will destroy and then re-create the frame buffer being used by this Dynamic Texture.
In Canvas it will resize the underlying canvas DOM element.
Both approaches will erase everything currently drawn to this texture.
If the dimensions given are the same as those already being used, calling this method will do nothing.
Parameters:
name type optional default description
width number No The new width of this Dynamic Texture.
height number Yes "width" The new height of this Dynamic Texture. If not specified, will be set the same as the width .
forceEven boolean Yes true Force the given width and height to be rounded to even values. This significantly improves the rendering quality. Set to false if you know you need an odd sized texture.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture.
Source: src/textures/DynamicTexture.js#L234
Since: 3.10.0
snapshot ​
<instance> snapshot(callback, [type], [encoderOptions]) ​
Description:
Takes a snapshot of the whole of this Dynamic Texture.
The snapshot is taken immediately, but the results are returned via the given callback.
To capture a portion of this Dynamic Texture see the snapshotArea method.
To capture just a specific pixel, see the snapshotPixel method.
Snapshots work by using the WebGL readPixels feature to grab every pixel from the frame buffer
into an ArrayBufferView. It then parses this, copying the contents to a temporary Canvas and finally
creating an Image object from it, which is the image returned to the callback provided.
All in all, this is a computationally expensive and blocking process, which gets more expensive
the larger the resolution this Dynamic Texture has, so please be careful how you employ this in your game.
Parameters:
name type optional default description
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot image is created.
type string Yes "'image/png'" The format of the image to create, usually image/png or image/jpeg .
encoderOptions number Yes 0.92 The image quality, between 0 and 1. Used for image formats with lossy compression, such as image/jpeg .
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L1523
Since: 3.19.0
snapshotArea ​
<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions]) ​
Description:
Takes a snapshot of the given area of this Dynamic Texture.
The snapshot is taken immediately, but the results are returned via the given callback.
To capture the whole Dynamic Texture see the snapshot method.
To capture just a specific pixel, see the snapshotPixel method.
Snapshots work by using the WebGL readPixels feature to grab every pixel from the frame buffer
into an ArrayBufferView. It then parses this, copying the contents to a temporary Canvas and finally
creating an Image object from it, which is the image returned to the callback provided.
All in all, this is a computationally expensive and blocking process, which gets more expensive
the larger the resolution this Dynamic Texture has, so please be careful how you employ this in your game.
Parameters:
name type optional default description
x number No The x coordinate to grab from.
y number No The y coordinate to grab from.
width number No The width of the area to grab.
height number No The height of the area to grab.
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot image is created.
type string Yes "'image/png'" The format of the image to create, usually image/png or image/jpeg .
encoderOptions number Yes 0.92 The image quality, between 0 and 1. Used for image formats with lossy compression, such as image/jpeg .
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L1481
Since: 3.19.0
snapshotPixel ​
<instance> snapshotPixel(x, y, callback) ​
Description:
Takes a snapshot of the given pixel from this Dynamic Texture.
The snapshot is taken immediately, but the results are returned via the given callback.
To capture the whole Dynamic Texture see the snapshot method.
To capture a portion of this Dynamic Texture see the snapshotArea method.
Unlike the two other snapshot methods, this one will send your callback a Color object
containing the color data for the requested pixel. It doesn't need to create an internal
Canvas or Image object, so is a lot faster to execute, using less memory than the other snapshot methods.
Parameters:
name type optional description
x number No The x coordinate of the pixel to get.
y number No The y coordinate of the pixel to get.
callback Phaser.Types.Renderer.Snapshot.SnapshotCallback No The Function to invoke after the snapshot pixel data is extracted.
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L1552
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
Returns: Phaser.Textures.DynamicTexture - This Dynamic Texture instance.
Source: src/textures/DynamicTexture.js#L499
Since: 3.60.0
Previous
CanvasTexture
Next
Frame
Inherited Members
Public Members
camera
canvas
context
dirty
height
isDrawing
isSpriteTexture
pipeline
renderer
renderTarget
type
width
Inherited Methods
Public Methods
batchDraw
batchDrawFrame
beginDraw
clear
destroy
draw
drawFrame
endDraw
erase
fill
getWebGLTexture
renderCanvas
renderWebGL
repeat
setFromRenderTarget
setIsSpriteTexture
setSize
snapshot
snapshotArea
snapshotPixel
stamp
