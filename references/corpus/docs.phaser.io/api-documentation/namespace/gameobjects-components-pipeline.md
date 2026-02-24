# Phaser.GameObjects.Components.Pipeline | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-pipeline

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.Pipeline
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.Pipeline
Scope: static
Source: src/gameobjects/components/Pipeline.js#L9
Since: 3.0.0
Static functions ​
defaultPipeline ​
defaultPipeline: Phaser.Renderer.WebGL.WebGLPipeline ​
Description:
The initial WebGL pipeline of this Game Object.
If you call resetPipeline on this Game Object, the pipeline is reset to this default.
Tags:
webglOnly
Source: src/gameobjects/components/Pipeline.js#L19
Since: 3.0.0
pipeline ​
pipeline: Phaser.Renderer.WebGL.WebGLPipeline ​
Description:
The current WebGL pipeline of this Game Object.
Tags:
webglOnly
Source: src/gameobjects/components/Pipeline.js#L32
Since: 3.0.0
pipelineData ​
pipelineData: object ​
Description:
An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.
Tags:
webglOnly
Source: src/gameobjects/components/Pipeline.js#L43
Since: 3.50.0
Static functions ​
getPipelineName ​
<instance> getPipelineName() ​
Description:
Gets the name of the WebGL Pipeline this Game Object is currently using.
Tags:
webglOnly
Returns: string - The string-based name of the pipeline being used by this Game Object, or null.
Source: src/gameobjects/components/Pipeline.js#L201
Since: 3.0.0
initPipeline ​
<instance> initPipeline([pipeline]) ​
Description:
Sets the initial WebGL Pipeline of this Game Object.
This should only be called during the instantiation of the Game Object. After that, use setPipeline .
Tags:
webglOnly
Parameters:
name type optional description
pipeline string | Phaser.Renderer.WebGL.WebGLPipeline Yes Either the string-based name of the pipeline, or a pipeline instance to set.
Returns: boolean - true if the pipeline was set successfully, otherwise false .
Source: src/gameobjects/components/Pipeline.js#L53
Since: 3.0.0
resetPipeline ​
<instance> resetPipeline([resetData]) ​
Description:
Resets the WebGL Pipeline of this Game Object back to the default it was created with.
Tags:
webglOnly
Parameters:
name type optional default description
resetData boolean Yes false Reset the pipelineData object to being an empty object?
Returns: boolean - true if the pipeline was reset successfully, otherwise false .
Source: src/gameobjects/components/Pipeline.js#L176
Since: 3.0.0
setPipeline ​
<instance> setPipeline(pipeline, [pipelineData], [copyData]) ​
Description:
Sets the main WebGL Pipeline of this Game Object.
Also sets the pipelineData property, if the parameter is given.
Tags:
webglOnly
Parameters:
name type optional default description
pipeline string | Phaser.Renderer.WebGL.WebGLPipeline No Either the string-based name of the pipeline, or a pipeline instance to set.
pipelineData object Yes Optional pipeline data object that is set in to the pipelineData property of this Game Object.
copyData boolean Yes true Should the pipeline data object be deep copied into the pipelineData property of this Game Object? If false it will be set by reference instead.
Returns: Phaser.GameObjects.Components.Pipeline - This Game Object instance.
Source: src/gameobjects/components/Pipeline.js#L100
Since: 3.0.0
setPipelineData ​
<instance> setPipelineData(key, [value]) ​
Description:
Adds an entry to the pipelineData object belonging to this Game Object.
If the 'key' already exists, its value is updated. If it doesn't exist, it is created.
If value is undefined, and key exists, key is removed from the data object.
Tags:
webglOnly
Parameters:
name type optional description
key string No The key of the pipeline data to set, update, or delete.
value any Yes The value to be set with the key. If undefined then key will be deleted from the object.
Returns: Phaser.GameObjects.Components.Pipeline - This Game Object instance.
Source: src/gameobjects/components/Pipeline.js#L144
Since: 3.50.0
Previous
Phaser.GameObjects.Components.PathFollower
Next
Phaser.GameObjects.Components.PostPipeline
Static functions
defaultPipeline
pipeline
pipelineData
Static functions
getPipelineName
initPipeline
resetPipeline
setPipeline
setPipelineData
