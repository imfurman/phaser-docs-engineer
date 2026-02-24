# InputManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-inputmanager

Phaser API Documentation
Class
InputManager
Version: Phaser v3.90.0
On this page
InputManager
The Input Manager is responsible for handling the pointer related systems in a single Phaser Game instance.
Based on the Game Config it will create handlers for mouse and touch support.
Keyboard and Gamepad are plugins, handled directly by the InputPlugin class.
It then manages the events, pointer creation and general hit test related operations.
You rarely need to interact with the Input Manager directly, and as such, all of its properties and methods
should be considered private. Instead, you should use the Input Plugin, which is a Scene level system, responsible
for dealing with all input events for a Scene.
Constructor
new InputManager(game, config)
Parameters
name type optional description
game Phaser.Game No The Game instance that owns the Input Manager.
config object No The Input Configuration object, as set in the Game Config.
Scope : static
Source: src/input/InputManager.js#L19
Since: 3.0.0
Public Members ​
activePointer ​
activePointer: Phaser.Input.Pointer ​
Description:
The most recently active Pointer object.
If you've only 1 Pointer in your game then this will accurately be either the first finger touched, or the mouse.
If your game doesn't need to support multi-touch then you can safely use this property in all of your game
code and it will adapt to be either the mouse or the touch, based on device.
Source: src/input/InputManager.js#L200
Since: 3.0.0
canvas ​
canvas: HTMLCanvasElement ​
Description:
The Canvas that is used for all DOM event input listeners.
Source: src/input/InputManager.js#L68
Since: 3.0.0
config ​
config: Phaser.Core.Config ​
Description:
The Game Configuration object, as set during the game boot.
Source: src/input/InputManager.js#L77
Since: 3.0.0
defaultCursor ​
defaultCursor: string ​
Description:
The default CSS cursor to be used when interacting with your game.
See the setDefaultCursor method for more details.
Source: src/input/InputManager.js#L116
Since: 3.10.0
enabled ​
enabled: boolean ​
Description:
If set, the Input Manager will run its update loop every frame.
Source: src/input/InputManager.js#L86
Since: 3.0.0
events ​
events: Phaser.Events.EventEmitter ​
Description:
The Event Emitter instance that the Input Manager uses to emit events from.
Source: src/input/InputManager.js#L96
Since: 3.0.0
game ​
game: Phaser.Game ​
Description:
The Game instance that owns the Input Manager.
A Game only maintains one instance of the Input Manager at any time.
Source: src/input/InputManager.js#L47
Since: 3.0.0
globalTopOnly ​
globalTopOnly: boolean ​
Description:
If the top-most Scene in the Scene List receives an input it will stop input from
propagating any lower down the scene list, i.e. if you have a UI Scene at the top
and click something on it, that click will not then be passed down to any other
Scene below. Disable this to have input events passed through all Scenes, all the time.
Source: src/input/InputManager.js#L214
Since: 3.0.0
isOver ​
isOver: boolean ​
Description:
Are any mouse or touch pointers currently over the game canvas?
This is updated automatically by the canvas over and out handlers.
Source: src/input/InputManager.js#L105
Since: 3.16.0
keyboard ​
keyboard: Phaser.Input.Keyboard.KeyboardManager ​
Description:
A reference to the Keyboard Manager class, if enabled via the input.keyboard Game Config property.
Source: src/input/InputManager.js#L127
Since: 3.16.0
mouse ​
mouse: Phaser.Input.Mouse.MouseManager ​
Description:
A reference to the Mouse Manager class, if enabled via the input.mouse Game Config property.
Source: src/input/InputManager.js#L136
Since: 3.0.0
mousePointer ​
mousePointer: Phaser.Input.Pointer ​
Description:
The mouse has its own unique Pointer object, which you can reference directly if making a desktop specific game .
If you are supporting both desktop and touch devices then do not use this property, instead use activePointer
which will always map to the most recently interacted pointer.
Source: src/input/InputManager.js#L189
Since: 3.10.0
pointers ​
pointers: Array.< Phaser.Input.Pointer > ​
Description:
An array of Pointers that have been added to the game.
The first entry is reserved for the Mouse Pointer, the rest are Touch Pointers.
By default there is 1 touch pointer enabled. If you need more use the addPointer method to start them,
or set the input.activePointers property in the Game Config.
Source: src/input/InputManager.js#L154
Since: 3.10.0
pointersTotal ​
pointersTotal: number ​
Description:
The number of touch objects activated and being processed each update.
You can change this by either calling addPointer at run-time, or by
setting the input.activePointers property in the Game Config.
Source: src/input/InputManager.js#L167
Since: 3.10.0
scaleManager ​
scaleManager: Phaser.Scale.ScaleManager ​
Description:
A reference to the global Game Scale Manager.
Used for all bounds checks and pointer scaling.
Source: src/input/InputManager.js#L58
Since: 3.16.0
time ​
time: number ​
Description:
The time this Input Manager was last updated.
This value is populated by the Game Step each frame.
Source: src/input/InputManager.js#L227
Since: 3.16.2
touch ​
touch: Phaser.Input.Touch.TouchManager ​
Description:
A reference to the Touch Manager class, if enabled via the input.touch Game Config property.
Source: src/input/InputManager.js#L145
Since: 3.0.0
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
Source: src/input/InputManager.js#L466
Since: 3.10.0
boot ​
<instance> boot() ​
Description:
The Boot handler is called by Phaser.Game when it first starts up.
The renderer is available by now.
Access: protected
Fires: Phaser.Input.Events#event:MANAGER_BOOT
Source: src/input/InputManager.js#L302
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys the Input Manager and all of its systems.
There is no way to recover from doing this.
Source: src/input/InputManager.js#L1057
Since: 3.0.0
hitTest ​
<instance> hitTest(pointer, gameObjects, camera, [output]) ​
Description:
Performs a hit test using the given Pointer and camera, against an array of interactive Game Objects.
The Game Objects are culled against the camera, and then the coordinates are translated into the local camera space
and used to determine if they fall within the remaining Game Objects hit areas or not.
If nothing is matched an empty array is returned.
This method is called automatically by InputPlugin.hitTestPointer and doesn't usually need to be invoked directly.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The Pointer to test against.
gameObjects array No An array of interactive Game Objects to check.
camera Phaser.Cameras.Scene2D.Camera No The Camera which is being tested against.
output array Yes An array to store the results in. If not given, a new empty array is created.
Returns: array - An array of the Game Objects that were hit during this hit test.
Source: src/input/InputManager.js#L868
Since: 3.0.0
pointWithinHitArea ​
<instance> pointWithinHitArea(gameObject, x, y) ​
Description:
Checks if the given x and y coordinate are within the hit area of the Game Object.
This method assumes that the coordinate values have already been translated into the space of the Game Object.
If the coordinates are within the hit area they are set into the Game Objects Input localX and localY properties.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The interactive Game Object to check against.
x number No The translated x coordinate for the hit test.
y number No The translated y coordinate for the hit test.
Returns: boolean - true if the coordinates were inside the Game Objects hit area, otherwise false .
Source: src/input/InputManager.js#L947
Since: 3.0.0
pointWithinInteractiveObject ​
<instance> pointWithinInteractiveObject(object, x, y) ​
Description:
Checks if the given x and y coordinate are within the hit area of the Interactive Object.
This method assumes that the coordinate values have already been translated into the space of the Interactive Object.
If the coordinates are within the hit area they are set into the Interactive Objects Input localX and localY properties.
Parameters:
name type optional description
object Phaser.Types.Input.InteractiveObject No The Interactive Object to check against.
x number No The translated x coordinate for the hit test.
y number No The translated y coordinate for the hit test.
Returns: boolean - true if the coordinates were inside the Game Objects hit area, otherwise false .
Source: src/input/InputManager.js#L984
Since: 3.0.0
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
Source: src/input/InputManager.js#L390
Since: 3.10.0
transformPointer ​
<instance> transformPointer(pointer, pageX, pageY, wasMove) ​
Description:
Transforms the pageX and pageY values of a Pointer into the scaled coordinate space of the Input Manager.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No The Pointer to transform the values for.
pageX number No The Page X value.
pageY number No The Page Y value.
wasMove boolean No Are we transforming the Pointer from a move event, or an up / down event?
Source: src/input/InputManager.js#L1017
Since: 3.10.0
updateInputPlugins ​
<instance> updateInputPlugins(type, pointers) ​
Description:
Internal method that gets a list of all the active Input Plugins in the game
and updates each of them in turn, in reverse order (top to bottom), to allow
for DOM top-level event handling simulation.
Parameters:
name type optional description
type number No The type of event to process.
pointers Array.< Phaser.Input.Pointer > No An array of Pointers on which the event occurred.
Source: src/input/InputManager.js#L513
Since: 3.16.0
Previous
GamepadPlugin
Next
InputPlugin
Public Members
activePointer
canvas
config
defaultCursor
enabled
events
game
globalTopOnly
isOver
keyboard
mouse
mousePointer
pointers
pointersTotal
scaleManager
time
touch
Public Methods
addPointer
boot
destroy
hitTest
pointWithinHitArea
pointWithinInteractiveObject
setDefaultCursor
transformPointer
updateInputPlugins
