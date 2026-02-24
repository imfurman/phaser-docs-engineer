# MultiScriptFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-multiscriptfile

Phaser API Documentation
Class
MultiScriptFile
Version: Phaser v3.90.0
On this page
MultiScriptFile
A Multi Script File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#scripts method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#scripts.
Constructor
new MultiScriptFile(loader, key, [url], [xhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.MultiScriptFileConfig No The key to use for this file, or a file configuration object.
url Array.<string> Yes An array of absolute or relative URLs to load the script files from. They are processed in the order given in the array.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the script files. Used in replacement of the Loaders default XHR Settings.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/MultiScriptFile.js#L14
Since: 3.17.0
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
Source: src/loader/filetypes/MultiScriptFile.js#L80
Since: 3.17.0
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
MultiAtlasFile
Next
OBJFile
Inherited Methods
Public Methods
addToCache
Inherited Members
