# AudioFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-audiofile

Phaser API Documentation
Class
AudioFile
Version: Phaser v3.90.0
On this page
AudioFile
A single Audio File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#audio method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#audio.
Constructor
new AudioFile(loader, key, [urlConfig], [xhrSettings], [audioContext])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.AudioFileConfig No The key to use for this file, or a file configuration object.
urlConfig Phaser.Types.Loader.FileTypes.AudioFileURLConfig Yes The absolute or relative URL to load this file from in a config object.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
audioContext AudioContext Yes The AudioContext this file will use to process itself.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/AudioFile.js#L15
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
Source: src/loader/filetypes/AudioFile.js#L67
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
AtlasXMLFile
Next
AudioSpriteFile
Inherited Methods
Public Methods
onProcess
Inherited Members
