# Grid | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-grid

Phaser API Documentation
Class
Grid
Version: Phaser v3.90.0
On this page
Grid
The Grid Shape is a Game Object that can be added to a Scene, Group or Container. You can
treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling
it for input or physics. It provides a quick and easy way for you to render this shape in your
game without using a texture, while still taking advantage of being fully batched in WebGL.
This shape supports only fill colors and cannot be stroked.
A Grid Shape allows you to display a grid in your game, where you can control the size of the
grid as well as the width and height of the grid cells. You can set a fill color for each grid
cell as well as an alternate fill color. When the alternate fill color is set then the grid
cells will alternate the fill colors as they render, creating a chess-board effect. You can
also optionally have an outline fill color. If set, this draws lines between the grid cells
in the given color. If you specify an outline color with an alpha of zero, then it will draw
the cells spaced out, but without the lines between them.
Constructor
new Grid(scene, [x], [y], [width], [height], [cellWidth], [cellHeight], [fillColor], [fillAlpha], [outlineFillColor], [outlineFillAlpha])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this Game Object in the world.
y number Yes 0 The vertical position of this Game Object in the world.
width number Yes 128 The width of the grid.
height number Yes 128 The height of the grid.
cellWidth number Yes 32 The width of one cell in the grid.
cellHeight number Yes 32 The height of one cell in the grid.
fillColor number Yes The color the grid cells will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes The alpha the grid cells will be filled with. You can also set the alpha of the overall Shape using its alpha property.
outlineFillColor number Yes The color of the lines between the grid cells. See the setOutline method.
outlineFillAlpha number Yes The alpha of the lines between the grid cells.
Scope : static
Extends
Phaser.GameObjects.Shape
Source: src/gameobjects/shape/grid/Grid.js#L11
Since: 3.13.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
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
From Phaser.GameObjects.Shape :
closePath
displayHeight
displayWidth
fillAlpha
fillColor
geom
height
isFilled
isRounded
isStroked
lineWidth
pathData
pathIndexes
radius
strokeAlpha
strokeColor
width
Public Members ​
altFillAlpha ​
altFillAlpha: number ​
Description:
The alpha the alternating grid cells will be filled with.
You can also set the alpha of the overall Shape using its alpha property.
Source: src/gameobjects/shape/grid/Grid.js#L141
Since: 3.13.0
altFillColor ​
altFillColor: number ​
Description:
The color the alternating grid cells will be filled with, i.e. 0xff0000 for red.
Source: src/gameobjects/shape/grid/Grid.js#L132
Since: 3.13.0
cellHeight ​
cellHeight: number ​
Description:
The height of each grid cell.
Must be a positive value.
Source: src/gameobjects/shape/grid/Grid.js#L77
Since: 3.13.0
cellWidth ​
cellWidth: number ​
Description:
The width of each grid cell.
Must be a positive value.
Source: src/gameobjects/shape/grid/Grid.js#L67
Since: 3.13.0
outlineFillAlpha ​
outlineFillAlpha: number ​
Description:
The alpha value for the color of the lines between each grid cell.
Source: src/gameobjects/shape/grid/Grid.js#L105
Since: 3.13.0
outlineFillColor ​
outlineFillColor: number ​
Description:
The color of the lines between each grid cell.
Source: src/gameobjects/shape/grid/Grid.js#L96
Since: 3.13.0
showAltCells ​
showAltCells: boolean ​
Description:
Will the grid render the alternating cells in the altFillColor ?
Source: src/gameobjects/shape/grid/Grid.js#L123
Since: 3.13.0
showCells ​
showCells: boolean ​
Description:
Will the grid render its cells in the fillColor ?
Source: src/gameobjects/shape/grid/Grid.js#L87
Since: 3.13.0
showOutline ​
showOutline: boolean ​
Description:
Will the grid display the lines between each cell when it renders?
Source: src/gameobjects/shape/grid/Grid.js#L114
Since: 3.13.0
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
From Phaser.GameObjects.Shape :
preDestroy
setClosePath
setDisplaySize
setStrokeStyle
Public Methods ​
setAltFillStyle ​
<instance> setAltFillStyle([fillColor], [fillAlpha]) ​
Description:
Sets the fill color and alpha level that the alternating grid cells will use.
If this method is called with no values then alternating grid cells will not be rendered in a different color.
Also see the setOutlineStyle and setFillStyle methods.
This call can be chained.
Parameters:
name type optional default description
fillColor number Yes The color the alternating grid cells will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes 1 The alpha the alternating grid cells will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Returns: Phaser.GameObjects.Grid - This Game Object instance.
Source: src/gameobjects/shape/grid/Grid.js#L200
Since: 3.13.0
setFillStyle ​
<instance> setFillStyle([fillColor], [fillAlpha]) ​
Description:
Sets the fill color and alpha level the grid cells will use when rendering.
If this method is called with no values then the grid cells will not be rendered,
however the grid lines and alternating cells may still be.
Also see the setOutlineStyle and setAltFillStyle methods.
This call can be chained.
Parameters:
name type optional default description
fillColor number Yes The color the grid cells will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes 1 The alpha the grid cells will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Overrides: Phaser.GameObjects.Shape#setFillStyle
Returns: Phaser.GameObjects.Grid - This Game Object instance.
Source: src/gameobjects/shape/grid/Grid.js#L164
Since: 3.13.0
setOutlineStyle ​
<instance> setOutlineStyle([fillColor], [fillAlpha]) ​
Description:
Sets the fill color and alpha level that the lines between each grid cell will use.
If this method is called with no values then the grid lines will not be rendered at all, however
the cells themselves may still be if they have colors set.
Also see the setFillStyle and setAltFillStyle methods.
This call can be chained.
Parameters:
name type optional default description
fillColor number Yes The color the lines between the grid cells will be filled with, i.e. 0xff0000 for red.
fillAlpha number Yes 1 The alpha the lines between the grid cells will be filled with. You can also set the alpha of the overall Shape using its alpha property.
Returns: Phaser.GameObjects.Grid - This Game Object instance.
Source: src/gameobjects/shape/grid/Grid.js#L235
Since: 3.13.0
Previous
Graphics
Next
Group
Inherited Members
Public Members
altFillAlpha
altFillColor
cellHeight
cellWidth
outlineFillAlpha
outlineFillColor
showAltCells
showCells
showOutline
Inherited Methods
Public Methods
setAltFillStyle
setFillStyle
setOutlineStyle
