# PluginManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/plugins-pluginmanager

Phaser API Documentation
Class
PluginManager
Version: Phaser v3.90.0
On this page
PluginManager
The PluginManager is responsible for installing and adding plugins to Phaser.
It is a global system and therefore belongs to the Game instance, not a specific Scene.
It works in conjunction with the PluginCache. Core internal plugins automatically register themselves
with the Cache, but it's the Plugin Manager that is responsible for injecting them into the Scenes.
There are two types of plugin:
A Global Plugin
A Scene Plugin
A Global Plugin is a plugin that lives within the Plugin Manager rather than a Scene. You can get
access to it by calling PluginManager.get and providing a key. Any Scene that requests a plugin in
this way will get access to the same plugin instance, allowing you to use a single plugin across
multiple Scenes.
A Scene Plugin is a plugin dedicated to running within a Scene. These are different to Global Plugins
in that their instances do not live within the Plugin Manager, but within the Scene Systems class instead.
Also, every Scene created is given its own unique instance of a Scene Plugin. Examples of core Scene
Plugins include the Input Plugin, the Tween Plugin and the physics Plugins.
You can add a plugin to Phaser in three different ways:
Preload it
Include it in your source code and install it via the Game Config
Include it in your source code and install it within a Scene
For examples of all of these approaches please see the Phaser 3 Examples Repo plugins folder.
For information on creating your own plugin please see the Phaser 3 Plugin Template.
Constructor
new PluginManager(game)
Parameters
name type optional description
game Phaser.Game No The game instance that owns this Plugin Manager.
Scope : static
Source: src/plugins/PluginManager.js#L18
Since: 3.0.0
Public Members ​
game ​
game: Phaser.Game ​
Description:
The game instance that owns this Plugin Manager.
Source: src/plugins/PluginManager.js#L69
Since: 3.0.0
plugins ​
plugins: Array.< Phaser.Types.Plugins.GlobalPlugin > ​
Description:
The global plugins currently running and managed by this Plugin Manager.
A plugin must have been started at least once in order to appear in this list.
Source: src/plugins/PluginManager.js#L78
Since: 3.8.0
scenePlugins ​
scenePlugins: Array.<string> ​
Description:
A list of plugin keys that should be installed into Scenes as well as the Core Plugins.
Source: src/plugins/PluginManager.js#L88
Since: 3.8.0
Public Methods ​
addToScene ​
<instance> addToScene(sys, globalPlugins, scenePlugins) ​
Description:
Called by the Scene Systems class. Tells the plugin manager to install all Scene plugins into it.
First it will install global references, i.e. references from the Game systems into the Scene Systems (and Scene if mapped.)
Then it will install Core Scene Plugins followed by Scene Plugins registered with the PluginManager.
Finally it will install any references to Global Plugins that have a Scene mapping property into the Scene itself.
Access: protected
Parameters:
name type optional description
sys Phaser.Scenes.Systems No The Scene Systems class to install all the plugins in to.
globalPlugins array No An array of global plugins to install.
scenePlugins array No An array of scene plugins to install.
Source: src/plugins/PluginManager.js#L212
Since: 3.8.0
boot ​
<instance> boot() ​
Description:
Runs once the game has booted and installs all of the plugins configured in the Game Config.
Access: protected
Source: src/plugins/PluginManager.js#L127
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Plugin Manager and all associated plugins.
It will iterate all plugins found and call their destroy methods.
The PluginCache will remove all custom plugins.
Source: src/plugins/PluginManager.js#L866
Since: 3.8.0
get ​
<instance> get(key, [autoStart]) ​
Description:
Gets a global plugin from the Plugin Manager based on the given key and returns it.
If it cannot find an active plugin based on the key, but there is one in the Plugin Cache with the same key,
then it will create a new instance of the cached plugin and return that.
Parameters:
name type optional default description
key string No The key of the plugin to get.
autoStart boolean Yes true Automatically start a new instance of the plugin if found in the cache, but not actively running.
Returns: Phaser.Plugins.BasePlugin , function - The plugin, or null if no plugin was found matching the key.
Source: src/plugins/PluginManager.js#L644
Since: 3.8.0
getClass ​
<instance> getClass(key) ​
Description:
Returns the plugin class from the cache.
Used internally by the Plugin Manager.
Parameters:
name type optional description
key string No The key of the plugin to get.
Returns: Phaser.Plugins.BasePlugin - A Plugin object
Source: src/plugins/PluginManager.js#L687
Since: 3.8.0
getDefaultScenePlugins ​
<instance> getDefaultScenePlugins() ​
Description:
Called by the Scene Systems class. Returns a list of plugins to be installed.
Access: protected
Returns: Array.<string> - A list keys of all the Scene Plugins to install.
Source: src/plugins/PluginManager.js#L311
Since: 3.8.0
getEntry ​
<instance> getEntry(key) ​
Description:
Gets a global plugin based on the given key.
Access: protected
Parameters:
name type optional description
key string No The unique plugin key.
Returns: Phaser.Types.Plugins.GlobalPlugin - The plugin entry.
Source: src/plugins/PluginManager.js#L501
Since: 3.8.0
getIndex ​
<instance> getIndex(key) ​
Description:
Gets an index of a global plugin based on the given key.
Access: protected
Parameters:
name type optional description
key string No The unique plugin key.
Returns: number - The index of the plugin within the plugins array.
Source: src/plugins/PluginManager.js#L473
Since: 3.8.0
install ​
<instance> install(key, plugin, [start], [mapping], [data]) ​
Description:
Installs a new Global Plugin into the Plugin Manager and optionally starts it running.
A global plugin belongs to the Plugin Manager, rather than a specific Scene, and can be accessed
and used by all Scenes in your game.
The key property is what you use to access this plugin from the Plugin Manager.
this . plugins . install ( 'powerupsPlugin' , pluginCode ) ;
// and from within the scene:
this . plugins . get ( 'powerupsPlugin' ) ;
This method is called automatically by Phaser if you install your plugins using either the
Game Configuration object, or by preloading them via the Loader.
The same plugin can be installed multiple times into the Plugin Manager by simply giving each
instance its own unique key.
Parameters:
name type optional default description
key string No The unique handle given to this plugin within the Plugin Manager.
plugin function No The plugin code. This should be the non-instantiated version.
start boolean Yes false Automatically start the plugin running? This is always true if you provide a mapping value.
mapping string Yes If this plugin is injected into the Phaser.Scene class, this is the property key to use.
data any Yes A value passed to the plugin's init method.
Returns: Phaser.Plugins.BasePlugin - The plugin that was started, or null if start was false, or game isn't yet booted.
Source: src/plugins/PluginManager.js#L401
Since: 3.8.0
installScenePlugin ​
<instance> installScenePlugin(key, plugin, [mapping], [addToScene], [fromLoader]) ​
Description:
Installs a new Scene Plugin into the Plugin Manager and optionally adds it
to the given Scene as well. A Scene Plugin added to the manager in this way
will be automatically installed into all new Scenes using the key and mapping given.
The key property is what the plugin is injected into Scene.Systems as.
The mapping property is optional, and if specified is what the plugin is installed into
the Scene as. For example:
this . plugins . installScenePlugin ( 'powerupsPlugin' , pluginCode , 'powerups' ) ;
// and from within the scene:
this . sys . powerupsPlugin ; // key value
this . powerups ; // mapping value
This method is called automatically by Phaser if you install your plugins using either the
Game Configuration object, or by preloading them via the Loader.
Parameters:
name type optional default description
key string No The property key that will be used to add this plugin to Scene.Systems.
plugin function No The plugin code. This should be the non-instantiated version.
mapping string Yes If this plugin is injected into the Phaser.Scene class, this is the property key to use.
addToScene Phaser.Scene Yes Optionally automatically add this plugin to the given Scene.
fromLoader boolean Yes false Is this being called by the Loader?
Source: src/plugins/PluginManager.js#L330
Since: 3.8.0
isActive ​
<instance> isActive(key) ​
Description:
Checks if the given global plugin, based on its key, is active or not.
Parameters:
name type optional description
key string No The unique plugin key.
Returns: boolean - true if the plugin is active, otherwise false .
Source: src/plugins/PluginManager.js#L522
Since: 3.8.0
registerFileType ​
<instance> registerFileType(key, callback, [addToScene]) ​
Description:
Registers a new file type with the global File Types Manager, making it available to all Loader
Plugins created after this.
This is usually called from within your Plugin code and is a helpful short-cut for creating
new loader file types.
The key is the property that will be injected into the Loader Plugin and used to load the
files. For example:
this . plugins . registerFileType ( 'wad' , doomWadLoaderCallback ) ;
// later in your preload code:
this . load . wad ( ) ;
The callback is what is called when the loader tries to load a file matching the given key.
It's important to understand that the callback is invoked within
the context of the LoaderPlugin. In this context there are several properties / methods available
to use:
this.addFile - A method to add the new file to the load queue.
this.scene - The Scene that owns the Loader Plugin instance.
See the LoaderPlugin class for more details. Any public property or method listed is available from
your callback under this .
Parameters:
name type optional description
key string No The key of the Game Object that the given callbacks will create, i.e. image , sprite .
callback function No The callback to invoke when the Game Object Factory is called.
addToScene Phaser.Scene Yes Optionally add this file type into the Loader Plugin owned by the given Scene.
Source: src/plugins/PluginManager.js#L822
Since: 3.8.0
registerGameObject ​
<instance> registerGameObject(key, [factoryCallback], [creatorCallback]) ​
Description:
Registers a new type of Game Object with the global Game Object Factory and / or Creator.
This is usually called from within your Plugin code and is a helpful short-cut for creating
new Game Objects.
The key is the property that will be injected into the factories and used to create the
Game Object. For example:
this . plugins . registerGameObject ( 'clown' , clownFactoryCallback , clownCreatorCallback ) ;
// later in your game code:
this . add . clown ( ) ;
this . make . clown ( ) ;
The callbacks are what are called when the factories try to create a Game Object
matching the given key. It's important to understand that the callbacks are invoked within
the context of the GameObjectFactory. In this context there are several properties available
to use:
this.scene - A reference to the Scene that owns the GameObjectFactory.
this.displayList - A reference to the Display List the Scene owns.
this.updateList - A reference to the Update List the Scene owns.
See the GameObjectFactory and GameObjectCreator classes for more details.
Any public property or method listed is available from your callbacks under this .
Parameters:
name type optional description
key string No The key of the Game Object that the given callbacks will create, i.e. image , sprite .
factoryCallback function Yes The callback to invoke when the Game Object Factory is called.
creatorCallback function Yes The callback to invoke when the Game Object Creator is called.
Source: src/plugins/PluginManager.js#L744
Since: 3.8.0
removeGameObject ​
<instance> removeGameObject(key, [removeFromFactory], [removeFromCreator]) ​
Description:
Removes a previously registered Game Object from the global Game Object Factory and / or Creator.
This is usually called from within your Plugin destruction code to help clean-up after your plugin has been removed.
Parameters:
name type optional default description
key string No The key of the Game Object to be removed from the factories.
removeFromFactory boolean Yes true Should the Game Object be removed from the Game Object Factory?
removeFromCreator boolean Yes true Should the Game Object be removed from the Game Object Creator?
Source: src/plugins/PluginManager.js#L793
Since: 3.19.0
removeGlobalPlugin ​
<instance> removeGlobalPlugin(key) ​
Description:
Removes a global plugin from the Plugin Manager and Plugin Cache.
It is up to you to remove all references to this plugin that you may hold within your game code.
Parameters:
name type optional description
key string No The key of the plugin to remove.
Source: src/plugins/PluginManager.js#L703
Since: 3.8.0
removeScenePlugin ​
<instance> removeScenePlugin(key) ​
Description:
Removes a scene plugin from the Plugin Manager and Plugin Cache.
This will not remove the plugin from any active Scenes that are already using it.
It is up to you to remove all references to this plugin that you may hold within your game code.
Parameters:
name type optional description
key string No The key of the plugin to remove.
Source: src/plugins/PluginManager.js#L725
Since: 3.8.0
start ​
<instance> start(key, [runAs]) ​
Description:
Starts a global plugin running.
If the plugin was previously active then calling start will reset it to an active state and then
call its start method.
If the plugin has never been run before a new instance of it will be created within the Plugin Manager,
its active state set and then both of its init and start methods called, in that order.
If the plugin is already running under the given key then nothing happens.
Parameters:
name type optional description
key string No The key of the plugin to start.
runAs string Yes Run the plugin under a new key. This allows you to run one plugin multiple times.
Returns: Phaser.Plugins.BasePlugin - The plugin that was started, or null if invalid key given or plugin is already stopped.
Source: src/plugins/PluginManager.js#L539
Since: 3.8.0
stop ​
<instance> stop(key) ​
Description:
Stops a global plugin from running.
If the plugin is active then its active state will be set to false and the plugins stop method
will be called.
If the plugin is not already running, nothing will happen.
Parameters:
name type optional description
key string No The key of the plugin to stop.
Returns: Phaser.Plugins.PluginManager - The Plugin Manager.
Source: src/plugins/PluginManager.js#L616
Since: 3.8.0
Previous
BasePlugin
Next
ScenePlugin
Public Members
game
plugins
scenePlugins
Public Methods
addToScene
boot
destroy
get
getClass
getDefaultScenePlugins
getEntry
getIndex
install
installScenePlugin
isActive
registerFileType
registerGameObject
removeGameObject
removeGlobalPlugin
removeScenePlugin
start
stop
