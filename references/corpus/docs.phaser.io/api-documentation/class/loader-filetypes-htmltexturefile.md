# HTMLTextureFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-htmltexturefile

Phaser API Documentation
Class
HTMLTextureFile
Version: Phaser v3.90.0
On this page
HTMLTextureFile
A single HTML File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#htmlTexture method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#htmlTexture.
Constructor
new HTMLTextureFile(loader, key, [url], [width], [height], [xhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig No The key to use for this file, or a file configuration object.
url string Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.png , i.e. if key was "alien" then the URL will be "alien.png".
width number Yes The width of the texture the HTML will be rendered to.
height number Yes The height of the texture the HTML will be rendered to.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/HTMLTextureFile.js#L14
Since: 3.12.0
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
Source: src/loader/filetypes/HTMLTextureFile.js#L138
Since: 3.7.0
onProcess ​
<instance> onProcess() ​
Description:
Called automatically by Loader.nextFile.
This method controls what extra work this File does with its loaded data.
Overrides: Phaser.Loader.File#onProcess
Source: src/loader/filetypes/HTMLTextureFile.js#L77
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
HTMLFile
Next
ImageFile
Inherited Methods
Public Methods
addToCache
onProcess
Inherited Members
