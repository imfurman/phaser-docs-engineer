# BitmapFontFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-bitmapfontfile

Phaser API Documentation
Class
BitmapFontFile
Version: Phaser v3.90.0
On this page
BitmapFontFile
A single Bitmap Font based File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#bitmapFont method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#bitmapFont.
Constructor
new BitmapFontFile(loader, key, [textureURL], [fontDataURL], [textureXhrSettings], [fontDataXhrSettings])
Parameters
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.BitmapFontFileConfig No The key to use for this file, or a file configuration object.
textureURL string | Array.<string> Yes The absolute or relative URL to load the font image file from. If undefined or null it will be set to <key>.png , i.e. if key was "alien" then the URL will be "alien.png".
fontDataURL string Yes The absolute or relative URL to load the font xml data file from. If undefined or null it will be set to <key>.xml , i.e. if key was "alien" then the URL will be "alien.xml".
textureXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the font image file. Used in replacement of the Loaders default XHR Settings.
fontDataXhrSettings Phaser.Types.Loader.XHRSettingsObject Yes An XHR Settings configuration object for the font data xml file. Used in replacement of the Loaders default XHR Settings.
Scope : static
Extends
Phaser.Loader.MultiFile
Source: src/loader/filetypes/BitmapFontFile.js#L16
Since: 3.0.0
Inherited Methods ​
From Phaser.Loader.MultiFile :
addToMultiFile
destroy
isReadyToProcess
onFileComplete
onFileFailed
pendingDestroy
Public Methods ​
addToCache ​
<instance> addToCache() ​
Description:
Adds this file to its target cache upon successful loading and processing.
Source: src/loader/filetypes/BitmapFontFile.js#L86
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
BinaryFile
Next
CSSFile
Inherited Methods
Public Methods
addToCache
Inherited Members
