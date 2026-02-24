# TweenFrameData | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tweens-tweenframedata

Phaser API Documentation
Class
TweenFrameData
Version: Phaser v3.90.0
On this page
TweenFrameData
The TweenFrameData is a class that contains a single target that will change the texture frame
at the conclusion of the Tween.
TweenFrameData instances are typically created by the TweenBuilder automatically, when it
detects the presence of a 'texture' property as the key being tweened.
A Tween can own multiple TweenFrameData instances, but a TweenFrameData only
ever belongs to a single Tween.
You should not typically create these yourself, but rather use the TweenBuilder,
or the Tween.addFrame method.
Constructor
new TweenFrameData(tween, targetIndex, texture, frame, delay, duration, hold, repeat, repeatDelay, flipX, flipY)
Parameters
name type optional description
tween Phaser.Tweens.Tween No The tween this TweenData instance belongs to.
targetIndex number No The target index within the Tween targets array.
texture string No The texture key to set at the end of this tween.
frame string | number No The texture frame to set at the end of this tween.
delay function No Function that returns the time in milliseconds before tween will start.
duration number No The duration of the tween in milliseconds.
hold number No Function that returns the time in milliseconds the tween will pause before repeating or returning to its starting value if yoyo is set to true.
repeat number No Function that returns the number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice.
repeatDelay number No Function that returns the time in milliseconds before the repeat will start.
flipX boolean No Should toggleFlipX be called when yoyo or repeat happens?
flipY boolean No Should toggleFlipY be called when yoyo or repeat happens?
Scope : static
Extends
Phaser.Tweens.BaseTweenData
Source: src/tweens/tween/TweenFrameData.js#L12
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
Public Members ​
endFrame ​
endFrame: string, number ​
Description:
The frame to be set at the end of the tween.
Source: src/tweens/tween/TweenFrameData.js#L93
Since: 3.60.0
endTexture ​
endTexture: string ​
Description:
The texture to be set at the end of the tween.
Source: src/tweens/tween/TweenFrameData.js#L75
Since: 3.60.0
key ​
key: string ​
Description:
The property of the target to be tweened.
Always 'texture' for a TweenFrameData object.
Source: src/tweens/tween/TweenFrameData.js#L54
Since: 3.60.0
startFrame ​
startFrame: string, number ​
Description:
The frame to be set at the start of the tween.
Source: src/tweens/tween/TweenFrameData.js#L84
Since: 3.60.0
startTexture ​
startTexture: string ​
Description:
The texture to be set at the start of the tween.
Source: src/tweens/tween/TweenFrameData.js#L66
Since: 3.60.0
yoyo ​
yoyo: boolean ​
Description:
Will the Tween ease back to its starting values, after reaching the end
and any hold value that may be set?
Overrides: Phaser.Tweens.BaseTweenData#yoyo
Source: src/tweens/tween/TweenFrameData.js#L102
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
Source: src/tweens/tween/TweenFrameData.js#L298
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
Source: src/tweens/tween/TweenFrameData.js#L268
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
Source: src/tweens/tween/TweenFrameData.js#L113
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
Source: src/tweens/tween/TweenFrameData.js#L141
Since: 3.60.0
Previous
TweenData
Next
TweenManager
Inherited Members
Public Members
endFrame
endTexture
key
startFrame
startTexture
yoyo
Inherited Methods
Public Methods
destroy
dispatchEvent
reset
update
