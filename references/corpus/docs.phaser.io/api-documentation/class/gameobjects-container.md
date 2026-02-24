# Container | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-container

Phaser API Documentation
Class
Container
Version: Phaser v3.90.0
On this page
Container
A Container Game Object.
A Container, as the name implies, can 'contain' other types of Game Object.
When a Game Object is added to a Container, the Container becomes responsible for the rendering of it.
By default it will be removed from the Display List and instead added to the Containers own internal list.
The position of the Game Object automatically becomes relative to the position of the Container.
The transform point of a Container is 0x0 (in local space) and that cannot be changed. The children you add to the
Container should be positioned with this value in mind. I.e. you should treat 0x0 as being the center of
the Container, and position children positively and negative around it as required.
When the Container is rendered, all of its children are rendered as well, in the order in which they exist
within the Container. Container children can be repositioned using methods such as MoveUp , MoveDown and SendToBack .
If you modify a transform property of the Container, such as Container.x or Container.rotation then it will
automatically influence all children as well.
Containers can include other Containers for deeply nested transforms.
Containers can have masks set on them and can be used as a mask too. However, Container children cannot be masked.
The masks do not 'stack up'. Only a Container on the root of the display list will use its mask.
Containers can be enabled for input. Because they do not have a texture you need to provide a shape for them
to use as their hit area. Container children can also be enabled for input, independent of the Container.
If input enabling a child you should not set both the origin and a negative scale factor on the child,
or the input area will become misaligned.
Containers can be given a physics body for either Arcade Physics, Impact Physics or Matter Physics. However,
if Container children are enabled for physics you may get unexpected results, such as offset bodies,
if the Container itself, or any of its ancestors, is positioned anywhere other than at 0 x 0. Container children
with physics do not factor in the Container due to the excessive extra calculations needed. Please structure
your game to work around this.
It's important to understand the impact of using Containers. They add additional processing overhead into
every one of their children. The deeper you nest them, the more the cost escalates. This is especially true
for input events. You also lose the ability to set the display depth of Container children in the same
flexible manner as those not within them. In short, don't use them for the sake of it. You pay a small cost
every time you create one, try to structure your game around avoiding that where possible.
Constructor
new Container(scene, [x], [y], [children])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
children Array.< Phaser.GameObjects.GameObject > Yes An optional array of Game Objects to add to this Container.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.ComputedSize
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/container/Container.js#L21
Since: 3.4.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.ComputedSize :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
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
displayOriginX ​
displayOriginX: number ​
Description:
Internal value to allow Containers to be used for input and physics.
Do not change this value. It has no effect other than to break things.
Source: src/gameobjects/container/Container.js#L289
Since: 3.4.0
displayOriginY ​
displayOriginY: number ​
Description:
Internal value to allow Containers to be used for input and physics.
Do not change this value. It has no effect other than to break things.
Source: src/gameobjects/container/Container.js#L308
Since: 3.4.0
exclusive ​
exclusive: boolean ​
Description:
Does this Container exclusively manage its children?
The default is true which means a child added to this Container cannot
belong in another Container, which includes the Scene display list.
If you disable this then this Container will no longer exclusively manage its children.
This allows you to create all kinds of interesting graphical effects, such as replicating
Game Objects without reparenting them all over the Scene.
However, doing so will prevent children from receiving any kind of input event or have
their physics bodies work by default, as they're no longer a single entity on the
display list, but are being replicated where-ever this Container is.
Source: src/gameobjects/container/Container.js#L115
Since: 3.4.0
first ​
first: Phaser.GameObjects.GameObject ​
Description:
Returns the first Game Object within the Container, or null if it is empty.
You can move the cursor by calling Container.next and Container.previous .
Source: src/gameobjects/container/Container.js#L1322
Since: 3.4.0
last ​
last: Phaser.GameObjects.GameObject ​
Description:
Returns the last Game Object within the Container, or null if it is empty.
You can move the cursor by calling Container.next and Container.previous .
Source: src/gameobjects/container/Container.js#L1350
Since: 3.4.0
length ​
length: number ​
Description:
The number of Game Objects inside this Container.
Source: src/gameobjects/container/Container.js#L1305
Since: 3.4.0
list ​
list: Array.< Phaser.GameObjects.GameObject > ​
Description:
An array holding the children of this Container.
Source: src/gameobjects/container/Container.js#L106
Since: 3.4.0
localTransform ​
localTransform: Phaser.GameObjects.Components.TransformMatrix ​
Description:
Internal Transform Matrix used for local space conversion.
Source: src/gameobjects/container/Container.js#L156
Since: 3.4.0
maxSize ​
maxSize: number ​
Description:
Containers can have an optional maximum size. If set to anything above 0 it
will constrict the addition of new Game Objects into the Container, capping off
the maximum limit the Container can grow in size to.
Source: src/gameobjects/container/Container.js#L135
Since: 3.4.0
next ​
next: Phaser.GameObjects.GameObject ​
Description:
Returns the next Game Object within the Container, or null if it is empty.
You can move the cursor by calling Container.next and Container.previous .
Source: src/gameobjects/container/Container.js#L1378
Since: 3.4.0
originX ​
originX: number ​
Description:
Internal value to allow Containers to be used for input and physics.
Do not change this value. It has no effect other than to break things.
Source: src/gameobjects/container/Container.js#L251
Since: 3.4.0
originY ​
originY: number ​
Description:
Internal value to allow Containers to be used for input and physics.
Do not change this value. It has no effect other than to break things.
Source: src/gameobjects/container/Container.js#L270
Since: 3.4.0
position ​
position: number ​
Description:
The cursor position.
Source: src/gameobjects/container/Container.js#L147
Since: 3.4.0
previous ​
previous: Phaser.GameObjects.GameObject ​
Description:
Returns the previous Game Object within the Container, or null if it is empty.
You can move the cursor by calling Container.next and Container.previous .
Source: src/gameobjects/container/Container.js#L1406
Since: 3.4.0
scrollFactorX ​
scrollFactorX: number ​
Description:
The horizontal scroll factor of this Container.
The scroll factor controls the influence of the movement of a Camera upon this Container.
When a camera scrolls it will change the location at which this Container is rendered on-screen.
It does not change the Containers actual position values.
For a Container, setting this value will only update the Container itself, not its children.
If you wish to change the scrollFactor of the children as well, use the setScrollFactor method.
A value of 1 means it will move exactly in sync with a camera.
A value of 0 means it will not move at all, even if the camera moves.
Other values control the degree to which the camera movement is mapped to this Container.
Please be aware that scroll factor values other than 1 are not taken in to consideration when
calculating physics collisions. Bodies always collide based on their world position, but changing
the scroll factor is a visual adjustment to where the textures are rendered, which can offset
them from physics bodies if not accounted for in your code.
Source: src/gameobjects/container/Container.js#L185
Since: 3.4.0
scrollFactorY ​
scrollFactorY: number ​
Description:
The vertical scroll factor of this Container.
The scroll factor controls the influence of the movement of a Camera upon this Container.
When a camera scrolls it will change the location at which this Container is rendered on-screen.
It does not change the Containers actual position values.
For a Container, setting this value will only update the Container itself, not its children.
If you wish to change the scrollFactor of the children as well, use the setScrollFactor method.
A value of 1 means it will move exactly in sync with a camera.
A value of 0 means it will not move at all, even if the camera moves.
Other values control the degree to which the camera movement is mapped to this Container.
Please be aware that scroll factor values other than 1 are not taken in to consideration when
calculating physics collisions. Bodies always collide based on their world position, but changing
the scroll factor is a visual adjustment to where the textures are rendered, which can offset
them from physics bodies if not accounted for in your code.
Source: src/gameobjects/container/Container.js#L212
Since: 3.4.0
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
From Phaser.GameObjects.Components.ComputedSize :
setDisplaySize
setSize
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
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
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
Public Methods ​
add ​
<instance> add(child) ​
Description:
Adds the given Game Object, or array of Game Objects, to this Container.
Each Game Object must be unique within the Container.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No The Game Object, or array of Game Objects, to add to the Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L526
Since: 3.4.0
addAt ​
<instance> addAt(child, [index]) ​
Description:
Adds the given Game Object, or array of Game Objects, to this Container at the specified position.
Existing Game Objects in the Container are shifted up.
Each Game Object must be unique within the Container.
Tags:
generic
genericUse
Parameters:
name type optional default description
child Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No The Game Object, or array of Game Objects, to add to the Container.
index number Yes 0 The position to insert the Game Object/s at.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L548
Since: 3.4.0
bringToTop ​
<instance> bringToTop(child) ​
Description:
Brings the given Game Object to the top of this Container.
This will cause it to render on-top of any other objects in the Container.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object to bring to the top of the Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L989
Since: 3.4.0
count ​
<instance> count(property, value, [startIndex], [endIndex]) ​
Description:
Returns the total number of Game Objects in this Container that have a property
matching the given value.
For example: count('visible', true) would count all the elements that have their visible property set.
You can optionally limit the operation to the startIndex - endIndex range.
Parameters:
name type optional default description
property string No The property to check.
value any No The value to check.
startIndex number Yes 0 An optional start index to search from.
endIndex number Yes "Container.length" An optional end index to search up to (but not included)
Returns: number - The total number of Game Objects in this Container with a property matching the given value.
Source: src/gameobjects/container/Container.js#L740
Since: 3.4.0
each ​
<instance> each(callback, [context], [args]) ​
Description:
Passes all Game Objects in this Container to the given callback.
A copy of the Container is made before passing each entry to your callback.
This protects against the callback itself modifying the Container.
If you know for sure that the callback will not change the size of this Container
then you can use the more performant Container.iterate method instead.
Parameters:
name type optional description
callback function No The function to call.
context object Yes Value to use as this when executing callback.
args * Yes Additional arguments that will be passed to the callback, after the child.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1187
Since: 3.4.0
exists ​
<instance> exists(child) ​
Description:
Returns true if the given Game Object is a direct child of this Container.
This check does not scan nested Containers.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object to check for within this Container.
Returns: boolean - True if the Game Object is an immediate child of this Container, otherwise false.
Source: src/gameobjects/container/Container.js#L1135
Since: 3.4.0
getAll ​
<instance> getAll([property], [value], [startIndex], [endIndex]) ​
Description:
Returns all Game Objects in this Container.
You can optionally specify a matching criteria using the property and value arguments.
For example: getAll('body') would return only Game Objects that have a body property.
You can also specify a value to compare the property to:
getAll('visible', true) would return only Game Objects that have their visible property set to true .
Optionally you can specify a start and end index. For example if this Container had 100 Game Objects,
and you set startIndex to 0 and endIndex to 50, it would return matches from only
the first 50 Game Objects.
Tags:
generic
genericUse
Parameters:
name type optional default description
property string Yes The property to test on each Game Object in the Container.
value any Yes If property is set then the property must strictly equal this value to be included in the results.
startIndex number Yes 0 An optional start index to search from.
endIndex number Yes "Container.length" An optional end index to search up to (but not included)
Returns: Array.< Phaser.GameObjects.GameObject > - An array of matching Game Objects from this Container.
Source: src/gameobjects/container/Container.js#L707
Since: 3.4.0
getAt ​
<instance> getAt(index) ​
Description:
Returns the Game Object at the given position in this Container.
Tags:
generic
genericUse
Parameters:
name type optional description
index number No The position to get the Game Object from.
Returns: Phaser.GameObjects.GameObject - The Game Object at the specified index, or null if none found.
Source: src/gameobjects/container/Container.js#L573
Since: 3.4.0
getBounds ​
<instance> getBounds([output]) ​
Description:
Gets the bounds of this Container. It works by iterating all children of the Container,
getting their respective bounds, and then working out a min-max rectangle from that.
It does not factor in if the children render or not, all are included.
Some children are unable to return their bounds, such as Graphics objects, in which case
they are skipped.
Depending on the quantity of children in this Container it could be a really expensive call,
so cache it and only poll it as needed.
The values are stored and returned in a Rectangle object.
Parameters:
name type optional description
output Phaser.Geom.Rectangle Yes A Geom.Rectangle object to store the values in. If not provided a new Rectangle will be created.
Returns: Phaser.Geom.Rectangle - The values stored in the output object.
Source: src/gameobjects/container/Container.js#L356
Since: 3.4.0
getBoundsTransformMatrix ​
<instance> getBoundsTransformMatrix() ​
Description:
Returns the world transform matrix as used for Bounds checks.
The returned matrix is temporal and shouldn't be stored.
Returns: Phaser.GameObjects.Components.TransformMatrix - The world transform matrix.
Source: src/gameobjects/container/Container.js#L511
Since: 3.4.0
getByName ​
<instance> getByName(name) ​
Description:
Searches for the first instance of a child with its name property matching the given argument.
Should more than one child have the same name only the first is returned.
Tags:
generic
genericUse
Parameters:
name type optional description
name string No The name to search for.
Returns: Phaser.GameObjects.GameObject - The first child with a matching name, or null if none were found.
Source: src/gameobjects/container/Container.js#L641
Since: 3.4.0
getFirst ​
<instance> getFirst(property, value, [startIndex], [endIndex]) ​
Description:
Gets the first Game Object in this Container.
You can also specify a property and value to search for, in which case it will return the first
Game Object in this Container with a matching property and / or value.
For example: getFirst('visible', true) would return the first Game Object that had its visible property set.
You can limit the search to the startIndex - endIndex range.
Tags:
generic
genericUse
Parameters:
name type optional default description
property string No The property to test on each Game Object in the Container.
value * No The value to test the property against. Must pass a strict ( === ) comparison check.
startIndex number Yes 0 An optional start index to search from.
endIndex number Yes "Container.length" An optional end index to search up to (but not included)
Returns: Phaser.GameObjects.GameObject - The first matching Game Object, or null if none was found.
Source: src/gameobjects/container/Container.js#L679
Since: 3.4.0
getIndex ​
<instance> getIndex(child) ​
Description:
Returns the index of the given Game Object in this Container.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object to search for in this Container.
Returns: number - The index of the Game Object in this Container, or -1 if not found.
Source: src/gameobjects/container/Container.js#L591
Since: 3.4.0
getRandom ​
<instance> getRandom([startIndex], [length]) ​
Description:
Returns a random Game Object from this Container.
Tags:
generic
genericUse
Parameters:
name type optional default description
startIndex number Yes 0 An optional start index.
length number Yes An optional length, the total number of elements (from the startIndex) to choose from.
Returns: Phaser.GameObjects.GameObject - A random child from the Container, or null if the Container is empty.
Source: src/gameobjects/container/Container.js#L660
Since: 3.4.0
iterate ​
<instance> iterate(callback, [context], [args]) ​
Description:
Passes all Game Objects in this Container to the given callback.
Only use this method when you absolutely know that the Container will not be modified during
the iteration, i.e. by removing or adding to its contents.
Parameters:
name type optional description
callback function No The function to call.
context object Yes Value to use as this when executing callback.
args * Yes Additional arguments that will be passed to the callback, after the child.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1227
Since: 3.4.0
moveAbove ​
<instance> moveAbove(child1, child2) ​
Description:
Moves a Game Object above another one within this Container.
If the Game Object is already above the other, it isn't moved.
These 2 Game Objects must already be children of this Container.
Tags:
generic
genericUse
Parameters:
name type optional description
child1 Phaser.GameObjects.GameObject No The Game Object to move above base Game Object.
child2 Phaser.GameObjects.GameObject No The base Game Object.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L811
Since: 3.55.0
moveBelow ​
<instance> moveBelow(child1, child2) ​
Description:
Moves a Game Object below another one within this Container.
If the Game Object is already below the other, it isn't moved.
These 2 Game Objects must already be children of this Container.
Tags:
generic
genericUse
Parameters:
name type optional description
child1 Phaser.GameObjects.GameObject No The Game Object to move below base Game Object.
child2 Phaser.GameObjects.GameObject No The base Game Object.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L835
Since: 3.55.0
moveDown ​
<instance> moveDown(child) ​
Description:
Moves the given Game Object down one place in this Container, unless it's already at the bottom.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object to be moved in the Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1051
Since: 3.4.0
moveTo ​
<instance> moveTo(child, index) ​
Description:
Moves a Game Object to a new position within this Container.
The Game Object must already be a child of this Container.
The Game Object is removed from its old position and inserted into the new one.
Therefore the Container size does not change. Other children will change position accordingly.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object to move.
index number No The new position of the Game Object in this Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L785
Since: 3.4.0
moveUp ​
<instance> moveUp(child) ​
Description:
Moves the given Game Object up one place in this Container, unless it's already at the top.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object to be moved in the Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1031
Since: 3.4.0
onChildDestroyed ​
<instance> onChildDestroyed() ​
Description:
Internal handler, called when a child is destroyed.
Access: protected
Source: src/gameobjects/container/Container.js#L1450
Since: 3.80.0
pointToContainer ​
<instance> pointToContainer(source, [output]) ​
Description:
Takes a Point-like object, such as a Vector2, Geom.Point or object with public x and y properties,
and transforms it into the space of this Container, then returns it in the output object.
Parameters:
name type optional description
source Phaser.Types.Math.Vector2Like No The Source Point to be transformed.
output Phaser.Types.Math.Vector2Like Yes A destination object to store the transformed point in. If none given a Vector2 will be created and returned.
Returns: Phaser.Types.Math.Vector2Like - The transformed point.
Source: src/gameobjects/container/Container.js#L473
Since: 3.4.0
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/container/Container.js#L1434
Since: 3.9.0
remove ​
<instance> remove(child, [destroyChild]) ​
Description:
Removes the given Game Object, or array of Game Objects, from this Container.
The Game Objects must already be children of this Container.
You can also optionally call destroy on each Game Object that is removed from the Container.
Tags:
generic
genericUse
Parameters:
name type optional default description
child Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No The Game Object, or array of Game Objects, to be removed from the Container.
destroyChild boolean Yes false Optionally call destroy on each child successfully removed from this Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L859
Since: 3.4.0
removeAll ​
<instance> removeAll([destroyChild]) ​
Description:
Removes all Game Objects from this Container.
You can also optionally call destroy on each Game Object that is removed from the Container.
Parameters:
name type optional default description
destroyChild boolean Yes false Optionally call destroy on each Game Object successfully removed from this Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L951
Since: 3.4.0
removeAt ​
<instance> removeAt(index, [destroyChild]) ​
Description:
Removes the Game Object at the given position in this Container.
You can also optionally call destroy on the Game Object, if one is found.
Parameters:
name type optional default description
index number No The index of the Game Object to be removed.
destroyChild boolean Yes false Optionally call destroy on the Game Object if successfully removed from this Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L897
Since: 3.4.0
removeBetween ​
<instance> removeBetween([startIndex], [endIndex], [destroyChild]) ​
Description:
Removes the Game Objects between the given positions in this Container.
You can also optionally call destroy on each Game Object that is removed from the Container.
Parameters:
name type optional default description
startIndex number Yes 0 An optional start index to search from.
endIndex number Yes "Container.length" An optional end index to search up to (but not included)
destroyChild boolean Yes false Optionally call destroy on each Game Object successfully removed from this Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L922
Since: 3.4.0
replace ​
<instance> replace(oldChild, newChild, [destroyChild]) ​
Description:
Replaces a Game Object in this Container with the new Game Object.
The new Game Object cannot already be a child of this Container.
Tags:
generic
genericUse
Parameters:
name type optional default description
oldChild Phaser.GameObjects.GameObject No The Game Object in this Container that will be replaced.
newChild Phaser.GameObjects.GameObject No The Game Object to be added to this Container.
destroyChild boolean Yes false Optionally call destroy on the Game Object if successfully removed from this Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1101
Since: 3.4.0
reverse ​
<instance> reverse() ​
Description:
Reverses the order of all Game Objects in this Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1071
Since: 3.4.0
sendToBack ​
<instance> sendToBack(child) ​
Description:
Sends the given Game Object to the bottom of this Container.
This will cause it to render below any other objects in the Container.
Tags:
generic
genericUse
Parameters:
name type optional description
child Phaser.GameObjects.GameObject No The Game Object to send to the bottom of the Container.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1010
Since: 3.4.0
setAll ​
<instance> setAll(property, value, [startIndex], [endIndex]) ​
Description:
Sets the property to the given value on all Game Objects in this Container.
Optionally you can specify a start and end index. For example if this Container had 100 Game Objects,
and you set startIndex to 0 and endIndex to 50, it would return matches from only
the first 50 Game Objects.
Parameters:
name type optional default description
property string No The property that must exist on the Game Object.
value any No The value to get the property to.
startIndex number Yes 0 An optional start index to search from.
endIndex number Yes "Container.length" An optional end index to search up to (but not included)
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1155
Since: 3.4.0
setExclusive ​
<instance> setExclusive([value]) ​
Description:
Does this Container exclusively manage its children?
The default is true which means a child added to this Container cannot
belong in another Container, which includes the Scene display list.
If you disable this then this Container will no longer exclusively manage its children.
This allows you to create all kinds of interesting graphical effects, such as replicating
Game Objects without reparenting them all over the Scene.
However, doing so will prevent children from receiving any kind of input event or have
their physics bodies work by default, as they're no longer a single entity on the
display list, but are being replicated where-ever this Container is.
Parameters:
name type optional default description
value boolean Yes true The exclusive state of this Container.
Returns: Phaser.GameObjects.Container - This Container.
Source: src/gameobjects/container/Container.js#L327
Since: 3.4.0
setScrollFactor ​
<instance> setScrollFactor(x, [y], [updateChildren]) ​
Description:
Sets the scroll factor of this Container and optionally all of its children.
The scroll factor controls the influence of the movement of a Camera upon this Game Object.
When a camera scrolls it will change the location at which this Game Object is rendered on-screen.
It does not change the Game Objects actual position values.
A value of 1 means it will move exactly in sync with a camera.
A value of 0 means it will not move at all, even if the camera moves.
Other values control the degree to which the camera movement is mapped to this Game Object.
Please be aware that scroll factor values other than 1 are not taken in to consideration when
calculating physics collisions. Bodies always collide based on their world position, but changing
the scroll factor is a visual adjustment to where the textures are rendered, which can offset
them from physics bodies if not accounted for in your code.
Parameters:
name type optional default description
x number No The horizontal scroll factor of this Game Object.
y number Yes "x" The vertical scroll factor of this Game Object. If not set it will use the x value.
updateChildren boolean Yes false Apply this scrollFactor to all Container children as well?
Returns: Phaser.GameObjects.Container - This Game Object instance.
Source: src/gameobjects/container/Container.js#L1262
Since: 3.4.0
shuffle ​
<instance> shuffle() ​
Description:
Shuffles the all Game Objects in this Container using the Fisher-Yates implementation.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L1086
Since: 3.4.0
sort ​
<instance> sort(property, [handler]) ​
Description:
Sort the contents of this Container so the items are in order based on the given property.
For example: sort('alpha') would sort the elements based on the value of their alpha property.
Parameters:
name type optional description
property string No The property to lexically sort by.
handler function Yes Provide your own custom handler function. Will receive 2 children which it should compare and return a boolean.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L609
Since: 3.4.0
swap ​
<instance> swap(child1, child2) ​
Description:
Swaps the position of two Game Objects in this Container.
Both Game Objects must belong to this Container.
Tags:
generic
genericUse
Parameters:
name type optional description
child1 Phaser.GameObjects.GameObject No The first Game Object to swap.
child2 Phaser.GameObjects.GameObject No The second Game Object to swap.
Returns: Phaser.GameObjects.Container - This Container instance.
Source: src/gameobjects/container/Container.js#L763
Since: 3.4.0
Previous
TransformMatrix
Next
Curve
Inherited Members
Public Members
displayOriginX
displayOriginY
exclusive
first
last
length
list
localTransform
maxSize
next
originX
originY
position
previous
scrollFactorX
scrollFactorY
Inherited Methods
Public Methods
add
addAt
bringToTop
count
each
exists
getAll
getAt
getBounds
getBoundsTransformMatrix
getByName
getFirst
getIndex
getRandom
iterate
moveAbove
moveBelow
moveDown
moveTo
moveUp
onChildDestroyed
pointToContainer
preDestroy
remove
removeAll
removeAt
removeBetween
replace
reverse
sendToBack
setAll
setExclusive
setScrollFactor
shuffle
sort
swap
