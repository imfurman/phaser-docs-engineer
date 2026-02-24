# ObjectHelper | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tilemaps-objecthelper

Phaser API Documentation
Class
ObjectHelper
Version: Phaser v3.90.0
On this page
ObjectHelper
The ObjectHelper helps tie objects with gids into the tileset
that sits behind them.
Constructor
new ObjectHelper(tilesets)
Parameters
name type optional description
tilesets Array.< Phaser.Tilemaps.Tileset > No The backing tileset data.
Scope : static
Source: src/tilemaps/ObjectHelper.js#L9
Since: 3.60.0
Public Members ​
enabled ​
enabled: boolean ​
Description:
Enabled if the object helper reaches in to tilesets for data.
Disabled if it only uses data directly on a gid object.
Source: src/tilemaps/ObjectHelper.js#L60
Since: 3.60.0
gids ​
gids: array ​
Description:
The Tile GIDs array.
Source: src/tilemaps/ObjectHelper.js#L27
Since: 3.60.0
Public Methods ​
getTypeIncludingTile ​
<instance> getTypeIncludingTile(obj) ​
Description:
Gets the Tiled type field value from the object or the gid behind it.
Parameters:
name type optional description
obj Phaser.Types.Tilemaps.TiledObject No The Tiled object to investigate.
Returns: string - The type of the object, the tile behind the gid of the object, or undefined .
Source: src/tilemaps/ObjectHelper.js#L82
Since: 3.60.0
setPropertiesFromTiledObject ​
<instance> setPropertiesFromTiledObject(sprite, obj) ​
Description:
Sets the sprite.data field from the tiled properties on the object and its tile (if any).
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No No description provided
obj Phaser.Types.Tilemaps.TiledObject No No description provided
Source: src/tilemaps/ObjectHelper.js#L168
Since: 3.60.0
setTextureAndFrame ​
<instance> setTextureAndFrame(sprite, [key], [frame], [obj]) ​
Description:
Sets the sprite texture data as specified (usually in a config) or, failing that,
as specified in the gid of the object being loaded (if any).
This fallback will only work if the tileset was loaded as a spritesheet matching
the geometry of sprites fed into tiled, so that, for example: "tile id # 3 "" within
the tileset is the same as texture frame 3 from the image of the tileset.
Parameters:
name type optional description
sprite Phaser.GameObjects.GameObject No The Game Object to modify.
key string | Phaser.Textures.Texture Yes The texture key to set (or else the obj.gid 's tile is used if available).
frame string | number Phaser.Textures.Frame Yes
obj Phaser.Types.Tilemaps.TiledObject Yes The Tiled object for fallback.
Source: src/tilemaps/ObjectHelper.js#L121
Since: 3.60.0
Previous
MapData
Next
ObjectLayer
Public Members
enabled
gids
Public Methods
getTypeIncludingTile
setPropertiesFromTiledObject
setTextureAndFrame
