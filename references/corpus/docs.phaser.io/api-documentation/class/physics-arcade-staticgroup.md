# StaticGroup | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-arcade-staticgroup

Phaser API Documentation
Class
StaticGroup
Version: Phaser v3.90.0
On this page
StaticGroup
An Arcade Physics Static Group object.
All Game Objects created by or added to this Group will automatically be given static Arcade Physics bodies, if they have no body.
Its dynamic counterpart is Phaser.Physics.Arcade.Group .
Constructor
new StaticGroup(world, scene, [children], [config])
Parameters
name type optional description
world Phaser.Physics.Arcade.World No The physics simulation.
scene Phaser.Scene No The scene this group belongs to.
children Array.< Phaser.GameObjects.GameObject > | Phaser.Types.GameObjects.Group.GroupConfig Phaser.Types.GameObjects.Group.GroupCreateConfig Yes
config Phaser.Types.GameObjects.Group.GroupConfig | Phaser.Types.GameObjects.Group.GroupCreateConfig Yes Settings for this group.
Scope : static
Extends
Phaser.GameObjects.Group
Phaser.Physics.Arcade.Components.Collision
Source: src/physics/arcade/StaticPhysicsGroup.js#L15
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Group :
active
children
classType
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
collisionCategory ​
collisionCategory: number ​
Description:
The Arcade Physics Static Group Collision Category.
This can be set to any valid collision bitfield value.
See the setCollisionCategory method for more details.
Source: src/physics/arcade/StaticPhysicsGroup.js#L110
Since: 3.70.0
collisionMask ​
collisionMask: number ​
Description:
The Arcade Physics Static Group Collision Mask.
See the setCollidesWith method for more details.
Source: src/physics/arcade/StaticPhysicsGroup.js#L123
Since: 3.70.0
physicsType ​
physicsType: number ​
Description:
The scene this group belongs to.
Source: src/physics/arcade/StaticPhysicsGroup.js#L100
Since: 3.0.0
type ​
type: string ​
Description:
A textual representation of this Game Object.
Used internally by Phaser but is available for your own custom classes to populate.
Overrides: Phaser.GameObjects.Group#type
Source: src/physics/arcade/StaticPhysicsGroup.js#L136
Since: 3.21.0
world ​
world: Phaser.Physics.Arcade.World ​
Description:
The physics simulation.
Source: src/physics/arcade/StaticPhysicsGroup.js#L91
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
Adds a static physics body to the new group member (if it lacks one) and adds it to the simulation.
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The new group member.
Source: src/physics/arcade/StaticPhysicsGroup.js#L148
Since: 3.0.0
createMultipleCallbackHandler ​
<instance> createMultipleCallbackHandler(entries) ​
Description:
Refreshes the group.
Parameters:
name type optional description
entries Array.< Phaser.GameObjects.GameObject > No The newly created group members.
Source: src/physics/arcade/StaticPhysicsGroup.js#L184
Since: 3.0.0
refresh ​
<instance> refresh() ​
Description:
Resets each Body to the position of its parent Game Object.
Body sizes aren't changed (use Phaser.Physics.Arcade.Components.Enable#refreshBody for that).
Returns: Phaser.Physics.Arcade.StaticGroup - This group.
Source: src/physics/arcade/StaticPhysicsGroup.js#L199
Since: 3.0.0
removeCallbackHandler ​
<instance> removeCallbackHandler(child) ​
Description:
Disables the group member's physics body, removing it from the simulation.
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The group member being removed.
Source: src/physics/arcade/StaticPhysicsGroup.js#L166
Since: 3.0.0
Previous
StaticBody
Next
World
Inherited Members
Public Members
collisionCategory
collisionMask
physicsType
type
world
Inherited Methods
Public Methods
createCallbackHandler
createMultipleCallbackHandler
refresh
removeCallbackHandler
