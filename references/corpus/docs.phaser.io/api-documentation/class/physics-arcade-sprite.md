# Sprite | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-arcade-sprite

Phaser API Documentation
Class
Sprite
Version: Phaser v3.90.0
On this page
Sprite
An Arcade Physics Sprite is a Sprite with an Arcade Physics body and related components.
The body can be dynamic or static.
The main difference between an Arcade Sprite and an Arcade Image is that you cannot animate an Arcade Image.
If you do not require animation then you can safely use Arcade Images instead of Arcade Sprites.
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
Phaser.GameObjects.Sprite
Phaser.Physics.Arcade.Components.Acceleration
Phaser.Physics.Arcade.Components.Angular
Phaser.Physics.Arcade.Components.Bounce
Phaser.Physics.Arcade.Components.Collision
Phaser.Physics.Arcade.Components.Debug
Phaser.Physics.Arcade.Components.Drag
Phaser.Physics.Arcade.Components.Enable
Phaser.Physics.Arcade.Components.Friction
Phaser.Physics.Arcade.Components.Gravity
Phaser.Physics.Arcade.Components.Immovable
Phaser.Physics.Arcade.Components.Mass
Phaser.Physics.Arcade.Components.Pushable
Phaser.Physics.Arcade.Components.Size
Phaser.Physics.Arcade.Components.Velocity
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
Phaser.GameObjects.Components.Texture
Phaser.GameObjects.Components.Tint
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/physics/arcade/ArcadeSprite.js#L11
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
From Phaser.Physics.Arcade.Components.Debug :
debugBodyColor
debugShowBody
debugShowVelocity
Public Members ​
body ​
body: Phaser.Physics.Arcade.Body , Phaser.Physics.Arcade.StaticBody ​
Description:
This Game Object's Physics Body.
Overrides: Phaser.GameObjects.Sprite#body
Source: src/physics/arcade/ArcadeSprite.js#L88
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
From Phaser.GameObjects.Sprite :
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
From Phaser.Physics.Arcade.Components.Acceleration :
setAcceleration
setAccelerationX
setAccelerationY
From Phaser.Physics.Arcade.Components.Angular :
setAngularAcceleration
setAngularDrag
setAngularVelocity
From Phaser.Physics.Arcade.Components.Bounce :
setBounce
setBounceX
setBounceY
setCollideWorldBounds
From Phaser.Physics.Arcade.Components.Collision :
addCollidesWith
removeCollidesWith
resetCollisionCategory
setCollidesWith
setCollisionCategory
willCollideWith
From Phaser.Physics.Arcade.Components.Debug :
setDebug
setDebugBodyColor
From Phaser.Physics.Arcade.Components.Drag :
setDamping
setDrag
setDragX
setDragY
From Phaser.Physics.Arcade.Components.Enable :
disableBody
enableBody
refreshBody
setDirectControl
From Phaser.Physics.Arcade.Components.Friction :
setFriction
setFrictionX
setFrictionY
From Phaser.Physics.Arcade.Components.Gravity :
setGravity
setGravityX
setGravityY
From Phaser.Physics.Arcade.Components.Immovable :
setImmovable
From Phaser.Physics.Arcade.Components.Mass :
setMass
From Phaser.Physics.Arcade.Components.Pushable :
setPushable
From Phaser.Physics.Arcade.Components.Size :
setBodySize
setCircle
setOffset
From Phaser.Physics.Arcade.Components.Velocity :
setMaxVelocity
setVelocity
setVelocityX
setVelocityY
Previous
Image
Next
StaticBody
Inherited Members
Public Members
body
Inherited Methods
