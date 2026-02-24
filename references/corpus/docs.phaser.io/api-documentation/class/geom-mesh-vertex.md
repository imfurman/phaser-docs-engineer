# Vertex | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/geom-mesh-vertex

Phaser API Documentation
Class
Vertex
Version: Phaser v3.90.0
On this page
Vertex
A Vertex Geometry Object.
This class consists of all the information required for a single vertex within a Face Geometry Object.
Faces, and thus Vertex objects, are used by the Mesh Game Object in order to render objects in WebGL.
Constructor
new Vertex(x, y, z, u, v, [color], [alpha], [nx], [ny], [nz])
Parameters
name type optional default description
x number No The x position of the vertex.
y number No The y position of the vertex.
z number No The z position of the vertex.
u number No The UV u coordinate of the vertex.
v number No The UV v coordinate of the vertex.
color number Yes "0xffffff" The color value of the vertex.
alpha number Yes 1 The alpha value of the vertex.
nx number Yes 0 The x normal value of the vertex.
ny number Yes 0 The y normal value of the vertex.
nz number Yes 0 The z normal value of the vertex.
Scope : static
Extends
Phaser.Math.Vector3
Source: src/geom/mesh/Vertex.js#L11
Since: 3.50.0
Inherited Members ​
From Phaser.Math.Vector3 :
x
y
z
Public Members ​
alpha ​
alpha: number ​
Description:
The alpha value of this vertex.
Source: src/geom/mesh/Vertex.js#L133
Since: 3.50.0
color ​
color: number ​
Description:
The color value of this vertex.
Source: src/geom/mesh/Vertex.js#L124
Since: 3.50.0
nx ​
nx: number ​
Description:
The normalized projected x coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L79
Since: 3.50.0
ny ​
ny: number ​
Description:
The normalized projected y coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L88
Since: 3.50.0
nz ​
nz: number ​
Description:
The normalized projected z coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L97
Since: 3.50.0
ta ​
ta: number ​
Description:
The translated alpha value of this vertex.
Source: src/geom/mesh/Vertex.js#L160
Since: 3.50.0
tu ​
tu: number ​
Description:
The translated uv u coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L169
Since: 3.60.0
tv ​
tv: number ​
Description:
The translated uv v coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L178
Since: 3.60.0
tx ​
tx: number ​
Description:
The translated x coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L142
Since: 3.50.0
ty ​
ty: number ​
Description:
The translated y coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L151
Since: 3.50.0
u ​
u: number ​
Description:
UV u coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L106
Since: 3.50.0
v ​
v: number ​
Description:
UV v coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L115
Since: 3.50.0
vx ​
vx: number ​
Description:
The projected x coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L52
Since: 3.50.0
vy ​
vy: number ​
Description:
The projected y coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L61
Since: 3.50.0
vz ​
vz: number ​
Description:
The projected z coordinate of this vertex.
Source: src/geom/mesh/Vertex.js#L70
Since: 3.50.0
Inherited Methods ​
From Phaser.Math.Vector3 :
add
addScalar
addScale
addVectors
applyMatrix3
applyMatrix4
clone
copy
cross
crossVectors
distance
distanceSq
divide
dot
equals
fromArray
length
lengthSq
lerp
max
min
multiply
negate
normalize
project
projectViewMatrix
reset
scale
set
setFromMatrixColumn
setFromMatrixPosition
subtract
subVectors
transformCoordinates
transformMat3
transformMat4
transformQuat
unproject
unprojectViewMatrix
up
Public Methods ​
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
Returns: number - The new array offset.
Source: src/geom/mesh/Vertex.js#L379
Since: 3.50.0
resize ​
<instance> resize(x, y, width, height, originX, originY) ​
Description:
Resizes this Vertex by setting the x and y coordinates, then transforms this vertex
by an identity matrix and dimensions, storing the results in vx , vy and vz .
Parameters:
name type optional description
x number No The x position of the vertex.
y number No The y position of the vertex.
width number No The width of the parent Mesh.
height number No The height of the parent Mesh.
originX number No The originX of the parent Mesh.
originY number No The originY of the parent Mesh.
Returns: Phaser.Geom.Mesh.Vertex - This Vertex.
Source: src/geom/mesh/Vertex.js#L298
Since: 3.60.0
scaleUV ​
<instance> scaleUV(x, y) ​
Description:
Scales the original UV values by the given amounts.
The original properties Vertex.u and Vertex.v
remain unchanged, only the translated properties
Vertex.tu and Vertex.tv , as used in rendering,
are updated.
Parameters:
name type optional description
x number No The amount to scale the UV u coordinate by.
y number No The amount to scale the UV v coordinate by.
Returns: Phaser.Geom.Mesh.Vertex - This Vertex.
Source: src/geom/mesh/Vertex.js#L237
Since: 3.60.0
scrollUV ​
<instance> scrollUV(x, y) ​
Description:
Translates the original UV positions by the given amounts.
The original properties Vertex.u and Vertex.v
remain unchanged, only the translated properties
Vertex.tu and Vertex.tv , as used in rendering,
are updated.
Parameters:
name type optional description
x number No The amount to scroll the UV u coordinate by.
y number No The amount to scroll the UV v coordinate by.
Returns: Phaser.Geom.Mesh.Vertex - This Vertex.
Source: src/geom/mesh/Vertex.js#L213
Since: 3.60.0
setUVs ​
<instance> setUVs(u, v) ​
Description:
Sets the U and V properties.
Also resets the translated uv properties, undoing any scale
or shift they may have had.
Parameters:
name type optional description
u number No The UV u coordinate of the vertex.
v number No The UV v coordinate of the vertex.
Returns: Phaser.Geom.Mesh.Vertex - This Vertex.
Source: src/geom/mesh/Vertex.js#L188
Since: 3.50.0
transformCoordinatesLocal ​
<instance> transformCoordinatesLocal(transformMatrix, width, height, cameraZ) ​
Description:
Transforms this vertex by the given matrix, storing the results in vx , vy and vz .
Parameters:
name type optional description
transformMatrix Phaser.Math.Matrix4 No The transform matrix to apply to this vertex.
width number No The width of the parent Mesh.
height number No The height of the parent Mesh.
cameraZ number No The z position of the MeshCamera.
Source: src/geom/mesh/Vertex.js#L261
Since: 3.50.0
update ​
<instance> update(a, b, c, d, e, f, roundPixels, alpha) ​
Description:
Updates this Vertex based on the given transform.
Parameters:
name type optional description
a number No The parent transform matrix data a component.
b number No The parent transform matrix data b component.
c number No The parent transform matrix data c component.
d number No The parent transform matrix data d component.
e number No The parent transform matrix data e component.
f number No The parent transform matrix data f component.
roundPixels boolean No Round the vertex position or not?
alpha number No The alpha of the parent object.
Returns: Phaser.Geom.Mesh.Vertex - This Vertex.
Source: src/geom/mesh/Vertex.js#L344
Since: 3.50.0
Previous
Face
Next
Point
Inherited Members
Public Members
alpha
color
nx
ny
nz
ta
tu
tv
tx
ty
u
v
vx
vy
vz
Inherited Methods
Public Methods
load
resize
scaleUV
scrollUV
setUVs
transformCoordinatesLocal
update
