# Image | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-matter-image

Phaser API Documentation
Class
Image
Version: Phaser v3.90.0
On this page
Image
A Matter Physics Image Game Object.
An Image is a light-weight Game Object useful for the display of static images in your game,
such as logos, backgrounds, scenery or other non-animated elements. Images can have input
events and physics bodies, or be tweened, tinted or scrolled. The main difference between an
Image and a Sprite is that you cannot animate an Image as they do not have the Animation component.
Constructor
new Image(world, x, y, texture, [frame], [options])
Parameters
name type optional description
world Phaser.Physics.Matter.World No A reference to the Matter.World instance that this body belongs to.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
texture string | Phaser.Textures.Texture No The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
frame string | number Yes An optional frame from the Texture this Game Object is rendering with.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Scope : static
Extends
Phaser.GameObjects.Image
Phaser.Physics.Matter.Components.Bounce
Phaser.Physics.Matter.Components.Collision
Phaser.Physics.Matter.Components.Force
Phaser.Physics.Matter.Components.Friction
Phaser.Physics.Matter.Components.Gravity
Phaser.Physics.Matter.Components.Mass
Phaser.Physics.Matter.Components.Sensor
Phaser.Physics.Matter.Components.SetBody
Phaser.Physics.Matter.Components.Sleep
Phaser.Physics.Matter.Components.Static
Phaser.Physics.Matter.Components.Transform
Phaser.Physics.Matter.Components.Velocity
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
Source: src/physics/matter-js/MatterImage.js#L15
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
From Phaser.Physics.Matter.Components.Mass :
centerOfMass
Public Members ​
world ​
world: Phaser.Physics.Matter.World ​
Description:
A reference to the Matter.World instance that this body belongs to.
Source: src/physics/matter-js/MatterImage.js#L105
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
toJSON
update
willRender
From Phaser.Physics.Matter.Components.Bounce :
setBounce
From Phaser.Physics.Matter.Components.Collision :
setCollidesWith
setCollisionCategory
setCollisionGroup
setOnCollide
setOnCollideActive
setOnCollideEnd
setOnCollideWith
From Phaser.Physics.Matter.Components.Force :
applyForce
applyForceFrom
thrust
thrustBack
thrustLeft
thrustRight
From Phaser.Physics.Matter.Components.Friction :
setFriction
setFrictionAir
setFrictionStatic
From Phaser.Physics.Matter.Components.Gravity :
setIgnoreGravity
From Phaser.Physics.Matter.Components.Mass :
setDensity
setMass
From Phaser.Physics.Matter.Components.Sensor :
isSensor
setSensor
From Phaser.Physics.Matter.Components.SetBody :
setBody
setCircle
setExistingBody
setPolygon
setRectangle
setTrapezoid
From Phaser.Physics.Matter.Components.Sleep :
setAwake
setSleepEndEvent
setSleepEvents
setSleepStartEvent
setSleepThreshold
setToSleep
From Phaser.Physics.Matter.Components.Static :
isStatic
setStatic
From Phaser.Physics.Matter.Components.Transform :
setFixedRotation
From Phaser.Physics.Matter.Components.Velocity :
getAngularSpeed
getAngularVelocity
getVelocity
setAngularSpeed
setAngularVelocity
setVelocity
setVelocityX
setVelocityY
Previous
Factory
Next
MatterPhysics
Inherited Members
Public Members
world
Inherited Methods
