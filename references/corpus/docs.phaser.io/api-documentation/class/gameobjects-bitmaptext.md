# BitmapText | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-bitmaptext

Phaser API Documentation
Class
BitmapText
Version: Phaser v3.90.0
On this page
BitmapText
BitmapText objects work by taking a texture file and an XML or JSON file that describes the font structure.
During rendering for each letter of the text is rendered to the display, proportionally spaced out and aligned to
match the font structure.
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
new BitmapText(scene, x, y, font, [text], [size], [align])
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
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Alpha
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Texture
Phaser.GameObjects.Components.Tint
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L17
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
align ​
align: number ​
Description:
Controls the alignment of each line of text in this BitmapText object.
Only has any effect when this BitmapText contains multiple lines of text, split with carriage-returns.
Has no effect with single-lines of text.
See the methods setLeftAlign , setCenterAlign and setRightAlign .
0 = Left aligned (default)
1 = Middle aligned
2 = Right aligned
The alignment position is based on the longest line of text.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L883
Since: 3.11.0
ALIGN_CENTER ​
ALIGN_CENTER: number ​
Description:
Center align the text characters in a multi-line BitmapText object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1203
Since: 3.11.0
ALIGN_LEFT ​
ALIGN_LEFT: number ​
Description:
Left align the text characters in a multi-line BitmapText object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1194
Since: 3.11.0
ALIGN_RIGHT ​
ALIGN_RIGHT: number ​
Description:
Right align the text characters in a multi-line BitmapText object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1212
Since: 3.11.0
displayHeight ​
displayHeight: number ​
Description:
The displayed height of this Bitmap Text.
This value takes into account the scale factor.
This property is read-only.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1118
Since: 3.60.0
displayWidth ​
displayWidth: number ​
Description:
The displayed width of this Bitmap Text.
This value takes into account the scale factor.
This property is read-only.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1086
Since: 3.60.0
dropShadowAlpha ​
dropShadowAlpha: number ​
Description:
The alpha value of the drop shadow.
You can set this directly, or use Phaser.GameObjects.BitmapText#setDropShadow .
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L273
Since: 3.50.0
dropShadowColor ​
dropShadowColor: number ​
Description:
The color of the drop shadow.
You can set this directly, or use Phaser.GameObjects.BitmapText#setDropShadow .
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L262
Since: 3.50.0
dropShadowX ​
dropShadowX: number ​
Description:
The horizontal offset of the drop shadow.
You can set this directly, or use Phaser.GameObjects.BitmapText#setDropShadow .
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L240
Since: 3.50.0
dropShadowY ​
dropShadowY: number ​
Description:
The vertical offset of the drop shadow.
You can set this directly, or use Phaser.GameObjects.BitmapText#setDropShadow .
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L251
Since: 3.50.0
font ​
font: string ​
Description:
The key of the Bitmap Font used by this Bitmap Text.
To change the font after creation please use setFont .
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L98
Since: 3.0.0
fontData ​
fontData: Phaser.Types.GameObjects.BitmapText.BitmapFontData ​
Description:
The data of the Bitmap Font used by this Bitmap Text.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L116
Since: 3.0.0
fontSize ​
fontSize: number ​
Description:
The font size of this Bitmap Text.
You can also use the method setFontSize if you want a chainable way to change the font size.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L939
Since: 3.0.0
fromAtlas ​
fromAtlas: boolean ​
Description:
Indicates whether the font texture is from an atlas or not.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L284
Since: 3.54.0
height ​
height: number ​
Description:
The height of this Bitmap text.
This property is read-only.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1065
Since: 3.0.0
letterSpacing ​
letterSpacing: number ​
Description:
Adds / Removes spacing between characters.
Can be a negative or positive number.
You can also use the method setLetterSpacing if you want a chainable way to change the letter spacing.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L963
Since: 3.0.0
lineSpacing ​
lineSpacing: number ​
Description:
Adds / Removes spacing between lines.
Can be a negative or positive number.
You can also use the method setLineSpacing if you want a chainable way to change the line spacing.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L989
Since: 3.60.0
maxWidth ​
maxWidth: number ​
Description:
The maximum display width of this BitmapText in pixels.
If BitmapText.text is longer than maxWidth then the lines will be automatically wrapped
based on the last whitespace character found in the line.
If no whitespace was found then no wrapping will take place and consequently the maxWidth value will not be honored.
Disable maxWidth by setting the value to 0.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1015
Since: 3.21.0
text ​
text: string ​
Description:
The text that this Bitmap Text object displays.
You can also use the method setText if you want a chainable way to change the text content.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L916
Since: 3.0.0
width ​
width: number ​
Description:
The width of this Bitmap Text.
This property is read-only.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1044
Since: 3.0.0
wordWrapCharCode ​
wordWrapCharCode: number ​
Description:
The character code used to detect for word wrapping.
Defaults to 32 (a space character).
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L220
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
getCharacterAt ​
<instance> getCharacterAt(x, y, [camera]) ​
Description:
Gets the character located at the given x/y coordinate within this Bitmap Text.
The coordinates you pass in are translated into the local space of the
Bitmap Text, however, it is up to you to first translate the input coordinates to world space.
If you wish to use this in combination with an input event, be sure
to pass in Pointer.worldX and worldY so they are in world space.
In some cases, based on kerning, characters can overlap. When this happens,
the first character in the word is returned.
Note that this does not work for DynamicBitmapText if you have changed the
character positions during render. It will only scan characters in their un-translated state.
Parameters:
name type optional description
x number No The x position to check.
y number No The y position to check.
camera Phaser.Cameras.Scene2D.Camera Yes The Camera which is being tested against. If not given will use the Scene default camera.
Returns: Phaser.Types.GameObjects.BitmapText.BitmapTextCharacter - The character object at the given position, or null .
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L716
Since: 3.50.0
getTextBounds ​
<instance> getTextBounds([round]) ​
Description:
Calculate the bounds of this Bitmap Text.
An object is returned that contains the position, width and height of the Bitmap Text in local and global
contexts.
Local size is based on just the font size and a [0, 0] position.
Global size takes into account the Game Object's scale, world position and display origin.
Also in the object is data regarding the length of each line, should this be a multi-line BitmapText.
Parameters:
name type optional default description
round boolean Yes false Whether to round the results up to the nearest integer.
Returns: Phaser.Types.GameObjects.BitmapText.BitmapTextSize - An object that describes the size of this Bitmap Text.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L679
Since: 3.0.0
ParseFromAtlas ​
<static> ParseFromAtlas(scene, fontName, textureKey, frameKey, xmlKey, [xSpacing], [ySpacing]) ​
Description:
Parse an XML Bitmap Font from an Atlas.
Adds the parsed Bitmap Font data to the cache with the fontName key.
Parameters:
name type optional description
scene Phaser.Scene No The Scene to parse the Bitmap Font for.
fontName string No The key of the font to add to the Bitmap Font cache.
textureKey string No The key of the BitmapFont's texture.
frameKey string No The key of the BitmapFont texture's frame.
xmlKey string No The key of the XML data of the font to parse.
xSpacing number Yes The x-axis spacing to add between each letter.
ySpacing number Yes The y-axis spacing to add to the line height.
Returns: boolean - Whether the parsing was successful or not.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1221
Since: 3.0.0
ParseXMLBitmapFont ​
<static> ParseXMLBitmapFont(xml, frame, [xSpacing], [ySpacing]) ​
Description:
Parse an XML font to Bitmap Font data for the Bitmap Font cache.
Parameters:
name type optional default description
xml XMLDocument No The XML Document to parse the font from.
frame Phaser.Textures.Frame No The texture frame to take into account when creating the uv data.
xSpacing number Yes 0 The x-axis spacing to add between each letter.
ySpacing number Yes 0 The y-axis spacing to add to the line height.
Returns: Phaser.Types.GameObjects.BitmapText.BitmapFontData - The parsed Bitmap Font data.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1241
Since: 3.17.0
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1178
Since: 3.50.0
setCenterAlign ​
<instance> setCenterAlign() ​
Description:
Set the lines of text in this BitmapText to be center-aligned.
This only has any effect if this BitmapText contains more than one line of text.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L321
Since: 3.11.0
setCharacterTint ​
<instance> setCharacterTint([start], [length], [tintFill], [topLeft], [topRight], [bottomLeft], [bottomRight]) ​
Description:
Sets a tint on a range of characters in this Bitmap Text, starting from the start parameter index
and running for length quantity of characters.
The start parameter can be negative. In this case, it starts at the end of the text and counts
backwards start places.
You can also pass in -1 as the length and it will tint all characters from start
up until the end of the string.
Remember that spaces and punctuation count as characters.
This is a WebGL only feature and only works with Static Bitmap Text, not Dynamic.
The tint works by taking the pixel color values from the Bitmap Text texture, and then
multiplying it by the color value of the tint. You can provide either one color value,
in which case the whole character will be tinted in that color. Or you can provide a color
per corner. The colors are blended together across the extent of the character range.
To swap this from being an additive tint to a fill based tint, set the tintFill parameter to true .
To modify the tint color once set, call this method again with new color values.
Using setWordTint can override tints set by this function, and vice versa.
To remove a tint call this method with just the start , and optionally, the length parameters defined.
Tags:
webglOnly
Parameters:
name type optional default description
start number Yes 0 The starting character to begin the tint at. If negative, it counts back from the end of the text.
length number Yes 1 The number of characters to tint. Remember that spaces count as a character too. Pass -1 to tint all characters from start onwards.
tintFill boolean Yes false Use a fill-based tint (true), or an additive tint (false)
topLeft number Yes "0xffffff" The tint being applied to the top-left of the character. If not other values are given this value is applied evenly, tinting the whole character.
topRight number Yes The tint being applied to the top-right of the character.
bottomLeft number Yes The tint being applied to the bottom-left of the character.
bottomRight number Yes The tint being applied to the bottom-right of the character.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L497
Since: 3.50.0
setDisplaySize ​
<instance> setDisplaySize(width, height) ​
Description:
Sets the display size of this BitmapText Game Object.
Calling this will adjust the scale.
Parameters:
name type optional description
width number No The width of this BitmapText Game Object.
height number No The height of this BitmapText Game Object.
Returns: Phaser.GameObjects.BitmapText - This Game Object instance.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L855
Since: 3.61.0
setDropShadow ​
<instance> setDropShadow([x], [y], [color], [alpha]) ​
Description:
Sets a drop shadow effect on this Bitmap Text.
This is a WebGL only feature and only works with Static Bitmap Text, not Dynamic.
You can set the vertical and horizontal offset of the shadow, as well as the color and alpha.
Once a shadow has been enabled you can modify the dropShadowX and dropShadowY properties of this
Bitmap Text directly to adjust the position of the shadow in real-time.
If you wish to clear the shadow, call this method with no parameters specified.
Tags:
webglOnly
Parameters:
name type optional default description
x number Yes 0 The horizontal offset of the drop shadow.
y number Yes 0 The vertical offset of the drop shadow.
color number Yes "0x000000" The color of the drop shadow, given as a hex value, i.e. 0x000000 for black.
alpha number Yes 0.5 The alpha of the drop shadow, given as a float between 0 and 1. This is combined with the Bitmap Text alpha as well.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L459
Since: 3.50.0
setFont ​
<instance> setFont(font, [size], [align]) ​
Description:
Changes the font this BitmapText is using to render.
The new texture is loaded and applied to the BitmapText. The existing text, size and alignment are preserved,
unless overridden via the arguments.
Parameters:
name type optional default description
font string No The key of the font to use from the Bitmap Font cache.
size number Yes The font size of this Bitmap Text. If not specified the current size will be used.
align number Yes 0 The alignment of the text in a multi-line BitmapText object. If not specified the current alignment will be used.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L783
Since: 3.11.0
setFontSize ​
<instance> setFontSize(size) ​
Description:
Set the font size of this Bitmap Text.
Parameters:
name type optional description
size number No The font size to set.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L357
Since: 3.0.0
setLeftAlign ​
<instance> setLeftAlign() ​
Description:
Set the lines of text in this BitmapText to be left-aligned.
This only has any effect if this BitmapText contains more than one line of text.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L303
Since: 3.11.0
setLetterSpacing ​
<instance> setLetterSpacing([spacing]) ​
Description:
Sets the letter spacing between each character of this Bitmap Text.
Can be a positive value to increase the space, or negative to reduce it.
Spacing is applied after the kerning values have been set.
Parameters:
name type optional default description
spacing number Yes 0 The amount of horizontal space to add between each character.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L376
Since: 3.4.0
setLineSpacing ​
<instance> setLineSpacing([spacing]) ​
Description:
Sets the line spacing value. This value is added to the font height to
calculate the overall line height.
Spacing can be a negative or positive number.
Only has an effect if this BitmapText object contains multiple lines of text.
Parameters:
name type optional default description
spacing number Yes 0 The amount of space to add between each line in multi-line text.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L399
Since: 3.60.0
setMaxWidth ​
<instance> setMaxWidth(value, [wordWrapCharCode]) ​
Description:
Sets the maximum display width of this BitmapText in pixels.
If BitmapText.text is longer than maxWidth then the lines will be automatically wrapped
based on the previous whitespace character found in the line.
If no whitespace was found then no wrapping will take place and consequently the maxWidth value will not be honored.
Disable maxWidth by setting the value to 0.
You can set the whitespace character to be searched for by setting the wordWrapCharCode parameter or property.
Parameters:
name type optional description
value number No The maximum display width of this BitmapText in pixels. Set to zero to disable.
wordWrapCharCode number Yes The character code to check for when word wrapping. Defaults to 32 (the space character).
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L821
Since: 3.21.0
setRightAlign ​
<instance> setRightAlign() ​
Description:
Set the lines of text in this BitmapText to be right-aligned.
This only has any effect if this BitmapText contains more than one line of text.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L339
Since: 3.11.0
setText ​
<instance> setText(value) ​
Description:
Set the textual content of this BitmapText.
An array of strings will be converted into multi-line text. Use the align methods to change multi-line alignment.
Parameters:
name type optional description
value string | Array.<string> No The string, or array of strings, to be set as the content of this BitmapText.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L423
Since: 3.0.0
setWordTint ​
<instance> setWordTint(word, [count], [tintFill], [topLeft], [topRight], [bottomLeft], [bottomRight]) ​
Description:
Sets a tint on a matching word within this Bitmap Text.
The word parameter can be either a string or a number.
If a string, it will run a string comparison against the text contents, and if matching,
it will tint the whole word.
If a number, if till that word, based on its offset within the text contents.
The count parameter controls how many words are replaced. Pass in -1 to replace them all.
This parameter is ignored if you pass a number as the word to be searched for.
This is a WebGL only feature and only works with Static Bitmap Text, not Dynamic.
The tint works by taking the pixel color values from the Bitmap Text texture, and then
multiplying it by the color value of the tint. You can provide either one color value,
in which case the whole character will be tinted in that color. Or you can provide a color
per corner. The colors are blended together across the extent of the character range.
To swap this from being an additive tint to a fill based tint, set the tintFill parameter to true .
To modify the tint color once set, call this method again with new color values.
Using setCharacterTint can override tints set by this function, and vice versa.
Tags:
webglOnly
Parameters:
name type optional default description
word string | number No The word to search for. Either a string, or an index of the word in the words array.
count number Yes 1 The number of matching words to tint. Pass -1 to tint all matching words.
tintFill boolean Yes false Use a fill-based tint (true), or an additive tint (false)
topLeft number Yes "0xffffff" The tint being applied to the top-left of the word. If not other values are given this value is applied evenly, tinting the whole word.
topRight number Yes The tint being applied to the top-right of the word.
bottomLeft number Yes The tint being applied to the bottom-left of the word.
bottomRight number Yes The tint being applied to the bottom-right of the word.
Returns: Phaser.GameObjects.BitmapText - This BitmapText Object.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L606
Since: 3.50.0
toJSON ​
<instance> toJSON() ​
Description:
Build a JSON representation of this Bitmap Text.
Overrides: Phaser.GameObjects.GameObject#toJSON
Returns: Phaser.Types.GameObjects.BitmapText.JSONBitmapText - A JSON representation of this Bitmap Text.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L1150
Since: 3.0.0
updateDisplayOrigin ​
<instance> updateDisplayOrigin() ​
Description:
Updates the Display Origin cached values internally stored on this Game Object.
You don't usually call this directly, but it is exposed for edge-cases where you may.
Overrides: Phaser.GameObjects.Components.Origin#updateDisplayOrigin
Returns: Phaser.GameObjects.BitmapText - This Game Object instance.
Source: src/gameobjects/bitmaptext/static/BitmapText.js#L765
Since: 3.0.0
Previous
Arc
Next
Blitter
Inherited Members
Public Members
align
ALIGN_CENTER
ALIGN_LEFT
ALIGN_RIGHT
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
Inherited Methods
Public Methods
getCharacterAt
getTextBounds
ParseFromAtlas
ParseXMLBitmapFont
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
