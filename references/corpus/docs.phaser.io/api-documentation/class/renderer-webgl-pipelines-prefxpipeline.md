# PreFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-prefxpipeline

Phaser API Documentation
Class
PreFXPipeline
Version: Phaser v3.90.0
On this page
PreFXPipeline
The Pre FX Pipeline is a special kind of pipeline designed specifically for applying
special effects to Game Objects before they are rendered. Where-as the Post FX Pipeline applies an effect after the
object has been rendered, the Pre FX Pipeline allows you to control the rendering of
the object itself - passing it off to its own texture, where multi-buffer compositing
can take place.
You can only use the PreFX Pipeline on the following types of Game Objects, or those
that extend from them:
Sprite
Image
Text
TileSprite
RenderTexture
Video
Constructor
new PreFXPipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.WebGLPipeline
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L20
Since: 3.60.0
Inherited Members ​
From Phaser.Renderer.WebGL.WebGLPipeline :
active
activeBuffer
activeTextures
batch
bytes
config
currentBatch
currentRenderTarget
currentShader
currentTexture
currentUnit
forceZero
game
gl
glReset
hasBooted
height
isPostFX
isPreFX
manager
name
projectionHeight
projectionMatrix
projectionWidth
renderer
renderTargets
resizeUniform
shaders
topology
vertexBuffer
vertexCapacity
vertexCount
vertexData
vertexViewF32
vertexViewU32
view
width
Public Members ​
colorMatrixShader ​
colorMatrixShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Color Matrix Shader belonging to this Pipeline.
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L139
Since: 3.60.0
copyShader ​
copyShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Copy Shader belonging to this Pipeline.
This shader is used when you call the copySprite method.
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L111
Since: 3.60.0
drawSpriteShader ​
drawSpriteShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Draw Sprite Shader belonging to this Pipeline.
This shader is used when the sprite is drawn to this fbo (or to the game if drawToFrame is false)
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L97
Since: 3.60.0
fsTarget ​
fsTarget: Phaser.Renderer.WebGL.RenderTarget ​
Description:
The full-screen Render Target that the sprite is first drawn to.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L199
Since: 3.60.0
gameShader ​
gameShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Game Draw Shader belonging to this Pipeline.
This shader draws the fbo to the game.
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L125
Since: 3.60.0
quadVertexBuffer ​
quadVertexBuffer: Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper ​
Description:
The WebGLBuffer that holds the quadVertexData.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L160
Since: 3.60.0
quadVertexData ​
quadVertexData: ArrayBuffer ​
Description:
Raw byte buffer of vertices used specifically during the copySprite method.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L150
Since: 3.60.0
quadVertexViewF32 ​
quadVertexViewF32: Float32Array ​
Description:
Float32 view of the quad array buffer.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L170
Since: 3.60.0
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
From Phaser.Renderer.WebGL.WebGLPipeline :
addTextureToBatch
batchTri
batchVert
bind
bindRenderTarget
bindTexture
boot
createBatch
drawFillRect
flipProjectionMatrix
flush
getShaderByName
onActive
onAfterFlush
onBatch
onBeforeFlush
onBind
onBoot
onPostBatch
onPostRender
onPreBatch
onPreRender
onRebind
onRender
postBatch
preBatch
pushBatch
rebind
resize
restoreContext
set1f
set1fv
set1i
set1iv
set2f
set2fv
set2i
set2iv
set3f
set3fv
set3i
set3iv
set4f
set4fv
set4i
set4iv
setBoolean
setGameObject
setMatrix2fv
setMatrix3fv
setMatrix4fv
setProjectionMatrix
setShader
setShadersFromConfig
setTexture2D
setTime
setVertexBuffer
shouldFlush
unbind
updateProjectionMatrix
vertexAvailable
Public Methods ​
batchQuad ​
<instance> batchQuad(gameObject, x0, y0, x1, y1, x2, y2, x3, y3, u0, v0, u1, v1, tintTL, tintTR, tintBL, tintBR, tintEffect, [texture]) ​
Description:
Adds the vertices data into the batch and flushes if full.
Assumes 6 vertices in the following arrangement:
0----3
|\ B|
| \ |
| \ |
| A \|
| \
1----2
Where x0 / y0 = 0, x1 / y1 = 1, x2 / y2 = 2 and x3 / y3 = 3
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject | null No The Game Object, if any, drawing this quad.
x0 number No The top-left x position.
y0 number No The top-left y position.
x1 number No The bottom-left x position.
y1 number No The bottom-left y position.
x2 number No The bottom-right x position.
y2 number No The bottom-right y position.
x3 number No The top-right x position.
y3 number No The top-right y position.
u0 number No UV u0 value.
v0 number No UV v0 value.
u1 number No UV u1 value.
v1 number No UV v1 value.
tintTL number No The top-left tint color value.
tintTR number No The top-right tint color value.
tintBL number No The bottom-left tint color value.
tintBR number No The bottom-right tint color value.
tintEffect number | boolean No The tint effect for the shader to use.
texture Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper Yes Texture that will be assigned to the current batch if a flush occurs.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#batchQuad
Returns: boolean - true if this method caused the batch to flush, otherwise false .
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L294
Since: 3.60.0
bindAndDraw ​
<instance> bindAndDraw(source) ​
Description:
This method is called by drawToGame and copyToGame . It takes the source Render Target
and copies it back to the game canvas, or the next frame buffer in the stack, and should
be considered the very last thing this pipeline does.
You don't normally need to call this method, or override it, however it is left public
should you wish to do so.
Note that it does not set a shader. You should do this yourself if invoking this.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The Render Target to draw to the game.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L701
Since: 3.60.0
blendFrames ​
<instance> blendFrames(source1, source2, [target], [strength], [clearAlpha]) ​
Description:
Draws the source1 and source2 Render Targets to the target Render Target
using a linear blend effect, which is controlled by the strength parameter.
Parameters:
name type optional default description
source1 Phaser.Renderer.WebGL.RenderTarget No The first source Render Target.
source2 Phaser.Renderer.WebGL.RenderTarget No The second source Render Target.
target Phaser.Renderer.WebGL.RenderTarget Yes The target Render Target.
strength number Yes 1 The strength of the blend.
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L617
Since: 3.60.0
blendFramesAdditive ​
<instance> blendFramesAdditive(source1, source2, [target], [strength], [clearAlpha]) ​
Description:
Draws the source1 and source2 Render Targets to the target Render Target
using an additive blend effect, which is controlled by the strength parameter.
Parameters:
name type optional default description
source1 Phaser.Renderer.WebGL.RenderTarget No The first source Render Target.
source2 Phaser.Renderer.WebGL.RenderTarget No The second source Render Target.
target Phaser.Renderer.WebGL.RenderTarget Yes The target Render Target.
strength number Yes 1 The strength of the blend.
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L635
Since: 3.60.0
copy ​
<instance> copy(source, target) ​
Description:
Draws the source Render Target to the target Render Target.
This is done using whatever the currently bound shader is. This method does
not set a shader. All it does is bind the source texture, set the viewport and UVs
then bind the target framebuffer, clears it and draws the source to it.
At the end a null framebuffer is bound. No other clearing-up takes place, so
use this method carefully.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L575
Since: 3.60.0
copySprite ​
<instance> copySprite(source, target, [clear], [clearAlpha], [eraseMode], [colorMatrix], [shader]) ​
Description:
Copy the source Render Target to the target Render Target.
No target resizing takes place. If the source Render Target is larger than the target ,
then only a portion the same size as the target dimensions is copied across.
Calling this method will invoke the onCopySprite handler and will also call
the onFXCopy callback on the Sprite. Both of these happen prior to the copy, allowing you
to use them to set shader uniforms and other values.
You can optionally pass in a ColorMatrix. If so, it will use the ColorMatrix shader
during the copy, allowing you to manipulate the colors to a fine degree.
See the ColorMatrix class for more details.
Parameters:
name type optional default description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target being copied from.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target that will be copied to.
clear boolean Yes true Clear the target before copying?
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
eraseMode boolean Yes false Erase source from target using ERASE Blend Mode?
colorMatrix Phaser.Display.ColorMatrix Yes Optional ColorMatrix to use when copying the Sprite.
shader Phaser.Renderer.WebGL.WebGLShader Yes The shader to use to copy the target. Defaults to the copyShader .
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L468
Since: 3.60.0
copyToGame ​
<instance> copyToGame(source) ​
Description:
This method will copy the given Render Target to the game canvas using the gameShader .
Unless you've changed it, the gameShader copies the target without modifying it, just
ensuring it is placed in the correct location on the canvas.
If you wish to draw the target with and apply the fragment shader at the same time,
see the drawToGame method instead.
This method should be the final thing called in your pipeline.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The Render Target to copy to the game.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L676
Since: 3.60.0
destroy ​
<instance> destroy() ​
Description:
Destroys all shader instances, removes all object references and nulls all external references.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#destroy
Returns: Phaser.Renderer.WebGL.Pipelines.PreFXPipeline - This WebGLPipeline instance.
Fires: Phaser.Renderer.WebGL.Pipelines.Events#event:DESTROY
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L888
Since: 3.60.0
drawToGame ​
<instance> drawToGame(source) ​
Description:
This method will copy the given Render Target to the game canvas using the copyShader .
This applies the results of the copy shader during the draw.
If you wish to copy the target without any effects see the copyToGame method instead.
This method should be the final thing called in your pipeline.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The Render Target to draw to the game.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L653
Since: 3.60.0
onCopySprite ​
<instance> onCopySprite(source, target, gameObject) ​
Description:
This callback is invoked when you call the copySprite method.
It will fire after the shader has been set, but before the source target has been copied,
so use it to set any additional uniforms you may need.
Note: Manipulating the Sprite during this callback will not change the Render Targets.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target being copied from.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target that will be copied to.
gameObject Phaser.GameObjects.Sprite No The Sprite being copied.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L449
Since: 3.60.0
onDraw ​
<instance> onDraw(target, [swapTarget], [altSwapTarget]) ​
Description:
This method is called every time the batchSprite method is called and is passed a
reference to the current render target.
If you override this method, then it should make sure it calls either the
drawToGame or copyToGame methods as the final thing it does. However, you can do as
much additional processing as you like prior to this.
Parameters:
name type optional description
target Phaser.Renderer.WebGL.RenderTarget No The Render Target to draw to the game.
swapTarget Phaser.Renderer.WebGL.RenderTarget Yes The Swap Render Target, useful for double-buffer effects.
altSwapTarget Phaser.Renderer.WebGL.RenderTarget Yes The Swap Render Target, useful for double-buffer effects.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#onDraw
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L787
Since: 3.60.0
onDrawSprite ​
<instance> onDrawSprite(gameObject, target) ​
Description:
This callback is invoked when a sprite is drawn by this pipeline.
It will fire after the shader has been set, but before the sprite has been drawn,
so use it to set any additional uniforms you may need.
Note: Manipulating the Sprite during this callback will not change how it is drawn to the Render Target.
Parameters:
name type optional description
gameObject Phaser.GameObjects.Sprite No The Sprite being drawn.
target Phaser.Renderer.WebGL.RenderTarget No The Render Target the Sprite will be drawn to.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L431
Since: 3.60.0
onResize ​
<instance> onResize(width, height) ​
Description:
Handles the resizing of the quad vertex data.
Parameters:
name type optional description
width number No The new width of the quad.
height number No The new height of the quad.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#onResize
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L261
Since: 3.60.0
resetUVs ​
<instance> resetUVs() ​
Description:
Resets the quad vertice UV values to their default settings.
The quad is used by the copy shader in this pipeline.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L875
Since: 3.60.0
setTargetUVs ​
<instance> setTargetUVs(source, target) ​
Description:
Sets the vertex UV coordinates of the quad used by the copy shaders
so that they correctly adjust the texture coordinates for a blit frame effect.
Be sure to call resetUVs once you have finished manipulating the UV coordinates.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L847
Since: 3.60.0
setUVs ​
<instance> setUVs(uA, vA, uB, vB, uC, vC, uD, vD) ​
Description:
Set the UV values for the 6 vertices that make up the quad used by the copy shader.
Be sure to call resetUVs once you have finished manipulating the UV coordinates.
Parameters:
name type optional description
uA number No The u value of vertex A.
vA number No The v value of vertex A.
uB number No The u value of vertex B.
vB number No The v value of vertex B.
uC number No The u value of vertex C.
vC number No The v value of vertex C.
uD number No The u value of vertex D.
vD number No The v value of vertex D.
Source: src/renderer/webgl/pipelines/PreFXPipeline.js#L807
Since: 3.60.0
Previous
PostFXPipeline
Next
RopePipeline
Inherited Members
Public Members
colorMatrixShader
copyShader
drawSpriteShader
fsTarget
gameShader
quadVertexBuffer
quadVertexData
quadVertexViewF32
Inherited Methods
Public Methods
batchQuad
bindAndDraw
blendFrames
blendFramesAdditive
copy
copySprite
copyToGame
destroy
drawToGame
onCopySprite
onDraw
onDrawSprite
onResize
resetUVs
setTargetUVs
setUVs
