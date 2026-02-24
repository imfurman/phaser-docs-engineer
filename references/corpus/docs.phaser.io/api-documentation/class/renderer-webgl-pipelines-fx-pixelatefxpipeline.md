# PixelateFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-pixelatefxpipeline

Phaser API Documentation
Class
PixelateFXPipeline
Version: Phaser v3.90.0
On this page
PixelateFXPipeline
The Pixelate FX Pipeline.
The pixelate effect is a visual technique that deliberately reduces the resolution or detail of an image,
creating a blocky or mosaic appearance composed of large, visible pixels. This effect can be used for stylistic
purposes, as a homage to retro gaming, or as a means to obscure certain elements within the game, such as
during a transition or to censor specific content.
A Pixelate effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addPixelate ( ) ;
Constructor
new PixelateFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/PixelateFXPipeline.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.Renderer.WebGL.Pipelines.PostFXPipeline :
colorMatrix
controller
fullFrame1
fullFrame2
gameObject
halfFrame1
halfFrame2
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
amount ​
amount: number ​
Description:
The amount of pixelation to apply.
Source: src/renderer/webgl/pipelines/fx/PixelateFXPipeline.js#L49
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
From Phaser.Renderer.WebGL.Pipelines.PostFXPipeline :
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
Previous
GradientFXPipeline
Next
ShadowFXPipeline
Inherited Members
Public Members
amount
Inherited Methods
