# PathFollower | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-pathfollower

Phaser API Documentation
Class
PathFollower
Version: Phaser v3.90.0
On this page
PathFollower
A PathFollower Game Object.
A PathFollower is a Sprite Game Object with some extra helpers to allow it to follow a Path automatically.
Anything you can do with a standard Sprite can be done with this PathFollower, such as animate it, tint it,
scale it and so on.
PathFollowers are bound to a single Path at any one time and can traverse the length of the Path, from start
to finish, forwards or backwards, or from any given point on the Path to its end. They can optionally rotate
to face the direction of the path, be offset from the path coordinates or rotate independently of the Path.
Constructor
new PathFollower(scene, path, x, y, texture, [frame])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this PathFollower belongs.
path Phaser.Curves.Path No The Path this PathFollower is following. It can only follow one Path at a time.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
texture string | Phaser.Textures.Texture No The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
Scope : static
Extends
Phaser.GameObjects.Sprite
Phaser.GameObjects.Components.PathFollower
Source: src/gameobjects/pathfollower/PathFollower.js#L11
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
From Phaser.GameObjects.Components.PathFollower :
path
rotateToPath
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
From Phaser.GameObjects.Sprite :
anims
Public Members ​
pathConfig ​
pathConfig: Phaser.Types.GameObjects.PathFollower.PathConfig ​
Description:
Settings for the PathFollower.
Source: src/gameobjects/components/PathFollower.js#L91
Since: 3.0.0
pathDelta ​
pathDelta: Phaser.Math.Vector2 ​
Description:
The distance the follower has traveled from the previous point to the current one, at the last update.
Source: src/gameobjects/components/PathFollower.js#L73
Since: 3.23.0
pathOffset ​
pathOffset: Phaser.Math.Vector2 ​
Description:
An additional vector to add to the PathFollowers position, allowing you to offset it from the
Path coordinates.
Source: src/gameobjects/components/PathFollower.js#L54
Since: 3.0.0
pathRotationOffset ​
pathRotationOffset: number ​
Description:
If the PathFollower is rotating to match the Path (@see Phaser.GameObjects.PathFollower#rotateToPath)
this value is added to the rotation value. This allows you to rotate objects to a path but control
the angle of the rotation as well.
Source: src/gameobjects/components/PathFollower.js#L42
Since: 3.0.0
pathTween ​
pathTween: Phaser.Tweens.Tween ​
Description:
The Tween used for following the Path.
Source: src/gameobjects/components/PathFollower.js#L82
Since: 3.0.0
pathVector ​
pathVector: Phaser.Math.Vector2 ​
Description:
A Vector2 that stores the current point of the path the follower is on.
Source: src/gameobjects/components/PathFollower.js#L64
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
From Phaser.GameObjects.Components.PathFollower :
isFollowing
pathUpdate
pauseFollow
resumeFollow
setPath
setRotateToPath
startFollow
stopFollow
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
From Phaser.GameObjects.Sprite :
chain
play
playAfterDelay
playAfterRepeat
playReverse
stop
stopAfterDelay
stopAfterRepeat
stopOnFrame
toJSON
Public Methods ​
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
Internal update handler that advances this PathFollower along the path.
Called automatically by the Scene step, should not typically be called directly.
Access: protected
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time, in ms, elapsed since the last frame.
Overrides: Phaser.GameObjects.Sprite#preUpdate
Source: src/gameobjects/pathfollower/PathFollower.js#L56
Since: 3.0.0
Previous
RandomZone
Next
Plane
Inherited Members
Public Members
pathConfig
pathDelta
pathOffset
pathRotationOffset
pathTween
pathVector
Inherited Methods
Public Methods
preUpdate
