# Group | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-group

Phaser API Documentation
Class
Group
Version: Phaser v3.90.0
On this page
Group
A Group is a way for you to create, manipulate, or recycle similar Game Objects.
Group membership is non-exclusive. A Game Object can belong to several groups, one group, or none.
Groups themselves aren't displayable, and can't be positioned, rotated, scaled, or hidden.
Constructor
new Group(scene, [children], [config])
Parameters
name type optional description
scene Phaser.Scene No The scene this group belongs to.
children Array.< Phaser.GameObjects.GameObject > | Phaser.Types.GameObjects.Group.GroupConfig Phaser.Types.GameObjects.Group.GroupCreateConfig Yes
config Phaser.Types.GameObjects.Group.GroupConfig | Phaser.Types.GameObjects.Group.GroupCreateConfig Yes Settings for this group. If key is set, Phaser.GameObjects.Group#createMultiple is also called with these settings.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/gameobjects/group/Group.js#L20
Since: 3.0.0
Public Members ​
active ​
active: boolean ​
Description:
Whether this group runs its Phaser.GameObjects.Group#preUpdate method (which may update any members).
Source: src/gameobjects/group/Group.js#L147
Since: 3.0.0
children ​
children: Phaser.Structs.Set.<Phaser.GameObjects.GameObject> ​
Description:
Members of this group.
Source: src/gameobjects/group/Group.js#L95
Since: 3.0.0
classType ​
classType: function ​
Description:
The class to create new group members from.
Source: src/gameobjects/group/Group.js#L125
Since: 3.0.0
createCallback ​
createCallback: Phaser.Types.GameObjects.Group.GroupCallback ​
Description:
A function to be called when adding or creating group members.
Source: src/gameobjects/group/Group.js#L198
Since: 3.0.0
createMultipleCallback ​
createMultipleCallback: Phaser.Types.GameObjects.Group.GroupMultipleCreateCallback ​
Description:
A function to be called when creating several group members at once.
Source: src/gameobjects/group/Group.js#L216
Since: 3.0.0
defaultFrame ​
defaultFrame: string, number ​
Description:
A default texture frame to use when creating new group members.
Source: src/gameobjects/group/Group.js#L178
Since: 3.0.0
defaultKey ​
defaultKey: string ​
Description:
A default texture key to use when creating new group members.
This is used in Phaser.GameObjects.Group#create
but not in Phaser.GameObjects.Group#createMultiple .
Source: src/gameobjects/group/Group.js#L166
Since: 3.0.0
isParent ​
isParent: boolean ​
Description:
A flag identifying this object as a group.
Source: src/gameobjects/group/Group.js#L104
Since: 3.0.0
maxSize ​
maxSize: number ​
Description:
The maximum size of this group, if used as a pool. -1 is no limit.
Source: src/gameobjects/group/Group.js#L156
Since: 3.0.0
name ​
name: string ​
Description:
The name of this group.
Empty by default and never populated by Phaser, this is left for developers to use.
Source: src/gameobjects/group/Group.js#L136
Since: 3.18.0
removeCallback ​
removeCallback: Phaser.Types.GameObjects.Group.GroupCallback ​
Description:
A function to be called when removing group members.
Source: src/gameobjects/group/Group.js#L207
Since: 3.0.0
runChildUpdate ​
runChildUpdate: boolean ​
Description:
Whether to call the update method of any members.
Source: src/gameobjects/group/Group.js#L187
Since: 3.0.0
scene ​
scene: Phaser.Scene ​
Description:
This scene this group belongs to.
Source: src/gameobjects/group/Group.js#L86
Since: 3.0.0
type ​
type: string ​
Description:
A textual representation of this Game Object.
Used internally by Phaser but is available for your own custom classes to populate.
Source: src/gameobjects/group/Group.js#L114
Since: 3.21.0
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
Public Methods ​
add ​
<instance> add(child, [addToScene]) ​
Description:
Adds a Game Object to this group.
Calls Phaser.GameObjects.Group#createCallback .
Parameters:
name type optional default description
child Phaser.GameObjects.GameObject No The Game Object to add.
addToScene boolean Yes false Also add the Game Object to the scene.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L575
Since: 3.0.0
addMultiple ​
<instance> addMultiple(children, [addToScene]) ​
Description:
Adds several Game Objects to this group.
Calls Phaser.GameObjects.Group#createCallback .
Parameters:
name type optional default description
children Array.< Phaser.GameObjects.GameObject > No The Game Objects to add.
addToScene boolean Yes false Also add the Game Objects to the scene.
Returns: Phaser.GameObjects.Group - This group.
Source: src/gameobjects/group/Group.js#L620
Since: 3.0.0
angle ​
<instance> angle(value, [step]) ​
Description:
Sets the angle of each group member.
Parameters:
name type optional default description
value number No The amount to set the angle to, in degrees.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1392
Since: 3.21.0
clear ​
<instance> clear([removeFromScene], [destroyChild]) ​
Description:
Removes all members of this Group and optionally removes them from the Scene and / or destroys them.
Does not call Phaser.GameObjects.Group#removeCallback .
Parameters:
name type optional default description
removeFromScene boolean Yes false Optionally remove each Group member from the Scene.
destroyChild boolean Yes false Optionally call destroy on the removed Group members.
Returns: Phaser.GameObjects.Group - This group.
Source: src/gameobjects/group/Group.js#L699
Since: 3.0.0
contains ​
<instance> contains(child) ​
Description:
Tests if a Game Object is a member of this group.
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No A Game Object.
Returns: boolean - True if the Game Object is a member of this group.
Source: src/gameobjects/group/Group.js#L741
Since: 3.0.0
countActive ​
<instance> countActive([value]) ​
Description:
Counts the number of active (or inactive) group members.
Parameters:
name type optional default description
value boolean Yes true Count active (true) or inactive (false) group members.
Returns: number - The number of group members with an active state matching the active argument.
Source: src/gameobjects/group/Group.js#L1122
Since: 3.0.0
create ​
<instance> create([x], [y], [key], [frame], [visible], [active]) ​
Description:
Creates a new Game Object and adds it to this group, unless the group is .
Calls Phaser.GameObjects.Group#createCallback .
Parameters:
name type optional default description
x number Yes 0 The horizontal position of the new Game Object in the world.
y number Yes 0 The vertical position of the new Game Object in the world.
key string Yes "defaultKey" The texture key of the new Game Object.
frame string | number Yes "defaultFrame" The texture frame of the new Game Object.
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of the new Game Object.
active boolean Yes true The {@link Phaser.GameObjects.GameObject#active} state of the new Game Object.
Returns: any - The new Game Object (usually a Sprite, etc.).
Source: src/gameobjects/group/Group.js#L273
Since: 3.0.0
createFromConfig ​
<instance> createFromConfig(options) ​
Description:
A helper for Phaser.GameObjects.Group#createMultiple .
Parameters:
name type optional description
options Phaser.Types.GameObjects.Group.GroupCreateConfig No Creation settings.
Returns: Array.<any> - The newly created Game Objects.
Source: src/gameobjects/group/Group.js#L359
Since: 3.0.0
createMultiple ​
<instance> createMultiple(config) ​
Description:
Creates several Game Objects and adds them to this group.
If the group becomes Phaser.GameObjects.Group#isFull , no further Game Objects are created.
Calls Phaser.GameObjects.Group#createMultipleCallback and Phaser.GameObjects.Group#createCallback .
Parameters:
name type optional description
config Phaser.Types.GameObjects.Group.GroupCreateConfig | Array.< Phaser.Types.GameObjects.Group.GroupCreateConfig > No Creation settings. This can be a single configuration object or an array of such objects, which will be applied in turn.
Returns: Array.<any> - The newly created Game Objects.
Source: src/gameobjects/group/Group.js#L318
Since: 3.0.0
destroy ​
<instance> destroy([destroyChildren], [removeFromScene]) ​
Description:
Empties this Group of all children and removes it from the Scene.
Does not call Phaser.GameObjects.Group#removeCallback .
Children of this Group will not be removed from the Scene by calling this method
unless you specify the removeFromScene parameter.
Children of this Group will also not be destroyed by calling this method
unless you specify the destroyChildren parameter.
Parameters:
name type optional default description
destroyChildren boolean Yes false Also {@link Phaser.GameObjects.GameObject#destroy} each Group member.
removeFromScene boolean Yes false Optionally remove each Group member from the Scene.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/gameobjects/group/Group.js#L1714
Since: 3.0.0
get ​
<instance> get([x], [y], [key], [frame], [visible]) ​
Description:
Scans the group for the first member that has an Phaser.GameObjects.GameObject#active state set to false ,
assigns x and y , and returns the member.
If no inactive member is found and the group isn't full then it will create a new Game Object using x , y , key , frame , and visible .
The new Game Object will have its active state set to true .
Unless a new member is created, key , frame , and visible are ignored.
Parameters:
name type optional default description
x number Yes The horizontal position of the Game Object in the world.
y number Yes The vertical position of the Game Object in the world.
key string Yes "defaultKey" The texture key assigned to a new Game Object (if one is created).
frame string | number Yes "defaultFrame" A texture frame assigned to a new Game Object (if one is created).
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created).
Returns: any - The first inactive group member, or a newly created member, or null.
Source: src/gameobjects/group/Group.js#L1011
Since: 3.0.0
getChildren ​
<instance> getChildren() ​
Description:
All members of the group.
Returns: Array.< Phaser.GameObjects.GameObject > - The group members.
Source: src/gameobjects/group/Group.js#L756
Since: 3.0.0
getFirst ​
<instance> getFirst([state], [createIfNull], [x], [y], [key], [frame], [visible]) ​
Description:
Scans the Group, from top to bottom, for the first member that has an Phaser.GameObjects.GameObject#active state matching the argument,
assigns x and y , and returns the member.
If no matching member is found and createIfNull is true and the group isn't full then it will create a new Game Object using x , y , key , frame , and visible .
Unless a new member is created, key , frame , and visible are ignored.
Parameters:
name type optional default description
state boolean Yes false The {@link Phaser.GameObjects.GameObject#active} value to match.
createIfNull boolean Yes false Create a new Game Object if no matching members are found, using the following arguments.
x number Yes The horizontal position of the Game Object in the world.
y number Yes The vertical position of the Game Object in the world.
key string Yes "defaultKey" The texture key assigned to a new Game Object (if one is created).
frame string | number Yes "defaultFrame" A texture frame assigned to a new Game Object (if one is created).
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created).
Returns: any - The first matching group member, or a newly created member, or null.
Source: src/gameobjects/group/Group.js#L806
Since: 3.0.0
getFirstAlive ​
<instance> getFirstAlive([createIfNull], [x], [y], [key], [frame], [visible]) ​
Description:
Scans the group for the first member that has an Phaser.GameObjects.GameObject#active state set to true ,
assigns x and y , and returns the member.
If no active member is found and createIfNull is true and the group isn't full then it will create a new one using x , y , key , frame , and visible .
Unless a new member is created, key , frame , and visible are ignored.
Parameters:
name type optional default description
createIfNull boolean Yes false Create a new Game Object if no matching members are found, using the following arguments.
x number Yes The horizontal position of the Game Object in the world.
y number Yes The vertical position of the Game Object in the world.
key string Yes "defaultKey" The texture key assigned to a new Game Object (if one is created).
frame string | number Yes "defaultFrame" A texture frame assigned to a new Game Object (if one is created).
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created).
Returns: any - The first active group member, or a newly created member, or null.
Source: src/gameobjects/group/Group.js#L1035
Since: 3.0.0
getFirstDead ​
<instance> getFirstDead([createIfNull], [x], [y], [key], [frame], [visible]) ​
Description:
Scans the group for the first member that has an Phaser.GameObjects.GameObject#active state set to false ,
assigns x and y , and returns the member.
If no inactive member is found and createIfNull is true and the group isn't full then it will create a new one using x , y , key , frame , and visible .
The new Game Object will have an active state set to true .
Unless a new member is created, key , frame , and visible are ignored.
Parameters:
name type optional default description
createIfNull boolean Yes false Create a new Game Object if no matching members are found, using the following arguments.
x number Yes The horizontal position of the Game Object in the world.
y number Yes The vertical position of the Game Object in the world.
key string Yes "defaultKey" The texture key assigned to a new Game Object (if one is created).
frame string | number Yes "defaultFrame" A texture frame assigned to a new Game Object (if one is created).
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created).
Returns: any - The first inactive group member, or a newly created member, or null.
Source: src/gameobjects/group/Group.js#L1059
Since: 3.0.0
getFirstNth ​
<instance> getFirstNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible]) ​
Description:
Scans the Group, from top to bottom, for the nth member that has an Phaser.GameObjects.GameObject#active state matching the argument,
assigns x and y , and returns the member.
If no matching member is found and createIfNull is true and the group isn't full then it will create a new Game Object using x , y , key , frame , and visible .
Unless a new member is created, key , frame , and visible are ignored.
Parameters:
name type optional default description
nth number No The nth matching Group member to search for.
state boolean Yes false The {@link Phaser.GameObjects.GameObject#active} value to match.
createIfNull boolean Yes false Create a new Game Object if no matching members are found, using the following arguments.
x number Yes The horizontal position of the Game Object in the world.
y number Yes The vertical position of the Game Object in the world.
key string Yes "defaultKey" The texture key assigned to a new Game Object (if one is created).
frame string | number Yes "defaultFrame" A texture frame assigned to a new Game Object (if one is created).
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created).
Returns: any - The first matching group member, or a newly created member, or null.
Source: src/gameobjects/group/Group.js#L831
Since: 3.6.0
getLast ​
<instance> getLast([state], [createIfNull], [x], [y], [key], [frame], [visible]) ​
Description:
Scans the Group for the last member that has an Phaser.GameObjects.GameObject#active state matching the argument,
assigns x and y , and returns the member.
If no matching member is found and createIfNull is true and the group isn't full then it will create a new Game Object using x , y , key , frame , and visible .
Unless a new member is created, key , frame , and visible are ignored.
Parameters:
name type optional default description
state boolean Yes false The {@link Phaser.GameObjects.GameObject#active} value to match.
createIfNull boolean Yes false Create a new Game Object if no matching members are found, using the following arguments.
x number Yes The horizontal position of the Game Object in the world.
y number Yes The vertical position of the Game Object in the world.
key string Yes "defaultKey" The texture key assigned to a new Game Object (if one is created).
frame string | number Yes "defaultFrame" A texture frame assigned to a new Game Object (if one is created).
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created).
Returns: any - The first matching group member, or a newly created member, or null.
Source: src/gameobjects/group/Group.js#L857
Since: 3.6.0
getLastNth ​
<instance> getLastNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible]) ​
Description:
Scans the Group for the last nth member that has an Phaser.GameObjects.GameObject#active state matching the argument,
assigns x and y , and returns the member.
If no matching member is found and createIfNull is true and the group isn't full then it will create a new Game Object using x , y , key , frame , and visible .
Unless a new member is created, key , frame , and visible are ignored.
Parameters:
name type optional default description
nth number No The nth matching Group member to search for.
state boolean Yes false The {@link Phaser.GameObjects.GameObject#active} value to match.
createIfNull boolean Yes false Create a new Game Object if no matching members are found, using the following arguments.
x number Yes The horizontal position of the Game Object in the world.
y number Yes The vertical position of the Game Object in the world.
key string Yes "defaultKey" The texture key assigned to a new Game Object (if one is created).
frame string | number Yes "defaultFrame" A texture frame assigned to a new Game Object (if one is created).
visible boolean Yes true The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created).
Returns: any - The first matching group member, or a newly created member, or null.
Source: src/gameobjects/group/Group.js#L882
Since: 3.6.0
getLength ​
<instance> getLength() ​
Description:
The number of members of the group.
Returns: number - undefined
Source: src/gameobjects/group/Group.js#L769
Since: 3.0.0
getMatching ​
<instance> getMatching([property], [value], [startIndex], [endIndex]) ​
Description:
Returns all children in this Group that match the given criteria based on the property and value arguments.
For example: getMatching('visible', true) would return only children that have their visible property set.
Optionally, you can specify a start and end index. For example if the Group has 100 elements,
and you set startIndex to 0 and endIndex to 50, it would return matches from only
the first 50.
Parameters:
name type optional description
property string Yes The property to test on each array element.
value * Yes The value to test the property against. Must pass a strict ( === ) comparison check.
startIndex number Yes An optional start index to search from.
endIndex number Yes An optional end index to search to.
Returns: Array.<any> - An array of matching Group members. The array will be empty if nothing matched.
Source: src/gameobjects/group/Group.js#L782
Since: 3.50.0
getTotalFree ​
<instance> getTotalFree() ​
Description:
The difference of Phaser.GameObjects.Group#maxSize and the number of active group members.
This represents the number of group members that could be created or reactivated before reaching the size limit.
Returns: number - maxSize minus the number of active group numbers; or a large number (if maxSize is -1).
Source: src/gameobjects/group/Group.js#L1162
Since: 3.0.0
getTotalUsed ​
<instance> getTotalUsed() ​
Description:
Counts the number of in-use (active) group members.
Returns: number - The number of group members with an active state of true.
Source: src/gameobjects/group/Group.js#L1149
Since: 3.0.0
incX ​
<instance> incX(value, [step]) ​
Description:
Adds the given value to the x of each group member.
Parameters:
name type optional default description
value number No The amount to be added to the x property.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1314
Since: 3.21.0
incXY ​
<instance> incXY(x, [y], [stepX], [stepY]) ​
Description:
Adds the given value to the x, y of each group member.
Parameters:
name type optional default description
x number No The amount to be added to the x property.
y number Yes "x" The amount to be added to the y property. If undefined or null it uses the x value.
stepX number Yes 0 This is added to the x amount, multiplied by the iteration counter.
stepY number Yes 0 This is added to the y amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1350
Since: 3.21.0
incY ​
<instance> incY(value, [step]) ​
Description:
Adds the given value to the y of each group member.
Parameters:
name type optional default description
value number No The amount to be added to the y property.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1332
Since: 3.21.0
isFull ​
<instance> isFull() ​
Description:
Whether this group's size at its maximum .
Returns: boolean - True if the number of members equals {@link Phaser.GameObjects.Group#maxSize}.
Source: src/gameobjects/group/Group.js#L1102
Since: 3.0.0
kill ​
<instance> kill(gameObject) ​
Description:
Deactivates a member of this group.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No A member of this group.
Source: src/gameobjects/group/Group.js#L1647
Since: 3.0.0
killAndHide ​
<instance> killAndHide(gameObject) ​
Description:
Deactivates and hides a member of this group.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No A member of this group.
Source: src/gameobjects/group/Group.js#L1663
Since: 3.0.0
playAnimation ​
<instance> playAnimation(key, [startFrame]) ​
Description:
Plays an animation for all members of this group.
Parameters:
name type optional default description
key string No The string-based key of the animation to play.
startFrame string Yes 0 Optionally start the animation playing from this frame index.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1084
Since: 3.0.0
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
Updates any group members, if Phaser.GameObjects.Group#runChildUpdate is enabled.
Parameters:
name type optional description
time number No The current timestamp.
delta number No The delta time elapsed since the last frame.
Source: src/gameobjects/group/Group.js#L545
Since: 3.0.0
propertyValueInc ​
<instance> propertyValueInc(key, value, [step], [index], [direction]) ​
Description:
Adds the given value to the property as defined in key of each group member.
Parameters:
name type optional default description
key string No The property to be updated.
value number No The amount to set the property to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
index number Yes 0 An optional offset to start searching from within the items array.
direction number Yes 1 The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1237
Since: 3.21.0
propertyValueSet ​
<instance> propertyValueSet(key, value, [step], [index], [direction]) ​
Description:
Sets the property as defined in key of each group member to the given value.
Parameters:
name type optional default description
key string No The property to be updated.
value number No The amount to set the property to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
index number Yes 0 An optional offset to start searching from within the items array.
direction number Yes 1 The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1216
Since: 3.21.0
remove ​
<instance> remove(child, [removeFromScene], [destroyChild]) ​
Description:
Removes a member of this Group and optionally removes it from the Scene and / or destroys it.
Calls Phaser.GameObjects.Group#removeCallback .
Parameters:
name type optional default description
child Phaser.GameObjects.GameObject No The Game Object to remove.
removeFromScene boolean Yes false Optionally remove the Group member from the Scene it belongs to.
destroyChild boolean Yes false Optionally call destroy on the removed Group member.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L648
Since: 3.0.0
rotate ​
<instance> rotate(value, [step]) ​
Description:
Sets the rotation of each group member.
Parameters:
name type optional default description
value number No The amount to set the rotation to, in radians.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1410
Since: 3.21.0
rotateAround ​
<instance> rotateAround(point, angle) ​
Description:
Rotates each group member around the given point by the given angle.
Parameters:
name type optional description
point Phaser.Types.Math.Vector2Like No Any object with public x and y properties.
angle number No The angle to rotate by, in radians.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1428
Since: 3.21.0
rotateAroundDistance ​
<instance> rotateAroundDistance(point, angle, distance) ​
Description:
Rotates each group member around the given point by the given angle and distance.
Parameters:
name type optional description
point Phaser.Types.Math.Vector2Like No Any object with public x and y properties.
angle number No The angle to rotate by, in radians.
distance number No The distance from the point of rotation in pixels.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1446
Since: 3.21.0
scaleX ​
<instance> scaleX(value, [step]) ​
Description:
Sets the scaleX of each group member.
Parameters:
name type optional default description
value number No The amount to set the property to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1523
Since: 3.21.0
scaleXY ​
<instance> scaleXY(scaleX, [scaleY], [stepX], [stepY]) ​
Description:
Sets the scaleX, scaleY of each group member.
Parameters:
name type optional default description
scaleX number No The amount to be added to the scaleX property.
scaleY number Yes The amount to be added to the scaleY property. If undefined or null it uses the scaleX value.
stepX number Yes 0 This is added to the scaleX amount, multiplied by the iteration counter.
stepY number Yes 0 This is added to the scaleY amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1559
Since: 3.21.0
scaleY ​
<instance> scaleY(value, [step]) ​
Description:
Sets the scaleY of each group member.
Parameters:
name type optional default description
value number No The amount to set the property to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1541
Since: 3.21.0
setActive ​
<instance> setActive(value) ​
Description:
Sets the active property of this Group.
When active, this Group runs its preUpdate method.
Parameters:
name type optional description
value boolean No True if this Group should be set as active, false if not.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1180
Since: 3.24.0
setAlpha ​
<instance> setAlpha(value, [step]) ​
Description:
Sets the alpha of each group member.
Parameters:
name type optional default description
value number No The amount to set the alpha to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1465
Since: 3.21.0
setBlendMode ​
<instance> setBlendMode(value) ​
Description:
Sets the blendMode of each group member.
Parameters:
name type optional description
value number No The amount to set the property to.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1597
Since: 3.21.0
setDepth ​
<instance> setDepth(value, [step]) ​
Description:
Sets the depth of each group member.
Parameters:
name type optional default description
value number No The amount to set the property to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1579
Since: 3.0.0
setHitArea ​
<instance> setHitArea(hitArea, hitAreaCallback) ​
Description:
Passes all group members to the Input Manager to enable them for input with identical areas and callbacks.
Parameters:
name type optional description
hitArea * No Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not specified a Rectangle will be used.
hitAreaCallback Phaser.Types.Input.HitAreaCallback No A callback to be invoked when the Game Object is interacted with. If you provide a shape you must also provide a callback.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1614
Since: 3.21.0
setName ​
<instance> setName(value) ​
Description:
Sets the name property of this Group.
The name property is not populated by Phaser and is presented for your own use.
Parameters:
name type optional description
value string No The name to be given to this Group.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1198
Since: 3.24.0
setOrigin ​
<instance> setOrigin(originX, [originY], [stepX], [stepY]) ​
Description:
Sets the originX, originY of each group member.
Parameters:
name type optional default description
originX number No The amount to set the originX property to.
originY number Yes The amount to set the originY property to. If undefined or null it uses the originX value.
stepX number Yes 0 This is added to the originX amount, multiplied by the iteration counter.
stepY number Yes 0 This is added to the originY amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1503
Since: 3.21.0
setTint ​
<instance> setTint(topLeft, [topRight], [bottomLeft], [bottomRight]) ​
Description:
Sets the tint of each group member.
Parameters:
name type optional description
topLeft number No The tint being applied to top-left corner of item. If other parameters are given no value, this tint will be applied to whole item.
topRight number Yes The tint to be applied to top-right corner of item.
bottomLeft number Yes The tint to be applied to the bottom-left corner of item.
bottomRight number Yes The tint to be applied to the bottom-right corner of item.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1483
Since: 3.21.0
setVisible ​
<instance> setVisible(value, [index], [direction]) ​
Description:
Sets the visible of each group member.
Parameters:
name type optional default description
value boolean No The value to set the property to.
index number Yes 0 An optional offset to start searching from within the items array.
direction number Yes 1 The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1680
Since: 3.21.0
setX ​
<instance> setX(value, [step]) ​
Description:
Sets the x of each group member.
Parameters:
name type optional default description
value number No The amount to set the property to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1258
Since: 3.21.0
setXY ​
<instance> setXY(x, [y], [stepX], [stepY]) ​
Description:
Sets the x, y of each group member.
Parameters:
name type optional default description
x number No The amount to set the x property to.
y number Yes "x" The amount to set the y property to. If undefined or null it uses the x value.
stepX number Yes 0 This is added to the x amount, multiplied by the iteration counter.
stepY number Yes 0 This is added to the y amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1294
Since: 3.21.0
setY ​
<instance> setY(value, [step]) ​
Description:
Sets the y of each group member.
Parameters:
name type optional default description
value number No The amount to set the property to.
step number Yes 0 This is added to the value amount, multiplied by the iteration counter.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1276
Since: 3.21.0
shiftPosition ​
<instance> shiftPosition(x, y, [direction]) ​
Description:
Iterate through the group members changing the position of each element to be that of the element that came before
it in the array (or after it if direction = 1)
The first group member position is set to x/y.
Parameters:
name type optional default description
x number No The x coordinate to place the first item in the array at.
y number No The y coordinate to place the first item in the array at.
direction number Yes 0 The iteration direction. 0 = first to last and 1 = last to first.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1370
Since: 3.21.0
shuffle ​
<instance> shuffle() ​
Description:
Shuffles the group members in place.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1632
Since: 3.21.0
toggleVisible ​
<instance> toggleVisible() ​
Description:
Toggles (flips) the visible state of each member of this group.
Returns: Phaser.GameObjects.Group - This Group object.
Source: src/gameobjects/group/Group.js#L1699
Since: 3.0.0
Previous
Grid
Next
Image
Public Members
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
type
Inherited Methods
Public Methods
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
