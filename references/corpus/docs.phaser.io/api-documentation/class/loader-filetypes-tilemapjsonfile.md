# TilemapJSONFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-tilemapjsonfile

Phaser API Documentation
Class
TilemapJSONFile
Version: Phaser v3.90.0
On this page
TilemapJSONFile
A single Tiled Tilemap JSON File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#tilemapTiledJSON method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#tilemapTiledJSON.
Constructor
new TilemapJSONFile(loader, key, [url], [xhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig No The key to use for this file, or a file configuration object.
url object | string Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.json , i.e. if key was "alien" then the URL will be "alien.json". Or, a well formed JSON object.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.FileTypes.JSONFile
Source: src/loader/filetypes/TilemapJSONFile.js#L12
Since: 3.0.0
Inherited Methods ​
From Phaser.Loader.File :
destroy
hasCacheConflict
load
onBase64Load
onError
onLoad
onProcessComplete
onProcessError
onProgress
pendingDestroy
resetXHR
setLink
From Phaser.Loader.FileTypes.JSONFile :
onProcess
Public Methods ​
addToCache ​
<instance> addToCache() ​
Description:
Adds this file to its target cache upon successful loading and processing.
Overrides: Phaser.Loader.FileTypes.JSONFile#addToCache
Source: src/loader/filetypes/TilemapJSONFile.js#L46
Since: 3.7.0
Inherited Members ​
From Phaser.Loader.File :
base64
bytesLoaded
bytesTotal
cache
config
crossOrigin
data
key
linkFile
loader
multiFile
percentComplete
retryAttempts
src
state
type
url
xhrLoader
xhrSettings
Previous
TilemapImpactFile
Next
UnityAtlasFile
Inherited Methods
Public Methods
addToCache
Inherited Members
