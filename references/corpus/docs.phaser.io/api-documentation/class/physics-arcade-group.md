# Group | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-arcade-group

Phaser API Documentation
Class
Group
Version: Phaser v3.90.0
On this page
Group
An Arcade Physics Group object.
The primary use of a Physics Group is a way to collect together physics enable objects
that share the same intrinsic structure into a single pool. They can they be easily
compared against other Groups, or Game Objects.
All Game Objects created by, or added to this Group will automatically be given dynamic
Arcade Physics bodies (if they have no body already) and the bodies will receive the
Groups default .
You should not pass objects into this Group that should not receive a body. For example,
do not add basic Geometry or Tilemap Layers into a Group, as they will not behave in the
way you may expect. Groups should all ideally have objects of the same type in them.
If you wish to create a Group filled with Static Bodies, please see Phaser.Physics.Arcade.StaticGroup .
Constructor
new Group(world, scene, [children], [config])
Parameters
name type optional description
world Phaser.Physics.Arcade.World No The physics simulation.
scene Phaser.Scene No The scene this group belongs to.
children Array.< Phaser.GameObjects.GameObject > | Phaser.Types.Physics.Arcade.PhysicsGroupConfig Phaser.Types.GameObjects.Group.GroupCreateConfig Yes
config Phaser.Types.Physics.Arcade.PhysicsGroupConfig | Phaser.Types.GameObjects.Group.GroupCreateConfig Yes Settings for this group.
Scope : static
Extends
Phaser.GameObjects.Group
Phaser.Physics.Arcade.Components.Collision
Source: src/physics/arcade/PhysicsGroup.js#L15
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Group :
active
children
createCallback
createMultipleCallback
defaultFrame
defaultKey
isParent
maxSize
name
removeCallback
runChildUpdate
scene
Public Members ​
classType ​
classType: function ​
Description:
The class to create new Group members from.
This should be either Phaser.Physics.Arcade.Image , Phaser.Physics.Arcade.Sprite , or a class extending one of those.
Overrides: Phaser.GameObjects.Group#classType
Source: src/physics/arcade/PhysicsGroup.js#L106
Since: 3.0.0
collisionCategory ​
collisionCategory: number ​
Description:
The Arcade Physics Group Collision Category.
This can be set to any valid collision bitfield value.
See the setCollisionCategory method for more details.
Source: src/physics/arcade/PhysicsGroup.js#L132
Since: 3.70.0
collisionMask ​
collisionMask: number ​
Description:
The Arcade Physics Group Collision Mask.
See the setCollidesWith method for more details.
Source: src/physics/arcade/PhysicsGroup.js#L145
Since: 3.70.0
defaults ​
defaults: Phaser.Types.Physics.Arcade.PhysicsGroupDefaults ​
Description:
Default physics properties applied to Game Objects added to the Group or created by the Group. Derived from the config argument.
You can remove the default values by setting this property to {} .
Source: src/physics/arcade/PhysicsGroup.js#L156
Since: 3.0.0
physicsType ​
physicsType: number ​
Description:
The physics type of the Group's members.
Source: src/physics/arcade/PhysicsGroup.js#L122
Since: 3.0.0
type ​
type: string ​
Description:
A textual representation of this Game Object.
Used internally by Phaser but is available for your own custom classes to populate.
Overrides: Phaser.GameObjects.Group#type
Source: src/physics/arcade/PhysicsGroup.js#L197
Since: 3.21.0
world ​
world: Phaser.Physics.Arcade.World ​
Description:
The physics simulation.
Source: src/physics/arcade/PhysicsGroup.js#L97
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
From Phaser.GameObjects.Group :
add
addMultiple
angle
clear
contains
countActive
create
createFromConfig
createMultiple
destroy
get
getChildren
getFirst
getFirstAlive
getFirstDead
getFirstNth
getLast
getLastNth
getLength
getMatching
getTotalFree
getTotalUsed
incX
incXY
incY
isFull
kill
killAndHide
playAnimation
preUpdate
propertyValueInc
propertyValueSet
remove
rotate
rotateAround
rotateAroundDistance
scaleX
scaleXY
scaleY
setActive
setAlpha
setBlendMode
setDepth
setHitArea
setName
setOrigin
setTint
setVisible
setX
setXY
setY
shiftPosition
shuffle
toggleVisible
From Phaser.Physics.Arcade.Components.Collision :
addCollidesWith
removeCollidesWith
resetCollisionCategory
setCollidesWith
setCollisionCategory
willCollideWith
Public Methods ​
createCallbackHandler ​
<instance> createCallbackHandler(child) ​
Description:
Enables a Game Object's Body and assigns defaults . Called when a Group member is added or created.
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object being added.
Source: src/physics/arcade/PhysicsGroup.js#L209
Since: 3.0.0
removeCallbackHandler ​
<instance> removeCallbackHandler(child) ​
Description:
Disables a Game Object's Body. Called when a Group member is removed.
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object being removed.
Source: src/physics/arcade/PhysicsGroup.js#L232
Since: 3.0.0
setVelocity ​
<instance> setVelocity(x, y, [step]) ​
Description:
Sets the velocity of each Group member.
Parameters:
name type optional default description
x number No The horizontal velocity.
y number No The vertical velocity.
step number Yes 0 The velocity increment. When set, the first member receives velocity (x, y), the second (x + step, y + step), and so on.
Returns: Phaser.Physics.Arcade.Group - This Physics Group object.
Source: src/physics/arcade/PhysicsGroup.js#L248
Since: 3.0.0
setVelocityX ​
<instance> setVelocityX(value, [step]) ​
Description:
Sets the horizontal velocity of each Group member.
Parameters:
name type optional default description
value number No The velocity value.
step number Yes 0 The velocity increment. When set, the first member receives velocity (x), the second (x + step), and so on.
Returns: Phaser.Physics.Arcade.Group - This Physics Group object.
Source: src/physics/arcade/PhysicsGroup.js#L274
Since: 3.0.0
setVelocityY ​
<instance> setVelocityY(value, [step]) ​
Description:
Sets the vertical velocity of each Group member.
Parameters:
name type optional default description
value number No The velocity value.
step number Yes 0 The velocity increment. When set, the first member receives velocity (y), the second (y + step), and so on.
Returns: Phaser.Physics.Arcade.Group - This Physics Group object.
Source: src/physics/arcade/PhysicsGroup.js#L299
Since: 3.0.0
Previous
Factory
Next
Image
Inherited Members
Public Members
classType
collisionCategory
collisionMask
defaults
physicsType
type
world
Inherited Methods
Public Methods
createCallbackHandler
removeCallbackHandler
setVelocity
setVelocityX
setVelocityY
