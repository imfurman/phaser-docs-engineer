# Face | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/geom-mesh-face

Phaser API Documentation
Class
Face
Version: Phaser v3.90.0
On this page
Face
A Face Geometry Object.
A Face is used by the Mesh Game Object. A Mesh consists of one, or more, faces that are
used to render the Mesh Game Objects in WebGL.
A Face consists of 3 Vertex instances, for the 3 corners of the face and methods to help
you modify and test them.
Constructor
new Face(vertex1, vertex2, vertex3)
Parameters
name type optional description
vertex1 Phaser.Geom.Mesh.Vertex No The first vertex of the Face.
vertex2 Phaser.Geom.Mesh.Vertex No The second vertex of the Face.
vertex3 Phaser.Geom.Mesh.Vertex No The third vertex of the Face.
Scope : static
Source: src/geom/mesh/Face.js#L33
Since: 3.50.0
Public Members ​
alpha ​
alpha: number ​
Description:
Set the alpha value of this Face.
Each vertex is given the same value. If you need to adjust the alpha on a per-vertex basis
then use the Vertex.alpha property instead.
When getting the alpha of this Face, it will return an average of the alpha
component of all three vertices.
Source: src/geom/mesh/Face.js#L585
Since: 3.50.0
bounds ​
bounds: Phaser.Geom.Rectangle ​
Description:
The bounds of this Face.
Be sure to call the Face.updateBounds method before using this property.
Source: src/geom/mesh/Face.js#L85
Since: 3.50.0
depth ​
depth: number ​
Description:
The depth of this Face, which is an average of the z component of all three vertices.
The depth is calculated based on the transformed z value, not the local one.
Source: src/geom/mesh/Face.js#L618
Since: 3.50.0
vertex1 ​
vertex1: Phaser.Geom.Mesh.Vertex ​
Description:
The first vertex in this Face.
Source: src/geom/mesh/Face.js#L58
Since: 3.50.0
vertex2 ​
vertex2: Phaser.Geom.Mesh.Vertex ​
Description:
The second vertex in this Face.
Source: src/geom/mesh/Face.js#L67
Since: 3.50.0
vertex3 ​
vertex3: Phaser.Geom.Mesh.Vertex ​
Description:
The third vertex in this Face.
Source: src/geom/mesh/Face.js#L76
Since: 3.50.0
x ​
x: number ​
Description:
The x coordinate of this Face, based on the in center position of the Face.
Source: src/geom/mesh/Face.js#L539
Since: 3.50.0
y ​
y: number ​
Description:
The y coordinate of this Face, based on the in center position of the Face.
Source: src/geom/mesh/Face.js#L562
Since: 3.50.0
Public Methods ​
contains ​
<instance> contains(x, y, [calcMatrix]) ​
Description:
Checks if the given coordinates are within this Face.
You can optionally provide a transform matrix. If given, the Face vertices
will be transformed first, before being checked against the coordinates.
Parameters:
name type optional description
x number No The horizontal position to check.
y number No The vertical position to check.
calcMatrix Phaser.GameObjects.Components.TransformMatrix Yes Optional transform matrix to apply to the vertices before comparison.
Returns: boolean - true if the coordinates lay within this Face, otherwise false .
Source: src/geom/mesh/Face.js#L169
Since: 3.50.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Face and nulls the references to the vertices.
Source: src/geom/mesh/Face.js#L641
Since: 3.50.0
getInCenter ​
<instance> getInCenter([local]) ​
Description:
Calculates and returns the in-center position of this Face.
Parameters:
name type optional default description
local boolean Yes true Return the in center from the un-transformed vertex positions ( true ), or transformed? ( false )
Returns: Phaser.Math.Vector2 - A Vector2 containing the in center position of this Face.
Source: src/geom/mesh/Face.js#L107
Since: 3.50.0
isCounterClockwise ​
<instance> isCounterClockwise(z) ​
Description:
Checks if the vertices in this Face are orientated counter-clockwise, or not.
It checks the transformed position of the vertices, not the local one.
Parameters:
name type optional description
z number No The z-axis value to test against. Typically the Mesh.modelPosition.z .
Returns: boolean - true if the vertices in this Face run counter-clockwise, otherwise false .
Source: src/geom/mesh/Face.js#L242
Since: 3.50.0
isInView ​
<instance> isInView(camera, hideCCW, z, alpha, a, b, c, d, e, f, roundPixels) ​
Description:
Checks if this Face is within the view of the given Camera.
This method is called in the MeshWebGLRenderer function. It performs the following tasks:
First, the Vertex.update method is called on each of the vertices. This populates them
with the new translated values, updating their tx , ty and ta properties.
Then it tests to see if this face is visible due to the alpha values, if not, it returns.
After this, if hideCCW is set, it calls isCounterClockwise and returns if not.
Finally, it will update the Face.bounds based on the newly translated vertex values
and return the results of an intersection test between the bounds and the camera world view
rectangle.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The Camera to check against.
hideCCW boolean No Test the counter-clockwise orientation of the verts?
z number No The Cameras z position, used in the CCW test.
alpha number No The alpha of the parent object.
a number No The parent transform matrix data a component.
b number No The parent transform matrix data b component.
c number No The parent transform matrix data c component.
d number No The parent transform matrix data d component.
e number No The parent transform matrix data e component.
f number No The parent transform matrix data f component.
roundPixels boolean No Round the vertex position or not?
Returns: boolean - true if this Face can be seen by the Camera.
Source: src/geom/mesh/Face.js#L336
Since: 3.50.0
load ​
<instance> load(F32, U32, offset, textureUnit, tintEffect) ​
Description:
Loads the data from this Vertex into the given Typed Arrays.
Parameters:
name type optional description
F32 Float32Array No A Float32 Array to insert the position, UV and unit data in to.
U32 Uint32Array No A Uint32 Array to insert the color and alpha data in to.
offset number No The index of the array to insert this Vertex to.
textureUnit number No The texture unit currently in use.
tintEffect number No The tint effect to use.
Returns: number - The new vertex index array offset.
Source: src/geom/mesh/Face.js#L265
Since: 3.50.0
scaleUV ​
<instance> scaleUV(x, y) ​
Description:
Scales the original UV values of each vertex by the given amounts.
The original properties Vertex.u and Vertex.v
remain unchanged, only the translated properties
Vertex.tu and Vertex.tv , as used in rendering,
are updated.
Parameters:
name type optional description
x number No The amount to scale the UV u coordinate by.
y number No The amount to scale the UV v coordinate by.
Returns: Phaser.Geom.Mesh.Face - This Face instance.
Source: src/geom/mesh/Face.js#L433
Since: 3.60.0
scrollUV ​
<instance> scrollUV(x, y) ​
Description:
Translates the original UV positions of each vertex by the given amounts.
The original properties Vertex.u and Vertex.v
remain unchanged, only the translated properties
Vertex.tu and Vertex.tv , as used in rendering,
are updated.
Parameters:
name type optional description
x number No The amount to scroll the UV u coordinate by.
y number No The amount to scroll the UV v coordinate by.
Returns: Phaser.Geom.Mesh.Face - This Face instance.
Source: src/geom/mesh/Face.js#L408
Since: 3.60.0
setColor ​
<instance> setColor(color) ​
Description:
Sets the color value for each Vertex in this Face.
Parameters:
name type optional description
color number No The color value for each vertex.
Returns: Phaser.Geom.Mesh.Face - This Face instance.
Source: src/geom/mesh/Face.js#L458
Since: 3.60.0
transformCoordinatesLocal ​
<instance> transformCoordinatesLocal(transformMatrix, width, height, cameraZ) ​
Description:
Transforms all Face vertices by the given matrix, storing the results in their vx , vy and vz properties.
Parameters:
name type optional description
transformMatrix Phaser.Math.Matrix4 No The transform matrix to apply to this vertex.
width number No The width of the parent Mesh.
height number No The height of the parent Mesh.
cameraZ number No The z position of the MeshCamera.
Returns: Phaser.Geom.Mesh.Face - This Face instance.
Source: src/geom/mesh/Face.js#L288
Since: 3.50.0
translate ​
<instance> translate(x, [y]) ​
Description:
Translates the vertices of this Face by the given amounts.
The actual vertex positions are adjusted, not their transformed position.
Therefore, this updates the vertex data directly.
Parameters:
name type optional default description
x number No The amount to horizontally translate by.
y number Yes 0 The amount to vertically translate by.
Returns: Phaser.Geom.Mesh.Face - This Face instance.
Source: src/geom/mesh/Face.js#L504
Since: 3.50.0
update ​
<instance> update(alpha, a, b, c, d, e, f, roundPixels) ​
Description:
Calls the Vertex.update method on each of the vertices. This populates them
with the new translated values, updating their tx , ty and ta properties.
Parameters:
name type optional description
alpha number No The alpha of the parent object.
a number No The parent transform matrix data a component.
b number No The parent transform matrix data b component.
c number No The parent transform matrix data c component.
d number No The parent transform matrix data d component.
e number No The parent transform matrix data e component.
f number No The parent transform matrix data f component.
roundPixels boolean No Round the vertex position or not?
Returns: Phaser.Geom.Mesh.Face - This Face instance.
Source: src/geom/mesh/Face.js#L477
Since: 3.60.0
updateBounds ​
<instance> updateBounds() ​
Description:
Updates the bounds of this Face, based on the translated values of the vertices.
Call this method prior to accessing the Face.bounds property.
Returns: Phaser.Geom.Mesh.Face - This Face instance.
Source: src/geom/mesh/Face.js#L310
Since: 3.50.0
Previous
Line
Next
Vertex
Public Members
alpha
bounds
depth
vertex1
vertex2
vertex3
x
y
Public Methods
contains
destroy
getInCenter
isCounterClockwise
isInView
load
scaleUV
scrollUV
setColor
transformCoordinatesLocal
translate
update
updateBounds
