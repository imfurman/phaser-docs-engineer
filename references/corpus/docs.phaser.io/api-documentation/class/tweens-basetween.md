# BaseTween | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tweens-basetween

Phaser API Documentation
Class
BaseTween
Version: Phaser v3.90.0
On this page
BaseTween
As the name implies, this is the base Tween class that both the Tween and TweenChain
inherit from. It contains shared properties and methods common to both types of Tween.
Typically you would never instantiate this class directly, although you could certainly
use it to create your own variation of Tweens from.
Constructor
new BaseTween(parent)
Parameters
name type optional description
parent Phaser.Tweens.TweenManager | Phaser.Tweens.TweenChain No A reference to the Tween Manager, or Tween Chain, that owns this Tween.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/tweens/tween/BaseTween.js#L12
Since: 3.60.0
Public Members ​
callbacks ​
callbacks: Phaser.Types.Tweens.TweenCallbacks ​
Description:
An object containing the different Tween callback functions.
You can either set these in the Tween config, or by calling the Tween.setCallback method.
The types available are:
onActive - When the Tween is first created it moves to an 'active' state when added to the Tween Manager. 'Active' does not mean 'playing'.
onStart - When the Tween starts playing after a delayed or paused state. This will happen at the same time as onActive if the tween has no delay and isn't paused.
onLoop - When a Tween loops, if it has been set to do so. This happens after the loopDelay expires, if set.
onComplete - When the Tween finishes playback fully. Never invoked if the Tween is set to repeat infinitely.
onStop - Invoked only if the Tween.stop method is called.
onPause - Invoked only if the Tween.pause method is called. Not invoked if the Tween Manager is paused.
onResume - Invoked only if the Tween.resume method is called. Not invoked if the Tween Manager is resumed.
The following types are also available and are invoked on a TweenData level - that is per-object, per-property, being tweened.
onYoyo - When a TweenData starts a yoyo. This happens after the hold delay expires, if set.
onRepeat - When a TweenData repeats playback. This happens after the repeatDelay expires, if set.
onUpdate - When a TweenData updates a property on a source target during playback.
Source: src/tweens/tween/BaseTween.js#L195
Since: 3.60.0
callbackScope ​
callbackScope: any ​
Description:
The scope (or context) in which all of the callbacks are invoked.
This defaults to be this Tween, but you can override this property
to set it to whatever object you require.
Source: src/tweens/tween/BaseTween.js#L233
Since: 3.60.0
completeDelay ​
completeDelay: number ​
Description:
The time in milliseconds before the 'onComplete' event fires.
This never fires if loop = -1 as it never completes because it has been
set to loop forever.
Source: src/tweens/tween/BaseTween.js#L149
Since: 3.60.0
countdown ​
countdown: number ​
Description:
An internal countdown timer (used by loopDelay and completeDelay)
Source: src/tweens/tween/BaseTween.js#L162
Since: 3.60.0
data ​
data: Array.< Phaser.Tweens.TweenData >, Array.< Phaser.Tweens.Tween > ​
Description:
The main data array. For a Tween, this contains all of the TweenData objects, each
containing a unique property and target that is being tweened.
For a TweenChain, this contains an array of Tween instances, which are being played
through in sequence.
Source: src/tweens/tween/BaseTween.js#L47
Since: 3.60.0
hasStarted ​
hasStarted: boolean ​
Description:
Has this Tween started playback yet?
This boolean is toggled when the Tween leaves the 'start delayed' state and begins running.
Source: src/tweens/tween/BaseTween.js#L82
Since: 3.60.0
loop ​
loop: number ​
Description:
The number of times this Tween will loop.
Can be -1 for an infinite loop, zero for none, or a positive integer.
Typically this is set in the configuration object, but can also be set directly
as long as this Tween is paused and hasn't started playback.
When enabled it will play through ALL Tweens again.
Use TweenData.repeat to loop a single element.
Source: src/tweens/tween/BaseTween.js#L108
Since: 3.60.0
loopCounter ​
loopCounter: number ​
Description:
Internal counter recording how many loops are left to run.
Source: src/tweens/tween/BaseTween.js#L139
Since: 3.60.0
loopDelay ​
loopDelay: number ​
Description:
The time in milliseconds before the Tween loops.
Only used if loop is > 0.
Source: src/tweens/tween/BaseTween.js#L127
Since: 3.60.0
parent ​
parent: Phaser.Tweens.TweenManager , Phaser.Tweens.TweenChain ​
Description:
A reference to the Tween Manager, or Tween Chain, that owns this Tween.
Source: src/tweens/tween/BaseTween.js#L38
Since: 3.60.0
paused ​
paused: boolean ​
Description:
Is the Tween currently paused?
A paused Tween needs to be started with the play method, or resumed with the resume method.
This property can be toggled at runtime if required.
Source: src/tweens/tween/BaseTween.js#L181
Since: 3.60.0
persist ​
persist: boolean ​
Description:
Will this Tween persist after playback? A Tween that persists will not be destroyed by the
Tween Manager, or when calling Tween.stop , and can be re-played as required. You can either
set this property when creating the tween in the tween config, or set it prior to playback.
However, it's up to you to ensure you destroy persistent tweens when you are finished with them,
or they will retain references you may no longer require and waste memory.
By default, Tweens are set to not persist, so they are automatically cleaned-up by
the Tween Manager.
Source: src/tweens/tween/BaseTween.js#L245
Since: 3.60.0
startDelay ​
startDelay: number ​
Description:
The time in milliseconds before the 'onStart' event fires.
For a Tween, this is the shortest delay value across all of the TweenDatas it owns.
For a TweenChain, it is whatever delay value was given in the configuration.
Source: src/tweens/tween/BaseTween.js#L69
Since: 3.60.0
state ​
state: Phaser.Tweens.StateType ​
Description:
The current state of the Tween.
Source: src/tweens/tween/BaseTween.js#L172
Since: 3.60.0
timeScale ​
timeScale: number ​
Description:
Scales the time applied to this Tween. A value of 1 runs in real-time. A value of 0.5 runs 50% slower, and so on.
The value isn't used when calculating total duration of the tween, it's a run-time delta adjustment only.
This value is multiplied by the TweenManager.timeScale .
Source: src/tweens/tween/BaseTween.js#L94
Since: 3.60.0
totalData ​
totalData: number ​
Description:
The cached size of the data array.
Source: src/tweens/tween/BaseTween.js#L60
Since: 3.60.0
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
complete ​
<instance> complete([delay]) ​
Description:
Flags the Tween as being complete, whatever stage of progress it is at.
If an onComplete callback has been defined it will automatically invoke it, unless a delay
argument is provided, in which case the Tween will delay for that period of time before calling the callback.
If you don't need a delay or don't have an onComplete callback then call Tween.stop instead.
Parameters:
name type optional default description
delay number Yes 0 The time to wait before invoking the complete callback. If zero it will fire immediately.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Fires: Phaser.Tweens.Events#event:TWEEN_COMPLETE
Source: src/tweens/tween/BaseTween.js#L404
Since: 3.2.0
completeAfterLoop ​
<instance> completeAfterLoop([loops]) ​
Description:
Flags the Tween as being complete only once the current loop has finished.
This is a useful way to stop an infinitely looping tween once a complete cycle is over,
rather than abruptly.
If you don't have a loop then call Tween.stop instead.
Parameters:
name type optional default description
loops number Yes 0 The number of loops that should finish before this tween completes. Zero means complete just the current loop.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Fires: Phaser.Tweens.Events#event:TWEEN_COMPLETE
Source: src/tweens/tween/BaseTween.js#L438
Since: 3.60.0
destroy ​
<instance> destroy() ​
Description:
Handles the destroy process of this Tween, clearing out the
Tween Data and resetting the targets. A Tween that has been
destroyed cannot ever be played or used again.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/tweens/tween/BaseTween.js#L851
Since: 3.60.0
getTimeScale ​
<instance> getTimeScale() ​
Description:
Gets the value of the time scale applied to this Tween. A value of 1 runs in real-time.
A value of 0.5 runs 50% slower, and so on.
Returns: number - The value of the time scale applied to this Tween.
Source: src/tweens/tween/BaseTween.js#L285
Since: 3.60.0
isActive ​
<instance> isActive() ​
Description:
Returns true if this Tween has a current state of ACTIVE, otherwise false .
Returns: boolean - true if this Tween has a current state of ACTIVE, otherwise false .
Source: src/tweens/tween/BaseTween.js#L747
Since: 3.60.0
isCompleteDelayed ​
<instance> isCompleteDelayed() ​
Description:
Returns true if this Tween has a current state of COMPLETE_DELAY, otherwise false .
Returns: boolean - true if this Tween has a current state of COMPLETE_DELAY, otherwise false .
Source: src/tweens/tween/BaseTween.js#L773
Since: 3.60.0
isDestroyed ​
<instance> isDestroyed() ​
Description:
Returns true if this Tween has a current state of DESTROYED, otherwise false .
Returns: boolean - true if this Tween has a current state of DESTROYED, otherwise false .
Source: src/tweens/tween/BaseTween.js#L838
Since: 3.60.0
isFinished ​
<instance> isFinished() ​
Description:
Returns true if this Tween has a current state of FINISHED, otherwise false .
Returns: boolean - true if this Tween has a current state of FINISHED, otherwise false .
Source: src/tweens/tween/BaseTween.js#L825
Since: 3.60.0
isLoopDelayed ​
<instance> isLoopDelayed() ​
Description:
Returns true if this Tween has a current state of LOOP_DELAY, otherwise false .
Returns: boolean - true if this Tween has a current state of LOOP_DELAY, otherwise false .
Source: src/tweens/tween/BaseTween.js#L760
Since: 3.60.0
isPaused ​
<instance> isPaused() ​
Description:
Checks if the Tween is currently paused.
This is the same as inspecting the BaseTween.paused property directly.
Returns: boolean - true if the Tween is paused, otherwise false .
Source: src/tweens/tween/BaseTween.js#L314
Since: 3.60.0
isPending ​
<instance> isPending() ​
Description:
Returns true if this Tween has a current state of PENDING, otherwise false .
Returns: boolean - true if this Tween has a current state of PENDING, otherwise false .
Source: src/tweens/tween/BaseTween.js#L734
Since: 3.60.0
isPendingRemove ​
<instance> isPendingRemove() ​
Description:
Returns true if this Tween has a current state of PENDING_REMOVE, otherwise false .
Returns: boolean - true if this Tween has a current state of PENDING_REMOVE, otherwise false .
Source: src/tweens/tween/BaseTween.js#L799
Since: 3.60.0
isPlaying ​
<instance> isPlaying() ​
Description:
Checks if this Tween is currently playing.
If this Tween is paused, or not active, this method will return false.
Returns: boolean - true if the Tween is playing, otherwise false .
Source: src/tweens/tween/BaseTween.js#L299
Since: 3.60.0
isRemoved ​
<instance> isRemoved() ​
Description:
Returns true if this Tween has a current state of REMOVED, otherwise false .
Returns: boolean - true if this Tween has a current state of REMOVED, otherwise false .
Source: src/tweens/tween/BaseTween.js#L812
Since: 3.60.0
isStartDelayed ​
<instance> isStartDelayed() ​
Description:
Returns true if this Tween has a current state of START_DELAY, otherwise false .
Returns: boolean - true if this Tween has a current state of START_DELAY, otherwise false .
Source: src/tweens/tween/BaseTween.js#L786
Since: 3.60.0
makeActive ​
<instance> makeActive() ​
Description:
Internal method that makes this Tween active within the TweenManager
and emits the onActive event and callback.
Fires: Phaser.Tweens.Events#event:TWEEN_ACTIVE
Source: src/tweens/tween/BaseTween.js#L375
Since: 3.60.0
onCompleteHandler ​
<instance> onCompleteHandler() ​
Description:
Internal method that handles this tween completing and emitting the onComplete event
and callback.
Source: src/tweens/tween/BaseTween.js#L390
Since: 3.60.0
pause ​
<instance> pause() ​
Description:
Pauses the Tween immediately. Use resume to continue playback.
You can also toggle the Tween.paused boolean property, but doing so will not trigger the PAUSE event.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Fires: Phaser.Tweens.Events#event:TWEEN_PAUSE
Source: src/tweens/tween/BaseTween.js#L329
Since: 3.60.0
remove ​
<instance> remove() ​
Description:
Immediately removes this Tween from the TweenManager and all of its internal arrays,
no matter what stage it is at. Then sets the tween state to REMOVED .
You should dispose of your reference to this tween after calling this method, to
free it from memory. If you no longer require it, call Tween.destroy() on it.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Source: src/tweens/tween/BaseTween.js#L466
Since: 3.60.0
resume ​
<instance> resume() ​
Description:
Resumes the playback of a previously paused Tween.
You can also toggle the Tween.paused boolean property, but doing so will not trigger the RESUME event.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Fires: Phaser.Tweens.Events#event:TWEEN_RESUME
Source: src/tweens/tween/BaseTween.js#L352
Since: 3.60.0
setActiveState ​
<instance> setActiveState() ​
Description:
Sets this Tween state to ACTIVE.
Source: src/tweens/tween/BaseTween.js#L640
Since: 3.60.0
setCallback ​
<instance> setCallback(type, callback, [params]) ​
Description:
Sets an event based callback to be invoked during playback.
Calling this method will replace a previously set callback for the given type, if any exists.
The types available are:
onActive - When the Tween is first created it moves to an 'active' state when added to the Tween Manager. 'Active' does not mean 'playing'.
onStart - When the Tween starts playing after a delayed or paused state. This will happen at the same time as onActive if the tween has no delay and isn't paused.
onLoop - When a Tween loops, if it has been set to do so. This happens after the loopDelay expires, if set.
onComplete - When the Tween finishes playback fully. Never invoked if the Tween is set to repeat infinitely.
onStop - Invoked only if the Tween.stop method is called.
onPause - Invoked only if the Tween.pause method is called. Not invoked if the Tween Manager is paused.
onResume - Invoked only if the Tween.resume method is called. Not invoked if the Tween Manager is resumed.
The following types are also available and are invoked on a TweenData level - that is per-object, per-property, being tweened.
onYoyo - When a TweenData starts a yoyo. This happens after the hold delay expires, if set.
onRepeat - When a TweenData repeats playback. This happens after the repeatDelay expires, if set.
onUpdate - When a TweenData updates a property on a source target during playback.
Parameters:
name type optional description
type Phaser.Types.Tweens.TweenCallbackTypes No The type of callback to set. One of: onActive , onComplete , onLoop , onPause , onRepeat , onResume , onStart , onStop , onUpdate or onYoyo .
callback function No Your callback that will be invoked.
params array Yes The parameters to pass to the callback. Pass an empty array if you don't want to define any, but do wish to set the scope.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Source: src/tweens/tween/BaseTween.js#L587
Since: 3.60.0
setCompleteDelayState ​
<instance> setCompleteDelayState() ​
Description:
Sets this Tween state to COMPLETE_DELAY.
Source: src/tweens/tween/BaseTween.js#L664
Since: 3.60.0
setDestroyedState ​
<instance> setDestroyedState() ​
Description:
Sets this Tween state to DESTROYED.
Source: src/tweens/tween/BaseTween.js#L723
Since: 3.60.0
setFinishedState ​
<instance> setFinishedState() ​
Description:
Sets this Tween state to FINISHED.
Source: src/tweens/tween/BaseTween.js#L712
Since: 3.60.0
setLoopDelayState ​
<instance> setLoopDelayState() ​
Description:
Sets this Tween state to LOOP_DELAY.
Source: src/tweens/tween/BaseTween.js#L653
Since: 3.60.0
setPendingRemoveState ​
<instance> setPendingRemoveState() ​
Description:
Sets this Tween state to PENDING_REMOVE.
Source: src/tweens/tween/BaseTween.js#L690
Since: 3.60.0
setPendingState ​
<instance> setPendingState() ​
Description:
Sets this Tween state to PENDING.
Source: src/tweens/tween/BaseTween.js#L629
Since: 3.60.0
setRemovedState ​
<instance> setRemovedState() ​
Description:
Sets this Tween state to REMOVED.
Source: src/tweens/tween/BaseTween.js#L701
Since: 3.60.0
setStartDelayState ​
<instance> setStartDelayState() ​
Description:
Sets this Tween state to START_DELAY.
Source: src/tweens/tween/BaseTween.js#L675
Since: 3.60.0
setTimeScale ​
<instance> setTimeScale(value) ​
Description:
Sets the value of the time scale applied to this Tween. A value of 1 runs in real-time.
A value of 0.5 runs 50% slower, and so on.
The value isn't used when calculating total duration of the tween, it's a run-time delta adjustment only.
This value is multiplied by the TweenManager.timeScale .
Parameters:
name type optional description
value number No The time scale value to set.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Source: src/tweens/tween/BaseTween.js#L263
Since: 3.60.0
stop ​
<instance> stop() ​
Description:
Stops the Tween immediately, whatever stage of progress it is at.
If not a part of a Tween Chain it is also flagged for removal by the Tween Manager.
If an onStop callback has been defined it will automatically invoke it.
The Tween will be removed during the next game frame, but should be considered 'destroyed' from this point on.
Typically, you cannot play a Tween that has been stopped. If you just wish to pause the tween, not destroy it,
then call the pause method instead and use resume to continue playback. If you wish to restart the Tween,
use the restart or seek methods.
Returns: Phaser.Tweens.BaseTween - This Tween instance.
Fires: Phaser.Tweens.Events#event:TWEEN_STOP
Source: src/tweens/tween/BaseTween.js#L488
Since: 3.60.0
updateCompleteDelay ​
<instance> updateCompleteDelay(delta) ​
Description:
Internal method that handles the processing of the complete delay countdown timer and
the dispatch of related events. Called automatically by Tween.update .
Parameters:
name type optional description
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/tweens/tween/BaseTween.js#L568
Since: 3.60.0
updateLoopCountdown ​
<instance> updateLoopCountdown(delta) ​
Description:
Internal method that handles the processing of the loop delay countdown timer and
the dispatch of related events. Called automatically by Tween.update .
Parameters:
name type optional description
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/tweens/tween/BaseTween.js#L519
Since: 3.60.0
updateStartCountdown ​
<instance> updateStartCountdown(delta) ​
Description:
Internal method that handles the processing of the start delay countdown timer and
the dispatch of related events. Called automatically by Tween.update .
Parameters:
name type optional description
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/tweens/tween/BaseTween.js#L540
Since: 3.60.0
Previous
TimerEvent
Next
BaseTweenData
Public Members
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
Inherited Methods
Public Methods
complete
completeAfterLoop
destroy
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
onCompleteHandler
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
