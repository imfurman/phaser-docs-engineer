# HTML5AudioFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-html5audiofile

Phaser API Documentation
Class
HTML5AudioFile
Version: Phaser v3.90.0
On this page
HTML5AudioFile
A single Audio File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#audio method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#audio.
Constructor
new HTML5AudioFile(loader, key, [urlConfig], [xhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.AudioFileConfig No The key to use for this file, or a file configuration object.
urlConfig string Yes The absolute or relative URL to load this file from.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/HTML5AudioFile.js#L14
Since: 3.0.0
Inherited Methods ​
From Phaser.Loader.File :
addToCache
destroy
hasCacheConflict
onBase64Load
onProcess
onProcessComplete
onProcessError
pendingDestroy
resetXHR
setLink
Public Methods ​
load ​
<instance> load() ​
Description:
Called by the Loader, starts the actual file downloading.
During the load the methods onLoad, onError and onProgress are called, based on the XHR events.
You shouldn't normally call this method directly, it's meant to be invoked by the Loader.
Overrides: Phaser.Loader.File#load
Source: src/loader/filetypes/HTML5AudioFile.js#L130
Since: 3.0.0
onError ​
<instance> onError() ​
Description:
Called if the file errors while loading.
Overrides: Phaser.Loader.File#onError
Source: src/loader/filetypes/HTML5AudioFile.js#L85
Since: 3.0.0
onLoad ​
<instance> onLoad() ​
Description:
Called when the file finishes loading.
Overrides: Phaser.Loader.File#onLoad
Source: src/loader/filetypes/HTML5AudioFile.js#L67
Since: 3.0.0
onProgress ​
<instance> onProgress() ​
Description:
Called during the file load progress. Is sent a DOM ProgressEvent.
Overrides: Phaser.Loader.File#onProgress
Fires: Phaser.Loader.Events#event:FILE_PROGRESS
Source: src/loader/filetypes/HTML5AudioFile.js#L104
Since: 3.0.0
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
GLSLFile
Next
HTMLFile
Inherited Methods
Public Methods
load
onError
onLoad
onProgress
Inherited Members
