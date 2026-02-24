# BlurFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-blurfxpipeline

Phaser API Documentation
Class
BlurFXPipeline
Version: Phaser v3.90.0
On this page
BlurFXPipeline
The Blur FX Pipeline.
A Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect,
typically to reduce image noise and reduce detail. The visual effect of this blurring technique is a
smooth blur resembling that of viewing the image through a translucent screen, distinctly different
from the bokeh effect produced by an out-of-focus lens or the shadow of an object under usual illumination.
A Blur effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addBlur ( ) ;
Constructor
new BlurFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L13
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
glcolor ​
glcolor: Array.<number> ​
Description:
The internal gl color array.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L110
Since: 3.60.0
steps ​
steps: number ​
Description:
The number of steps to run the Blur effect for.
This value should always be an integer.
It defaults to 4. The higher the value, the smoother the blur,
but at the cost of exponentially more gl operations.
Keep this to the lowest possible number you can have it, while
still looking correct for your game.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L84
Since: 3.60.0
strength ​
strength: number ​
Description:
The strength of the blur effect.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L101
Since: 3.60.0
x ​
x: number ​
Description:
The horizontal offset of the blur effect.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L66
Since: 3.60.0
y ​
y: number ​
Description:
The vertical offset of the blur effect.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L75
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
Public Methods ​
setQualityHigh ​
<instance> setQualityHigh() ​
Description:
Sets the quality of the blur effect to high.
Returns: Phaser.Renderer.WebGL.Pipelines.FX.BlurFXPipeline - This FX Pipeline.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L150
Since: 3.60.0
setQualityLow ​
<instance> setQualityLow() ​
Description:
Sets the quality of the blur effect to low.
Returns: Phaser.Renderer.WebGL.Pipelines.FX.BlurFXPipeline - This FX Pipeline.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L120
Since: 3.60.0
setQualityMedium ​
<instance> setQualityMedium() ​
Description:
Sets the quality of the blur effect to medium.
Returns: Phaser.Renderer.WebGL.Pipelines.FX.BlurFXPipeline - This FX Pipeline.
Source: src/renderer/webgl/pipelines/fx/BlurFXPipeline.js#L135
Since: 3.60.0
Previous
BloomFXPipeline
Next
BokehFXPipeline
Inherited Members
Public Members
glcolor
steps
strength
x
y
Inherited Methods
Public Methods
setQualityHigh
setQualityLow
setQualityMedium
