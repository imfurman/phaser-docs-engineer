# AtlasJSONFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-atlasjsonfile

Phaser API Documentation
Class
AtlasJSONFile
Version: Phaser v3.90.0
On this page
AtlasJSONFile
A single JSON based Texture Atlas File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#atlas method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#atlas.
https://www.codeandweb.com/texturepacker/tutorials/how-to-create-sprite-sheets-for-phaser3?source=photonstorm
Constructor
new AtlasJSONFile(loader, key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.AtlasJSONFileConfig No The key to use for this file, or a file configuration object.
textureURL string | Array.<string> Yes The absolute or relative URL to load the texture image file from. If undefined or null it will be set to <key>.png , i.e. if key was "alien" then the URL will be "alien.png".
atlasURL object | string Yes The absolute or relative URL to load the texture atlas json data file from. If undefined or null it will be set to <key>.json , i.e. if key was "alien" then the URL will be "alien.json". Or, a well formed JSON object.
textureXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the atlas image file. Used in replacement of the Loaders default XHR Settings.
atlasXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the atlas json file. Used in replacement of the Loaders default XHR Settings.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/AtlasJSONFile.js#L15
Since: 3.0.0
Inherited Methods ​
From Phaser.Loader.MultiFile :
addToMultiFile
destroy
isReadyToProcess
onFileComplete
onFileFailed
pendingDestroy
Public Methods ​
addToCache ​
<instance> addToCache() ​
Description:
Adds this file to its target cache upon successful loading and processing.
Source: src/loader/filetypes/AtlasJSONFile.js#L87
Since: 3.7.0
Inherited Members ​
From Phaser.Loader.MultiFile :
baseURL
complete
config
failed
files
key
loader
path
pending
prefix
state
type
Previous
AsepriteFile
Next
AtlasXMLFile
Inherited Methods
Public Methods
addToCache
Inherited Members
