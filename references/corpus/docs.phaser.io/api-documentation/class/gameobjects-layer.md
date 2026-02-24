# Layer | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-layer

Phaser API Documentation
Class
Layer
Version: Phaser v3.90.0
On this page
Layer
A Layer Game Object.
A Layer is a special type of Game Object that acts as a Display List. You can add any type of Game Object
to a Layer, just as you would to a Scene. Layers can be used to visually group together 'layers' of Game
Objects:
const spaceman = this . add . sprite ( 150 , 300 , 'spaceman' ) ;
const bunny = this . add . sprite ( 400 , 300 , 'bunny' ) ;
const elephant = this . add . sprite ( 650 , 300 , 'elephant' ) ;
const layer = this . add . layer ( ) ;
layer . add ( [ spaceman , bunny , elephant ] ) ;
The 3 sprites in the example above will now be managed by the Layer they were added to. Therefore,
if you then set layer.setVisible(false) they would all vanish from the display.
You can also control the depth of the Game Objects within the Layer. For example, calling the
setDepth method of a child of a Layer will allow you to adjust the depth of that child _within the
Layer itself_, rather than the whole Scene. The Layer, too, can have its depth set as well.
The Layer class also offers many different methods for manipulating the list, such as the
methods moveUp , moveDown , sendToBack , bringToTop and so on. These allow you to change the
display list position of the Layers children, causing it to adjust the order in which they are
rendered. Using setDepth on a child allows you to override this.
Layers can have Post FX Pipelines set, which allows you to easily enable a post pipeline across
a whole range of children, which, depending on the effect, can often be far more efficient that doing so
on a per-child basis.
Layers have no position or size within the Scene. This means you cannot enable a Layer for
physics or input, or change the position, rotation or scale of a Layer. They also have no scroll
factor, texture, tint, origin, crop or bounds.
If you need those kind of features then you should use a Container instead. Containers can be added
to Layers, but Layers cannot be added to Containers.
However, you can set the Alpha, Blend Mode, Depth, Mask and Visible state of a Layer. These settings
will impact all children being rendered by the Layer.
Constructor
new Layer(scene, [children])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
children Array.< Phaser.GameObjects.GameObject > Yes An optional array of Game Objects to add to this Layer.
Scope : static
Extends
Phaser.Structs.List.<Phaser.GameObjects.GameObject>
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/layer/Layer.js#L19
Since: 3.50.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
From Phaser.GameObjects.Components.Visible :
visible
Public Members ​
active ​
active: boolean ​
Description:
The active state of this Game Object.
A Game Object with an active state of true is processed by the Scenes UpdateList, if added to it.
An active object is one which is having its logic and internal systems updated.
Source: src/gameobjects/layer/Layer.js#L178
Since: 3.50.0
body ​
body: Phaser.Physics.Arcade.Body , Phaser.Physics.Arcade.StaticBody , MatterJS.BodyType ​
Description:
This property is kept purely so a Layer has the same
shape as a Game Object. You cannot give a Layer a physics body.
Source: src/gameobjects/layer/Layer.js#L251
Since: 3.51.0
cameraFilter ​
cameraFilter: number ​
Description:
A bitmask that controls if this Game Object is drawn by a Camera or not.
Not usually set directly, instead call Camera.ignore , however you can
set this property directly using the Camera.id property:
Source: src/gameobjects/layer/Layer.js#L225
Since: 3.50.0
data ​
data: Phaser.Data.DataManager ​
Description:
A Data Manager.
It allows you to store, query and get key/value paired information specific to this Game Object.
null by default. Automatically created if you use getData or setData or setDataEnabled .
Source: src/gameobjects/layer/Layer.js#L201
Since: 3.50.0
displayList ​
displayList: Phaser.GameObjects.DisplayList , Phaser.GameObjects.Layer ​
Description:
Holds a reference to the Display List that contains this Game Object.
This is set automatically when this Game Object is added to a Scene or Layer.
You should treat this property as being read-only.
Source: src/gameobjects/layer/Layer.js#L115
Since: 3.50.0
events ​
events: Phaser.Events.EventEmitter ​
Description:
A reference to the Scene Event Emitter.
Source: src/gameobjects/layer/Layer.js#L284
Since: 3.50.0
ignoreDestroy ​
ignoreDestroy: boolean ​
Description:
This Game Object will ignore all calls made to its destroy method if this flag is set to true .
This includes calls that may come from a Group, Container or the Scene itself.
While it allows you to persist a Game Object across Scenes, please understand you are entirely
responsible for managing references to and from this Game Object.
Source: src/gameobjects/layer/Layer.js#L262
Since: 3.50.0
input ​
input: Phaser.Types.Input.InteractiveObject ​
Description:
This property is kept purely so a Layer has the same
shape as a Game Object. You cannot input enable a Layer.
Source: src/gameobjects/layer/Layer.js#L240
Since: 3.51.0
name ​
name: string ​
Description:
The name of this Game Object.
Empty by default and never populated by Phaser, this is left for developers to use.
Source: src/gameobjects/layer/Layer.js#L167
Since: 3.50.0
parentContainer ​
parentContainer: Phaser.GameObjects.Container ​
Description:
A Layer cannot be placed inside a Container.
This property is kept purely so a Layer has the same
shape as a Game Object.
Source: src/gameobjects/layer/Layer.js#L155
Since: 3.51.0
renderFlags ​
renderFlags: number ​
Description:
The flags that are compared against RENDER_MASK to determine if this Game Object will render or not.
The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.
If those components are not used by your custom class then you can use this bitmask as you wish.
Source: src/gameobjects/layer/Layer.js#L213
Since: 3.50.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene to which this Game Object belongs.
Game Objects can only belong to one Scene.
You should consider this property as being read-only. You cannot move a
Game Object to another Scene by simply changing it.
Source: src/gameobjects/layer/Layer.js#L101
Since: 3.50.0
sortChildrenFlag ​
sortChildrenFlag: boolean ​
Description:
The flag the determines whether Game Objects should be sorted when depthSort() is called.
Source: src/gameobjects/layer/Layer.js#L293
Since: 3.50.0
state ​
state: number, string ​
Description:
The current state of this Game Object.
Phaser itself will never modify this value, although plugins may do so.
Use this property to track the state of a Game Object during its lifetime. For example, it could change from
a state of 'moving', to 'attacking', to 'dead'. The state value should be an integer (ideally mapped to a constant
in your game code), or a string. These are recommended to keep it light and simple, with fast comparisons.
If you need to store complex data about your Game Object, look at using the Data Component instead.
Source: src/gameobjects/layer/Layer.js#L139
Since: 3.50.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
A reference to the Scene Systems.
Source: src/gameobjects/layer/Layer.js#L275
Since: 3.50.0
tabIndex ​
tabIndex: number ​
Description:
The Tab Index of the Game Object.
Reserved for future use by plugins and the Input Manager.
Source: src/gameobjects/layer/Layer.js#L190
Since: 3.51.0
type ​
type: string ​
Description:
A textual representation of this Game Object, i.e. sprite .
Used internally by Phaser but is available for your own custom classes to populate.
Source: src/gameobjects/layer/Layer.js#L129
Since: 3.50.0
Inherited Methods ​
From Phaser.GameObjects.Components.AlphaSingle :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
From Phaser.GameObjects.Components.Visible :
setVisible
Public Methods ​
addedToScene ​
<instance> addedToScene() ​
Description:
This callback is invoked when this Game Object is added to a Scene.
Can be overriden by custom Game Objects, but be aware of some Game Objects that
will use this, such as Sprites, to add themselves into the Update List.
You can also listen for the ADDED_TO_SCENE event from this Game Object.
Source: src/gameobjects/layer/Layer.js#L607
Since: 3.50.0
addToDisplayList ​
<instance> addToDisplayList([displayList]) ​
Description:
Adds this Layer to the given Display List.
If no Display List is specified, it will default to the Display List owned by the Scene to which
this Layer belongs.
A Layer can only exist on one Display List at any given time, but may move freely between them.
If this Layer is already on another Display List when this method is called, it will first
be removed from it, before being added to the new list.
You can query which list it is on by looking at the Phaser.GameObjects.Layer#displayList property.
If a Layer isn't on any display list, it will not be rendered. If you just wish to temporarily
disable it from rendering, consider using the setVisible method, instead.
Parameters:
name type optional description
displayList Phaser.GameObjects.DisplayList | Phaser.GameObjects.Layer Yes The Display List to add to. Defaults to the Scene Display List.
Returns: Phaser.GameObjects.Layer - This Layer instance.
Fires: Phaser.Scenes.Events#event:ADDED_TO_SCENE , Phaser.GameObjects.Events#event:ADDED_TO_SCENE
Source: src/gameobjects/layer/Layer.js#L832
Since: 3.60.0
depthSort ​
<instance> depthSort() ​
Description:
Immediately sorts the display list if the flag is set.
Source: src/gameobjects/layer/Layer.js#L785
Since: 3.50.0
destroy ​
<instance> destroy([fromScene]) ​
Description:
Destroys this Layer removing it from the Display List and Update List and
severing all ties to parent resources.
Also destroys all children of this Layer. If you do not wish for the
children to be destroyed, you should move them from this Layer first.
Use this to remove this Layer from your game if you don't ever plan to use it again.
As long as no reference to it exists within your own code it should become free for
garbage collection by the browser.
If you just want to temporarily disable an object then look at using the
Game Object Pool instead of destroying it, as destroyed objects cannot be resurrected.
Parameters:
name type optional default description
fromScene boolean Yes false True if this Game Object is being destroyed by the Scene, false if not.
Fires: Phaser.GameObjects.Events#event:DESTROY
Source: src/gameobjects/layer/Layer.js#L953
Since: 3.50.0
disableInteractive ​
<instance> disableInteractive() ​
Description:
A Layer cannot be enabled for input.
This method does nothing and is kept to ensure
the Layer has the same shape as a Game Object.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L575
Since: 3.51.0
getChildren ​
<instance> getChildren() ​
Description:
Returns a reference to the array which contains all Game Objects in this Layer.
This is a reference, not a copy of it, so be very careful not to mutate it.
Returns: Array.< Phaser.GameObjects.GameObject > - An array of Game Objects within this Layer.
Source: src/gameobjects/layer/Layer.js#L817
Since: 3.50.0
getData ​
<instance> getData(key) ​
Description:
Retrieves the value for the given key in this Game Objects Data Manager, or undefined if it doesn't exist.
You can also access values via the values object. For example, if you had a key called gold you can do either:
sprite . getData ( 'gold' ) ;
Or access the value directly:
sprite . data . values . gold ;
You can also pass in an array of keys, in which case an array of values will be returned:
sprite . getData ( [ 'gold' , 'armor' , 'health' ] ) ;
This approach is useful for destructuring arrays in ES6.
Parameters:
name type optional description
key string | Array.<string> No The key of the value to retrieve, or an array of keys.
Returns: * - The value belonging to the given key, or an array of values, the order of which will match the input array.
Source: src/gameobjects/layer/Layer.js#L519
Since: 3.50.0
getDisplayList ​
<instance> getDisplayList() ​
Description:
Returns a reference to the underlying display list array that contains this Game Object,
which will be either the Scene's Display List or the internal list belonging
to its parent Container, if it has one.
If this Game Object is not on a display list or in a container, it will return null .
You should be very careful with this method, and understand that it returns a direct reference to the
internal array used by the Display List. Mutating this array directly can cause all kinds of subtle
and difficult to debug issues in your game.
Returns: Array.< Phaser.GameObjects.GameObject > - The internal Display List array of Game Objects, or null .
Source: src/gameobjects/layer/Layer.js#L921
Since: 3.88.0
getIndexList ​
<instance> getIndexList() ​
Description:
Returns an array containing the display list index of either this Game Object, or if it has one,
its parent Container. It then iterates up through all of the parent containers until it hits the
root of the display list (which is index 0 in the returned array).
Used internally by the InputPlugin but also useful if you wish to find out the display depth of
this Game Object and all of its ancestors.
Returns: Array.<number> - An array of display list position indexes.
Source: src/gameobjects/layer/Layer.js#L678
Since: 3.51.0
incData ​
<instance> incData(key, [data]) ​
Description:
Increase a value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is increased from 0.
If the Game Object has not been enabled for data (via setDataEnabled ) then it will be enabled
before setting the value.
If the key doesn't already exist in the Data Manager then it is created.
When the value is first set, a setdata event is emitted from this Game Object.
Parameters:
name type optional description
key string | object No The key to increase the value for.
data * Yes The value to increase for the given key.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L460
Since: 3.50.0
queueDepthSort ​
<instance> queueDepthSort() ​
Description:
Force a sort of the display list on the next call to depthSort.
Source: src/gameobjects/layer/Layer.js#L774
Since: 3.50.0
removedFromScene ​
<instance> removedFromScene() ​
Description:
This callback is invoked when this Game Object is removed from a Scene.
Can be overriden by custom Game Objects, but be aware of some Game Objects that
will use this, such as Sprites, to removed themselves from the Update List.
You can also listen for the REMOVED_FROM_SCENE event from this Game Object.
Source: src/gameobjects/layer/Layer.js#L622
Since: 3.50.0
removeFromDisplayList ​
<instance> removeFromDisplayList() ​
Description:
Removes this Layer from the Display List it is currently on.
A Layer can only exist on one Display List at any given time, but may move freely removed
and added back at a later stage.
You can query which list it is on by looking at the Phaser.GameObjects.GameObject#displayList property.
If a Layer isn't on any Display List, it will not be rendered. If you just wish to temporarily
disable it from rendering, consider using the setVisible method, instead.
Returns: Phaser.GameObjects.Layer - This Layer instance.
Fires: Phaser.Scenes.Events#event:REMOVED_FROM_SCENE , Phaser.GameObjects.Events#event:REMOVED_FROM_SCENE
Source: src/gameobjects/layer/Layer.js#L883
Since: 3.60.0
removeInteractive ​
<instance> removeInteractive() ​
Description:
A Layer cannot be enabled for input.
This method does nothing and is kept to ensure
the Layer has the same shape as a Game Object.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L591
Since: 3.51.0
setActive ​
<instance> setActive(value) ​
Description:
Sets the active property of this Game Object and returns this Game Object for further chaining.
A Game Object with its active property set to true will be updated by the Scenes UpdateList.
Parameters:
name type optional description
value boolean No True if this Game Object should be set as active, false if not.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L322
Since: 3.50.0
setData ​
<instance> setData(key, [data]) ​
Description:
Allows you to store a key value pair within this Game Objects Data Manager.
If the Game Object has not been enabled for data (via setDataEnabled ) then it will be enabled
before setting the value.
If the key doesn't already exist in the Data Manager then it is created.
sprite . setData ( 'name' , 'Red Gem Stone' ) ;
You can also pass in an object of key value pairs as the first argument:
sprite . setData ( { name : 'Red Gem Stone' , level : 2 , owner : 'Link' , gold : 50 } ) ;
To get a value back again you can call getData :
sprite . getData ( 'gold' ) ;
Or you can access the value directly via the values property, where it works like any other variable:
sprite . data . values . gold += 50 ;
When the value is first set, a setdata event is emitted from this Game Object.
If the key already exists, a changedata event is emitted instead, along an event named after the key.
For example, if you updated an existing key called PlayerLives then it would emit the event changedata-PlayerLives .
These events will be emitted regardless if you use this method to set the value, or the direct values setter.
Please note that the data keys are case-sensitive and must be valid JavaScript Object property strings.
This means the keys gold and Gold are treated as two unique values within the Data Manager.
Parameters:
name type optional description
key string | object No The key to set the value for. Or an object of key value pairs. If an object the data argument is ignored.
data * Yes The value to set for the given key. If an object is provided as the key this argument is ignored.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L401
Since: 3.50.0
setDataEnabled ​
<instance> setDataEnabled() ​
Description:
Adds a Data Manager component to this Game Object.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L382
Since: 3.50.0
setInteractive ​
<instance> setInteractive() ​
Description:
A Layer cannot be enabled for input.
This method does nothing and is kept to ensure
the Layer has the same shape as a Game Object.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L559
Since: 3.51.0
setName ​
<instance> setName(value) ​
Description:
Sets the name property of this Game Object and returns this Game Object for further chaining.
The name property is not populated by Phaser and is presented for your own use.
Parameters:
name type optional description
value string No The name to be given to this Game Object.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L340
Since: 3.50.0
setState ​
<instance> setState(value) ​
Description:
Sets the current state of this Game Object.
Phaser itself will never modify the State of a Game Object, although plugins may do so.
For example, a Game Object could change from a state of 'moving', to 'attacking', to 'dead'.
The state value should typically be an integer (ideally mapped to a constant
in your game code), but could also be a string. It is recommended to keep it light and simple.
If you need to store complex data about your Game Object, look at using the Data Component instead.
Parameters:
name type optional description
value number | string No The state of the Game Object.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L358
Since: 3.50.0
sortByDepth ​
<instance> sortByDepth(childA, childB) ​
Description:
Compare the depth of two Game Objects.
Parameters:
name type optional description
childA Phaser.GameObjects.GameObject No The first Game Object.
childB Phaser.GameObjects.GameObject No The second Game Object.
Returns: number - The difference between the depths of each Game Object.
Source: src/gameobjects/layer/Layer.js#L801
Since: 3.50.0
toggleData ​
<instance> toggleData(key) ​
Description:
Toggle a boolean value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is toggled from false.
If the Game Object has not been enabled for data (via setDataEnabled ) then it will be enabled
before setting the value.
If the key doesn't already exist in the Data Manager then it is created.
When the value is first set, a setdata event is emitted from this Game Object.
Parameters:
name type optional description
key string | object No The key to toggle the value for.
Returns: Phaser.GameObjects.Layer - This GameObject.
Source: src/gameobjects/layer/Layer.js#L490
Since: 3.50.0
toJSON ​
<instance> toJSON() ​
Description:
Returns a JSON representation of the Game Object.
Returns: Phaser.Types.GameObjects.JSONGameObject - A JSON representation of the Game Object.
Source: src/gameobjects/layer/Layer.js#L649
Since: 3.50.0
update ​
<instance> update([args]) ​
Description:
To be overridden by custom GameObjects. Allows base objects to be used in a Pool.
Parameters:
name type optional description
args * Yes args
Source: src/gameobjects/layer/Layer.js#L637
Since: 3.50.0
willRender ​
<instance> willRender(camera) ​
Description:
Compares the renderMask with the renderFlags to see if this Game Object will render or not.
Also checks the Game Object against the given Cameras exclusion list.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The Camera to check against this Game Object.
Returns: boolean - True if the Game Object should be rendered, otherwise false.
Source: src/gameobjects/layer/Layer.js#L662
Since: 3.50.0
Previous
IsoTriangle
Next
Light
Inherited Members
Public Members
active
body
cameraFilter
data
displayList
events
ignoreDestroy
input
name
parentContainer
renderFlags
scene
sortChildrenFlag
state
systems
tabIndex
type
Inherited Methods
Public Methods
addedToScene
addToDisplayList
depthSort
destroy
disableInteractive
getChildren
getData
getDisplayList
getIndexList
incData
queueDepthSort
removedFromScene
removeFromDisplayList
removeInteractive
setActive
setData
setDataEnabled
setInteractive
setName
setState
sortByDepth
toggleData
toJSON
update
willRender
