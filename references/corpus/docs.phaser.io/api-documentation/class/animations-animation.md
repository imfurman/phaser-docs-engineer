# Animation | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/animations-animation

Phaser API Documentation
Class
Animation
Version: Phaser v3.90.0
On this page
Animation
A Frame based Animation.
Animations in Phaser consist of a sequence of AnimationFrame objects, which are managed by
this class, along with properties that impact playback, such as the animations frame rate
or delay.
This class contains all of the properties and methods needed to handle playback of the animation
directly to an AnimationState instance, which is owned by a Sprite, or similar Game Object.
You don't typically create an instance of this class directly, but instead go via
either the AnimationManager or the AnimationState and use their create methods,
depending on if you need a global animation, or local to a specific Sprite.
Constructor
new Animation(manager, key, config)
Parameters
name type optional description
manager Phaser.Animations.AnimationManager No A reference to the global Animation Manager
key string No The unique identifying string for this animation.
config Phaser.Types.Animations.Animation No The Animation configuration.
Scope : static
Source: src/animations/Animation.js#L15
Since: 3.0.0
Public Members ​
delay ​
delay: number ​
Description:
The delay in ms before the playback will begin.
Source: src/animations/Animation.js#L127
Since: 3.0.0
duration ​
duration: number ​
Description:
How long the animation should play for, in milliseconds.
If the frameRate property has been set then it overrides this value,
otherwise the frameRate is derived from duration .
Source: src/animations/Animation.js#L97
Since: 3.0.0
frameRate ​
frameRate: number ​
Description:
The frame rate of playback in frames per second (default 24 if duration is null)
Source: src/animations/Animation.js#L87
Since: 3.0.0
frames ​
frames: Array.< Phaser.Animations.AnimationFrame > ​
Description:
Extract all the frame data into the frames array.
Source: src/animations/Animation.js#L73
Since: 3.0.0
hideOnComplete ​
hideOnComplete: boolean ​
Description:
Should the GameObject's visible property be set to false when the animation finishes?
Source: src/animations/Animation.js#L190
Since: 3.0.0
key ​
key: string ​
Description:
The unique identifying string for this animation.
Source: src/animations/Animation.js#L54
Since: 3.0.0
manager ​
manager: Phaser.Animations.AnimationManager ​
Description:
A reference to the global Animation Manager.
Source: src/animations/Animation.js#L45
Since: 3.0.0
msPerFrame ​
msPerFrame: number ​
Description:
How many ms per frame, not including frame specific modifiers.
Source: src/animations/Animation.js#L108
Since: 3.0.0
paused ​
paused: boolean ​
Description:
Global pause. All Game Objects using this Animation instance are impacted by this property.
Source: src/animations/Animation.js#L210
Since: 3.0.0
randomFrame ​
randomFrame: boolean ​
Description:
Start playback of this animation from a random frame?
Source: src/animations/Animation.js#L200
Since: 3.60.0
repeat ​
repeat: number ​
Description:
Number of times to repeat the animation. Set to -1 to repeat forever.
Source: src/animations/Animation.js#L137
Since: 3.0.0
repeatDelay ​
repeatDelay: number ​
Description:
The delay in ms before the a repeat play starts.
Source: src/animations/Animation.js#L147
Since: 3.0.0
showBeforeDelay ​
showBeforeDelay: boolean ​
Description:
If the animation has a delay set, before playback will begin, this
controls when the first frame is set on the Sprite. If this property
is 'false' then the frame is set only after the delay has expired.
This is the default behavior.
Source: src/animations/Animation.js#L167
Since: 3.60.0
showOnStart ​
showOnStart: boolean ​
Description:
Should the GameObject's visible property be set to true when the animation starts to play?
Source: src/animations/Animation.js#L180
Since: 3.0.0
skipMissedFrames ​
skipMissedFrames: boolean ​
Description:
Skip frames if the time lags, or always advanced anyway?
Source: src/animations/Animation.js#L117
Since: 3.0.0
type ​
type: string ​
Description:
A frame based animation (as opposed to a bone based animation)
Source: src/animations/Animation.js#L63
Since: 3.0.0
yoyo ​
yoyo: boolean ​
Description:
Should the animation yoyo (reverse back down to the start) before repeating?
Source: src/animations/Animation.js#L157
Since: 3.0.0
Public Methods ​
addFrame ​
<instance> addFrame(config) ​
Description:
Add frames to the end of the animation.
Parameters:
name type optional description
config string | Array.< Phaser.Types.Animations.AnimationFrame > No Either a string, in which case it will use all frames from a texture with the matching key, or an array of Animation Frame configuration objects.
Returns: Phaser.Animations.Animation - This Animation object.
Source: src/animations/Animation.js#L281
Since: 3.0.0
addFrameAt ​
<instance> addFrameAt(index, config) ​
Description:
Add frame/s into the animation.
Parameters:
name type optional description
index number No The index to insert the frame at within the animation.
config string | Array.< Phaser.Types.Animations.AnimationFrame > No Either a string, in which case it will use all frames from a texture with the matching key, or an array of Animation Frame configuration objects.
Returns: Phaser.Animations.Animation - This Animation object.
Source: src/animations/Animation.js#L296
Since: 3.0.0
calculateDuration ​
<instance> calculateDuration(target, totalFrames, [duration], [frameRate]) ​
Description:
Calculates the duration, frame rate and msPerFrame values.
Parameters:
name type optional description
target Phaser.Animations.Animation No The target to set the values on.
totalFrames number No The total number of frames in the animation.
duration number Yes The duration to calculate the frame rate from. Pass null if you wish to set the frameRate instead.
frameRate number Yes The frame rate to calculate the duration from.
Source: src/animations/Animation.js#L242
Since: 3.50.0
checkFrame ​
<instance> checkFrame(index) ​
Description:
Check if the given frame index is valid.
Parameters:
name type optional description
index number No The index to be checked.
Returns: boolean - true if the index is valid, otherwise false .
Source: src/animations/Animation.js#L335
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Animation instance. It will remove all event listeners,
remove this animation and its key from the global Animation Manager,
and then destroy all Animation Frames in turn.
Source: src/animations/Animation.js#L917
Since: 3.0.0
getFirstTick ​
<instance> getFirstTick(state) ​
Description:
Called internally when this Animation first starts to play.
Sets the accumulator and nextTick properties.
Access: protected
Parameters:
name type optional description
state Phaser.Animations.AnimationState No The Animation State belonging to the Game Object invoking this call.
Source: src/animations/Animation.js#L350
Since: 3.0.0
getFrameAt ​
<instance> getFrameAt(index) ​
Description:
Returns the AnimationFrame at the provided index
Parameters:
name type optional description
index number No The index in the AnimationFrame array
Returns: Phaser.Animations.AnimationFrame - The frame at the index provided from the animation sequence
Source: src/animations/Animation.js#L368
Since: 3.0.0
getFrameByProgress ​
<instance> getFrameByProgress(value) ​
Description:
Returns the frame closest to the given progress value between 0 and 1.
Parameters:
name type optional description
value number No A value between 0 and 1.
Returns: Phaser.Animations.AnimationFrame - The frame closest to the given progress value.
Source: src/animations/Animation.js#L521
Since: 3.4.0
getFrames ​
<instance> getFrames(textureManager, frames, [defaultTextureKey]) ​
Description:
Creates AnimationFrame instances based on the given frame data.
Parameters:
name type optional description
textureManager Phaser.Textures.TextureManager No A reference to the global Texture Manager.
frames string | Array.< Phaser.Types.Animations.AnimationFrame > No Either a string, in which case it will use all frames from a texture with the matching key, or an array of Animation Frame configuration objects.
defaultTextureKey string Yes The key to use if no key is set in the frame configuration object.
Returns: Array.< Phaser.Animations.AnimationFrame > - An array of newly created AnimationFrame instances.
Source: src/animations/Animation.js#L383
Since: 3.0.0
getLastFrame ​
<instance> getLastFrame() ​
Description:
Returns the animation last frame.
Returns: Phaser.Animations.AnimationFrame - The last Animation Frame.
Source: src/animations/Animation.js#L623
Since: 3.12.0
getNextTick ​
<instance> getNextTick(state) ​
Description:
Called internally. Sets the accumulator and nextTick values of the current Animation.
Parameters:
name type optional description
state Phaser.Animations.AnimationState No The Animation State belonging to the Game Object invoking this call.
Source: src/animations/Animation.js#L506
Since: 3.0.0
getTotalFrames ​
<instance> getTotalFrames() ​
Description:
Gets the total number of frames in this animation.
Returns: number - The total number of frames in this animation.
Source: src/animations/Animation.js#L229
Since: 3.50.0
nextFrame ​
<instance> nextFrame(state) ​
Description:
Advance the animation frame.
Parameters:
name type optional description
state Phaser.Animations.AnimationState No The Animation State to advance.
Source: src/animations/Animation.js#L538
Since: 3.0.0
pause ​
<instance> pause() ​
Description:
Pauses playback of this Animation. The paused state is set immediately.
Returns: Phaser.Animations.Animation - This Animation object.
Source: src/animations/Animation.js#L887
Since: 3.0.0
previousFrame ​
<instance> previousFrame(state) ​
Description:
Called internally when the Animation is playing backwards.
Sets the previous frame, causing a yoyo, repeat, complete or update, accordingly.
Parameters:
name type optional description
state Phaser.Animations.AnimationState No The Animation State belonging to the Game Object invoking this call.
Source: src/animations/Animation.js#L636
Since: 3.0.0
removeFrame ​
<instance> removeFrame(frame) ​
Description:
Removes the given AnimationFrame from this Animation instance.
This is a global action. Any Game Object using this Animation will be impacted by this change.
Parameters:
name type optional description
frame Phaser.Animations.AnimationFrame No The AnimationFrame to be removed.
Returns: Phaser.Animations.Animation - This Animation object.
Source: src/animations/Animation.js#L698
Since: 3.0.0
removeFrameAt ​
<instance> removeFrameAt(index) ​
Description:
Removes a frame from the AnimationFrame array at the provided index
and updates the animation accordingly.
Parameters:
name type optional description
index number No The index in the AnimationFrame array
Returns: Phaser.Animations.Animation - This Animation object.
Source: src/animations/Animation.js#L721
Since: 3.0.0
repeatAnimation ​
<instance> repeatAnimation(state) ​
Description:
Called internally during playback. Forces the animation to repeat, providing there are enough counts left
in the repeat counter.
Parameters:
name type optional description
state Phaser.Animations.AnimationState No The Animation State belonging to the Game Object invoking this call.
Fires: Phaser.Animations.Events#event:ANIMATION_REPEAT , Phaser.Animations.Events#event:SPRITE_ANIMATION_REPEAT, Phaser.Animations.Events#event:SPRITE_ANIMATION_KEY_REPEAT
Source: src/animations/Animation.js#L741
Since: 3.0.0
resume ​
<instance> resume() ​
Description:
Resumes playback of this Animation. The paused state is reset immediately.
Returns: Phaser.Animations.Animation - This Animation object.
Source: src/animations/Animation.js#L902
Since: 3.0.0
toJSON ​
<instance> toJSON() ​
Description:
Converts the animation data to JSON.
Returns: Phaser.Types.Animations.JSONAnimation - The resulting JSONAnimation formatted object.
Source: src/animations/Animation.js#L795
Since: 3.0.0
updateFrameSequence ​
<instance> updateFrameSequence() ​
Description:
Called internally whenever frames are added to, or removed from, this Animation.
Returns: Phaser.Animations.Animation - This Animation object.
Source: src/animations/Animation.js#L830
Since: 3.0.0
Previous
Class
Next
AnimationFrame
Public Members
delay
duration
frameRate
frames
hideOnComplete
key
manager
msPerFrame
paused
randomFrame
repeat
repeatDelay
showBeforeDelay
showOnStart
skipMissedFrames
type
yoyo
Public Methods
addFrame
addFrameAt
calculateDuration
checkFrame
destroy
getFirstTick
getFrameAt
getFrameByProgress
getFrames
getLastFrame
getNextTick
getTotalFrames
nextFrame
pause
previousFrame
removeFrame
removeFrameAt
repeatAnimation
resume
toJSON
updateFrameSequence
