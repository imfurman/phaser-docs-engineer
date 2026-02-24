# ShadowFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-shadowfxpipeline

Phaser API Documentation
Class
ShadowFXPipeline
Version: Phaser v3.90.0
On this page
ShadowFXPipeline
The Shadow FX Pipeline.
The shadow effect is a visual technique used to create the illusion of depth and realism by adding darker,
offset silhouettes or shapes beneath game objects, characters, or environments. These simulated shadows
help to enhance the visual appeal and immersion, making the 2D game world appear more dynamic and three-dimensional.
A Shadow effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addShadow ( ) ;
Constructor
new ShadowFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L11
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
decay ​
decay: number ​
Description:
The amount of decay for the shadow effect.
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L66
Since: 3.60.0
glcolor ​
glcolor: Array.<number> ​
Description:
The internal gl color array.
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L84
Since: 3.60.0
intensity ​
intensity: number ​
Description:
The intensity of the shadow effect.
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L104
Since: 3.60.0
power ​
power: number ​
Description:
The power of the shadow effect.
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L75
Since: 3.60.0
samples ​
samples: number ​
Description:
The number of samples that the shadow effect will run for.
This should be an integer with a minimum value of 1 and a maximum of 12.
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L93
Since: 3.60.0
x ​
x: number ​
Description:
The horizontal offset of the shadow effect.
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L48
Since: 3.60.0
y ​
y: number ​
Description:
The vertical offset of the shadow effect.
Source: src/renderer/webgl/pipelines/fx/ShadowFXPipeline.js#L57
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
PixelateFXPipeline
Next
ShineFXPipeline
Inherited Members
Public Members
decay
glcolor
intensity
power
samples
x
y
Inherited Methods
