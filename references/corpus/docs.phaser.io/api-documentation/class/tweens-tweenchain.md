# TweenChain | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tweens-tweenchain

Phaser API Documentation
Class
TweenChain
Version: Phaser v3.90.0
On this page
TweenChain
A TweenChain is a special type of Tween that allows you to create a sequence of Tweens, chained to one-another,
and add them to the Tween Manager.
The tweens are played in order, from start to finish. You can optionally set the chain
to repeat as many times as you like. Once the chain has finished playing, or repeating if set,
all tweens in the chain will be destroyed automatically. To override this, set the 'persist'
argument to 'true'.
Playback will start immediately unless the first Tween has been configured to be paused.
Please note that Tweens will not manipulate any target property that begins with an underscore.
Constructor
new TweenChain(parent)
Parameters
name type optional description
parent Phaser.Tweens.TweenManager | Phaser.Tweens.TweenChain No A reference to the Tween Manager, or TweenChain, that owns this TweenChain.
Scope : static
Extends
Phaser.Tweens.BaseTween
Source: src/tweens/tween/TweenChain.js#L15
Since: 3.60.0
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
currentIndex ​
currentIndex: number ​
Description:
A reference to the data array index of the currently playing tween.
Source: src/tweens/tween/TweenChain.js#L56
Since: 3.60.0
currentTween ​
currentTween: Phaser.Tweens.Tween ​
Description:
A reference to the Tween that this TweenChain is currently playing.
Source: src/tweens/tween/TweenChain.js#L47
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
onCompleteHandler
pause
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
From Phaser.Tweens.TweenChain :
makeActive
remove
Public Methods ​
add ​
<instance> add(tweens) ​
Description:
Create a sequence of Tweens, chained to one-another, and add them to this Tween Manager.
The tweens are played in order, from start to finish. You can optionally set the chain
to repeat as many times as you like. Once the chain has finished playing, or repeating if set,
all tweens in the chain will be destroyed automatically. To override this, set the 'persist'
argument to 'true'.
Playback will start immediately unless the first Tween has been configured to be paused.
Please note that Tweens will not manipulate any target property that begins with an underscore.
Parameters:
name type optional description
tweens Array.< Phaser.Types.Tweens.TweenBuilderConfig > | Array.<object> No An array of Tween configuration objects for the Tweens in this chain.
Returns: Phaser.Tweens.TweenChain - This TweenChain instance.
Source: src/tweens/tween/TweenChain.js#L95
Since: 3.60.0
destroy ​
<instance> destroy() ​
Description:
Immediately destroys this TweenChain, nulling of all its references.
Overrides: Phaser.Tweens.BaseTween#destroy
Source: src/tweens/tween/TweenChain.js#L534
Since: 3.60.0
dispatchEvent ​
<instance> dispatchEvent(event, [callback]) ​
Description:
Internal method that will emit a TweenChain based Event and invoke the given callback.
Parameters:
name type optional description
event Phaser.Types.Tweens.Event No The Event to be dispatched.
callback Phaser.Types.Tweens.TweenCallbackTypes Yes The name of the callback to be invoked. Can be null or undefined to skip invocation.
Source: src/tweens/tween/TweenChain.js#L513
Since: 3.60.0
hasTarget ​
<instance> hasTarget(target) ​
Description:
See if any of the tweens in this Tween Chain is currently acting upon the given target.
Parameters:
name type optional description
target object No The target to check against this TweenChain.
Returns: boolean - true if the given target is a target of this TweenChain, otherwise false .
Source: src/tweens/tween/TweenChain.js#L172
Since: 3.60.0
init ​
<instance> init() ​
Description:
Prepares this TweenChain for playback.
Called automatically by the TweenManager. Should not be called directly.
Returns: Phaser.Tweens.TweenChain - This TweenChain instance.
Fires: Phaser.Tweens.Events#event:TWEEN_ACTIVE
Source: src/tweens/tween/TweenChain.js#L66
Since: 3.60.0
makeActive ​
<instance> makeActive(tween) ​
Description:
Re-initialises the given Tween and sets it to the Active state.
Parameters:
name type optional description
tween Phaser.Tweens.Tween No The Tween to check.
Returns: Phaser.Tweens.TweenChain - This TweenChain instance.
Source: src/tweens/tween/TweenChain.js#L251
Since: 3.60.0
nextState ​
<instance> nextState() ​
Description:
Internal method that advances to the next state of the TweenChain playback.
Returns: boolean - true if this TweenChain has completed, otherwise false .
Fires: Phaser.Tweens.Events#event:TWEEN_COMPLETE , Phaser.Tweens.Events#event:TWEEN_LOOP
Source: src/tweens/tween/TweenChain.js#L271
Since: 3.60.0
nextTween ​
<instance> nextTween() ​
Description:
Immediately advances to the next Tween in the chain.
This is typically called internally, but can be used if you need to
advance playback for some reason.
Returns: boolean - true if there are no more Tweens in the chain, otherwise false .
Source: src/tweens/tween/TweenChain.js#L468
Since: 3.60.0
play ​
<instance> play() ​
Description:
Starts this TweenChain playing.
You only need to call this method if you have configured this TweenChain to be paused on creation.
If the TweenChain is already playing, calling this method again will have no effect. If you wish to
restart the chain, use TweenChain.restart instead.
Calling this method after the TweenChain has completed will start the chain playing again from the beginning.
Returns: Phaser.Tweens.TweenChain - This TweenChain instance.
Source: src/tweens/tween/TweenChain.js#L318
Since: 3.60.0
remove ​
<instance> remove(tween) ​
Description:
Removes the given Tween from this Tween Chain.
The removed tween is not destroyed. It is just removed from this Tween Chain.
If the given Tween is currently playing then the chain will automatically move
to the next tween in the chain. If there are no more tweens, this chain will complete.
Parameters:
name type optional description
tween Phaser.Tweens.Tween No The Tween to be removed.
Returns: Phaser.Tweens.TweenChain - This Tween Chain instance.
Source: src/tweens/tween/TweenChain.js#L139
Since: 3.60.0
reset ​
<instance> reset(tween) ​
Description:
Resets the given Tween.
It will seek to position 0 and playback will start on the next frame.
Parameters:
name type optional description
tween Phaser.Tweens.Tween No The Tween to be reset.
Returns: Phaser.Tweens.TweenChain - This TweenChain instance.
Source: src/tweens/tween/TweenChain.js#L230
Since: 3.60.0
resetTweens ​
<instance> resetTweens() ​
Description:
Internal method that resets all of the Tweens and the current index pointer.
Source: src/tweens/tween/TweenChain.js#L361
Since: 3.60.0
restart ​
<instance> restart() ​
Description:
Restarts the TweenChain from the beginning.
If this TweenChain was configured to have a loop, or start delay, those
are reset to their initial values as well. It will also dispatch the
onActive callback and event again.
Returns: Phaser.Tweens.TweenChain - This TweenChain instance.
Source: src/tweens/tween/TweenChain.js#L197
Since: 3.60.0
setCurrentTween ​
<instance> setCurrentTween(index) ​
Description:
Sets the current active Tween to the given index, based on its
entry in the TweenChain data array.
Parameters:
name type optional description
index number No The index of the Tween to be made current.
Source: src/tweens/tween/TweenChain.js#L495
Since: 3.60.0
update ​
<instance> update(delta) ​
Description:
Internal method that advances the TweenChain based on the time values.
Parameters:
name type optional description
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Returns: boolean - Returns true if this TweenChain has finished and should be removed from the Tween Manager, otherwise returns false .
Fires: Phaser.Tweens.Events#event:TWEEN_COMPLETE , Phaser.Tweens.Events#event:TWEEN_LOOP , Phaser.Tweens.Events#event:TWEEN_START
Source: src/tweens/tween/TweenChain.js#L380
Since: 3.60.0
Previous
Tween
Next
TweenData
Inherited Members
Public Members
currentIndex
currentTween
Inherited Methods
Public Methods
add
destroy
dispatchEvent
hasTarget
init
makeActive
nextState
nextTween
play
remove
reset
resetTweens
restart
setCurrentTween
update
