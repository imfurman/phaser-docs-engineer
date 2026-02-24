# CircleFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-circlefxpipeline

Phaser API Documentation
Class
CircleFXPipeline
Version: Phaser v3.90.0
On this page
CircleFXPipeline
The Circle FX Pipeline.
This effect will draw a circle around the texture of the Game Object, effectively masking off
any area outside of the circle without the need for an actual mask. You can control the thickness
of the circle, the color of the circle and the color of the background, should the texture be
transparent. You can also control the feathering applied to the circle, allowing for a harsh or soft edge.
Please note that adding this effect to a Game Object will not change the input area or physics body of
the Game Object, should it have one.
A Circle effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addCircle ( ) ;
Constructor
new CircleFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/CircleFXPipeline.js#L11
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
feather ​
feather: number ​
Description:
The amount of feathering to apply to the circle from the ring,
extending into the middle of the circle. The default is 0.005,
which is a very low amount of feathering just making sure the ring
has a smooth edge. Increase this amount to a value such as 0.5
or 0.025 for larger amounts of feathering.
Source: src/renderer/webgl/pipelines/fx/CircleFXPipeline.js#L64
Since: 3.60.0
glcolor ​
glcolor: Array.<number> ​
Description:
The internal gl color array for the ring color.
Source: src/renderer/webgl/pipelines/fx/CircleFXPipeline.js#L88
Since: 3.60.0
glcolor2 ​
glcolor2: Array.<number> ​
Description:
The internal gl color array for the background color.
Source: src/renderer/webgl/pipelines/fx/CircleFXPipeline.js#L97
Since: 3.60.0
scale ​
scale: number ​
Description:
The scale of the circle. The default scale is 1, which is a circle
the full size of the underlying texture. Reduce this value to create
a smaller circle, or increase it to create a circle that extends off
the edges of the texture.
Source: src/renderer/webgl/pipelines/fx/CircleFXPipeline.js#L52
Since: 3.60.0
thickness ​
thickness: number ​
Description:
The width of the circle around the texture, in pixels. This value
doesn't factor in the feather, which can extend the thickness
internally depending on its value.
Source: src/renderer/webgl/pipelines/fx/CircleFXPipeline.js#L77
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
BokehFXPipeline
Next
ColorMatrixFXPipeline
Inherited Members
Public Members
feather
glcolor
glcolor2
scale
thickness
Inherited Methods
