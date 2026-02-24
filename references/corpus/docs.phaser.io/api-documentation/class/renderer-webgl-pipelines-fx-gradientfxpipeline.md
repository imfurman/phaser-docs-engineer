# GradientFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-gradientfxpipeline

Phaser API Documentation
Class
GradientFXPipeline
Version: Phaser v3.90.0
On this page
GradientFXPipeline
The Gradient FX Pipeline.
The gradient overlay effect is a visual technique where a smooth color transition is applied over Game Objects,
such as sprites or UI components. This effect is used to enhance visual appeal, emphasize depth, or create
stylistic and atmospheric variations. It can also be utilized to convey information, such as representing
progress or health status through color changes.
A Gradient effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addGradient ( ) ;
Constructor
new GradientFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L11
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
alpha ​
alpha: number ​
Description:
The alpha value of the gradient effect.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L49
Since: 3.60.0
fromX ​
fromX: number ​
Description:
The horizontal position the gradient will start from. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L70
Since: 3.60.0
fromY ​
fromY: number ​
Description:
The vertical position the gradient will start from. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L79
Since: 3.60.0
glcolor1 ​
glcolor1: Array.<number> ​
Description:
The internal gl color array for the starting color.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L106
Since: 3.60.0
glcolor2 ​
glcolor2: Array.<number> ​
Description:
The internal gl color array for the ending color.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L115
Since: 3.60.0
size ​
size: number ​
Description:
Sets how many 'chunks' the gradient is divided in to, as spread over the
entire height of the texture. Leave this at zero for a smooth gradient,
or set to a higher number to split the gradient into that many sections, giving
a more banded 'retro' effect.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L58
Since: 3.60.0
toX ​
toX: number ​
Description:
The horizontal position the gradient will end. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L88
Since: 3.60.0
toY ​
toY: number ​
Description:
The vertical position the gradient will end. This value is normalized, between 0 and 1 and is not in pixels.
Source: src/renderer/webgl/pipelines/fx/GradientFXPipeline.js#L97
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
GlowFXPipeline
Next
PixelateFXPipeline
Inherited Members
Public Members
alpha
fromX
fromY
glcolor1
glcolor2
size
toX
toY
Inherited Methods
