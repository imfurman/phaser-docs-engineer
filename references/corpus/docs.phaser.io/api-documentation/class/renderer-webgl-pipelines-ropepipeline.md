# RopePipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-ropepipeline

Phaser API Documentation
Class
RopePipeline
Version: Phaser v3.90.0
On this page
RopePipeline
The Rope Pipeline is a variation of the Multi Pipeline that uses a TRIANGLE_STRIP for
its topology, instead of TRIANGLES. This is primarily used by the Rope Game Object,
or anything that extends it.
Prior to Phaser v3.50 this pipeline was called the TextureTintStripPipeline .
The fragment shader it uses can be found in shaders/src/Multi.frag .
The vertex shader it uses can be found in shaders/src/Multi.vert .
The default shader attributes for this pipeline are:
inPosition (vec2, offset 0)
inTexCoord (vec2, offset 8)
inTexId (float, offset 16)
inTintEffect (float, offset 20)
inTint (vec4, offset 24, normalized)
The default shader uniforms for this pipeline are:
uProjectionMatrix (mat4)
uResolution (vec2)
uMainSampler (sampler2D, or sampler2D array)
The pipeline is structurally identical to the Multi Pipeline and should be treated as such.
Constructor
new RopePipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.MultiPipeline
Source: src/renderer/webgl/pipelines/RopePipeline.js#L11
Since: 3.50.0
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
boot
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
Previous
PreFXPipeline
Next
SinglePipeline
Inherited Members
Inherited Methods
