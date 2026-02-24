# Phaser.GameObjects | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects

Phaser API Documentation
Namespaces
Phaser.GameObjects
Version: Phaser v3.90.0
On this page
Phaser.GameObjects
Scope: static
Source: src/gameobjects/index.js#L7
Static functions ​
Arc
BitmapText
Blitter
Bob
Container
Curve
DisplayList
DOMElement
DynamicBitmapText
Ellipse
Extern
GameObject
GameObjectCreator
GameObjectFactory
Graphics
Grid
Group
Image
IsoBox
IsoTriangle
Layer
Light
LightsManager
LightsPlugin
Line
Mesh
NineSlice
PathFollower
Plane
PointLight
Polygon
Rectangle
RenderTexture
Rope
Shader
Shape
Sprite
Star
Text
TextStyle
TileSprite
Triangle
UpdateList
Video
Zone
Static functions ​
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
Static functions ​
Components
Events
Particles
RetroFont
Previous
Phaser.GameObjects.RetroFont
Next
Phaser.Geom.Intersects
Static functions
Static functions
BuildGameObject
BuildGameObjectAnimation
GetCalcMatrix
GetTextSize
MeasureText
Static functions
