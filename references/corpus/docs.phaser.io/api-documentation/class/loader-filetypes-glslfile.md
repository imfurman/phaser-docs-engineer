# GLSLFile | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/loader-filetypes-glslfile

Phaser API Documentation
Class
GLSLFile
Version: Phaser v3.90.0
On this page
GLSLFile
A single GLSL File suitable for loading by the Loader.
These are created when you use the Phaser.Loader.LoaderPlugin#glsl method and are not typically created directly.
For documentation about what all the arguments and configuration options mean please see Phaser.Loader.LoaderPlugin#glsl.
Constructor
new GLSLFile(loader, key, [url], [shaderType], [xhrSettings])
Parameters
name type optional default description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader that is responsible for this file.
key string | Phaser.Types.Loader.FileTypes.GLSLFileConfig No The key to use for this file, or a file configuration object.
url string Yes The absolute or relative URL to load this file from. If undefined or null it will be set to <key>.txt , i.e. if key was "alien" then the URL will be "alien.txt".
shaderType string Yes "'fragment'" The type of shader. Either fragment for a fragment shader, or vertex for a vertex shader. This is ignored if you load a shader bundle.
xhrSettings Phaser.Types.Loader.XHRSettingsObject Yes Extra XHR Settings specifically for this file.
Scope : static
Extends
Phaser.Loader.File
Source: src/loader/filetypes/GLSLFile.js#L15
Since: 3.0.0
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
Source: src/loader/filetypes/GLSLFile.js#L92
Since: 3.17.0
getShaderName ​
<instance> getShaderName(headerSource) ​
Description:
Returns the name of the shader from the header block.
Parameters:
name type optional description
headerSource Array.<string> No The header data.
Returns: string - The shader name.
Source: src/loader/filetypes/GLSLFile.js#L155
Since: 3.17.0
getShaderType ​
<instance> getShaderType(headerSource) ​
Description:
Returns the type of the shader from the header block.
Parameters:
name type optional description
headerSource Array.<string> No The header data.
Returns: string - The shader type. Either 'fragment' or 'vertex'.
Source: src/loader/filetypes/GLSLFile.js#L180
Since: 3.17.0
getShaderUniforms ​
<instance> getShaderUniforms(headerSource) ​
Description:
Returns the shader uniforms from the header block.
Parameters:
name type optional description
headerSource Array.<string> No The header data.
Returns: any - The shader uniforms object.
Source: src/loader/filetypes/GLSLFile.js#L205
Since: 3.17.0
onProcess ​
<instance> onProcess() ​
Description:
Called automatically by Loader.nextFile.
This method controls what extra work this File does with its loaded data.
Overrides: Phaser.Loader.File#onProcess
Source: src/loader/filetypes/GLSLFile.js#L76
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
FontFile
Next
HTML5AudioFile
Inherited Methods
Public Methods
addToCache
getShaderName
getShaderType
getShaderUniforms
onProcess
Inherited Members
