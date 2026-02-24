# TextureSource | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/textures-texturesource

Phaser API Documentation
Class
TextureSource
Version: Phaser v3.90.0
On this page
TextureSource
A Texture Source is the encapsulation of the actual source data for a Texture.
This is typically an Image Element, loaded from the file system or network, a Canvas Element or a Video Element.
A Texture can contain multiple Texture Sources, which only happens when a multi-atlas is loaded.
Constructor
new TextureSource(texture, source, [width], [height], [flipY])
Parameters
name type optional default description
texture Phaser.Textures.Texture No The Texture this TextureSource belongs to.
source HTMLImageElement | HTMLCanvasElement HTMLVideoElement Phaser.GameObjects.RenderTexture Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper
width number Yes Optional width of the source image. If not given it's derived from the source itself.
height number Yes Optional height of the source image. If not given it's derived from the source itself.
flipY boolean Yes false Sets the UNPACK_FLIP_Y_WEBGL flag the WebGL Texture uses during upload.
Scope : static
Source: src/textures/TextureSource.js#L13
Since: 3.0.0
Public Members ​
compressionAlgorithm ​
compressionAlgorithm: number ​
Description:
Holds the compressed textured algorithm, or null if it's not a compressed texture.
Prior to Phaser 3.60 this value always held null .
Source: src/textures/TextureSource.js#L84
Since: 3.0.0
flipY ​
flipY: boolean ​
Description:
Sets the UNPACK_FLIP_Y_WEBGL flag the WebGL Texture uses during upload.
Source: src/textures/TextureSource.js#L193
Since: 3.20.0
glTexture ​
glTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper ​
Description:
The wrapped WebGL Texture of the source image.
If this TextureSource is driven from a WebGLTexture already,
then this wrapper contains a reference to that WebGLTexture.
Source: src/textures/TextureSource.js#L181
Since: 3.0.0
height ​
height: number ​
Description:
The height of the source image. If not specified in the constructor it will check
the naturalHeight and then height properties of the source image.
Source: src/textures/TextureSource.js#L116
Since: 3.0.0
image ​
image: HTMLImageElement, HTMLCanvasElement, HTMLVideoElement, Uint8Array ​
Description:
The image data.
This is either an Image element, Canvas element, Video Element, or Uint8Array.
Source: src/textures/TextureSource.js#L73
Since: 3.0.0
isCanvas ​
isCanvas: boolean ​
Description:
Is the source image a Canvas Element?
Source: src/textures/TextureSource.js#L136
Since: 3.0.0
isGLTexture ​
isGLTexture: boolean ​
Description:
Is the source image a WebGLTextureWrapper?
Source: src/textures/TextureSource.js#L163
Since: 3.19.0
isPowerOf2 ​
isPowerOf2: boolean ​
Description:
Are the source image dimensions a power of two?
Source: src/textures/TextureSource.js#L172
Since: 3.0.0
isRenderTexture ​
isRenderTexture: boolean ​
Description:
Is the source image a Render Texture?
Source: src/textures/TextureSource.js#L154
Since: 3.12.0
isVideo ​
isVideo: boolean ​
Description:
Is the source image a Video Element?
Source: src/textures/TextureSource.js#L145
Since: 3.20.0
renderer ​
renderer: Phaser.Renderer.Canvas.CanvasRenderer , Phaser.Renderer.WebGL.WebGLRenderer ​
Description:
A reference to the Canvas or WebGL Renderer.
Source: src/textures/TextureSource.js#L42
Since: 3.7.0
resolution ​
resolution: number ​
Description:
The resolution of the source image.
Source: src/textures/TextureSource.js#L96
Since: 3.0.0
scaleMode ​
scaleMode: number ​
Description:
The Scale Mode the image will use when rendering.
Either Linear or Nearest.
Source: src/textures/TextureSource.js#L126
Since: 3.0.0
source ​
source: HTMLImageElement, HTMLCanvasElement, HTMLVideoElement, Phaser.GameObjects.RenderTexture , Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper , Phaser.Types.Textures.CompressedTextureData , Phaser.Textures.DynamicTexture ​
Description:
The source of the image data.
This is either an Image Element, a Canvas Element, a Video Element, a RenderTexture or a WebGLTextureWrapper.
In Phaser 3.60 and above it can also be a Compressed Texture data object.
Source: src/textures/TextureSource.js#L60
Since: 3.12.0
texture ​
texture: Phaser.Textures.Texture ​
Description:
The Texture this TextureSource instance belongs to.
Source: src/textures/TextureSource.js#L51
Since: 3.0.0
width ​
width: number ​
Description:
The width of the source image. If not specified in the constructor it will check
the naturalWidth and then width properties of the source image.
Source: src/textures/TextureSource.js#L106
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Texture Source and nulls the references.
Source: src/textures/TextureSource.js#L341
Since: 3.0.0
init ​
<instance> init(game) ​
Description:
Creates a WebGL Texture, if required, and sets the Texture filter mode.
Parameters:
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Source: src/textures/TextureSource.js#L205
Since: 3.0.0
setFilter ​
<instance> setFilter(filterMode) ​
Description:
Sets the Filter Mode for this Texture.
The mode can be either Linear, the default, or Nearest.
For pixel-art you should use Nearest.
Parameters:
name type optional description
filterMode Phaser.Textures.FilterMode No The Filter Mode.
Source: src/textures/TextureSource.js#L275
Since: 3.0.0
setFlipY ​
<instance> setFlipY([value]) ​
Description:
Sets the UNPACK_FLIP_Y_WEBGL flag for the WebGL Texture during texture upload.
Parameters:
name type optional default description
value boolean Yes true Should the WebGL Texture be flipped on the Y axis on texture upload or not?
Source: src/textures/TextureSource.js#L297
Since: 3.20.0
update ​
<instance> update() ​
Description:
If this TextureSource is backed by a Canvas and is running under WebGL,
it updates the WebGLTexture using the canvas data.
Source: src/textures/TextureSource.js#L317
Since: 3.7.0
Previous
TextureManager
Next
ImageCollection
Public Members
compressionAlgorithm
flipY
glTexture
height
image
isCanvas
isGLTexture
isPowerOf2
isRenderTexture
isVideo
renderer
resolution
scaleMode
source
texture
width
Public Methods
destroy
init
setFilter
setFlipY
update
