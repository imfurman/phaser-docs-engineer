# VideoFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-videofile

Phaser API Documentation
Class
VideoFile
Version: Phaser v3.90.0
On this page
VideoFile
A single Video File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#video method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#video.
Constructor
new VideoFile(loader, key, [urls], [noAudio])
Parameters
name type optional default description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.VideoFileConfig No The key to use for this file, or a file configuration object.
urls string | Array.<string> Phaser.Types.Loader.FileTypes.VideoFileURLConfig Array.< Phaser.Types.Loader.FileTypes.VideoFileURLConfig > Yes
noAudio boolean Yes false Does the video have an audio track? If not you can enable auto-playing on it.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/VideoFile.js#L15
Since: 3.20.0
Inherited Methods ​
From Phaser.Loader.File :
addToCache
destroy
hasCacheConflict
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
load ​
<instance> load() ​
Description:
Called by the Loader, starts the actual file downloading.
During the load the methods onLoad, onError and onProgress are called, based on the XHR events.
You shouldn't normally call this method directly, it's meant to be invoked by the Loader.
Overrides: Phaser.Loader.File#load
Source: src/loader/filetypes/VideoFile.js#L92
Since: 3.20.0
onProcess ​
<instance> onProcess() ​
Description:
Called automatically by Loader.nextFile.
This method controls what extra work this File does with its loaded data.
Overrides: Phaser.Loader.File#onProcess
Source: src/loader/filetypes/VideoFile.js#L74
Since: 3.20.0
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
UnityAtlasFile
Next
XMLFile
Inherited Methods
Public Methods
load
onProcess
Inherited Members
