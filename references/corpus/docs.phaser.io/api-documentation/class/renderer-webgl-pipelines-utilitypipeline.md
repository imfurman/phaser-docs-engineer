# UtilityPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-utilitypipeline

Phaser API Documentation
Class
UtilityPipeline
Version: Phaser v3.90.0
On this page
UtilityPipeline
The Utility Pipeline is a special-use pipeline that belongs to the Pipeline Manager.
It provides 4 shaders and handy associated methods:
Copy Shader. A fast texture to texture copy shader with optional brightness setting.
Additive Blend Mode Shader. Blends two textures using an additive blend mode.
Linear Blend Mode Shader. Blends two textures using a linear blend mode.
Color Matrix Copy Shader. Draws a texture to a target using a Color Matrix.
You do not extend this pipeline, but instead get a reference to it from the Pipeline
Manager via the setUtility method. You can also access methods such as copyFrame
directly from the Pipeline Manager.
This pipeline provides methods for manipulating framebuffer backed textures, such as
copying or blending one texture to another, copying a portion of a texture, additively
blending two textures, flipping textures and more.
The default shader attributes for this pipeline are:
inPosition (vec2, offset 0)
inTexCoord (vec2, offset 8)
This pipeline has a hard-coded batch size of 1 and a hard coded set of vertices.
Constructor
new UtilityPipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.WebGLPipeline
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L18
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
addShader ​
addShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Additive Blend Shader belonging to this Utility Pipeline.
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L146
Since: 3.50.0
colorMatrix ​
colorMatrix: Phaser.Display.ColorMatrix ​
Description:
A default Color Matrix, used by the Color Matrix Shader when one
isn't provided.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L124
Since: 3.50.0
colorMatrixShader ​
colorMatrixShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Color Matrix Shader belonging to this Utility Pipeline.
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L168
Since: 3.50.0
copyShader ​
copyShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Copy Shader belonging to this Utility Pipeline.
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L134
Since: 3.50.0
fullFrame1 ​
fullFrame1: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Full Frame 1 Render Target.
This property is set during the boot method.
This Render Target is the full size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L179
Since: 3.50.0
fullFrame2 ​
fullFrame2: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Full Frame 2 Render Target.
This property is set during the boot method.
This Render Target is the full size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L195
Since: 3.50.0
halfFrame1 ​
halfFrame1: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Half Frame 1 Render Target.
This property is set during the boot method.
This Render Target is half the size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L211
Since: 3.50.0
halfFrame2 ​
halfFrame2: Phaser.Renderer.WebGL.RenderTarget ​
Description:
A reference to the Half Frame 2 Render Target.
This property is set during the boot method.
This Render Target is half the size of the renderer.
You can use this directly in Post FX Pipelines for multi-target effects.
However, be aware that these targets are shared between all post fx pipelines.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L227
Since: 3.50.0
linearShader ​
linearShader: Phaser.Renderer.WebGL.WebGLShader ​
Description:
A reference to the Linear Blend Shader belonging to this Utility Pipeline.
This property is set during the boot method.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L157
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
destroy
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
blendFrames ​
<instance> blendFrames(source1, source2, [target], [strength], [clearAlpha], [blendShader]) ​
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
blendShader Phaser.Renderer.WebGL.WebGLShader Yes The shader to use during the blend copy.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L571
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
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L634
Since: 3.50.0
blitFrame ​
<instance> blitFrame(source, target, [brightness], [clear], [clearAlpha], [eraseMode], [flipY]) ​
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
flipY boolean Yes false Flip the UV on the Y axis before drawing?
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L328
Since: 3.50.0
clearFrame ​
<instance> clearFrame(target, [clearAlpha]) ​
Description:
Clears the given Render Target.
Parameters:
name type optional default description
target Phaser.Renderer.WebGL.RenderTarget No The Render Target to clear.
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L652
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
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L262
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
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L422
Since: 3.50.0
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
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L476
Since: 3.50.0
drawFrame ​
<instance> drawFrame(source, [target], [clearAlpha], [colorMatrix]) ​
Description:
Copy the source Render Target to the target Render Target, using the
given Color Matrix.
The difference between this method and copyFrame is that this method
uses a color matrix shader, where you have full control over the luminance
values used during the copy. If you don't need this, you can use the faster
copyFrame method instead.
Parameters:
name type optional default description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget Yes The target Render Target.
clearAlpha boolean Yes true Clear the alpha channel when running gl.clear on the target?
colorMatrix Phaser.Display.ColorMatrix Yes The Color Matrix to use when performing the draw.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L509
Since: 3.50.0
flipX ​
<instance> flipX() ​
Description:
Horizontally flips the UV coordinates of the quad used by the shaders in this
Utility Pipeline.
Be sure to call resetUVs once you have finished manipulating the UV coordinates.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L751
Since: 3.50.0
flipY ​
<instance> flipY() ​
Description:
Vertically flips the UV coordinates of the quad used by the shaders in this
Utility Pipeline.
Be sure to call resetUVs once you have finished manipulating the UV coordinates.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L765
Since: 3.50.0
resetUVs ​
<instance> resetUVs() ​
Description:
Resets the quad vertice UV values to their default settings.
The quad is used by all shaders of the Utility Pipeline.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L779
Since: 3.50.0
setTargetUVs ​
<instance> setTargetUVs(source, target) ​
Description:
Sets the vertex UV coordinates of the quad used by the shaders in the Utility Pipeline
so that they correctly adjust the texture coordinates for a blit frame effect.
Be sure to call resetUVs once you have finished manipulating the UV coordinates.
Parameters:
name type optional description
source Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target Phaser.Renderer.WebGL.RenderTarget No The target Render Target.
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L723
Since: 3.50.0
setUVs ​
<instance> setUVs(uA, vA, uB, vB, uC, vC, uD, vD) ​
Description:
Set the UV values for the 6 vertices that make up the quad used by the shaders
in the Utility Pipeline.
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
Source: src/renderer/webgl/pipelines/UtilityPipeline.js#L687
Since: 3.50.0
Previous
SinglePipeline
Next
RenderTarget
Inherited Members
Public Members
addShader
colorMatrix
colorMatrixShader
copyShader
fullFrame1
fullFrame2
halfFrame1
halfFrame2
linearShader
Inherited Methods
Public Methods
blendFrames
blendFramesAdditive
blitFrame
clearFrame
copyFrame
copyFrameRect
copyToGame
drawFrame
flipX
flipY
resetUVs
setTargetUVs
setUVs
