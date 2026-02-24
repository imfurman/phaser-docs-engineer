# Types.Geom.Mesh | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/types-geom-mesh

Phaser API Documentation
Typedefs
Types.Geom.Mesh
Version: Phaser v3.90.0
On this page
Types.Geom.Mesh
GenerateGridConfig ​
<static> GenerateGridConfig ​
name type optional default description
texture string | Phaser.Textures.Texture No The texture to be used for this Grid. Must be a Texture instance. Can also be a string but only if the mesh property is set.
frame string | number Yes The name or index of the frame within the Texture.
mesh Phaser.GameObjects.Mesh Yes If specified, the vertices of the generated grid will be added to this Mesh Game Object.
width number Yes 1 The width of the grid in 3D units. If you wish to get a pixel accurate grid based on a texture, you can use an Ortho Mesh or the isOrtho parameter.
height number Yes "width" The height of the grid in 3D units.
widthSegments number Yes 1 The number of segments to split the grid horizontally in to.
heightSegments number Yes "widthSegments" The number of segments to split the grid vertically in to.
x number Yes 0 Offset the grid x position by this amount.
y number Yes 0 Offset the grid y position by this amount.
colors number | Array.<number> Yes "0xffffff" An array of colors, one per vertex, or a single color value applied to all vertices.
alphas number | Array.<number> Yes 1 An array of alpha values, one per vertex, or a single alpha value applied to all vertices.
tile boolean Yes false Should the texture tile (repeat) across the grid segments, or display as a single texture?
isOrtho boolean Yes false If set and using a texture with an ortho Mesh, the width and height parameters will be calculated based on the frame size for you.
flipY boolean Yes false If set and using a texture, vertically flipping render result.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/GenerateGridConfig.js#L1
Since: 3.50.0
GenerateGridVertsResult ​
<static> GenerateGridVertsResult ​
name type optional default description
verts Array.<number> No An array of vertex values in x, y pairs.
indices Array.<number> No An array of vertex indexes. This array will be empty if the tile parameter was true .
uvs Array.<number> No An array of UV values, two per vertex.
colors number | Array.<number> Yes "0xffffff" An array of colors, one per vertex, or a single color value applied to all vertices.
alphas number | Array.<number> Yes 1 An array of alpha values, one per vertex, or a single alpha value applied to all vertices.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/GenerateGridVertsResult.js#L1
Since: 3.50.0
GenerateVertsResult ​
<static> GenerateVertsResult ​
name type optional description
faces Array.< Phaser.Geom.Mesh.Face > No An array of Face objects generated from the OBJ Data.
vertices Array.< Phaser.Geom.Mesh.Vertex > No An array of Vertex objects generated from the OBJ Data.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/GenerateVertsResult.js#L1
Since: 3.50.0
OBJData ​
<static> OBJData ​
name type optional description
materialLibraries Array.<string> No An array of material library filenames found in the OBJ file.
materials object No If the obj was loaded with an mtl file, the parsed material names are stored in this object.
models Array.< Phaser.Types.Geom.Mesh.OBJModel > No An array of parsed models extracted from the OBJ file.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/OBJData.js#L1
Since: 3.50.0
OBJFace ​
<static> OBJFace ​
name type optional description
group string No The name of the Group this Face is in.
material string No The name of the material this Face uses.
vertices Array.< Phaser.Types.Geom.Mesh.OBJFaceVertice > No An array of vertices in this Face.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/OBJFace.js#L1
Since: 3.50.0
OBJFaceVertice ​
<static> OBJFaceVertice ​
name type optional description
textureCoordsIndex number No The index in the textureCoords array that this vertex uses.
vertexIndex number No The index in the vertices array that this vertex uses.
vertexNormalIndex number No The index in the vertexNormals array that this vertex uses.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/OBJFaceVertice.js#L1
Since: 3.50.0
OBJModel ​
<static> OBJModel ​
name type optional description
faces Array.< Phaser.Types.Geom.Mesh.OBJFace > No An array of Faces.
name string No The name of the model.
textureCoords Array.< Phaser.Types.Geom.Mesh.UV > No An array of texture coordinates.
vertexNormals Array.< Phaser.Types.Math.Vector3Like > No An array of vertex normals.
vertices Array.< Phaser.Types.Math.Vector3Like > No An array of vertices in the model.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/OBJModel.js#L1
Since: 3.50.0
UV ​
<static> UV ​
name type optional description
u number No The u component.
v number No The v component.
w number No The w component.
Type : object
Member of : Phaser.Types.Geom.Mesh
Source: src/geom/mesh/typedefs/UV.js#L1
Since: 3.50.0
Previous
Types.GameObjects
Next
Types.Input.Gamepad
GenerateGridConfig
<static> GenerateGridConfig
GenerateGridVertsResult
<static> GenerateGridVertsResult
GenerateVertsResult
<static> GenerateVertsResult
OBJData
<static> OBJData
OBJFace
<static> OBJFace
OBJFaceVertice
<static> OBJFaceVertice
OBJModel
<static> OBJModel
UV
<static> UV
