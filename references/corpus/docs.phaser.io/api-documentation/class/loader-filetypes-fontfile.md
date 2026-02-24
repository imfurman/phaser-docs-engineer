# FontFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-fontfile

Phaser API Documentation
Class
FontFile
Version: Phaser v3.90.0
On this page
FontFile
A single Font File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#font method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#font.
Constructor
new FontFile(loader, key, [url], [format], [descriptors], [xhrSettings])
Parameters
name type optional default description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.FontFileConfig No The key to use for this file, or a file configuration object.
url string Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.ttf , i.e. if key was "alien" then the URL will be "alien.ttf".
format string Yes "'truetype'" The font type. Should be a string, like 'truetype' or 'opentype'.
descriptors object Yes An optional object containing font descriptors for the Font Face. See https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace#descriptors for more details.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/FontFile.js#L15
Since: 3.87.0
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
Source: src/loader/filetypes/FontFile.js#L82
Since: 3.87.0
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
CompressedTextureFile
Next
GLSLFile
Inherited Methods
Public Methods
onProcess
Inherited Members
