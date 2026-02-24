# Systems | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/scenes-systems

Phaser API Documentation
Class
Systems
Version: Phaser v3.90.0
On this page
Systems
The Scene Systems class.
This class is available from within a Scene under the property sys .
It is responsible for managing all of the plugins a Scene has running, including the display list, and
handling the update step and renderer. It also contains references to global systems belonging to Game.
Constructor
new Systems(scene, config)
Parameters
name type optional description
scene Phaser.Scene No The Scene that owns this Systems instance.
config string | Phaser.Types.Scenes.SettingsConfig No Scene specific configuration settings.
Scope : static
Source: src/scene/Systems.js#L16
Since: 3.0.0
Public Members ​
add ​
add: Phaser.GameObjects.GameObjectFactory ​
Description:
A reference to the Scene's Game Object Factory.
Use this to quickly and easily create new Game Objects.
In the default set-up you can access this from within a Scene via the this.add property.
Source: src/scene/Systems.js#L196
Since: 3.0.0
anims ​
anims: Phaser.Animations.AnimationManager ​
Description:
A reference to the global Animations Manager.
In the default set-up you can access this from within a Scene via the this.anims property.
Source: src/scene/Systems.js#L115
Since: 3.0.0
cache ​
cache: Phaser.Cache.CacheManager ​
Description:
A reference to the global Cache. The Cache stores all files brought in to Phaser via
the Loader, with the exception of images. Images are stored in the Texture Manager.
In the default set-up you can access this from within a Scene via the this.cache property.
Source: src/scene/Systems.js#L126
Since: 3.0.0
cameras ​
cameras: Phaser.Cameras.Scene2D.CameraManager ​
Description:
A reference to the Scene's Camera Manager.
Use this to manipulate and create Cameras for this specific Scene.
In the default set-up you can access this from within a Scene via the this.cameras property.
Source: src/scene/Systems.js#L209
Since: 3.0.0
canvas ​
canvas: HTMLCanvasElement ​
Description:
A handy reference to the Scene canvas / context.
Source: src/scene/Systems.js#L95
Since: 3.0.0
config ​
config: string, Phaser.Types.Scenes.SettingsConfig ​
Description:
The Scene Configuration object, as passed in when creating the Scene.
Source: src/scene/Systems.js#L77
Since: 3.0.0
context ​
context: CanvasRenderingContext2D ​
Description:
A reference to the Canvas Rendering Context being used by the renderer.
Source: src/scene/Systems.js#L104
Since: 3.0.0
displayList ​
displayList: Phaser.GameObjects.DisplayList ​
Description:
A reference to the Scene's Display List.
Use this to organize the children contained in the display list.
In the default set-up you can access this from within a Scene via the this.children property.
Source: src/scene/Systems.js#L222
Since: 3.0.0
events ​
events: Phaser.Events.EventEmitter ​
Description:
A reference to the Scene's Event Manager.
Use this to listen for Scene specific events, such as pause and shutdown .
In the default set-up you can access this from within a Scene via the this.events property.
Source: src/scene/Systems.js#L235
Since: 3.0.0
facebook ​
facebook: Phaser.FacebookInstantGamesPlugin ​
Description:
The Facebook Instant Games Plugin.
Source: src/scene/Systems.js#L67
Since: 3.12.0
game ​
game: Phaser.Game ​
Description:
A reference to the Phaser Game instance.
Source: src/scene/Systems.js#L47
Since: 3.0.0
make ​
make: Phaser.GameObjects.GameObjectCreator ​
Description:
A reference to the Scene's Game Object Creator.
Use this to quickly and easily create new Game Objects. The difference between this and the
Game Object Factory, is that the Creator just creates and returns Game Object instances, it
doesn't then add them to the Display List or Update List.
In the default set-up you can access this from within a Scene via the this.make property.
Source: src/scene/Systems.js#L248
Since: 3.0.0
plugins ​
plugins: Phaser.Plugins.PluginManager ​
Description:
A reference to the global Plugins Manager.
In the default set-up you can access this from within a Scene via the this.plugins property.
Source: src/scene/Systems.js#L138
Since: 3.0.0
registry ​
registry: Phaser.Data.DataManager ​
Description:
A reference to the global registry. This is a game-wide instance of the Data Manager, allowing
you to exchange data between Scenes via a universal and shared point.
In the default set-up you can access this from within a Scene via the this.registry property.
Source: src/scene/Systems.js#L149
Since: 3.0.0
renderer ​
renderer: Phaser.Renderer.Canvas.CanvasRenderer , Phaser.Renderer.WebGL.WebGLRenderer ​
Description:
A reference to either the Canvas or WebGL Renderer that this Game is using.
Source: src/scene/Systems.js#L56
Since: 3.17.0
scale ​
scale: Phaser.Scale.ScaleManager ​
Description:
A reference to the global Scale Manager.
In the default set-up you can access this from within a Scene via the this.scale property.
Source: src/scene/Systems.js#L161
Since: 3.15.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene that these Systems belong to.
Source: src/scene/Systems.js#L38
Since: 3.0.0
scenePlugin ​
scenePlugin: Phaser.Scenes.ScenePlugin ​
Description:
A reference to the Scene Manager Plugin.
Use this to manipulate both this and other Scenes in your game. For example, to launch a parallel Scene,
or pause or resume a Scene, or switch from this Scene to another.
In the default set-up you can access this from within a Scene via the this.scene property.
Source: src/scene/Systems.js#L263
Since: 3.0.0
settings ​
settings: Phaser.Types.Scenes.SettingsObject ​
Description:
The Scene Settings. This is the parsed output based on the Scene configuration.
Source: src/scene/Systems.js#L86
Since: 3.0.0
sound ​
sound: Phaser.Sound.NoAudioSoundManager , Phaser.Sound.HTML5AudioSoundManager , Phaser.Sound.WebAudioSoundManager ​
Description:
A reference to the global Sound Manager.
In the default set-up you can access this from within a Scene via the this.sound property.
Source: src/scene/Systems.js#L172
Since: 3.0.0
textures ​
textures: Phaser.Textures.TextureManager ​
Description:
A reference to the global Texture Manager.
In the default set-up you can access this from within a Scene via the this.textures property.
Source: src/scene/Systems.js#L183
Since: 3.0.0
updateList ​
updateList: Phaser.GameObjects.UpdateList ​
Description:
A reference to the Scene's Update List.
Use this to organize the children contained in the update list.
The Update List is responsible for managing children that need their preUpdate methods called,
in order to process internal components - such as Sprites with Animations.
In the default set-up there is no reference to this from within the Scene itself.
Source: src/scene/Systems.js#L277
Since: 3.0.0
Public Methods ​
canInput ​
<instance> canInput() ​
Description:
Can this Scene receive Input events?
Returns: boolean - true if this Scene can receive Input events.
Source: src/scene/Systems.js#L575
Since: 3.60.0
depthSort ​
<instance> depthSort() ​
Description:
Immediately sorts the display list if the flag is set.
Source: src/scene/Systems.js#L404
Since: 3.0.0
getData ​
<instance> getData() ​
Description:
Returns any data that was sent to this Scene by another Scene.
The data is also passed to Scene.init and in various Scene events, but
you can access it at any point via this method.
Returns: any - The Scene Data.
Source: src/scene/Systems.js#L546
Since: 3.22.0
getStatus ​
<instance> getStatus() ​
Description:
Returns the current status of this Scene.
Returns: number - The status of this Scene. One of the Phaser.Scene constants.
Source: src/scene/Systems.js#L562
Since: 3.60.0
init ​
<instance> init(game) ​
Description:
This method is called only once by the Scene Manager when the Scene is instantiated.
It is responsible for setting up all of the Scene plugins and references.
It should never be called directly.
Access: protected
Parameters:
name type optional description
game Phaser.Game No A reference to the Phaser Game instance.
Fires: Phaser.Scenes.Events#event:BOOT
Source: src/scene/Systems.js#L307
Since: 3.0.0
isActive ​
<instance> isActive() ​
Description:
Is this Scene running?
Returns: boolean - true if this Scene is running, otherwise false .
Source: src/scene/Systems.js#L603
Since: 3.0.0
isPaused ​
<instance> isPaused() ​
Description:
Is this Scene paused?
Returns: boolean - true if this Scene is paused, otherwise false .
Source: src/scene/Systems.js#L616
Since: 3.13.0
isSleeping ​
<instance> isSleeping() ​
Description:
Is this Scene sleeping?
Returns: boolean - true if this Scene is asleep, otherwise false .
Source: src/scene/Systems.js#L590
Since: 3.0.0
isTransitionIn ​
<instance> isTransitionIn() ​
Description:
Is this Scene currently transitioning in from another Scene?
Returns: boolean - true if this Scene is transitioning in from another Scene, otherwise false .
Source: src/scene/Systems.js#L655
Since: 3.5.0
isTransitioning ​
<instance> isTransitioning() ​
Description:
Is this Scene currently transitioning out to, or in from another Scene?
Returns: boolean - true if this Scene is currently transitioning, otherwise false .
Source: src/scene/Systems.js#L629
Since: 3.5.0
isTransitionOut ​
<instance> isTransitionOut() ​
Description:
Is this Scene currently transitioning out from itself to another Scene?
Returns: boolean - true if this Scene is in transition to another Scene, otherwise false .
Source: src/scene/Systems.js#L642
Since: 3.5.0
isVisible ​
<instance> isVisible() ​
Description:
Is this Scene visible and rendering?
Returns: boolean - true if this Scene is visible, otherwise false .
Source: src/scene/Systems.js#L668
Since: 3.0.0
pause ​
<instance> pause([data]) ​
Description:
Pause this Scene.
A paused Scene still renders, it just doesn't run any of its update handlers or systems.
Parameters:
name type optional description
data object Yes A data object that will be passed in the 'pause' event.
Returns: Phaser.Scenes.Systems - This Systems object.
Fires: Phaser.Scenes.Events#event:PAUSE
Source: src/scene/Systems.js#L415
Since: 3.0.0
queueDepthSort ​
<instance> queueDepthSort() ​
Description:
Force a sort of the display list on the next render.
Source: src/scene/Systems.js#L393
Since: 3.0.0
render ​
<instance> render(renderer) ​
Description:
Called automatically by the Scene Manager.
Instructs the Scene to render itself via its Camera Manager to the renderer given.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer | Phaser.Renderer.WebGL.WebGLRenderer No The renderer that invoked the render call.
Fires: Phaser.Scenes.Events#event:PRE_RENDER , Phaser.Scenes.Events#event:RENDER
Source: src/scene/Systems.js#L369
Since: 3.0.0
resume ​
<instance> resume([data]) ​
Description:
Resume this Scene from a paused state.
Parameters:
name type optional description
data object Yes A data object that will be passed in the 'resume' event.
Returns: Phaser.Scenes.Systems - This Systems object.
Fires: Phaser.Scenes.Events#event:RESUME
Source: src/scene/Systems.js#L449
Since: 3.0.0
setActive ​
<instance> setActive(value, [data]) ​
Description:
Set the active state of this Scene.
An active Scene will run its core update loop.
Parameters:
name type optional description
value boolean No If true the Scene will be resumed, if previously paused. If false it will be paused.
data object Yes A data object that will be passed in the 'resume' or 'pause' events.
Returns: Phaser.Scenes.Systems - This Systems object.
Source: src/scene/Systems.js#L699
Since: 3.0.0
setVisible ​
<instance> setVisible(value) ​
Description:
Sets the visible state of this Scene.
An invisible Scene will not render, but will still process updates.
Parameters:
name type optional description
value boolean No true to render this Scene, otherwise false .
Returns: Phaser.Scenes.Systems - This Systems object.
Source: src/scene/Systems.js#L681
Since: 3.0.0
shutdown ​
<instance> shutdown([data]) ​
Description:
Shutdown this Scene and send a shutdown event to all of its systems.
A Scene that has been shutdown will not run its update loop or render, but it does
not destroy any of its plugins or references. It is put into hibernation for later use.
If you don't ever plan to use this Scene again, then it should be destroyed instead
to free-up resources.
Parameters:
name type optional description
data object Yes A data object that will be passed in the 'shutdown' event.
Fires: Phaser.Scenes.Events#event:SHUTDOWN
Source: src/scene/Systems.js#L757
Since: 3.0.0
sleep ​
<instance> sleep([data]) ​
Description:
Send this Scene to sleep.
A sleeping Scene doesn't run its update step or render anything, but it also isn't shut down
or has any of its systems or children removed, meaning it can be re-activated at any point and
will carry on from where it left off. It also keeps everything in memory and events and callbacks
from other Scenes may still invoke changes within it, so be careful what is left active.
Parameters:
name type optional description
data object Yes A data object that will be passed in the 'sleep' event.
Returns: Phaser.Scenes.Systems - This Systems object.
Fires: Phaser.Scenes.Events#event:SLEEP
Source: src/scene/Systems.js#L477
Since: 3.0.0
start ​
<instance> start(data) ​
Description:
Start this Scene running and rendering.
Called automatically by the SceneManager.
Parameters:
name type optional description
data object No Optional data object that may have been passed to this Scene from another.
Fires: Phaser.Scenes.Events#event:START , Phaser.Scenes.Events#event:READY
Source: src/scene/Systems.js#L724
Since: 3.0.0
step ​
<instance> step(time, delta) ​
Description:
A single game step. Called automatically by the Scene Manager as a result of a Request Animation
Frame or Set Timeout call to the main Game instance.
Parameters:
name type optional description
time number No The time value from the most recent Game step. Typically a high-resolution timer value, or Date.now().
delta number No The delta value since the last frame. This is smoothed to avoid delta spikes by the TimeStep class.
Fires: Phaser.Scenes.Events#event:PRE_UPDATE , Phaser.Scenes.Events#event:UPDATE , Phaser.Scenes.Events#event:POST_UPDATE
Source: src/scene/Systems.js#L343
Since: 3.0.0
wake ​
<instance> wake([data]) ​
Description:
Wake-up this Scene if it was previously asleep.
Parameters:
name type optional description
data object Yes A data object that will be passed in the 'wake' event.
Returns: Phaser.Scenes.Systems - This Systems object.
Fires: Phaser.Scenes.Events#event:WAKE
Source: src/scene/Systems.js#L515
Since: 3.0.0
Previous
ScenePlugin
Next
BaseSound
Public Members
add
anims
cache
cameras
canvas
config
context
displayList
events
facebook
game
make
plugins
registry
renderer
scale
scene
scenePlugin
settings
sound
textures
updateList
Public Methods
canInput
depthSort
getData
getStatus
init
isActive
isPaused
isSleeping
isTransitionIn
isTransitioning
isTransitionOut
isVisible
pause
queueDepthSort
render
resume
setActive
setVisible
shutdown
sleep
start
step
wake
