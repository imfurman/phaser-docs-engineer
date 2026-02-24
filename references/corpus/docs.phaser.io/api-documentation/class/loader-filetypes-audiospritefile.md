# AudioSpriteFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-audiospritefile

Phaser API Documentation
Class
AudioSpriteFile
Version: Phaser v3.90.0
On this page
AudioSpriteFile
An Audio Sprite File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#audioSprite method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#audioSprite.
Constructor
new AudioSpriteFile(loader, key, jsonURL, [audioURL], [audioConfig], [audioXhrSettings], [jsonXhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig No The key to use for this file, or a file configuration object.
jsonURL string No The absolute or relative URL to load the json file from. Or a well formed JSON object to use instead.
audioURL Object Yes The absolute or relative URL to load the audio file from. If empty it will be obtained by parsing the JSON file.
audioConfig any Yes The audio configuration options.
audioXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the audio file. Used in replacement of the Loaders default XHR Settings.
jsonXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the json file. Used in replacement of the Loaders default XHR Settings.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/AudioSpriteFile.js#L15
Since: 3.7.0
Inherited Methods ​
From Phaser.Loader.MultiFile :
addToMultiFile
destroy
isReadyToProcess
onFileFailed
pendingDestroy
Public Methods ​
addToCache ​
<instance> addToCache() ​
Description:
Adds this file to its target cache upon successful loading and processing.
Source: src/loader/filetypes/AudioSpriteFile.js#L121
Since: 3.7.0
onFileComplete ​
<instance> onFileComplete(file) ​
Description:
Called by each File when it finishes loading.
Parameters:
name type optional description
file Phaser.Loader.File No The File that has completed processing.
Overrides: Phaser.Loader.MultiFile#onFileComplete
Source: src/loader/filetypes/AudioSpriteFile.js#L85
Since: 3.7.0
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
AudioFile
Next
BinaryFile
Inherited Methods
Public Methods
addToCache
onFileComplete
Inherited Members
