# Blitter | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-blitter

Phaser API Documentation
Class
Blitter
Version: Phaser v3.90.0
On this page
Blitter
A Blitter Game Object.
The Blitter Game Object is a special kind of container that creates, updates and manages Bob objects.
Bobs are designed for rendering speed rather than flexibility. They consist of a texture, or frame from a texture,
a position and an alpha value. You cannot scale or rotate them. They use a batched drawing method for speed
during rendering.
A Blitter Game Object has one texture bound to it. Bobs created by the Blitter can use any Frame from this
Texture to render with, but they cannot use any other Texture. It is this single texture-bind that allows
them their speed.
If you have a need to blast a large volume of frames around the screen then Blitter objects are well worth
investigating. They are especially useful for using as a base for your own special effects systems.
Constructor
new Blitter(scene, [x], [y], [texture], [frame])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. It can only belong to one Scene at any given time.
x number Yes 0 The x coordinate of this Game Object in world space.
y number Yes 0 The y coordinate of this Game Object in world space.
texture string Yes "'__DEFAULT'" The key of the texture this Game Object will use for rendering. The Texture must already exist in the Texture Manager.
frame string | number Yes 0 The Frame of the Texture that this Game Object will use. Only set if the Texture has multiple frames, such as a Texture Atlas or Sprite Sheet.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Alpha
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Size
Phaser.GameObjects.Components.Texture
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/blitter/Blitter.js#L22
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
Public Members ​
children ​
children: Phaser.Structs.List.<Phaser.GameObjects.Bob> ​
Description:
The children of this Blitter.
This List contains all of the Bob objects created by the Blitter.
Source: src/gameobjects/blitter/Blitter.js#L92
Since: 3.0.0
dirty ​
dirty: boolean ​
Description:
Is the Blitter considered dirty?
A 'dirty' Blitter has had its child count changed since the last frame.
Source: src/gameobjects/blitter/Blitter.js#L114
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
setInteractive
setName
setState
toggleData
toJSON
update
willRender
Public Methods ​
childCanRender ​
<instance> childCanRender(child) ​
Description:
Checks if the given child can render or not, by checking its visible and alpha values.
Parameters:
name type optional description
child Phaser.GameObjects.Bob No The Bob to check for rendering.
Returns: boolean - Returns true if the given child can render, otherwise false .
Source: src/gameobjects/blitter/Blitter.js#L233
Since: 3.0.0
clear ​
<instance> clear() ​
Description:
Removes all Bobs from the children List and clears the dirty flag.
Source: src/gameobjects/blitter/Blitter.js#L268
Since: 3.0.0
create ​
<instance> create(x, y, [frame], [visible], [index]) ​
Description:
Creates a new Bob in this Blitter.
The Bob is created at the given coordinates, relative to the Blitter and uses the given frame.
A Bob can use any frame belonging to the texture bound to the Blitter.
Parameters:
name type optional default description
x number No The x position of the Bob. Bob coordinate are relative to the position of the Blitter object.
y number No The y position of the Bob. Bob coordinate are relative to the position of the Blitter object.
frame string | number Phaser.Textures.Frame Yes
visible boolean Yes true Should the created Bob render or not?
index number Yes The position in the Blitters Display List to add the new Bob at. Defaults to the top of the list.
Returns: Phaser.GameObjects.Bob - The newly created Bob object.
Source: src/gameobjects/blitter/Blitter.js#L125
Since: 3.0.0
createFromCallback ​
<instance> createFromCallback(callback, quantity, [frame], [visible]) ​
Description:
Creates multiple Bob objects within this Blitter and then passes each of them to the specified callback.
Parameters:
name type optional default description
callback CreateCallback No The callback to invoke after creating a bob. It will be sent two arguments: The Bob and the index of the Bob.
quantity number No The quantity of Bob objects to create.
frame string | number Phaser.Textures.Frame Array.<string> Array.<number>
visible boolean Yes true Should the created Bob render or not?
Returns: Array.< Phaser.GameObjects.Bob > - An array of Bob objects that were created.
Source: src/gameobjects/blitter/Blitter.js#L165
Since: 3.0.0
createMultiple ​
<instance> createMultiple(quantity, [frame], [visible]) ​
Description:
Creates multiple Bobs in one call.
The amount created is controlled by a combination of the quantity argument and the number of frames provided.
If the quantity is set to 10 and you provide 2 frames, then 20 Bobs will be created. 10 with the first
frame and 10 with the second.
Parameters:
name type optional default description
quantity number No The quantity of Bob objects to create.
frame string | number Phaser.Textures.Frame Array.<string> Array.<number>
visible boolean Yes true Should the created Bob render or not?
Returns: Array.< Phaser.GameObjects.Bob > - An array of Bob objects that were created.
Source: src/gameobjects/blitter/Blitter.js#L192
Since: 3.0.0
getRenderList ​
<instance> getRenderList() ​
Description:
Returns an array of Bobs to be rendered.
If the Blitter is dirty then a new list is generated and stored in renderList .
Returns: Array.< Phaser.GameObjects.Bob > - An array of Bob objects that will be rendered this frame.
Source: src/gameobjects/blitter/Blitter.js#L248
Since: 3.0.0
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/blitter/Blitter.js#L280
Since: 3.9.0
Previous
BitmapText
Next
Bob
Inherited Members
Public Members
children
dirty
Inherited Methods
Public Methods
childCanRender
clear
create
createFromCallback
createMultiple
getRenderList
preDestroy
