# Mesh | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-mesh

Phaser API Documentation
Class
Mesh
Version: Phaser v3.90.0
On this page
Mesh
A Mesh Game Object.
The Mesh Game Object allows you to render a group of textured vertices and manipulate
the view of those vertices, such as rotation, translation or scaling.
Support for generating mesh data from grids, model data or Wavefront OBJ Files is included.
Although you can use this to render 3D objects, its primary use is for displaying more complex
Sprites, or Sprites where you need fine-grained control over the vertex positions in order to
achieve special effects in your games. Note that rendering still takes place using Phaser's
orthographic camera (after being transformed via projectionMesh , see setPerspective ,
setOrtho , and panZ methods). As a result, all depth and face tests are done in an eventually
orthographic space.
The rendering process will iterate through the faces of this Mesh and render out each face
that is considered as being in view of the camera. No depth buffer is used, and because of this,
you should be careful not to use model data with too many vertices, or overlapping geometry,
or you'll probably encounter z-depth fighting. The Mesh was designed to allow for more advanced
2D layouts, rather than displaying 3D objects, even though it can do this to a degree.
In short, if you want to remake Crysis, use a 3D engine, not a Mesh. However, if you want
to easily add some small fun 3D elements into your game, or create some special effects involving
vertex warping, this is the right object for you. Mesh data becomes part of the WebGL batch,
just like standard Sprites, so doesn't introduce any additional shader overhead. Because
the Mesh just generates vertices into the WebGL batch, like any other Sprite, you can use all of
the common Game Object components on a Mesh too, such as a custom pipeline, mask, blend mode
or texture.
Note that the Mesh object is WebGL only and does not have a Canvas counterpart.
The Mesh origin is always 0.5 x 0.5 and cannot be changed.
Constructor
new Mesh(scene, [x], [y], [texture], [frame], [vertices], [uvs], [indicies], [containsZ], [normals], [colors], [alphas])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes The horizontal position of this Game Object in the world.
y number Yes The vertical position of this Game Object in the world.
texture string | Phaser.Textures.Texture Yes The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
vertices Array.<number> Yes The vertices array. Either xy pairs, or xyz if the containsZ parameter is true (but see note).
uvs Array.<number> Yes The UVs pairs array.
indicies Array.<number> Yes Optional vertex indicies array. If you don't have one, pass null or an empty array.
containsZ boolean Yes false Does the vertices data include a z component? Note: If not, it will be assumed z=0 , see method panZ or setOrtho .
normals Array.<number> Yes Optional vertex normals array. If you don't have one, pass null or an empty array.
colors number | Array.<number> Yes "0xffffff" An array of colors, one per vertex, or a single color value applied to all vertices.
alphas number | Array.<number> Yes 1 An array of alpha values, one per vertex, or a single alpha value applied to all vertices.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Size
Phaser.GameObjects.Components.Texture
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/mesh/Mesh.js#L22
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Pipeline :
defaultPipeline
pipeline
pipelineData
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
From Phaser.GameObjects.Components.Size :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.Texture :
frame
texture
From Phaser.GameObjects.Components.Transform :
angle
hasTransformComponent
rotation
scale
scaleX
scaleY
w
x
y
z
From Phaser.GameObjects.Components.Visible :
visible
From Phaser.GameObjects.GameObject :
active
body
cameraFilter
data
displayList
ignoreDestroy
input
name
parentContainer
renderFlags
scene
state
tabIndex
type
Public Members ​
debugCallback ​
debugCallback: function ​
Description:
You can optionally choose to render the vertices of this Mesh to a Graphics instance.
Achieve this by setting the debugCallback and the debugGraphic properties.
You can do this in a single call via the Mesh.setDebug method, which will use the
built-in debug function. You can also set it to your own callback. The callback
will be invoked once per render and sent the following parameters:
debugCallback(src, meshLength, verts)
src is the Mesh instance being debugged.
meshLength is the number of mesh vertices in total.
verts is an array of the translated vertex coordinates.
To disable rendering, set this property back to null .
Please note that high vertex count Meshes will struggle to debug properly.
Source: src/gameobjects/mesh/Mesh.js#L154
Since: 3.50.0
debugGraphic ​
debugGraphic: Phaser.GameObjects.Graphics ​
Description:
The Graphics instance that the debug vertices will be drawn to, if setDebug has
been called.
Source: src/gameobjects/mesh/Mesh.js#L179
Since: 3.50.0
faces ​
faces: Array.< Phaser.Geom.Mesh.Face > ​
Description:
An array containing the Face instances belonging to this Mesh.
A Face consists of 3 Vertex objects.
This array is populated during calls such as addVertices or addOBJ .
Source: src/gameobjects/mesh/Mesh.js#L117
Since: 3.50.0
fov ​
fov: number ​
Description:
The Camera fov (field of view) in degrees.
This is set automatically as part of the Mesh.setPerspective call, but exposed
here for additional math.
Do not modify this property directly, doing so will not change the fov. For that,
call the respective Mesh methods.
Source: src/gameobjects/mesh/Mesh.js#L351
Since: 3.60.0
hideCCW ​
hideCCW: boolean ​
Description:
When rendering, skip any Face that isn't counter clockwise?
Enable this to hide backward-facing Faces during rendering.
Disable it to render all Faces.
Source: src/gameobjects/mesh/Mesh.js#L189
Since: 3.50.0
ignoreDirtyCache ​
ignoreDirtyCache: boolean ​
Description:
By default, the Mesh will check to see if its model or view transform has
changed each frame and only recalculate the vertex positions if they have.
This avoids lots of additional math in the preUpdate step when not required.
However, if you are performing per-Face or per-Vertex manipulation on this Mesh,
such as tweening a Face, or moving it without moving the rest of the Mesh,
then you may need to disable the dirty cache in order for the Mesh to re-render
correctly. You can toggle this property to do that. Please note that leaving
this set to true will cause the Mesh to recalculate the position of every single
vertex in it, every single frame. So only really do this if you know you
need it.
Source: src/gameobjects/mesh/Mesh.js#L331
Since: 3.50.0
modelPosition ​
modelPosition: Phaser.Math.Vector3 ​
Description:
A Vector3 containing the 3D position of the vertices in this Mesh.
Modifying the components of this property will allow you to reposition where
the vertices are rendered within the Mesh. This happens in the preUpdate phase,
where each vertex is transformed using the view and projection matrices.
Changing this property will impact all vertices being rendered by this Mesh.
You can also adjust the 'view' by using the pan methods.
Source: src/gameobjects/mesh/Mesh.js#L202
Since: 3.50.0
modelRotation ​
modelRotation: Phaser.Math.Vector3 ​
Description:
A Vector3 containing the 3D rotation of the vertices in this Mesh.
The values should be given in radians, i.e. to rotate the vertices by 90
degrees you can use modelRotation.x = Phaser.Math.DegToRad(90) .
Modifying the components of this property will allow you to rotate
the vertices within the Mesh. This happens in the preUpdate phase,
where each vertex is transformed using the view and projection matrices.
Changing this property will impact all vertices being rendered by this Mesh.
Source: src/gameobjects/mesh/Mesh.js#L234
Since: 3.50.0
modelScale ​
modelScale: Phaser.Math.Vector3 ​
Description:
A Vector3 containing the 3D scale of the vertices in this Mesh.
Modifying the components of this property will allow you to scale
the vertices within the Mesh. This happens in the preUpdate phase,
where each vertex is transformed using the view and projection matrices.
Changing this property will impact all vertices being rendered by this Mesh.
Source: src/gameobjects/mesh/Mesh.js#L219
Since: 3.50.0
projectionMatrix ​
projectionMatrix: Phaser.Math.Matrix4 ​
Description:
The projection matrix for this Mesh.
Update it with the setPerspective or setOrtho methods.
Source: src/gameobjects/mesh/Mesh.js#L294
Since: 3.50.0
tintFill ​
tintFill: boolean ​
Description:
The tint fill mode.
false = An additive tint (the default), where vertices colors are blended with the texture.
true = A fill tint, where the vertex colors replace the texture, but respects texture alpha.
Source: src/gameobjects/mesh/Mesh.js#L141
Since: 3.50.0
totalRendered ​
totalRendered: number ​
Description:
How many faces were rendered by this Mesh Game Object in the last
draw? This is reset in the preUpdate method and then incremented
each time a face is drawn. Note that in multi-camera Scenes this
value may exceed that found in Mesh.getFaceCount due to
cameras drawing the same faces more than once.
Source: src/gameobjects/mesh/Mesh.js#L305
Since: 3.50.0
transformMatrix ​
transformMatrix: Phaser.Math.Matrix4 ​
Description:
The transformation matrix for this Mesh.
Source: src/gameobjects/mesh/Mesh.js#L265
Since: 3.50.0
vertices ​
vertices: Array.< Phaser.Geom.Mesh.Vertex > ​
Description:
An array containing Vertex instances. One instance per vertex in this Mesh.
This array is populated during calls such as addVertex or addOBJ .
Source: src/gameobjects/mesh/Mesh.js#L130
Since: 3.50.0
viewMatrix ​
viewMatrix: Phaser.Math.Matrix4 ​
Description:
The view matrix for this Mesh.
Source: src/gameobjects/mesh/Mesh.js#L285
Since: 3.50.0
viewPosition ​
viewPosition: Phaser.Math.Vector3 ​
Description:
The view position for this Mesh.
Use the methods panX , panY and panZ to adjust the view.
Source: src/gameobjects/mesh/Mesh.js#L274
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
From Phaser.GameObjects.Components.AlphaSingle :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.Pipeline :
getPipelineName
initPipeline
resetPipeline
setPipeline
setPipelineData
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
From Phaser.GameObjects.Components.Size :
setDisplaySize
setSize
setSizeToFrame
From Phaser.GameObjects.Components.Texture :
setFrame
setTexture
From Phaser.GameObjects.Components.Transform :
copyPosition
getLocalPoint
getLocalTransformMatrix
getParentRotation
getWorldPoint
getWorldTransformMatrix
setAngle
setPosition
setRandomPosition
setRotation
setScale
setW
setX
setY
setZ
From Phaser.GameObjects.Components.Visible :
setVisible
From Phaser.GameObjects.GameObject :
addedToScene
addToDisplayList
addToUpdateList
destroy
disableInteractive
getData
getDisplayList
getIndexList
incData
removedFromScene
removeFromDisplayList
removeFromUpdateList
removeInteractive
setActive
setData
setDataEnabled
setName
setState
toggleData
toJSON
update
willRender
Public Methods ​
addFace ​
<instance> addFace(vertex1, vertex2, vertex3) ​
Description:
Adds a new Face into the faces array of this Mesh.
A Face consists of references to 3 Vertex instances, which must be provided.
Parameters:
name type optional description
vertex1 Phaser.Geom.Mesh.Vertex No The first vertex of the Face.
vertex2 Phaser.Geom.Mesh.Vertex No The second vertex of the Face.
vertex3 Phaser.Geom.Mesh.Vertex No The third vertex of the Face.
Returns: Phaser.GameObjects.Mesh - This Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L660
Since: 3.50.0
addVertex ​
<instance> addVertex(x, y, z, u, v, [color], [alpha]) ​
Description:
Adds a new Vertex into the vertices array of this Mesh.
Just adding a vertex isn't enough to render it. You need to also
make it part of a Face, with 3 Vertex instances per Face.
Parameters:
name type optional default description
x number No The x position of the vertex.
y number No The y position of the vertex.
z number No The z position of the vertex.
u number No The UV u coordinate of the vertex.
v number No The UV v coordinate of the vertex.
color number Yes "0xffffff" The color value of the vertex.
alpha number Yes 1 The alpha value of the vertex.
Returns: Phaser.GameObjects.Mesh - This Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L632
Since: 3.50.0
addVertices ​
<instance> addVertices(vertices, uvs, [indicies], [containsZ], [normals], [colors], [alphas]) ​
Description:
Adds new vertices to this Mesh by parsing the given data.
This method will take vertex data in one of two formats, based on the containsZ parameter.
If your vertex data are x , y pairs, then containsZ should be false (this is the default, and will result in z=0 for each vertex).
If your vertex data is groups of x , y and z values, then the containsZ parameter must be true.
The uvs parameter is a numeric array consisting of u and v pairs.
The normals parameter is a numeric array consisting of x , y vertex normal values and, if containsZ is true, z values as well.
The indicies parameter is an optional array that, if given, is an indexed list of vertices to be added.
The colors parameter is an optional array, or single value, that if given sets the color of each vertex created.
The alphas parameter is an optional array, or single value, that if given sets the alpha of each vertex created.
When providing indexed data it is assumed that all of the arrays are indexed, not just the vertices.
The following example will create a 256 x 256 sized quad using an index array:
let mesh = new Mesh ( this ) ; // Assuming `this` is a scene!
const vertices = [
- 128 , 128 ,
128 , 128 ,
- 128 , - 128 ,
128 , - 128
] ;
const uvs = [
0 , 1 ,
1 , 1 ,
0 , 0 ,
1 , 0
] ;
const indices = [ 0 , 2 , 1 , 2 , 3 , 1 ] ;
mesh . addVertices ( vertices , uvs , indicies ) ;
// Note: Otherwise the added points will be "behind" the camera! This value will project vertex `x` & `y` values 1:1 to pixel values.
mesh . hideCCW = false ;
mesh . setOrtho ( mesh . width , mesh . height ) ;
If the data is not indexed, it's assumed that the arrays all contain sequential data.
Parameters:
name type optional default description
vertices Array.<number> No The vertices array. Either xy pairs, or xyz if the containsZ parameter is true .
uvs Array.<number> No The UVs pairs array.
indicies Array.<number> Yes Optional vertex indicies array. If you don't have one, pass null or an empty array.
containsZ boolean Yes false Does the vertices data include a z component? If not, it will be assumed z=0 , see methods panZ or setOrtho .
normals Array.<number> Yes Optional vertex normals array. If you don't have one, pass null or an empty array.
colors number | Array.<number> Yes "0xffffff" An array of colors, one per vertex, or a single color value applied to all vertices.
alphas number | Array.<number> Yes 1 An array of alpha values, one per vertex, or a single alpha value applied to all vertices.
Returns: Phaser.GameObjects.Mesh - This Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L685
Since: 3.50.0
addVerticesFromObj ​
<instance> addVerticesFromObj(key, [scale], [x], [y], [z], [rotateX], [rotateY], [rotateZ], [zIsUp]) ​
Description:
This method will add the data from a triangulated Wavefront OBJ model file to this Mesh.
The data should have been loaded via the OBJFile:
this . load . obj ( key , url ) ;
Then use the same key as the first parameter to this method.
Multiple Mesh Game Objects can use the same model data without impacting on each other.
Make sure your 3D package has triangulated the model data prior to exporting it.
You can add multiple models to a single Mesh, although they will act as one when
moved or rotated. You can scale the model data, should it be too small, or too large, to see.
You can also offset the vertices of the model via the x , y and z parameters.
Parameters:
name type optional default description
key string No The key of the model data in the OBJ Cache to add to this Mesh.
scale number Yes 1 An amount to scale the model data by. Use this if the model has exported too small, or large, to see.
x number Yes 0 Translate the model x position by this amount.
y number Yes 0 Translate the model y position by this amount.
z number Yes 0 Translate the model z position by this amount.
rotateX number Yes 0 Rotate the model on the x axis by this amount, in radians.
rotateY number Yes 0 Rotate the model on the y axis by this amount, in radians.
rotateZ number Yes 0 Rotate the model on the z axis by this amount, in radians.
zIsUp boolean Yes true Is the z axis up (true), or is y axis up (false)?
Returns: Phaser.GameObjects.Mesh - This Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L546
Since: 3.50.0
clear ​
<instance> clear() ​
Description:
Iterates and destroys all current Faces in this Mesh, then resets the
faces and vertices arrays.
Returns: Phaser.GameObjects.Mesh - This Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L524
Since: 3.50.0
clearTint ​
<instance> clearTint() ​
Description:
Clears all tint values associated with this Game Object.
Immediately sets the color values back to 0xffffff on all vertices,
which results in no visible change to the texture.
Tags:
webglOnly
Returns: Phaser.GameObjects.Mesh - This Game Object instance.
Source: src/gameobjects/mesh/Mesh.js#L1136
Since: 3.60.0
depthSort ​
<instance> depthSort() ​
Description:
Runs a depth sort across all Faces in this Mesh, comparing their averaged depth.
This is called automatically if you use any of the rotate methods, but you can
also invoke it to sort the Faces should you manually position them.
Returns: Phaser.GameObjects.Mesh - This Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L614
Since: 3.50.0
getFace ​
<instance> getFace(index) ​
Description:
Returns the Face at the given index in this Mesh Game Object.
Parameters:
name type optional description
index number No The index of the Face to get.
Returns: Phaser.Geom.Mesh.Face - The Face at the given index, or undefined if index out of range.
Source: src/gameobjects/mesh/Mesh.js#L792
Since: 3.50.0
getFaceAt ​
<instance> getFaceAt(x, y, [camera]) ​
Description:
Return an array of Face objects from this Mesh that intersect with the given coordinates.
The given position is translated through the matrix of this Mesh and the given Camera,
before being compared against the vertices.
If more than one Face intersects, they will all be returned in the array, but the array will
be depth sorted first, so the first element will always be that closest to the camera.
Parameters:
name type optional description
x number No The x position to check against.
y number No The y position to check against.
camera Phaser.Cameras.Scene2D.Camera Yes The camera to pass the coordinates through. If not give, the default Scene Camera is used.
Returns: Array.< Phaser.Geom.Mesh.Face > - An array of Face objects that intersect with the given point, ordered by depth.
Source: src/gameobjects/mesh/Mesh.js#L843
Since: 3.50.0
getFaceCount ​
<instance> getFaceCount() ​
Description:
Returns the total number of Faces in this Mesh Game Object.
Returns: number - The number of Faces in this Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L766
Since: 3.50.0
getVertexCount ​
<instance> getVertexCount() ​
Description:
Returns the total number of Vertices in this Mesh Game Object.
Returns: number - The number of Vertices in this Mesh Game Object.
Source: src/gameobjects/mesh/Mesh.js#L779
Since: 3.50.0
hasFaceAt ​
<instance> hasFaceAt(x, y, [camera]) ​
Description:
Tests to see if any face in this Mesh intersects with the given coordinates.
The given position is translated through the matrix of this Mesh and the given Camera,
before being compared against the vertices.
Parameters:
name type optional description
x number No The x position to check against.
y number No The y position to check against.
camera Phaser.Cameras.Scene2D.Camera Yes The camera to pass the coordinates through. If not give, the default Scene Camera is used.
Returns: boolean - Returns true if any face of this Mesh intersects with the given coordinate, otherwise false .
Source: src/gameobjects/mesh/Mesh.js#L807
Since: 3.60.0
isDirty ​
<instance> isDirty() ​
Description:
Checks if the transformation data in this mesh is dirty.
This is used internally by the preUpdate step to determine if the vertices should
be recalculated or not.
Returns: boolean - Returns true if the data of this mesh is dirty, otherwise false .
Source: src/gameobjects/mesh/Mesh.js#L949
Since: 3.50.0
panX ​
<instance> panX(v) ​
Description:
Translates the view position of this Mesh on the x axis by the given amount.
Parameters:
name type optional description
v number No The amount to pan by.
Source: src/gameobjects/mesh/Mesh.js#L399
Since: 3.50.0
panY ​
<instance> panY(v) ​
Description:
Translates the view position of this Mesh on the y axis by the given amount.
Parameters:
name type optional description
v number No The amount to pan by.
Source: src/gameobjects/mesh/Mesh.js#L416
Since: 3.50.0
panZ ​
<instance> panZ(v) ​
Description:
Translates the view position of this Mesh on the z axis by the given amount.
As the default panZ value is 0, vertices with z=0 (the default) need special
care or else they will not display as they are "behind" the camera.
Consider using mesh.panZ(mesh.height / (2 * Math.tan(Math.PI / 16))) ,
which will interpret vertex geometry 1:1 with pixel geometry (or see setOrtho ).
Parameters:
name type optional description
v number No The amount to pan by.
Source: src/gameobjects/mesh/Mesh.js#L433
Since: 3.50.0
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
The Mesh update loop. The following takes place in this method:
First, the totalRendered and totalFrame properties are set.
If the view matrix of this Mesh isn't dirty, and the model position, rotate or scale properties are
all clean, then the method returns at this point.
Otherwise, if the viewPosition is dirty (i.e. from calling a method like panZ ), then it will
refresh the viewMatrix.
After this, a new transformMatrix is built and it then iterates through all Faces in this
Mesh, calling transformCoordinatesLocal on all of them. Internally, this updates every
vertex, calculating its new transformed position, based on the new transform matrix.
Finally, the faces are depth sorted.
Access: protected
Parameters:
name type optional description
time number No The current timestamp.
delta number No The delta time, in ms, elapsed since the last frame.
Source: src/gameobjects/mesh/Mesh.js#L1017
Since: 3.50.0
renderDebug ​
<instance> renderDebug(src, faces) ​
Description:
The built-in Mesh debug rendering method.
See Mesh.setDebug for more details.
Parameters:
name type optional description
src Phaser.GameObjects.Mesh No The Mesh object being rendered.
faces Array.< Phaser.Geom.Mesh.Face > No An array of Faces.
Source: src/gameobjects/mesh/Mesh.js#L1091
Since: 3.50.0
rotateX ​
<instance> rotateX() ​
Description:
The x rotation of the Model in 3D space, as specified in degrees.
If you need the value in radians use the modelRotation.x property directly.
Returns: number - undefined
Source: src/gameobjects/mesh/Mesh.js#L1324
Since: 3.60.0
rotateY ​
<instance> rotateY() ​
Description:
The y rotation of the Model in 3D space, as specified in degrees.
If you need the value in radians use the modelRotation.y property directly.
Returns: number - undefined
Source: src/gameobjects/mesh/Mesh.js#L1347
Since: 3.60.0
rotateZ ​
<instance> rotateZ() ​
Description:
The z rotation of the Model in 3D space, as specified in degrees.
If you need the value in radians use the modelRotation.z property directly.
Returns: number - undefined
Source: src/gameobjects/mesh/Mesh.js#L1370
Since: 3.60.0
setDebug ​
<instance> setDebug([graphic], [callback]) ​
Description:
This method enables rendering of the Mesh vertices to the given Graphics instance.
If you enable this feature, you must call Graphics.clear() in your Scene update ,
otherwise the Graphics instance you provide to debug will fill-up with draw calls,
eventually crashing the browser. This is not done automatically to allow you to debug
draw multiple Mesh objects to a single Graphics instance.
The Mesh class has a built-in debug rendering callback Mesh.renderDebug , however
you can also provide your own callback to be used instead. Do this by setting the callback parameter.
The callback is invoked once per render and sent the following parameters:
callback(src, faces)
src is the Mesh instance being debugged.
faces is an array of the Faces that were rendered.
You can get the final drawn vertex position from a Face object like this:
let face = faces [ i ] ;
let x0 = face . vertex1 . tx ;
let y0 = face . vertex1 . ty ;
let x1 = face . vertex2 . tx ;
let y1 = face . vertex2 . ty ;
let x2 = face . vertex3 . tx ;
let y2 = face . vertex3 . ty ;
graphic . strokeTriangle ( x0 , y0 , x1 , y1 , x2 , y2 ) ;
If using your own callback you do not have to provide a Graphics instance to this method.
To disable debug rendering, to either your own callback or the built-in one, call this method
with no arguments.
Parameters:
name type optional description
graphic Phaser.GameObjects.Graphics Yes The Graphic instance to render to if using the built-in callback.
callback function Yes The callback to invoke during debug render. Leave as undefined to use the built-in callback.
Returns: Phaser.GameObjects.Mesh - This Game Object instance.
Source: src/gameobjects/mesh/Mesh.js#L883
Since: 3.50.0
setInteractive ​
<instance> setInteractive([config]) ​
Description:
Pass this Mesh Game Object to the Input Manager to enable it for Input.
Unlike other Game Objects, the Mesh Game Object uses its own special hit area callback, which you cannot override.
Parameters:
name type optional description
config Phaser.Types.Input.InputConfiguration Yes An input configuration object but it will ignore hitArea, hitAreaCallback and pixelPerfect with associated alphaTolerance properties.
Overrides: Phaser.GameObjects.GameObject#setInteractive
Returns: Phaser.GameObjects.Mesh - This GameObject.
Source: src/gameobjects/mesh/Mesh.js#L1153
Since: 3.60.0
setOrtho ​
<instance> setOrtho([scaleX], [scaleY], [near], [far]) ​
Description:
Builds a new orthographic projection matrix from the given values.
If using this mode you will often need to set Mesh.hideCCW to false as well.
By default, calling this method with no parameters will set the scaleX value to
match the renderer's aspect ratio. If you would like to render vertex positions 1:1
to pixel positions, consider calling as mesh.setOrtho(mesh.width, mesh.height) .
See also setPerspective .
Parameters:
name type optional default description
scaleX number Yes 1 The default horizontal scale in relation to the Mesh / Renderer dimensions.
scaleY number Yes 1 The default vertical scale in relation to the Mesh / Renderer dimensions.
near number Yes -1000 The near value of the view.
far number Yes 1000 The far value of the view.
Source: src/gameobjects/mesh/Mesh.js#L488
Since: 3.50.0
setPerspective ​
<instance> setPerspective(width, height, [fov], [near], [far]) ​
Description:
Builds a new perspective projection matrix from the given values.
These are also the initial projection matrix and parameters for Mesh (see Mesh.panZ for more discussion).
See also setOrtho .
Parameters:
name type optional default description
width number No The width of the projection matrix. Typically the same as the Mesh and/or Renderer.
height number No The height of the projection matrix. Typically the same as the Mesh and/or Renderer.
fov number Yes 45 The field of view, in degrees.
near number Yes 0.01 The near value of the view.
far number Yes 1000 The far value of the view.
Source: src/gameobjects/mesh/Mesh.js#L456
Since: 3.50.0
setTint ​
<instance> setTint([tint]) ​
Description:
Sets an additive tint on all vertices of this Mesh Game Object.
The tint works by taking the pixel color values from the Game Objects texture, and then
multiplying it by the color value of the tint.
To modify the tint color once set, either call this method again with new values or use the
tint property to set all colors at once.
To remove a tint call clearTint .
Tags:
webglOnly
Parameters:
name type optional default description
tint number Yes "0xffffff" The tint being applied to all vertices of this Mesh Game Object.
Returns: Phaser.GameObjects.Mesh - This Game Object instance.
Source: src/gameobjects/mesh/Mesh.js#L1198
Since: 3.60.0
sortByDepth ​
<instance> sortByDepth(faceA, faceB) ​
Description:
Compare the depth of two Faces.
Parameters:
name type optional description
faceA Phaser.Geom.Mesh.Face No The first Face.
faceB Phaser.Geom.Mesh.Face No The second Face.
Returns: number - The difference between the depths of each Face.
Source: src/gameobjects/mesh/Mesh.js#L598
Since: 3.50.0
tint ​
<instance> tint() ​
Description:
The tint value being applied to the whole of the Game Object.
This property is a setter-only.
Tags:
webglOnly
Returns: number - undefined
Source: src/gameobjects/mesh/Mesh.js#L1307
Since: 3.60.0
uvScale ​
<instance> uvScale(x, y) ​
Description:
Scales the UV texture coordinates of all faces in this Mesh by
the exact given amounts.
If you only wish to scale one coordinate, pass a value of one
to the other.
Due to a limitation in WebGL1 you can only UV scale textures
that are a power-of-two in size. Scaling NPOT textures will
work but will result in clamping the pixels to the edges if
you scale beyond a value of 1. Scaling below 1 will work
regardless of texture size.
Note that if this Mesh is using a frame from a texture atlas
then you will be unable to UV scale its texture.
Tags:
webglOnly
Parameters:
name type optional description
x number No The amount to horizontally scale the UV coordinates by.
y number No The amount to vertically scale the UV coordinates by.
Returns: Phaser.GameObjects.Mesh - This Game Object instance.
Source: src/gameobjects/mesh/Mesh.js#L1270
Since: 3.60.0
uvScroll ​
<instance> uvScroll(x, y) ​
Description:
Scrolls the UV texture coordinates of all faces in this Mesh by
adding the given x/y amounts to them.
If you only wish to scroll one coordinate, pass a value of zero
to the other.
Use small values for scrolling. UVs are set from the range 0
to 1, so you should increment (or decrement) them by suitably
small values, such as 0.01.
Due to a limitation in WebGL1 you can only UV scroll textures
that are a power-of-two in size. Scrolling NPOT textures will
work but will result in clamping the pixels to the edges.
Note that if this Mesh is using a frame from a texture atlas
then you will be unable to UV scroll its texture.
Tags:
webglOnly
Parameters:
name type optional description
x number No The amount to horizontally shift the UV coordinates by.
y number No The amount to vertically shift the UV coordinates by.
Returns: Phaser.GameObjects.Mesh - This Game Object instance.
Source: src/gameobjects/mesh/Mesh.js#L1231
Since: 3.60.0
Previous
Line
Next
NineSlice
Inherited Members
Public Members
debugCallback
debugGraphic
faces
fov
hideCCW
ignoreDirtyCache
modelPosition
modelRotation
modelScale
projectionMatrix
tintFill
totalRendered
transformMatrix
vertices
viewMatrix
viewPosition
Inherited Methods
Public Methods
addFace
addVertex
addVertices
addVerticesFromObj
clear
clearTint
depthSort
getFace
getFaceAt
getFaceCount
getVertexCount
hasFaceAt
isDirty
panX
panY
panZ
preUpdate
renderDebug
rotateX
rotateY
rotateZ
setDebug
setInteractive
setOrtho
setPerspective
setTint
sortByDepth
tint
uvScale
uvScroll
