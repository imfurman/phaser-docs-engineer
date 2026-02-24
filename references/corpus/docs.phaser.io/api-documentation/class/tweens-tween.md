# Tween | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tweens-tween

Phaser API Documentation
Class
Tween
Version: Phaser v3.90.0
On this page
Tween
A Tween is able to manipulate the properties of one or more objects to any given value, based
on a duration and type of ease. They are rarely instantiated directly and instead should be
created via the TweenManager.
Please note that a Tween will not manipulate any property that begins with an underscore.
Constructor
new Tween(parent, targets)
Parameters
name type optional description
parent Phaser.Tweens.TweenManager No A reference to the Tween Manager that owns this Tween.
targets Array.<object> No An array of targets to be tweened. This array should not be manipulated outside of this Tween.
Scope : static
Extends
Phaser.Tweens.BaseTween
Source: src/tweens/tween/Tween.js#L17
Since: 3.0.0
Inherited Members ​
From Phaser.Tweens.BaseTween :
callbacks
callbackScope
completeDelay
countdown
data
hasStarted
loop
loopCounter
loopDelay
parent
paused
persist
startDelay
state
timeScale
totalData
Public Members ​
duration ​
duration: number ​
Description:
Time in milliseconds for the whole Tween to play through once, excluding loop amounts and loop delays.
This value is set in the Tween.initTweenData method and is zero before that point.
Source: src/tweens/tween/Tween.js#L112
Since: 3.60.0
elapsed ​
elapsed: number ​
Description:
Elapsed time in milliseconds of this run through of the Tween.
Source: src/tweens/tween/Tween.js#L92
Since: 3.60.0
isInfinite ​
isInfinite: boolean ​
Description:
Does this Tween loop or repeat infinitely?
Source: src/tweens/tween/Tween.js#L82
Since: 3.60.0
isNumberTween ​
isNumberTween: boolean ​
Description:
Is this Tween a Number Tween? Number Tweens are a special kind of tween that don't have a target.
Source: src/tweens/tween/Tween.js#L158
Since: 3.88.0
isSeeking ​
isSeeking: boolean ​
Description:
Is this Tween currently seeking?
This boolean is toggled in the Tween.seek method.
When a tween is seeking, by default it will not dispatch any events or callbacks.
Source: src/tweens/tween/Tween.js#L68
Since: 3.19.0
progress ​
progress: number ​
Description:
Value between 0 and 1. The amount of progress through the Tween, excluding loops.
Source: src/tweens/tween/Tween.js#L124
Since: 3.60.0
targets ​
targets: Array.<object> ​
Description:
An array of references to the target/s this Tween is operating on.
This array should not be manipulated outside of this Tween.
Source: src/tweens/tween/Tween.js#L44
Since: 3.0.0
totalDuration ​
totalDuration: number ​
Description:
Time in milliseconds it takes for the Tween to complete a full playthrough (including looping)
For an infinite Tween, this value is a very large integer.
Source: src/tweens/tween/Tween.js#L134
Since: 3.60.0
totalElapsed ​
totalElapsed: number ​
Description:
Total elapsed time in milliseconds of the entire Tween, including looping.
Source: src/tweens/tween/Tween.js#L102
Since: 3.60.0
totalProgress ​
totalProgress: number ​
Description:
The amount of progress that has been made through the entire Tween, including looping.
A value between 0 and 1.
Source: src/tweens/tween/Tween.js#L146
Since: 3.60.0
totalTargets ​
totalTargets: number ​
Description:
Cached target total.
Used internally and should be treated as read-only.
This is not necessarily the same as the data total.
Source: src/tweens/tween/Tween.js#L55
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
From Phaser.Tweens.BaseTween :
complete
completeAfterLoop
getTimeScale
isActive
isCompleteDelayed
isDestroyed
isFinished
isLoopDelayed
isPaused
isPending
isPendingRemove
isPlaying
isRemoved
isStartDelayed
makeActive
pause
remove
resume
setActiveState
setCallback
setCompleteDelayState
setDestroyedState
setFinishedState
setLoopDelayState
setPendingRemoveState
setPendingState
setRemovedState
setStartDelayState
setTimeScale
stop
updateCompleteDelay
updateLoopCountdown
updateStartCountdown
Public Methods ​
add ​
<instance> add(targetIndex, key, getEnd, getStart, getActive, ease, delay, duration, yoyo, hold, repeat, repeatDelay, flipX, flipY, interpolation, interpolationData) ​
Description:
Adds a new TweenData to this Tween. Typically, this method is called
automatically by the TweenBuilder, however you can also invoke it
yourself.
Parameters:
name type optional description
targetIndex number No The target index within the Tween targets array.
key string No The property of the target to tween.
getEnd Phaser.Types.Tweens.GetEndCallback No What the property will be at the END of the Tween.
getStart Phaser.Types.Tweens.GetStartCallback No What the property will be at the START of the Tween.
getActive Phaser.Types.Tweens.GetActiveCallback No If not null, is invoked immediately as soon as the TweenData is running, and is set on the target property.
ease function No The ease function this tween uses.
delay function No Function that returns the time in milliseconds before tween will start.
duration number No The duration of the tween in milliseconds.
yoyo boolean No Determines whether the tween should return back to its start value after hold has expired.
hold number No Function that returns the time in milliseconds the tween will pause before repeating or returning to its starting value if yoyo is set to true.
repeat number No Function that returns the number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice.
repeatDelay number No Function that returns the time in milliseconds before the repeat will start.
flipX boolean No Should toggleFlipX be called when yoyo or repeat happens?
flipY boolean No Should toggleFlipY be called when yoyo or repeat happens?
interpolation function No The interpolation function to be used for arrays of data. Defaults to 'null'.
interpolationData Array.<number> No The array of interpolation data to be set. Defaults to 'null'.
Returns: Phaser.Tweens.TweenData - The TweenData instance that was added.
Source: src/tweens/tween/Tween.js#L169
Since: 3.60.0
addFrame ​
<instance> addFrame(targetIndex, texture, frame, delay, duration, hold, repeat, repeatDelay, flipX, flipY) ​
Description:
Adds a new TweenFrameData to this Tween. Typically, this method is called
automatically by the TweenBuilder, however you can also invoke it
yourself.
Parameters:
name type optional description
targetIndex number No The target index within the Tween targets array.
texture string No The texture to set on the target at the end of the tween.
frame string | number No The texture frame to set on the target at the end of the tween.
delay function No Function that returns the time in milliseconds before tween will start.
duration number No The duration of the tween in milliseconds.
hold number No Function that returns the time in milliseconds the tween will pause before repeating or returning to its starting value if yoyo is set to true.
repeat number No Function that returns the number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice.
repeatDelay number No Function that returns the time in milliseconds before the repeat will start.
flipX boolean No Should toggleFlipX be called when yoyo or repeat happens?
flipY boolean No Should toggleFlipY be called when yoyo or repeat happens?
Returns: Phaser.Tweens.TweenFrameData - The TweenFrameData instance that was added.
Source: src/tweens/tween/Tween.js#L205
Since: 3.60.0
destroy ​
<instance> destroy() ​
Description:
Handles the destroy process of this Tween, clearing out the
Tween Data and resetting the targets. A Tween that has been
destroyed cannot ever be played or used again.
Overrides: Phaser.Tweens.BaseTween#destroy
Source: src/tweens/tween/Tween.js#L816
Since: 3.60.0
dispatchEvent ​
<instance> dispatchEvent(event, [callback]) ​
Description:
Internal method that will emit a Tween based Event and invoke the given callback.
Parameters:
name type optional description
event Phaser.Types.Tweens.Event No The Event to be dispatched.
callback Phaser.Types.Tweens.TweenCallbackTypes Yes The name of the callback to be invoked. Can be null or undefined to skip invocation.
Source: src/tweens/tween/Tween.js#L787
Since: 3.60.0
forward ​
<instance> forward(ms) ​
Description:
Moves this Tween forward by the given amount of milliseconds.
It will only advance through the current loop of the Tween. For example, if the
Tween is set to repeat or yoyo, it can only fast forward through a single
section of the sequence. Use Tween.seek for more complex playhead control.
If the Tween is paused or has already finished, calling this will have no effect.
Parameters:
name type optional description
ms number No The number of milliseconds to advance this Tween by.
Returns: Phaser.Tweens.Tween - This Tween instance.
Source: src/tweens/tween/Tween.js#L741
Since: 3.60.0
getValue ​
<instance> getValue([index]) ​
Description:
Returns the current value of the specified Tween Data.
If this Tween has been destroyed, it will return null .
Parameters:
name type optional default description
index number Yes 0 The Tween Data to return the value from.
Returns: number, null - The value of the requested Tween Data, or null if this Tween has been destroyed.
Source: src/tweens/tween/Tween.js#L235
Since: 3.0.0
hasTarget ​
<instance> hasTarget(target) ​
Description:
See if this Tween is currently acting upon the given target.
Parameters:
name type optional description
target object No The target to check against this Tween.
Returns: boolean - true if the given target is a target of this Tween, otherwise false .
Source: src/tweens/tween/Tween.js#L261
Since: 3.0.0
initTweenData ​
<instance> initTweenData([isSeeking]) ​
Description:
Initialises all of the Tween Data and Tween values.
This is called automatically and should not typically be invoked directly.
Parameters:
name type optional default description
isSeeking boolean Yes false Is the Tween Data being reset as part of a seek?
Source: src/tweens/tween/Tween.js#L553
Since: 3.60.0
nextState ​
<instance> nextState() ​
Description:
Internal method that advances to the next state of the Tween during playback.
Returns: boolean - true if this Tween has completed, otherwise false .
Fires: Phaser.Tweens.Events#event:TWEEN_COMPLETE , Phaser.Tweens.Events#event:TWEEN_LOOP
Source: src/tweens/tween/Tween.js#L365
Since: 3.0.0
onCompleteHandler ​
<instance> onCompleteHandler() ​
Description:
Internal method that handles this tween completing and starting
the next tween in the chain, if any.
Overrides: Phaser.Tweens.BaseTween#onCompleteHandler
Source: src/tweens/tween/Tween.js#L414
Since: 3.60.0
play ​
<instance> play() ​
Description:
Starts a Tween playing.
You only need to call this method if you have configured the tween to be paused on creation.
If the Tween is already playing, calling this method again will have no effect. If you wish to
restart the Tween, use Tween.restart instead.
Calling this method after the Tween has completed will start the Tween playing again from the beginning.
This is the same as calling Tween.seek(0) and then Tween.play() .
Returns: Phaser.Tweens.Tween - This Tween instance.
Source: src/tweens/tween/Tween.js#L429
Since: 3.0.0
reset ​
<instance> reset([skipInit]) ​
Description:
Resets this Tween ready for another play-through.
This is called automatically from the Tween Manager, or from the parent TweenChain,
and should not typically be invoked directly.
If you wish to restart this Tween, use the Tween.restart or Tween.seek methods instead.
Parameters:
name type optional default description
skipInit boolean Yes false Skip resetting the TweenData and Active State?
Returns: Phaser.Tweens.Tween - This Tween instance.
Fires: Phaser.Tweens.Events#event:TWEEN_ACTIVE
Source: src/tweens/tween/Tween.js#L596
Since: 3.60.0
restart ​
<instance> restart() ​
Description:
Restarts the Tween from the beginning.
If the Tween has already finished and been destroyed, restarting it will throw an error.
If you wish to restart the Tween from a specific point, use the Tween.seek method instead.
Returns: Phaser.Tweens.Tween - This Tween instance.
Source: src/tweens/tween/Tween.js#L323
Since: 3.0.0
rewind ​
<instance> rewind(ms) ​
Description:
Moves this Tween backward by the given amount of milliseconds.
It will only rewind through the current loop of the Tween. For example, if the
Tween is set to repeat or yoyo, it can only fast forward through a single
section of the sequence. Use Tween.seek for more complex playhead control.
If the Tween is paused or has already finished, calling this will have no effect.
Parameters:
name type optional description
ms number No The number of milliseconds to rewind this Tween by.
Returns: Phaser.Tweens.Tween - This Tween instance.
Source: src/tweens/tween/Tween.js#L764
Since: 3.60.0
seek ​
<instance> seek([amount], [delta], [emit]) ​
Description:
Seeks to a specific point in the Tween.
The given amount is a value in milliseconds that represents how far into the Tween
you wish to seek, based on the start of the Tween.
Note that the seek amount takes the entire duration of the Tween into account, including delays, loops and repeats.
For example, a Tween that lasts for 2 seconds, but that loops 3 times, would have a total duration of 6 seconds,
so seeking to 3000 ms would seek to the Tweens half-way point based on its entire duration.
Prior to Phaser 3.60 this value was given as a number between 0 and 1 and didn't
work for Tweens had an infinite repeat. This new method works for all Tweens.
Seeking works by resetting the Tween to its initial values and then iterating through the Tween at delta
jumps per step. The longer the Tween, the longer this can take. If you need more precision you can
reduce the delta value. If you need a faster seek, you can increase it. When the Tween is
reset it will refresh the starting and ending values. If these are coming from a dynamic function,
or a random array, it will be called for each seek.
While seeking the Tween will not emit any of its events or callbacks unless
the 3rd parameter is set to true .
If this Tween is paused, seeking will not change this fact. It will advance the Tween
to the desired point and then pause it again.
Parameters:
name type optional default description
amount number Yes 0 The number of milliseconds to seek into the Tween from the beginning.
delta number Yes 16.6 The size of each step when seeking through the Tween. A higher value completes faster but at the cost of less precision.
emit boolean Yes false While seeking, should the Tween emit any of its events or callbacks? The default is 'false', i.e. to seek silently.
Returns: Phaser.Tweens.Tween - This Tween instance.
Source: src/tweens/tween/Tween.js#L466
Since: 3.0.0
update ​
<instance> update(delta) ​
Description:
Internal method that advances the Tween based on the time values.
Parameters:
name type optional description
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Returns: boolean - Returns true if this Tween has finished and should be removed from the Tween Manager, otherwise returns false .
Fires: Phaser.Tweens.Events#event:TWEEN_COMPLETE , Phaser.Tweens.Events#event:TWEEN_LOOP , Phaser.Tweens.Events#event:TWEEN_START
Source: src/tweens/tween/Tween.js#L640
Since: 3.0.0
updateTo ​
<instance> updateTo(key, value, [startToCurrent]) ​
Description:
Updates the 'end' value of the given property across all matching targets, as long
as this Tween is currently playing (either forwards or backwards).
Calling this does not adjust the duration of the Tween, or the current progress.
You can optionally tell it to set the 'start' value to be the current value.
If this Tween is in any other state other than playing then calling this method has no effect.
Additionally, if the Tween repeats, is reset, or is seeked, it will revert to the original
starting and ending values.
Parameters:
name type optional default description
key string No The property to set the new value for. You cannot update the 'texture' property via this method.
value number No The new value of the property.
startToCurrent boolean Yes false Should this change set the start value to be the current value?
Returns: Phaser.Tweens.Tween - This Tween instance.
Source: src/tweens/tween/Tween.js#L276
Since: 3.0.0
Previous
BaseTweenData
Next
TweenChain
Inherited Members
Public Members
duration
elapsed
isInfinite
isNumberTween
isSeeking
progress
targets
totalDuration
totalElapsed
totalProgress
totalTargets
Inherited Methods
Public Methods
add
addFrame
destroy
dispatchEvent
forward
getValue
hasTarget
initTweenData
nextState
onCompleteHandler
play
reset
restart
rewind
seek
update
updateTo
