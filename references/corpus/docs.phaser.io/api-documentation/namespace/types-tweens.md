# Phaser.Types.Tweens | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/types-tweens

Phaser API Documentation
Namespaces
Phaser.Types.Tweens
Version: Phaser v3.90.0
On this page
Phaser.Types.Tweens
Scope: static
Source: src/tweens/typedefs/index.js#L7
Static functions ​
Event ​
Event ​
Description:
A Tween Event.
Source: src/tweens/typedefs/Event.js#L1
Since: 3.19.0
GetActiveCallback ​
GetActiveCallback ​
Parameters:
name type optional description
target any No The tween target.
key string No The target property.
value number No The current value of the target property.
targetIndex number No The index of the target within the Tween.
totalTargets number No The total number of targets in this Tween.
tween Phaser.Tweens.Tween No The Tween that invoked this callback.
Returns: number - - The new value.
Source: src/tweens/typedefs/GetActiveCallback.js#L1
Since: 3.19.0
GetEndCallback ​
GetEndCallback ​
Parameters:
name type optional description
target any No The tween target.
key string No The target property.
value number No The current value of the target property.
targetIndex number No The index of the target within the Tween.
totalTargets number No The total number of targets in this Tween.
tween Phaser.Tweens.Tween No The Tween that invoked this callback.
Returns: number - - The new value.
Source: src/tweens/typedefs/GetEndCallback.js#L1
Since: 3.18.0
GetStartCallback ​
GetStartCallback ​
Parameters:
name type optional description
target any No The tween target.
key string No The target property.
value number No The current value of the target property.
targetIndex number No The index of the target within the Tween.
totalTargets number No The total number of targets in this Tween.
tween Phaser.Tweens.Tween No The Tween that invoked this callback.
Returns: number - - The new value.
Source: src/tweens/typedefs/GetStartCallback.js#L1
Since: 3.18.0
NumberTweenBuilderConfig ​
NumberTweenBuilderConfig ​
Source: src/tweens/typedefs/NumberTweenBuilderConfig.js#L1
Since: 3.18.0
StaggerConfig ​
StaggerConfig ​
Source: src/tweens/typedefs/StaggerConfig.js#L1
Since: 3.19.0
TweenBuilderConfig ​
TweenBuilderConfig ​
Source: src/tweens/typedefs/TweenBuilderConfig.js#L1
Since: 3.18.0
TweenCallbacks ​
TweenCallbacks ​
Source: src/tweens/typedefs/TweenCallbacks.js#L1
Since: 3.60.0
TweenCallbackTypes ​
TweenCallbackTypes ​
Source: src/tweens/typedefs/TweenCallbackTypes.js#L1
Since: 3.60.0
TweenChainBuilderConfig ​
TweenChainBuilderConfig ​
Source: src/tweens/typedefs/TweenChainBuilderConfig.js#L1
Since: 3.60.0
TweenConfigDefaults ​
TweenConfigDefaults ​
Source: src/tweens/tween/Defaults.js#L7
Since: 3.0.0
TweenDataConfig ​
TweenDataConfig ​
Source: src/tweens/typedefs/TweenDataConfig.js#L1
Since: 3.0.0
TweenDataGenConfig ​
TweenDataGenConfig ​
Source: src/tweens/typedefs/TweenDataGenConfig.js#L1
Since: 3.0.0
TweenFrameDataConfig ​
TweenFrameDataConfig ​
Source: src/tweens/typedefs/TweenFrameDataConfig.js#L1
Since: 3.60.0
TweenOnActiveCallback ​
TweenOnActiveCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
targets any | Array.<any> No The targets of the Tween. If this Tween has multiple targets this will be an array of the targets.
param any No Any value passed in onActiveParams .
Source: src/tweens/typedefs/TweenOnActiveCallback.js#L1
Since: 3.19.0
TweenOnCompleteCallback ​
TweenOnCompleteCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
targets any | Array.<any> No The targets of the Tween. If this Tween has multiple targets this will be an array of the targets.
param any No Any value passed in onCompleteParams .
Source: src/tweens/typedefs/TweenOnCompleteCallback.js#L1
Since: 3.18.0
TweenOnLoopCallback ​
TweenOnLoopCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
targets any | Array.<any> No The targets of the Tween. If this Tween has multiple targets this will be an array of the targets.
param any No Any value passed in onLoopParams .
Source: src/tweens/typedefs/TweenOnLoopCallback.js#L1
Since: 3.18.0
TweenOnPauseCallback ​
TweenOnPauseCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
targets any | Array.<any> No The targets of the Tween. If this Tween has multiple targets this will be an array of the targets.
param any No Any value passed in onPauseParams .
Source: src/tweens/typedefs/TweenOnPauseCallback.js#L1
Since: 3.60.0
TweenOnRepeatCallback ​
TweenOnRepeatCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
target any No The current target of the Tween. If this Tween has multiple targets, this will be a reference to just the single one being updated prior to this callback.
key string No The property that is being updated on the target.
current number No The current value of the property being set on the target.
previous number No The previous value of the property being set on the target.
param any No Any value passed in onRepeatParams .
Source: src/tweens/typedefs/TweenOnRepeatCallback.js#L1
Since: 3.18.0
TweenOnResumeCallback ​
TweenOnResumeCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
targets any | Array.<any> No The targets of the Tween. If this Tween has multiple targets this will be an array of the targets.
param any No Any value passed in onPauseParams .
Source: src/tweens/typedefs/TweenOnResumeCallback.js#L1
Since: 3.60.0
TweenOnStartCallback ​
TweenOnStartCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
targets any | Array.<any> No The targets of the Tween. If this Tween has multiple targets this will be an array of the targets.
param any No Any value passed in onStartParams .
Source: src/tweens/typedefs/TweenOnStartCallback.js#L1
Since: 3.18.0
TweenOnStopCallback ​
TweenOnStopCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
targets any | Array.<any> No The targets of the Tween. If this Tween has multiple targets this will be an array of the targets.
param any No Any value passed in onStopParams .
Source: src/tweens/typedefs/TweenOnStopCallback.js#L1
Since: 3.24.0
TweenOnUpdateCallback ​
TweenOnUpdateCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
target any No The current target of the Tween. If this Tween has multiple targets, this will be a reference to just the single one being updated prior to this callback.
key string No The property that is being updated on the target.
current number No The current value of the property being set on the target.
previous number No The previous value of the property being set on the target.
param any No Any value passed in onUpdateParams .
Source: src/tweens/typedefs/TweenOnUpdateCallback.js#L1
Since: 3.18.0
TweenOnYoyoCallback ​
TweenOnYoyoCallback ​
Parameters:
name type optional description
tween Phaser.Tweens.Tween No A reference to the Tween.
target any No The current target of the Tween. If this Tween has multiple targets, this will be a reference to just the single one being updated prior to this callback.
key string No The property that is being updated on the target.
current number No The current value of the property being set on the target.
previous number No The previous value of the property being set on the target.
param any No Any value passed in onYoyoParams .
Source: src/tweens/typedefs/TweenOnYoyoCallback.js#L1
Since: 3.18.0
TweenPropConfig ​
TweenPropConfig ​
Source: src/tweens/typedefs/TweenPropConfig.js#L1
Since: 3.18.0
Previous
Phaser.Types.Time
Next
Phaser.Types
Static functions
Event
GetActiveCallback
GetEndCallback
GetStartCallback
NumberTweenBuilderConfig
StaggerConfig
TweenBuilderConfig
TweenCallbacks
TweenCallbackTypes
TweenChainBuilderConfig
TweenConfigDefaults
TweenDataConfig
TweenDataGenConfig
TweenFrameDataConfig
TweenOnActiveCallback
TweenOnCompleteCallback
TweenOnLoopCallback
TweenOnPauseCallback
TweenOnRepeatCallback
TweenOnResumeCallback
TweenOnStartCallback
TweenOnStopCallback
TweenOnUpdateCallback
TweenOnYoyoCallback
TweenPropConfig
