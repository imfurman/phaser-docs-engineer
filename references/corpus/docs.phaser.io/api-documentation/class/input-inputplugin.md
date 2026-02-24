# InputPlugin | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-inputplugin

Phaser API Documentation
Class
InputPlugin
Version: Phaser v3.90.0
On this page
InputPlugin
The Input Plugin belongs to a Scene and handles all input related events and operations for it.
You can access it from within a Scene using this.input .
It emits events directly. For example, you can do:
this . input . on ( 'pointerdown' , callback , context ) ;
To listen for a pointer down event anywhere on the game canvas.
Game Objects can be enabled for input by calling their setInteractive method. After which they
will directly emit input events:
var sprite = this . add . sprite ( x , y , texture ) ;
sprite . setInteractive ( ) ;
sprite . on ( 'pointerdown' , callback , context ) ;
There are lots of game configuration options available relating to input.
See the [Input Config object](code Phaser.Types.Core.InputConfig) for more details, including how to deal with Phaser
listening for input events outside of the canvas, how to set a default number of pointers, input
capture settings and more.
Please also see the Input examples and tutorials for further information.
Incorrect input coordinates with Angular
If you are using Phaser within Angular, and use nglf or the router, to make the component in which the Phaser game resides
change state (i.e. appear or disappear) then you'll need to notify the Scale Manager about this, as Angular will mess with
the DOM in a way in which Phaser can't detect directly. Call this.scale.updateBounds() as part of your game init in order
to refresh the canvas DOM bounds values, which Phaser uses for input point position calculations.
Constructor
new InputPlugin(scene)
Parameters
name type optional description
scene Phaser.Scene No A reference to the Scene that this Input Plugin is responsible for.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/input/InputPlugin.js#L29
Since: 3.0.0
Public Members ​
activePointer ​
activePointer: Phaser.Input.Pointer ​
Description:
The current active input Pointer.
Source: src/input/InputPlugin.js#L3271
Since: 3.0.0
cameras ​
cameras: Phaser.Cameras.Scene2D.CameraManager ​
Description:
A reference to the Scene Cameras Manager. This property is set during the boot method.
Source: src/input/InputPlugin.js#L149
Since: 3.0.0
displayList ​
displayList: Phaser.GameObjects.DisplayList ​
Description:
A reference to the Scene Display List. This property is set during the boot method.
Source: src/input/InputPlugin.js#L140
Since: 3.0.0
dragDistanceThreshold ​
dragDistanceThreshold: number ​
Description:
The distance, in pixels, a pointer has to move while being held down, before it thinks it is being dragged.
Source: src/input/InputPlugin.js#L247
Since: 3.0.0
dragTimeThreshold ​
dragTimeThreshold: number ​
Description:
The amount of time, in ms, a pointer has to be held down before it thinks it is dragging.
The default polling rate is to poll only on move so once the time threshold is reached the
drag event will not start until you move the mouse. If you want it to start immediately
when the time threshold is reached, you must increase the polling rate by calling
setPollAlways or
setPollRate .
Source: src/input/InputPlugin.js#L257
Since: 3.0.0
enabled ​
enabled: boolean ​
Description:
If true this Input Plugin will process DOM input events.
Source: src/input/InputPlugin.js#L130
Since: 3.5.0
gamepad ​
gamepad: Phaser.Input.Gamepad.GamepadPlugin ​
Description:
An instance of the Gamepad Plugin class, if enabled via the input.gamepad Scene or Game Config property.
Use this to create access Gamepads connected to the browser and respond to gamepad buttons.
Source: src/input/gamepad/GamepadPlugin.js#L630
Since: 3.10.0
isOver ​
isOver: boolean ​
Description:
Are any mouse or touch pointers currently over the game canvas?
Source: src/input/InputPlugin.js#L3235
Since: 3.16.0
keyboard ​
keyboard: Phaser.Input.Keyboard.KeyboardPlugin ​
Description:
An instance of the Keyboard Plugin class, if enabled via the input.keyboard Scene or Game Config property.
Use this to create Key objects and listen for keyboard specific events.
Source: src/input/keyboard/KeyboardPlugin.js#L946
Since: 3.10.0
manager ​
manager: Phaser.Input.InputManager ​
Description:
A reference to the Game Input Manager.
Source: src/input/InputPlugin.js#L111
Since: 3.0.0
mouse ​
mouse: Phaser.Input.Mouse.MouseManager ​
Description:
A reference to the Mouse Manager.
This property is only set if Mouse support has been enabled in your Game Configuration file.
If you just wish to get access to the mouse pointer, use the mousePointer property instead.
Source: src/input/InputPlugin.js#L161
Since: 3.0.0
mousePointer ​
mousePointer: Phaser.Input.Pointer ​
Description:
The mouse has its own unique Pointer object, which you can reference directly if making a desktop specific game .
If you are supporting both desktop and touch devices then do not use this property, instead use activePointer
which will always map to the most recently interacted pointer.
Source: src/input/InputPlugin.js#L3252
Since: 3.10.0
pointer1 ​
pointer1: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3288
Since: 3.10.0
pointer10 ​
pointer10: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3450
Since: 3.10.0
pointer2 ​
pointer2: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3306
Since: 3.10.0
pointer3 ​
pointer3: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3324
Since: 3.10.0
pointer4 ​
pointer4: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3342
Since: 3.10.0
pointer5 ​
pointer5: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3360
Since: 3.10.0
pointer6 ​
pointer6: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3378
Since: 3.10.0
pointer7 ​
pointer7: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3396
Since: 3.10.0
pointer8 ​
pointer8: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3414
Since: 3.10.0
pointer9 ​
pointer9: Phaser.Input.Pointer ​
Description:
A touch-based Pointer object.
This will be undefined by default unless you add a new Pointer using addPointer .
Source: src/input/InputPlugin.js#L3432
Since: 3.10.0
pollRate ​
pollRate: number ​
Description:
How often should the Pointers be checked?
The value is a time, given in ms, and is the time that must have elapsed between game steps before
the Pointers will be polled again. When a pointer is polled it runs a hit test to see which Game
Objects are currently below it, or being interacted with it.
Pointers will always be checked if they have been moved by the user, or press or released.
This property only controls how often they will be polled if they have not been updated.
You should set this if you want to have Game Objects constantly check against the pointers, even
if the pointer didn't itself move.
Set to 0 to poll constantly. Set to -1 to only poll on user movement.
Source: src/input/InputPlugin.js#L187
Since: 3.0.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene that this Input Plugin is responsible for.
Source: src/input/InputPlugin.js#L84
Since: 3.0.0
settings ​
settings: Phaser.Types.Scenes.SettingsObject ​
Description:
A reference to the Scene Systems Settings.
Source: src/input/InputPlugin.js#L102
Since: 3.5.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
A reference to the Scene Systems class.
Source: src/input/InputPlugin.js#L93
Since: 3.0.0
topOnly ​
topOnly: boolean ​
Description:
When set to true (the default) the Input Plugin will emulate DOM behavior by only emitting events from
the top-most Game Objects in the Display List.
If set to false it will emit events from all Game Objects below a Pointer, not just the top one.
Source: src/input/InputPlugin.js#L174
Since: 3.0.0
x ​
x: number ​
Description:
The x coordinates of the ActivePointer based on the first camera in the camera list.
This is only safe to use if your game has just 1 non-transformed camera and doesn't use multi-touch.
Source: src/input/InputPlugin.js#L3199
Since: 3.0.0
y ​
y: number ​
Description:
The y coordinates of the ActivePointer based on the first camera in the camera list.
This is only safe to use if your game has just 1 non-transformed camera and doesn't use multi-touch.
Source: src/input/InputPlugin.js#L3217
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
Public Methods ​
addPointer ​
<instance> addPointer([quantity]) ​
Description:
Adds new Pointer objects to the Input Manager.
By default Phaser creates 2 pointer objects: mousePointer and pointer1 .
You can create more either by calling this method, or by setting the input.activePointers property
in the Game Config, up to a maximum of 10 pointers.
The first 10 pointers are available via the InputPlugin.pointerX properties, once they have been added
via this method.
Parameters:
name type optional default description
quantity number Yes 1 The number of new Pointers to create. A maximum of 10 is allowed in total.
Returns: Array.< Phaser.Input.Pointer > - An array containing all of the new Pointer objects that were created.
Source: src/input/InputPlugin.js#L3011
Since: 3.10.0
clear ​
<instance> clear(gameObject, [skipQueue]) ​
Description:
Clears a Game Object so it no longer has an Interactive Object associated with it.
The Game Object is then queued for removal from the Input Plugin on the next update.
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No The Game Object that will have its Interactive Object removed.
skipQueue boolean Yes false Skip adding this Game Object into the removal queue?
Returns: Phaser.GameObjects.GameObject - The Game Object that had its Interactive Object removed.
Source: src/input/InputPlugin.js#L797
Since: 3.0.0
disable ​
<instance> disable(gameObject, [resetCursor]) ​
Description:
Disables Input on a single Game Object.
An input disabled Game Object still retains its Interactive Object component and can be re-enabled
at any time, by passing it to InputPlugin.enable .
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No The Game Object to have its input system disabled.
resetCursor boolean Yes false Reset the cursor to the default?
Returns: Phaser.Input.InputPlugin - This Input Plugin.
Source: src/input/InputPlugin.js#L847
Since: 3.0.0
enable ​
<instance> enable(gameObject, [hitArea], [hitAreaCallback], [dropZone]) ​
Description:
Enable a Game Object for interaction.
If the Game Object already has an Interactive Object component, it is enabled and returned.
Otherwise, a new Interactive Object component is created and assigned to the Game Object's input property.
Input works by using hit areas, these are nearly always geometric shapes, such as rectangles or circles, that act as the hit area
for the Game Object. However, you can provide your own hit area shape and callback, should you wish to handle some more advanced
input detection.
If no arguments are provided it will try and create a rectangle hit area based on the texture frame the Game Object is using. If
this isn't a texture-bound object, such as a Graphics or BitmapText object, this will fail, and you'll need to provide a specific
shape for it to use.
You can also provide an Input Configuration Object as the only argument to this method.
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No The Game Object to be enabled for input.
hitArea Phaser.Types.Input.InputConfiguration | any Yes Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not specified a Rectangle will be used.
hitAreaCallback Phaser.Types.Input.HitAreaCallback Yes The 'contains' function to invoke to check if the pointer is within the hit area.
dropZone boolean Yes false Is this Game Object a drop zone or not?
Returns: Phaser.Input.InputPlugin - This Input Plugin.
Source: src/input/InputPlugin.js#L903
Since: 3.0.0
enableDebug ​
<instance> enableDebug(gameObject, [color]) ​
Description:
Creates an Input Debug Shape for the given Game Object.
The Game Object must have already been enabled for input prior to calling this method.
This is intended to assist you during development and debugging.
Debug Shapes can only be created for Game Objects that are using standard Phaser Geometry for input,
including: Circle, Ellipse, Line, Polygon, Rectangle and Triangle.
Game Objects that are using their automatic hit areas are using Rectangles by default, so will also work.
The Debug Shape is created and added to the display list and is then kept in sync with the Game Object
it is connected with. Should you need to modify it yourself, such as to hide it, you can access it via
the Game Object property: GameObject.input.hitAreaDebug .
Calling this method on a Game Object that already has a Debug Shape will first destroy the old shape,
before creating a new one. If you wish to remove the Debug Shape entirely, you should call the
method InputPlugin.removeDebug .
Note that the debug shape will only show the outline of the input area. If the input test is using a
pixel perfect check, for example, then this is not displayed. If you are using a custom shape, that
doesn't extend one of the base Phaser Geometry objects, as your hit area, then this method will not
work.
Parameters:
name type optional default description
gameObject Phaser.GameObjects.GameObject No The Game Object to create the input debug shape for.
color number Yes "0x00ff00" The outline color of the debug shape.
Returns: Phaser.Input.InputPlugin - This Input Plugin.
Source: src/input/InputPlugin.js#L2608
Since: 3.19.0
forceDownState ​
<instance> forceDownState(pointer, gameObject) ​
Description:
This method will force the given Game Object into the 'down' input state.
This will check to see if the Game Object is enabled for input, and if so,
it will emit the GAMEOBJECT_POINTER_DOWN event for it. If that doesn't change
the input state, it will then emit the GAMEOBJECT_DOWN event.
The Game Object is not checked against the Pointer to see if it can enter this state,
that is up to you to do before calling this method.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The pointer to use when setting the state.
gameObject Phaser.GameObjects.GameObject No The Game Object to have its state set.
Fires: Phaser.Input.Events#event:GAMEOBJECT_POINTER_DOWN , Phaser.Input.Events#event:GAMEOBJECT_DOWN
Source: src/input/InputPlugin.js#L2080
Since: 3.85.0
forceOutState ​
<instance> forceOutState(pointer, gameObject) ​
Description:
This method will force the given Game Object into the 'out' input state.
This will check to see if the Game Object is enabled for input, and if so,
it will emit the GAMEOBJECT_POINTER_OUT event for it. If that doesn't change
the input state, it will then emit the GAMEOBJECT_OUT event.
The Game Object is not checked against the Pointer to see if it can enter this state,
that is up to you to do before calling this method.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The pointer to use when setting the state.
gameObject Phaser.GameObjects.GameObject No The Game Object to have its state set.
Fires: Phaser.Input.Events#event:GAMEOBJECT_POINTER_OUT , Phaser.Input.Events#event:GAMEOBJECT_OUT
Source: src/input/InputPlugin.js#L2149
Since: 3.85.0
forceOverState ​
<instance> forceOverState(pointer, gameObject) ​
Description:
This method will force the given Game Object into the 'over' input state.
This will check to see if the Game Object is enabled for input, and if so,
it will emit the GAMEOBJECT_POINTER_OVER event for it. If that doesn't change
the input state, it will then emit the GAMEOBJECT_OVER event.
The Game Object is not checked against the Pointer to see if it can enter this state,
that is up to you to do before calling this method.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The pointer to use when setting the state.
gameObject Phaser.GameObjects.GameObject No The Game Object to have its state set.
Fires: Phaser.Input.Events#event:GAMEOBJECT_POINTER_OVER , Phaser.Input.Events#event:GAMEOBJECT_OVER
Source: src/input/InputPlugin.js#L2126
Since: 3.85.0
forceState ​
<instance> forceState(pointer, gameObject, gameObjectEvent, inputPluginEvent, [setCursor]) ​
Description:
This method will force the given Game Object into the given input state.
Parameters:
name type optional default description
pointer Phaser.Input.Pointer No The pointer to use when setting the state.
gameObject Phaser.GameObjects.GameObject No The Game Object to have its state set.
gameObjectEvent string No The event to emit on the Game Object.
inputPluginEvent string No The event to emit on the Input Plugin.
setCursor boolean Yes false Should the cursor be set to the Game Object's cursor?
Source: src/input/InputPlugin.js#L2172
Since: 3.85.0
forceUpState ​
<instance> forceUpState(pointer, gameObject) ​
Description:
This method will force the given Game Object into the 'up' input state.
This will check to see if the Game Object is enabled for input, and if so,
it will emit the GAMEOBJECT_POINTER_UP event for it. If that doesn't change
the input state, it will then emit the GAMEOBJECT_UP event.
The Game Object is not checked against the Pointer to see if it can enter this state,
that is up to you to do before calling this method.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The pointer to use when setting the state.
gameObject Phaser.GameObjects.GameObject No The Game Object to have its state set.
Fires: Phaser.Input.Events#event:GAMEOBJECT_POINTER_UP , Phaser.Input.Events#event:GAMEOBJECT_UP
Source: src/input/InputPlugin.js#L2103
Since: 3.85.0
getDragState ​
<instance> getDragState(pointer) ​
Description:
Returns the drag state of the given Pointer for this Input Plugin.
The state will be one of the following:
0 = Not dragging anything
1 = Primary button down and objects below, so collect a draglist
2 = Pointer being checked if meets drag criteria
3 = Pointer meets criteria, notify the draglist
4 = Pointer actively dragging the draglist and has moved
5 = Pointer actively dragging but has been released, notify draglist
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The Pointer to get the drag state for.
Returns: number - The drag state of the given Pointer.
Source: src/input/InputPlugin.js#L1085
Since: 3.16.0
hitTestPointer ​
<instance> hitTestPointer(pointer) ​
Description:
Takes the given Pointer and performs a hit test against it, to see which interactive Game Objects
it is currently above.
The hit test is performed against which-ever Camera the Pointer is over. If it is over multiple
cameras, it starts checking the camera at the top of the camera list, and if nothing is found, iterates down the list.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The Pointer to check against the Game Objects.
Returns: Array.< Phaser.GameObjects.GameObject > - An array of all the interactive Game Objects the Pointer was above.
Source: src/input/InputPlugin.js#L953
Since: 3.0.0
isActive ​
<instance> isActive() ​
Description:
Checks to see if the Input Manager, this plugin and the Scene to which it belongs are all active and input enabled.
Returns: boolean - true if the plugin and the Scene it belongs to is active.
Source: src/input/InputPlugin.js#L528
Since: 3.10.0
makePixelPerfect ​
<instance> makePixelPerfect([alphaTolerance]) ​
Description:
Creates a function that can be passed to setInteractive , enable or setHitArea that will handle
pixel-perfect input detection on an Image or Sprite based Game Object, or any custom class that extends them.
The following will create a sprite that is clickable on any pixel that has an alpha value >= 1.
this . add . sprite ( x , y , key ) . setInteractive ( this . input . makePixelPerfect ( ) ) ;
The following will create a sprite that is clickable on any pixel that has an alpha value >= 150.
this . add . sprite ( x , y , key ) . setInteractive ( this . input . makePixelPerfect ( 150 ) ) ;
Once you have made an Interactive Object pixel perfect it impacts all input related events for it: down, up,
dragstart, drag, etc.
As a pointer interacts with the Game Object it will constantly poll the texture, extracting a single pixel from
the given coordinates and checking its color values. This is an expensive process, so should only be enabled on
Game Objects that really need it.
You cannot make non-texture based Game Objects pixel perfect. So this will not work on Graphics, BitmapText,
Render Textures, Text, Tilemaps, Containers or Particles.
Parameters:
name type optional default description
alphaTolerance number Yes 1 The alpha level that the pixel should be above to be included as a successful interaction.
Returns: function - A Pixel Perfect Handler for use as a hitArea shape callback.
Source: src/input/InputPlugin.js#L2291
Since: 3.10.0
removeDebug ​
<instance> removeDebug(gameObject) ​
Description:
Removes an Input Debug Shape from the given Game Object.
The shape is destroyed immediately and the hitAreaDebug property is set to null .
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to remove the input debug shape from.
Returns: Phaser.Input.InputPlugin - This Input Plugin.
Source: src/input/InputPlugin.js#L2748
Since: 3.19.0
resetCursor ​
<instance> resetCursor() ​
Description:
Forces the Input Manager to clear the custom or hand cursor, regardless of the
interactive state of any Game Objects.
Source: src/input/InputPlugin.js#L562
Since: 3.85.0
resetPointers ​
<instance> resetPointers() ​
Description:
Loops through all of the Input Manager Pointer instances and calls reset on them.
Use this function if you find that input has been stolen from Phaser via a 3rd
party component, such as Vue, and you need to tell Phaser to reset the Pointer states.
Source: src/input/InputPlugin.js#L3153
Since: 3.60.0
setCursor ​
<instance> setCursor(interactiveObject) ​
Description:
Sets a custom cursor on the parent canvas element of the game, based on the cursor
setting of the given Interactive Object (i.e. a Sprite).
See the CSS property cursor for more information on MDN:
https://developer.mozilla.org/en-US/docs/Web/CSS/cursor
Parameters:
name type optional description
interactiveObject Phaser.Types.Input.InteractiveObject No The Interactive Object that will set the cursor on the canvas.
Source: src/input/InputPlugin.js#L541
Since: 3.85.0
setDefaultCursor ​
<instance> setDefaultCursor(cursor) ​
Description:
Tells the Input system to set a custom cursor.
This cursor will be the default cursor used when interacting with the game canvas.
If an Interactive Object also sets a custom cursor, this is the cursor that is reset after its use.
Any valid CSS cursor value is allowed, including paths to image files, i.e.:
this . input . setDefaultCursor ( 'url(assets/cursors/sword.cur), pointer' ) ;
Please read about the differences between browsers when it comes to the file formats and sizes they support:
https://developer.mozilla.org/en-US/docs/Web/CSS/cursor
https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_User_Interface/Using_URL_values_for_the_cursor_property
It's up to you to pick a suitable cursor format that works across the range of browsers you need to support.
Parameters:
name type optional description
cursor string No The CSS to be used when setting the default cursor.
Returns: Phaser.Input.InputPlugin - This Input instance.
Source: src/input/InputPlugin.js#L3034
Since: 3.10.0
setDraggable ​
<instance> setDraggable(gameObjects, [value]) ​
Description:
Sets the draggable state of the given array of Game Objects.
They can either be set to be draggable, or can have their draggable state removed by passing false .
A Game Object will not fire drag events unless it has been specifically enabled for drag.
Parameters:
name type optional default description
gameObjects Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to change the draggable state on.
value boolean Yes true Set to true if the Game Objects should be made draggable, false if they should be unset.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2246
Since: 3.0.0
setDragState ​
<instance> setDragState(pointer, state) ​
Description:
Sets the drag state of the given Pointer for this Input Plugin.
The state must be one of the following values:
0 = Not dragging anything
1 = Primary button down and objects below, so collect a draglist
2 = Pointer being checked if meets drag criteria
3 = Pointer meets criteria, notify the draglist
4 = Pointer actively dragging the draglist and has moved
5 = Pointer actively dragging but has been released, notify draglist
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The Pointer to set the drag state for.
state number No The drag state value. An integer between 0 and 5.
Source: src/input/InputPlugin.js#L1109
Since: 3.16.0
setGlobalTopOnly ​
<instance> setGlobalTopOnly(value) ​
Description:
When set to true the global Input Manager will emulate DOM behavior by only emitting events from
the top-most Scene in the Scene List. By default, if a Scene receives an input event it will then stop the event
from flowing down to any Scenes below it in the Scene list. To disable this behavior call this method with false .
Parameters:
name type optional description
value boolean No Set to true to stop processing input events on the Scene that receives it, or false to let the event continue down the Scene list.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2832
Since: 3.0.0
setHitArea ​
<instance> setHitArea(gameObjects, [hitArea], [hitAreaCallback]) ​
Description:
Sets the hit area for the given array of Game Objects.
A hit area is typically one of the geometric shapes Phaser provides, such as a Phaser.Geom.Rectangle
or Phaser.Geom.Circle . However, it can be any object as long as it works with the provided callback.
If no hit area is provided a Rectangle is created based on the size of the Game Object, if possible
to calculate.
The hit area callback is the function that takes an x and y coordinate and returns a boolean if
those values fall within the area of the shape or not. All of the Phaser geometry objects provide this,
such as Phaser.Geom.Rectangle.Contains .
A hit area callback can be supplied to the hitArea parameter without using the hitAreaCallback parameter.
Parameters:
name type optional description
gameObjects Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to set the hit area on.
hitArea Phaser.Types.Input.InputConfiguration | Phaser.Types.Input.HitAreaCallback any Yes
hitAreaCallback Phaser.Types.Input.HitAreaCallback Yes The 'contains' function to invoke to check if the pointer is within the hit area.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2333
Since: 3.0.0
setHitAreaCircle ​
<instance> setHitAreaCircle(gameObjects, x, y, radius, [callback]) ​
Description:
Sets the hit area for an array of Game Objects to be a Phaser.Geom.Circle shape, using
the given coordinates and radius to control its position and size.
Parameters:
name type optional description
gameObjects Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to set as having a circle hit area.
x number No The center of the circle.
y number No The center of the circle.
radius number No The radius of the circle.
callback Phaser.Types.Input.HitAreaCallback Yes The hit area callback. If undefined it uses Circle.Contains.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2449
Since: 3.0.0
setHitAreaEllipse ​
<instance> setHitAreaEllipse(gameObjects, x, y, width, height, [callback]) ​
Description:
Sets the hit area for an array of Game Objects to be a Phaser.Geom.Ellipse shape, using
the given coordinates and dimensions to control its position and size.
Parameters:
name type optional description
gameObjects Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to set as having an ellipse hit area.
x number No The center of the ellipse.
y number No The center of the ellipse.
width number No The width of the ellipse.
height number No The height of the ellipse.
callback Phaser.Types.Input.HitAreaCallback Yes The hit area callback. If undefined it uses Ellipse.Contains.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2473
Since: 3.0.0
setHitAreaFromTexture ​
<instance> setHitAreaFromTexture(gameObjects, [callback]) ​
Description:
Sets the hit area for an array of Game Objects to be a Phaser.Geom.Rectangle shape, using
the Game Objects texture frame to define the position and size of the hit area.
Parameters:
name type optional description
gameObjects Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to set as having an ellipse hit area.
callback Phaser.Types.Input.HitAreaCallback Yes The hit area callback. If undefined it uses Rectangle.Contains.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2498
Since: 3.0.0
setHitAreaRectangle ​
<instance> setHitAreaRectangle(gameObjects, x, y, width, height, [callback]) ​
Description:
Sets the hit area for an array of Game Objects to be a Phaser.Geom.Rectangle shape, using
the given coordinates and dimensions to control its position and size.
Parameters:
name type optional description
gameObjects Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to set as having a rectangular hit area.
x number No The top-left of the rectangle.
y number No The top-left of the rectangle.
width number No The width of the rectangle.
height number No The height of the rectangle.
callback Phaser.Types.Input.HitAreaCallback Yes The hit area callback. If undefined it uses Rectangle.Contains.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2556
Since: 3.0.0
setHitAreaTriangle ​
<instance> setHitAreaTriangle(gameObjects, x1, y1, x2, y2, x3, y3, [callback]) ​
Description:
Sets the hit area for an array of Game Objects to be a Phaser.Geom.Triangle shape, using
the given coordinates to control the position of its points.
Parameters:
name type optional description
gameObjects Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to set as having a triangular hit area.
x1 number No The x coordinate of the first point of the triangle.
y1 number No The y coordinate of the first point of the triangle.
x2 number No The x coordinate of the second point of the triangle.
y2 number No The y coordinate of the second point of the triangle.
x3 number No The x coordinate of the third point of the triangle.
y3 number No The y coordinate of the third point of the triangle.
callback Phaser.Types.Input.HitAreaCallback Yes The hit area callback. If undefined it uses Triangle.Contains.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2581
Since: 3.0.0
setPollAlways ​
<instance> setPollAlways() ​
Description:
Sets the Pointers to always poll.
When a pointer is polled it runs a hit test to see which Game Objects are currently below it,
or being interacted with it, regardless if the Pointer has actually moved or not.
You should enable this if you want objects in your game to fire over / out events, and the objects
are constantly moving, but the pointer may not have. Polling every frame has additional computation
costs, especially if there are a large number of interactive objects in your game.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2777
Since: 3.0.0
setPollOnMove ​
<instance> setPollOnMove() ​
Description:
Sets the Pointers to only poll when they are moved or updated.
When a pointer is polled it runs a hit test to see which Game Objects are currently below it,
or being interacted with it.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2797
Since: 3.0.0
setPollRate ​
<instance> setPollRate(value) ​
Description:
Sets the poll rate value. This is the amount of time that should have elapsed before a pointer
will be polled again. See the setPollAlways and setPollOnMove methods.
Parameters:
name type optional description
value number No The amount of time, in ms, that should elapsed before re-polling the pointers.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2813
Since: 3.0.0
setTopOnly ​
<instance> setTopOnly(value) ​
Description:
When set to true this Input Plugin will emulate DOM behavior by only emitting events from
the top-most Game Objects in the Display List.
If set to false it will emit events from all Game Objects below a Pointer, not just the top one.
Parameters:
name type optional description
value boolean No true to only include the top-most Game Object, or false to include all Game Objects in a hit test.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2851
Since: 3.0.0
sortDropZones ​
<instance> sortDropZones(gameObjects) ​
Description:
Given an array of Drop Zone Game Objects, sort the array and return it,
so that the objects are in depth index order with the lowest at the bottom.
Parameters:
name type optional description
gameObjects Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to be sorted.
Returns: Array.< Phaser.GameObjects.GameObject > - The sorted array of Game Objects.
Source: src/input/InputPlugin.js#L2901
Since: 3.52.0
sortGameObjects ​
<instance> sortGameObjects(gameObjects, pointer) ​
Description:
Given an array of Game Objects and a Pointer, sort the array and return it,
so that the objects are in render order with the lowest at the bottom.
Parameters:
name type optional description
gameObjects Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to be sorted.
pointer Phaser.Input.Pointer No The Pointer to check against the Game Objects.
Returns: Array.< Phaser.GameObjects.GameObject > - The sorted array of Game Objects.
Source: src/input/InputPlugin.js#L2871
Since: 3.0.0
stopPropagation ​
<instance> stopPropagation() ​
Description:
This method should be called from within an input event handler, such as pointerdown .
When called, it stops the Input Manager from allowing this specific event to be processed by any other Scene
not yet handled in the scene list.
Returns: Phaser.Input.InputPlugin - This InputPlugin object.
Source: src/input/InputPlugin.js#L2993
Since: 3.0.0
updatePoll ​
<instance> updatePoll(time, delta) ​
Description:
This is called automatically by the Input Manager.
It emits events for plugins to listen to and also handles polling updates, if enabled.
Parameters:
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Returns: boolean - true if the plugin and the Scene it belongs to is active.
Source: src/input/InputPlugin.js#L577
Since: 3.18.0
Previous
InputManager
Next
Key
Public Members
activePointer
cameras
displayList
dragDistanceThreshold
dragTimeThreshold
enabled
gamepad
isOver
keyboard
manager
mouse
mousePointer
pointer1
pointer10
pointer2
pointer3
pointer4
pointer5
pointer6
pointer7
pointer8
pointer9
pollRate
scene
settings
systems
topOnly
x
y
Inherited Methods
Public Methods
addPointer
clear
disable
enable
enableDebug
forceDownState
forceOutState
forceOverState
forceState
forceUpState
getDragState
hitTestPointer
isActive
makePixelPerfect
removeDebug
resetCursor
resetPointers
setCursor
setDefaultCursor
setDraggable
setDragState
setGlobalTopOnly
setHitArea
setHitAreaCircle
setHitAreaEllipse
setHitAreaFromTexture
setHitAreaRectangle
setHitAreaTriangle
setPollAlways
setPollOnMove
setPollRate
setTopOnly
sortDropZones
sortGameObjects
stopPropagation
updatePoll
