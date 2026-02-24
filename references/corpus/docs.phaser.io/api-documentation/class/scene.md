# Scene | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/scene

Phaser API Documentation
Class
Scene
Version: Phaser v3.90.0
On this page
Scene
A base Phaser.Scene class which can be extended for your own use.
You can also define the optional methods init() , preload() , and create() .
Constructor
new Scene([config])
Parameters
name type optional description
config string | Phaser.Types.Scenes.SettingsConfig Yes The scene key or scene specific configuration settings.
Scope : static
Source: src/scene/Scene.js#L10
Since: 3.0.0
Public Members ​
add ​
add: Phaser.GameObjects.GameObjectFactory ​
Description:
The Scene Game Object Factory.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L126
Since: 3.0.0
anims ​
anims: Phaser.Animations.AnimationManager ​
Description:
A reference to the global Animation Manager.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L49
Since: 3.0.0
cache ​
cache: Phaser.Cache.CacheManager ​
Description:
A reference to the global Cache.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L60
Since: 3.0.0
cameras ​
cameras: Phaser.Cameras.Scene2D.CameraManager ​
Description:
The Scene Camera Manager.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L115
Since: 3.0.0
children ​
children: Phaser.GameObjects.DisplayList ​
Description:
The Game Object Display List belonging to this Scene.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L159
Since: 3.0.0
data ​
data: Phaser.Data.DataManager ​
Description:
A Scene specific Data Manager Plugin.
See the registry property for the global Data Manager.
This property will only be available if defined in the Scene Injection Map and the plugin is installed.
Source: src/scene/Scene.js#L181
Since: 3.0.0
events ​
events: Phaser.Events.EventEmitter ​
Description:
A Scene specific Event Emitter.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L104
Since: 3.0.0
facebook ​
facebook: Phaser.FacebookInstantGamesPlugin ​
Description:
The Facebook Instant Games Plugin.
This property will only be available if defined in the Scene Injection Map, the plugin is installed and configured.
Source: src/scene/Scene.js#L262
Since: 3.12.0
game ​
game: Phaser.Game ​
Description:
A reference to the Phaser.Game instance.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L38
Since: 3.0.0
input ​
input: Phaser.Input.InputPlugin ​
Description:
The Scene Input Manager Plugin.
This property will only be available if defined in the Scene Injection Map and the plugin is installed.
Source: src/scene/Scene.js#L194
Since: 3.0.0
lights ​
lights: Phaser.GameObjects.LightsManager ​
Description:
The Scene Lights Manager Plugin.
This property will only be available if defined in the Scene Injection Map and the plugin is installed.
Source: src/scene/Scene.js#L170
Since: 3.0.0
load ​
load: Phaser.Loader.LoaderPlugin ​
Description:
The Scene Loader Plugin.
This property will only be available if defined in the Scene Injection Map and the plugin is installed.
Source: src/scene/Scene.js#L205
Since: 3.0.0
make ​
make: Phaser.GameObjects.GameObjectCreator ​
Description:
The Scene Game Object Creator.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L137
Since: 3.0.0
matter ​
matter: Phaser.Physics.Matter.MatterPhysics ​
Description:
The Scene Matter Physics Plugin.
This property will only be available if defined in the Scene Injection Map, the plugin is installed and configured.
Source: src/scene/Scene.js#L249
Since: 3.0.0
physics ​
physics: Phaser.Physics.Arcade.ArcadePhysics ​
Description:
The Scene Arcade Physics Plugin.
This property will only be available if defined in the Scene Injection Map, the plugin is installed and configured.
Source: src/scene/Scene.js#L238
Since: 3.0.0
plugins ​
plugins: Phaser.Plugins.PluginManager ​
Description:
A reference to the global Plugin Manager.
The Plugin Manager is a global system that allows plugins to register themselves with it, and can then install
those plugins into Scenes as required.
Source: src/scene/Scene.js#L285
Since: 3.0.0
registry ​
registry: Phaser.Data.DataManager ​
Description:
A reference to the global Data Manager.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L71
Since: 3.0.0
renderer ​
renderer: Phaser.Renderer.Canvas.CanvasRenderer , Phaser.Renderer.WebGL.WebGLRenderer ​
Description:
A reference to the renderer instance Phaser is using, either Canvas Renderer or WebGL Renderer.
Source: src/scene/Scene.js#L297
Since: 3.50.0
scale ​
scale: Phaser.Scale.ScaleManager ​
Description:
A reference to the global Scale Manager.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L274
Since: 3.16.2
scene ​
scene: Phaser.Scenes.ScenePlugin ​
Description:
A reference to the Scene Manager Plugin.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L148
Since: 3.0.0
sound ​
sound: Phaser.Sound.NoAudioSoundManager , Phaser.Sound.HTML5AudioSoundManager , Phaser.Sound.WebAudioSoundManager ​
Description:
A reference to the Sound Manager.
This property will only be available if defined in the Scene Injection Map and the plugin is installed.
Source: src/scene/Scene.js#L82
Since: 3.0.0
sys ​
sys: Phaser.Scenes.Systems ​
Description:
The Scene Systems. You must never overwrite this property, or all hell will break loose.
Source: src/scene/Scene.js#L29
Since: 3.0.0
textures ​
textures: Phaser.Textures.TextureManager ​
Description:
A reference to the Texture Manager.
This property will only be available if defined in the Scene Injection Map.
Source: src/scene/Scene.js#L93
Since: 3.0.0
time ​
time: Phaser.Time.Clock ​
Description:
The Scene Time and Clock Plugin.
This property will only be available if defined in the Scene Injection Map and the plugin is installed.
Source: src/scene/Scene.js#L216
Since: 3.0.0
tweens ​
tweens: Phaser.Tweens.TweenManager ​
Description:
The Scene Tween Manager Plugin.
This property will only be available if defined in the Scene Injection Map and the plugin is installed.
Source: src/scene/Scene.js#L227
Since: 3.0.0
Public Methods ​
update ​
<instance> update(time, delta) ​
Description:
This method should be overridden by your own Scenes.
This method is called once per game step while the scene is running.
Parameters:
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/scene/Scene.js#L307
Since: 3.0.0
Previous
ScaleManager
Next
SceneManager
Public Members
add
anims
cache
cameras
children
data
events
facebook
game
input
lights
load
make
matter
physics
plugins
registry
renderer
scale
scene
sound
sys
textures
time
tweens
Public Methods
update
