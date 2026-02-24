# Key | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-keyboard-key

Phaser API Documentation
Class
Key
Version: Phaser v3.90.0
On this page
Key
A generic Key object which can be passed to the Process functions (and so on)
keycode must be an integer
Constructor
new Key(plugin, keyCode)
Parameters
name type optional description
plugin Phaser.Input.Keyboard.KeyboardPlugin No The Keyboard Plugin instance that owns this Key object.
keyCode number No The keycode of this key.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/input/keyboard/keys/Key.js#L11
Since: 3.0.0
Public Members ​
altKey ​
altKey: boolean ​
Description:
The down state of the ALT key, if pressed at the same time as this key.
Source: src/input/keyboard/keys/Key.js#L92
Since: 3.0.0
ctrlKey ​
ctrlKey: boolean ​
Description:
The down state of the CTRL key, if pressed at the same time as this key.
Source: src/input/keyboard/keys/Key.js#L102
Since: 3.0.0
duration ​
duration: number ​
Description:
The number of milliseconds this key was held down for in the previous down - up sequence.
This value isn't updated every game step, only when the Key changes state.
To get the current duration use the getDuration method.
Source: src/input/keyboard/keys/Key.js#L153
Since: 3.0.0
emitOnRepeat ​
emitOnRepeat: boolean ​
Description:
When a key is held down should it continuously fire the down event each time it repeats?
By default it will emit the down event just once, but if you wish to receive the event
for each repeat as well, enable this property.
Source: src/input/keyboard/keys/Key.js#L175
Since: 3.16.0
enabled ​
enabled: boolean ​
Description:
Can this Key be processed?
Source: src/input/keyboard/keys/Key.js#L62
Since: 3.0.0
isDown ​
isDown: boolean ​
Description:
The "down" state of the key. This will remain true for as long as the keyboard thinks this key is held down.
Source: src/input/keyboard/keys/Key.js#L72
Since: 3.0.0
isUp ​
isUp: boolean ​
Description:
The "up" state of the key. This will remain true for as long as the keyboard thinks this key is up.
Source: src/input/keyboard/keys/Key.js#L82
Since: 3.0.0
keyCode ​
keyCode: number ​
Description:
The keycode of this key.
Source: src/input/keyboard/keys/Key.js#L44
Since: 3.0.0
location ​
location: number ​
Description:
The location of the modifier key. 0 for standard (or unknown), 1 for left, 2 for right, 3 for numpad.
Source: src/input/keyboard/keys/Key.js#L133
Since: 3.0.0
metaKey ​
metaKey: boolean ​
Description:
The down state of the Meta key, if pressed at the same time as this key.
On a Mac the Meta Key is the Command key. On Windows keyboards, it's the Windows key.
Source: src/input/keyboard/keys/Key.js#L122
Since: 3.16.0
originalEvent ​
originalEvent: KeyboardEvent ​
Description:
The original DOM event.
Source: src/input/keyboard/keys/Key.js#L53
Since: 3.0.0
plugin ​
plugin: Phaser.Input.Keyboard.KeyboardPlugin ​
Description:
The Keyboard Plugin instance that owns this Key object.
Source: src/input/keyboard/keys/Key.js#L35
Since: 3.17.0
repeats ​
repeats: number ​
Description:
If a key is held down this holds down the number of times the key has 'repeated'.
Source: src/input/keyboard/keys/Key.js#L188
Since: 3.0.0
shiftKey ​
shiftKey: boolean ​
Description:
The down state of the SHIFT key, if pressed at the same time as this key.
Source: src/input/keyboard/keys/Key.js#L112
Since: 3.0.0
timeDown ​
timeDown: number ​
Description:
The timestamp when the key was last pressed down.
Source: src/input/keyboard/keys/Key.js#L143
Since: 3.0.0
timeUp ​
timeUp: number ​
Description:
The timestamp when the key was last released.
Source: src/input/keyboard/keys/Key.js#L165
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
destroy ​
<instance> destroy() ​
Description:
Removes any bound event handlers and removes local references.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/input/keyboard/keys/Key.js#L379
Since: 3.16.0
getDuration ​
<instance> getDuration() ​
Description:
Returns the duration, in ms, that the Key has been held down for.
If the key is not currently down it will return zero.
To get the duration the Key was held down for in the previous up-down cycle,
use the Key.duration property value instead.
Returns: number - The duration, in ms, that the Key has been held down for if currently down.
Source: src/input/keyboard/keys/Key.js#L354
Since: 3.17.0
onDown ​
<instance> onDown(event) ​
Description:
Processes the Key Down action for this Key.
Called automatically by the Keyboard Plugin.
Parameters:
name type optional description
event KeyboardEvent No The native DOM Keyboard event.
Fires: Phaser.Input.Keyboard.Events#event:DOWN
Source: src/input/keyboard/keys/Key.js#L249
Since: 3.16.0
onUp ​
<instance> onUp(event) ​
Description:
Processes the Key Up action for this Key.
Called automatically by the Keyboard Plugin.
Parameters:
name type optional description
event KeyboardEvent No The native DOM Keyboard event.
Fires: Phaser.Input.Keyboard.Events#event:UP
Source: src/input/keyboard/keys/Key.js#L293
Since: 3.16.0
reset ​
<instance> reset() ​
Description:
Resets this Key object back to its default un-pressed state.
As of version 3.60.0 it no longer resets the enabled or preventDefault flags.
Returns: Phaser.Input.Keyboard.Key - This Key instance.
Source: src/input/keyboard/keys/Key.js#L325
Since: 3.6.0
setEmitOnRepeat ​
<instance> setEmitOnRepeat(value) ​
Description:
Controls if this Key will continuously emit a down event while being held down (true),
or emit the event just once, on first press, and then skip future events (false).
Parameters:
name type optional description
value boolean No Emit down events on repeated key down actions, or just once?
Returns: Phaser.Input.Keyboard.Key - This Key instance.
Source: src/input/keyboard/keys/Key.js#L231
Since: 3.16.0
Previous
InputPlugin
Next
KeyCombo
Public Members
altKey
ctrlKey
duration
emitOnRepeat
enabled
isDown
isUp
keyCode
location
metaKey
originalEvent
plugin
repeats
shiftKey
timeDown
timeUp
Inherited Methods
Public Methods
destroy
getDuration
onDown
onUp
reset
setEmitOnRepeat
