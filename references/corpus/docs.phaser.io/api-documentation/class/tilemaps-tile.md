# Tile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tilemaps-tile

Phaser API Documentation
Class
Tile
Version: Phaser v3.90.0
On this page
Tile
A Tile is a representation of a single tile within the Tilemap. This is a lightweight data
representation, so its position information is stored without factoring in scroll, layer
scale or layer position.
Constructor
new Tile(layer, index, x, y, width, height, baseWidth, baseHeight)
Parameters
name type optional description
layer Phaser.Tilemaps.LayerData No The LayerData object in the Tilemap that this tile belongs to.
index number No The unique index of this tile within the map.
x number No The x coordinate of this tile in tile coordinates.
y number No The y coordinate of this tile in tile coordinates.
width number No Width of the tile in pixels.
height number No Height of the tile in pixels.
baseWidth number No The base width a tile in the map (in pixels). Tiled maps support multiple tileset sizes within one map, but they are still placed at intervals of the base tile width.
baseHeight number No The base height of the tile in pixels (in pixels). Tiled maps support multiple tileset sizes within one map, but they are still placed at intervals of the base tile height.
Scope : static
Extends
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.Flip
Phaser.GameObjects.Components.Visible
Source: src/tilemaps/Tile.js#L13
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.Flip :
flipX
flipY
From Phaser.GameObjects.Components.Visible :
visible
Public Members ​
baseHeight ​
baseHeight: number ​
Description:
The maps base height of a tile in pixels. Tiled maps support multiple tileset sizes
within one map, but they are still placed at intervals of the base tile size.
Source: src/tilemaps/Tile.js#L140
Since: 3.0.0
baseWidth ​
baseWidth: number ​
Description:
The maps base width of a tile in pixels. Tiled maps support multiple tileset sizes
within one map, but they are still placed at intervals of the base tile size.
Source: src/tilemaps/Tile.js#L130
Since: 3.0.0
bottom ​
bottom: number ​
Description:
The bottom of the tile in pixels.
Set in the updatePixelXY method.
Source: src/tilemaps/Tile.js#L119
Since: 3.50.0
canCollide ​
canCollide: boolean ​
Description:
True if this tile can collide on any of its faces or has a collision callback set.
Source: src/tilemaps/Tile.js#L849
Since: 3.0.0
collideDown ​
collideDown: boolean ​
Description:
Whether the tile should collide with any object on the bottom side.
This property is used by Arcade Physics only, however, you can also use it
in your own checks.
Source: src/tilemaps/Tile.js#L228
Since: 3.0.0
collideLeft ​
collideLeft: boolean ​
Description:
Whether the tile should collide with any object on the left side.
This property is used by Arcade Physics only, however, you can also use it
in your own checks.
Source: src/tilemaps/Tile.js#L192
Since: 3.0.0
collideRight ​
collideRight: boolean ​
Description:
Whether the tile should collide with any object on the right side.
This property is used by Arcade Physics only, however, you can also use it
in your own checks.
Source: src/tilemaps/Tile.js#L204
Since: 3.0.0
collides ​
collides: boolean ​
Description:
True if this tile can collide on any of its faces.
Source: src/tilemaps/Tile.js#L866
Since: 3.0.0
collideUp ​
collideUp: boolean ​
Description:
Whether the tile should collide with any object on the top side.
This property is used by Arcade Physics only, however, you can also use it
in your own checks.
Source: src/tilemaps/Tile.js#L216
Since: 3.0.0
collisionCallback ​
collisionCallback: function ​
Description:
Tile collision callback.
Source: src/tilemaps/Tile.js#L276
Since: 3.0.0
collisionCallbackContext ​
collisionCallbackContext: object ​
Description:
The context in which the collision callback will be called.
Source: src/tilemaps/Tile.js#L285
Since: 3.0.0
faceBottom ​
faceBottom: boolean ​
Description:
Whether the tiles bottom edge is interesting for collisions.
Source: src/tilemaps/Tile.js#L267
Since: 3.0.0
faceLeft ​
faceLeft: boolean ​
Description:
Whether the tiles left edge is interesting for collisions.
Source: src/tilemaps/Tile.js#L240
Since: 3.0.0
faceRight ​
faceRight: boolean ​
Description:
Whether the tiles right edge is interesting for collisions.
Source: src/tilemaps/Tile.js#L249
Since: 3.0.0
faceTop ​
faceTop: boolean ​
Description:
Whether the tiles top edge is interesting for collisions.
Source: src/tilemaps/Tile.js#L258
Since: 3.0.0
hasInterestingFace ​
hasInterestingFace: boolean ​
Description:
True if this tile has any interesting faces.
Source: src/tilemaps/Tile.js#L883
Since: 3.0.0
height ​
height: number ​
Description:
The height of the tile in pixels.
Source: src/tilemaps/Tile.js#L99
Since: 3.0.0
index ​
index: number ​
Description:
The index of this tile within the map data corresponding to the tileset, or -1 if this
represents a blank tile.
Source: src/tilemaps/Tile.js#L62
Since: 3.0.0
layer ​
layer: Phaser.Tilemaps.LayerData ​
Description:
The LayerData in the Tilemap data that this tile belongs to.
Source: src/tilemaps/Tile.js#L53
Since: 3.0.0
physics ​
physics: object ​
Description:
An empty object where physics-engine specific information (e.g. bodies) may be stored.
Source: src/tilemaps/Tile.js#L318
Since: 3.0.0
pixelX ​
pixelX: number ​
Description:
The x coordinate of the top left of this tile in pixels. This is relative to the top left
of the layer this tile is being rendered within. This property does NOT factor in camera
scroll, layer scale or layer position.
Source: src/tilemaps/Tile.js#L150
Since: 3.0.0
pixelY ​
pixelY: number ​
Description:
The y coordinate of the top left of this tile in pixels. This is relative to the top left
of the layer this tile is being rendered within. This property does NOT factor in camera
scroll, layer scale or layer position.
Source: src/tilemaps/Tile.js#L161
Since: 3.0.0
properties ​
properties: any ​
Description:
Tile specific properties. These usually come from Tiled.
Source: src/tilemaps/Tile.js#L174
Since: 3.0.0
right ​
right: number ​
Description:
The right of the tile in pixels.
Set in the updatePixelXY method.
Source: src/tilemaps/Tile.js#L108
Since: 3.50.0
rotation ​
rotation: number ​
Description:
The rotation angle of this tile.
Source: src/tilemaps/Tile.js#L183
Since: 3.0.0
tilemap ​
tilemap: Phaser.Tilemaps.Tilemap ​
Description:
The tilemap that contains this Tile. This will only return null if accessed from a LayerData
instance before the tile is placed within a TilemapLayer.
Source: src/tilemaps/Tile.js#L949
Since: 3.0.0
tilemapLayer ​
tilemapLayer: Phaser.Tilemaps.TilemapLayer ​
Description:
The tilemap layer that contains this Tile. This will only return null if accessed from a
LayerData instance before the tile is placed within a TilemapLayer.
Source: src/tilemaps/Tile.js#L931
Since: 3.0.0
tileset ​
tileset: Phaser.Tilemaps.Tileset ​
Description:
The tileset that contains this Tile. This is null if accessed from a LayerData instance
before the tile is placed in a TilemapLayer, or if the tile has an index that doesn't correspond
to any of the maps tilesets.
Source: src/tilemaps/Tile.js#L900
Since: 3.0.0
tint ​
tint: number ​
Description:
The tint to apply to this tile. Note: tint is currently a single color value instead of
the 4 corner tint component on other GameObjects.
Source: src/tilemaps/Tile.js#L294
Since: 3.0.0
tintFill ​
tintFill: boolean ​
Description:
The tint fill mode.
false = An additive tint (the default), where vertices colors are blended with the texture.
true = A fill tint, where the vertices colors replace the texture, but respects texture alpha.
Source: src/tilemaps/Tile.js#L305
Since: 3.70.0
width ​
width: number ​
Description:
The width of the tile in pixels.
Source: src/tilemaps/Tile.js#L90
Since: 3.0.0
x ​
x: number ​
Description:
The x map coordinate of this tile in tile units.
Source: src/tilemaps/Tile.js#L72
Since: 3.0.0
y ​
y: number ​
Description:
The y map coordinate of this tile in tile units.
Source: src/tilemaps/Tile.js#L81
Since: 3.0.0
Inherited Methods ​
From Phaser.GameObjects.Components.AlphaSingle :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.Flip :
resetFlip
setFlip
setFlipX
setFlipY
toggleFlipX
toggleFlipY
From Phaser.GameObjects.Components.Visible :
setVisible
Public Methods ​
containsPoint ​
<instance> containsPoint(x, y) ​
Description:
Check if the given x and y world coordinates are within this Tile. This does not factor in
camera scroll, layer scale or layer position.
Parameters:
name type optional description
x number No The x coordinate to test.
y number No The y coordinate to test.
Returns: boolean - True if the coordinates are within this Tile, otherwise false.
Source: src/tilemaps/Tile.js#L328
Since: 3.0.0
copy ​
<instance> copy(tile) ​
Description:
Copies the tile data and properties from the given Tile to this Tile. This copies everything
except for position and interesting face calculations.
Parameters:
name type optional description
tile Phaser.Tilemaps.Tile No The tile to copy from.
Returns: Phaser.Tilemaps.Tile - This Tile object instance.
Source: src/tilemaps/Tile.js#L345
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Clean up memory.
Source: src/tilemaps/Tile.js#L836
Since: 3.0.0
getBottom ​
<instance> getBottom([camera]) ​
Description:
Gets the world Y position of the bottom side of the tile, factoring in the layer's position,
scale and scroll.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use to perform the check.
Returns: number - The bottom (y) value of this tile.
Source: src/tilemaps/Tile.js#L477
Since: 3.0.0
getBounds ​
<instance> getBounds([camera], [output]) ​
Description:
Gets the world rectangle bounding box for the tile, factoring in the layers position,
scale and scroll.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use to perform the check.
output Phaser.Geom.Rectangle Yes Optional Rectangle object to store the results in.
Returns: Phaser.Geom.Rectangle , object - The bounds of this Tile.
Source: src/tilemaps/Tile.js#L497
Since: 3.0.0
getCenterX ​
<instance> getCenterX([camera]) ​
Description:
Gets the world X position of the center of the tile, factoring in the layer's position,
scale and scroll.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use to perform the check.
Returns: number - The center x position of this Tile.
Source: src/tilemaps/Tile.js#L521
Since: 3.0.0
getCenterY ​
<instance> getCenterY([camera]) ​
Description:
Gets the world Y position of the center of the tile, factoring in the layer's position,
scale and scroll.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use to perform the check.
Returns: number - The center y position of this Tile.
Source: src/tilemaps/Tile.js#L537
Since: 3.0.0
getCollisionGroup ​
<instance> getCollisionGroup() ​
Description:
The collision group for this Tile, defined within the Tileset. This returns a reference to
the collision group stored within the Tileset, so any modification of the returned object
will impact all tiles that have the same index as this tile.
Returns: object - The collision group for this Tile, as defined in the Tileset, or null if no group was defined.
Source: src/tilemaps/Tile.js#L375
Since: 3.0.0
getLeft ​
<instance> getLeft([camera]) ​
Description:
Gets the world X position of the left side of the tile, factoring in the layers position,
scale and scroll.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use to perform the check.
Returns: number - The left (x) value of this tile.
Source: src/tilemaps/Tile.js#L406
Since: 3.0.0
getRight ​
<instance> getRight([camera]) ​
Description:
Gets the world X position of the right side of the tile, factoring in the layer's position,
scale and scroll.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use to perform the check.
Returns: number - The right (x) value of this tile.
Source: src/tilemaps/Tile.js#L431
Since: 3.0.0
getTileData ​
<instance> getTileData() ​
Description:
The tile data for this Tile, defined within the Tileset. This typically contains Tiled
collision data, tile animations and terrain information. This returns a reference to the tile
data stored within the Tileset, so any modification of the returned object will impact all
tiles that have the same index as this tile.
Returns: object - The tile data for this Tile, as defined in the Tileset, or null if no data was defined.
Source: src/tilemaps/Tile.js#L390
Since: 3.0.0
getTop ​
<instance> getTop([camera]) ​
Description:
Gets the world Y position of the top side of the tile, factoring in the layer's position,
scale and scroll.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera to use to perform the check.
Returns: number - The top (y) value of this tile.
Source: src/tilemaps/Tile.js#L449
Since: 3.0.0
intersects ​
<instance> intersects(x, y, right, bottom) ​
Description:
Check for intersection with this tile. This does not factor in camera scroll, layer scale or
layer position.
Parameters:
name type optional description
x number No The x axis in pixels.
y number No The y axis in pixels.
right number No The right point.
bottom number No The bottom point.
Returns: boolean - true if the Tile intersects with the given dimensions, otherwise false .
Source: src/tilemaps/Tile.js#L553
Since: 3.0.0
isInteresting ​
<instance> isInteresting(collides, faces) ​
Description:
Checks if the tile is interesting.
Parameters:
name type optional description
collides boolean No If true, will consider the tile interesting if it collides on any side.
faces boolean No If true, will consider the tile interesting if it has an interesting face.
Returns: boolean - True if the Tile is interesting, otherwise false.
Source: src/tilemaps/Tile.js#L575
Since: 3.0.0
resetCollision ​
<instance> resetCollision([recalculateFaces]) ​
Description:
Reset collision status flags.
Parameters:
name type optional default description
recalculateFaces boolean Yes true Whether or not to recalculate interesting faces for this tile and its neighbors.
Returns: Phaser.Tilemaps.Tile - This Tile object instance.
Source: src/tilemaps/Tile.js#L604
Since: 3.0.0
resetFaces ​
<instance> resetFaces() ​
Description:
Reset faces.
Returns: Phaser.Tilemaps.Tile - This Tile object instance.
Source: src/tilemaps/Tile.js#L641
Since: 3.0.0
setCollision ​
<instance> setCollision(left, [right], [up], [down], [recalculateFaces]) ​
Description:
Sets the collision flags for each side of this tile and updates the interesting faces list.
Parameters:
name type optional default description
left boolean No Indicating collide with any object on the left.
right boolean Yes Indicating collide with any object on the right.
up boolean Yes Indicating collide with any object on the top.
down boolean Yes Indicating collide with any object on the bottom.
recalculateFaces boolean Yes true Whether or not to recalculate interesting faces for this tile and its neighbors.
Returns: Phaser.Tilemaps.Tile - This Tile object instance.
Source: src/tilemaps/Tile.js#L659
Since: 3.0.0
setCollisionCallback ​
<instance> setCollisionCallback(callback, context) ​
Description:
Set a callback to be called when this tile is hit by an object. The callback must true for
collision processing to take place.
Parameters:
name type optional description
callback function No Callback function.
context object No Callback will be called within this context.
Returns: Phaser.Tilemaps.Tile - This Tile object instance.
Source: src/tilemaps/Tile.js#L703
Since: 3.0.0
setSize ​
<instance> setSize(tileWidth, tileHeight, baseWidth, baseHeight) ​
Description:
Sets the size of the tile and updates its pixelX and pixelY.
Parameters:
name type optional description
tileWidth number No The width of the tile in pixels.
tileHeight number No The height of the tile in pixels.
baseWidth number No The base width a tile in the map (in pixels).
baseHeight number No The base height of the tile in pixels (in pixels).
Returns: Phaser.Tilemaps.Tile - This Tile object instance.
Source: src/tilemaps/Tile.js#L731
Since: 3.0.0
updatePixelXY ​
<instance> updatePixelXY() ​
Description:
Used internally. Updates the tiles world XY position based on the current tile size.
Returns: Phaser.Tilemaps.Tile - This Tile object instance.
Source: src/tilemaps/Tile.js#L756
Since: 3.0.0
Previous
ObjectLayer
Next
Tilemap
Inherited Members
Public Members
baseHeight
baseWidth
bottom
canCollide
collideDown
collideLeft
collideRight
collides
collideUp
collisionCallback
collisionCallbackContext
faceBottom
faceLeft
faceRight
faceTop
hasInterestingFace
height
index
layer
physics
pixelX
pixelY
properties
right
rotation
tilemap
tilemapLayer
tileset
tint
tintFill
width
x
y
Inherited Methods
Public Methods
containsPoint
copy
destroy
getBottom
getBounds
getCenterX
getCenterY
getCollisionGroup
getLeft
getRight
getTileData
getTop
intersects
isInteresting
resetCollision
resetFaces
setCollision
setCollisionCallback
setSize
updatePixelXY
