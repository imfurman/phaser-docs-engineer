# BloomFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-bloomfxpipeline

Phaser API Documentation
Class
BloomFXPipeline
Version: Phaser v3.90.0
On this page
BloomFXPipeline
The Bloom FX Pipeline.
Bloom is an effect used to reproduce an imaging artifact of real-world cameras.
The effect produces fringes of light extending from the borders of bright areas in an image,
contributing to the illusion of an extremely bright light overwhelming the
camera or eye capturing the scene.
A Bloom effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addBloom ( ) ;
Constructor
new BloomFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/BloomFXPipeline.js#L11
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
blurStrength ​
blurStrength: number ​
Description:
The strength of the blur process of the bloom effect.
Source: src/renderer/webgl/pipelines/fx/BloomFXPipeline.js#L84
Since: 3.60.0
glcolor ​
glcolor: Array.<number> ​
Description:
The internal gl color array.
Source: src/renderer/webgl/pipelines/fx/BloomFXPipeline.js#L102
Since: 3.60.0
offsetX ​
offsetX: number ​
Description:
The horizontal offset of the bloom effect.
Source: src/renderer/webgl/pipelines/fx/BloomFXPipeline.js#L66
Since: 3.60.0
offsetY ​
offsetY: number ​
Description:
The vertical offset of the bloom effect.
Source: src/renderer/webgl/pipelines/fx/BloomFXPipeline.js#L75
Since: 3.60.0
steps ​
steps: number ​
Description:
The number of steps to run the Bloom effect for.
This value should always be an integer.
It defaults to 4. The higher the value, the smoother the Bloom,
but at the cost of exponentially more gl operations.
Keep this to the lowest possible number you can have it, while
still looking correct for your game.
Source: src/renderer/webgl/pipelines/fx/BloomFXPipeline.js#L49
Since: 3.60.0
strength ​
strength: number ​
Description:
The strength of the blend process of the bloom effect.
Source: src/renderer/webgl/pipelines/fx/BloomFXPipeline.js#L93
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
BarrelFXPipeline
Next
BlurFXPipeline
Inherited Members
Public Members
blurStrength
glcolor
offsetX
offsetY
steps
strength
Inherited Methods
