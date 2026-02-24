# Phaser.Tilemaps.Parsers | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/tilemaps-parsers

Phaser API Documentation
Namespaces
Phaser.Tilemaps.Parsers
Version: Phaser v3.90.0
On this page
Phaser.Tilemaps.Parsers
Scope: static
Source: src/tilemaps/parsers/index.js#L7
Static functions ​
FromOrientationString ​
<static> FromOrientationString([orientation]) ​
Description:
Get the Tilemap orientation from the given string.
Parameters:
name type optional description
orientation string Yes The orientation type as a string.
Returns: Phaser.Tilemaps.OrientationType - The Tilemap Orientation type.
Source: src/tilemaps/parsers/FromOrientationString.js#L9
Since: 3.50.0
Parse ​
<static> Parse(name, mapFormat, data, tileWidth, tileHeight, insertNull) ​
Description:
Parses raw data of a given Tilemap format into a new MapData object. If no recognized data format
is found, returns null . When loading from CSV or a 2D array, you should specify the tileWidth &
tileHeight. When parsing from a map from Tiled, the tileWidth & tileHeight will be pulled from
the map data.
Parameters:
name type optional description
name string No The name of the tilemap, used to set the name on the MapData.
mapFormat number No See ../Formats.js.
data Array.<Array.<number>> | string object No
tileWidth number No The width of a tile in pixels. Required for 2D array and CSV, but ignored for Tiled JSON.
tileHeight number No The height of a tile in pixels. Required for 2D array and CSV, but ignored for Tiled JSON.
insertNull boolean No Controls how empty tiles, tiles with an index of -1, in the map data are handled. If true , empty locations will get a value of null . If false , empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to true will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set.
Returns: Phaser.Tilemaps.MapData - The created MapData object.
Source: src/tilemaps/parsers/Parse.js#L13
Since: 3.0.0
Parse2DArray ​
<static> Parse2DArray(name, data, tileWidth, tileHeight, insertNull) ​
Description:
Parses a 2D array of tile indexes into a new MapData object with a single layer.
Parameters:
name type optional description
name string No The name of the tilemap, used to set the name on the MapData.
data Array.<Array.<number>> No 2D array, CSV string or Tiled JSON object.
tileWidth number No The width of a tile in pixels.
tileHeight number No The height of a tile in pixels.
insertNull boolean No Controls how empty tiles, tiles with an index of -1, in the map data are handled. If true , empty locations will get a value of null . If false , empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to true will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set.
Returns: Phaser.Tilemaps.MapData - The MapData object.
Source: src/tilemaps/parsers/Parse2DArray.js#L12
Since: 3.0.0
ParseCSV ​
<static> ParseCSV(name, data, tileWidth, tileHeight, insertNull) ​
Description:
Parses a CSV string of tile indexes into a new MapData object with a single layer.
Parameters:
name type optional description
name string No The name of the tilemap, used to set the name on the MapData.
data string No CSV string of tile indexes.
tileWidth number No The width of a tile in pixels.
tileHeight number No The height of a tile in pixels.
insertNull boolean No Controls how empty tiles, tiles with an index of -1, in the map data are handled. If true , empty locations will get a value of null . If false , empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to true will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set.
Returns: Phaser.Tilemaps.MapData - The resulting MapData object.
Source: src/tilemaps/parsers/ParseCSV.js#L10
Since: 3.0.0
Static functions ​
Impact
Tiled
Previous
Phaser.Tilemaps.Parsers.Tiled
Next
Phaser.Tilemaps
Static functions
FromOrientationString
Parse
Parse2DArray
ParseCSV
Static functions
