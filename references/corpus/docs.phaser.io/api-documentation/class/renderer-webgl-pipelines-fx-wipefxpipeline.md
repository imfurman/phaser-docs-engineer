# WipeFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-wipefxpipeline

Phaser API Documentation
Class
WipeFXPipeline
Version: Phaser v3.90.0
On this page
WipeFXPipeline
The Wipe FX Pipeline.
The wipe or reveal effect is a visual technique that gradually uncovers or conceals elements
in the game, such as images, text, or scene transitions. This effect is often used to create
a sense of progression, reveal hidden content, or provide a smooth and visually appealing transition
between game states.
You can set both the direction and the axis of the wipe effect. The following combinations are possible:
left to right: direction 0, axis 0
right to left: direction 1, axis 0
top to bottom: direction 1, axis 1
bottom to top: direction 1, axis 0
It is up to you to set the progress value yourself, i.e. via a Tween, in order to transition the effect.
A Wipe effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addWipe ( ) ;
sprite . postFX . addReveal ( ) ;
Constructor
new WipeFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/WipeFXPipeline.js#L11
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
axis ​
axis: number ​
Description:
The axis of the wipe effect. Either 0 or 1. Set in conjunction with the direction property.
Source: src/renderer/webgl/pipelines/fx/WipeFXPipeline.js#L88
Since: 3.60.0
direction ​
direction: number ​
Description:
The direction of the wipe effect. Either 0 or 1. Set in conjunction with the axis property.
Source: src/renderer/webgl/pipelines/fx/WipeFXPipeline.js#L79
Since: 3.60.0
progress ​
progress: number ​
Description:
The progress of the Wipe effect. This value is normalized to the range 0 to 1.
Adjust this value to make the wipe transition (i.e. via a Tween)
Source: src/renderer/webgl/pipelines/fx/WipeFXPipeline.js#L59
Since: 3.60.0
reveal ​
reveal: boolean ​
Description:
Is this a reveal (true) or a fade (false) effect?
Source: src/renderer/webgl/pipelines/fx/WipeFXPipeline.js#L97
Since: 3.60.0
wipeWidth ​
wipeWidth: number ​
Description:
The width of the wipe effect. This value is normalized in the range 0 to 1.
Source: src/renderer/webgl/pipelines/fx/WipeFXPipeline.js#L70
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
VignetteFXPipeline
Next
FXPipeline
Inherited Members
Public Members
axis
direction
progress
reveal
wipeWidth
Inherited Methods
