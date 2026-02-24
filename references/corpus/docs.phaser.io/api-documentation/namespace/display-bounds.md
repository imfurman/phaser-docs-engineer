# Phaser.Display.Bounds | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/display-bounds

Phaser API Documentation
Namespaces
Phaser.Display.Bounds
Version: Phaser v3.90.0
On this page
Phaser.Display.Bounds
Scope: static
Source: src/display/bounds/index.js#L7
Static functions ​
CenterOn ​
<static> CenterOn(gameObject, x, y) ​
Description:
Positions the Game Object so that it is centered on the given coordinates.
Tags:
generic
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that will be re-positioned.
x number No The horizontal coordinate to position the Game Object on.
y number No The vertical coordinate to position the Game Object on.
Returns: Phaser.GameObjects.GameObject - The Game Object that was positioned.
Source: src/display/bounds/CenterOn.js#L10
Since: 3.0.0
GetBottom ​
<static> GetBottom(gameObject) ​
Description:
Returns the bottom coordinate from the bounds of the Game Object.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The bottom coordinate of the bounds of the Game Object.
Source: src/display/bounds/GetBottom.js#L7
Since: 3.0.0
GetBounds ​
<static> GetBounds(gameObject, [output]) ​
Description:
Returns the unrotated bounds of the Game Object as a rectangle.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
output Phaser.Geom.Rectangle | object Yes An object to store the values in. If not provided a new Rectangle will be created.
Returns: Phaser.Geom.Rectangle , object - - The bounds of the Game Object.
Source: src/display/bounds/GetBounds.js#L13
Since: 3.24.0
GetCenterX ​
<static> GetCenterX(gameObject) ​
Description:
Returns the center x coordinate from the bounds of the Game Object.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The center x coordinate of the bounds of the Game Object.
Source: src/display/bounds/GetCenterX.js#L7
Since: 3.0.0
GetCenterY ​
<static> GetCenterY(gameObject) ​
Description:
Returns the center y coordinate from the bounds of the Game Object.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The center y coordinate of the bounds of the Game Object.
Source: src/display/bounds/GetCenterY.js#L7
Since: 3.0.0
GetLeft ​
<static> GetLeft(gameObject) ​
Description:
Returns the left coordinate from the bounds of the Game Object.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The left coordinate of the bounds of the Game Object.
Source: src/display/bounds/GetLeft.js#L7
Since: 3.0.0
GetOffsetX ​
<static> GetOffsetX(gameObject) ​
Description:
Returns the amount the Game Object is visually offset from its x coordinate.
This is the same as width * origin.x .
This value will only be > 0 if origin.x is not equal to zero.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The horizontal offset of the Game Object.
Source: src/display/bounds/GetOffsetX.js#L7
Since: 3.0.0
GetOffsetY ​
<static> GetOffsetY(gameObject) ​
Description:
Returns the amount the Game Object is visually offset from its y coordinate.
This is the same as width * origin.y .
This value will only be > 0 if origin.y is not equal to zero.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The vertical offset of the Game Object.
Source: src/display/bounds/GetOffsetY.js#L7
Since: 3.0.0
GetRight ​
<static> GetRight(gameObject) ​
Description:
Returns the right coordinate from the bounds of the Game Object.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The right coordinate of the bounds of the Game Object.
Source: src/display/bounds/GetRight.js#L7
Since: 3.0.0
GetTop ​
<static> GetTop(gameObject) ​
Description:
Returns the top coordinate from the bounds of the Game Object.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to get the bounds value from.
Returns: number - The top coordinate of the bounds of the Game Object.
Source: src/display/bounds/GetTop.js#L7
Since: 3.0.0
SetBottom ​
<static> SetBottom(gameObject, value) ​
Description:
Positions the Game Object so that the bottom of its bounds aligns with the given coordinate.
Tags:
generic
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that will be re-positioned.
value number No The coordinate to position the Game Object bounds on.
Returns: Phaser.GameObjects.GameObject - The Game Object that was positioned.
Source: src/display/bounds/SetBottom.js#L7
Since: 3.0.0
SetCenterX ​
<static> SetCenterX(gameObject, x) ​
Description:
Positions the Game Object so that the center top of its bounds aligns with the given coordinate.
Tags:
generic
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that will be re-positioned.
x number No The coordinate to position the Game Object bounds on.
Returns: Phaser.GameObjects.GameObject - The Game Object that was positioned.
Source: src/display/bounds/SetCenterX.js#L7
Since: 3.0.0
SetCenterY ​
<static> SetCenterY(gameObject, y) ​
Description:
Positions the Game Object so that the center top of its bounds aligns with the given coordinate.
Tags:
generic
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that will be re-positioned.
y number No The coordinate to position the Game Object bounds on.
Returns: Phaser.GameObjects.GameObject - The Game Object that was positioned.
Source: src/display/bounds/SetCenterY.js#L7
Since: 3.0.0
SetLeft ​
<static> SetLeft(gameObject, value) ​
Description:
Positions the Game Object so that the left of its bounds aligns with the given coordinate.
Tags:
generic
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that will be re-positioned.
value number No The coordinate to position the Game Object bounds on.
Returns: Phaser.GameObjects.GameObject - The Game Object that was positioned.
Source: src/display/bounds/SetLeft.js#L7
Since: 3.0.0
SetRight ​
<static> SetRight(gameObject, value) ​
Description:
Positions the Game Object so that the left of its bounds aligns with the given coordinate.
Tags:
generic
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that will be re-positioned.
value number No The coordinate to position the Game Object bounds on.
Returns: Phaser.GameObjects.GameObject - The Game Object that was positioned.
Source: src/display/bounds/SetRight.js#L7
Since: 3.0.0
SetTop ​
<static> SetTop(gameObject, value) ​
Description:
Positions the Game Object so that the top of its bounds aligns with the given coordinate.
Tags:
generic
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that will be re-positioned.
value number No The coordinate to position the Game Object bounds on.
Returns: Phaser.GameObjects.GameObject - The Game Object that was positioned.
Source: src/display/bounds/SetTop.js#L7
Since: 3.0.0
Previous
Phaser.Display.Align
Next
Phaser.Display.Canvas.CanvasInterpolation
Static functions
CenterOn
GetBottom
GetBounds
GetCenterX
GetCenterY
GetLeft
GetOffsetX
GetOffsetY
GetRight
GetTop
SetBottom
SetCenterX
SetCenterY
SetLeft
SetRight
SetTop
