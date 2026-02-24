# Clock | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/time-clock

Phaser API Documentation
Class
Clock
Version: Phaser v3.90.0
On this page
Clock
The Clock is a Scene plugin which creates and updates Timer Events for its Scene.
Constructor
new Clock(scene)
Parameters
name type optional description
scene Phaser.Scene No The Scene which owns this Clock.
Scope : static
Source: src/time/Clock.js#L13
Since: 3.0.0
Public Members ​
now ​
now: number ​
Description:
The current time of the Clock, in milliseconds.
If accessed externally, this is equivalent to the time parameter normally passed to a Scene's update method.
Source: src/time/Clock.js#L48
Since: 3.0.0
paused ​
paused: boolean ​
Description:
Whether the Clock is paused ( true ) or active ( false ).
When paused, the Clock will not update any of its Timer Events, thus freezing time.
Source: src/time/Clock.js#L82
Since: 3.0.0
scene ​
scene: Phaser.Scene ​
Description:
The Scene which owns this Clock.
Source: src/time/Clock.js#L30
Since: 3.0.0
startTime ​
startTime: number ​
Description:
The time the Clock (and Scene) started, in milliseconds.
This can be compared to the time parameter passed to a Scene's update method.
Source: src/time/Clock.js#L59
Since: 3.60.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
The Scene Systems object of the Scene which owns this Clock.
Source: src/time/Clock.js#L39
Since: 3.0.0
timeScale ​
timeScale: number ​
Description:
The scale of the Clock's time delta.
The time delta is the time elapsed between two consecutive frames and influences the speed of time for this Clock and anything which uses it, such as its Timer Events. Values higher than 1 increase the speed of time, while values smaller than 1 decrease it. A value of 0 freezes time and is effectively equivalent to pausing the Clock.
Source: src/time/Clock.js#L70
Since: 3.0.0
Public Methods ​
addEvent ​
<instance> addEvent(config) ​
Description:
Creates a Timer Event and adds it to this Clock at the start of the next frame.
You can pass in either a TimerEventConfig object, from with a new TimerEvent will
be created, or you can pass in a TimerEvent instance.
If passing an instance please make sure that this instance hasn't been used before.
If it has ever entered a 'completed' state then it will no longer be suitable to
run again.
Also, if the TimerEvent instance is being used by another Clock (in another Scene)
it will still be updated by that Clock as well, so be careful when using this feature.
Parameters:
name type optional description
config Phaser.Time.TimerEvent | Phaser.Types.Time.TimerEventConfig No The configuration for the Timer Event, or an existing Timer Event object.
Returns: Phaser.Time.TimerEvent - The Timer Event which was created, or passed in.
Source: src/time/Clock.js#L167
Since: 3.0.0
clearPendingEvents ​
<instance> clearPendingEvents() ​
Description:
Clears and recreates the array of pending Timer Events.
Returns: Phaser.Time.Clock - - This Clock instance.
Source: src/time/Clock.js#L236
Since: 3.0.0
delayedCall ​
<instance> delayedCall(delay, callback, [args], [callbackScope]) ​
Description:
Creates a Timer Event and adds it to the Clock at the start of the frame.
This is a shortcut for #addEvent which can be shorter and is compatible with the syntax of the GreenSock Animation Platform (GSAP).
Parameters:
name type optional description
delay number No The delay of the function call, in milliseconds.
callback function No The function to call after the delay expires.
args Array.<*> Yes The arguments to call the function with.
callbackScope * Yes The scope ( this object) to call the function with.
Returns: Phaser.Time.TimerEvent - The Timer Event which was created.
Source: src/time/Clock.js#L216
Since: 3.0.0
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
Updates the arrays of active and pending Timer Events. Called at the start of the frame.
Parameters:
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/time/Clock.js#L298
Since: 3.0.0
removeAllEvents ​
<instance> removeAllEvents() ​
Description:
Schedules all active Timer Events for removal at the start of the frame.
Returns: Phaser.Time.Clock - - This Clock instance.
Source: src/time/Clock.js#L283
Since: 3.0.0
removeEvent ​
<instance> removeEvent(events) ​
Description:
Removes the given Timer Event, or an array of Timer Events, from this Clock.
The events are removed from all internal lists (active, pending and removal),
freeing the event up to be re-used.
Parameters:
name type optional description
events Phaser.Time.TimerEvent | Array.< Phaser.Time.TimerEvent > No The Timer Event, or an array of Timer Events, to remove from this Clock.
Returns: Phaser.Time.Clock - - This Clock instance.
Source: src/time/Clock.js#L251
Since: 3.50.0
update ​
<instance> update(time, delta) ​
Description:
Updates the Clock's internal time and all of its Timer Events.
Parameters:
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/time/Clock.js#L349
Since: 3.0.0
Previous
Tileset
Next
Timeline
Public Members
now
paused
scene
startTime
systems
timeScale
Public Methods
addEvent
clearPendingEvents
delayedCall
preUpdate
removeAllEvents
removeEvent
update
