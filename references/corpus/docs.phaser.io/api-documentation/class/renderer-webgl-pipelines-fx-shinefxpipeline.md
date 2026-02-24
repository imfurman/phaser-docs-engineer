# ShineFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-shinefxpipeline

Phaser API Documentation
Class
ShineFXPipeline
Version: Phaser v3.90.0
On this page
ShineFXPipeline
The Shine FX Pipeline.
The shine effect is a visual technique that simulates the appearance of reflective
or glossy surfaces by passing a light beam across a Game Object. This effect is used to
enhance visual appeal, emphasize certain features, and create a sense of depth or
material properties.
A Shine effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addShine ( ) ;
Constructor
new ShineFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/ShineFXPipeline.js#L11
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
gradient ​
gradient: number ​
Description:
The gradient of the Shine effect.
Source: src/renderer/webgl/pipelines/fx/ShineFXPipeline.js#L67
Since: 3.60.0
lineWidth ​
lineWidth: number ​
Description:
The line width of the Shine effect.
Source: src/renderer/webgl/pipelines/fx/ShineFXPipeline.js#L58
Since: 3.60.0
reveal ​
reveal: boolean ​
Description:
Does this Shine effect reveal or get added to its target?
Source: src/renderer/webgl/pipelines/fx/ShineFXPipeline.js#L76
Since: 3.60.0
speed ​
speed: number ​
Description:
The speed of the Shine effect.
Source: src/renderer/webgl/pipelines/fx/ShineFXPipeline.js#L49
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
ShadowFXPipeline
Next
VignetteFXPipeline
Inherited Members
Public Members
gradient
lineWidth
reveal
speed
Inherited Methods
