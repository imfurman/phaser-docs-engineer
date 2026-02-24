# TweenData | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tweens-tweendata

Phaser API Documentation
Class
TweenData
Version: Phaser v3.90.0
On this page
TweenData
The TweenData is a class that contains a single target and property that is being tweened.
Tweens create TweenData instances when they are created, with one TweenData instance per
target, per property. A Tween can own multiple TweenData instances, but a TweenData only
ever belongs to a single Tween.
You should not typically create these yourself, but rather use the TweenBuilder,
or the Tween.add method.
Prior to Phaser 3.60 the TweenData was just an object, but was refactored to a class,
to make it responsible for its own state and updating.
Constructor
new TweenData(tween, targetIndex, key, getEnd, getStart, getActive, ease, delay, duration, yoyo, hold, repeat, repeatDelay, flipX, flipY, interpolation, interpolationData)
Parameters
name type optional description
tween Phaser.Tweens.Tween No The tween this TweenData instance belongs to.
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
Scope : static
Extends
Phaser.Tweens.BaseTweenData
Source: src/tweens/tween/TweenData.js#L12
Since: 3.60.0
Inherited Members ​
From Phaser.Tweens.BaseTweenData :
delay
duration
elapsed
flipX
flipY
getDelay
hold
isCountdown
progress
repeat
repeatCounter
repeatDelay
state
targetIndex
totalDuration
tween
yoyo
Public Members ​
current ​
current: number ​
Description:
The targets current value, as recorded in the most recent step.
Source: src/tweens/tween/TweenData.js#L135
Since: 3.60.0
ease ​
ease: function ​
Description:
The ease function this Tween uses to calculate the target value.
Source: src/tweens/tween/TweenData.js#L108
Since: 3.60.0
end ​
end: number ​
Description:
The targets ending value, as returned by getEndValue .
Source: src/tweens/tween/TweenData.js#L144
Since: 3.60.0
getActiveValue ​
getActiveValue: Phaser.Types.Tweens.GetActiveCallback ​
Description:
A function that returns what to set the target property to,
the moment the TweenData is invoked.
This is called when this TweenData is initialised or reset.
Source: src/tweens/tween/TweenData.js#L70
Since: 3.60.0
getEndValue ​
getEndValue: Phaser.Types.Tweens.GetEndCallback ​
Description:
A function that returns what to set the target property to
at the end of the tween.
This is called when the tween starts playing, after any initial
start delay, or if the tween is reset, or is set to repeat.
Source: src/tweens/tween/TweenData.js#L82
Since: 3.60.0
getStartValue ​
getStartValue: Phaser.Types.Tweens.GetStartCallback ​
Description:
A function that returns what to set the target property to
at the start of the tween.
This is called when the tween starts playing, after any initial
start delay, or if the tween is reset, or is set to repeat.
Source: src/tweens/tween/TweenData.js#L95
Since: 3.60.0
interpolation ​
interpolation: function ​
Description:
The interpolation function to be used for arrays of data.
Source: src/tweens/tween/TweenData.js#L153
Since: 3.60.0
interpolationData ​
interpolationData: Array.<number> ​
Description:
The array of data to interpolate, if interpolation is being used.
Source: src/tweens/tween/TweenData.js#L163
Since: 3.60.0
key ​
key: string ​
Description:
The property of the target to be tweened.
Source: src/tweens/tween/TweenData.js#L60
Since: 3.60.0
previous ​
previous: number ​
Description:
The target value from the previous step.
Source: src/tweens/tween/TweenData.js#L126
Since: 3.60.0
start ​
start: number ​
Description:
The targets starting value, as returned by getStartValue .
Source: src/tweens/tween/TweenData.js#L117
Since: 3.60.0
Inherited Methods ​
From Phaser.Tweens.BaseTweenData :
getTarget
isComplete
isCreated
isDelayed
isHolding
isPendingRender
isPlayingBackward
isPlayingForward
isRepeating
onRepeat
setCompleteState
setCreatedState
setDelayState
setHoldState
setPendingRenderState
setPlayingBackwardState
setPlayingForwardState
setRepeatState
setStateFromEnd
setStateFromStart
setTargetValue
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Immediately destroys this TweenData, nulling of all its references.
Overrides: Phaser.Tweens.BaseTweenData#destroy
Source: src/tweens/tween/TweenData.js#L399
Since: 3.60.0
dispatchEvent ​
<instance> dispatchEvent(event, [callback]) ​
Description:
Internal method that will emit a TweenData based Event on the
parent Tween and also invoke the given callback, if provided.
Parameters:
name type optional description
event Phaser.Types.Tweens.Event No The Event to be dispatched.
callback Phaser.Types.Tweens.TweenCallbackTypes Yes The name of the callback to be invoked. Can be null or undefined to skip invocation.
Source: src/tweens/tween/TweenData.js#L366
Since: 3.60.0
reset ​
<instance> reset([isSeeking]) ​
Description:
Internal method that resets this Tween Data entirely, including the progress and elapsed values.
Called automatically by the parent Tween. Should not be called directly.
Parameters:
name type optional default description
isSeeking boolean Yes false Is the Tween Data being reset as part of a Tween seek?
Overrides: Phaser.Tweens.BaseTweenData#reset
Source: src/tweens/tween/TweenData.js#L173
Since: 3.60.0
update ​
<instance> update(delta) ​
Description:
Internal method that advances this TweenData based on the delta value given.
Parameters:
name type optional description
delta number No The elapsed delta time in ms.
Returns: boolean - true if this TweenData is still playing, or false if it has finished entirely.
Fires: Phaser.Tweens.Events#event:TWEEN_UPDATE , Phaser.Tweens.Events#event:TWEEN_REPEAT
Source: src/tweens/tween/TweenData.js#L206
Since: 3.60.0
Previous
TweenChain
Next
TweenFrameData
Inherited Members
Public Members
current
ease
end
getActiveValue
getEndValue
getStartValue
interpolation
interpolationData
key
previous
start
Inherited Methods
Public Methods
destroy
dispatchEvent
reset
update
