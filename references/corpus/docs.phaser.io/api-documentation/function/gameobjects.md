# Phaser.GameObjects | Phaser Help

Source: https://docs.phaser.io/api-documentation/function/gameobjects

Phaser API Documentation
Functions
Phaser.GameObjects
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.GameObjectFactory
register ​
<static> register(factoryType, factoryFunction) ​
Description:
Static method called directly by the Game Object factory functions.
With this method you can register a custom GameObject factory in the GameObjectFactory,
providing a name ( factoryType ) and the constructor ( factoryFunction ) in order
to be called when you call to Phaser.Scene.add[ factoryType ] method.
Parameters:
name type optional description
factoryType string No The key of the factory that you will use to call to Phaser.Scene.add[ factoryType ] method.
factoryFunction function No The constructor function to be called when you invoke to the Phaser.Scene.add method.
Source: src/gameobjects/GameObjectFactory.js#L185
Since: 3.0.0
remove ​
<static> remove(factoryType) ​
Description:
Static method called directly by the Game Object factory functions.
With this method you can remove a custom GameObject factory registered in the GameObjectFactory,
providing a its factoryType .
Parameters:
name type optional description
factoryType string No The key of the factory that you want to remove from the GameObjectFactory.
Source: src/gameobjects/GameObjectFactory.js#L206
Since: 3.0.0
BuildGameObject ​
<static> BuildGameObject(scene, gameObject, config) ​
Description:
Builds a Game Object using the provided configuration object.
Parameters:
name type optional description
scene Phaser.Scene No A reference to the Scene.
gameObject Phaser.GameObjects.GameObject No The initial GameObject.
config Phaser.Types.GameObjects.GameObjectConfig No The config to build the GameObject with.
Returns: Phaser.GameObjects.GameObject - The built Game Object.
Source: src/gameobjects/BuildGameObject.js#L10
Since: 3.0.0
BuildGameObjectAnimation ​
<static> BuildGameObjectAnimation(sprite, config) ​
Description:
Adds an Animation component to a Sprite and populates it based on the given config.
Parameters:
name type optional description
sprite Phaser.GameObjects.Sprite No The sprite to add an Animation component to.
config object No The animation config.
Returns: Phaser.GameObjects.Sprite - The updated Sprite.
Source: src/gameobjects/BuildGameObjectAnimation.js#L9
Since: 3.0.0
GetCalcMatrix ​
<static> GetCalcMatrix(src, camera, [parentMatrix]) ​
Description:
Calculates the Transform Matrix of the given Game Object and Camera, factoring in
the parent matrix if provided.
Note that the object this results contains references to the Transform Matrices,
not new instances of them. Therefore, you should use their values immediately, or
copy them to your own matrix, as they will be replaced as soon as another Game
Object is rendered.
Parameters:
name type optional description
src Phaser.GameObjects.GameObject No The Game Object to calculate the transform matrix for.
camera Phaser.Cameras.Scene2D.Camera No The camera being used to render the Game Object.
parentMatrix Phaser.GameObjects.Components.TransformMatrix Yes The transform matrix of the parent container, if any.
Returns: Phaser.Types.GameObjects.GetCalcMatrixResults - The results object containing the updated transform matrices.
Source: src/gameobjects/GetCalcMatrix.js#L15
Since: 3.50.0
GetTextSize ​
<static> GetTextSize(text, size, lines) ​
Description:
Returns an object containing dimensions of the Text object.
Parameters:
name type optional description
text Phaser.GameObjects.Text No The Text object to calculate the size from.
size Phaser.Types.GameObjects.Text.TextMetrics No The Text metrics to use when calculating the size.
lines Array.<string> No The lines of text to calculate the size from.
Returns: Phaser.Types.GameObjects.Text.GetTextSizeObject - An object containing dimensions of the Text object.
Source: src/gameobjects/text/GetTextSize.js#L7
Since: 3.0.0
MeasureText ​
<static> MeasureText(textStyle) ​
Description:
Calculates the ascent, descent and fontSize of a given font style.
Parameters:
name type optional description
textStyle Phaser.GameObjects.TextStyle No The TextStyle object to measure.
Returns: Phaser.Types.GameObjects.Text.TextMetrics - An object containing the ascent, descent and fontSize of the TextStyle.
Source: src/gameobjects/text/MeasureText.js#L9
Since: 3.0.0
Phaser.GameObjects.GameObjectCreator
register ​
<static> register(factoryType, factoryFunction) ​
Description:
Static method called directly by the Game Object creator functions.
With this method you can register a custom GameObject factory in the GameObjectCreator,
providing a name ( factoryType ) and the constructor ( factoryFunction ) in order
to be called when you invoke Phaser.Scene.make[ factoryType ] method.
Parameters:
name type optional description
factoryType string No The key of the factory that you will use to call to Phaser.Scene.make[ factoryType ] method.
factoryFunction function No The constructor function to be called when you invoke to the Phaser.Scene.make method.
Source: src/gameobjects/GameObjectCreator.js#L154
Since: 3.0.0
remove ​
<static> remove(factoryType) ​
Description:
Static method called directly by the Game Object Creator functions.
With this method you can remove a custom Game Object Creator that has been previously
registered in the Game Object Creator. Pass in its factoryType in order to remove it.
Parameters:
name type optional description
factoryType string No The key of the factory that you want to remove from the GameObjectCreator.
Source: src/gameobjects/GameObjectCreator.js#L175
Since: 3.0.0
Phaser.GameObjects.RetroFont
Parse ​
<static> Parse(scene, config) ​
Description:
Parses a Retro Font configuration object so you can pass it to the BitmapText constructor
and create a BitmapText object using a fixed-width retro font.
Parameters:
name type optional description
scene Phaser.Scene No A reference to the Phaser Scene.
config Phaser.Types.GameObjects.BitmapText.RetroFontConfig No The font configuration object.
Returns: Phaser.Types.GameObjects.BitmapText.BitmapFontData - A parsed Bitmap Font data entry for the Bitmap Font cache.
Source: src/gameobjects/bitmaptext/ParseRetroFont.js#L9
Since: 3.0.0
Phaser.GameObjects.BitmapText
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
Phaser.GameObjects.Components
ToJSON ​
<static> ToJSON(gameObject) ​
Description:
Build a JSON representation of the given Game Object.
This is typically extended further by Game Object specific implementations.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to export as JSON.
Returns: Phaser.Types.GameObjects.JSONGameObject - A JSON representation of the Game Object.
Source: src/gameobjects/components/ToJSON.js#L7
Since: 3.0.0
Previous
Phaser.Display
Next
Phaser.Geom
register
remove
BuildGameObject
BuildGameObjectAnimation
GetCalcMatrix
GetTextSize
MeasureText
register
remove
Parse
ParseFromAtlas
ParseXMLBitmapFont
ToJSON
