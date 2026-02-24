# Phaser.Types.GameObjects.BitmapText | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/types-gameobjects-bitmaptext

Phaser API Documentation
Namespaces
Phaser.Types.GameObjects.BitmapText
Version: Phaser v3.90.0
On this page
Phaser.Types.GameObjects.BitmapText
Scope: static
Source: src/gameobjects/bitmaptext/typedefs/index.js#L7
Static functions ​
BitmapFontCharacterData ​
BitmapFontCharacterData ​
Description:
The font data for an individual character of a Bitmap Font.
Describes the character's position, size, offset and kerning.
As of version 3.50 it also includes the WebGL texture uv data.
Source: src/gameobjects/bitmaptext/typedefs/BitmapFontCharacterData.js#L1
Since: 3.0.0
BitmapFontData ​
BitmapFontData ​
Description:
Bitmap Font data that can be used by a BitmapText Game Object.
Source: src/gameobjects/bitmaptext/typedefs/BitmapFontData.js#L1
Since: 3.0.0
BitmapTextCharacter ​
BitmapTextCharacter ​
Description:
A single entry from the BitmapTextSize characters array.
The position and dimensions take the font size into account,
but are not translated into the local space of the Game Object itself.
Source: src/gameobjects/bitmaptext/typedefs/BitmapTextCharacter.js#L1
Since: 3.50.0
BitmapTextConfig ​
BitmapTextConfig ​
Source: src/gameobjects/bitmaptext/typedefs/BitmapTextConfig.js#L1
Since: 3.0.0
BitmapTextLines ​
BitmapTextLines ​
Description:
Details about the line data in the BitmapTextSize object.
Source: src/gameobjects/bitmaptext/typedefs/BitmapTextLines.js#L1
Since: 3.50.0
BitmapTextSize ​
BitmapTextSize ​
Source: src/gameobjects/bitmaptext/typedefs/BitmapTextSize.js#L1
Since: 3.0.0
BitmapTextWord ​
BitmapTextWord ​
Description:
Details about a single world entry in the BitmapTextSize object words array.
Source: src/gameobjects/bitmaptext/typedefs/BitmapTextWord.js#L1
Since: 3.50.0
DisplayCallback ​
DisplayCallback ​
Parameters:
name type optional description
display Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig No Settings of the character that is about to be rendered.
Returns: Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig - Altered position, scale and rotation values for the character that is about to be rendered.
Source: src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L16
DisplayCallbackConfig ​
DisplayCallbackConfig ​
Source: src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L1
Since: 3.0.0
GlobalBitmapTextSize ​
GlobalBitmapTextSize ​
Description:
The position and size of the Bitmap Text in global space, taking into account the Game Object's scale and world position.
Source: src/gameobjects/bitmaptext/typedefs/GlobalBitmapTextSize.js#L1
Since: 3.0.0
JSONBitmapText ​
JSONBitmapText ​
Source: src/gameobjects/bitmaptext/typedefs/JSONBitmapText.js#L1
Since: 3.0.0
LocalBitmapTextSize ​
LocalBitmapTextSize ​
Description:
The position and size of the Bitmap Text in local space, taking just the font size into account.
Source: src/gameobjects/bitmaptext/typedefs/LocalBitmapTextSize.js#L1
Since: 3.0.0
RetroFontConfig ​
RetroFontConfig ​
Source: src/gameobjects/bitmaptext/typedefs/RetroFontConfig.js#L1
Since: 3.6.0
TintConfig ​
TintConfig ​
Source: src/gameobjects/bitmaptext/typedefs/TintConfig.js#L1
Since: 3.0.0
Previous
Phaser.Types.Display
Next
Phaser.Types.GameObjects.Container
Static functions
BitmapFontCharacterData
BitmapFontData
BitmapTextCharacter
BitmapTextConfig
BitmapTextLines
BitmapTextSize
BitmapTextWord
DisplayCallback
DisplayCallbackConfig
GlobalBitmapTextSize
JSONBitmapText
LocalBitmapTextSize
RetroFontConfig
TintConfig
