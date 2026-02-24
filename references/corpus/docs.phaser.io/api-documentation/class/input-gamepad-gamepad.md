# Gamepad | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-gamepad-gamepad

Phaser API Documentation
Class
Gamepad
Version: Phaser v3.90.0
On this page
Gamepad
A single Gamepad.
These are created, updated and managed by the Gamepad Plugin.
Constructor
new Gamepad(manager, pad)
Parameters
name type optional description
manager Phaser.Input.Gamepad.GamepadPlugin No A reference to the Gamepad Plugin.
pad Phaser.Types.Input.Gamepad.Pad No The Gamepad object, as extracted from GamepadEvent.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/input/gamepad/Gamepad.js#L13
Since: 3.0.0
Public Members ​
A ​
A: boolean ​
Description:
Is the Gamepad's bottom button in the right button cluster being pressed?
If the Gamepad doesn't have this button it will always return false.
On a Dual Shock controller it's the X button.
On an XBox controller it's the A button.
Source: src/input/gamepad/Gamepad.js#L609
Since: 3.10.0
axes ​
axes: Array.< Phaser.Input.Gamepad.Axis > ​
Description:
An array of Gamepad Axis objects, corresponding to the different axes available on the Gamepad, if any.
Source: src/input/gamepad/Gamepad.js#L105
Since: 3.0.0
B ​
B: boolean ​
Description:
Is the Gamepad's right button in the right button cluster being pressed?
If the Gamepad doesn't have this button it will always return false.
On a Dual Shock controller it's the Circle button.
On an XBox controller it's the B button.
Source: src/input/gamepad/Gamepad.js#L666
Since: 3.10.0
buttons ​
buttons: Array.< Phaser.Input.Gamepad.Button > ​
Description:
An array of Gamepad Button objects, corresponding to the different buttons available on the Gamepad.
Source: src/input/gamepad/Gamepad.js#L89
Since: 3.0.0
connected ​
connected: boolean ​
Description:
Is this Gamepad currently connected or not?
Source: src/input/gamepad/Gamepad.js#L504
Since: 3.0.0
down ​
down: boolean ​
Description:
Is the Gamepad's Down button being pressed?
If the Gamepad doesn't have this button it will always return false.
This is the d-pad down button under standard Gamepad mapping.
Source: src/input/gamepad/Gamepad.js#L591
Since: 3.10.0
id ​
id: string ​
Description:
A string containing some information about the controller.
This is not strictly specified, but in Firefox it will contain three pieces of information
separated by dashes (-): two 4-digit hexadecimal strings containing the USB vendor and
product id of the controller, and the name of the controller as provided by the driver.
In Chrome it will contain the name of the controller as provided by the driver,
followed by vendor and product 4-digit hexadecimal strings.
Source: src/input/gamepad/Gamepad.js#L56
Since: 3.0.0
index ​
index: number ​
Description:
An integer that is unique for each Gamepad currently connected to the system.
This can be used to distinguish multiple controllers.
Note that disconnecting a device and then connecting a new device may reuse the previous index.
Source: src/input/gamepad/Gamepad.js#L71
Since: 3.0.0
L1 ​
L1: number ​
Description:
Returns the value of the Gamepad's top left shoulder button.
If the Gamepad doesn't have this button it will always return zero.
The value is a float between 0 and 1, corresponding to how depressed the button is.
On a Dual Shock controller it's the L1 button.
On an XBox controller it's the LB button.
Source: src/input/gamepad/Gamepad.js#L685
Since: 3.10.0
L2 ​
L2: number ​
Description:
Returns the value of the Gamepad's bottom left shoulder button.
If the Gamepad doesn't have this button it will always return zero.
The value is a float between 0 and 1, corresponding to how depressed the button is.
On a Dual Shock controller it's the L2 button.
On an XBox controller it's the LT button.
Source: src/input/gamepad/Gamepad.js#L705
Since: 3.10.0
left ​
left: boolean ​
Description:
Is the Gamepad's Left button being pressed?
If the Gamepad doesn't have this button it will always return false.
This is the d-pad left button under standard Gamepad mapping.
Source: src/input/gamepad/Gamepad.js#L537
Since: 3.10.0
leftStick ​
leftStick: Phaser.Math.Vector2 ​
Description:
A Vector2 containing the most recent values from the Gamepad's left axis stick.
This is updated automatically as part of the Gamepad.update cycle.
The H Axis is mapped to the Vector2.x property, and the V Axis to the Vector2.y property.
The values are based on the Axis thresholds.
If the Gamepad does not have a left axis stick, the values will always be zero.
Source: src/input/gamepad/Gamepad.js#L291
Since: 3.10.0
manager ​
manager: Phaser.Input.Gamepad.GamepadPlugin ​
Description:
A reference to the Gamepad Plugin.
Source: src/input/gamepad/Gamepad.js#L38
Since: 3.0.0
pad ​
pad: any ​
Description:
A reference to the native Gamepad object that is connected to the browser.
Source: src/input/gamepad/Gamepad.js#L47
Since: 3.10.0
R1 ​
R1: number ​
Description:
Returns the value of the Gamepad's top right shoulder button.
If the Gamepad doesn't have this button it will always return zero.
The value is a float between 0 and 1, corresponding to how depressed the button is.
On a Dual Shock controller it's the R1 button.
On an XBox controller it's the RB button.
Source: src/input/gamepad/Gamepad.js#L725
Since: 3.10.0
R2 ​
R2: number ​
Description:
Returns the value of the Gamepad's bottom right shoulder button.
If the Gamepad doesn't have this button it will always return zero.
The value is a float between 0 and 1, corresponding to how depressed the button is.
On a Dual Shock controller it's the R2 button.
On an XBox controller it's the RT button.
Source: src/input/gamepad/Gamepad.js#L745
Since: 3.10.0
right ​
right: boolean ​
Description:
Is the Gamepad's Right button being pressed?
If the Gamepad doesn't have this button it will always return false.
This is the d-pad right button under standard Gamepad mapping.
Source: src/input/gamepad/Gamepad.js#L555
Since: 3.10.0
rightStick ​
rightStick: Phaser.Math.Vector2 ​
Description:
A Vector2 containing the most recent values from the Gamepad's right axis stick.
This is updated automatically as part of the Gamepad.update cycle.
The H Axis is mapped to the Vector2.x property, and the V Axis to the Vector2.y property.
The values are based on the Axis thresholds.
If the Gamepad does not have a right axis stick, the values will always be zero.
Source: src/input/gamepad/Gamepad.js#L304
Since: 3.10.0
timestamp ​
timestamp: number ​
Description:
A timestamp containing the most recent time this Gamepad was updated.
Source: src/input/gamepad/Gamepad.js#L521
Since: 3.0.0
up ​
up: boolean ​
Description:
Is the Gamepad's Up button being pressed?
If the Gamepad doesn't have this button it will always return false.
This is the d-pad up button under standard Gamepad mapping.
Source: src/input/gamepad/Gamepad.js#L573
Since: 3.10.0
vibration ​
vibration: GamepadHapticActuator ​
Description:
The Gamepad's Haptic Actuator (Vibration / Rumble support).
This is highly experimental and only set if both present on the device,
and exposed by both the hardware and browser.
Source: src/input/gamepad/Gamepad.js#L114
Since: 3.10.0
X ​
X: boolean ​
Description:
Is the Gamepad's left button in the right button cluster being pressed?
If the Gamepad doesn't have this button it will always return false.
On a Dual Shock controller it's the Square button.
On an XBox controller it's the X button.
Source: src/input/gamepad/Gamepad.js#L647
Since: 3.10.0
Y ​
Y: boolean ​
Description:
Is the Gamepad's top button in the right button cluster being pressed?
If the Gamepad doesn't have this button it will always return false.
On a Dual Shock controller it's the Triangle button.
On an XBox controller it's the Y button.
Source: src/input/gamepad/Gamepad.js#L628
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
shutdown
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Gamepad instance, its buttons and axes, and releases external references it holds.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/input/gamepad/Gamepad.js#L475
Since: 3.10.0
getAxisTotal ​
<instance> getAxisTotal() ​
Description:
Gets the total number of axis this Gamepad claims to support.
Returns: number - The total number of axes this Gamepad claims to support.
Source: src/input/gamepad/Gamepad.js#L328
Since: 3.10.0
getAxisValue ​
<instance> getAxisValue(index) ​
Description:
Gets the value of an axis based on the given index.
The index must be valid within the range of axes supported by this Gamepad.
The return value will be a float between 0 and 1.
Parameters:
name type optional description
index number No The index of the axes to get the value for.
Returns: number - The value of the axis, between 0 and 1.
Source: src/input/gamepad/Gamepad.js#L341
Since: 3.10.0
getButtonTotal ​
<instance> getButtonTotal() ​
Description:
Gets the total number of buttons this Gamepad claims to have.
Returns: number - The total number of buttons this Gamepad claims to have.
Source: src/input/gamepad/Gamepad.js#L375
Since: 3.10.0
getButtonValue ​
<instance> getButtonValue(index) ​
Description:
Gets the value of a button based on the given index.
The index must be valid within the range of buttons supported by this Gamepad.
The return value will be either 0 or 1 for an analogue button, or a float between 0 and 1
for a pressure-sensitive digital button, such as the shoulder buttons on a Dual Shock.
Parameters:
name type optional description
index number No The index of the button to get the value for.
Returns: number - The value of the button, between 0 and 1.
Source: src/input/gamepad/Gamepad.js#L388
Since: 3.10.0
isButtonDown ​
<instance> isButtonDown(index) ​
Description:
Returns if the button is pressed down or not.
The index must be valid within the range of buttons supported by this Gamepad.
Parameters:
name type optional description
index number No The index of the button to get the value for.
Returns: boolean - true if the button is considered as being pressed down, otherwise false .
Source: src/input/gamepad/Gamepad.js#L407
Since: 3.10.0
setAxisThreshold ​
<instance> setAxisThreshold(value) ​
Description:
Sets the threshold value of all axis on this Gamepad.
The value is a float between 0 and 1 and is the amount below which the axis is considered as not having been moved.
Parameters:
name type optional description
value number No A value between 0 and 1.
Source: src/input/gamepad/Gamepad.js#L358
Since: 3.10.0
Previous
Button
Next
GamepadPlugin
Public Members
A
axes
B
buttons
connected
down
id
index
L1
L2
left
leftStick
manager
pad
R1
R2
right
rightStick
timestamp
up
vibration
X
Y
Inherited Methods
Public Methods
destroy
getAxisTotal
getAxisValue
getButtonTotal
getButtonValue
isButtonDown
setAxisThreshold
