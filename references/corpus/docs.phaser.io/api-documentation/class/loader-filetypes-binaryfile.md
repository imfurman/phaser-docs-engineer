# BinaryFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-binaryfile

Phaser API Documentation
Class
BinaryFile
Version: Phaser v3.90.0
On this page
BinaryFile
A single Binary File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#binary method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#binary.
Constructor
new BinaryFile(loader, key, [url], [xhrSettings], [dataType])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.BinaryFileConfig No The key to use for this file, or a file configuration object.
url string Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.bin , i.e. if key was "alien" then the URL will be "alien.bin".
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
dataType any Yes Optional type to cast the binary file to once loaded. For example, Uint8Array .
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/BinaryFile.js#L14
Since: 3.0.0
Inherited Methods ​
From Phaser.Loader.File :
addToCache
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
Public Methods ​
onProcess ​
<instance> onProcess() ​
Description:
Called automatically by Loader.nextFile.
This method controls what extra work this File does with its loaded data.
Overrides: Phaser.Loader.File#onProcess
Source: src/loader/filetypes/BinaryFile.js#L69
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
AudioSpriteFile
Next
BitmapFontFile
Inherited Methods
Public Methods
onProcess
Inherited Members
