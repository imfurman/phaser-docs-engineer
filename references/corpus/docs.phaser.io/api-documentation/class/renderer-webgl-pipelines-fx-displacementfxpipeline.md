# DisplacementFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-displacementfxpipeline

Phaser API Documentation
Class
DisplacementFXPipeline
Version: Phaser v3.90.0
On this page
DisplacementFXPipeline
The Displacement FX Pipeline.
The displacement effect is a visual technique that alters the position of pixels in an image
or texture based on the values of a displacement map. This effect is used to create the illusion
of depth, surface irregularities, or distortion in otherwise flat elements. It can be applied to
characters, objects, or backgrounds to enhance realism, convey movement, or achieve various
stylistic appearances.
A Displacement effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addDisplacement ( ) ;
Constructor
new DisplacementFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/DisplacementFXPipeline.js#L11
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
glTexture ​
glTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper ​
Description:
The underlying texture used for displacement.
Source: src/renderer/webgl/pipelines/fx/DisplacementFXPipeline.js#L68
Since: 3.60.0
x ​
x: number ​
Description:
The amount of horizontal displacement to apply.
Source: src/renderer/webgl/pipelines/fx/DisplacementFXPipeline.js#L50
Since: 3.60.0
y ​
y: number ​
Description:
The amount of vertical displacement to apply.
Source: src/renderer/webgl/pipelines/fx/DisplacementFXPipeline.js#L59
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
ColorMatrixFXPipeline
Next
GlowFXPipeline
Inherited Members
Public Members
glTexture
x
y
Inherited Methods
