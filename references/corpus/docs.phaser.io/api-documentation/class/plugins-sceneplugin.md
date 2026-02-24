# ScenePlugin | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/plugins-sceneplugin

Phaser API Documentation
Class
ScenePlugin
Version: Phaser v3.90.0
On this page
ScenePlugin
A Scene Level Plugin is installed into every Scene and belongs to that Scene.
It can listen for Scene events and respond to them.
It can map itself to a Scene property, or into the Scene Systems, or both.
Constructor
new ScenePlugin(scene, pluginManager, pluginKey)
Parameters
name type optional description
scene Phaser.Scene No A reference to the Scene that has installed this plugin.
pluginManager Phaser.Plugins.PluginManager No A reference to the Plugin Manager.
pluginKey string No The key under which this plugin has been installed into the Scene Systems.
Scope : static
Extends
Phaser.Plugins.BasePlugin
Source: src/plugins/ScenePlugin.js#L11
Since: 3.8.0
Inherited Members ​
From Phaser.Plugins.BasePlugin :
game
pluginManager
Public Members ​
pluginKey ​
pluginKey: string ​
Description:
The key under which this plugin was installed into the Scene Systems.
This property is only set when the plugin is instantiated and added to the Scene, not before.
You can use it during the boot method.
Source: src/plugins/ScenePlugin.js#L63
Since: 3.54.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene that has installed this plugin.
Only set if it's a Scene Plugin, otherwise null .
This property is only set when the plugin is instantiated and added to the Scene, not before.
You can use it during the boot method.
Access: protected
Source: src/plugins/ScenePlugin.js#L37
Since: 3.8.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
A reference to the Scene Systems of the Scene that has installed this plugin.
Only set if it's a Scene Plugin, otherwise null .
This property is only set when the plugin is instantiated and added to the Scene, not before.
You can use it during the boot method.
Access: protected
Source: src/plugins/ScenePlugin.js#L50
Since: 3.8.0
Inherited Methods ​
From Phaser.Plugins.BasePlugin :
init
start
stop
Public Methods ​
boot ​
<instance> boot() ​
Description:
This method is called when the Scene boots. It is only ever called once.
By this point the plugin properties scene and systems will have already been set.
In here you can listen for Scene and set-up whatever you need for this plugin to run.
Here are the Scene events you can listen to:
start
ready
preupdate
update
postupdate
resize
pause
resume
sleep
wake
transitioninit
transitionstart
transitioncomplete
transitionout
shutdown
destroy
At the very least you should offer a destroy handler for when the Scene closes down, i.e:
var eventEmitter = this . systems . events ;
eventEmitter . once ( 'destroy' , this . sceneDestroy , this ) ;
Source: src/plugins/ScenePlugin.js#L79
Since: 3.8.0
destroy ​
<instance> destroy() ​
Description:
Game instance has been destroyed.
You must release everything in here, all references, all objects, free it all up.
Overrides: Phaser.Plugins.BasePlugin#destroy
Source: src/plugins/ScenePlugin.js#L118
Since: 3.8.0
Previous
PluginManager
Next
CanvasRenderer
Inherited Members
Public Members
pluginKey
scene
systems
Inherited Methods
Public Methods
boot
destroy
