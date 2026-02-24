# SceneFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-scenefile

Phaser API Documentation
Class
SceneFile
Version: Phaser v3.90.0
On this page
SceneFile
An external Scene JavaScript File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#sceneFile method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#sceneFile.
Constructor
new SceneFile(loader, key, [url], [xhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.SceneFileConfig No The key to use for this file, or a file configuration object.
url string Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.js , i.e. if key was "alien" then the URL will be "alien.js".
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/SceneFile.js#L14
Since: 3.16.0
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
Source: src/loader/filetypes/SceneFile.js#L81
Since: 3.16.0
onProcess ​
<instance> onProcess() ​
Description:
Called automatically by Loader.nextFile.
This method controls what extra work this File does with its loaded data.
Overrides: Phaser.Loader.File#onProcess
Source: src/loader/filetypes/SceneFile.js#L65
Since: 3.16.0
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
SVGFile
Next
ScenePluginFile
Inherited Methods
Public Methods
addToCache
onProcess
Inherited Members
