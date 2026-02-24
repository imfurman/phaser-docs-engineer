# MultiAtlasFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-multiatlasfile

Phaser API Documentation
Class
MultiAtlasFile
Version: Phaser v3.90.0
On this page
MultiAtlasFile
A single Multi Texture Atlas File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#multiatlas method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#multiatlas.
Constructor
new MultiAtlasFile(loader, key, [atlasURL], [path], [baseURL], [atlasXhrSettings], [textureXhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig No The key of the file. Must be unique within both the Loader and the Texture Manager. Or a config object.
atlasURL string Yes The absolute or relative URL to load the multi atlas json file from.
path string Yes Optional path to use when loading the textures defined in the atlas data.
baseURL string Yes Optional Base URL to use when loading the textures defined in the atlas data.
atlasXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for the atlas json file.
textureXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for the texture files.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/MultiAtlasFile.js#L15
Since: 3.7.0
Inherited Methods ​
From Phaser.Loader.MultiFile :
addToMultiFile
destroy
isReadyToProcess
onFileFailed
pendingDestroy
Public Methods ​
addToCache ​
<instance> addToCache() ​
Description:
Adds this file to its target cache upon successful loading and processing.
Source: src/loader/filetypes/MultiAtlasFile.js#L148
Since: 3.7.0
onFileComplete ​
<instance> onFileComplete(file) ​
Description:
Called by each File when it finishes loading.
Parameters:
name type optional description
file Phaser.Loader.File No The File that has completed processing.
Overrides: Phaser.Loader.MultiFile#onFileComplete
Source: src/loader/filetypes/MultiAtlasFile.js#L75
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
JSONFile
Next
MultiScriptFile
Inherited Methods
Public Methods
addToCache
onFileComplete
Inherited Members
