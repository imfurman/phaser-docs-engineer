# Phaser.Renderer.WebGL.Pipelines.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/renderer-webgl-pipelines-events

Phaser API Documentation
Namespaces
Phaser.Renderer.WebGL.Pipelines.Events
Version: Phaser v3.90.0
On this page
Phaser.Renderer.WebGL.Pipelines.Events
Scope: static
Source: src/renderer/webgl/pipelines/events/index.js#L7
Static functions ​
AFTER_FLUSH ​
AFTER_FLUSH ​
Description:
The WebGLPipeline After Flush Event.
This event is dispatched by a WebGLPipeline right after it has issued a drawArrays command
and cleared its vertex count.
Parameters:
name type optional description
pipeline Phaser.Renderer.WebGL.WebGLPipeline No The pipeline that has flushed.
isPostFlush boolean No Was this flush invoked as part of a post-process, or not?
Source: src/renderer/webgl/pipelines/events/AFTER_FLUSH_EVENT.js#L7
Since: 3.50.0
BEFORE_FLUSH ​
BEFORE_FLUSH ​
Description:
The WebGLPipeline Before Flush Event.
This event is dispatched by a WebGLPipeline right before it is about to
flush and issue a bufferData and drawArrays command.
Parameters:
name type optional description
pipeline Phaser.Renderer.WebGL.WebGLPipeline No The pipeline that is about to flush.
isPostFlush boolean No Was this flush invoked as part of a post-process, or not?
Source: src/renderer/webgl/pipelines/events/BEFORE_FLUSH_EVENT.js#L7
Since: 3.50.0
BIND ​
BIND ​
Description:
The WebGLPipeline Bind Event.
This event is dispatched by a WebGLPipeline when it is bound by the Pipeline Manager.
Parameters:
name type optional description
pipeline Phaser.Renderer.WebGL.WebGLPipeline No The pipeline that was bound.
currentShader Phaser.Renderer.WebGL.WebGLShader No The shader that was set as being current.
Source: src/renderer/webgl/pipelines/events/BIND_EVENT.js#L7
Since: 3.50.0
BOOT ​
BOOT ​
Description:
The WebGLPipeline Boot Event.
This event is dispatched by a WebGLPipeline when it has completed its boot phase.
Parameters:
name type optional description
pipeline Phaser.Renderer.WebGL.WebGLPipeline No The pipeline that booted.
Source: src/renderer/webgl/pipelines/events/BOOT_EVENT.js#L7
Since: 3.50.0
DESTROY ​
DESTROY ​
Description:
The WebGLPipeline Destroy Event.
This event is dispatched by a WebGLPipeline when it is starting its destroy process.
Parameters:
name type optional description
pipeline Phaser.Renderer.WebGL.WebGLPipeline No The pipeline that has flushed.
Source: src/renderer/webgl/pipelines/events/DESTROY_EVENT.js#L7
Since: 3.50.0
REBIND ​
REBIND ​
Description:
The WebGLPipeline ReBind Event.
This event is dispatched by a WebGLPipeline when it is re-bound by the Pipeline Manager.
Parameters:
name type optional description
pipeline Phaser.Renderer.WebGL.WebGLPipeline No The pipeline that was rebound.
currentShader Phaser.Renderer.WebGL.WebGLShader No The shader that was set as being current.
Source: src/renderer/webgl/pipelines/events/REBIND_EVENT.js#L7
Since: 3.50.0
RESIZE ​
RESIZE ​
Description:
The WebGLPipeline Resize Event.
This event is dispatched by a WebGLPipeline when it is resized, usually as a result
of the Renderer resizing.
Parameters:
name type optional description
width number No The new width of the pipeline.
height number No The new height of the pipeline.
pipeline Phaser.Renderer.WebGL.WebGLPipeline No The pipeline that was resized.
Source: src/renderer/webgl/pipelines/events/RESIZE_EVENT.js#L7
Since: 3.50.0
Previous
Phaser.Renderer.Snapshot
Next
Phaser.Renderer.WebGL.Pipelines.FX
Static functions
AFTER_FLUSH
BEFORE_FLUSH
BIND
BOOT
DESTROY
REBIND
RESIZE
