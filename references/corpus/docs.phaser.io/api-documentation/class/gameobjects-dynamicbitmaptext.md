# DynamicBitmapText | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-dynamicbitmaptext

Phaser API Documentation
Class
DynamicBitmapText
Version: Phaser v3.90.0
On this page
DynamicBitmapText
BitmapText objects work by taking a texture file and an XML or JSON file that describes the font structure.
During rendering for each letter of the text is rendered to the display, proportionally spaced out and aligned to
match the font structure.
Dynamic Bitmap Text objects are different from Static Bitmap Text in that they invoke a callback for each
letter being rendered during the render pass. This callback allows you to manipulate the properties of
each letter being rendered, such as its position, scale or tint, allowing you to create interesting effects
like jiggling text, which can't be done with Static text. This means that Dynamic Text takes more processing
time, so only use them if you require the callback ability they have.
BitmapText objects are less flexible than Text objects, in that they have less features such as shadows, fills and the ability
to use Web Fonts, however you trade this flexibility for rendering speed. You can also create visually compelling BitmapTexts by
processing the font texture in an image editor, applying fills and any other effects required.
To create multi-line text insert \r, \n or \r\n escape codes into the text string.
To create a BitmapText data files you need a 3rd party app such as:
BMFont (Windows, free): http://www.angelcode.com/products/bmfont/
Glyph Designer (OS X, commercial): http://www.71squared.com/en/glyphdesigner
Snow BMF (Web-based, free): https://snowb.org/
Littera (Flash-based, free): http://kvazars.com/littera/
For most use cases it is recommended to use XML. If you wish to use JSON, the formatting should be equal to the result of
converting a valid XML file through the popular X2JS library. An online tool for conversion can be found here: http://codebeautify.org/xmltojson
Constructor
new DynamicBitmapText(scene, x, y, font, [text], [size], [align])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. It can only belong to one Scene at any given time.
x number No The x coordinate of this Game Object in world space.
y number No The y coordinate of this Game Object in world space.
font string No The key of the font to use from the Bitmap Font cache.
text string | Array.<string> Yes The string, or array of strings, to be set as the content of this Bitmap Text.
size number Yes The font size of this Bitmap Text.
align number Yes 0 The alignment of the text in a multi-line BitmapText object.
Scope : static
Extends
Phaser.GameObjects.BitmapText
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L11
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.BitmapText :
align
displayHeight
displayWidth
dropShadowAlpha
dropShadowColor
dropShadowX
dropShadowY
font
fontData
fontSize
fromAtlas
height
letterSpacing
lineSpacing
maxWidth
text
width
wordWrapCharCode
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
From Phaser.GameObjects.Components.Texture :
frame
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
Public Members ​
callbackData ​
callbackData: Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig ​
Description:
The data object that is populated during rendering, then passed to the displayCallback.
You should modify this object then return it back from the callback. It's updated values
will be used to render the specific glyph.
Please note that if you need a reference to this object locally in your game code then you
should shallow copy it, as it's updated and re-used for every glyph in the text.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L119
Since: 3.11.0
cropHeight ​
cropHeight: number ​
Description:
The crop height of the Bitmap Text.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L100
Since: 3.0.0
cropWidth ​
cropWidth: number ​
Description:
The crop width of the Bitmap Text.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L90
Since: 3.0.0
displayCallback ​
displayCallback: Phaser.Types.GameObjects.BitmapText.DisplayCallback ​
Description:
A callback that alters how each character of the Bitmap Text is rendered.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L110
Since: 3.0.0
scrollX ​
scrollX: number ​
Description:
The horizontal scroll position of the Bitmap Text.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L70
Since: 3.0.0
scrollY ​
scrollY: number ​
Description:
The vertical scroll position of the Bitmap Text.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L80
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
From Phaser.GameObjects.BitmapText :
getCharacterAt
getTextBounds
preDestroy
setCenterAlign
setCharacterTint
setDisplaySize
setDropShadow
setFont
setFontSize
setLeftAlign
setLetterSpacing
setLineSpacing
setMaxWidth
setRightAlign
setText
setWordTint
toJSON
updateDisplayOrigin
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
From Phaser.GameObjects.Components.Texture :
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
Public Methods ​
setDisplayCallback ​
<instance> setDisplayCallback(callback) ​
Description:
Set a callback that alters how each character of the Bitmap Text is rendered.
The callback receives a Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig object that contains information about the character that's
about to be rendered.
It should return an object with x , y , scale and rotation properties that will be used instead of the
usual values when rendering.
Parameters:
name type optional description
callback Phaser.Types.GameObjects.BitmapText.DisplayCallback No The display callback to set.
Returns: Phaser.GameObjects.DynamicBitmapText - This Game Object.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L169
Since: 3.0.0
setScrollX ​
<instance> setScrollX(value) ​
Description:
Set the horizontal scroll position of this Bitmap Text.
Parameters:
name type optional description
value number No The horizontal scroll position to set.
Returns: Phaser.GameObjects.DynamicBitmapText - This Game Object.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L192
Since: 3.0.0
setScrollY ​
<instance> setScrollY(value) ​
Description:
Set the vertical scroll position of this Bitmap Text.
Parameters:
name type optional description
value number No The vertical scroll position to set.
Returns: Phaser.GameObjects.DynamicBitmapText - This Game Object.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L209
Since: 3.0.0
setSize ​
<instance> setSize(width, height) ​
Description:
Set the crop size of this Bitmap Text.
Parameters:
name type optional description
width number No The width of the crop.
height number No The height of the crop.
Returns: Phaser.GameObjects.DynamicBitmapText - This Game Object.
Source: src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L150
Since: 3.0.0
Previous
DisplayList
Next
Ellipse
Inherited Members
Public Members
callbackData
cropHeight
cropWidth
displayCallback
scrollX
scrollY
Inherited Methods
Public Methods
setDisplayCallback
setScrollX
setScrollY
setSize
