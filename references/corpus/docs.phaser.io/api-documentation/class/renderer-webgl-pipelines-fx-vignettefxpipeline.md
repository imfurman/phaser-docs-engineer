# VignetteFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-vignettefxpipeline

Phaser API Documentation
Class
VignetteFXPipeline
Version: Phaser v3.90.0
On this page
VignetteFXPipeline
The Vignette FX Pipeline.
The vignette effect is a visual technique where the edges of the screen, or a Game Object, gradually darken or blur,
creating a frame-like appearance. This effect is used to draw the player's focus towards the central action or subject,
enhance immersion, and provide a cinematic or artistic quality to the game's visuals.
A Vignette effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addVignette ( ) ;
Constructor
new VignetteFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/VignetteFXPipeline.js#L11
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
radius ​
radius: number ​
Description:
The radius of the vignette effect. This value is normalized to the range 0 to 1.
Source: src/renderer/webgl/pipelines/fx/VignetteFXPipeline.js#L66
Since: 3.60.0
strength ​
strength: number ​
Description:
The strength of the vignette effect.
Source: src/renderer/webgl/pipelines/fx/VignetteFXPipeline.js#L75
Since: 3.60.0
x ​
x: number ​
Description:
The horizontal offset of the vignette effect. This value is normalized to the range 0 to 1.
Source: src/renderer/webgl/pipelines/fx/VignetteFXPipeline.js#L48
Since: 3.60.0
y ​
y: number ​
Description:
The vertical offset of the vignette effect. This value is normalized to the range 0 to 1.
Source: src/renderer/webgl/pipelines/fx/VignetteFXPipeline.js#L57
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
ShineFXPipeline
Next
WipeFXPipeline
Inherited Members
Public Members
radius
strength
x
y
Inherited Methods
