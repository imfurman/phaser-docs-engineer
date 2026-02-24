# GameObject | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-gameobject

Phaser API Documentation
Class
GameObject
Version: Phaser v3.90.0
On this page
GameObject
The base class that all Game Objects extend.
You don't create GameObjects directly and they cannot be added to the display list.
Instead, use them as the base for your own custom classes.
Constructor
new GameObject(scene, type)
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs.
type string No A textual representation of the type of Game Object, i.e. sprite .
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/gameobjects/GameObject.js#L14
Since: 3.0.0
Public Members ​
active ​
active: boolean ​
Description:
The active state of this Game Object.
A Game Object with an active state of true is processed by the Scenes UpdateList, if added to it.
An active object is one which is having its logic and internal systems updated.
Source: src/gameobjects/GameObject.js#L113
Since: 3.0.0
body ​
body: Phaser.Physics.Arcade.Body , Phaser.Physics.Arcade.StaticBody , MatterJS.BodyType ​
Description:
If this Game Object is enabled for Arcade or Matter Physics then this property will contain a reference to a Physics Body.
Source: src/gameobjects/GameObject.js#L186
Since: 3.0.0
cameraFilter ​
cameraFilter: number ​
Description:
A bitmask that controls if this Game Object is drawn by a Camera or not.
Not usually set directly, instead call Camera.ignore , however you can
set this property directly using the Camera.id property:
Source: src/gameobjects/GameObject.js#L160
Since: 3.0.0
data ​
data: Phaser.Data.DataManager ​
Description:
A Data Manager.
It allows you to store, query and get key/value paired information specific to this Game Object.
null by default. Automatically created if you use getData or setData or setDataEnabled .
Source: src/gameobjects/GameObject.js#L136
Since: 3.0.0
displayList ​
displayList: Phaser.GameObjects.DisplayList , Phaser.GameObjects.Layer ​
Description:
Holds a reference to the Display List that contains this Game Object.
This is set automatically when this Game Object is added to a Scene or Layer.
You should treat this property as being read-only.
Source: src/gameobjects/GameObject.js#L53
Since: 3.50.0
ignoreDestroy ​
ignoreDestroy: boolean ​
Description:
This Game Object will ignore all calls made to its destroy method if this flag is set to true .
This includes calls that may come from a Group, Container or the Scene itself.
While it allows you to persist a Game Object across Scenes, please understand you are entirely
responsible for managing references to and from this Game Object.
Source: src/gameobjects/GameObject.js#L196
Since: 3.5.0
input ​
input: Phaser.Types.Input.InteractiveObject ​
Description:
If this Game Object is enabled for input then this property will contain an InteractiveObject instance.
Not usually set directly. Instead call GameObject.setInteractive() .
Source: src/gameobjects/GameObject.js#L175
Since: 3.0.0
name ​
name: string ​
Description:
The name of this Game Object.
Empty by default and never populated by Phaser, this is left for developers to use.
Source: src/gameobjects/GameObject.js#L102
Since: 3.0.0
parentContainer ​
parentContainer: Phaser.GameObjects.Container ​
Description:
The parent Container of this Game Object, if it has one.
Source: src/gameobjects/GameObject.js#L93
Since: 3.4.0
renderFlags ​
renderFlags: number ​
Description:
The flags that are compared against RENDER_MASK to determine if this Game Object will render or not.
The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.
If those components are not used by your custom class then you can use this bitmask as you wish.
Source: src/gameobjects/GameObject.js#L148
Since: 3.0.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene to which this Game Object belongs.
Game Objects can only belong to one Scene.
You should consider this property as being read-only. You cannot move a
Game Object to another Scene by simply changing it.
Source: src/gameobjects/GameObject.js#L39
Since: 3.0.0
state ​
state: number, string ​
Description:
The current state of this Game Object.
Phaser itself will never modify this value, although plugins may do so.
Use this property to track the state of a Game Object during its lifetime. For example, it could change from
a state of 'moving', to 'attacking', to 'dead'. The state value should be an integer (ideally mapped to a constant
in your game code), or a string. These are recommended to keep it light and simple, with fast comparisons.
If you need to store complex data about your Game Object, look at using the Data Component instead.
Source: src/gameobjects/GameObject.js#L77
Since: 3.16.0
tabIndex ​
tabIndex: number ​
Description:
The Tab Index of the Game Object.
Reserved for future use by plugins and the Input Manager.
Source: src/gameobjects/GameObject.js#L125
Since: 3.0.0
type ​
type: string ​
Description:
A textual representation of this Game Object, i.e. sprite .
Used internally by Phaser but is available for your own custom classes to populate.
Source: src/gameobjects/GameObject.js#L67
Since: 3.0.0
Inherited Methods ​
From Phaser.Events.EventEmitter :
addListener
emit
eventNames
listenerCount
listeners
off
on
once
removeAllListeners
removeListener
shutdown
Public Methods ​
addedToScene ​
<instance> addedToScene() ​
Description:
This callback is invoked when this Game Object is added to a Scene.
Can be overriden by custom Game Objects, but be aware of some Game Objects that
will use this, such as Sprites, to add themselves into the Update List.
You can also listen for the ADDED_TO_SCENE event from this Game Object.
Source: src/gameobjects/GameObject.js#L562
Since: 3.50.0
addToDisplayList ​
<instance> addToDisplayList([displayList]) ​
Description:
Adds this Game Object to the given Display List.
If no Display List is specified, it will default to the Display List owned by the Scene to which
this Game Object belongs.
A Game Object can only exist on one Display List at any given time, but may move freely between them.
If this Game Object is already on another Display List when this method is called, it will first
be removed from it, before being added to the new list.
You can query which list it is on by looking at the Phaser.GameObjects.GameObject#displayList property.
If a Game Object isn't on any display list, it will not be rendered. If you just wish to temporarly
disable it from rendering, consider using the setVisible method, instead.
Parameters:
name type optional description
displayList Phaser.GameObjects.DisplayList | Phaser.GameObjects.Layer Yes The Display List to add to. Defaults to the Scene Display List.
Returns: Phaser.GameObjects.GameObject - This Game Object.
Fires: Phaser.Scenes.Events#event:ADDED_TO_SCENE , Phaser.GameObjects.Events#event:ADDED_TO_SCENE
Source: src/gameobjects/GameObject.js#L684
Since: 3.53.0
addToUpdateList ​
<instance> addToUpdateList() ​
Description:
Adds this Game Object to the Update List belonging to the Scene.
When a Game Object is added to the Update List it will have its preUpdate method called
every game frame. This method is passed two parameters: delta and time .
If you wish to run your own logic within preUpdate then you should always call
super.preUpdate(time, delta) within it, or it may fail to process required operations,
such as Sprite animations.
Returns: Phaser.GameObjects.GameObject - This Game Object.
Source: src/gameobjects/GameObject.js#L735
Since: 3.53.0
destroy ​
<instance> destroy([fromScene]) ​
Description:
Destroys this Game Object removing it from the Display List and Update List and
severing all ties to parent resources.
Also removes itself from the Input Manager and Physics Manager if previously enabled.
Use this to remove a Game Object from your game if you don't ever plan to use it again.
As long as no reference to it exists within your own code it should become free for
garbage collection by the browser.
If you just want to temporarily disable an object then look at using the
Game Object Pool instead of destroying it, as destroyed objects cannot be resurrected.
Parameters:
name type optional default description
fromScene boolean Yes false True if this Game Object is being destroyed by the Scene, false if not.
Overrides: Phaser.Events.EventEmitter#destroy
Fires: Phaser.GameObjects.Events#event:DESTROY
Source: src/gameobjects/GameObject.js#L855
Since: 3.0.0
disableInteractive ​
<instance> disableInteractive([resetCursor]) ​
Description:
If this Game Object has previously been enabled for input, this will disable it.
An object that is disabled for input stops processing or being considered for
input events, but can be turned back on again at any time by simply calling
setInteractive() with no arguments provided.
If want to completely remove interaction from this Game Object then use removeInteractive instead.
Parameters:
name type optional default description
resetCursor boolean Yes false Should the currently active Input cursor, if any, be reset to the default cursor?
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L494
Since: 3.7.0
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
Source: src/gameobjects/GameObject.js#L416
Since: 3.0.0
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
Source: src/gameobjects/GameObject.js#L823
Since: 3.85.0
getIndexList ​
<instance> getIndexList() ​
Description:
Returns an array containing the display list index of either this Game Object, or if it has one,
its parent Container. It then iterates up through all of the parent containers until it hits the
root of the display list (which is index 0 in the returned array).
Used internally by the InputPlugin but also useful if you wish to find out the display depth of
this Game Object and all of its ancestors.
Returns: Array.<number> - An array of display list position indexes.
Source: src/gameobjects/GameObject.js#L635
Since: 3.4.0
incData ​
<instance> incData(key, [amount]) ​
Description:
Increase a value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is increased from 0.
If the Game Object has not been enabled for data (via setDataEnabled ) then it will be enabled
before setting the value.
If the key doesn't already exist in the Data Manager then it is created.
When the value is first set, a setdata event is emitted from this Game Object.
Parameters:
name type optional default description
key string No The key to change the value for.
amount number Yes 1 The amount to increase the given key by. Pass a negative value to decrease the key.
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L357
Since: 3.23.0
removedFromScene ​
<instance> removedFromScene() ​
Description:
This callback is invoked when this Game Object is removed from a Scene.
Can be overriden by custom Game Objects, but be aware of some Game Objects that
will use this, such as Sprites, to removed themselves from the Update List.
You can also listen for the REMOVED_FROM_SCENE event from this Game Object.
Source: src/gameobjects/GameObject.js#L577
Since: 3.50.0
removeFromDisplayList ​
<instance> removeFromDisplayList() ​
Description:
Removes this Game Object from the Display List it is currently on.
A Game Object can only exist on one Display List at any given time, but may move freely removed
and added back at a later stage.
You can query which list it is on by looking at the Phaser.GameObjects.GameObject#displayList property.
If a Game Object isn't on any Display List, it will not be rendered. If you just wish to temporarly
disable it from rendering, consider using the setVisible method, instead.
Returns: Phaser.GameObjects.GameObject - This Game Object.
Fires: Phaser.Scenes.Events#event:REMOVED_FROM_SCENE , Phaser.GameObjects.Events#event:REMOVED_FROM_SCENE
Source: src/gameobjects/GameObject.js#L760
Since: 3.53.0
removeFromUpdateList ​
<instance> removeFromUpdateList() ​
Description:
Removes this Game Object from the Scene's Update List.
When a Game Object is on the Update List, it will have its preUpdate method called
every game frame. Calling this method will remove it from the list, preventing this.
Removing a Game Object from the Update List will stop most internal functions working.
For example, removing a Sprite from the Update List will prevent it from being able to
run animations.
Returns: Phaser.GameObjects.GameObject - This Game Object.
Source: src/gameobjects/GameObject.js#L798
Since: 3.53.0
removeInteractive ​
<instance> removeInteractive([resetCursor]) ​
Description:
If this Game Object has previously been enabled for input, this will queue it
for removal, causing it to no longer be interactive. The removal happens on
the next game step, it is not immediate.
The Interactive Object that was assigned to this Game Object will be destroyed,
removed from the Input Manager and cleared from this Game Object.
If you wish to re-enable this Game Object at a later date you will need to
re-create its InteractiveObject by calling setInteractive again.
If you wish to only temporarily stop an object from receiving input then use
disableInteractive instead, as that toggles the interactive state, where-as
this erases it completely.
If you wish to resize a hit area, don't remove and then set it as being
interactive. Instead, access the hitarea object directly and resize the shape
being used. I.e.: sprite.input.hitArea.setSize(width, height) (assuming the
shape is a Rectangle, which it is by default.)
Parameters:
name type optional default description
resetCursor boolean Yes false Should the currently active Input cursor, if any, be reset to the default cursor?
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L519
Since: 3.7.0
setActive ​
<instance> setActive(value) ​
Description:
Sets the active property of this Game Object and returns this Game Object for further chaining.
A Game Object with its active property set to true will be updated by the Scenes UpdateList.
Parameters:
name type optional description
value boolean No True if this Game Object should be set as active, false if not.
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L216
Since: 3.0.0
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
Tags:
generic
genericUse
Parameters:
name type optional description
key string | object No The key to set the value for. Or an object of key value pairs. If an object the data argument is ignored.
data * Yes The value to set for the given key. If an object is provided as the key this argument is ignored.
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L295
Since: 3.0.0
setDataEnabled ​
<instance> setDataEnabled() ​
Description:
Adds a Data Manager component to this Game Object.
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L276
Since: 3.0.0
setInteractive ​
<instance> setInteractive([hitArea], [callback], [dropZone]) ​
Description:
Pass this Game Object to the Input Manager to enable it for Input.
Input works by using hit areas, these are nearly always geometric shapes, such as rectangles or circles, that act as the hit area
for the Game Object. However, you can provide your own hit area shape and callback, should you wish to handle some more advanced
input detection.
If no arguments are provided it will try and create a rectangle hit area based on the texture frame the Game Object is using. If
this isn't a texture-bound object, such as a Graphics or BitmapText object, this will fail, and you'll need to provide a specific
shape for it to use.
You can also provide an Input Configuration Object as the only argument to this method.
Parameters:
name type optional default description
hitArea Phaser.Types.Input.InputConfiguration | any Yes Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not given it will try to create a Rectangle based on the texture frame.
callback Phaser.Types.Input.HitAreaCallback Yes The callback that determines if the pointer is within the Hit Area shape or not. If you provide a shape you must also provide a callback.
dropZone boolean Yes false Should this Game Object be treated as a drop zone target?
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L456
Since: 3.0.0
setName ​
<instance> setName(value) ​
Description:
Sets the name property of this Game Object and returns this Game Object for further chaining.
The name property is not populated by Phaser and is presented for your own use.
Parameters:
name type optional description
value string No The name to be given to this Game Object.
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L234
Since: 3.0.0
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
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L252
Since: 3.16.0
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
key string No The key to toggle the value for.
Returns: Phaser.GameObjects.GameObject - This GameObject.
Source: src/gameobjects/GameObject.js#L387
Since: 3.23.0
toJSON ​
<instance> toJSON() ​
Description:
Returns a JSON representation of the Game Object.
Returns: Phaser.Types.GameObjects.JSONGameObject - A JSON representation of the Game Object.
Source: src/gameobjects/GameObject.js#L604
Since: 3.0.0
update ​
<instance> update([args]) ​
Description:
To be overridden by custom GameObjects. Allows base objects to be used in a Pool.
Parameters:
name type optional description
args * Yes args
Source: src/gameobjects/GameObject.js#L592
Since: 3.0.0
willRender ​
<instance> willRender(camera) ​
Description:
Compares the renderMask with the renderFlags to see if this Game Object will render or not.
Also checks the Game Object against the given Cameras exclusion list.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The Camera to check against this Game Object.
Returns: boolean - True if the Game Object should be rendered, otherwise false.
Source: src/gameobjects/GameObject.js#L617
Since: 3.0.0
Constants: ​
Public Members ​
RENDER_MASK ​
RENDER_MASK: number ​
Description:
The bitmask that GameObject.renderFlags is compared against to determine if the Game Object will render or not.
Source: src/gameobjects/GameObject.js#L945
Previous
Extern
Next
GameObjectCreator
Public Members
active
body
cameraFilter
data
displayList
ignoreDestroy
input
name
parentContainer
renderFlags
scene
state
tabIndex
type
Inherited Methods
Public Methods
addedToScene
addToDisplayList
addToUpdateList
destroy
disableInteractive
getData
getDisplayList
getIndexList
incData
removedFromScene
removeFromDisplayList
removeFromUpdateList
removeInteractive
setActive
setData
setDataEnabled
setInteractive
setName
setState
toggleData
toJSON
update
willRender
Constants:
Public Members
RENDER_MASK
