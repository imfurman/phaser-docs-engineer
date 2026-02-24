# GlowFXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fx-glowfxpipeline

Phaser API Documentation
Class
GlowFXPipeline
Version: Phaser v3.90.0
On this page
GlowFXPipeline
The Glow FX Pipeline.
The glow effect is a visual technique that creates a soft, luminous halo around game objects,
characters, or UI elements. This effect is used to emphasize importance, enhance visual appeal,
or convey a sense of energy, magic, or otherworldly presence. The effect can also be set on
the inside of the Game Object. The color and strength of the glow can be modified.
A Glow effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . postFX . addGlow ( ) ;
Constructor
new GlowFXPipeline(game, config)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
config object No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PostFXPipeline
Source: src/renderer/webgl/pipelines/fx/GlowFXPipeline.js#L13
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
A 4 element array of gl color values.
Source: src/renderer/webgl/pipelines/fx/GlowFXPipeline.js#L82
Since: 3.60.0
innerStrength ​
innerStrength: number ​
Description:
The strength of the glow inward from the edge of the Sprite.
Source: src/renderer/webgl/pipelines/fx/GlowFXPipeline.js#L64
Since: 3.60.0
knockout ​
knockout: number ​
Description:
If true only the glow is drawn, not the texture itself.
Source: src/renderer/webgl/pipelines/fx/GlowFXPipeline.js#L73
Since: 3.60.0
outerStrength ​
outerStrength: number ​
Description:
The strength of the glow outward from the edge of the Sprite.
Source: src/renderer/webgl/pipelines/fx/GlowFXPipeline.js#L55
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
DisplacementFXPipeline
Next
GradientFXPipeline
Inherited Members
Public Members
glcolor
innerStrength
knockout
outerStrength
Inherited Methods
