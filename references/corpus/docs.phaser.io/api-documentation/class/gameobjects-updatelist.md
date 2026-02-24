# UpdateList | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-updatelist

Phaser API Documentation
Class
UpdateList
Version: Phaser v3.90.0
On this page
UpdateList
The Update List plugin.
Update Lists belong to a Scene and maintain the list Game Objects to be updated every frame.
Some or all of these Game Objects may also be part of the Scene's Display List , for Rendering.
Constructor
new UpdateList(scene)
Parameters
name type optional description
scene Phaser.Scene No The Scene that the Update List belongs to.
Scope : static
Extends
Phaser.Structs.ProcessQueue.<Phaser.GameObjects.GameObject>
Source: src/gameobjects/UpdateList.js#L12
Since: 3.0.0
Public Members ​
scene ​
scene: Phaser.Scene ​
Description:
The Scene that the Update List belongs to.
Source: src/gameobjects/UpdateList.js#L41
Since: 3.0.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
The Scene's Systems.
Source: src/gameobjects/UpdateList.js#L50
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
The Scene that owns this plugin is being destroyed.
We need to shutdown and then kill off all external references.
Source: src/gameobjects/UpdateList.js#L207
Since: 3.0.0
sceneUpdate ​
<instance> sceneUpdate(time, delta) ​
Description:
The update step.
Pre-updates every active Game Object in the list.
Parameters:
name type optional description
time number No The current timestamp.
delta number No The delta time elapsed since the last frame.
Source: src/gameobjects/UpdateList.js#L134
Since: 3.20.0
shutdown ​
<instance> shutdown() ​
Description:
The Scene that owns this plugin is shutting down.
We need to kill and reset all internal properties as well as stop listening to Scene events.
Source: src/gameobjects/UpdateList.js#L161
Since: 3.0.0
Previous
Triangle
Next
Video
Public Members
scene
systems
Public Methods
destroy
sceneUpdate
shutdown
