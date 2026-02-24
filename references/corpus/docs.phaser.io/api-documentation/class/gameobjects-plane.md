# Plane | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-plane

Phaser API Documentation
Class
Plane
Version: Phaser v3.90.0
On this page
Plane
A Plane Game Object.
The Plane Game Object is a helper class that takes the Mesh Game Object and extends it,
allowing for fast and easy creation of Planes. A Plane is a one-sided grid of cells,
where you specify the number of cells in each dimension. The Plane can have a texture
that is either repeated (tiled) across each cell, or applied to the full Plane.
The Plane can then be manipulated in 3D space, with rotation across all 3 axis.
This allows you to create effects not possible with regular Sprites, such as perspective
distortion. You can also adjust the vertices on a per-vertex basis. Plane data becomes
part of the WebGL batch, just like standard Sprites, so doesn't introduce any additional
shader overhead. Because the Plane just generates vertices into the WebGL batch, like any
other Sprite, you can use all of the common Game Object components on a Plane too,
such as a custom pipeline, mask, blend mode or texture.
You can use the uvScroll and uvScale methods to adjust the placement and scaling
of the texture if this Plane is using a single texture, and not a frame from a texture
atlas or sprite sheet.
The Plane Game Object also has the Animation component, allowing you to play animations
across the Plane just as you would with a Sprite. The animation frame size must be fixed
as the first frame will be the size of the entire animation, for example use a SpriteSheet .
Note that the Plane object is WebGL only and does not have a Canvas counterpart.
The Plane origin is always 0.5 x 0.5 and cannot be changed.
Constructor
new Plane(scene, [x], [y], [texture], [frame], [width], [height], [tile])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Plane belongs. A Plane can only belong to one Scene at a time.
x number Yes The horizontal position of this Plane in the world.
y number Yes The vertical position of this Plane in the world.
texture string | Phaser.Textures.Texture Yes The key, or instance of the Texture this Plane will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Plane is rendering with.
width number Yes 8 The width of this Plane, in cells, not pixels.
height number Yes 8 The height of this Plane, in cells, not pixels.
tile boolean Yes false Is the texture tiled? I.e. repeated across each cell.
Scope : static
Extends
Phaser.GameObjects.Mesh
Source: src/gameobjects/plane/Plane.js#L14
Since: 3.60.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
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
From Phaser.GameObjects.Components.Texture :
frame
texture
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
From Phaser.GameObjects.Mesh :
debugCallback
debugGraphic
faces
fov
hideCCW
ignoreDirtyCache
modelPosition
modelRotation
modelScale
projectionMatrix
tintFill
totalRendered
transformMatrix
vertices
viewMatrix
viewPosition
Public Members ​
anims ​
anims: Phaser.Animations.AnimationState ​
Description:
The Animation State component of this Sprite.
This component provides features to apply animations to this Sprite.
It is responsible for playing, loading, queuing animations for later playback,
mixing between animations and setting the current animation frame to this Sprite.
Source: src/gameobjects/plane/Plane.js#L73
Since: 3.60.0
gridHeight ​
gridHeight: number ​
Description:
The height of this Plane in cells, not pixels.
This value is read-only. To adjust it, see the setGridSize method.
Source: src/gameobjects/plane/Plane.js#L98
Since: 3.60.0
gridWidth ​
gridWidth: number ​
Description:
The width of this Plane in cells, not pixels.
This value is read-only. To adjust it, see the setGridSize method.
Source: src/gameobjects/plane/Plane.js#L86
Since: 3.60.0
isTiled ​
isTiled: boolean ​
Description:
Is the texture of this Plane tiled across all cells, or not?
This value is read-only. To adjust it, see the setGridSize method.
Source: src/gameobjects/plane/Plane.js#L110
Since: 3.60.0
originX ​
originX: number ​
Description:
Do not change this value. It has no effect other than to break things.
Source: src/gameobjects/plane/Plane.js#L140
Since: 3.70.0
originY ​
originY: number ​
Description:
Do not change this value. It has no effect other than to break things.
Source: src/gameobjects/plane/Plane.js#L158
Since: 3.70.0
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
From Phaser.GameObjects.Components.AlphaSingle :
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
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
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
From Phaser.GameObjects.Components.Texture :
setFrame
setTexture
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
setName
setState
toggleData
toJSON
update
willRender
From Phaser.GameObjects.Mesh :
addFace
addVertex
addVertices
addVerticesFromObj
clear
clearTint
depthSort
getFace
getFaceAt
getFaceCount
getVertexCount
hasFaceAt
isDirty
panX
panY
panZ
renderDebug
rotateX
rotateY
rotateZ
setDebug
setInteractive
setOrtho
setPerspective
setTint
sortByDepth
tint
uvScale
uvScroll
Public Methods ​
createCheckerboard ​
<instance> createCheckerboard([color1], [color2], [alpha1], [alpha2], [height]) ​
Description:
Creates a checkerboard style texture, based on the given colors and alpha
values and applies it to this Plane, replacing any current texture it may
have.
The colors are used in an alternating pattern, like a chess board.
Calling this method generates a brand new 16x16 pixel WebGLTexture internally
and applies it to this Plane. While quite fast to do, you should still be
mindful of calling this method either extensively, or in tight parts of
your game.
Parameters:
name type optional default description
color1 number Yes "0xffffff" The odd cell color, specified as a hex value.
color2 number Yes "0x0000ff" The even cell color, specified as a hex value.
alpha1 number Yes 255 The odd cell alpha value, specified as a number between 0 and 255.
alpha2 number Yes 255 The even cell alpha value, specified as a number between 0 and 255.
height number Yes 128 The view height of the Plane after creation, in pixels.
Source: src/gameobjects/plane/Plane.js#L360
Since: 3.60.0
play ​
<instance> play(key, [ignoreIfPlaying]) ​
Description:
Start playing the given animation on this Plane.
Animations in Phaser can either belong to the global Animation Manager, or specifically to this Plane.
The benefit of a global animation is that multiple Game Objects can all play the same animation, without
having to duplicate the data. You can just create it once and then play it on any animating Game Object.
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
However, if you wish to create an animation that is unique to this Plane, and this Plane alone,
you can call the Animation.create method instead. It accepts the exact same parameters as when
creating a global animation, however the resulting data is kept locally in this Plane.
With the animation created, either globally or locally, you can now play it on this Plane:
const plane = this . add . plane ( ... ) ;
plane . play ( 'run' ) ;
Alternatively, if you wish to run it at a different frame rate for example, you can pass a config
object instead:
const plane = this . add . plane ( ... ) ;
plane . play ( { key : 'run' , frameRate : 24 } ) ;
When playing an animation on a Plane it will first check to see if it can find a matching key
locally within the Plane. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
If you need a Plane to be able to play both local and global animations, make sure they don't
have conflicting keys.
See the documentation for the PlayAnimationConfig config object for more details about this.
Also, see the documentation in the Animation Manager for further details on creating animations.
Parameters:
name type optional default description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
ignoreIfPlaying boolean Yes false If an animation is already playing then ignore this call.
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/plane/Plane.js#L441
Since: 3.60.0
playAfterDelay ​
<instance> playAfterDelay(key, delay) ​
Description:
Waits for the specified delay, in milliseconds, then starts playback of the given animation.
If the animation also has a delay value set in its config, it will be added to the delay given here.
If an animation is already running and a new animation is given to this method, it will wait for
the given delay before starting the new animation.
If no animation is currently running, the given one begins after the delay.
When playing an animation on a Game Object it will first check to see if it can find a matching key
locally within the Game Object. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
Parameters:
name type optional description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
delay number No The delay, in milliseconds, to wait before starting the animation playing.
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/plane/Plane.js#L575
Since: 3.60.0
playAfterRepeat ​
<instance> playAfterRepeat(key, [repeatCount]) ​
Description:
Waits for the current animation to complete the repeatCount number of repeat cycles, then starts playback
of the given animation.
You can use this to ensure there are no harsh jumps between two sets of animations, i.e. going from an
idle animation to a walking animation, by making them blend smoothly into each other.
If no animation is currently running, the given one will start immediately.
When playing an animation on a Game Object it will first check to see if it can find a matching key
locally within the Game Object. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
Parameters:
name type optional default description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
repeatCount number Yes 1 How many times should the animation repeat before the next one starts?
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/plane/Plane.js#L603
Since: 3.60.0
playReverse ​
<instance> playReverse(key, [ignoreIfPlaying]) ​
Description:
Start playing the given animation on this Plane, in reverse.
Animations in Phaser can either belong to the global Animation Manager, or specifically to a Game Object.
The benefit of a global animation is that multiple Game Objects can all play the same animation, without
having to duplicate the data. You can just create it once and then play it on any animating Game Object.
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
However, if you wish to create an animation that is unique to this Game Object, and this Game Object alone,
you can call the Animation.create method instead. It accepts the exact same parameters as when
creating a global animation, however the resulting data is kept locally in this Game Object.
With the animation created, either globally or locally, you can now play it on this Game Object:
const plane = this . add . plane ( ... ) ;
plane . playReverse ( 'run' ) ;
Alternatively, if you wish to run it at a different frame rate, for example, you can pass a config
object instead:
const plane = this . add . plane ( ... ) ;
plane . playReverse ( { key : 'run' , frameRate : 24 } ) ;
When playing an animation on a Game Object it will first check to see if it can find a matching key
locally within the Game Object. If it can, it will play the local animation. If not, it will then
search the global Animation Manager and look for it there.
If you need a Game Object to be able to play both local and global animations, make sure they don't
have conflicting keys.
See the documentation for the PlayAnimationConfig config object for more details about this.
Also, see the documentation in the Animation Manager for further details on creating animations.
Parameters:
name type optional default description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
ignoreIfPlaying boolean Yes false If an animation is already playing then ignore this call.
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_START
Source: src/gameobjects/plane/Plane.js#L508
Since: 3.60.0
preDestroy ​
<instance> preDestroy([width], [height], [tile]) ​
Description:
Modifies the layout of this Plane by adjusting the grid dimensions to the
given width and height. The values are given in cells, not pixels.
The tile parameter allows you to control if the texture is tiled, or
applied across the entire Plane? A tiled texture will repeat with one
iteration per cell. A non-tiled texture will be applied across the whole
Plane.
Note that if this Plane is using a single texture, not from a texture atlas
or sprite sheet, then you can use the Plane.uvScale method to have much
more fine-grained control over the texture tiling.
Parameters:
name type optional default description
width number Yes 8 The width of this Plane, in cells, not pixels.
height number Yes 8 The height of this Plane, in cells, not pixels.
tile boolean Yes false Is the texture tiled? I.e. repeated across each cell.
Overrides: Phaser.GameObjects.Mesh#preDestroy
Source: src/gameobjects/plane/Plane.js#L176
Since: 3.60.0
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
Runs the preUpdate for this Plane, which will check its Animation State,
if one is playing, and refresh view / model matrices, if updated.
Access: protected
Parameters:
name type optional description
time number No The current timestamp.
delta number No The delta time, in ms, elapsed since the last frame.
Overrides: Phaser.GameObjects.Mesh#preUpdate
Source: src/gameobjects/plane/Plane.js#L718
Since: 3.60.0
removeCheckerboard ​
<instance> removeCheckerboard() ​
Description:
If this Plane has a Checkerboard Texture, this method will destroy it
and reset the internal flag for it.
Source: src/gameobjects/plane/Plane.js#L424
Since: 3.60.0
setSizeToFrame ​
<instance> setSizeToFrame([resetUV]) ​
Description:
An internal method that resets the perspective projection for this Plane
when it changes texture or frame, and also resets the cell UV coordinates,
if required.
Parameters:
name type optional default description
resetUV boolean Yes true Reset all of the cell UV coordinates?
Returns: Phaser.GameObjects.Plane - This Game Object instance.
Source: src/gameobjects/plane/Plane.js#L227
Since: 3.60.0
setViewHeight ​
<instance> setViewHeight([value]) ​
Description:
Sets the height of this Plane to match the given value, in pixels.
This adjusts the Plane.viewPosition.z value to achieve this.
If no value parameter is given, it will set the view height to match
that of the current texture frame the Plane is using.
Parameters:
name type optional description
value number Yes The height, in pixels, to set this Plane view height to.
Source: src/gameobjects/plane/Plane.js#L336
Since: 3.60.0
stop ​
<instance> stop() ​
Description:
Immediately stops the current animation from playing and dispatches the ANIMATION_STOP events.
If no animation is playing, no event will be dispatched.
If there is another animation queued (via the chain method) then it will start playing immediately.
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/plane/Plane.js#L630
Since: 3.60.0
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
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/plane/Plane.js#L648
Since: 3.60.0
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
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/plane/Plane.js#L671
Since: 3.60.0
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
Returns: Phaser.GameObjects.Plane - This Game Object.
Fires: Phaser.Animations.Events#event:ANIMATION_STOP
Source: src/gameobjects/plane/Plane.js#L694
Since: 3.60.0
Previous
PathFollower
Next
PointLight
Inherited Members
Public Members
anims
gridHeight
gridWidth
isTiled
originX
originY
Inherited Methods
Public Methods
createCheckerboard
play
playAfterDelay
playAfterRepeat
playReverse
preDestroy
preUpdate
removeCheckerboard
setSizeToFrame
setViewHeight
stop
stopAfterDelay
stopAfterRepeat
stopOnFrame
