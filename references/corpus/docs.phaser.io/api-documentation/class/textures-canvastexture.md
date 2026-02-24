# CanvasTexture | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/textures-canvastexture

Phaser API Documentation
Class
CanvasTexture
Version: Phaser v3.90.0
On this page
CanvasTexture
A Canvas Texture is a special kind of Texture that is backed by an HTML Canvas Element as its source.
You can use the properties of this texture to draw to the canvas element directly, using all of the standard
canvas operations available in the browser. Any Game Object can be given this texture and will render with it.
Note: When running under WebGL the Canvas Texture needs to re-generate its base WebGLTexture and reupload it to
the GPU every time you modify it, otherwise the changes you make to this texture will not be visible. To do this
you should call CanvasTexture.refresh() once you are finished with your changes to the canvas. Try and keep
this to a minimum, especially on large canvas sizes, or you may inadvertently thrash the GPU by constantly uploading
texture data to it. This restriction does not apply if using the Canvas Renderer.
It starts with only one frame that covers the whole of the canvas. You can add further frames, that specify
sections of the canvas using the add method.
Should you need to resize the canvas use the setSize method so that it accurately updates all of the underlying
texture data as well. Forgetting to do this (i.e. by changing the canvas size directly from your code) could cause
graphical errors.
Constructor
new CanvasTexture(manager, key, source, width, height)
Parameters
name type optional description
manager Phaser.Textures.TextureManager No A reference to the Texture Manager this Texture belongs to.
key string No The unique string-based key of this Texture.
source HTMLCanvasElement No The canvas element that is used as the base of this texture.
width number No The width of the canvas.
height number No The height of the canvas.
Scope : static
Extends
Phaser.Textures.Texture
Source: src/textures/CanvasTexture.js#L14
Since: 3.7.0
Inherited Members ​
From Phaser.Textures.Texture :
customData
dataSource
firstFrame
frames
frameTotal
key
manager
source
Public Members ​
buffer ​
buffer: ArrayBuffer ​
Description:
An ArrayBuffer the same size as the context ImageData.
Source: src/textures/CanvasTexture.js#L145
Since: 3.13.0
canvas ​
canvas: HTMLCanvasElement ​
Description:
The source Canvas Element.
Source: src/textures/CanvasTexture.js#L68
Since: 3.7.0
context ​
context: CanvasRenderingContext2D ​
Description:
The 2D Canvas Rendering Context.
Source: src/textures/CanvasTexture.js#L78
Since: 3.7.0
data ​
data: Uint8ClampedArray ​
Description:
A Uint8ClampedArray view into the buffer .
Use the update method to populate this when the canvas changes.
Note that this is unavailable in some browsers, such as Epic Browser, due to their security restrictions.
Source: src/textures/CanvasTexture.js#L120
Since: 3.13.0
height ​
height: number ​
Description:
The height of the Canvas.
This property is read-only, if you wish to change it use the setSize method.
Source: src/textures/CanvasTexture.js#L99
Since: 3.7.0
imageData ​
imageData: ImageData ​
Description:
The context image data.
Use the update method to populate this when the canvas changes.
Source: src/textures/CanvasTexture.js#L110
Since: 3.13.0
pixels ​
pixels: Uint32Array ​
Description:
An Uint32Array view into the buffer .
Source: src/textures/CanvasTexture.js#L136
Since: 3.13.0
width ​
width: number ​
Description:
The width of the Canvas.
This property is read-only, if you wish to change it use the setSize method.
Source: src/textures/CanvasTexture.js#L88
Since: 3.7.0
Inherited Methods ​
From Phaser.Textures.Texture :
add
get
getDataSourceImage
getFrameBounds
getFrameNames
getFramesFromTextureSource
getSourceImage
getTextureSourceIndex
has
remove
setDataSource
setFilter
Public Methods ​
clear ​
<instance> clear([x], [y], [width], [height], [update]) ​
Description:
Clears the given region of this Canvas Texture, resetting it back to transparent.
If no region is given, the whole Canvas Texture is cleared.
Parameters:
name type optional default description
x number Yes 0 The x coordinate of the top-left of the region to clear.
y number Yes 0 The y coordinate of the top-left of the region to clear.
width number Yes The width of the region.
height number Yes The height of the region.
update boolean Yes true Update the internal ImageData buffer and arrays.
Returns: Phaser.Textures.CanvasTexture - The Canvas Texture.
Source: src/textures/CanvasTexture.js#L554
Since: 3.7.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Texture and releases references to its sources and frames.
Overrides: Phaser.Textures.Texture#destroy
Source: src/textures/CanvasTexture.js#L626
Since: 3.16.0
draw ​
<instance> draw(x, y, source, [update]) ​
Description:
Draws the given Image or Canvas element to this CanvasTexture, then updates the internal
ImageData buffer and arrays.
Parameters:
name type optional default description
x number No The x coordinate to draw the source at.
y number No The y coordinate to draw the source at.
source HTMLImageElement | HTMLCanvasElement No The element to draw to this canvas.
update boolean Yes true Update the internal ImageData buffer and arrays.
Returns: Phaser.Textures.CanvasTexture - This CanvasTexture.
Source: src/textures/CanvasTexture.js#L213
Since: 3.13.0
drawFrame ​
<instance> drawFrame(key, [frame], [x], [y], [update]) ​
Description:
Draws the given texture frame to this CanvasTexture, then updates the internal
ImageData buffer and arrays.
Parameters:
name type optional default description
key string No The unique string-based key of the Texture.
frame string | number Yes The string-based name, or integer based index, of the Frame to get from the Texture.
x number Yes 0 The x coordinate to draw the source at.
y number Yes 0 The y coordinate to draw the source at.
update boolean Yes true Update the internal ImageData buffer and arrays.
Returns: Phaser.Textures.CanvasTexture - This CanvasTexture.
Source: src/textures/CanvasTexture.js#L241
Since: 3.16.0
getCanvas ​
<instance> getCanvas() ​
Description:
Gets the Canvas Element.
Returns: HTMLCanvasElement - The Canvas DOM element this texture is using.
Source: src/textures/CanvasTexture.js#L528
Since: 3.7.0
getContext ​
<instance> getContext() ​
Description:
Gets the 2D Canvas Rendering Context.
Returns: CanvasRenderingContext2D - The Canvas Rendering Context this texture is using.
Source: src/textures/CanvasTexture.js#L541
Since: 3.7.0
getData ​
<instance> getData(x, y, width, height) ​
Description:
Gets an ImageData region from this CanvasTexture from the position and size specified.
You can write this back using CanvasTexture.putData , or manipulate it.
Parameters:
name type optional description
x number No The x coordinate of the top-left of the area to get the ImageData from. Must lay within the dimensions of this CanvasTexture and be an integer.
y number No The y coordinate of the top-left of the area to get the ImageData from. Must lay within the dimensions of this CanvasTexture and be an integer.
width number No The width of the rectangle from which the ImageData will be extracted. Positive values are to the right, and negative to the left.
height number No The height of the rectangle from which the ImageData will be extracted. Positive values are down, and negative are up.
Returns: ImageData - The ImageData extracted from this CanvasTexture.
Source: src/textures/CanvasTexture.js#L360
Since: 3.16.0
getIndex ​
<instance> getIndex(x, y) ​
Description:
Returns the Image Data index for the given pixel in this CanvasTexture.
The index can be used to read directly from the this.data array.
The index points to the red value in the array. The subsequent 3 indexes
point to green, blue and alpha respectively.
Parameters:
name type optional description
x number No The x coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer.
y number No The y coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer.
Returns: number - undefined
Source: src/textures/CanvasTexture.js#L480
Since: 3.16.0
getPixel ​
<instance> getPixel(x, y, [out]) ​
Description:
Get the color of a specific pixel from this texture and store it in a Color object.
If you have drawn anything to this CanvasTexture since it was created you must call CanvasTexture.update to refresh the array buffer,
otherwise this may return out of date color values, or worse - throw a run-time error as it tries to access an array element that doesn't exist.
Parameters:
name type optional description
x number No The x coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer.
y number No The y coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer.
out Phaser.Display.Color Yes A Color object to store the pixel values in. If not provided a new Color object will be created.
Returns: Phaser.Display.Color - An object with the red, green, blue and alpha values set in the r, g, b and a properties.
Source: src/textures/CanvasTexture.js#L386
Since: 3.13.0
getPixels ​
<instance> getPixels([x], [y], [width], [height]) ​
Description:
Returns an array containing all of the pixels in the given region.
If the requested region extends outside the bounds of this CanvasTexture,
the region is truncated to fit.
If you have drawn anything to this CanvasTexture since it was created you must call CanvasTexture.update to refresh the array buffer,
otherwise this may return out of date color values, or worse - throw a run-time error as it tries to access an array element that doesn't exist.
Parameters:
name type optional default description
x number Yes 0 The x coordinate of the top-left of the region. Must lay within the dimensions of this CanvasTexture and be an integer.
y number Yes 0 The y coordinate of the top-left of the region. Must lay within the dimensions of this CanvasTexture and be an integer.
width number Yes The width of the region to get. Must be an integer. Defaults to the canvas width if not given.
height number Yes The height of the region to get. Must be an integer. If not given will be set to the width .
Returns: Array.<Array.< Phaser.Types.Textures.PixelConfig >> - A 2d array of Pixel objects.
Source: src/textures/CanvasTexture.js#L425
Since: 3.16.0
putData ​
<instance> putData(imageData, x, y, [dirtyX], [dirtyY], [dirtyWidth], [dirtyHeight]) ​
Description:
Puts the ImageData into the context of this CanvasTexture at the given coordinates.
Parameters:
name type optional default description
imageData ImageData No The ImageData to put at the given location.
x number No The x coordinate to put the imageData. Must lay within the dimensions of this CanvasTexture and be an integer.
y number No The y coordinate to put the imageData. Must lay within the dimensions of this CanvasTexture and be an integer.
dirtyX number Yes 0 Horizontal position (x coordinate) of the top-left corner from which the image data will be extracted.
dirtyY number Yes 0 Vertical position (x coordinate) of the top-left corner from which the image data will be extracted.
dirtyWidth number Yes Width of the rectangle to be painted. Defaults to the width of the image data.
dirtyHeight number Yes Height of the rectangle to be painted. Defaults to the height of the image data.
Returns: Phaser.Textures.CanvasTexture - This CanvasTexture.
Source: src/textures/CanvasTexture.js#L332
Since: 3.16.0
refresh ​
<instance> refresh() ​
Description:
This should be called manually if you are running under WebGL.
It will refresh the WebGLTexture from the Canvas source. Only call this if you know that the
canvas has changed, as there is a significant GPU texture allocation cost involved in doing so.
Returns: Phaser.Textures.CanvasTexture - This CanvasTexture.
Source: src/textures/CanvasTexture.js#L511
Since: 3.7.0
setPixel ​
<instance> setPixel(x, y, red, green, blue, [alpha]) ​
Description:
Sets a pixel in the CanvasTexture to the given color and alpha values.
This is an expensive operation to run in large quantities, so use sparingly.
Parameters:
name type optional default description
x number No The x coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer.
y number No The y coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer.
red number No The red color value. A number between 0 and 255.
green number No The green color value. A number between 0 and 255.
blue number No The blue color value. A number between 0 and 255.
alpha number Yes 255 The alpha value. A number between 0 and 255.
Returns: Phaser.Textures.CanvasTexture - This CanvasTexture.
Source: src/textures/CanvasTexture.js#L291
Since: 3.16.0
setSize ​
<instance> setSize(width, [height]) ​
Description:
Changes the size of this Canvas Texture.
Parameters:
name type optional description
width number No The new width of the Canvas.
height number Yes The new height of the Canvas. If not given it will use the width as the height.
Returns: Phaser.Textures.CanvasTexture - The Canvas Texture.
Source: src/textures/CanvasTexture.js#L587
Since: 3.7.0
update ​
<instance> update() ​
Description:
This re-creates the imageData from the current context.
It then re-builds the ArrayBuffer, the data Uint8ClampedArray reference and the pixels Int32Array.
Warning: This is a very expensive operation, so use it sparingly.
Returns: Phaser.Textures.CanvasTexture - This CanvasTexture.
Source: src/textures/CanvasTexture.js#L173
Since: 3.13.0
Previous
Size
Next
DynamicTexture
Inherited Members
Public Members
buffer
canvas
context
data
height
imageData
pixels
width
Inherited Methods
Public Methods
clear
destroy
draw
drawFrame
getCanvas
getContext
getData
getIndex
getPixel
getPixels
putData
refresh
setPixel
setSize
update
