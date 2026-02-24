# WebGLBufferWrapper | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-wrappers-webglbufferwrapper

Phaser API Documentation
Class
WebGLBufferWrapper
Version: Phaser v3.90.0
On this page
WebGLBufferWrapper
Wrapper for a WebGL buffer, containing all the information that was used
to create it. This can be a VertexBuffer or IndexBuffer.
A WebGLBuffer should never be exposed outside the WebGLRenderer, so the
WebGLRenderer can handle context loss and other events without other
systems having to be aware of it. Always use WebGLBufferWrapper instead.
Constructor
new WebGLBufferWrapper(gl, initialDataOrSize, bufferType, bufferUsage)
Parameters
name type optional description
gl WebGLRenderingContext No The WebGLRenderingContext to create the WebGLBuffer for.
initialDataOrSize ArrayBuffer | number No Either an ArrayBuffer of data, or the size of the buffer to create.
bufferType GLenum No The type of the buffer being created.
bufferUsage GLenum No The usage of the buffer being created. gl.DYNAMIC_DRAW, gl.STATIC_DRAW or gl.STREAM_DRAW.
Scope : static
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L9
Since: 3.80.0
Public Members ​
bufferType ​
bufferType: GLenum ​
Description:
The type of the buffer.
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L68
Since: 3.80.0
bufferUsage ​
bufferUsage: GLenum ​
Description:
The usage of the buffer. gl.DYNAMIC_DRAW, gl.STATIC_DRAW or gl.STREAM_DRAW.
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L77
Since: 3.80.0
gl ​
gl: WebGLRenderingContext ​
Description:
The WebGLRenderingContext that owns this WebGLBuffer.
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L48
Since: 3.80.0
initialDataOrSize ​
initialDataOrSize: ArrayBuffer, number ​
Description:
The initial data or size of the buffer.
Note that this will be used to recreate the buffer if the WebGL context is lost.
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L57
Since: 3.80.0
webGLBuffer ​
webGLBuffer: WebGLBuffer ​
Description:
The WebGLBuffer being wrapped by this class.
This property could change at any time.
Therefore, you should never store a reference to this value.
It should only be passed directly to the WebGL API for drawing.
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L34
Since: 3.80.0
Public Methods ​
createResource ​
<instance> createResource() ​
Description:
Creates a WebGLBuffer for this WebGLBufferWrapper.
This is called automatically by the constructor. It may also be
called again if the WebGLBuffer needs re-creating.
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L89
Since: 3.80.0
destroy ​
<instance> destroy() ​
Description:
Remove this WebGLBufferWrapper from the GL context.
Source: src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L124
Since: 3.80.0
Previous
WebGLAttribLocationWrapper
Next
WebGLFramebufferWrapper
Public Members
bufferType
bufferUsage
gl
initialDataOrSize
webGLBuffer
Public Methods
createResource
destroy
