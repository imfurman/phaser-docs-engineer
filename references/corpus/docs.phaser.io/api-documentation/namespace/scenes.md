# Phaser.Scenes | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/scenes

Phaser API Documentation
Namespaces
Phaser.Scenes
Version: Phaser v3.90.0
On this page
Phaser.Scenes
Scope: static
Source: src/scene/index.js#L10
Static functions ​
SceneManager
ScenePlugin
Systems
Static functions ​
GetPhysicsPlugins ​
<static> GetPhysicsPlugins(sys) ​
Description:
Builds an array of which physics plugins should be activated for the given Scene.
Parameters:
name type optional description
sys Phaser.Scenes.Systems No The scene system to get the physics systems of.
Returns: array - An array of Physics systems to start for this Scene.
Source: src/scene/GetPhysicsPlugins.js#L10
Since: 3.0.0
GetScenePlugins ​
<static> GetScenePlugins(sys) ​
Description:
Builds an array of which plugins (not including physics plugins) should be activated for the given Scene.
Parameters:
name type optional description
sys Phaser.Scenes.Systems No The Scene Systems object to check for plugins.
Returns: array - An array of all plugins which should be activated, either the default ones or the ones configured in the Scene Systems object.
Source: src/scene/GetScenePlugins.js#L9
Since: 3.0.0
Static functions ​
Events
Settings
Static functions ​
CREATING ​
CREATING: number ​
Description:
Scene state.
Source: src/scene/const.js#L55
Since: 3.0.0
DESTROYED ​
DESTROYED: number ​
Description:
Scene state.
Source: src/scene/const.js#L105
Since: 3.0.0
INIT ​
INIT: number ​
Description:
Scene state.
Source: src/scene/const.js#L25
Since: 3.0.0
LOADING ​
LOADING: number ​
Description:
Scene state.
Source: src/scene/const.js#L45
Since: 3.0.0
PAUSED ​
PAUSED: number ​
Description:
Scene state.
Source: src/scene/const.js#L75
Since: 3.0.0
PENDING ​
PENDING: number ​
Description:
Scene state.
Source: src/scene/const.js#L15
Since: 3.0.0
RUNNING ​
RUNNING: number ​
Description:
Scene state.
Source: src/scene/const.js#L65
Since: 3.0.0
SHUTDOWN ​
SHUTDOWN: number ​
Description:
Scene state.
Source: src/scene/const.js#L95
Since: 3.0.0
SLEEPING ​
SLEEPING: number ​
Description:
Scene state.
Source: src/scene/const.js#L85
Since: 3.0.0
START ​
START: number ​
Description:
Scene state.
Source: src/scene/const.js#L35
Since: 3.0.0
Previous
Phaser.Scenes.Settings
Next
Phaser.Sound.Events
Static functions
Static functions
GetPhysicsPlugins
GetScenePlugins
Static functions
Static functions
CREATING
DESTROYED
INIT
LOADING
PAUSED
PENDING
RUNNING
SHUTDOWN
SLEEPING
START
