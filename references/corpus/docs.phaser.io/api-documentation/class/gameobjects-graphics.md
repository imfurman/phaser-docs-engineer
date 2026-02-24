# Graphics | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-graphics

Phaser API Documentation
Class
Graphics
Version: Phaser v3.90.0
On this page
Graphics
A Graphics object is a way to draw primitive shapes to your game. Primitives include forms of geometry, such as
Rectangles, Circles, and Polygons. They also include lines, arcs and curves. When you initially create a Graphics
object it will be empty.
To draw to it you must first specify a line style or fill style (or both), draw shapes using paths, and finally
fill or stroke them. For example:
graphics . lineStyle ( 5 , 0xFF00FF , 1.0 ) ;
graphics . beginPath ( ) ;
graphics . moveTo ( 100 , 100 ) ;
graphics . lineTo ( 200 , 200 ) ;
graphics . closePath ( ) ;
graphics . strokePath ( ) ;
There are also many helpful methods that draw and fill/stroke common shapes for you.
graphics . lineStyle ( 5 , 0xFF00FF , 1.0 ) ;
graphics . fillStyle ( 0xFFFFFF , 1.0 ) ;
graphics . fillRect ( 50 , 50 , 400 , 200 ) ;
graphics . strokeRect ( 50 , 50 , 400 , 200 ) ;
When a Graphics object is rendered it will render differently based on if the game is running under Canvas or WebGL.
Under Canvas it will use the HTML Canvas context drawing operations to draw the path.
Under WebGL the graphics data is decomposed into polygons. Both of these are expensive processes, especially with
complex shapes.
If your Graphics object doesn't change much (or at all) once you've drawn your shape to it, then you will help
performance by calling Phaser.GameObjects.Graphics#generateTexture . This will 'bake' the Graphics object into
a Texture, and return it. You can then use this Texture for Sprites or other display objects. If your Graphics object
updates frequently then you should avoid doing this, as it will constantly generate new textures, which will consume
memory.
As you can tell, Graphics objects are a bit of a trade-off. While they are extremely useful, you need to be careful
in their complexity and quantity of them in your game.
Constructor
new Graphics(scene, [options])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Graphics object belongs.
options Phaser.Types.GameObjects.Graphics.Options Yes Options that set the position and default style of this Graphics object.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Phaser.GameObjects.Components.ScrollFactor
Source: src/gameobjects/graphics/Graphics.js#L18
Since: 3.0.0
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
commandBuffer ​
commandBuffer: array ​
Description:
The array of commands used to render the Graphics.
Source: src/gameobjects/graphics/Graphics.js#L128
Since: 3.0.0
defaultFillAlpha ​
defaultFillAlpha: number ​
Description:
The default fill alpha for shapes rendered by this Graphics object.
Set this value with setDefaultStyles() .
Source: src/gameobjects/graphics/Graphics.js#L150
Since: 3.0.0
defaultFillColor ​
defaultFillColor: number ​
Description:
The default fill color for shapes rendered by this Graphics object.
Set this value with setDefaultStyles() .
Source: src/gameobjects/graphics/Graphics.js#L138
Since: 3.0.0
defaultStrokeAlpha ​
defaultStrokeAlpha: number ​
Description:
The default stroke alpha for shapes rendered by this Graphics object.
Set this value with setDefaultStyles() .
Source: src/gameobjects/graphics/Graphics.js#L186
Since: 3.0.0
defaultStrokeColor ​
defaultStrokeColor: number ​
Description:
The default stroke color for shapes rendered by this Graphics object.
Set this value with setDefaultStyles() .
Source: src/gameobjects/graphics/Graphics.js#L174
Since: 3.0.0
defaultStrokeWidth ​
defaultStrokeWidth: number ​
Description:
The default stroke width for shapes rendered by this Graphics object.
Set this value with setDefaultStyles() .
Source: src/gameobjects/graphics/Graphics.js#L162
Since: 3.0.0
displayOriginX ​
displayOriginX: number ​
Description:
The horizontal display origin of the Graphics.
Source: src/gameobjects/graphics/Graphics.js#L108
Since: 3.0.0
displayOriginY ​
displayOriginY: number ​
Description:
The vertical display origin of the Graphics.
Source: src/gameobjects/graphics/Graphics.js#L118
Since: 3.0.0
TargetCamera ​
TargetCamera: Phaser.Cameras.Scene2D.Camera ​
Description:
A Camera used specifically by the Graphics system for rendering to textures.
Source: src/gameobjects/graphics/Graphics.js#L1565
Since: 3.1.0
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
arc ​
<instance> arc(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot]) ​
Description:
Draw an arc.
This method can be used to create circles, or parts of circles.
Make sure you call beginPath before starting the arc unless you wish for the arc to automatically
close when filled or stroked.
Use the optional overshoot argument increase the number of iterations that take place when
the arc is rendered in WebGL. This is useful if you're drawing an arc with an especially thick line,
as it will allow the arc to fully join-up. Try small values at first, i.e. 0.01.
Call Phaser.GameObjects.Graphics#fillPath or Phaser.GameObjects.Graphics#strokePath after calling
this method to draw the arc.
Parameters:
name type optional default description
x number No The x coordinate of the center of the circle.
y number No The y coordinate of the center of the circle.
radius number No The radius of the circle.
startAngle number No The starting angle, in radians.
endAngle number No The ending angle, in radians.
anticlockwise boolean Yes false Whether the drawing should be anticlockwise or clockwise.
overshoot number Yes 0 This value allows you to increase the segment iterations in WebGL rendering. Useful if the arc has a thick stroke and needs to overshoot to join-up cleanly. Use small numbers such as 0.01 to start with and increase as needed.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1242
Since: 3.0.0
beginPath ​
<instance> beginPath() ​
Description:
Start a new shape path.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L379
Since: 3.0.0
clear ​
<instance> clear() ​
Description:
Clear the command buffer and reset the fill style and line style to their defaults.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1442
Since: 3.0.0
closePath ​
<instance> closePath() ​
Description:
Close the current path.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L396
Since: 3.0.0
fill ​
<instance> fill() ​
Description:
Fill the current path.
This is an alias for Graphics.fillPath and does the same thing.
It was added to match the CanvasRenderingContext 2D API.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L430
Since: 3.16.0
fillCircle ​
<instance> fillCircle(x, y, radius) ​
Description:
Fill a circle with the given position and radius.
Parameters:
name type optional description
x number No The x coordinate of the center of the circle.
y number No The y coordinate of the center of the circle.
radius number No The radius of the circle.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L517
Since: 3.0.0
fillCircleShape ​
<instance> fillCircleShape(circle) ​
Description:
Fill the given circle.
Parameters:
name type optional description
circle Phaser.Geom.Circle No The circle to fill.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L487
Since: 3.0.0
fillEllipse ​
<instance> fillEllipse(x, y, width, height, [smoothness]) ​
Description:
Fill an ellipse with the given position and size.
Parameters:
name type optional default description
x number No The x coordinate of the center of the ellipse.
y number No The y coordinate of the center of the ellipse.
width number No The width of the ellipse.
height number No The height of the ellipse.
smoothness number Yes 32 The number of points to draw the ellipse with.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1217
Since: 3.0.0
fillEllipseShape ​
<instance> fillEllipseShape(ellipse, [smoothness]) ​
Description:
Fill the given ellipse.
Parameters:
name type optional default description
ellipse Phaser.Geom.Ellipse No The ellipse to fill.
smoothness number Yes 32 The number of points to draw the ellipse with.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1197
Since: 3.0.0
fillGradientStyle ​
<instance> fillGradientStyle(topLeft, topRight, bottomLeft, bottomRight, [alphaTopLeft], [alphaTopRight], [alphaBottomLeft], [alphaBottomRight]) ​
Description:
Sets a gradient fill style. This is a WebGL only feature.
The gradient color values represent the 4 corners of an untransformed rectangle.
The gradient is used to color all filled shapes and paths drawn after calling this method.
If you wish to turn a gradient off, call fillStyle and provide a new single fill color.
When filling a triangle only the first 3 color values provided are used for the 3 points of a triangle.
This feature is best used only on rectangles and triangles. All other shapes will give strange results.
Note that for objects such as arcs or ellipses, or anything which is made out of triangles, each triangle used
will be filled with a gradient on its own. There is no ability to gradient fill a shape or path as a single
entity at this time.
Tags:
webglOnly
Parameters:
name type optional default description
topLeft number No The top left fill color.
topRight number No The top right fill color.
bottomLeft number No The bottom left fill color.
bottomRight number No The bottom right fill color. Not used when filling triangles.
alphaTopLeft number Yes 1 The top left alpha value. If you give only this value, it's used for all corners.
alphaTopRight number Yes 1 The top right alpha value.
alphaBottomLeft number Yes 1 The bottom left alpha value.
alphaBottomRight number Yes 1 The bottom right alpha value.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L295
Since: 3.12.0
fillPath ​
<instance> fillPath() ​
Description:
Fill the current path.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L413
Since: 3.0.0
fillPoint ​
<instance> fillPoint(x, y, [size]) ​
Description:
Fill a point at the given position.
Draws a square at the given position, 1 pixel in size by default.
Parameters:
name type optional default description
x number No The x coordinate of the point.
y number No The y coordinate of the point.
size number Yes 1 The size of the square to draw.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L862
Since: 3.0.0
fillPoints ​
<instance> fillPoints(points, [closeShape], [closePath], [endIndex]) ​
Description:
Fill the shape represented by the given array of points.
Pass closeShape to automatically close the shape by joining the last to the first point.
Pass closePath to automatically close the path before it is filled.
Parameters:
name type optional default description
points array | Array.< Phaser.Geom.Point > No The points to fill.
closeShape boolean Yes false When true , the shape is closed by joining the last point to the first point.
closePath boolean Yes false When true , the path is closed before being stroked.
endIndex number Yes The index of points to stop at. Defaults to points.length .
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1105
Since: 3.0.0
fillPointShape ​
<instance> fillPointShape(point, [size]) ​
Description:
Fill the given point.
Draws a square at the given position, 1 pixel in size by default.
Parameters:
name type optional default description
point Phaser.Geom.Point | Phaser.Math.Vector2 object No
size number Yes 1 The size of the square to draw.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L844
Since: 3.0.0
fillRect ​
<instance> fillRect(x, y, width, height) ​
Description:
Fill a rectangle with the given position and size.
Parameters:
name type optional description
x number No The x coordinate of the top-left of the rectangle.
y number No The y coordinate of the top-left of the rectangle.
width number No The width of the rectangle.
height number No The height of the rectangle.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L589
Since: 3.0.0
fillRectShape ​
<instance> fillRectShape(rect) ​
Description:
Fill the given rectangle.
Parameters:
name type optional description
rect Phaser.Geom.Rectangle No The rectangle to fill.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L559
Since: 3.0.0
fillRoundedRect ​
<instance> fillRoundedRect(x, y, width, height, [radius]) ​
Description:
Fill a rounded rectangle with the given position, size and radius.
Parameters:
name type optional default description
x number No The x coordinate of the top-left of the rectangle.
y number No The y coordinate of the top-left of the rectangle.
width number No The width of the rectangle.
height number No The height of the rectangle.
radius Phaser.Types.GameObjects.Graphics.RoundedRectRadius | number Yes 20 The corner radius; It can also be an object to specify different radius for corners.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L654
Since: 3.11.0
fillStyle ​
<instance> fillStyle(color, [alpha]) ​
Description:
Set the current fill style. Used for all 'fill' related functions.
Parameters:
name type optional default description
color number No The fill color.
alpha number Yes 1 The fill alpha.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L272
Since: 3.0.0
fillTriangle ​
<instance> fillTriangle(x0, y0, x1, y1, x2, y2) ​
Description:
Fill a triangle with the given points.
Parameters:
name type optional description
x0 number No The x coordinate of the first point.
y0 number No The y coordinate of the first point.
x1 number No The x coordinate of the second point.
y1 number No The y coordinate of the second point.
x2 number No The x coordinate of the third point.
y2 number No The y coordinate of the third point.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L926
Since: 3.0.0
fillTriangleShape ​
<instance> fillTriangleShape(triangle) ​
Description:
Fill the given triangle.
Parameters:
name type optional description
triangle Phaser.Geom.Triangle No The triangle to fill.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L896
Since: 3.0.0
generateTexture ​
<instance> generateTexture(key, [width], [height]) ​
Description:
Generate a texture from this Graphics object.
If key is a string it'll generate a new texture using it and add it into the
Texture Manager (assuming no key conflict happens).
If key is a Canvas it will draw the texture to that canvas context. Note that it will NOT
automatically upload it to the GPU in WebGL mode.
Please understand that the texture is created via the Canvas API of the browser, therefore some
Graphics features, such as fillGradientStyle , will not appear on the resulting texture,
as they're unsupported by the Canvas API.
Parameters:
name type optional description
key string | HTMLCanvasElement No The key to store the texture with in the Texture Manager, or a Canvas to draw to.
width number Yes The width of the graphics to generate.
height number Yes The height of the graphics to generate.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1467
Since: 3.0.0
lineBetween ​
<instance> lineBetween(x1, y1, x2, y2) ​
Description:
Draw a line between the given points.
Parameters:
name type optional description
x1 number No The x coordinate of the start point of the line.
y1 number No The y coordinate of the start point of the line.
x2 number No The x coordinate of the end point of the line.
y2 number No The y coordinate of the end point of the line.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L991
Since: 3.0.0
lineGradientStyle ​
<instance> lineGradientStyle(lineWidth, topLeft, topRight, bottomLeft, bottomRight, [alpha]) ​
Description:
Sets a gradient line style. This is a WebGL only feature.
The gradient color values represent the 4 corners of an untransformed rectangle.
The gradient is used to color all stroked shapes and paths drawn after calling this method.
If you wish to turn a gradient off, call lineStyle and provide a new single line color.
This feature is best used only on single lines. All other shapes will give strange results.
Note that for objects such as arcs or ellipses, or anything which is made out of triangles, each triangle used
will be filled with a gradient on its own. There is no ability to gradient stroke a shape or path as a single
entity at this time.
Tags:
webglOnly
Parameters:
name type optional default description
lineWidth number No The stroke width.
topLeft number No The tint being applied to the top-left of the Game Object.
topRight number No The tint being applied to the top-right of the Game Object.
bottomLeft number No The tint being applied to the bottom-left of the Game Object.
bottomRight number No The tint being applied to the bottom-right of the Game Object.
alpha number Yes 1 The fill alpha.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L341
Since: 3.12.0
lineStyle ​
<instance> lineStyle(lineWidth, color, [alpha]) ​
Description:
Set the current line style. Used for all 'stroke' related functions.
Parameters:
name type optional default description
lineWidth number No The stroke width.
color number No The stroke color.
alpha number Yes 1 The stroke alpha.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L246
Since: 3.0.0
lineTo ​
<instance> lineTo(x, y) ​
Description:
Draw a line from the current drawing position to the given position.
Moves the current drawing position to the given position.
Parameters:
name type optional description
x number No The x coordinate to draw the line to.
y number No The y coordinate to draw the line to.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1014
Since: 3.0.0
moveTo ​
<instance> moveTo(x, y) ​
Description:
Move the current drawing position to the given position.
Parameters:
name type optional description
x number No The x coordinate to move to.
y number No The y coordinate to move to.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1037
Since: 3.0.0
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/graphics/Graphics.js#L1551
Since: 3.9.0
restore ​
<instance> restore() ​
Description:
Restores the most recently saved state of the Graphics by popping from the state stack.
Use Phaser.GameObjects.Graphics#save to save the current state, and call this afterwards to restore that state.
If there is no saved state, this command does nothing.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1341
Since: 3.0.0
rotateCanvas ​
<instance> rotateCanvas(radians) ​
Description:
Inserts a rotation command into this Graphics objects command buffer.
All objects drawn after calling this method will be rotated
by the given amount.
This does not change the rotation of the Graphics object itself,
only of the objects drawn by it after calling this method.
Parameters:
name type optional description
radians number No The rotation angle, in radians.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1416
Since: 3.0.0
save ​
<instance> save() ​
Description:
Saves the state of the Graphics by pushing the current state onto a stack.
The most recently saved state can then be restored with Phaser.GameObjects.Graphics#restore .
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1322
Since: 3.0.0
scaleCanvas ​
<instance> scaleCanvas(x, y) ​
Description:
Inserts a scale command into this Graphics objects command buffer.
All objects drawn after calling this method will be scaled
by the given amount.
This does not change the scale of the Graphics object itself,
only of the objects drawn by it after calling this method.
Parameters:
name type optional description
x number No The horizontal scale to apply.
y number No The vertical scale to apply.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1389
Since: 3.0.0
setDefaultStyles ​
<instance> setDefaultStyles(options) ​
Description:
Set the default style settings for this Graphics object.
Parameters:
name type optional description
options Phaser.Types.GameObjects.Graphics.Styles No The styles to set as defaults.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L214
Since: 3.0.0
slice ​
<instance> slice(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot]) ​
Description:
Creates a pie-chart slice shape centered at x , y with the given radius.
You must define the start and end angle of the slice.
Setting the anticlockwise argument to true creates a shape similar to Pacman.
Setting it to false creates a shape like a slice of pie.
This method will begin a new path and close the path at the end of it.
To display the actual slice you need to call either strokePath or fillPath after it.
Parameters:
name type optional default description
x number No The horizontal center of the slice.
y number No The vertical center of the slice.
radius number No The radius of the slice.
startAngle number No The start angle of the slice, given in radians.
endAngle number No The end angle of the slice, given in radians.
anticlockwise boolean Yes false Whether the drawing should be anticlockwise or clockwise.
overshoot number Yes 0 This value allows you to overshoot the endAngle by this amount. Useful if the arc has a thick stroke and needs to overshoot to join-up cleanly.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1283
Since: 3.4.0
stroke ​
<instance> stroke() ​
Description:
Stroke the current path.
This is an alias for Graphics.strokePath and does the same thing.
It was added to match the CanvasRenderingContext 2D API.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L467
Since: 3.16.0
strokeCircle ​
<instance> strokeCircle(x, y, radius) ​
Description:
Stroke a circle with the given position and radius.
Parameters:
name type optional description
x number No The x coordinate of the center of the circle.
y number No The y coordinate of the center of the circle.
radius number No The radius of the circle.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L538
Since: 3.0.0
strokeCircleShape ​
<instance> strokeCircleShape(circle) ​
Description:
Stroke the given circle.
Parameters:
name type optional description
circle Phaser.Geom.Circle No The circle to stroke.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L502
Since: 3.0.0
strokeEllipse ​
<instance> strokeEllipse(x, y, width, height, [smoothness]) ​
Description:
Stroke an ellipse with the given position and size.
Parameters:
name type optional default description
x number No The x coordinate of the center of the ellipse.
y number No The y coordinate of the center of the ellipse.
width number No The width of the ellipse.
height number No The height of the ellipse.
smoothness number Yes 32 The number of points to draw the ellipse with.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1172
Since: 3.0.0
strokeEllipseShape ​
<instance> strokeEllipseShape(ellipse, [smoothness]) ​
Description:
Stroke the given ellipse.
Parameters:
name type optional default description
ellipse Phaser.Geom.Ellipse No The ellipse to stroke.
smoothness number Yes 32 The number of points to draw the ellipse with.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1152
Since: 3.0.0
strokeLineShape ​
<instance> strokeLineShape(line) ​
Description:
Draw the given line.
Parameters:
name type optional description
line Phaser.Geom.Line No The line to stroke.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L976
Since: 3.0.0
strokePath ​
<instance> strokePath() ​
Description:
Stroke the current path.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L450
Since: 3.0.0
strokePoints ​
<instance> strokePoints(points, [closeShape], [closePath], [endIndex]) ​
Description:
Stroke the shape represented by the given array of points.
Pass closeShape to automatically close the shape by joining the last to the first point.
Pass closePath to automatically close the path before it is stroked.
Parameters:
name type optional default description
points array | Array.< Phaser.Geom.Point > No The points to stroke.
closeShape boolean Yes false When true , the shape is closed by joining the last point to the first point.
closePath boolean Yes false When true , the path is closed before being stroked.
endIndex number Yes The index of points to stop drawing at. Defaults to points.length .
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1058
Since: 3.0.0
strokeRect ​
<instance> strokeRect(x, y, width, height) ​
Description:
Stroke a rectangle with the given position and size.
Parameters:
name type optional description
x number No The x coordinate of the top-left of the rectangle.
y number No The y coordinate of the top-left of the rectangle.
width number No The width of the rectangle.
height number No The height of the rectangle.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L612
Since: 3.0.0
strokeRectShape ​
<instance> strokeRectShape(rect) ​
Description:
Stroke the given rectangle.
Parameters:
name type optional description
rect Phaser.Geom.Rectangle No The rectangle to stroke.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L574
Since: 3.0.0
strokeRoundedRect ​
<instance> strokeRoundedRect(x, y, width, height, [radius]) ​
Description:
Stroke a rounded rectangle with the given position, size and radius.
Parameters:
name type optional default description
x number No The x coordinate of the top-left of the rectangle.
y number No The y coordinate of the top-left of the rectangle.
width number No The width of the rectangle.
height number No The height of the rectangle.
radius Phaser.Types.GameObjects.Graphics.RoundedRectRadius | number Yes 20 The corner radius; It can also be an object to specify different radii for corners.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L746
Since: 3.11.0
strokeTriangle ​
<instance> strokeTriangle(x0, y0, x1, y1, x2, y2) ​
Description:
Stroke a triangle with the given points.
Parameters:
name type optional description
x0 number No The x coordinate of the first point.
y0 number No The y coordinate of the first point.
x1 number No The x coordinate of the second point.
y1 number No The y coordinate of the second point.
x2 number No The x coordinate of the third point.
y2 number No The y coordinate of the third point.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L951
Since: 3.0.0
strokeTriangleShape ​
<instance> strokeTriangleShape(triangle) ​
Description:
Stroke the given triangle.
Parameters:
name type optional description
triangle Phaser.Geom.Triangle No The triangle to stroke.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L911
Since: 3.0.0
translateCanvas ​
<instance> translateCanvas(x, y) ​
Description:
Inserts a translation command into this Graphics objects command buffer.
All objects drawn after calling this method will be translated
by the given amount.
This does not change the position of the Graphics object itself,
only of the objects drawn by it after calling this method.
Parameters:
name type optional description
x number No The horizontal translation to apply.
y number No The vertical translation to apply.
Returns: Phaser.GameObjects.Graphics - This Game Object.
Source: src/gameobjects/graphics/Graphics.js#L1362
Since: 3.0.0
Previous
GameObjectFactory
Next
Grid
Inherited Members
Public Members
commandBuffer
defaultFillAlpha
defaultFillColor
defaultStrokeAlpha
defaultStrokeColor
defaultStrokeWidth
displayOriginX
displayOriginY
TargetCamera
Inherited Methods
Public Methods
arc
beginPath
clear
closePath
fill
fillCircle
fillCircleShape
fillEllipse
fillEllipseShape
fillGradientStyle
fillPath
fillPoint
fillPoints
fillPointShape
fillRect
fillRectShape
fillRoundedRect
fillStyle
fillTriangle
fillTriangleShape
generateTexture
lineBetween
lineGradientStyle
lineStyle
lineTo
moveTo
preDestroy
restore
rotateCanvas
save
scaleCanvas
setDefaultStyles
slice
stroke
strokeCircle
strokeCircleShape
strokeEllipse
strokeEllipseShape
strokeLineShape
strokePath
strokePoints
strokeRect
strokeRectShape
strokeRoundedRect
strokeTriangle
strokeTriangleShape
translateCanvas
