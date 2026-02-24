# RequestAnimationFrame | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/dom-requestanimationframe

Phaser API Documentation
Class
RequestAnimationFrame
Version: Phaser v3.90.0
On this page
RequestAnimationFrame
Abstracts away the use of RAF or setTimeOut for the core game update loop.
This is invoked automatically by the Phaser.Game instance.
Scope : static
Source: src/dom/RequestAnimationFrame.js#L10
Since: 3.0.0
Public Members ​
callback ​
callback: FrameRequestCallback ​
Description:
The callback to be invoked each step.
Source: src/dom/RequestAnimationFrame.js#L37
Since: 3.0.0
delay ​
delay: number ​
Description:
The delay rate in ms for setTimeOut.
Source: src/dom/RequestAnimationFrame.js#L66
Since: 3.60.0
isRunning ​
isRunning: boolean ​
Description:
True if RequestAnimationFrame is running, otherwise false.
Source: src/dom/RequestAnimationFrame.js#L27
Since: 3.0.0
isSetTimeOut ​
isSetTimeOut: boolean ​
Description:
True if the step is using setTimeout instead of RAF.
Source: src/dom/RequestAnimationFrame.js#L46
Since: 3.0.0
step ​
step: FrameRequestCallback ​
Description:
The RAF step function.
Invokes the callback and schedules another call to requestAnimationFrame.
Parameters:
name type optional description
time number No The timestamp passed in from RequestAnimationFrame.
Source: src/dom/RequestAnimationFrame.js#L78
Since: 3.0.0
stepTimeout ​
stepTimeout: function ​
Description:
The SetTimeout step function.
Invokes the callback and schedules another call to setTimeout.
Source: src/dom/RequestAnimationFrame.js#L99
Since: 3.0.0
timeOutID ​
timeOutID: number ​
Description:
The setTimeout or RAF callback ID used when canceling them.
Source: src/dom/RequestAnimationFrame.js#L56
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Stops the step from running and clears the callback reference.
Source: src/dom/RequestAnimationFrame.js#L168
Since: 3.0.0
start ​
<instance> start(callback, forceSetTimeOut, delay) ​
Description:
Starts the requestAnimationFrame or setTimeout process running.
Parameters:
name type optional description
callback FrameRequestCallback No The callback to invoke each step.
forceSetTimeOut boolean No Should it use SetTimeout, even if RAF is available?
delay number No The setTimeout delay rate in ms.
Source: src/dom/RequestAnimationFrame.js#L120
Since: 3.0.0
stop ​
<instance> stop() ​
Description:
Stops the requestAnimationFrame or setTimeout from running.
Source: src/dom/RequestAnimationFrame.js#L148
Since: 3.0.0
Previous
Spline
Next
DataManager
Public Members
callback
delay
isRunning
isSetTimeOut
step
stepTimeout
timeOutID
Public Methods
destroy
start
stop
