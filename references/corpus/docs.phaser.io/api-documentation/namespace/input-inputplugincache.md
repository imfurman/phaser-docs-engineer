# Phaser.Input.InputPluginCache | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/input-inputplugincache

Phaser API Documentation
Namespaces
Phaser.Input.InputPluginCache
Version: Phaser v3.90.0
On this page
Phaser.Input.InputPluginCache
Scope: static
Source: src/input/InputPluginCache.js#L13
Static functions ​
getPlugin ​
<static> getPlugin(key) ​
Description:
Returns the input plugin object from the cache based on the given key.
Parameters:
name type optional description
key string No The key of the input plugin to get.
Returns: Phaser.Types.Input.InputPluginContainer - The input plugin object.
Source: src/input/InputPluginCache.js#L40
Since: 3.10.0
install ​
<static> install(target) ​
Description:
Installs all of the registered Input Plugins into the given target.
Parameters:
name type optional description
target Phaser.Input.InputPlugin No The target InputPlugin to install the plugins into.
Source: src/input/InputPluginCache.js#L56
Since: 3.10.0
register ​
<static> register(key, plugin, mapping, settingsKey, configKey) ​
Description:
Static method called directly by the Core internal Plugins.
Key is a reference used to get the plugin from the plugins object (i.e. InputPlugin)
Plugin is the object to instantiate to create the plugin
Mapping is what the plugin is injected into the Scene.Systems as (i.e. input)
Parameters:
name type optional description
key string No A reference used to get this plugin from the plugin cache.
plugin function No The plugin to be stored. Should be the core object, not instantiated.
mapping string No If this plugin is to be injected into the Input Plugin, this is the property key used.
settingsKey string No The key in the Scene Settings to check to see if this plugin should install or not.
configKey string No The key in the Game Config to check to see if this plugin should install or not.
Source: src/input/InputPluginCache.js#L19
Since: 3.10.0
remove ​
<static> remove(key) ​
Description:
Removes an input plugin based on the given key.
Parameters:
name type optional description
key string No The key of the input plugin to remove.
Source: src/input/InputPluginCache.js#L85
Since: 3.10.0
Previous
Phaser.Input.Gamepad
Next
Phaser.Input.Keyboard.Events
Static functions
getPlugin
install
register
remove
