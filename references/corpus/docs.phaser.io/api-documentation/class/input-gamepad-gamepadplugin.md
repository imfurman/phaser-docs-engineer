# GamepadPlugin | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-gamepad-gamepadplugin

Phaser API Documentation
Class
GamepadPlugin
Version: Phaser v3.90.0
On this page
GamepadPlugin
The Gamepad Plugin is an input plugin that belongs to the Scene-owned Input system.
Its role is to listen for native DOM Gamepad Events and then process them.
You do not need to create this class directly, the Input system will create an instance of it automatically.
You can access it from within a Scene using this.input.gamepad .
To listen for a gamepad being connected:
this . input . gamepad . once ( 'connected' , function ( pad ) {
// 'pad' is a reference to the gamepad that was just connected
} ) ;
Note that the browser may require you to press a button on a gamepad before it will allow you to access it,
this is for security reasons. However, it may also trust the page already, in which case you won't get the
'connected' event and instead should check GamepadPlugin.total to see if it thinks there are any gamepads
already connected.
Once you have received the connected event, or polled the gamepads and found them enabled, you can access
them via the built-in properties GamepadPlugin.pad1 to pad4 , for up to 4 game pads. With a reference
to the gamepads you can poll its buttons and axis sticks. See the properties and methods available on
the Gamepad class for more details.
As of September 2020 Chrome, and likely other browsers, will soon start to require that games requesting
access to the Gamepad API are running under SSL. They will actively block API access if they are not.
For more information about Gamepad support in browsers see the following resources:
https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API
https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API
https://www.smashingmagazine.com/2015/11/gamepad-api-in-web-games/
http://html5gamepad.com/
Constructor
new GamepadPlugin(sceneInputPlugin)
Parameters
name type optional description
sceneInputPlugin Phaser.Input.InputPlugin No A reference to the Scene Input Plugin that the KeyboardPlugin belongs to.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/input/gamepad/GamepadPlugin.js#L15
Since: 3.10.0
Public Members ​
enabled ​
enabled: boolean ​
Description:
A boolean that controls if the Gamepad Manager is enabled or not.
Can be toggled on the fly.
Source: src/input/gamepad/GamepadPlugin.js#L98
Since: 3.10.0
gamepads ​
gamepads: Array.< Phaser.Input.Gamepad.Gamepad > ​
Description:
An array of the connected Gamepads.
Source: src/input/gamepad/GamepadPlugin.js#L119
Since: 3.10.0
pad1 ​
pad1: Phaser.Input.Gamepad.Gamepad ​
Description:
A reference to the first connected Gamepad.
This will be undefined if either no pads are connected, or the browser
has not yet issued a gamepadconnect, which can happen even if a Gamepad
is plugged in, but hasn't yet had any buttons pressed on it.
Source: src/input/gamepad/GamepadPlugin.js#L548
Since: 3.10.0
pad2 ​
pad2: Phaser.Input.Gamepad.Gamepad ​
Description:
A reference to the second connected Gamepad.
This will be undefined if either no pads are connected, or the browser
has not yet issued a gamepadconnect, which can happen even if a Gamepad
is plugged in, but hasn't yet had any buttons pressed on it.
Source: src/input/gamepad/GamepadPlugin.js#L568
Since: 3.10.0
pad3 ​
pad3: Phaser.Input.Gamepad.Gamepad ​
Description:
A reference to the third connected Gamepad.
This will be undefined if either no pads are connected, or the browser
has not yet issued a gamepadconnect, which can happen even if a Gamepad
is plugged in, but hasn't yet had any buttons pressed on it.
Source: src/input/gamepad/GamepadPlugin.js#L588
Since: 3.10.0
pad4 ​
pad4: Phaser.Input.Gamepad.Gamepad ​
Description:
A reference to the fourth connected Gamepad.
This will be undefined if either no pads are connected, or the browser
has not yet issued a gamepadconnect, which can happen even if a Gamepad
is plugged in, but hasn't yet had any buttons pressed on it.
Source: src/input/gamepad/GamepadPlugin.js#L608
Since: 3.10.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene that this Input Plugin is responsible for.
Source: src/input/gamepad/GamepadPlugin.js#L71
Since: 3.10.0
sceneInputPlugin ​
sceneInputPlugin: Phaser.Input.InputPlugin ​
Description:
A reference to the Scene Input Plugin that created this Keyboard Plugin.
Source: src/input/gamepad/GamepadPlugin.js#L89
Since: 3.10.0
settings ​
settings: Phaser.Types.Scenes.SettingsObject ​
Description:
A reference to the Scene Systems Settings.
Source: src/input/gamepad/GamepadPlugin.js#L80
Since: 3.10.0
target ​
target: any ​
Description:
The Gamepad Event target, as defined in the Game Config.
Typically the browser window, but can be any interactive DOM element.
Source: src/input/gamepad/GamepadPlugin.js#L109
Since: 3.10.0
total ​
total: number ​
Description:
The total number of connected game pads.
Source: src/input/gamepad/GamepadPlugin.js#L532
Since: 3.10.0
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
disconnectAll ​
<instance> disconnectAll() ​
Description:
Disconnects all current Gamepads.
Source: src/input/gamepad/GamepadPlugin.js#L307
Since: 3.10.0
getAll ​
<instance> getAll() ​
Description:
Returns an array of all currently connected Gamepads.
Returns: Array.< Phaser.Input.Gamepad.Gamepad > - An array of all currently connected Gamepads.
Source: src/input/gamepad/GamepadPlugin.js#L397
Since: 3.10.0
getPad ​
<instance> getPad(index) ​
Description:
Looks-up a single Gamepad based on the given index value.
Parameters:
name type optional description
index number No The index of the Gamepad to get.
Returns: Phaser.Input.Gamepad.Gamepad - The Gamepad matching the given index, or undefined if none were found.
Source: src/input/gamepad/GamepadPlugin.js#L421
Since: 3.10.0
isActive ​
<instance> isActive() ​
Description:
Checks to see if both this plugin and the Scene to which it belongs is active.
Returns: boolean - true if the plugin and the Scene it belongs to is active.
Source: src/input/gamepad/GamepadPlugin.js#L234
Since: 3.10.0
Previous
Gamepad
Next
InputManager
Public Members
enabled
gamepads
pad1
pad2
pad3
pad4
scene
sceneInputPlugin
settings
target
total
Inherited Methods
Public Methods
disconnectAll
getAll
getPad
isActive
