# Button | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-gamepad-button

Phaser API Documentation
Class
Button
Version: Phaser v3.90.0
On this page
Button
Contains information about a specific button on a Gamepad.
Button objects are created automatically by the Gamepad as they are needed.
Constructor
new Button(pad, index)
Parameters
name type optional description
pad Phaser.Input.Gamepad.Gamepad No A reference to the Gamepad that this Button belongs to.
index number No The index of this Button.
Scope : static
Source: src/input/gamepad/Button.js#L10
Since: 3.0.0
Public Members ​
events ​
events: Phaser.Events.EventEmitter ​
Description:
An event emitter to use to emit the button events.
Source: src/input/gamepad/Button.js#L38
Since: 3.0.0
index ​
index: number ​
Description:
The index of this Button.
Source: src/input/gamepad/Button.js#L47
Since: 3.0.0
pad ​
pad: Phaser.Input.Gamepad.Gamepad ​
Description:
A reference to the Gamepad that this Button belongs to.
Source: src/input/gamepad/Button.js#L29
Since: 3.0.0
pressed ​
pressed: boolean ​
Description:
Is the Button being pressed down or not?
Source: src/input/gamepad/Button.js#L77
Since: 3.0.0
threshold ​
threshold: number ​
Description:
Can be set for analogue buttons to enable a 'pressure' threshold,
before a button is considered as being 'pressed'.
Source: src/input/gamepad/Button.js#L66
Since: 3.0.0
value ​
value: number ​
Description:
Between 0 and 1.
Source: src/input/gamepad/Button.js#L56
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Button instance and releases external references it holds.
Source: src/input/gamepad/Button.js#L126
Since: 3.10.0
Previous
Axis
Next
Gamepad
Public Members
events
index
pad
pressed
threshold
value
Public Methods
destroy
