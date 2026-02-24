# GameObjectCreator | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-gameobjectcreator

Phaser API Documentation
Class
GameObjectCreator
Version: Phaser v3.90.0
On this page
GameObjectCreator
The Game Object Creator is a Scene plugin that allows you to quickly create many common
types of Game Objects and return them using a configuration object, rather than
having to specify a limited set of parameters such as with the GameObjectFactory.
Game Objects made via this class are automatically added to the Scene and Update List
unless you explicitly set the add property in the configuration object to false .
Constructor
new GameObjectCreator(scene)
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object Factory belongs.
Scope : static
Source: src/gameobjects/GameObjectCreator.js#L11
Since: 3.0.0
Public Members ​
displayList ​
displayList: Phaser.GameObjects.DisplayList ​
Description:
A reference to the Scene Display List.
Access: protected
Source: src/gameobjects/GameObjectCreator.js#L63
Since: 3.0.0
events ​
events: Phaser.Events.EventEmitter ​
Description:
A reference to the Scene Event Emitter.
Access: protected
Source: src/gameobjects/GameObjectCreator.js#L53
Since: 3.50.0
scene ​
scene: Phaser.Scene ​
Description:
The Scene to which this Game Object Creator belongs.
Access: protected
Source: src/gameobjects/GameObjectCreator.js#L33
Since: 3.0.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
A reference to the Scene.Systems.
Access: protected
Source: src/gameobjects/GameObjectCreator.js#L43
Since: 3.0.0
updateList ​
updateList: Phaser.GameObjects.UpdateList ​
Description:
A reference to the Scene Update List.
Access: protected
Source: src/gameobjects/GameObjectCreator.js#L73
Since: 3.0.0
Public Methods ​
bitmapText ​
<instance> bitmapText(config, [addToScene]) ​
Description:
Creates a new Bitmap Text Game Object and returns it.
Note: This method will only be available if the Bitmap Text Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.BitmapText.BitmapTextConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.BitmapText - The Game Object that was created.
Source: src/gameobjects/bitmaptext/static/BitmapTextCreator.js#L13
Since: 3.0.0
blitter ​
<instance> blitter(config, [addToScene]) ​
Description:
Creates a new Blitter Game Object and returns it.
Note: This method will only be available if the Blitter Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Sprite.SpriteConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Blitter - The Game Object that was created.
Source: src/gameobjects/blitter/BlitterCreator.js#L12
Since: 3.0.0
container ​
<instance> container(config, [addToScene]) ​
Description:
Creates a new Container Game Object and returns it.
Note: This method will only be available if the Container Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Container.ContainerConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Container - The Game Object that was created.
Source: src/gameobjects/container/ContainerCreator.js#L14
Since: 3.4.0
dynamicBitmapText ​
<instance> dynamicBitmapText(config, [addToScene]) ​
Description:
Creates a new Dynamic Bitmap Text Game Object and returns it.
Note: This method will only be available if the Dynamic Bitmap Text Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.BitmapText.BitmapTextConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.DynamicBitmapText - The Game Object that was created.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapTextCreator.js#L12
Since: 3.0.0 ²
graphics ​
<instance> graphics([config], [addToScene]) ​
Description:
Creates a new Graphics Game Object and returns it.
Note: This method will only be available if the Graphics Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Graphics.Options Yes The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Graphics - The Game Object that was created.
Source: src/gameobjects/graphics/GraphicsCreator.js#L10
Since: 3.0.0
group ​
<instance> group(config) ​
Description:
Creates a new Group Game Object and returns it.
Note: This method will only be available if the Group Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Group.GroupConfig | Phaser.Types.GameObjects.Group.GroupCreateConfig No The configuration object this Game Object will use to create itself.
Returns: Phaser.GameObjects.Group - The Game Object that was created.
Source: src/gameobjects/group/GroupCreator.js#L10
Since: 3.0.0
image ​
<instance> image(config, [addToScene]) ​
Description:
Creates a new Image Game Object and returns it.
Note: This method will only be available if the Image Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Sprite.SpriteConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Image - The Game Object that was created.
Source: src/gameobjects/image/ImageCreator.js#L12
Since: 3.0.0
layer ​
<instance> layer(config, [addToScene]) ​
Description:
Creates a new Layer Game Object and returns it.
Note: This method will only be available if the Layer Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Sprite.SpriteConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Layer - The Game Object that was created.
Source: src/gameobjects/layer/LayerCreator.js#L12
Since: 3.50.0
mesh ​
<instance> mesh(config, [addToScene]) ​
Description:
Creates a new Mesh Game Object and returns it.
Note: This method will only be available if the Mesh Game Object and WebGL support have been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Mesh.MeshConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Mesh - The Game Object that was created.
Source: src/gameobjects/mesh/MeshCreator.js#L13
Since: 3.0.0
nineslice ​
<instance> nineslice(config, [addToScene]) ​
Description:
Creates a new Nine Slice Game Object and returns it.
Note: This method will only be available if the Nine Slice Game Object and WebGL support have been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.NineSlice.NineSliceConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.NineSlice - The Game Object that was created.
Source: src/gameobjects/nineslice/NineSliceCreator.js#L13
Since: 3.60.0
particles ​
<instance> particles(config, [addToScene]) ​
Description:
Creates a new Particle Emitter Game Object and returns it.
Prior to Phaser v3.60 this function would create a ParticleEmitterManager . These were removed
in v3.60 and replaced with creating a ParticleEmitter instance directly. Please see the
updated function parameters and class documentation for more details.
Note: This method will only be available if the Particles Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Particles.ParticleEmitterCreatorConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - The Game Object that was created.
Source: src/gameobjects/particles/ParticleEmitterCreator.js#L13
Since: 3.0.0
plane ​
<instance> plane(config, [addToScene]) ​
Description:
Creates a new Plane Game Object and returns it.
Note: This method will only be available if the Plane Game Object and WebGL support have been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Plane.PlaneConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Plane - The Game Object that was created.
Source: src/gameobjects/plane/PlaneCreator.js#L14
Since: 3.60.0
pointlight ​
<instance> pointlight(config, [addToScene]) ​
Description:
Creates a new Point Light Game Object and returns it.
Note: This method will only be available if the Point Light Game Object has been built into Phaser.
Parameters:
name type optional description
config object No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.PointLight - The Game Object that was created.
Source: src/gameobjects/pointlight/PointLightCreator.js#L12
Since: 3.50.0
register ​
<static> register(factoryType, factoryFunction) ​
Description:
Static method called directly by the Game Object creator functions.
With this method you can register a custom GameObject factory in the GameObjectCreator,
providing a name ( factoryType ) and the constructor ( factoryFunction ) in order
to be called when you invoke Phaser.Scene.make[ factoryType ] method.
Parameters:
name type optional description
factoryType string No The key of the factory that you will use to call to Phaser.Scene.make[ factoryType ] method.
factoryFunction function No The constructor function to be called when you invoke to the Phaser.Scene.make method.
Source: src/gameobjects/GameObjectCreator.js#L154
Since: 3.0.0
remove ​
<static> remove(factoryType) ​
Description:
Static method called directly by the Game Object Creator functions.
With this method you can remove a custom Game Object Creator that has been previously
registered in the Game Object Creator. Pass in its factoryType in order to remove it.
Parameters:
name type optional description
factoryType string No The key of the factory that you want to remove from the GameObjectCreator.
Source: src/gameobjects/GameObjectCreator.js#L175
Since: 3.0.0
renderTexture ​
<instance> renderTexture(config, [addToScene]) ​
Description:
Creates a new Render Texture Game Object and returns it.
Note: This method will only be available if the Render Texture Game Object has been built into Phaser.
A Render Texture is a combination of Dynamic Texture and an Image Game Object, that uses the
Dynamic Texture to display itself with.
A Dynamic Texture is a special texture that allows you to draw textures, frames and most kind of
Game Objects directly to it.
You can take many complex objects and draw them to this one texture, which can then be used as the
base texture for other Game Objects, such as Sprites. Should you then update this texture, all
Game Objects using it will instantly be updated as well, reflecting the changes immediately.
It's a powerful way to generate dynamic textures at run-time that are WebGL friendly and don't invoke
expensive GPU uploads on each change.
Parameters:
name type optional description
config Phaser.Types.GameObjects.RenderTexture.RenderTextureConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.RenderTexture - The Game Object that was created.
Source: src/gameobjects/rendertexture/RenderTextureCreator.js#L12
Since: 3.2.0
rope ​
<instance> rope(config, [addToScene]) ​
Description:
Creates a new Rope Game Object and returns it.
Note: This method will only be available if the Rope Game Object and WebGL support have been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Rope.RopeConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Rope - The Game Object that was created.
Source: src/gameobjects/rope/RopeCreator.js#L13
Since: 3.23.0
shader ​
<instance> shader(config, [addToScene]) ​
Description:
Creates a new Shader Game Object and returns it.
Note: This method will only be available if the Shader Game Object and WebGL support have been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Shader.ShaderConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Shader - The Game Object that was created.
Source: src/gameobjects/shader/ShaderCreator.js#L12
Since: 3.17.0
sprite ​
<instance> sprite(config, [addToScene]) ​
Description:
Creates a new Sprite Game Object and returns it.
Note: This method will only be available if the Sprite Game Object has been built into Phaser.
Parameters:
name type optional default description
config Phaser.Types.GameObjects.Sprite.SpriteConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes true Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Sprite - The Game Object that was created.
Source: src/gameobjects/sprite/SpriteCreator.js#L13
Since: 3.0.0
text ​
<instance> text(config, [addToScene]) ​
Description:
Creates a new Text Game Object and returns it.
Note: This method will only be available if the Text Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Text.TextConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Text - The Game Object that was created.
Source: src/gameobjects/text/TextCreator.js#L12
Since: 3.0.0
tilemap ​
<instance> tilemap([config]) ​
Description:
Creates a Tilemap from the given key or data, or creates a blank Tilemap if no key/data provided.
When loading from CSV or a 2D array, you should specify the tileWidth & tileHeight. When parsing
from a map from Tiled, the tileWidth, tileHeight, width & height will be pulled from the map
data. For an empty map, you should specify tileWidth, tileHeight, width & height.
Parameters:
name type optional description
config Phaser.Types.Tilemaps.TilemapConfig Yes The config options for the Tilemap.
Returns: Phaser.Tilemaps.Tilemap - undefined
Source: src/tilemaps/TilemapCreator.js#L10
Since: 3.0.0
tileSprite ​
<instance> tileSprite(config, [addToScene]) ​
Description:
Creates a new TileSprite Game Object and returns it.
Note: This method will only be available if the TileSprite Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.TileSprite.TileSpriteConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.TileSprite - The Game Object that was created.
Source: src/gameobjects/tilesprite/TileSpriteCreator.js#L12
Since: 3.0.0
tween ​
<instance> tween(config) ​
Description:
Creates a new Tween object and returns it.
Note: This method will only be available if Tweens have been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.Tweens.TweenBuilderConfig | Phaser.Types.Tweens.TweenChainBuilderConfig Phaser.Tweens.Tween Phaser.Tweens.TweenChain
Returns: Phaser.Tweens.Tween - The Tween that was created.
Source: src/tweens/tween/Tween.js#L850
Since: 3.0.0
tweenchain ​
<instance> tweenchain(config) ​
Description:
Creates a new TweenChain object and returns it, without adding it to the Tween Manager.
Note: This method will only be available if Tweens have been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.Tweens.TweenBuilderConfig | object No The TweenChain configuration.
Returns: Phaser.Tweens.TweenChain - The TweenChain that was created.
Source: src/tweens/tween/TweenChain.js#L566
Since: 3.60.0
video ​
<instance> video(config, [addToScene]) ​
Description:
Creates a new Video Game Object and returns it.
Note: This method will only be available if the Video Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Video.VideoConfig No The configuration object this Game Object will use to create itself.
addToScene boolean Yes Add this Game Object to the Scene after creating it? If set this argument overrides the add property in the config object.
Returns: Phaser.GameObjects.Video - The Game Object that was created.
Source: src/gameobjects/video/VideoCreator.js#L12
Since: 3.20.0
zone ​
<instance> zone(config) ​
Description:
Creates a new Zone Game Object and returns it.
Note: This method will only be available if the Zone Game Object has been built into Phaser.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Zone.ZoneConfig No The configuration object this Game Object will use to create itself.
Returns: Phaser.GameObjects.Zone - The Game Object that was created.
Source: src/gameobjects/zone/ZoneCreator.js#L11
Since: 3.0.0
Previous
GameObject
Next
GameObjectFactory
Public Members
displayList
events
scene
systems
updateList
Public Methods
bitmapText
blitter
container
dynamicBitmapText
graphics
group
image
layer
mesh
nineslice
particles
plane
pointlight
register
remove
renderTexture
rope
shader
sprite
text
tilemap
tileSprite
tween
tweenchain
video
zone
