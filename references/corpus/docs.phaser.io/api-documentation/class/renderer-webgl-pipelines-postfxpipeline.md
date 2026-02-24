# PostFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-postfxpipeline

Phaser API Documentation
Class
PostFXPipeline
Version: Phaser v3.90.0
On this page
PostFXPipeline
The Post FX Pipeline is a special kind of pipeline specifically for handling post
processing effects. Where-as a standard Pipeline allows you to control the process
of rendering Game Objects by configuring the shaders and attributes used to draw them,
a Post FX Pipeline is designed to allow you to apply processing after the Game Object/s
have been rendered. Typical examples of post processing effects are bloom filters,
blurs, light effects and color manipulation.
The pipeline works by creating a tiny vertex buffer with just one single hard-coded quad
in it. Game Objects can have a Post Pipeline set on them. Those objects are then rendered
using their standard pipeline, but are redirected to the Render Targets owned by the
post pipeline, which can then apply their own shaders and effects, before passing them
back to the main renderer.
Please see the Phaser 3 examples for further details on this extensive subject.
The default fragment shader it uses can be found in shaders/src/PostFX.frag .
The default vertex shader it uses can be found in shaders/src/Quad.vert .
The default shader attributes for this pipeline are:
inPosition (vec2, offset 0)
inTexCoord (vec2, offset 8)
The vertices array layout is:
-1, 1 B----C 1, 1
0, 1 | /| 1, 1
| / |
| / |
|/ |
-1, -1 A----D 1, -1
0, 0 1, 0
A = -1, -1 (pos) and 0, 0 (uv)
B = -1, 1 (pos) and 0, 1 (uv)
C = 1, 1 (pos) and 1, 1 (uv)
D = 1, -1 (pos) and 1, 0 (uv)
First tri: A, B, C
Second tri: A, C, D
Array index:
0 = Tri 1 - Vert A - x pos
1 = Tri 1 - Vert A - y pos
2 = Tri 1 - Vert A - uv u
3 = Tri 1 - Vert A - uv v
4 = Tri 1 - Vert B - x pos
5 = Tri 1 - Vert B - y pos
6 = Tri 1 - Vert B - uv u
7 = Tri 1 - Vert B - uv v
8 = Tri 1 - Vert C - x pos
9 = Tri 1 - Vert C - y pos
10 = Tri 1 - Vert C - uv u
11 = Tri 1 - Vert C - uv v
12 = Tri 2 - Vert A - x pos
13 = Tri 2 - Vert A - y pos
14 = Tri 2 - Vert A - uv u
15 = Tri 2 - Vert A - uv v
16 = Tri 2 - Vert C - x pos
17 = Tri 2 - Vert C - y pos
18 = Tri 2 - Vert C - uv u
19 = Tri 2 - Vert C - uv v
20 = Tri 2 - Vert D - x pos
21 = Tri 2 - Vert D - y pos
22 = Tri 2 - Vert D - uv u
23 = Tri 2 - Vert D - uv v
Constructor
new PostFXPipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.WebGLPipeline
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L14
Since: 3.50.0
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
colorMatrix ​
colorMatrix: Phaser.Display.ColorMatrix ​
Description:
A Color Matrix instance belonging to this pipeline.
Used during calls to the drawFrame method.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L152
Since: 3.50.0
controller ​
controller: Phaser.FX.Controller ​
Description:
If this Post Pipeline belongs to an FX Controller, this is a
reference to it.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L142
Since: 3.60.0
fullFrame1 ​
fullFrame1: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Full Frame 1 Render Target that belongs to the
Utility Pipeline. This property is set during the boot method.
This Render Target is the full size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L163
Since: 3.50.0
fullFrame2 ​
fullFrame2: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Full Frame 2 Render Target that belongs to the
Utility Pipeline. This property is set during the boot method.
This Render Target is the full size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L179
Since: 3.50.0
gameObject ​
gameObject: Phaser.GameObjects.GameObject , Phaser.Cameras.Scene2D.Camera ​
Description:
If this Post Pipeline belongs to a Game Object or Camera,
this property contains a reference to it.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L132
Since: 3.50.0
halfFrame1 ​
halfFrame1: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Half Frame 1 Render Target that belongs to the
Utility Pipeline. This property is set during the boot method.
This Render Target is half the size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L195
Since: 3.50.0
halfFrame2 ​
halfFrame2: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Half Frame 2 Render Target that belongs to the
Utility Pipeline. This property is set during the boot method.
This Render Target is half the size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L211
Since: 3.50.0
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
batchQuad
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
onDraw
onPostBatch
onPostRender
onPreBatch
onPreRender
onRebind
onRender
onResize
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
bindAndDraw ​
<instance> bindAndDraw(source, [target], [clear], [clearAlpha], [currentShader]) ​
Description:
Binds this pipeline and draws the source Render Target to the target Render Target.
If no target is specified, it will pop the framebuffer from the Renderers FBO stack
and use that instead, which should be done when you need to draw the final results of
this pipeline to the game canvas.
You can optionally set the shader to be used for the draw here, if this is a multi-shader
pipeline. By default currentShader will be used. If you need to set a shader but not
a target, just pass null as the target parameter.
Parameters:
name type optional default description
source Phaser.Renderer.WebGL.RenderTarget No The Render Target to draw from.
target Phaser.Renderer.WebGL.RenderTarget Yes The Render Target to draw to. If not set, it will pop the fbo from the stack.
clear boolean Yes true Clear the target before copying? Only used if target parameter is set.
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
currentShader Phaser.Renderer.WebGL.WebGLShader Yes The shader to use during the draw.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L542
Since: 3.50.0
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
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L442
Since: 3.50.0
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
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L460
Since: 3.50.0
blitFrame ​
<instance> blitFrame(source, target, [brightness], [clear], [clearAlpha], [eraseMode]) ​
Description:
Copy the source Render Target to the target Render Target.
The difference with this copy is that no resizing takes place. If the source
Render Target is larger than the target then only a portion the same size as
the target dimensions is copied across.
You can optionally set the brightness factor of the copy.
Parameters:
name type optional default description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target.
brightness number Yes 1 The brightness value applied to the frame copy.
clear boolean Yes true Clear the target before copying?
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
eraseMode boolean Yes false Erase source from target using ERASE Blend Mode?
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L492
Since: 3.50.0
bootFX ​
<instance> bootFX() ​
Description:
This method is called once, when this Post FX Pipeline needs to be used.
Normally, pipelines will boot automatically, ready for instant-use, but Post FX
Pipelines create quite a lot of internal resources, such as Render Targets, so
they don't boot until they are told to do so by the Pipeline Manager, when an
actual Game Object needs to use them.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L233
Since: 3.70.0
clearFrame ​
<instance> clearFrame(target, [clearAlpha]) ​
Description:
Clears the given Render Target.
Parameters:
name type optional default description
target Phaser.Renderer.WebGL.RenderTarget No The Render Target to clear.
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L478
Since: 3.50.0
copyFrame ​
<instance> copyFrame(source, [target], [brightness], [clear], [clearAlpha]) ​
Description:
Copy the source Render Target to the target Render Target.
You can optionally set the brightness factor of the copy.
The difference between this method and drawFrame is that this method
uses a faster copy shader, where only the brightness can be modified.
If you need color level manipulation, see drawFrame instead.
Parameters:
name type optional default description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget Yes The target Render Target.
brightness number Yes 1 The brightness value applied to the frame copy.
clear boolean Yes true Clear the target before copying?
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L378
Since: 3.50.0
copyFrameRect ​
<instance> copyFrameRect(source, target, x, y, width, height, [clear], [clearAlpha]) ​
Description:
Binds the source Render Target and then copies a section of it to the target Render Target.
This method is extremely fast because it uses gl.copyTexSubImage2D and doesn't
require the use of any shaders. Remember the coordinates are given in standard WebGL format,
where x and y specify the lower-left corner of the section, not the top-left. Also, the
copy entirely replaces the contents of the target texture, no 'merging' or 'blending' takes
place.
Parameters:
name type optional default description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target.
x number No The x coordinate of the lower left corner where to start copying.
y number No The y coordinate of the lower left corner where to start copying.
width number No The width of the texture.
height number No The height of the texture.
clear boolean Yes true Clear the target before copying?
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L516
Since: 3.50.0
copySprite ​
<instance> copySprite(source, target) ​
Description:
Copy the source Render Target to the target Render Target.
This method does not bind a shader. It uses whatever shader
is currently bound in this pipeline. It also does not clear
the frame buffers after use. You should take care of both of
these things if you call this method directly.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L337
Since: 3.60.0
copyToGame ​
<instance> copyToGame(source) ​
Description:
Pops the framebuffer from the renderers FBO stack and sets that as the active target,
then draws the source Render Target to it. It then resets the renderer textures.
This should be done when you need to draw the final results of a pipeline to the game
canvas, or the next framebuffer in line on the FBO stack. You should only call this once
in the onDraw handler and it should be the final thing called. Be careful not to call
this if you need to actually use the pipeline shader, instead of the copy shader. In
those cases, use the bindAndDraw method.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The Render Target to draw from.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L401
Since: 3.50.0
destroy ​
<instance> destroy() ​
Description:
Destroys all shader instances, removes all object references and nulls all external references.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#destroy
Returns: Phaser.Renderer.WebGL.Pipelines.PostFXPipeline - This WebGLPipeline instance.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L619
Since: 3.60.0
drawFrame ​
<instance> drawFrame(source, [target], [clearAlpha]) ​
Description:
Copy the source Render Target to the target Render Target, using this pipelines
Color Matrix.
The difference between this method and copyFrame is that this method
uses a color matrix shader, where you have full control over the luminance
values used during the copy. If you don't need this, you can use the faster
copyFrame method instead.
Parameters:
name type optional default description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget Yes The target Render Target.
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L421
Since: 3.50.0
getController ​
<instance> getController([controller]) ​
Description:
Returns the FX Controller for this Post FX Pipeline.
This is called internally and not typically required outside.
Parameters:
name type optional description
controller Phaser.FX.Controller Yes An FX Controller, or undefined.
Returns: Phaser.FX.Controller , Phaser.Renderer.WebGL.Pipelines.PostFXPipeline - The FX Controller responsible, or this Pipeline.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L309
Since: 3.60.0
postBatch ​
<instance> postBatch([gameObject]) ​
Description:
This method is called as a result of the WebGLPipeline.batchQuad method, right after a quad
belonging to a Game Object has been added to the batch. When this is called, the
renderer has just performed a flush.
It calls the onDraw hook followed by the onPostBatch hook, which can be used to perform
additional Post FX Pipeline processing.
It is also called as part of the PipelineManager.postBatch method when processing Post FX Pipelines.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject | Phaser.Cameras.Scene2D.Camera Yes The Game Object or Camera that invoked this pipeline, if any.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#postBatch
Returns: Phaser.Renderer.WebGL.Pipelines.PostFXPipeline - This WebGLPipeline instance.
Source: src/renderer/webgl/pipelines/PostFXPipeline.js#L268
Since: 3.70.0
Previous
PointLightPipeline
Next
PreFXPipeline
Inherited Members
Public Members
colorMatrix
controller
fullFrame1
fullFrame2
gameObject
halfFrame1
halfFrame2
Inherited Methods
Public Methods
bindAndDraw
blendFrames
blendFramesAdditive
blitFrame
bootFX
clearFrame
copyFrame
copyFrameRect
copySprite
copyToGame
destroy
drawFrame
getController
postBatch
