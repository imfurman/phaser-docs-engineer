# MapData | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tilemaps-mapdata

Phaser API Documentation
Class
MapData
Version: Phaser v3.90.0
On this page
MapData
A class for representing data about a map. Maps are parsed from CSV, Tiled, etc. into this
format. A Tilemap object get a copy of this data and then unpacks the needed properties into
itself.
Constructor
new MapData([config])
Parameters
name type optional description
config Phaser.Types.Tilemaps.MapDataConfig Yes The Map configuration object.
Scope : static
Source: src/tilemaps/mapdata/MapData.js#L11
Since: 3.0.0
Public Members ​
collision ​
collision: object ​
Description:
An object of collision data. Must be created as physics object or will return undefined.
Source: src/tilemaps/mapdata/MapData.js#L187
Since: 3.0.0
format ​
format: number ​
Description:
The format of the map data.
Source: src/tilemaps/mapdata/MapData.js#L104
Since: 3.0.0
height ​
height: number ​
Description:
The height of the entire tilemap.
Source: src/tilemaps/mapdata/MapData.js#L50
Since: 3.0.0
heightInPixels ​
heightInPixels: number ​
Description:
The height in pixels of the entire tilemap.
Source: src/tilemaps/mapdata/MapData.js#L95
Since: 3.0.0
hexSideLength ​
hexSideLength: number ​
Description:
The length of the horizontal sides of the hexagon.
Only used for hexagonal orientation Tilemaps.
Source: src/tilemaps/mapdata/MapData.js#L223
Since: 3.50.0
imageCollections ​
imageCollections: array ​
Description:
The collection of images the map uses(specified in Tiled)
Source: src/tilemaps/mapdata/MapData.js#L205
Since: 3.0.0
images ​
images: array ​
Description:
An array of Tiled Image Layers.
Source: src/tilemaps/mapdata/MapData.js#L163
Since: 3.0.0
infinite ​
infinite: boolean ​
Description:
If the map is infinite or not.
Source: src/tilemaps/mapdata/MapData.js#L59
Since: 3.17.0
layers ​
layers: Array.< Phaser.Tilemaps.LayerData >, Phaser.Tilemaps.ObjectLayer ​
Description:
An array with all the layers configured to the MapData.
Source: src/tilemaps/mapdata/MapData.js#L154
Since: 3.0.0
name ​
name: string ​
Description:
The key in the Phaser cache that corresponds to the loaded tilemap data.
Source: src/tilemaps/mapdata/MapData.js#L32
Since: 3.0.0
objects ​
objects: Array.< Phaser.Types.Tilemaps.ObjectLayerConfig > ​
Description:
An object of Tiled Object Layers.
Source: src/tilemaps/mapdata/MapData.js#L172
Since: 3.0.0
orientation ​
orientation: Phaser.Tilemaps.OrientationType ​
Description:
The orientation of the map data (i.e. orthogonal, isometric, hexagonal), default 'orthogonal'.
Source: src/tilemaps/mapdata/MapData.js#L113
Since: 3.50.0
properties ​
properties: object ​
Description:
Map specific properties (can be specified in Tiled)
Source: src/tilemaps/mapdata/MapData.js#L145
Since: 3.0.0
renderOrder ​
renderOrder: string ​
Description:
Determines the draw order of tilemap. Default is right-down
0, or 'right-down'
1, or 'left-down'
2, or 'right-up'
3, or 'left-up'
Source: src/tilemaps/mapdata/MapData.js#L122
Since: 3.12.0
staggerAxis ​
staggerAxis: string ​
Description:
The Stagger Axis as defined in Tiled.
Only used for hexagonal orientation Tilemaps.
Source: src/tilemaps/mapdata/MapData.js#L234
Since: 3.60.0
staggerIndex ​
staggerIndex: string ​
Description:
The Stagger Index as defined in Tiled.
Either 'odd' or 'even'.
Only used for hexagonal orientation Tilemaps.
Source: src/tilemaps/mapdata/MapData.js#L245
Since: 3.60.0
tileHeight ​
tileHeight: number ​
Description:
The height of the tiles.
Source: src/tilemaps/mapdata/MapData.js#L77
Since: 3.0.0
tiles ​
tiles: array ​
Description:
An array of tile instances.
Source: src/tilemaps/mapdata/MapData.js#L214
Since: 3.0.0
tilesets ​
tilesets: Array.< Phaser.Tilemaps.Tileset > ​
Description:
An array of Tilesets.
Source: src/tilemaps/mapdata/MapData.js#L196
Since: 3.0.0
tileWidth ​
tileWidth: number ​
Description:
The width of the tiles.
Source: src/tilemaps/mapdata/MapData.js#L68
Since: 3.0.0
version ​
version: string ​
Description:
The version of the map data (as specified in Tiled).
Source: src/tilemaps/mapdata/MapData.js#L136
Since: 3.0.0
width ​
width: number ​
Description:
The width of the entire tilemap.
Source: src/tilemaps/mapdata/MapData.js#L41
Since: 3.0.0
widthInPixels ​
widthInPixels: number ​
Description:
The width in pixels of the entire tilemap.
Source: src/tilemaps/mapdata/MapData.js#L86
Since: 3.0.0
Previous
LayerData
Next
ObjectHelper
Public Members
collision
format
height
heightInPixels
hexSideLength
imageCollections
images
infinite
layers
name
objects
orientation
properties
renderOrder
staggerAxis
staggerIndex
tileHeight
tiles
tilesets
tileWidth
version
width
widthInPixels
