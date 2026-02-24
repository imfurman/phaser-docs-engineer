# MultiPipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-pipelines-multipipeline

Phaser API Documentation
Class
MultiPipeline
Version: Phaser v3.90.0
On this page
MultiPipeline
The Multi Pipeline is the core 2D texture rendering pipeline used by Phaser in WebGL.
Virtually all Game Objects use this pipeline by default, including Sprites, Graphics
and Tilemaps. It handles the batching of quads and tris, as well as methods for
drawing and batching geometry data.
Prior to Phaser v3.50 this pipeline was called the TextureTintPipeline .
In previous versions of Phaser only one single texture unit was supported at any one time.
The Multi Pipeline is an evolution of the old Texture Tint Pipeline, updated to support
multi-textures for increased performance.
The fragment shader it uses can be found in shaders/src/Multi.frag .
The vertex shader it uses can be found in shaders/src/Multi.vert .
The default shader attributes for this pipeline are:
inPosition (vec2, offset 0)
inTexCoord (vec2, offset 8)
inTexId (float, offset 16)
inTintEffect (float, offset 20)
inTint (vec4, offset 24, normalized)
The default shader uniforms for this pipeline are:
uProjectionMatrix (mat4)
uResolution (vec2)
uMainSampler (sampler2D, or sampler2D array)
If you wish to create a custom pipeline extending from this one, you can use two string
declarations in your fragment shader source: %count% and %forloop% , where count is
used to set the number of sampler2Ds available, and forloop is a block of GLSL code
that will get the currently bound texture unit.
This pipeline will automatically inject that code for you, should those values exist
in your shader source. If you wish to handle this yourself, you can also use the
function Utils.parseFragmentShaderMaxTextures .
The following fragment shader shows how to use the two variables:
#define SHADER_NAME PHASER_MULTI_FS
#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif
uniform sampler2D uMainSampler[%count%];
varying vec2 outTexCoord;
varying float outTexId;
varying float outTintEffect;
varying vec4 outTint;
void main ()
{
vec4 texture;
%forloop%
vec4 texel = vec4(outTint.bgr * outTint.a, outTint.a);
// Multiply texture tint
vec4 color = texture * texel;
if (outTintEffect == 1.0)
{
// Solid color + texture alpha
color.rgb = mix(texture.rgb, outTint.bgr * outTint.a, texture.a);
}
else if (outTintEffect == 2.0)
{
// Solid color, no texture
color = texel;
}
gl_FragColor = color;
}
If you wish to create a pipeline that works from a single texture, or that doesn't have
internal texture iteration, please see the SinglePipeline instead. If you wish to create
a special effect, especially one that can impact the pixels around a texture (i.e. such as
a glitch effect) then you should use the PreFX and PostFX Pipelines for this task.
Constructor
new MultiPipeline(config)
Parameters
name type optional description
config Phaser.Types.Renderer.WebGL.WebGLPipelineConfig No The configuration options for this pipeline.
Scope : static
Extends
Phaser.Renderer.WebGL.WebGLPipeline
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L18
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
Public Members ​
calcMatrix ​
calcMatrix: Phaser.GameObjects.Components.TransformMatrix ​
Description:
A temporary Transform Matrix, re-used internally during batching by the
Shape Game Objects.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L184
Since: 3.55.0
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
batchFillPath ​
<instance> batchFillPath(path, currentMatrix, parentMatrix) ​
Description:
Adds the given path to the vertex batch for rendering.
It works by taking the array of path data and then passing it through Earcut, which
creates a list of polygons. Each polygon is then added to the batch.
The path is always automatically closed because it's filled.
Parameters:
name type optional description
path Array.< Phaser.Types.Math.Vector2Like > No Collection of points that represent the path.
currentMatrix Phaser.GameObjects.Components.TransformMatrix No The current transform.
parentMatrix Phaser.GameObjects.Components.TransformMatrix No The parent transform.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L772
Since: 3.55.0
batchFillRect ​
<instance> batchFillRect(x, y, width, height, currentMatrix, parentMatrix) ​
Description:
Pushes a filled rectangle into the vertex batch.
Rectangle factors in the given transform matrices before adding to the batch.
Parameters:
name type optional description
x number No Horizontal top left coordinate of the rectangle.
y number No Vertical top left coordinate of the rectangle.
width number No Width of the rectangle.
height number No Height of the rectangle.
currentMatrix Phaser.GameObjects.Components.TransformMatrix No The current transform.
parentMatrix Phaser.GameObjects.Components.TransformMatrix No The parent transform.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L652
Since: 3.55.0
batchFillTriangle ​
<instance> batchFillTriangle(x0, y0, x1, y1, x2, y2, currentMatrix, parentMatrix) ​
Description:
Pushes a filled triangle into the vertex batch.
Triangle factors in the given transform matrices before adding to the batch.
Parameters:
name type optional description
x0 number No Point 0 x coordinate.
y0 number No Point 0 y coordinate.
x1 number No Point 1 x coordinate.
y1 number No Point 1 y coordinate.
x2 number No Point 2 x coordinate.
y2 number No Point 2 y coordinate.
currentMatrix Phaser.GameObjects.Components.TransformMatrix No The current transform.
parentMatrix Phaser.GameObjects.Components.TransformMatrix No The parent transform.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L686
Since: 3.55.0
batchLine ​
<instance> batchLine(ax, ay, bx, by, aLineWidth, bLineWidth, index, closePath, currentMatrix, parentMatrix) ​
Description:
Creates a line out of 4 quads and adds it to the vertex batch based on the given line values.
Parameters:
name type optional description
ax number No x coordinate of the start of the line.
ay number No y coordinate of the start of the line.
bx number No x coordinate of the end of the line.
by number No y coordinate of the end of the line.
aLineWidth number No Width of the start of the line.
bLineWidth number No Width of the end of the line.
index number No If this line is part of a multi-line draw, the index of the line in the draw.
closePath boolean No Does this line close a multi-line path?
currentMatrix Phaser.GameObjects.Components.TransformMatrix No The current transform.
parentMatrix Phaser.GameObjects.Components.TransformMatrix No The parent transform.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L893
Since: 3.55.0
batchSprite ​
<instance> batchSprite(gameObject, camera, [parentTransformMatrix]) ​
Description:
Takes a Sprite Game Object, or any object that extends it, and adds it to the batch.
Parameters:
name type optional description
gameObject Phaser.GameObjects.Image | Phaser.GameObjects.Sprite No The texture based Game Object to add to the batch.
camera Phaser.Cameras.Scene2D.Camera No The Camera to use for the rendering transform.
parentTransformMatrix Phaser.GameObjects.Components.TransformMatrix Yes The transform matrix of the parent container, if set.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L288
Since: 3.0.0
batchStrokePath ​
<instance> batchStrokePath(path, lineWidth, pathOpen, currentMatrix, parentMatrix) ​
Description:
Adds the given path to the vertex batch for rendering.
It works by taking the array of path data and calling batchLine for each section
of the path.
The path is optionally closed at the end.
Parameters:
name type optional description
path Array.< Phaser.Types.Math.Vector2Like > No Collection of points that represent the path.
lineWidth number No The width of the line segments in pixels.
pathOpen boolean No Indicates if the path should be closed or left open.
currentMatrix Phaser.GameObjects.Components.TransformMatrix No The current transform.
parentMatrix Phaser.GameObjects.Components.TransformMatrix No The parent transform.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L845
Since: 3.55.0
batchStrokeTriangle ​
<instance> batchStrokeTriangle(x0, y0, x1, y1, x2, y2, lineWidth, currentMatrix, parentMatrix) ​
Description:
Pushes a stroked triangle into the vertex batch.
Triangle factors in the given transform matrices before adding to the batch.
The triangle is created from 3 lines and drawn using the batchStrokePath method.
Parameters:
name type optional description
x0 number No Point 0 x coordinate.
y0 number No Point 0 y coordinate.
x1 number No Point 1 x coordinate.
y1 number No Point 1 y coordinate.
x2 number No Point 2 x coordinate.
y2 number No Point 2 y coordinate.
lineWidth number No The width of the line in pixels.
currentMatrix Phaser.GameObjects.Components.TransformMatrix No The current transform.
parentMatrix Phaser.GameObjects.Components.TransformMatrix No The parent transform.
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L729
Since: 3.55.0
batchTexture ​
<instance> batchTexture(gameObject, texture, textureWidth, textureHeight, srcX, srcY, srcWidth, srcHeight, scaleX, scaleY, rotation, flipX, flipY, scrollFactorX, scrollFactorY, displayOriginX, displayOriginY, frameX, frameY, frameWidth, frameHeight, tintTL, tintTR, tintBL, tintBR, tintEffect, uOffset, vOffset, camera, parentTransformMatrix, [skipFlip], [textureUnit], [skipPrePost]) ​
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
textureUnit number Yes The texture unit to set (defaults to currently bound if undefined or null)
skipPrePost boolean Yes false Skip the pre and post manager calls?
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L427
Since: 3.0.0
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
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L607
Since: 3.12.0
boot ​
<instance> boot() ​
Description:
Called every time the pipeline is bound by the renderer.
Sets the shader program, vertex buffer and other resources.
Should only be called when changing pipeline.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#boot
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L270
Since: 3.50.0
destroy ​
<instance> destroy() ​
Description:
Destroys all shader instances, removes all object references and nulls all external references.
Overrides: Phaser.Renderer.WebGL.WebGLPipeline#destroy
Returns: Phaser.Renderer.WebGL.Pipelines.MultiPipeline - This WebGLPipeline instance.
Fires: Phaser.Renderer.WebGL.Pipelines.Events#event:DESTROY
Source: src/renderer/webgl/pipelines/MultiPipeline.js#L1012
Since: 3.60.0
Previous
MobilePipeline
Next
PointLightPipeline
Inherited Members
Public Members
calcMatrix
Inherited Methods
Public Methods
batchFillPath
batchFillRect
batchFillTriangle
batchLine
batchSprite
batchStrokePath
batchStrokeTriangle
batchTexture
batchTextureFrame
boot
destroy
