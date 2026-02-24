# WebGLFramebufferWrapper | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-wrappers-webglframebufferwrapper

Phaser API Documentation
Class
WebGLFramebufferWrapper
Version: Phaser v3.90.0
On this page
WebGLFramebufferWrapper
Wrapper for a WebGL frame buffer,
containing all the information that was used to create it.
A WebGLFramebuffer should never be exposed outside the WebGLRenderer,
so the WebGLRenderer can handle context loss and other events
without other systems having to be aware of it.
Always use WebGLFramebufferWrapper instead.
Constructor
new WebGLFramebufferWrapper(gl, width, height, renderTexture, [addDepthStencilBuffer])
Parameters
name type optional default description
gl WebGLRenderingContext No The WebGLRenderingContext to create the WebGLFramebuffer for.
width number No If addDepthStencilBuffer is true, this controls the width of the depth stencil.
height number No If addDepthStencilBuffer is true, this controls the height of the depth stencil.
renderTexture Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper No The color texture where the color pixels are written.
addDepthStencilBuffer boolean Yes false Create a Renderbuffer for the depth stencil?
Scope : static
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L20
Since: 3.80.0
Public Members ​
addDepthStencilBuffer ​
addDepthStencilBuffer: boolean ​
Description:
Create a Renderbuffer for the depth stencil?
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L97
Since: 3.80.0
gl ​
gl: WebGLRenderingContext ​
Description:
The WebGL context this WebGLFramebuffer belongs to.
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L61
Since: 3.80.0
height ​
height: number ​
Description:
Height of the depth stencil.
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L79
Since: 3.80.0
renderTexture ​
renderTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper ​
Description:
The color texture where the color pixels are written.
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L88
Since: 3.80.0
webGLFramebuffer ​
webGLFramebuffer: WebGLFramebuffer ​
Description:
The WebGLFramebuffer being wrapped by this class.
This property could change at any time.
Therefore, you should never store a reference to this value.
It should only be passed directly to the WebGL API for drawing.
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L47
Since: 3.80.0
width ​
width: number ​
Description:
Width of the depth stencil.
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L70
Since: 3.80.0
Public Methods ​
createResource ​
<instance> createResource() ​
Description:
Creates a WebGLFramebuffer from the given parameters.
This is called automatically by the constructor. It may also be
called again if the WebGLFramebuffer needs re-creating.
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L110
Since: 3.80.0
destroy ​
<instance> destroy() ​
Description:
Destroys this WebGLFramebufferWrapper.
Source: src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L161
Since: 3.80.0
Previous
WebGLBufferWrapper
Next
WebGLProgramWrapper
Public Members
addDepthStencilBuffer
gl
height
renderTexture
webGLFramebuffer
width
Public Methods
createResource
destroy
