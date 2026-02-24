# WebGLUniformLocationWrapper | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/renderer-webgl-wrappers-webgluniformlocationwrapper

Phaser API Documentation
Class
WebGLUniformLocationWrapper
Version: Phaser v3.90.0
On this page
WebGLUniformLocationWrapper
Wrapper for a WebGL uniform location, containing all the information that was used to create it.
A WebGLUniformLocation should never be exposed outside the WebGLRenderer,
so the WebGLRenderer can handle context loss and other events without other systems having to be aware of it.
Always use WebGLUniformLocationWrapper instead.
Constructor
new WebGLUniformLocationWrapper(gl, program, name)
Parameters
name type optional description
gl WebGLRenderingContext No The WebGLRenderingContext to create the WebGLUniformLocation for.
program Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper No The WebGLProgram that this location refers to. This must be created first.
name string No The name of this location, as defined in the shader source code.
Scope : static
Source: src/renderer/webgl/wrappers/WebGLUniformLocationWrapper.js#L9
Since: 3.80.0
Public Members ​
gl ​
gl: WebGLRenderingContext ​
Description:
The WebGLRenderingContext that owns this location.
Source: src/renderer/webgl/wrappers/WebGLUniformLocationWrapper.js#L46
Since: 3.80.0
name ​
name: string ​
Description:
The name of this location, as defined in the shader source code.
Source: src/renderer/webgl/wrappers/WebGLUniformLocationWrapper.js#L64
Since: 3.80.0
program ​
program: Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper ​
Description:
The WebGLProgram that this location refers to.
Source: src/renderer/webgl/wrappers/WebGLUniformLocationWrapper.js#L55
Since: 3.80.0
webGLUniformLocation ​
webGLUniformLocation: WebGLUniformLocation ​
Description:
The WebGLUniformLocation being wrapped by this class.
This property could change at any time.
Therefore, you should never store a reference to this value.
It should only be passed directly to the WebGL API for drawing.
Source: src/renderer/webgl/wrappers/WebGLUniformLocationWrapper.js#L32
Since: 3.80.0
Public Methods ​
createResource ​
<instance> createResource() ​
Description:
Creates the WebGLUniformLocation.
Source: src/renderer/webgl/wrappers/WebGLUniformLocationWrapper.js#L76
Since: 3.80.0
destroy ​
<instance> destroy() ​
Description:
Destroys this WebGLUniformLocationWrapper.
Source: src/renderer/webgl/wrappers/WebGLUniformLocationWrapper.js#L102
Since: 3.80.0
Previous
WebGLTextureWrapper
Next
ScaleManager
Public Members
gl
name
program
webGLUniformLocation
Public Methods
createResource
destroy
