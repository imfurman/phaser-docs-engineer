# DisplayList | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-displaylist

Phaser API Documentation
Class
DisplayList
Version: Phaser v3.90.0
On this page
DisplayList
The Display List plugin.
Display Lists belong to a Scene and maintain the list of Game Objects to render every frame.
Some of these Game Objects may also be part of the Scene's Update List , for updating.
Constructor
new DisplayList(scene)
Parameters
name type optional description
scene Phaser.Scene No The Scene that this Display List belongs to.
Scope : static
Extends
Phaser.Structs.List.<Phaser.GameObjects.GameObject>
Source: src/gameobjects/DisplayList.js#L14
Since: 3.0.0
Public Members ​
events ​
events: Phaser.Events.EventEmitter ​
Description:
The Scene's Event Emitter.
Source: src/gameobjects/DisplayList.js#L68
Since: 3.50.0
scene ​
scene: Phaser.Scene ​
Description:
The Scene that this Display List belongs to.
Source: src/gameobjects/DisplayList.js#L50
Since: 3.0.0
sortChildrenFlag ​
sortChildrenFlag: boolean ​
Description:
The flag the determines whether Game Objects should be sorted when depthSort() is called.
Source: src/gameobjects/DisplayList.js#L40
Since: 3.0.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
The Scene's Systems.
Source: src/gameobjects/DisplayList.js#L59
Since: 3.0.0
Public Methods ​
depthSort ​
<instance> depthSort() ​
Description:
Immediately sorts the display list if the flag is set.
Source: src/gameobjects/DisplayList.js#L180
Since: 3.0.0
getChildren ​
<instance> getChildren() ​
Description:
Returns an array which contains all objects currently on the Display List.
This is a reference to the main list array, not a copy of it, so be careful not to modify it.
Returns: Array.< Phaser.GameObjects.GameObject > - The group members.
Source: src/gameobjects/DisplayList.js#L212
Since: 3.12.0
queueDepthSort ​
<instance> queueDepthSort() ​
Description:
Force a sort of the display list on the next call to depthSort.
Source: src/gameobjects/DisplayList.js#L169
Since: 3.0.0
sortByDepth ​
<instance> sortByDepth(childA, childB) ​
Description:
Compare the depth of two Game Objects.
Parameters:
name type optional description
childA Phaser.GameObjects.GameObject No The first Game Object.
childB Phaser.GameObjects.GameObject No The second Game Object.
Returns: number - The difference between the depths of each Game Object.
Source: src/gameobjects/DisplayList.js#L196
Since: 3.0.0
Previous
DOMElement
Next
DynamicBitmapText
Public Members
events
scene
sortChildrenFlag
systems
Public Methods
depthSort
getChildren
queueDepthSort
sortByDepth
