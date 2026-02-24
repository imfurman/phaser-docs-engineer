# Axis | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-gamepad-axis

Phaser API Documentation
Class
Axis
Version: Phaser v3.90.0
On this page
Axis
Contains information about a specific Gamepad Axis.
Axis objects are created automatically by the Gamepad as they are needed.
Constructor
new Axis(pad, index)
Parameters
name type optional description
pad Phaser.Input.Gamepad.Gamepad No A reference to the Gamepad that this Axis belongs to.
index number No The index of this Axis.
Scope : static
Source: src/input/gamepad/Axis.js#L9
Since: 3.0.0
Public Members ​
events ​
events: Phaser.Events.EventEmitter ​
Description:
An event emitter to use to emit the axis events.
Source: src/input/gamepad/Axis.js#L37
Since: 3.0.0
index ​
index: number ​
Description:
The index of this Axis.
Source: src/input/gamepad/Axis.js#L46
Since: 3.0.0
pad ​
pad: Phaser.Input.Gamepad.Gamepad ​
Description:
A reference to the Gamepad that this Axis belongs to.
Source: src/input/gamepad/Axis.js#L28
Since: 3.0.0
threshold ​
threshold: number ​
Description:
Movement tolerance threshold below which axis values are ignored in getValue .
Source: src/input/gamepad/Axis.js#L66
Since: 3.0.0
value ​
value: number ​
Description:
The raw axis value, between -1 and 1 with 0 being dead center.
Use the method getValue to get a normalized value with the threshold applied.
Source: src/input/gamepad/Axis.js#L55
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Axis instance and releases external references it holds.
Source: src/input/gamepad/Axis.js#L105
Since: 3.10.0
getValue ​
<instance> getValue() ​
Description:
Applies the threshold value to the axis and returns it.
Returns: number - The axis value, adjusted for the movement threshold.
Source: src/input/gamepad/Axis.js#L92
Since: 3.0.0
Previous
Triangle
Next
Button
Public Members
events
index
pad
threshold
value
Public Methods
destroy
getValue
