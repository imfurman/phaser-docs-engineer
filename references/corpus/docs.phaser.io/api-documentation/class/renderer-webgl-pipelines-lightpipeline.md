# LightPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-lightpipeline

Phaser API Documentation
Class
LightPipeline
Version: Phaser v3.90.0
On this page
LightPipeline
The Light Pipeline is an extension of the Multi Pipeline and uses a custom shader
designed to handle forward diffused rendering of 2D lights in a Scene.
The shader works in tandem with Light Game Objects, and optionally texture normal maps,
to provide an ambient illumination effect.
If you wish to provide your own shader, you can use the %LIGHT_COUNT% declaration in the source,
and it will be automatically replaced at run-time with the total number of configured lights.
The maximum number of lights can be set in the Render Config maxLights property and defaults to 10.
Prior to Phaser v3.50 this pipeline was called the ForwardDiffuseLightPipeline .
The fragment shader it uses can be found in shaders/src/Light.frag .
The vertex shader it uses can be found in shaders/src/Multi.vert .
The default shader attributes for this pipeline are:
inPosition (vec2, offset 0)
inTexCoord (vec2, offset 8)
inTexId (float, offset 16)
inTintEffect (float, offset 20)
inTint (vec4, offset 24, normalized)
The default shader uniforms for this pipeline are those from the Multi Pipeline, plus:
uMainSampler (sampler2D)
uNormSampler (sampler2D)
uCamera (vec4)
uResolution (vec2)
uAmbientLightColor (vec3)
uInverseRotationMatrix (mat3)
uLights (Light struct)
Constructor
new LightPipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.Pipelines.MultiPipeline
Source: src/renderer/webgl/pipelines/LightPipeline.js#L16
Since: 3.50.0
Inherited Members ​
From Phaser.Renderer.WebGL.Pipelines.MultiPipeline :
calcMatrix
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
currentNormalMap; ​
currentNormalMap;: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper ​
Description:
The currently bound normal map texture at texture unit one, if any.
Source: src/renderer/webgl/pipelines/LightPipeline.js#L88
Since: 3.60.0
lightsActive ​
lightsActive: boolean ​
Description:
A boolean that is set automatically during onRender that determines
if the Scene LightManager is active, or not.
Source: src/renderer/webgl/pipelines/LightPipeline.js#L97
Since: 3.53.0
tempVec2 ​
tempVec2: Phaser.Math.Vector2 ​
Description:
A persistent calculation vector used when processing the lights.
Source: src/renderer/webgl/pipelines/LightPipeline.js#L108
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
From Phaser.Renderer.WebGL.Pipelines.MultiPipeline :
batchFillPath
batchFillRect
batchFillTriangle
batchLine
batchStrokePath
batchStrokeTriangle
destroy
From Phaser.Renderer.WebGL.WebGLPipeline :
addTextureToBatch
batchQuad
batchTri
batchVert
bind
bindRenderTarget
bindTexture
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
setMatrix2fv
setMatrix3fv
setMatrix4fv
setProjectionMatrix
setShader
setShadersFromConfig
setTime
setVertexBuffer
shouldFlush
unbind
updateProjectionMatrix
vertexAvailable
Public Methods ​
batchSprite ​
<instance> batchSprite(gameObject, camera, [parentTransformMatrix]) ​
Description:
Takes a Sprite Game Object, or any object that extends it, and adds it to the batch.
Parameters:
name type optional description
gameObject Phaser.GameObjects.Image | Phaser.GameObjects.Sprite No The texture based Game Object to add to the batch.
camera Phaser.Cameras.Scene2D.Camera No The Camera to use for the rendering transform.
parentTransformMatrix Phaser.GameObjects.Components.TransformMatrix Yes The transform matrix of the parent container, if set.
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#batchSprite
Source: src/renderer/webgl/pipelines/LightPipeline.js#L422
Since: 3.50.0
batchTexture ​
<instance> batchTexture(gameObject, texture, textureWidth, textureHeight, srcX, srcY, srcWidth, srcHeight, scaleX, scaleY, rotation, flipX, flipY, scrollFactorX, scrollFactorY, displayOriginX, displayOriginY, frameX, frameY, frameWidth, frameHeight, tintTL, tintTR, tintBL, tintBR, tintEffect, uOffset, vOffset, camera, parentTransformMatrix, [skipFlip], [textureUnit]) ​
Description:
Generic function for batching a textured quad using argument values instead of a Game Object.
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No Source GameObject.
texture Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper No Texture associated with the quad.
textureWidth number No Real texture width.
textureHeight number No Real texture height.
srcX number No X coordinate of the quad.
srcY number No Y coordinate of the quad.
srcWidth number No Width of the quad.
srcHeight number No Height of the quad.
scaleX number No X component of scale.
scaleY number No Y component of scale.
rotation number No Rotation of the quad.
flipX boolean No Indicates if the quad is horizontally flipped.
flipY boolean No Indicates if the quad is vertically flipped.
scrollFactorX number No By which factor is the quad affected by the camera horizontal scroll.
scrollFactorY number No By which factor is the quad effected by the camera vertical scroll.
displayOriginX number No Horizontal origin in pixels.
displayOriginY number No Vertical origin in pixels.
frameX number No X coordinate of the texture frame.
frameY number No Y coordinate of the texture frame.
frameWidth number No Width of the texture frame.
frameHeight number No Height of the texture frame.
tintTL number No Tint for top left.
tintTR number No Tint for top right.
tintBL number No Tint for bottom left.
tintBR number No Tint for bottom right.
tintEffect number No The tint effect.
uOffset number No Horizontal offset on texture coordinate.
vOffset number No Vertical offset on texture coordinate.
camera Phaser.Cameras.Scene2D.Camera No Current used camera.
parentTransformMatrix Phaser.GameObjects.Components.TransformMatrix No Parent container.
skipFlip boolean Yes false Skip the renderTexture check.
textureUnit number Yes Use the currently bound texture unit?
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#batchTexture
Source: src/renderer/webgl/pipelines/LightPipeline.js#L440
Since: 3.50.0
batchTextureFrame ​
<instance> batchTextureFrame(frame, x, y, tint, alpha, transformMatrix, [parentTransformMatrix]) ​
Description:
Adds a Texture Frame into the batch for rendering.
Parameters:
name type optional description
frame Phaser.Textures.Frame No The Texture Frame to be rendered.
x number No The horizontal position to render the texture at.
y number No The vertical position to render the texture at.
tint number No The tint color.
alpha number No The alpha value.
transformMatrix Phaser.GameObjects.Components.TransformMatrix No The Transform Matrix to use for the texture.
parentTransformMatrix Phaser.GameObjects.Components.TransformMatrix Yes A parent Transform Matrix.
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#batchTextureFrame
Source: src/renderer/webgl/pipelines/LightPipeline.js#L523
Since: 3.50.0
boot ​
<instance> boot() ​
Description:
Called when the Game has fully booted and the Renderer has finished setting up.
By this stage all Game level systems are now in place and you can perform any final
tasks that the pipeline may need that relied on game systems such as the Texture Manager.
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#boot
Source: src/renderer/webgl/pipelines/LightPipeline.js#L138
Since: 3.11.0
getNormalMap ​
<instance> getNormalMap([gameObject]) ​
Description:
Returns the normal map WebGLTextureWrapper from the given Game Object.
If the Game Object doesn't have one, it returns the default normal map from this pipeline instead.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject Yes The Game Object to get the normal map from.
Returns: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper - The normal map texture.
Source: src/renderer/webgl/pipelines/LightPipeline.js#L375
Since: 3.50.0
onRender ​
<instance> onRender(scene, camera) ​
Description:
This function sets all the needed resources for each camera pass.
Parameters:
name type optional description
scene Phaser.Scene No The Scene being rendered.
camera Phaser.Cameras.Scene2D.Camera No The Scene Camera being rendered with.
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#onRender
Source: src/renderer/webgl/pipelines/LightPipeline.js#L152
Since: 3.0.0
setGameObject ​
<instance> setGameObject(gameObject, [frame]) ​
Description:
Custom pipelines can use this method in order to perform any required pre-batch tasks
for the given Game Object. It must return the texture unit the Game Object was assigned.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object being rendered or added to the batch.
frame Phaser.Textures.Frame Yes Optional frame to use. Can override that of the Game Object.
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#setGameObject
Returns: number - The texture unit the Game Object has been assigned.
Source: src/renderer/webgl/pipelines/LightPipeline.js#L307
Since: 3.50.0
setNormalMapRotation ​
<instance> setNormalMapRotation(rotation) ​
Description:
Rotates the normal map vectors inversely by the given angle.
Only works in 2D space.
Parameters:
name type optional description
rotation number No The angle of rotation in radians.
Source: src/renderer/webgl/pipelines/LightPipeline.js#L211
Since: 3.16.0
setTexture2D ​
<instance> setTexture2D([texture], [gameObject]) ​
Description:
Assigns a texture to the current batch. If a different texture is already set it creates a new batch object.
Parameters:
name type optional description
texture Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper Yes Texture that will be assigned to the current batch. If not given uses blankTexture.
gameObject Phaser.GameObjects.GameObject Yes The Game Object being rendered or added to the batch.
Overrides: Phaser.Renderer.WebGL.Pipelines.MultiPipeline#setTexture2D
Source: src/renderer/webgl/pipelines/LightPipeline.js#L253
Since: 3.50.0
Previous
FXPipeline
Next
MobilePipeline
Inherited Members
Public Members
currentNormalMap;
lightsActive
tempVec2
Inherited Methods
Public Methods
batchSprite
batchTexture
batchTextureFrame
boot
getNormalMap
onRender
setGameObject
setNormalMapRotation
setTexture2D
