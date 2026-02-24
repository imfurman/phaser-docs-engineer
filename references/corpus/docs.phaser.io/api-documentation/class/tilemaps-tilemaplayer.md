# TilemapLayer | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tilemaps-tilemaplayer

Phaser API Documentation
Class
TilemapLayer
Version: Phaser v3.90.0
On this page
TilemapLayer
A Tilemap Layer is a Game Object that renders LayerData from a Tilemap when used in combination
with one, or more, Tilesets.
Do not add TilemapLayers to Containers, they are stand-alone display objects.
Constructor
new TilemapLayer(scene, tilemap, layerIndex, tileset, [x], [y])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs.
tilemap Phaser.Tilemaps.Tilemap No The Tilemap this layer is a part of.
layerIndex number No The index of the LayerData associated with this layer.
tileset string | Array.<string> Phaser.Tilemaps.Tileset Array.< Phaser.Tilemaps.Tileset > No
x number Yes 0 The world x position where the top left of this layer will be placed.
y number Yes 0 The world y position where the top left of this layer will be placed.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Alpha
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.ComputedSize
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Flip
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Phaser.Physics.Arcade.Components.Collision
Source: src/tilemaps/TilemapLayer.js#L15
Since: 3.50.0
Inherited Members ​
From Phaser.GameObjects.Components.Alpha :
alpha
alphaBottomLeft
alphaBottomRight
alphaTopLeft
alphaTopRight
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.ComputedSize :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Flip :
flipX
flipY
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
collisionCategory ​
collisionCategory: number ​
Description:
The Tilemap Layer Collision Category.
This is exclusively used by the Arcade Physics system.
This can be set to any valid collision bitfield value.
See the setCollisionCategory method for more details.
Source: src/tilemaps/TilemapLayer.js#L264
Since: 3.70.0
collisionMask ​
collisionMask: number ​
Description:
The Tilemap Layer Collision Mask.
This is exclusively used by the Arcade Physics system.
See the setCollidesWith method for more details.
Source: src/tilemaps/TilemapLayer.js#L279
Since: 3.70.0
cullCallback ​
cullCallback: function ​
Description:
The callback that is invoked when the tiles are culled.
It will call a different function based on the map orientation:
Orthogonal (the default) is TilemapComponents.CullTiles
Isometric is TilemapComponents.IsometricCullTiles
Hexagonal is TilemapComponents.HexagonalCullTiles
Staggered is TilemapComponents.StaggeredCullTiles
However, you can override this to call any function you like.
It will be sent 4 arguments:
The Phaser.Tilemaps.LayerData object for this Layer
The Camera that is culling the layer. You can check its dirty property to see if it has changed since the last cull.
A reference to the culledTiles array, which should be used to store the tiles you want rendered.
The Render Order constant.
See the TilemapComponents.CullTiles source code for details on implementing your own culling system.
Source: src/tilemaps/TilemapLayer.js#L195
Since: 3.50.0
culledTiles ​
culledTiles: Array.< Phaser.Tilemaps.Tile > ​
Description:
Used internally during rendering. This holds the tiles that are visible within the Camera.
Source: src/tilemaps/TilemapLayer.js#L148
Since: 3.50.0
cullPaddingX ​
cullPaddingX: number ​
Description:
The amount of extra tiles to add into the cull rectangle when calculating its horizontal size.
See the method setCullPadding for more details.
Source: src/tilemaps/TilemapLayer.js#L171
Since: 3.50.0
cullPaddingY ​
cullPaddingY: number ​
Description:
The amount of extra tiles to add into the cull rectangle when calculating its vertical size.
See the method setCullPadding for more details.
Source: src/tilemaps/TilemapLayer.js#L183
Since: 3.50.0
displayOriginX ​
displayOriginX: number ​
Description:
The horizontal display origin of this Tilemap Layer.
Overrides: Phaser.GameObjects.Components.Origin#displayOriginX
Source: src/tilemaps/TilemapLayer.js#L312
Since: 3.0.0
displayOriginY ​
displayOriginY: number ​
Description:
The vertical display origin of this Tilemap Layer.
Overrides: Phaser.GameObjects.Components.Origin#displayOriginY
Source: src/tilemaps/TilemapLayer.js#L322
Since: 3.0.0
gidMap ​
gidMap: Array.< Phaser.Tilemaps.Tileset > ​
Description:
An array holding the mapping between the tile indexes and the tileset they belong to.
Source: src/tilemaps/TilemapLayer.js#L245
Since: 3.50.0
isTilemap ​
isTilemap: boolean ​
Description:
Used internally by physics system to perform fast type checks.
Source: src/tilemaps/TilemapLayer.js#L78
Since: 3.50.0
layer ​
layer: Phaser.Tilemaps.LayerData ​
Description:
The LayerData associated with this layer. LayerData can only be associated with one
tilemap layer.
Source: src/tilemaps/TilemapLayer.js#L106
Since: 3.50.0
layerIndex ​
layerIndex: number ​
Description:
The index of the LayerData associated with this layer.
Source: src/tilemaps/TilemapLayer.js#L97
Since: 3.50.0
originX ​
originX: number ​
Description:
The horizontal origin of this Tilemap Layer.
Overrides: Phaser.GameObjects.Components.Origin#originX
Source: src/tilemaps/TilemapLayer.js#L292
Since: 3.0.0
originY ​
originY: number ​
Description:
The vertical origin of this Tilemap Layer.
Overrides: Phaser.GameObjects.Components.Origin#originY
Source: src/tilemaps/TilemapLayer.js#L302
Since: 3.0.0
skipCull ​
skipCull: boolean ​
Description:
You can control if the camera should cull tiles on this layer before rendering them or not.
By default the camera will try to cull the tiles in this layer, to avoid over-drawing to the renderer.
However, there are some instances when you may wish to disable this, and toggling this flag allows
you to do so. Also see setSkipCull for a chainable method that does the same thing.
Source: src/tilemaps/TilemapLayer.js#L157
Since: 3.50.0
tilemap ​
tilemap: Phaser.Tilemaps.Tilemap ​
Description:
The Tilemap that this layer is a part of.
Source: src/tilemaps/TilemapLayer.js#L88
Since: 3.50.0
tilesDrawn ​
tilesDrawn: number ​
Description:
The total number of tiles drawn by the renderer in the last frame.
Source: src/tilemaps/TilemapLayer.js#L128
Since: 3.50.0
tileset ​
tileset: Array.< Phaser.Tilemaps.Tileset > ​
Description:
An array of Tileset objects associated with this layer.
Source: src/tilemaps/TilemapLayer.js#L119
Since: 3.50.0
tilesTotal ​
tilesTotal: number ​
Description:
The total number of tiles in this layer. Updated every frame.
Source: src/tilemaps/TilemapLayer.js#L138
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
From Phaser.GameObjects.Components.Alpha :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.ComputedSize :
setDisplaySize
setSize
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Flip :
resetFlip
setFlip
setFlipX
setFlipY
toggleFlipX
toggleFlipY
From Phaser.GameObjects.Components.GetBounds :
getBottomCenter
getBottomLeft
getBottomRight
getBounds
getCenter
getLeftCenter
getRightCenter
getTopCenter
getTopLeft
getTopRight
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
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
setInteractive
setName
setState
toggleData
toJSON
update
willRender
From Phaser.Physics.Arcade.Components.Collision :
addCollidesWith
removeCollidesWith
resetCollisionCategory
setCollidesWith
setCollisionCategory
willCollideWith
Public Methods ​
calculateFacesAt ​
<instance> calculateFacesAt(tileX, tileY) ​
Description:
Calculates interesting faces at the given tile coordinates of the specified layer. Interesting
faces are used internally for optimizing collisions against tiles. This method is mostly used
internally to optimize recalculating faces when only one tile has been changed.
Parameters:
name type optional description
tileX number No The x coordinate.
tileY number No The y coordinate.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L430
Since: 3.50.0
calculateFacesWithin ​
<instance> calculateFacesWithin([tileX], [tileY], [width], [height]) ​
Description:
Calculates interesting faces within the rectangular area specified (in tile coordinates) of the
layer. Interesting faces are used internally for optimizing collisions against tiles. This method
is mostly used internally.
Parameters:
name type optional description
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L450
Since: 3.50.0
copy ​
<instance> copy(srcTileX, srcTileY, width, height, destTileX, destTileY, [recalculateFaces]) ​
Description:
Copies the tiles in the source rectangular area to a new destination (all specified in tile
coordinates) within the layer. This copies all tile properties & recalculates collision
information in the destination region.
Parameters:
name type optional default description
srcTileX number No The x coordinate of the area to copy from, in tiles, not pixels.
srcTileY number No The y coordinate of the area to copy from, in tiles, not pixels.
width number No The width of the area to copy, in tiles, not pixels.
height number No The height of the area to copy, in tiles, not pixels.
destTileX number No The x coordinate of the area to copy to, in tiles, not pixels.
destTileY number No The y coordinate of the area to copy to, in tiles, not pixels.
recalculateFaces boolean Yes true true if the faces data should be recalculated.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L513
Since: 3.50.0
createFromTiles ​
<instance> createFromTiles(indexes, replacements, [spriteConfig], [scene], [camera]) ​
Description:
Creates a Sprite for every object matching the given tile indexes in the layer. You can
optionally specify if each tile will be replaced with a new tile after the Sprite has been
created. This is useful if you want to lay down special tiles in a level that are converted to
Sprites, but want to replace the tile itself with a floor tile or similar once converted.
Parameters:
name type optional description
indexes number | array No The tile index, or array of indexes, to create Sprites from.
replacements number | array No The tile index, or array of indexes, to change a converted tile to. Set to null to leave the tiles unchanged. If an array is given, it is assumed to be a one-to-one mapping with the indexes array.
spriteConfig Phaser.Types.GameObjects.Sprite.SpriteConfig Yes The config object to pass into the Sprite creator (i.e. scene.make.sprite).
scene Phaser.Scene Yes The Scene to create the Sprites within.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when determining the world XY
Returns: Array.< Phaser.GameObjects.Sprite > - An array of the Sprites that were created.
Source: src/tilemaps/TilemapLayer.js#L472
Since: 3.50.0
cull ​
<instance> cull([camera]) ​
Description:
Returns the tiles in the given layer that are within the cameras viewport.
This is used internally during rendering.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to run the cull check against.
Returns: Array.< Phaser.Tilemaps.Tile > - An array of Tile objects to render.
Source: src/tilemaps/TilemapLayer.js#L497
Since: 3.50.0
destroy ​
<instance> destroy([removeFromTilemap]) ​
Description:
Destroys this TilemapLayer and removes its link to the associated LayerData.
Parameters:
name type optional default description
removeFromTilemap boolean Yes true Remove this layer from the parent Tilemap?
Overrides: Phaser.GameObjects.GameObject#destroy
Source: src/tilemaps/TilemapLayer.js#L1491
Since: 3.50.0
fill ​
<instance> fill(index, [tileX], [tileY], [width], [height], [recalculateFaces]) ​
Description:
Sets the tiles in the given rectangular area (in tile coordinates) of the layer with the
specified index. Tiles will be set to collide if the given index is a colliding index.
Collision information in the region will be recalculated.
Parameters:
name type optional default description
index number No The tile index to fill the area with.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
recalculateFaces boolean Yes true true if the faces data should be recalculated.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L538
Since: 3.50.0
filterTiles ​
<instance> filterTiles(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions]) ​
Description:
For each tile in the given rectangular area (in tile coordinates) of the layer, run the given
filter callback function. Any tiles that pass the filter test (i.e. where the callback returns
true) will returned as a new array. Similar to Array.prototype.Filter in vanilla JS.
Parameters:
name type optional description
callback function No The callback. Each tile in the given area will be passed to this callback as the first and only parameter. The callback should return true for tiles that pass the filter.
context object Yes The context under which the callback should be run.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area to filter.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area to filter.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
Returns: Array.< Phaser.Tilemaps.Tile > - An array of Tile objects.
Source: src/tilemaps/TilemapLayer.js#L562
Since: 3.50.0
findByIndex ​
<instance> findByIndex(index, [skip], [reverse]) ​
Description:
Searches the entire map layer for the first tile matching the given index, then returns that Tile
object. If no match is found, it returns null. The search starts from the top-left tile and
continues horizontally until it hits the end of the row, then it drops down to the next column.
If the reverse boolean is true, it scans starting from the bottom-right corner traveling up to
the top-left.
Parameters:
name type optional default description
index number No The tile index value to search for.
skip number Yes 0 The number of times to skip a matching tile before returning.
reverse boolean Yes false If true it will scan the layer in reverse, starting at the bottom-right. Otherwise it scans from the top-left.
Returns: Phaser.Tilemaps.Tile - The first matching Tile object.
Source: src/tilemaps/TilemapLayer.js#L587
Since: 3.50.0
findTile ​
<instance> findTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions]) ​
Description:
Find the first tile in the given rectangular area (in tile coordinates) of the layer that
satisfies the provided testing function. I.e. finds the first tile for which callback returns
true. Similar to Array.prototype.find in vanilla JS.
Parameters:
name type optional description
callback FindTileCallback No The callback. Each tile in the given area will be passed to this callback as the first and only parameter.
context object Yes The context under which the callback should be run.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area to search.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area to search.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
Returns: Phaser.Tilemaps.Tile - The first Tile found at the given location.
Source: src/tilemaps/TilemapLayer.js#L608
Since: 3.50.0
forEachTile ​
<instance> forEachTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions]) ​
Description:
For each tile in the given rectangular area (in tile coordinates) of the layer, run the given
callback. Similar to Array.prototype.forEach in vanilla JS.
Parameters:
name type optional description
callback EachTileCallback No The callback. Each tile in the given area will be passed to this callback as the first and only parameter.
context object Yes The context, or scope, under which the callback should be run.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area to search.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area to search.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L631
Since: 3.50.0
getIsoTileAtWorldXY ​
<instance> getIsoTileAtWorldXY(worldX, worldY, [originTop], [nonNull], [camera]) ​
Description:
Gets a tile at the given world coordinates from the given isometric layer.
Parameters:
name type optional default description
worldX number No X position to get the tile from (given in pixels)
worldY number No Y position to get the tile from (given in pixels)
originTop boolean Yes true Which is the active face of the isometric tile? The top (default, true), or the base? (false)
nonNull boolean Yes false For empty tiles, return a Tile object with an index of -1 instead of null.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: Phaser.Tilemaps.Tile - The tile at the given coordinates or null if no tile was found or the coordinates were invalid.
Source: src/tilemaps/TilemapLayer.js#L766
Since: 3.60.0
getTileAt ​
<instance> getTileAt(tileX, tileY, [nonNull]) ​
Description:
Gets a tile at the given tile coordinates from the given layer.
Parameters:
name type optional default description
tileX number No X position to get the tile from (given in tile units, not pixels).
tileY number No Y position to get the tile from (given in tile units, not pixels).
nonNull boolean Yes false For empty tiles, return a Tile object with an index of -1 instead of null.
Returns: Phaser.Tilemaps.Tile - The Tile at the given coordinates or null if no tile was found or the coordinates were invalid.
Source: src/tilemaps/TilemapLayer.js#L731
Since: 3.50.0
getTileAtWorldXY ​
<instance> getTileAtWorldXY(worldX, worldY, [nonNull], [camera]) ​
Description:
Gets a tile at the given world coordinates from the given layer.
Parameters:
name type optional default description
worldX number No X position to get the tile from (given in pixels)
worldY number No Y position to get the tile from (given in pixels)
nonNull boolean Yes false For empty tiles, return a Tile object with an index of -1 instead of null.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: Phaser.Tilemaps.Tile - The tile at the given coordinates or null if no tile was found or the coordinates were invalid.
Source: src/tilemaps/TilemapLayer.js#L748
Since: 3.50.0
getTileCorners ​
<instance> getTileCorners(tileX, tileY, [camera]) ​
Description:
Returns an array of Vector2s where each entry corresponds to the corner of the requested tile.
The tileX and tileY parameters are in tile coordinates, not world coordinates.
The corner coordinates are in world space, having factored in TilemapLayer scale, position
and the camera, if given.
The size of the array will vary based on the orientation of the map. For example an
orthographic map will return an array of 4 vectors, where-as a hexagonal map will,
of course, return an array of 6 corner vectors.
Parameters:
name type optional description
tileX number No The x coordinate, in tiles, not pixels.
tileY number No The y coordinate, in tiles, not pixels.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: Array.< Phaser.Math.Vector2 > - Returns an array of Vector2s, or null if the layer given was invalid.
Source: src/tilemaps/TilemapLayer.js#L1367
Since: 3.60.0
getTilesWithin ​
<instance> getTilesWithin([tileX], [tileY], [width], [height], [filteringOptions]) ​
Description:
Gets the tiles in the given rectangular area (in tile coordinates) of the layer.
Parameters:
name type optional description
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
Returns: Array.< Phaser.Tilemaps.Tile > - An array of Tile objects found within the area.
Source: src/tilemaps/TilemapLayer.js#L791
Since: 3.50.0
getTilesWithinShape ​
<instance> getTilesWithinShape(shape, [filteringOptions], [camera]) ​
Description:
Gets the tiles that overlap with the given shape in the given layer. The shape must be a Circle,
Line, Rectangle or Triangle. The shape should be in world coordinates.
Parameters:
name type optional description
shape Phaser.Geom.Circle | Phaser.Geom.Line Phaser.Geom.Rectangle Phaser.Geom.Triangle
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when factoring in which tiles to return.
Returns: Array.< Phaser.Tilemaps.Tile > - An array of Tile objects found within the shape.
Source: src/tilemaps/TilemapLayer.js#L810
Since: 3.50.0
getTilesWithinWorldXY ​
<instance> getTilesWithinWorldXY(worldX, worldY, width, height, [filteringOptions], [camera]) ​
Description:
Gets the tiles in the given rectangular area (in world coordinates) of the layer.
Parameters:
name type optional description
worldX number No The world x coordinate for the top-left of the area.
worldY number No The world y coordinate for the top-left of the area.
width number No The width of the area.
height number No The height of the area.
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when factoring in which tiles to return.
Returns: Array.< Phaser.Tilemaps.Tile > - An array of Tile objects found within the area.
Source: src/tilemaps/TilemapLayer.js#L828
Since: 3.50.0
hasTileAt ​
<instance> hasTileAt(tileX, tileY) ​
Description:
Checks if there is a tile at the given location (in tile coordinates) in the given layer. Returns
false if there is no tile or if the tile at that location has an index of -1.
Parameters:
name type optional description
tileX number No The x coordinate, in tiles, not pixels.
tileY number No The y coordinate, in tiles, not pixels.
Returns: boolean - true if a tile was found at the given location, otherwise false .
Source: src/tilemaps/TilemapLayer.js#L848
Since: 3.50.0
hasTileAtWorldXY ​
<instance> hasTileAtWorldXY(worldX, worldY, [camera]) ​
Description:
Checks if there is a tile at the given location (in world coordinates) in the given layer. Returns
false if there is no tile or if the tile at that location has an index of -1.
Parameters:
name type optional description
worldX number No The x coordinate, in pixels.
worldY number No The y coordinate, in pixels.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when factoring in which tiles to return.
Returns: boolean - true if a tile was found at the given location, otherwise false .
Source: src/tilemaps/TilemapLayer.js#L865
Since: 3.50.0
putTileAt ​
<instance> putTileAt(tile, tileX, tileY, [recalculateFaces]) ​
Description:
Puts a tile at the given tile coordinates in the specified layer. You can pass in either an index
or a Tile object. If you pass in a Tile, all attributes will be copied over to the specified
location. If you pass in an index, only the index at the specified location will be changed.
Collision information will be recalculated at the specified location.
Parameters:
name type optional default description
tile number | Phaser.Tilemaps.Tile No The index of this tile to set or a Tile object.
tileX number No The x coordinate, in tiles, not pixels.
tileY number No The y coordinate, in tiles, not pixels.
recalculateFaces boolean Yes true true if the faces data should be recalculated.
Returns: Phaser.Tilemaps.Tile - The Tile object that was inserted at the given coordinates.
Source: src/tilemaps/TilemapLayer.js#L883
Since: 3.50.0
putTileAtWorldXY ​
<instance> putTileAtWorldXY(tile, worldX, worldY, [recalculateFaces], [camera]) ​
Description:
Puts a tile at the given world coordinates (pixels) in the specified layer. You can pass in either
an index or a Tile object. If you pass in a Tile, all attributes will be copied over to the
specified location. If you pass in an index, only the index at the specified location will be
changed. Collision information will be recalculated at the specified location.
Parameters:
name type optional description
tile number | Phaser.Tilemaps.Tile No The index of this tile to set or a Tile object.
worldX number No The x coordinate, in pixels.
worldY number No The y coordinate, in pixels.
recalculateFaces boolean Yes true if the faces data should be recalculated.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: Phaser.Tilemaps.Tile - The Tile object that was inserted at the given coordinates.
Source: src/tilemaps/TilemapLayer.js#L904
Since: 3.50.0
putTilesAt ​
<instance> putTilesAt(tile, tileX, tileY, [recalculateFaces]) ​
Description:
Puts an array of tiles or a 2D array of tiles at the given tile coordinates in the specified
layer. The array can be composed of either tile indexes or Tile objects. If you pass in a Tile,
all attributes will be copied over to the specified location. If you pass in an index, only the
index at the specified location will be changed. Collision information will be recalculated
within the region tiles were changed.
Parameters:
name type optional default description
tile Array.<number> | Array.<Array.<number>> Array.< Phaser.Tilemaps.Tile > Array.<Array.< Phaser.Tilemaps.Tile >> No
tileX number No The x coordinate, in tiles, not pixels.
tileY number No The y coordinate, in tiles, not pixels.
recalculateFaces boolean Yes true true if the faces data should be recalculated.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L926
Since: 3.50.0
randomize ​
<instance> randomize([tileX], [tileY], [width], [height], [indexes]) ​
Description:
Randomizes the indexes of a rectangular region of tiles (in tile coordinates) within the
specified layer. Each tile will receive a new index. If an array of indexes is passed in, then
those will be used for randomly assigning new tile indexes. If an array is not provided, the
indexes found within the region (excluding -1) will be used for randomly assigning new tile
indexes. This method only modifies tile indexes and does not change collision information.
Parameters:
name type optional description
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
indexes Array.<number> Yes An array of indexes to randomly draw from during randomization.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L950
Since: 3.50.0
removeTileAt ​
<instance> removeTileAt(tileX, tileY, [replaceWithNull], [recalculateFaces]) ​
Description:
Removes the tile at the given tile coordinates in the specified layer and updates the layers
collision information.
Parameters:
name type optional default description
tileX number No The x coordinate, in tiles, not pixels.
tileY number No The y coordinate, in tiles, not pixels.
replaceWithNull boolean Yes true If true, this will replace the tile at the specified location with null instead of a Tile with an index of -1.
recalculateFaces boolean Yes true true if the faces data should be recalculated.
Returns: Phaser.Tilemaps.Tile - A Tile object.
Source: src/tilemaps/TilemapLayer.js#L975
Since: 3.50.0
removeTileAtWorldXY ​
<instance> removeTileAtWorldXY(worldX, worldY, [replaceWithNull], [recalculateFaces], [camera]) ​
Description:
Removes the tile at the given world coordinates in the specified layer and updates the layers
collision information.
Parameters:
name type optional default description
worldX number No The x coordinate, in pixels.
worldY number No The y coordinate, in pixels.
replaceWithNull boolean Yes true If true, this will replace the tile at the specified location with null instead of a Tile with an index of -1.
recalculateFaces boolean Yes true true if the faces data should be recalculated.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: Phaser.Tilemaps.Tile - The Tile object that was removed from the given location.
Source: src/tilemaps/TilemapLayer.js#L994
Since: 3.50.0
renderDebug ​
<instance> renderDebug(graphics, [styleConfig]) ​
Description:
Draws a debug representation of the layer to the given Graphics. This is helpful when you want to
get a quick idea of which of your tiles are colliding and which have interesting faces. The tiles
are drawn starting at (0, 0) in the Graphics, allowing you to place the debug representation
wherever you want on the screen.
Parameters:
name type optional description
graphics Phaser.GameObjects.Graphics No The target Graphics object to draw upon.
styleConfig Phaser.Types.Tilemaps.StyleConfig Yes An object specifying the colors to use for the debug drawing.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1014
Since: 3.50.0
replaceByIndex ​
<instance> replaceByIndex(findIndex, newIndex, [tileX], [tileY], [width], [height]) ​
Description:
Scans the given rectangular area (given in tile coordinates) for tiles with an index matching
findIndex and updates their index to match newIndex . This only modifies the index and does
not change collision information.
Parameters:
name type optional description
findIndex number No The index of the tile to search for.
newIndex number No The index of the tile to replace it with.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1035
Since: 3.50.0
setCollision ​
<instance> setCollision(indexes, [collides], [recalculateFaces], [updateLayer]) ​
Description:
Sets collision on the given tile or tiles within a layer by index. You can pass in either a
single numeric index or an array of indexes: [2, 3, 15, 20]. The collides parameter controls if
collision will be enabled (true) or disabled (false).
Parameters:
name type optional default description
indexes number | array No Either a single tile index, or an array of tile indexes.
collides boolean Yes true If true it will enable collision. If false it will clear collision.
recalculateFaces boolean Yes true Whether or not to recalculate the tile faces after the update.
updateLayer boolean Yes true If true, updates the current tiles on the layer. Set to false if no tiles have been placed for significant performance boost.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1108
Since: 3.50.0
setCollisionBetween ​
<instance> setCollisionBetween(start, stop, [collides], [recalculateFaces]) ​
Description:
Sets collision on a range of tiles in a layer whose index is between the specified start and
stop (inclusive). Calling this with a start value of 10 and a stop value of 14 would set
collision for tiles 10, 11, 12, 13 and 14. The collides parameter controls if collision will be
enabled (true) or disabled (false).
Parameters:
name type optional default description
start number No The first index of the tile to be set for collision.
stop number No The last index of the tile to be set for collision.
collides boolean Yes true If true it will enable collision. If false it will clear collision.
recalculateFaces boolean Yes true Whether or not to recalculate the tile faces after the update.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1130
Since: 3.50.0
setCollisionByExclusion ​
<instance> setCollisionByExclusion(indexes, [collides], [recalculateFaces]) ​
Description:
Sets collision on all tiles in the given layer, except for tiles that have an index specified in
the given array. The collides parameter controls if collision will be enabled (true) or
disabled (false). Tile indexes not currently in the layer are not affected.
Parameters:
name type optional default description
indexes Array.<number> No An array of the tile indexes to not be counted for collision.
collides boolean Yes true If true it will enable collision. If false it will clear collision.
recalculateFaces boolean Yes true Whether or not to recalculate the tile faces after the update.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1178
Since: 3.50.0
setCollisionByProperty ​
<instance> setCollisionByProperty(properties, [collides], [recalculateFaces]) ​
Description:
Sets collision on the tiles within a layer by checking tile properties. If a tile has a property
that matches the given properties object, its collision flag will be set. The collides
parameter controls if collision will be enabled (true) or disabled (false). Passing in
{ collides: true } would update the collision flag on any tiles with a "collides" property that
has a value of true. Any tile that doesn't have "collides" set to true will be ignored. You can
also use an array of values, e.g. { types: ["stone", "lava", "sand" ] } . If a tile has a
"types" property that matches any of those values, its collision flag will be updated.
Parameters:
name type optional default description
properties object No An object with tile properties and corresponding values that should be checked.
collides boolean Yes true If true it will enable collision. If false it will clear collision.
recalculateFaces boolean Yes true Whether or not to recalculate the tile faces after the update.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1153
Since: 3.50.0
setCollisionFromCollisionGroup ​
<instance> setCollisionFromCollisionGroup([collides], [recalculateFaces]) ​
Description:
Sets collision on the tiles within a layer by checking each tiles collision group data
(typically defined in Tiled within the tileset collision editor). If any objects are found within
a tiles collision group, the tile's colliding information will be set. The collides parameter
controls if collision will be enabled (true) or disabled (false).
Parameters:
name type optional default description
collides boolean Yes true If true it will enable collision. If false it will clear collision.
recalculateFaces boolean Yes true Whether or not to recalculate the tile faces after the update.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1199
Since: 3.50.0
setCullPadding ​
<instance> setCullPadding([paddingX], [paddingY]) ​
Description:
When a Camera culls the tiles in this layer it does so using its view into the world, building up a
rectangle inside which the tiles must exist or they will be culled. Sometimes you may need to expand the size
of this 'cull rectangle', especially if you plan on rotating the Camera viewing the layer. Do so
by providing the padding values. The values given are in tiles, not pixels. So if the tile width was 32px
and you set paddingX to be 4, it would add 32px x 4 to the cull rectangle (adjusted for scale)
Parameters:
name type optional default description
paddingX number Yes 1 The amount of extra horizontal tiles to add to the cull check padding.
paddingY number Yes 1 The amount of extra vertical tiles to add to the cull check padding.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1082
Since: 3.50.0
setRenderOrder ​
<instance> setRenderOrder(renderOrder) ​
Description:
Sets the rendering (draw) order of the tiles in this layer.
The default is 'right-down', meaning it will order the tiles starting from the top-left,
drawing to the right and then moving down to the next row.
The draw orders are:
0 = right-down
1 = left-down
2 = right-up
3 = left-up
Setting the render order does not change the tiles or how they are stored in the layer,
it purely impacts the order in which they are rendered.
You can provide either an integer (0 to 3), or the string version of the order.
Parameters:
name type optional description
renderOrder number | string No The render (draw) order value. Either an integer between 0 and 3, or a string: 'right-down', 'left-down', 'right-up' or 'left-up'.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L388
Since: 3.50.0
setSkipCull ​
<instance> setSkipCull([value]) ​
Description:
You can control if the Cameras should cull tiles before rendering them or not.
By default the camera will try to cull the tiles in this layer, to avoid over-drawing to the renderer.
However, there are some instances when you may wish to disable this.
Parameters:
name type optional default description
value boolean Yes true Set to true to stop culling tiles. Set to false to enable culling again.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1059
Since: 3.50.0
setTileIndexCallback ​
<instance> setTileIndexCallback(indexes, callback, callbackContext) ​
Description:
Sets a global collision callback for the given tile index within the layer. This will affect all
tiles on this layer that have the same index. If a callback is already set for the tile index it
will be replaced. Set the callback to null to remove it. If you want to set a callback for a tile
at a specific location on the map then see setTileLocationCallback.
Parameters:
name type optional description
indexes number | Array.<number> No Either a single tile index, or an array of tile indexes to have a collision callback set for.
callback function No The callback that will be invoked when the tile is collided with.
callbackContext object No The context under which the callback is called.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1220
Since: 3.50.0
setTileLocationCallback ​
<instance> setTileLocationCallback([tileX], [tileY], [width], [height], [callback], [callbackContext]) ​
Description:
Sets a collision callback for the given rectangular area (in tile coordinates) within the layer.
If a callback is already set for the tile index it will be replaced. Set the callback to null to
remove it.
Parameters:
name type optional description
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
callback function Yes The callback that will be invoked when the tile is collided with.
callbackContext object Yes The context, or scope, under which the callback is invoked.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1242
Since: 3.50.0
setTint ​
<instance> setTint([tint], [tileX], [tileY], [width], [height], [filteringOptions]) ​
Description:
Sets an additive tint on each Tile within the given area.
The tint works by taking the pixel color values from the tileset texture, and then
multiplying it by the color value of the tint.
If no area values are given then all tiles will be tinted to the given color.
To remove a tint call this method with either no parameters, or by passing white 0xffffff as the tint color.
If a tile already has a tint set then calling this method will override that.
Tags:
webglOnly
Parameters:
name type optional default description
tint number Yes "0xffffff" The tint color being applied to each tile within the region. Given as a hex value, i.e. 0xff0000 for red. Set to white ( 0xffffff ) to reset the tint.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area to search.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area to search.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L655
Since: 3.60.0
setTintFill ​
<instance> setTintFill([tint], [tileX], [tileY], [width], [height], [filteringOptions]) ​
Description:
Sets a fill-based tint on each Tile within the given area.
Unlike an additive tint, a fill-tint literally replaces the pixel colors from the texture
with those in the tint.
If no area values are given then all tiles will be tinted to the given color.
To remove a tint call this method with either no parameters, or by passing white 0xffffff as the tint color.
If a tile already has a tint set then calling this method will override that.
Tags:
webglOnly
Parameters:
name type optional default description
tint number Yes "0xffffff" The tint color being applied to each tile within the region. Given as a hex value, i.e. 0xff0000 for red. Set to white ( 0xffffff ) to reset the tint.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area to search.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area to search.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
filteringOptions Phaser.Types.Tilemaps.FilteringOptions Yes Optional filters to apply when getting the tiles.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L693
Since: 3.70.0
shuffle ​
<instance> shuffle([tileX], [tileY], [width], [height]) ​
Description:
Shuffles the tiles in a rectangular region (specified in tile coordinates) within the given
layer. It will only randomize the tiles in that area, so if they're all the same nothing will
appear to have changed! This method only modifies tile indexes and does not change collision
information.
Parameters:
name type optional description
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1266
Since: 3.50.0
swapByIndex ​
<instance> swapByIndex(tileA, tileB, [tileX], [tileY], [width], [height]) ​
Description:
Scans the given rectangular area (given in tile coordinates) for tiles with an index matching
indexA and swaps then with indexB . This only modifies the index and does not change collision
information.
Parameters:
name type optional description
tileA number No First tile index.
tileB number No Second tile index.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1289
Since: 3.50.0
tileToWorldX ​
<instance> tileToWorldX(tileX, [camera]) ​
Description:
Converts from tile X coordinates (tile units) to world X coordinates (pixels), factoring in the
layers position, scale and scroll.
Parameters:
name type optional description
tileX number No The x coordinate, in tiles, not pixels.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: number - The Tile X coordinate converted to pixels.
Source: src/tilemaps/TilemapLayer.js#L1313
Since: 3.50.0
tileToWorldXY ​
<instance> tileToWorldXY(tileX, tileY, [point], [camera]) ​
Description:
Converts from tile XY coordinates (tile units) to world XY coordinates (pixels), factoring in the
layers position, scale and scroll. This will return a new Vector2 object or update the given
point object.
Parameters:
name type optional description
tileX number No The x coordinate, in tiles, not pixels.
tileY number No The y coordinate, in tiles, not pixels.
point Phaser.Math.Vector2 Yes A Vector2 to store the coordinates in. If not given a new Vector2 is created.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: Phaser.Math.Vector2 - A Vector2 containing the world coordinates of the Tile.
Source: src/tilemaps/TilemapLayer.js#L1347
Since: 3.50.0
tileToWorldY ​
<instance> tileToWorldY(tileY, [camera]) ​
Description:
Converts from tile Y coordinates (tile units) to world Y coordinates (pixels), factoring in the
layers position, scale and scroll.
Parameters:
name type optional description
tileY number No The y coordinate, in tiles, not pixels.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: number - The Tile Y coordinate converted to pixels.
Source: src/tilemaps/TilemapLayer.js#L1330
Since: 3.50.0
weightedRandomize ​
<instance> weightedRandomize(weightedIndexes, [tileX], [tileY], [width], [height]) ​
Description:
Randomizes the indexes of a rectangular region of tiles (in tile coordinates) within the
specified layer. Each tile will receive a new index. New indexes are drawn from the given
weightedIndexes array. An example weighted array:
[
{ index: 6, weight: 4 }, // Probability of index 6 is 4 / 8
{ index: 7, weight: 2 }, // Probability of index 7 would be 2 / 8
{ index: 8, weight: 1.5 }, // Probability of index 8 would be 1.5 / 8
{ index: 26, weight: 0.5 } // Probability of index 27 would be 0.5 / 8
]
The probability of any index being choose is (the index's weight) / (sum of all weights). This
method only modifies tile indexes and does not change collision information.
Parameters:
name type optional description
weightedIndexes Array.<object> No An array of objects to randomly draw from during randomization. They should be in the form: { index: 0, weight: 4 } or { index: [0, 1], weight: 4 } if you wish to draw from multiple tile indexes.
tileX number Yes The left most tile index (in tile coordinates) to use as the origin of the area.
tileY number Yes The top most tile index (in tile coordinates) to use as the origin of the area.
width number Yes How many tiles wide from the tileX index the area will be.
height number Yes How many tiles tall from the tileY index the area will be.
Returns: Phaser.Tilemaps.TilemapLayer - This Tilemap Layer object.
Source: src/tilemaps/TilemapLayer.js#L1393
Since: 3.50.0
worldToTileX ​
<instance> worldToTileX(worldX, [snapToFloor], [camera]) ​
Description:
Converts from world X coordinates (pixels) to tile X coordinates (tile units), factoring in the
layers position, scale and scroll.
You cannot call this method for Isometric or Hexagonal tilemaps as they require
both worldX and worldY values to determine the correct tile, instead you
should use the worldToTileXY method.
Parameters:
name type optional description
worldX number No The x coordinate to be converted, in pixels, not tiles.
snapToFloor boolean Yes Whether or not to round the tile coordinate down to the nearest integer.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: number - The tile X coordinate based on the world value.
Source: src/tilemaps/TilemapLayer.js#L1426
Since: 3.50.0
worldToTileXY ​
<instance> worldToTileXY(worldX, worldY, [snapToFloor], [point], [camera]) ​
Description:
Converts from world XY coordinates (pixels) to tile XY coordinates (tile units), factoring in the
layers position, scale and scroll. This will return a new Vector2 object or update the given
point object.
Parameters:
name type optional description
worldX number No The x coordinate to be converted, in pixels, not tiles.
worldY number No The y coordinate to be converted, in pixels, not tiles.
snapToFloor boolean Yes Whether or not to round the tile coordinate down to the nearest integer.
point Phaser.Math.Vector2 Yes A Vector2 to store the coordinates in. If not given a new Vector2 is created.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: Phaser.Math.Vector2 - A Vector2 containing the tile coordinates of the world values.
Source: src/tilemaps/TilemapLayer.js#L1470
Since: 3.50.0
worldToTileY ​
<instance> worldToTileY(worldY, [snapToFloor], [camera]) ​
Description:
Converts from world Y coordinates (pixels) to tile Y coordinates (tile units), factoring in the
layers position, scale and scroll.
You cannot call this method for Isometric or Hexagonal tilemaps as they require
both worldX and worldY values to determine the correct tile, instead you
should use the worldToTileXY method.
Parameters:
name type optional description
worldY number No The y coordinate to be converted, in pixels, not tiles.
snapToFloor boolean Yes Whether or not to round the tile coordinate down to the nearest integer.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use when calculating the tile index from the world values.
Returns: number - The tile Y coordinate based on the world value.
Source: src/tilemaps/TilemapLayer.js#L1448
Since: 3.50.0
Previous
Tilemap
Next
Tileset
Inherited Members
Public Members
collisionCategory
collisionMask
cullCallback
culledTiles
cullPaddingX
cullPaddingY
displayOriginX
displayOriginY
gidMap
isTilemap
layer
layerIndex
originX
originY
skipCull
tilemap
tilesDrawn
tileset
tilesTotal
Inherited Methods
Public Methods
calculateFacesAt
calculateFacesWithin
copy
createFromTiles
cull
destroy
fill
filterTiles
findByIndex
findTile
forEachTile
getIsoTileAtWorldXY
getTileAt
getTileAtWorldXY
getTileCorners
getTilesWithin
getTilesWithinShape
getTilesWithinWorldXY
hasTileAt
hasTileAtWorldXY
putTileAt
putTileAtWorldXY
putTilesAt
randomize
removeTileAt
removeTileAtWorldXY
renderDebug
replaceByIndex
setCollision
setCollisionBetween
setCollisionByExclusion
setCollisionByProperty
setCollisionFromCollisionGroup
setCullPadding
setRenderOrder
setSkipCull
setTileIndexCallback
setTileLocationCallback
setTint
setTintFill
shuffle
swapByIndex
tileToWorldX
tileToWorldXY
tileToWorldY
weightedRandomize
worldToTileX
worldToTileXY
worldToTileY
