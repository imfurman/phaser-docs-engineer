# AtlasXMLFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-atlasxmlfile

Phaser API Documentation
Class
AtlasXMLFile
Version: Phaser v3.90.0
On this page
AtlasXMLFile
A single XML based Texture Atlas File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#atlasXML method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#atlasXML.
Constructor
new AtlasXMLFile(loader, key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig No The key to use for this file, or a file configuration object.
textureURL string | Array.<string> Yes The absolute or relative URL to load the texture image file from. If undefined or null it will be set to <key>.png , i.e. if key was "alien" then the URL will be "alien.png".
atlasURL string Yes The absolute or relative URL to load the texture atlas xml data file from. If undefined or null it will be set to <key>.xml , i.e. if key was "alien" then the URL will be "alien.xml".
textureXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the atlas image file. Used in replacement of the Loaders default XHR Settings.
atlasXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the atlas xml file. Used in replacement of the Loaders default XHR Settings.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/AtlasXMLFile.js#L15
Since: 3.7.0
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
Source: src/loader/filetypes/AtlasXMLFile.js#L85
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
AtlasJSONFile
Next
AudioFile
Inherited Methods
Public Methods
addToCache
Inherited Members
