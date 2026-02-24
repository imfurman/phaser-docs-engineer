# OBJFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-objfile

Phaser API Documentation
Class
OBJFile
Version: Phaser v3.90.0
On this page
OBJFile
A single Wavefront OBJ File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#obj method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#obj.
Constructor
new OBJFile(loader, key, [objURL], [matURL], [flipUV], [xhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.OBJFileConfig No The key to use for this file, or a file configuration object.
objURL string Yes The absolute or relative URL to load the obj file from. If undefined or null it will be set to <key>.obj , i.e. if key was "alien" then the URL will be "alien.obj".
matURL string Yes The absolute or relative URL to load the material file from. If undefined or null it will be set to <key>.mat , i.e. if key was "alien" then the URL will be "alien.mat".
flipUV boolean Yes Flip the UV coordinates stored in the model data?
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for these files.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/OBJFile.js#L16
Since: 3.50.0
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
Source: src/loader/filetypes/OBJFile.js#L112
Since: 3.50.0
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
MultiScriptFile
Next
PackFile
Inherited Methods
Public Methods
addToCache
Inherited Members
