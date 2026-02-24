# WebGLProgramWrapper | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-wrappers-webglprogramwrapper

Phaser API Documentation
Class
WebGLProgramWrapper
Version: Phaser v3.90.0
On this page
WebGLProgramWrapper
Wrapper for a WebGL program, containing all the information that was used to create it.
A WebGLProgram should never be exposed outside the WebGLRenderer, so the WebGLRenderer
can handle context loss and other events without other systems having to be aware of it.
Always use WebGLProgramWrapper instead.
Constructor
new WebGLProgramWrapper(gl, vertexSource, fragmentShader)
Parameters
name type optional description
gl WebGLRenderingContext No The WebGLRenderingContext to create the WebGLProgram for.
vertexSource string No The vertex shader source code as a string.
fragmentShader string No The fragment shader source code as a string.
Scope : static
Source: src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L9
Since: 3.80.0
Public Members ​
fragmentSource ​
fragmentSource: string ​
Description:
The fragment shader source code as a string.
Source: src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L64
Since: 3.80.0
gl ​
gl: WebGLRenderingContext ​
Description:
The WebGLRenderingContext that owns this WebGLProgram.
Source: src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L46
Since: 3.80.0
vertexSource ​
vertexSource: string ​
Description:
The vertex shader source code as a string.
Source: src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L55
Since: 3.80.0
webGLProgram ​
webGLProgram: WebGLProgram ​
Description:
The WebGLProgram being wrapped by this class.
This property could change at any time.
Therefore, you should never store a reference to this value.
It should only be passed directly to the WebGL API for drawing.
Source: src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L32
Since: 3.80.0
Public Methods ​
createResource ​
<instance> createResource() ​
Description:
Creates a WebGLProgram from the given vertex and fragment shaders.
This is called automatically by the constructor. It may also be
called again if the WebGLProgram needs re-creating.
Source: src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L76
Since: 3.80.0
destroy ​
<instance> destroy() ​
Description:
Remove this WebGLProgram from the GL context.
Source: src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L135
Since: 3.80.0
Previous
WebGLFramebufferWrapper
Next
WebGLTextureWrapper
Public Members
fragmentSource
gl
vertexSource
webGLProgram
Public Methods
createResource
destroy
