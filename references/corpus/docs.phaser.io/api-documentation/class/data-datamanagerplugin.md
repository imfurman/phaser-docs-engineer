# DataManagerPlugin | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/data-datamanagerplugin

Phaser API Documentation
Class
DataManagerPlugin
Version: Phaser v3.90.0
On this page
DataManagerPlugin
The Data Component features a means to store pieces of data specific to a Game Object, System or Plugin.
You can then search, query it, and retrieve the data. The parent must either extend EventEmitter,
or have a property called events that is an instance of it.
Constructor
new DataManagerPlugin(scene)
Parameters
name type optional description
scene Phaser.Scene No A reference to the Scene that this DataManager belongs to.
Scope : static
Extends
Phaser.Data.DataManager
Source: src/data/DataManagerPlugin.js#L12
Since: 3.0.0
Inherited Members ​
From Phaser.Data.DataManager :
count
events
freeze
list
parent
values
Public Members ​
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene that this DataManager belongs to.
Source: src/data/DataManagerPlugin.js#L36
Since: 3.0.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
A reference to the Scene's Systems.
Source: src/data/DataManagerPlugin.js#L45
Since: 3.0.0
Inherited Methods ​
From Phaser.Data.DataManager :
each
get
getAll
has
inc
merge
pop
query
remove
reset
set
setFreeze
toggle
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
The Scene that owns this plugin is being destroyed.
We need to shutdown and then kill off all external references.
Overrides: Phaser.Data.DataManager#destroy
Source: src/data/DataManagerPlugin.js#L100
Since: 3.5.0
Previous
DataManager
Next
BaseShader
Inherited Members
Public Members
scene
systems
Inherited Methods
Public Methods
destroy
