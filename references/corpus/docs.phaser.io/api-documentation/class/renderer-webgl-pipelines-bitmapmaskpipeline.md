# BitmapMaskPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-bitmapmaskpipeline

Phaser API Documentation
Class
BitmapMaskPipeline
Version: Phaser v3.90.0
On this page
BitmapMaskPipeline
The Bitmap Mask Pipeline handles all of the bitmap mask rendering in WebGL for applying
alpha masks to Game Objects. It works by sampling two texture on the fragment shader and
using the fragments alpha to clip the region.
The fragment shader it uses can be found in shaders/src/BitmapMask.frag .
The vertex shader it uses can be found in shaders/src/BitmapMask.vert .
The default shader attributes for this pipeline are:
inPosition (vec2, offset 0)
The default shader uniforms for this pipeline are:
uResolution (vec2)
uMainSampler (sampler2D)
uMaskSampler (sampler2D)
uInvertMaskAlpha (bool)
Constructor
new BitmapMaskPipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.WebGLPipeline
Source: src/renderer/webgl/pipelines/BitmapMaskPipeline.js#L15
Since: 3.0.0
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
beginMask ​
<instance> beginMask(mask, maskedObject, camera) ​
Description:
Binds necessary resources and renders the mask to a separated framebuffer.
The framebuffer for the masked object is also bound for further use.
Parameters:
name type optional description
mask Phaser.Display.Masks.BitmapMask No The BitmapMask instance that called beginMask.
maskedObject Phaser.GameObjects.GameObject No GameObject masked by the mask GameObject.
camera Phaser.Cameras.Scene2D.Camera No The camera rendering the current mask.
Source: src/renderer/webgl/pipelines/BitmapMaskPipeline.js#L81
Since: 3.0.0
endMask ​
<instance> endMask(mask, camera, [renderTarget]) ​
Description:
The masked game objects framebuffer is unbound and its texture
is bound together with the mask texture and the mask shader and
a draw call with a single quad is processed. Here is where the
masking effect is applied.
Parameters:
name type optional description
mask Phaser.Display.Masks.BitmapMask No The BitmapMask instance that called endMask.
camera Phaser.Cameras.Scene2D.Camera No The Camera to render to.
renderTarget Phaser.Renderer.WebGL.RenderTarget Yes Optional WebGL RenderTarget.
Source: src/renderer/webgl/pipelines/BitmapMaskPipeline.js#L97
Since: 3.0.0
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
Previous
PipelineManager
Next
BarrelFXPipeline
Inherited Methods
Public Methods
beginMask
endMask
Inherited Members
