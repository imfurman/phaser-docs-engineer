# Shader | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-shader

Phaser API Documentation
Class
Shader
Version: Phaser v3.90.0
On this page
Shader
A Shader Game Object.
This Game Object allows you to easily add a quad with its own shader into the display list, and manipulate it
as you would any other Game Object, including scaling, rotating, positioning and adding to Containers. Shaders
can be masked with either Bitmap or Geometry masks and can also be used as a Bitmap Mask for a Camera or other
Game Object. They can also be made interactive and used for input events.
It works by taking a reference to a Phaser.Display.BaseShader instance, as found in the Shader Cache. These can
be created dynamically at runtime, or loaded in via the GLSL File Loader:
function preload ( )
{
this . load . glsl ( 'fire' , 'shaders/fire.glsl.js' ) ;
}
function create ( )
{
this . add . shader ( 'fire' , 400 , 300 , 512 , 512 ) ;
}
Please see the Phaser 3 Examples GitHub repo for examples of loading and creating shaders dynamically.
Due to the way in which they work, you cannot directly change the alpha or blend mode of a Shader. This should
be handled via exposed uniforms in the shader code itself.
By default a Shader will be created with a standard set of uniforms. These were added to match those
found on sites such as ShaderToy or GLSLSandbox, and provide common functionality a shader may need,
such as the timestamp, resolution or pointer position. You can replace them by specifying your own uniforms
in the Base Shader.
These Shaders work by halting the current pipeline during rendering, creating a viewport matched to the
size of this Game Object and then renders a quad using the bound shader. At the end, the pipeline is restored.
Because it blocks the pipeline it means it will interrupt any batching that is currently going on, so you should
use these Game Objects sparingly. If you need to have a fully batched custom shader, then please look at using
a custom pipeline instead. However, for background or special masking effects, they are extremely effective.
Constructor
new Shader(scene, key, [x], [y], [width], [height], [textures], [textureData])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
key string | Phaser.Display.BaseShader No The key of the shader to use from the shader cache, or a BaseShader instance.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
width number Yes 128 The width of the Game Object.
height number Yes 128 The height of the Game Object.
textures Array.<string> Yes Optional array of texture keys to bind to the iChannel0...3 uniforms. The textures must already exist in the Texture Manager.
textureData any Yes Additional texture data if you want to create shader with none NPOT textures.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.ComputedSize
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/shader/Shader.js#L18
Since: 3.17.0
Inherited Members ​
From Phaser.GameObjects.Components.ComputedSize :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
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
bytes ​
bytes: Uint8Array ​
Description:
Uint8 view to the vertex raw buffer. Used for uploading vertex buffer resources to the GPU.
Source: src/gameobjects/shader/Shader.js#L201
Since: 3.17.0
framebuffer ​
framebuffer: Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper ​
Description:
A reference to the GL Frame Buffer this Shader is drawing to.
This property is only set if you have called Shader.setRenderToTexture .
Source: src/gameobjects/shader/Shader.js#L328
Since: 3.19.0
gl ​
gl: WebGLRenderingContext ​
Description:
The WebGL context belonging to the renderer.
Source: src/gameobjects/shader/Shader.js#L143
Since: 3.17.0
glTexture ​
glTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper ​
Description:
A reference to the WebGLTextureWrapper this Shader is rendering to.
This property is only set if you have called Shader.setRenderToTexture .
Source: src/gameobjects/shader/Shader.js#L338
Since: 3.19.0
pointer ​
pointer: Phaser.Input.Pointer ​
Description:
The pointer bound to this shader, if any.
Set via the chainable setPointer method, or by modifying this property directly.
Source: src/gameobjects/shader/Shader.js#L288
Since: 3.17.0
program ​
program: Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper ​
Description:
The WebGL shader program this shader uses.
Source: src/gameobjects/shader/Shader.js#L192
Since: 3.17.0
projectionMatrix ​
projectionMatrix: Float32Array ​
Description:
The projection matrix the shader uses during rendering.
Source: src/gameobjects/shader/Shader.js#L259
Since: 3.17.0
renderer ​
renderer: Phaser.Renderer.Canvas.CanvasRenderer , Phaser.Renderer.WebGL.WebGLRenderer ​
Description:
A reference to the current renderer.
Shaders only work with the WebGL Renderer.
Source: src/gameobjects/shader/Shader.js#L133
Since: 3.17.0
renderToTexture ​
renderToTexture: boolean ​
Description:
A flag that indicates if this Shader has been set to render to a texture instead of the display list.
This property is true if you have called Shader.setRenderToTexture , otherwise it's false .
A Shader that is rendering to a texture does not appear on the display list.
Source: src/gameobjects/shader/Shader.js#L348
Since: 3.19.0
shader ​
shader: Phaser.Display.BaseShader ​
Description:
The underlying shader object being used.
Empty by default and set during a call to the setShader method.
Source: src/gameobjects/shader/Shader.js#L121
Since: 3.17.0
texture ​
texture: Phaser.Textures.Texture ​
Description:
A reference to the Phaser.Textures.Texture that has been stored in the Texture Manager for this Shader.
This property is only set if you have called Shader.setRenderToTexture with a key, otherwise it is null .
Source: src/gameobjects/shader/Shader.js#L362
Since: 3.19.0
uniforms ​
uniforms: any ​
Description:
The default uniform mappings. These can be added to (or replaced) by specifying your own uniforms when
creating this shader game object. The uniforms are updated automatically during the render step.
The defaults are:
resolution (2f) - Set to the size of this shader.
time (1f) - The elapsed game time, in seconds.
mouse (2f) - If a pointer has been bound (with setPointer ), this uniform contains its position each frame.
date (4fv) - A vec4 containing the year, month, day and time in seconds.
sampleRate (1f) - Sound sample rate. 44100 by default.
iChannel0...3 (sampler2D) - Input channels 0 to 3. null by default.
Source: src/gameobjects/shader/Shader.js#L269
Since: 3.17.0
vertexBuffer ​
vertexBuffer: Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper ​
Description:
The WebGL vertex buffer object this shader uses.
Source: src/gameobjects/shader/Shader.js#L161
Since: 3.17.0
vertexData ​
vertexData: ArrayBuffer ​
Description:
Raw byte buffer of vertices this Shader uses.
Source: src/gameobjects/shader/Shader.js#L152
Since: 3.17.0
vertexViewF32 ​
vertexViewF32: Float32Array ​
Description:
Float32 view of the array buffer containing the shaders vertices.
Source: src/gameobjects/shader/Shader.js#L210
Since: 3.17.0
viewMatrix ​
viewMatrix: Float32Array ​
Description:
The view matrix the shader uses during rendering.
Source: src/gameobjects/shader/Shader.js#L249
Since: 3.17.0
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
From Phaser.GameObjects.Components.ComputedSize :
setDisplaySize
setSize
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
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
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
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
Public Methods ​
flush ​
<instance> flush() ​
Description:
Called automatically during render.
Sets the active shader, loads the vertex buffer and then draws.
Source: src/gameobjects/shader/Shader.js#L1130
Since: 3.17.0
getUniform ​
<instance> getUniform(key) ​
Description:
Returns the uniform object for the given key, or null if the uniform couldn't be found.
Parameters:
name type optional description
key string No The key of the uniform to return the value for.
Returns: any - A reference to the uniform object. This is not a copy, so modifying it will update the original object also.
Source: src/gameobjects/shader/Shader.js#L835
Since: 3.17.0
load ​
<instance> load([matrix2D]) ​
Description:
Called automatically during render.
This method performs matrix ITRS and then stores the resulting value in the uViewMatrix uniform.
It then sets up the vertex buffer and shader, updates and syncs the uniforms ready
for flush to be called.
Parameters:
name type optional description
matrix2D Phaser.GameObjects.Components.TransformMatrix Yes The transform matrix to use during rendering.
Source: src/gameobjects/shader/Shader.js#L1058
Since: 3.17.0
onContextRestored ​
<instance> onContextRestored() ​
Description:
Run any logic that was deferred during context loss.
Source: src/gameobjects/shader/Shader.js#L1220
Since: 3.80.0
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/shader/Shader.js#L1248
Since: 3.17.0
projOrtho ​
<instance> projOrtho(left, right, bottom, top) ​
Description:
Sets this shader to use an orthographic projection matrix.
This matrix is stored locally in the projectionMatrix property,
as well as being bound to the uProjectionMatrix uniform.
Parameters:
name type optional description
left number No The left value.
right number No The right value.
bottom number No The bottom value.
top number No The top value.
Source: src/gameobjects/shader/Shader.js#L602
Since: 3.17.0
setChannel0 ​
<instance> setChannel0(textureKey, [textureData]) ​
Description:
A short-cut method that will directly set the texture being used by the iChannel0 sampler2D uniform.
The textureKey given is the key from the Texture Manager cache. You cannot use a single frame
from a texture, only the full image. Also, lots of shaders expect textures to be power-of-two sized.
Parameters:
name type optional description
textureKey string No The key of the texture, as stored in the Texture Manager. Must already be loaded.
textureData any Yes Additional texture data.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L850
Since: 3.17.0
setChannel1 ​
<instance> setChannel1(textureKey, [textureData]) ​
Description:
A short-cut method that will directly set the texture being used by the iChannel1 sampler2D uniform.
The textureKey given is the key from the Texture Manager cache. You cannot use a single frame
from a texture, only the full image. Also, lots of shaders expect textures to be power-of-two sized.
Parameters:
name type optional description
textureKey string No The key of the texture, as stored in the Texture Manager. Must already be loaded.
textureData any Yes Additional texture data.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L869
Since: 3.17.0
setChannel2 ​
<instance> setChannel2(textureKey, [textureData]) ​
Description:
A short-cut method that will directly set the texture being used by the iChannel2 sampler2D uniform.
The textureKey given is the key from the Texture Manager cache. You cannot use a single frame
from a texture, only the full image. Also, lots of shaders expect textures to be power-of-two sized.
Parameters:
name type optional description
textureKey string No The key of the texture, as stored in the Texture Manager. Must already be loaded.
textureData any Yes Additional texture data.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L888
Since: 3.17.0
setChannel3 ​
<instance> setChannel3(textureKey, [textureData]) ​
Description:
A short-cut method that will directly set the texture being used by the iChannel3 sampler2D uniform.
The textureKey given is the key from the Texture Manager cache. You cannot use a single frame
from a texture, only the full image. Also, lots of shaders expect textures to be power-of-two sized.
Parameters:
name type optional description
textureKey string No The key of the texture, as stored in the Texture Manager. Must already be loaded.
textureData any Yes Additional texture data.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L907
Since: 3.17.0
setPointer ​
<instance> setPointer([pointer]) ​
Description:
Binds a Phaser Pointer object to this Shader.
The screen position of the pointer will be set in to the shaders mouse uniform
automatically every frame. Call this method with no arguments to unbind the pointer.
Parameters:
name type optional description
pointer Phaser.Input.Pointer Yes The Pointer to bind to this shader.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L582
Since: 3.17.0
setRenderToTexture ​
<instance> setRenderToTexture([key], [flipY]) ​
Description:
Changes this Shader so instead of rendering to the display list it renders to a
WebGL Framebuffer and WebGL Texture instead. This allows you to use the output
of this shader as an input for another shader, by mapping a sampler2D uniform
to it.
After calling this method the Shader.framebuffer and Shader.glTexture properties
are populated.
Additionally, you can provide a key to this method. Doing so will create a Phaser Texture
from this Shader and save it into the Texture Manager, allowing you to then use it for
any texture-based Game Object, such as a Sprite or Image:
var shader = this . add . shader ( 'myShader' , x , y , width , height ) ;
shader . setRenderToTexture ( 'doodle' ) ;
this . add . image ( 400 , 300 , 'doodle' ) ;
Note that it stores an active reference to this Shader. That means as this shader updates,
so does the texture and any object using it to render with. Also, if you destroy this
shader, be sure to clear any objects that may have been using it as a texture too.
You can access the Phaser Texture that is created via the Shader.texture property.
By default it will create a single base texture. You can add frames to the texture
by using the Texture.add method. After doing this, you can then allow Game Objects
to use a specific frame from a Render Texture.
Parameters:
name type optional default description
key string Yes The unique key to store the texture as within the global Texture Manager.
flipY boolean Yes false Does this texture need vertically flipping before rendering? This should usually be set to true if being fed from a buffer.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L404
Since: 3.19.0
setSampler2D ​
<instance> setSampler2D(uniformKey, textureKey, [textureIndex], [textureData]) ​
Description:
Sets a sampler2D uniform on this shader.
The textureKey given is the key from the Texture Manager cache. You cannot use a single frame
from a texture, only the full image. Also, lots of shaders expect textures to be power-of-two sized.
If you wish to use another Shader as a sampler2D input for this shader, see the Shader.setSampler2DBuffer method.
Parameters:
name type optional default description
uniformKey string No The key of the sampler2D uniform to be updated, i.e. iChannel0 .
textureKey string No The key of the texture, as stored in the Texture Manager. Must already be loaded.
textureIndex number Yes 0 The texture index.
textureData any Yes Additional texture data.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L739
Since: 3.17.0
setSampler2DBuffer ​
<instance> setSampler2DBuffer(uniformKey, texture, width, height, [textureIndex], [textureData]) ​
Description:
Sets a sampler2D uniform on this shader where the source texture is a WebGLTextureBuffer.
This allows you to feed the output from one Shader into another:
let shader1 = this . add . shader ( baseShader1 , 0 , 0 , 512 , 512 ) . setRenderToTexture ( ) ;
let shader2 = this . add . shader ( baseShader2 , 0 , 0 , 512 , 512 ) . setRenderToTexture ( 'output' ) ;
shader1 . setSampler2DBuffer ( 'iChannel0' , shader2 . glTexture , 512 , 512 ) ;
shader2 . setSampler2DBuffer ( 'iChannel0' , shader1 . glTexture , 512 , 512 ) ;
In the above code, the result of baseShader1 is fed into Shader2 as the iChannel0 sampler2D uniform.
The result of baseShader2 is then fed back into shader1 again, creating a feedback loop.
If you wish to use an image from the Texture Manager as a sampler2D input for this shader,
see the Shader.setSampler2D method.
Parameters:
name type optional default description
uniformKey string No The key of the sampler2D uniform to be updated, i.e. iChannel0 .
texture Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper No A texture reference.
width number No The width of the texture.
height number No The height of the texture.
textureIndex number Yes 0 The texture index.
textureData any Yes Additional texture data.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L687
Since: 3.19.0
setShader ​
<instance> setShader(key, [textures], [textureData]) ​
Description:
Sets the fragment and, optionally, the vertex shader source code that this Shader will use.
This will immediately delete the active shader program, if set, and then create a new one
with the given source. Finally, the shader uniforms are initialized.
Parameters:
name type optional description
key string | Phaser.Display.BaseShader No The key of the shader to use from the shader cache, or a BaseShader instance.
textures Array.<string> Yes Optional array of texture keys to bind to the iChannel0...3 uniforms. The textures must already exist in the Texture Manager.
textureData any Yes Additional texture data.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L485
Since: 3.17.0
setUniform ​
<instance> setUniform(key, value) ​
Description:
Sets a property of a uniform already present on this shader.
To modify the value of a uniform such as a 1f or 1i use the value property directly:
shader . setUniform ( 'size.value' , 16 ) ;
You can use dot notation to access deeper values, for example:
shader . setUniform ( 'resolution.value.x' , 512 ) ;
The change to the uniform will take effect the next time the shader is rendered.
Parameters:
name type optional description
key string No The key of the uniform to modify. Use dots for deep properties, i.e. resolution.value.x .
value any No The value to set into the uniform.
Returns: Phaser.GameObjects.Shader - This Shader instance.
Source: src/gameobjects/shader/Shader.js#L803
Since: 3.17.0
willRender ​
<instance> willRender(camera) ​
Description:
Compares the renderMask with the renderFlags to see if this Game Object will render or not.
Also checks the Game Object against the given Cameras exclusion list.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The Camera to check against this Game Object.
Overrides: Phaser.GameObjects.GameObject#willRender
Returns: boolean - True if the Game Object should be rendered, otherwise false.
Source: src/gameobjects/shader/Shader.js#L381
Since: 3.0.0
Previous
Rope
Next
Shape
Inherited Members
Public Members
bytes
framebuffer
gl
glTexture
pointer
program
projectionMatrix
renderer
renderToTexture
shader
texture
uniforms
vertexBuffer
vertexData
vertexViewF32
viewMatrix
Inherited Methods
Public Methods
flush
getUniform
load
onContextRestored
preDestroy
projOrtho
setChannel0
setChannel1
setChannel2
setChannel3
setPointer
setRenderToTexture
setSampler2D
setSampler2DBuffer
setShader
setUniform
willRender
