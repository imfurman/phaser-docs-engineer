# CompressedTextureFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-compressedtexturefile

Phaser API Documentation
Class
CompressedTextureFile
Version: Phaser v3.90.0
On this page
CompressedTextureFile
A Compressed Texture File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#texture method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#texture.
Constructor
new CompressedTextureFile(loader, key, entry, [xhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string No The key to use for this file.
entry Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry No The compressed texture file entry to load.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/CompressedTextureFile.js#L22
Since: 3.60.0
Inherited Methods ​
From Phaser.Loader.MultiFile :
addToMultiFile
destroy
isReadyToProcess
onFileFailed
pendingDestroy
Public Methods ​
addMultiToCache ​
<instance> addMultiToCache() ​
Description:
Adds all of the multi-file entties to their target caches upon successful loading and processing.
Source: src/loader/filetypes/CompressedTextureFile.js#L257
Since: 3.60.0
addToCache ​
<instance> addToCache() ​
Description:
Adds this file to its target cache upon successful loading and processing.
Source: src/loader/filetypes/CompressedTextureFile.js#L186
Since: 3.60.0
onFileComplete ​
<instance> onFileComplete(file) ​
Description:
Called by each File when it finishes loading.
Parameters:
name type optional description
file Phaser.Loader.File No The File that has completed processing.
Overrides: Phaser.Loader.MultiFile#onFileComplete
Source: src/loader/filetypes/CompressedTextureFile.js#L97
Since: 3.60.0
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
CSSFile
Next
FontFile
Inherited Methods
Public Methods
addMultiToCache
addToCache
onFileComplete
Inherited Members
