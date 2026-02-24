# Phaser.Input.Keyboard | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/input-keyboard

Phaser API Documentation
Namespaces
Phaser.Input.Keyboard
Version: Phaser v3.90.0
On this page
Phaser.Input.Keyboard
Scope: static
Source: src/input/keyboard/index.js#L7
Static functions ​
Key
KeyboardManager
KeyboardPlugin
KeyCombo
Static functions ​
DownDuration ​
<static> DownDuration(key, [duration]) ​
Description:
Returns true if the Key was pressed down within the duration value given, based on the current
game clock time. Or false if it either isn't down, or was pressed down longer ago than the given duration.
Parameters:
name type optional default description
key Phaser.Input.Keyboard.Key No The Key object to test.
duration number Yes 50 The duration, in ms, within which the key must have been pressed down.
Returns: boolean - true if the Key was pressed down within duration ms ago, otherwise false .
Source: src/input/keyboard/keys/DownDuration.js#L7
Since: 3.0.0
JustDown ​
<static> JustDown(key) ​
Description:
The justDown value allows you to test if this Key has just been pressed down or not.
When you check this value it will return true if the Key is down, otherwise false .
You can only call justDown once per key press. It will only return true once, until the Key is released and pressed down again.
This allows you to use it in situations where you want to check if this key is down without using an event, such as in a core game loop.
Parameters:
name type optional description
key Phaser.Input.Keyboard.Key No The Key to check to see if it's just down or not.
Returns: boolean - true if the Key was just pressed, otherwise false .
Source: src/input/keyboard/keys/JustDown.js#L7
Since: 3.0.0
JustUp ​
<static> JustUp(key) ​
Description:
The justUp value allows you to test if this Key has just been released or not.
When you check this value it will return true if the Key is up, otherwise false .
You can only call JustUp once per key release. It will only return true once, until the Key is pressed down and released again.
This allows you to use it in situations where you want to check if this key is up without using an event, such as in a core game loop.
Parameters:
name type optional description
key Phaser.Input.Keyboard.Key No The Key to check to see if it's just up or not.
Returns: boolean - true if the Key was just released, otherwise false .
Source: src/input/keyboard/keys/JustUp.js#L7
Since: 3.0.0
UpDuration ​
<static> UpDuration(key, [duration]) ​
Description:
Returns true if the Key was released within the duration value given, based on the current
game clock time. Or returns false if it either isn't up, or was released longer ago than the given duration.
Parameters:
name type optional default description
key Phaser.Input.Keyboard.Key No The Key object to test.
duration number Yes 50 The duration, in ms, within which the key must have been released.
Returns: boolean - true if the Key was released within duration ms ago, otherwise false .
Source: src/input/keyboard/keys/UpDuration.js#L7
Since: 3.0.0
Static functions ​
Events
KeyCodes
Previous
Phaser.Input.Keyboard.KeyCodes
Next
Phaser.Input.Mouse
Static functions
Static functions
DownDuration
JustDown
JustUp
UpDuration
Static functions
