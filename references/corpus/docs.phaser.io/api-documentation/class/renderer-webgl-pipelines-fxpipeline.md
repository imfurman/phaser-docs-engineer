# FXPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-fxpipeline

Phaser API Documentation
Class
FXPipeline
Version: Phaser v3.90.0
On this page
FXPipeline
The FXPipeline is a built-in pipeline that controls the application of FX Controllers during
the rendering process. It maintains all of the FX shaders, instances of Post FX Pipelines and
is responsible for rendering.
You should rarely interact with this pipeline directly. Instead, use the FX Controllers that
is part of the Game Object class in order to manage the effects.
Constructor
new FXPipeline(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser game instance.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.PreFXPipeline
Source: src/renderer/webgl/pipelines/FXPipeline.js#L15
Since: 3.60.0
Inherited Members ​
From Phaser.Renderer.WebGL.Pipelines.PreFXPipeline :
colorMatrixShader
copyShader
drawSpriteShader
fsTarget
gameShader
quadVertexBuffer
quadVertexData
quadVertexViewF32
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
barrel ​
barrel: Phaser.Renderer.WebGL.Pipelines.FX.BarrelFXPipeline ​
Description:
An instance of the Barrel Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L127
Since: 3.60.0
bokeh ​
bokeh: Phaser.Renderer.WebGL.Pipelines.FX.BokehFXPipeline ​
Description:
An instance of the Bokeh Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L145
Since: 3.60.0
circle ​
circle: Phaser.Renderer.WebGL.Pipelines.FX.CircleFXPipeline ​
Description:
An instance of the Circle Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L118
Since: 3.60.0
fxHandlers ​
fxHandlers: Array.<function()> ​
Description:
An array containing references to the methods that map to the FX CONSTs.
This array is intentionally sparse. Do not adjust.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L172
Since: 3.60.0
glow ​
glow: Phaser.Renderer.WebGL.Pipelines.FX.GlowFXPipeline ​
Description:
An instance of the Glow Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L64
Since: 3.60.0
gradient ​
gradient: Phaser.Renderer.WebGL.Pipelines.FX.GradientFXPipeline ​
Description:
An instance of the Gradient Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L109
Since: 3.60.0
pixelate ​
pixelate: Phaser.Renderer.WebGL.Pipelines.FX.PixelateFXPipeline ​
Description:
An instance of the Pixelate Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L82
Since: 3.60.0
shadow ​
shadow: Phaser.Renderer.WebGL.Pipelines.FX.ShadowFXPipeline ​
Description:
An instance of the Shadow Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L73
Since: 3.60.0
shine ​
shine: Phaser.Renderer.WebGL.Pipelines.FX.ShineFXPipeline ​
Description:
An instance of the Shine Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L100
Since: 3.60.0
source ​
source: Phaser.Renderer.WebGL.RenderTarget ​
Description:
The source Render Target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L183
Since: 3.60.0
swap ​
swap: Phaser.Renderer.WebGL.RenderTarget ​
Description:
The swap Render Target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L201
Since: 3.60.0
target ​
target: Phaser.Renderer.WebGL.RenderTarget ​
Description:
The target Render Target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L192
Since: 3.60.0
vignette ​
vignette: Phaser.Renderer.WebGL.Pipelines.FX.VignetteFXPipeline ​
Description:
An instance of the Vignette Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L91
Since: 3.60.0
wipe ​
wipe: Phaser.Renderer.WebGL.Pipelines.FX.WipeFXPipeline ​
Description:
An instance of the Wipe Post FX Pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L136
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
From Phaser.Renderer.WebGL.Pipelines.PreFXPipeline :
batchQuad
bindAndDraw
blendFrames
blendFramesAdditive
copy
copySprite
copyToGame
drawToGame
onCopySprite
onDrawSprite
onResize
resetUVs
setTargetUVs
setUVs
From Phaser.Renderer.WebGL.WebGLPipeline :
addTextureToBatch
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
onPostBatch
onPostRender
onPreBatch
onPreRender
onRebind
onRender
postBatch
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
destroy ​
<instance> destroy() ​
Description:
Destroys all shader instances, removes all object references and nulls all external references.
Overrides: Phaser.Renderer.WebGL.Pipelines.PreFXPipeline#destroy
Returns: Phaser.Renderer.WebGL.Pipelines.FXPipeline - This WebGLPipeline instance.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L585
Since: 3.60.0
onBarrel ​
<instance> onBarrel(config) ​
Description:
Runs the Barrel FX controller.
Parameters:
name type optional description
config Phaser.FX.Barrel No The Barrel FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L508
Since: 3.60.0
onBloom ​
<instance> onBloom(config, width, height) ​
Description:
Runs the Bloom FX controller.
Parameters:
name type optional description
config Phaser.FX.Bloom No The Bloom FX controller.
width number No The width of the target.
height number No The height of the target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L430
Since: 3.60.0
onBlur ​
<instance> onBlur(config, width, height) ​
Description:
Runs the Blur FX controller.
Parameters:
name type optional description
config Phaser.FX.Blur No The Blur FX controller.
width number No The width of the target.
height number No The height of the target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L374
Since: 3.60.0
onBokeh ​
<instance> onBokeh(config) ​
Description:
Runs the Bokeh FX controller.
Parameters:
name type optional description
config Phaser.FX.Bokeh No The Bokeh FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L566
Since: 3.60.0
onCircle ​
<instance> onCircle(config, width, height) ​
Description:
Runs the Circle FX controller.
Parameters:
name type optional description
config Phaser.FX.Circle No The Circle FX controller.
width number No The width of the target.
height number No The height of the target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L487
Since: 3.60.0
onColorMatrix ​
<instance> onColorMatrix(config) ​
Description:
Runs the ColorMatrix FX controller.
Parameters:
name type optional description
config Phaser.FX.ColorMatrix No The ColorMatrix FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L469
Since: 3.60.0
onDisplacement ​
<instance> onDisplacement(config) ​
Description:
Runs the Displacement FX controller.
Parameters:
name type optional description
config Phaser.FX.Displacement No The Displacement FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L527
Since: 3.60.0
onDraw ​
<instance> onDraw(target1, target2, target3) ​
Description:
Takes the currently bound Game Object and runs all of its pre-render effects,
using the given Render Target as the source.
Finally calls drawToGame to copy the result to the Game Canvas.
Parameters:
name type optional description
target1 Phaser.Renderer.WebGL.RenderTarget No The source Render Target.
target2 Phaser.Renderer.WebGL.RenderTarget No The target Render Target.
target3 Phaser.Renderer.WebGL.RenderTarget No The swap Render Target.
Overrides: Phaser.Renderer.WebGL.Pipelines.PreFXPipeline#onDraw
Source: src/renderer/webgl/pipelines/FXPipeline.js#L211
Since: 3.60.0
onGlow ​
<instance> onGlow(config, width, height) ​
Description:
Runs the Glow FX controller.
Parameters:
name type optional description
config Phaser.FX.Glow No The Glow FX controller.
width number No The width of the target.
height number No The height of the target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L273
Since: 3.60.0
onGradient ​
<instance> onGradient(config) ​
Description:
Runs the Gradient FX controller.
Parameters:
name type optional description
config Phaser.FX.Gradient No The Gradient FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L411
Since: 3.60.0
onPixelate ​
<instance> onPixelate(config, width, height) ​
Description:
Runs the Pixelate FX controller.
Parameters:
name type optional description
config Phaser.FX.Pixelate No The Pixelate FX controller.
width number No The width of the target.
height number No The height of the target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L313
Since: 3.60.0
onShadow ​
<instance> onShadow(config) ​
Description:
Runs the Shadow FX controller.
Parameters:
name type optional description
config Phaser.FX.Shadow No The Shadow FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L294
Since: 3.60.0
onShine ​
<instance> onShine(config, width, height) ​
Description:
Runs the Shine FX controller.
Parameters:
name type optional description
config Phaser.FX.Shine No The Shine FX controller.
width number No The width of the target.
height number No The height of the target.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L353
Since: 3.60.0
onVignette ​
<instance> onVignette(config) ​
Description:
Runs the Vignette FX controller.
Parameters:
name type optional description
config Phaser.FX.Vignette No The Vignette FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L334
Since: 3.60.0
onWipe ​
<instance> onWipe(config) ​
Description:
Runs the Wipe FX controller.
Parameters:
name type optional description
config Phaser.FX.Wipe No The Wipe FX controller.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L547
Since: 3.60.0
runDraw ​
<instance> runDraw() ​
Description:
Takes the source and target and runs a copy from source to target.
This will use the current shader and pipeline.
Source: src/renderer/webgl/pipelines/FXPipeline.js#L254
Since: 3.60.0
Previous
WipeFXPipeline
Next
LightPipeline
Inherited Members
Public Members
barrel
bokeh
circle
fxHandlers
glow
gradient
pixelate
shadow
shine
source
swap
target
vignette
wipe
Inherited Methods
Public Methods
destroy
onBarrel
onBloom
onBlur
onBokeh
onCircle
onColorMatrix
onDisplacement
onDraw
onGlow
onGradient
onPixelate
onShadow
onShine
onVignette
onWipe
runDraw
