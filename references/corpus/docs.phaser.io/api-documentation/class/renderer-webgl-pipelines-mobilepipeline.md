# MobilePipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-mobilepipeline

Phaser API Documentation
Class
MobilePipeline
Version: Phaser v3.90.0
On this page
MobilePipeline
The Mobile Pipeline is the core 2D texture rendering pipeline used by Phaser in WebGL
when the device running the game is detected to be a mobile.
You can control the use of this pipeline by setting the Game Configuration
property autoMobilePipeline . If set to false then all devices will use
the Multi Tint Pipeline. You can also call the PipelineManager.setDefaultPipeline
method at run-time, rather than boot-time, to modify the default Game Object
pipeline.
Virtually all Game Objects use this pipeline by default, including Sprites, Graphics
and Tilemaps. It handles the batching of quads and tris, as well as methods for
drawing and batching geometry data.
The fragment shader it uses can be found in shaders/src/Mobile.frag .
The vertex shader it uses can be found in shaders/src/Mobile.vert .
The default shader attributes for this pipeline are:
inPosition (vec2, offset 0)
inTexCoord (vec2, offset 8)
inTexId (float, offset 16)
inTintEffect (float, offset 20)
inTint (vec4, offset 24, normalized)
Note that inTexId isn't used in the shader, it's just kept to allow us
to piggy-back on the Multi Tint Pipeline functions.
The default shader uniforms for this pipeline are:
uProjectionMatrix (mat4)
uResolution (vec2)
uMainSampler (sampler2D, or sampler2D array)
Constructor
new MobilePipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.MultiPipeline
Source: src/renderer/webgl/pipelines/MobilePipeline.js#L15
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
From Phaser.Renderer.WebGL.Pipelines.MultiPipeline :
batchFillPath
batchFillRect
batchFillTriangle
batchLine
batchSprite
batchStrokePath
batchStrokeTriangle
batchTexture
batchTextureFrame
destroy
From Phaser.Renderer.WebGL.WebGLPipeline :
addTextureToBatch
batchQuad
batchTri
batchVert
bind
bindRenderTarget
bindTexture
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
boot ​
<instance> boot() ​
Description:
Called when the Game has fully booted and the Renderer has finished setting up.
By this stage all Game level systems are now in place and you can perform any final
tasks that the pipeline may need that relied on game systems such as the Texture Manager.
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#boot
Source: src/renderer/webgl/pipelines/MobilePipeline.js#L96
Since: 3.60.0
Inherited Members ​
From Phaser.Renderer.WebGL.Pipelines.MultiPipeline :
calcMatrix
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
Previous
LightPipeline
Next
MultiPipeline
Inherited Methods
Public Methods
boot
Inherited Members
