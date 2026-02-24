# ScriptFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-scriptfile

Phaser API Documentation
Class
ScriptFile
Version: Phaser v3.90.0
On this page
ScriptFile
A single Script File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#script method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#script.
Constructor
new ScriptFile(loader, key, [url], [type], [xhrSettings])
Parameters
name type optional default description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.ScriptFileConfig No The key to use for this file, or a file configuration object.
url string Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.js , i.e. if key was "alien" then the URL will be "alien.js".
type string Yes "'script'" The script type. Should be either 'script' for classic JavaScript, or 'module' if the file contains an exported module.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/ScriptFile.js#L14
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
Source: src/loader/filetypes/ScriptFile.js#L72
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
ScenePluginFile
Next
SpriteSheetFile
Inherited Methods
Public Methods
onProcess
Inherited Members
