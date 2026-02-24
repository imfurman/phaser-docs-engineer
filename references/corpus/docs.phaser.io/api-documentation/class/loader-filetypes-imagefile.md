# ImageFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-imagefile

Phaser API Documentation
Class
ImageFile
Version: Phaser v3.90.0
On this page
ImageFile
A single Image File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#image method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#image.
Constructor
new ImageFile(loader, key, [url], [xhrSettings], [frameConfig])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.ImageFileConfig No The key to use for this file, or a file configuration object.
url string | Array.<string> Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.png , i.e. if key was "alien" then the URL will be "alien.png".
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
frameConfig Phaser.Types.Loader.FileTypes.ImageFrameConfig Yes The frame configuration object. Only provided for, and used by, Sprite Sheets.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/ImageFile.js#L15
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
Public Methods ​
addToCache ​
<instance> addToCache() ​
Description:
Adds this file to its target cache upon successful loading and processing.
Overrides: Phaser.Loader.File#addToCache
Source: src/loader/filetypes/ImageFile.js#L189
Since: 3.7.0
onProcess ​
<instance> onProcess() ​
Description:
Called automatically by Loader.nextFile.
This method controls what extra work this File does with its loaded data.
Overrides: Phaser.Loader.File#onProcess
Source: src/loader/filetypes/ImageFile.js#L98
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
HTMLTextureFile
Next
JSONFile
Inherited Methods
Public Methods
addToCache
onProcess
Inherited Members
