# PointLightPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-pointlightpipeline

Phaser API Documentation
Class
PointLightPipeline
Version: Phaser v3.90.0
On this page
PointLightPipeline
The Point Light Pipeline handles rendering the Point Light Game Objects in WebGL.
The fragment shader it uses can be found in shaders/src/PointLight.frag .
The vertex shader it uses can be found in shaders/src/PointLight.vert .
The default shader attributes for this pipeline are:
inPosition (vec2)
inLightPosition (vec2)
inLightRadius (float)
inLightAttenuation (float)
inLightColor (vec4)
The default shader uniforms for this pipeline are:
uProjectionMatrix (mat4)
uResolution (vec2)
uCameraZoom (sampler2D)
Constructor
new PointLightPipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.WebGLPipeline
Source: src/renderer/webgl/pipelines/PointLightPipeline.js#L13
Since: 3.50.0
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
destroy
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
batchLightVert ​
<instance> batchLightVert(x, y, lightX, lightY, radius, attenuation, r, g, b, a) ​
Description:
Adds a single Point Light vertex to the current vertex buffer and increments the
vertexCount property by 1.
This method is called directly by batchPointLight .
Parameters:
name type optional description
x number No The vertex x position.
y number No The vertex y position.
lightX number No The horizontal center of the light.
lightY number No The vertical center of the light.
radius number No The radius of the light.
attenuation number No The attenuation of the light.
r number No The red color channel of the light.
g number No The green color channel of the light.
b number No The blue color channel of the light.
a number No The alpha color channel of the light.
Source: src/renderer/webgl/pipelines/PointLightPipeline.js#L133
Since: 3.50.0
batchPointLight ​
<instance> batchPointLight(light, camera, x0, y0, x1, y1, x2, y2, x3, y3, lightX, lightY) ​
Description:
Adds a Point Light Game Object to the batch, flushing if required.
Parameters:
name type optional description
light Phaser.GameObjects.PointLight No The Point Light Game Object.
camera Phaser.Cameras.Scene2D.Camera No The camera rendering the Point Light.
x0 number No The top-left x position.
y0 number No The top-left y position.
x1 number No The bottom-left x position.
y1 number No The bottom-left y position.
x2 number No The bottom-right x position.
y2 number No The bottom-right y position.
x3 number No The top-right x position.
y3 number No The top-right y position.
lightX number No The horizontal center of the light.
lightY number No The vertical center of the light.
Source: src/renderer/webgl/pipelines/PointLightPipeline.js#L82
Since: 3.50.0
Inherited Members ​
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
Previous
MultiPipeline
Next
PostFXPipeline
Inherited Methods
Public Methods
batchLightVert
batchPointLight
Inherited Members
