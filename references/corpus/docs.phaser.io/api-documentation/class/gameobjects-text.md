# Text | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-text

Phaser API Documentation
Class
Text
Version: Phaser v3.90.0
On this page
Text
A Text Game Object.
Text objects work by creating their own internal hidden Canvas and then renders text to it using
the standard Canvas fillText API. It then creates a texture from this canvas which is rendered
to your game during the render pass.
Because it uses the Canvas API you can take advantage of all the features this offers, such as
applying gradient fills to the text, or strokes, shadows and more. You can also use custom fonts
loaded externally, such as Google or TypeKit Web fonts.
Important: The font name must be quoted if it contains certain combinations of digits or
special characters, either when creating the Text object, or when setting the font via setFont
or setFontFamily , e.g.:
this . add . text ( 0 , 0 , 'Hello World' , { fontFamily : 'Georgia, "Goudy Bookletter 1911", Times, serif' } ) ;
this . add . text ( 0 , 0 , 'Hello World' , { font : '"Press Start 2P"' } ) ;
You can only display fonts that are currently loaded and available to the browser: therefore fonts must
be pre-loaded. Phaser does not do this for you, so you will require the use of a 3rd party font loader,
or have the fonts ready available in the CSS on the page in which your Phaser game resides.
See this for the available default fonts
across mobile browsers.
A note on performance: Every time the contents of a Text object changes, i.e. changing the text being
displayed, or the style of the text, it needs to remake the Text canvas, and if on WebGL, re-upload the
new texture to the GPU. This can be an expensive operation if used often, or with large quantities of
Text objects in your game. If you run into performance issues you would be better off using Bitmap Text
instead, as it benefits from batching and avoids expensive Canvas API calls.
Constructor
new Text(scene, x, y, text, style)
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
text string | Array.<string> No The text this Text object will display.
style Phaser.Types.GameObjects.Text.TextStyle No The text style configuration object.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Alpha
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.ComputedSize
Phaser.GameObjects.Components.Crop
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Flip
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Tint
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/text/Text.js#L19
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
From Phaser.GameObjects.Components.ComputedSize :
displayHeight
displayWidth
From Phaser.GameObjects.Components.Crop :
frame
isCropped
texture
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
autoRound ​
autoRound: boolean ​
Description:
Whether to automatically round line positions.
Source: src/gameobjects/text/Text.js#L161
Since: 3.0.0
canvas ​
canvas: HTMLCanvasElement ​
Description:
The canvas element that the text is rendered to.
Source: src/gameobjects/text/Text.js#L132
Since: 3.0.0
context ​
context: CanvasRenderingContext2D ​
Description:
The context of the canvas element that the text is rendered to.
Source: src/gameobjects/text/Text.js#L141
Since: 3.0.0
height ​
height: number ​
Description:
The height of this Text object.
Overrides: Phaser.GameObjects.Components.ComputedSize#height
Source: src/gameobjects/text/Text.js#L212
Since: 3.0.0
letterSpacing ​
letterSpacing: number ​
Description:
Adds / Removes spacing between characters.
Can be a negative or positive number.
If you update this property directly, instead of using the setLetterSpacing method, then
be sure to call updateText after, or you won't see the change reflected in the Text object.
Source: src/gameobjects/text/Text.js#L236
Since: 3.60.0
lineSpacing ​
lineSpacing: number ​
Description:
The line spacing value.
This value is added to the font height to calculate the overall line height.
Only has an effect if this Text object contains multiple lines of text.
If you update this property directly, instead of using the setLineSpacing method, then
be sure to call updateText after, or you won't see the change reflected in the Text object.
Source: src/gameobjects/text/Text.js#L222
Since: 3.13.0
padding ​
padding: Phaser.Types.GameObjects.Text.TextPadding ​
Description:
Specify a padding value which is added to the line width and height when calculating the Text size.
Allows you to add extra spacing if the browser is unable to accurately determine the true font dimensions.
Source: src/gameobjects/text/Text.js#L192
Since: 3.0.0
renderer ​
renderer: Phaser.Renderer.Canvas.CanvasRenderer , Phaser.Renderer.WebGL.WebGLRenderer ​
Description:
The renderer in use by this Text object.
Source: src/gameobjects/text/Text.js#L118
Since: 3.12.0
splitRegExp ​
splitRegExp: object ​
Description:
The Regular Expression that is used to split the text up into lines, in
multi-line text. By default this is /(?:\r\n|\r|\n)/ .
You can change this RegExp to be anything else that you may need.
Source: src/gameobjects/text/Text.js#L171
Since: 3.0.0
style ​
style: Phaser.GameObjects.TextStyle ​
Description:
The Text Style object.
Manages the style of this Text object.
Source: src/gameobjects/text/Text.js#L150
Since: 3.0.0
text ​
text: string ​
Description:
The text string being rendered by this Text Game Object.
Source: src/gameobjects/text/Text.js#L1487
Since: 3.0.0
width ​
width: number ​
Description:
The width of this Text object.
Overrides: Phaser.GameObjects.Components.ComputedSize#width
Source: src/gameobjects/text/Text.js#L202
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
From Phaser.GameObjects.Components.ComputedSize :
setDisplaySize
setSize
From Phaser.GameObjects.Components.Crop :
setCrop
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
advancedWordWrap ​
<instance> advancedWordWrap(text, context, wordWrapWidth) ​
Description:
Advanced wrapping algorithm that will wrap words as the line grows longer than its horizontal
bounds. Consecutive spaces will be collapsed and replaced with a single space. Lines will be
trimmed of white space before processing. Throws an error if wordWrapWidth is less than a
single character.
Parameters:
name type optional description
text string No The text to perform word wrap detection against.
context CanvasRenderingContext2D No The Canvas Rendering Context.
wordWrapWidth number No The word wrap width.
Returns: string - The wrapped text.
Source: src/gameobjects/text/Text.js#L392
Since: 3.0.0
appendText ​
<instance> appendText(value, [addCR]) ​
Description:
Appends the given text to the content already being displayed by this Text object.
An array of strings will be joined with \n line breaks.
Parameters:
name type optional default description
value string | Array.<string> No The string, or array of strings, to be appended to the existing content of this Text object.
addCR boolean Yes true Insert a carriage-return before the string value.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L643
Since: 3.60.0
basicWordWrap ​
<instance> basicWordWrap(text, context, wordWrapWidth) ​
Description:
Greedy wrapping algorithm that will wrap words as the line grows longer than its horizontal
bounds. Spaces are not collapsed and whitespace is not trimmed.
Parameters:
name type optional description
text string No The text to perform word wrap detection against.
context CanvasRenderingContext2D No The Canvas Rendering Context.
wordWrapWidth number No The word wrap width.
Returns: string - The wrapped text.
Source: src/gameobjects/text/Text.js#L516
Since: 3.0.0
getTextMetrics ​
<instance> getTextMetrics() ​
Description:
Get the current text metrics.
Returns: Phaser.Types.GameObjects.Text.TextMetrics - The text metrics.
Source: src/gameobjects/text/Text.js#L1474
Since: 3.0.0
getWrappedText ​
<instance> getWrappedText([text]) ​
Description:
Runs the given text through this Text objects word wrapping and returns the results as an
array, where each element of the array corresponds to a wrapped line of text.
Parameters:
name type optional description
text string Yes The text for which the wrapping will be calculated. If unspecified, the Text objects current text will be used.
Returns: Array.<string> - An array of strings with the pieces of wrapped text.
Source: src/gameobjects/text/Text.js#L587
Since: 3.0.0
initRTL ​
<instance> initRTL() ​
Description:
Initialize right to left text.
Source: src/gameobjects/text/Text.js#L315
Since: 3.0.0
preDestroy ​
<instance> preDestroy() ​
Description:
Internal destroy handler, called as part of the destroy process.
Access: protected
Source: src/gameobjects/text/Text.js#L1539
Since: 3.0.0
runWordWrap ​
<instance> runWordWrap(text) ​
Description:
Greedy wrapping algorithm that will wrap words as the line grows longer than its horizontal
bounds.
Parameters:
name type optional description
text string No The text to perform word wrap detection against.
Returns: string - The text after wrapping has been applied.
Source: src/gameobjects/text/Text.js#L349
Since: 3.0.0
setAlign ​
<instance> setAlign([align]) ​
Description:
Set the alignment of the text in this Text object.
The argument can be one of: left , right , center or justify .
Alignment only works if the Text object has more than one line of text.
Parameters:
name type optional default description
align string Yes "'left'" The text alignment for multi-line text.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1022
Since: 3.0.0
setBackgroundColor ​
<instance> setBackgroundColor(color) ​
Description:
Set the background color.
Parameters:
name type optional description
color string No The background color.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L823
Since: 3.0.0
setColor ​
<instance> setColor(color) ​
Description:
Set the text fill color.
Parameters:
name type optional description
color string | CanvasGradient CanvasPattern No
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L858
Since: 3.0.0
setFill ​
<instance> setFill(color) ​
Description:
Set the fill style to be used by the Text object.
This can be any valid CanvasRenderingContext2D fillStyle value, such as
a color (in hex, rgb, rgba, hsl or named values), a gradient or a pattern.
See the MDN fillStyle docs for more details.
Parameters:
name type optional description
color string | CanvasGradient CanvasPattern No
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L838
Since: 3.0.0
setFixedSize ​
<instance> setFixedSize(width, height) ​
Description:
Set a fixed width and height for the text.
Pass in 0 for either of these parameters to disable fixed width or height respectively.
Parameters:
name type optional description
width number No The fixed width to set. 0 disables fixed width.
height number No The fixed height to set. 0 disables fixed height.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L805
Since: 3.0.0
setFont ​
<instance> setFont(font) ​
Description:
Set the font.
If a string is given, the font family is set.
If an object is given, the fontFamily , fontSize and fontStyle
properties of that object are set.
Important: The font name must be quoted if it contains certain combinations of digits or
special characters:
Text . setFont ( '"Press Start 2P"' ) ;
Equally, if you wish to provide a list of fallback fonts, then you should ensure they are all
quoted properly, too:
Text . setFont ( 'Georgia, "Goudy Bookletter 1911", Times, serif' ) ;
Parameters:
name type optional description
font string No The font family or font settings to set.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L708
Since: 3.0.0
setFontFamily ​
<instance> setFontFamily(family) ​
Description:
Set the font family.
Important: The font name must be quoted if it contains certain combinations of digits or
special characters:
Text . setFont ( '"Press Start 2P"' ) ;
Equally, if you wish to provide a list of fallback fonts, then you should ensure they are all
quoted properly, too:
Text . setFont ( 'Georgia, "Goudy Bookletter 1911", Times, serif' ) ;
Parameters:
name type optional description
family string No The font family.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L744
Since: 3.0.0
setFontSize ​
<instance> setFontSize(size) ​
Description:
Set the font size. Can be a string with a valid CSS unit, i.e. 16px , or a number.
Parameters:
name type optional description
size string | number No The font size.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L775
Since: 3.0.0
setFontStyle ​
<instance> setFontStyle(style) ​
Description:
Set the font style.
Parameters:
name type optional description
style string No The font style.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L790
Since: 3.0.0
setLetterSpacing ​
<instance> setLetterSpacing(value) ​
Description:
Sets the letter spacing value.
This will add, or remove spacing between each character of this Text Game Object. The value can be
either positive or negative. Positive values increase the space between each character, whilst negative
values decrease it. Note that some fonts are spaced naturally closer together than others.
Please understand that enabling this feature will cause Phaser to render each character in this Text object
one by one, rather than use a draw for the whole string. This makes it extremely expensive when used with
either long strings, or lots of strings in total. You will be better off creating bitmap font text if you
need to display large quantities of characters with fine control over the letter spacing.
Parameters:
name type optional description
value number No The amount to add to the letter width. Set to zero to disable.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1081
Since: 3.70.0
setLineSpacing ​
<instance> setLineSpacing(value) ​
Description:
Sets the line spacing value.
This value is added to the height of the font when calculating the overall line height.
This only has an effect if this Text object consists of multiple lines of text.
Parameters:
name type optional description
value number No The amount to add to the font height to achieve the overall line height.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1061
Since: 3.13.0
setMaxLines ​
<instance> setMaxLines([max]) ​
Description:
Set the maximum number of lines to draw.
Parameters:
name type optional default description
max number Yes 0 The maximum number of lines to draw.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1173
Since: 3.0.0
setPadding ​
<instance> setPadding(left, [top], [right], [bottom]) ​
Description:
Set the text padding.
'left' can be an object.
If only 'left' and 'top' are given they are treated as 'x' and 'y'.
Parameters:
name type optional description
left number | Phaser.Types.GameObjects.Text.TextPadding No The left padding value, or a padding config object.
top number Yes The top padding value.
right number Yes The right padding value.
bottom number Yes The bottom padding value.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1107
Since: 3.0.0
setResolution ​
<instance> setResolution(value) ​
Description:
Set the resolution used by this Text object.
It allows for much clearer text on High DPI devices, at the cost of memory because it uses larger
internal Canvas textures for the Text.
Therefore, please use with caution, as the more high res Text you have, the more memory it uses.
Parameters:
name type optional description
value number No The resolution for this Text object to use.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1041
Since: 3.12.0
setRTL ​
<instance> setRTL([rtl]) ​
Description:
Render text from right-to-left or left-to-right.
Parameters:
name type optional default description
rtl boolean Yes true Set to true to render from right-to-left.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1188
Since: 3.70.0
setShadow ​
<instance> setShadow([x], [y], [color], [blur], [shadowStroke], [shadowFill]) ​
Description:
Set the shadow settings.
Parameters:
name type optional default description
x number Yes 0 The horizontal shadow offset.
y number Yes 0 The vertical shadow offset.
color string Yes "'#000'" The shadow color.
blur number Yes 0 The shadow blur radius.
shadowStroke boolean Yes false Whether to stroke the shadow.
shadowFill boolean Yes true Whether to fill the shadow.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L889
Since: 3.0.0
setShadowBlur ​
<instance> setShadowBlur(blur) ​
Description:
Set the shadow blur radius.
Parameters:
name type optional description
blur number No The shadow blur radius.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L940
Since: 3.0.0
setShadowColor ​
<instance> setShadowColor(color) ​
Description:
Set the shadow color.
Parameters:
name type optional description
color string No The shadow color.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L925
Since: 3.0.0
setShadowFill ​
<instance> setShadowFill(enabled) ​
Description:
Enable or disable shadow fill.
Parameters:
name type optional description
enabled boolean No Whether shadow fill is enabled or not.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L970
Since: 3.0.0
setShadowOffset ​
<instance> setShadowOffset(x, y) ​
Description:
Set the shadow offset.
Parameters:
name type optional description
x number No The horizontal shadow offset.
y number No The vertical shadow offset.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L909
Since: 3.0.0
setShadowStroke ​
<instance> setShadowStroke(enabled) ​
Description:
Enable or disable shadow stroke.
Parameters:
name type optional description
enabled boolean No Whether shadow stroke is enabled or not.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L955
Since: 3.0.0
setStroke ​
<instance> setStroke(color, thickness) ​
Description:
Set the stroke settings.
Parameters:
name type optional description
color string | CanvasGradient CanvasPattern No
thickness number No The stroke thickness.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L873
Since: 3.0.0
setStyle ​
<instance> setStyle(style) ​
Description:
Set the text style.
Parameters:
name type optional description
style object No The style settings to set.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L684
Since: 3.0.0
setText ​
<instance> setText(value) ​
Description:
Set the text to display.
An array of strings will be joined with \n line breaks.
Parameters:
name type optional description
value string | Array.<string> No The string, or array of strings, to be set as the content of this Text object.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L609
Since: 3.0.0
setWordWrapCallback ​
<instance> setWordWrapCallback(callback, [scope]) ​
Description:
Set a custom callback for wrapping lines. Pass in null to remove wrapping by callback.
Parameters:
name type optional default description
callback TextStyleWordWrapCallback No A custom function that will be responsible for wrapping the text. It will receive two arguments: text (the string to wrap), textObject (this Text instance). It should return the wrapped lines either as an array of lines or as a string with newline characters in place to indicate where breaks should happen.
scope object Yes null The scope that will be applied when the callback is invoked.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1003
Since: 3.0.0
setWordWrapWidth ​
<instance> setWordWrapWidth(width, [useAdvancedWrap]) ​
Description:
Set the width (in pixels) to use for wrapping lines. Pass in null to remove wrapping by width.
Parameters:
name type optional default description
width number | null No The maximum width of a line in pixels. Set to null to remove wrapping.
useAdvancedWrap boolean Yes false Whether or not to use the advanced wrapping algorithm. If true, spaces are collapsed and whitespace is trimmed from lines. If false, spaces and whitespace are left as is.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L985
Since: 3.0.0
toJSON ​
<instance> toJSON() ​
Description:
Build a JSON representation of the Text object.
Overrides: Phaser.GameObjects.GameObject#toJSON
Returns: Phaser.Types.GameObjects.JSONGameObject - A JSON representation of the Text object.
Source: src/gameobjects/text/Text.js#L1508
Since: 3.0.0
updateText ​
<instance> updateText() ​
Description:
Update the displayed text.
Returns: Phaser.GameObjects.Text - This Text object.
Source: src/gameobjects/text/Text.js#L1237
Since: 3.0.0
Previous
Star
Next
TextStyle
Inherited Members
Public Members
autoRound
canvas
context
height
letterSpacing
lineSpacing
padding
renderer
splitRegExp
style
text
width
Inherited Methods
Public Methods
advancedWordWrap
appendText
basicWordWrap
getTextMetrics
getWrappedText
initRTL
preDestroy
runWordWrap
setAlign
setBackgroundColor
setColor
setFill
setFixedSize
setFont
setFontFamily
setFontSize
setFontStyle
setLetterSpacing
setLineSpacing
setMaxLines
setPadding
setResolution
setRTL
setShadow
setShadowBlur
setShadowColor
setShadowFill
setShadowOffset
setShadowStroke
setStroke
setStyle
setText
setWordWrapCallback
setWordWrapWidth
toJSON
updateText
