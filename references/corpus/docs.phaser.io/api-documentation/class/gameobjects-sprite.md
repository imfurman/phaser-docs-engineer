# Sprite | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-sprite

Phaser API Documentation
Class
Sprite
Version: Phaser v3.90.0
On this page
Sprite
A Sprite Game Object.
A Sprite Game Object is used for the display of both static and animated images in your game.
Sprites can have input events and physics bodies. They can also be tweened, tinted, scrolled
and animated.
The main difference between a Sprite and an Image Game Object is that you cannot animate Images.
As such, Sprites take a fraction longer to process and have a larger API footprint due to the Animation
Component. If you do not require animation then you can safely use Images to replace Sprites in all cases.
Constructor
new Sprite(scene, x, y, texture, [frame])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
texture string | Phaser.Textures.Texture No The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Alpha
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Flip
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Size
Phaser.GameObjects.Components.TextureCrop
Phaser.GameObjects.Components.Tint
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/sprite/Sprite.js#L13
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Components.Alpha :
alpha
alphaBottomLeft
alphaBottomRight
alphaTopLeft
alphaTopRight
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Flip :
flipX
flipY
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
From Phaser.GameObjects.Components.Pipeline :
defaultPipeline
pipeline
pipelineData
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
From Phaser.GameObjects.Components.Size :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.TextureCrop :
frame
isCropped
texture
From Phaser.GameObjects.Components.Tint :
isTinted
tint
tintBottomLeft
tintBottomRight
tintFill
tintTopLeft
tintTopRight
From Phaser.GameObjects.Components.Transform :
angle
hasTransformComponent
rotation
scale
scaleX
scaleY
w
x
y
z
From Phaser.GameObjects.Components.Visible :
visible
From Phaser.GameObjects.GameObject :
active
body
cameraFilter
data
displayList
ignoreDestroy
input
name
parentContainer
renderFlags
scene
state
tabIndex
type
Public Members ​
anims ​
anims: Phaser.Animations.AnimationState ​
Description:
The Animation State component of this Sprite.
This component provides features to apply animations to this Sprite.
It is responsible for playing, loading, queuing animations for later playback,
mixing between animations and setting the current animation frame to this Sprite.
Source: src/gameobjects/sprite/Sprite.js#L92
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
From Phaser.GameObjects.Components.Alpha :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Flip :
resetFlip
setFlip
setFlipX
setFlipY
toggleFlipX
toggleFlipY
From Phaser.GameObjects.Components.GetBounds :
getBottomCenter
getBottomLeft
getBottomRight
getBounds
getCenter
getLeftCenter
getRightCenter
getTopCenter
getTopLeft
getTopRight
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
From Phaser.GameObjects.Components.Pipeline :
getPipelineName
initPipeline
resetPipeline
setPipeline
setPipelineData
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
From Phaser.GameObjects.Components.Size :
setDisplaySize
setSize
setSizeToFrame
From Phaser.GameObjects.Components.TextureCrop :
setCrop
setFrame
setTexture
From Phaser.GameObjects.Components.Tint :
clearTint
setTint
setTintFill
From Phaser.GameObjects.Components.Transform :
copyPosition
getLocalPoint
getLocalTransformMatrix
getParentRotation
getWorldPoint
getWorldTransformMatrix
setAngle
setPosition
setRandomPosition
setRotation
setScale
setW
setX
setY
setZ
From Phaser.GameObjects.Components.Visible :
setVisible
From Phaser.GameObjects.GameObject :
addedToScene
addToDisplayList
addToUpdateList
destroy
disableInteractive
getData
getDisplayList
getIndexList
incData
removedFromScene
removeFromDisplayList
removeFromUpdateList
removeInteractive
setActive
setData
setDataEnabled
setInteractive
setName
setState
toggleData
update
willRender
Public Methods ​
chain ​
<instance> chain([key]) ​
Description:
Sets an animation, or an array of animations, to be played immediately after the current one completes or stops.
The current animation must enter a 'completed' state for this to happen, i.e. finish all of its repeats, delays, etc,
or have the stop method called directly on it.
An animation set to repeat forever will never enter a completed state.
You can chain a new animation at any point, including before the current one starts playing, during it,
or when it ends (via its animationcomplete event).
Chained animations are specific to a Game Object, meaning different Game Objects can have different chained
animations without impacting the animation they're playing.
Call this method with no arguments to reset all currently chained animations.
When playing an animation on a Sprite it will first check to see if it can find a matching key
locally within the Sprite. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
Parameters:
name type optional description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig Array.<string>
Returns: Phaser.GameObjects.Sprite - This Game Object.
Source: src/gameobjects/sprite/Sprite.js#L327
Since: 3.50.0
play ​
<instance> play(key, [ignoreIfPlaying]) ​
Description:
Start playing the given animation on this Sprite.
Animations in Phaser can either belong to the global Animation Manager, or specifically to this Sprite.
The benefit of a global animation is that multiple Sprites can all play the same animation, without
having to duplicate the data. You can just create it once and then play it on any Sprite.
The following code shows how to create a global repeating animation. The animation will be created
from all of the frames within the sprite sheet that was loaded with the key 'muybridge':
var config = {
key : 'run' ,
frames : 'muybridge' ,
frameRate : 15 ,
repeat : - 1
} ;
// This code should be run from within a Scene:
this . anims . create ( config ) ;
However, if you wish to create an animation that is unique to this Sprite, and this Sprite alone,
you can call the Animation.create method instead. It accepts the exact same parameters as when
creating a global animation, however the resulting data is kept locally in this Sprite.
With the animation created, either globally or locally, you can now play it on this Sprite:
this . add . sprite ( x , y ) . play ( 'run' ) ;
Alternatively, if you wish to run it at a different frame rate, for example, you can pass a config
object instead:
this . add . sprite ( x , y ) . play ( { key : 'run' , frameRate : 24 } ) ;
When playing an animation on a Sprite it will first check to see if it can find a matching key
locally within the Sprite. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
If you need a Sprite to be able to play both local and global animations, make sure they don't
have conflicting keys.
See the documentation for the PlayAnimationConfig config object for more details about this.
Also, see the documentation in the Animation Manager for further details on creating animations.
Parameters:
name type optional default description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
ignoreIfPlaying boolean Yes false If an animation is already playing then ignore this call.
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/sprite/Sprite.js#L140
Since: 3.0.0
playAfterDelay ​
<instance> playAfterDelay(key, delay) ​
Description:
Waits for the specified delay, in milliseconds, then starts playback of the given animation.
If the animation also has a delay value set in its config, it will be added to the delay given here.
If an animation is already running and a new animation is given to this method, it will wait for
the given delay before starting the new animation.
If no animation is currently running, the given one begins after the delay.
When playing an animation on a Sprite it will first check to see if it can find a matching key
locally within the Sprite. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
Prior to Phaser 3.50 this method was called 'delayedPlay'.
Parameters:
name type optional description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
delay number No The delay, in milliseconds, to wait before starting the animation playing.
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/sprite/Sprite.js#L270
Since: 3.50.0
playAfterRepeat ​
<instance> playAfterRepeat(key, [repeatCount]) ​
Description:
Waits for the current animation to complete the repeatCount number of repeat cycles, then starts playback
of the given animation.
You can use this to ensure there are no harsh jumps between two sets of animations, i.e. going from an
idle animation to a walking animation, by making them blend smoothly into each other.
If no animation is currently running, the given one will start immediately.
When playing an animation on a Sprite it will first check to see if it can find a matching key
locally within the Sprite. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
Parameters:
name type optional default description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
repeatCount number Yes 1 How many times should the animation repeat before the next one starts?
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/sprite/Sprite.js#L300
Since: 3.50.0
playReverse ​
<instance> playReverse(key, [ignoreIfPlaying]) ​
Description:
Start playing the given animation on this Sprite, in reverse.
Animations in Phaser can either belong to the global Animation Manager, or specifically to this Sprite.
The benefit of a global animation is that multiple Sprites can all play the same animation, without
having to duplicate the data. You can just create it once and then play it on any Sprite.
The following code shows how to create a global repeating animation. The animation will be created
from all of the frames within the sprite sheet that was loaded with the key 'muybridge':
var config = {
key : 'run' ,
frames : 'muybridge' ,
frameRate : 15 ,
repeat : - 1
} ;
// This code should be run from within a Scene:
this . anims . create ( config ) ;
However, if you wish to create an animation that is unique to this Sprite, and this Sprite alone,
you can call the Animation.create method instead. It accepts the exact same parameters as when
creating a global animation, however the resulting data is kept locally in this Sprite.
With the animation created, either globally or locally, you can now play it on this Sprite:
this . add . sprite ( x , y ) . playReverse ( 'run' ) ;
Alternatively, if you wish to run it at a different frame rate, for example, you can pass a config
object instead:
this . add . sprite ( x , y ) . playReverse ( { key : 'run' , frameRate : 24 } ) ;
When playing an animation on a Sprite it will first check to see if it can find a matching key
locally within the Sprite. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
If you need a Sprite to be able to play both local and global animations, make sure they don't
have conflicting keys.
See the documentation for the PlayAnimationConfig config object for more details about this.
Also, see the documentation in the Animation Manager for further details on creating animations.
Parameters:
name type optional default description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
ignoreIfPlaying boolean Yes false If an animation is already playing then ignore this call.
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/sprite/Sprite.js#L205
Since: 3.50.0
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
Update this Sprite's animations.
Access: protected
Parameters:
name type optional description
time number No The current timestamp.
delta number No The delta time, in ms, elapsed since the last frame.
Source: src/gameobjects/sprite/Sprite.js#L125
Since: 3.0.0
stop ​
<instance> stop() ​
Description:
Immediately stops the current animation from playing and dispatches the ANIMATION_STOP events.
If no animation is playing, no event will be dispatched.
If there is another animation queued (via the chain method) then it will start playing immediately.
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/sprite/Sprite.js#L359
Since: 3.50.0
stopAfterDelay ​
<instance> stopAfterDelay(delay) ​
Description:
Stops the current animation from playing after the specified time delay, given in milliseconds.
It then dispatches the ANIMATION_STOP event.
If no animation is running, no events will be dispatched.
If there is another animation in the queue (set via the chain method) then it will start playing,
when the current one stops.
Parameters:
name type optional description
delay number No The number of milliseconds to wait before stopping this animation.
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/sprite/Sprite.js#L377
Since: 3.50.0
stopAfterRepeat ​
<instance> stopAfterRepeat([repeatCount]) ​
Description:
Stops the current animation from playing after the given number of repeats.
It then dispatches the ANIMATION_STOP event.
If no animation is running, no events will be dispatched.
If there is another animation in the queue (set via the chain method) then it will start playing,
when the current one stops.
Parameters:
name type optional default description
repeatCount number Yes 1 How many times should the animation repeat before stopping?
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/sprite/Sprite.js#L400
Since: 3.50.0
stopOnFrame ​
<instance> stopOnFrame(frame) ​
Description:
Stops the current animation from playing when it next sets the given frame.
If this frame doesn't exist within the animation it will not stop it from playing.
It then dispatches the ANIMATION_STOP event.
If no animation is running, no events will be dispatched.
If there is another animation in the queue (set via the chain method) then it will start playing,
when the current one stops.
Parameters:
name type optional description
frame Phaser.Animations.AnimationFrame No The frame to check before stopping this animation.
Returns: Phaser.GameObjects.Sprite - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/sprite/Sprite.js#L423
Since: 3.50.0
toJSON ​
<instance> toJSON() ​
Description:
Build a JSON representation of this Sprite.
Overrides: Phaser.GameObjects.GameObject#toJSON
Returns: Phaser.Types.GameObjects.JSONGameObject - A JSON representation of the Game Object.
Source: src/gameobjects/sprite/Sprite.js#L447
Since: 3.0.0
Previous
Shape
Next
Star
Inherited Members
Public Members
anims
Inherited Methods
Public Methods
chain
play
playAfterDelay
playAfterRepeat
playReverse
preUpdate
stop
stopAfterDelay
stopAfterRepeat
stopOnFrame
toJSON
