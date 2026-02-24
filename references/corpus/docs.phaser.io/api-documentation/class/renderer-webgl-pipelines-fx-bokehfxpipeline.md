# BokehFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-bokehfxpipeline

Phaser API Documentation
Class
BokehFXPipeline
Version: Phaser v3.90.0
On this page
BokehFXPipeline
The Bokeh FX Pipeline.
Bokeh refers to a visual effect that mimics the photographic technique of creating a shallow depth of field.
This effect is used to emphasize the game's main subject or action, by blurring the background or foreground
elements, resulting in a more immersive and visually appealing experience. It is achieved through rendering
techniques that simulate the out-of-focus areas, giving a sense of depth and realism to the game's graphics.
This effect can also be used to generate a Tilt Shift effect, which is a technique used to create a miniature
effect by blurring everything except a small area of the image. This effect is achieved by blurring the
top and bottom elements, while keeping the center area in focus.
A Bokeh effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addBokeh ( ) ;
Constructor
new BokehFXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L11
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
The amount, or strength, of the bokeh effect. Defaults to 1.
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L108
Since: 3.60.0
blurX ​
blurX: number ​
Description:
If a Tilt Shift effect this controls the amount of horizontal blur.
Setting this value on a non-Tilt Shift effect will have no effect.
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L73
Since: 3.60.0
blurY ​
blurY: number ​
Description:
If a Tilt Shift effect this controls the amount of vertical blur.
Setting this value on a non-Tilt Shift effect will have no effect.
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L84
Since: 3.60.0
contrast ​
contrast: number ​
Description:
The color contrast, or brightness, of the bokeh effect. Defaults to 0.2.
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L117
Since: 3.60.0
isTiltShift ​
isTiltShift: boolean ​
Description:
Is this a Tilt Shift effect or a standard bokeh effect?
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L53
Since: 3.60.0
radius ​
radius: number ​
Description:
The radius of the bokeh effect.
This is a float value, where a radius of 0 will result in no effect being applied,
and a radius of 1 will result in a strong bokeh. However, you can exceed this value
for even stronger effects.
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L95
Since: 3.60.0
strength ​
strength: number ​
Description:
If a Tilt Shift effect this controls the strength of the blur.
Setting this value on a non-Tilt Shift effect will have no effect.
Source: src/renderer/webgl/pipelines/fx/BokehFXPipeline.js#L62
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
BlurFXPipeline
Next
CircleFXPipeline
Inherited Members
Public Members
amount
blurX
blurY
contrast
isTiltShift
radius
strength
Inherited Methods
