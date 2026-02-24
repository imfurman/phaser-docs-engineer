# Phaser.GameObjects.Components.GetBounds | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-getbounds

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.GetBounds
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.GetBounds
Scope: static
Source: src/gameobjects/components/GetBounds.js#L11
Since: 3.0.0
Static functions ​
getBottomCenter ​
<instance> getBottomCenter([output], [includeParent]) ​
Description:
Gets the bottom-center coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L236
Since: 3.18.0
getBottomLeft ​
<instance> getBottomLeft([output], [includeParent]) ​
Description:
Gets the bottom-left corner coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L210
Since: 3.0.0
getBottomRight ​
<instance> getBottomRight([output], [includeParent]) ​
Description:
Gets the bottom-right corner coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L262
Since: 3.0.0
getBounds ​
<instance> getBounds([output]) ​
Description:
Gets the bounds of this Game Object, regardless of origin.
The values are stored and returned in a Rectangle, or Rectangle-like, object.
Tags:
generic
Parameters:
name type optional description
output Phaser.Geom.Rectangle | object Yes An object to store the values in. If not provided a new Rectangle will be created.
Returns: Phaser.Geom.Rectangle , object - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L288
Since: 3.0.0
getCenter ​
<instance> getCenter([output], [includeParent]) ​
Description:
Gets the center coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L54
Since: 3.0.0
getLeftCenter ​
<instance> getLeftCenter([output], [includeParent]) ​
Description:
Gets the left-center coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L158
Since: 3.18.0
getRightCenter ​
<instance> getRightCenter([output], [includeParent]) ​
Description:
Gets the right-center coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L184
Since: 3.18.0
getTopCenter ​
<instance> getTopCenter([output], [includeParent]) ​
Description:
Gets the top-center coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L106
Since: 3.18.0
getTopLeft ​
<instance> getTopLeft([output], [includeParent]) ​
Description:
Gets the top-left corner coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L80
Since: 3.0.0
getTopRight ​
<instance> getTopRight([output], [includeParent]) ​
Description:
Gets the top-right corner coordinate of this Game Object, regardless of origin.
The returned point is calculated in local space and does not factor in any parent Containers,
unless the includeParent argument is set to true .
Tags:
generic
Parameters:
name type optional default description
output Phaser.Types.Math.Vector2Like Yes An object to store the values in. If not provided a new Vector2 will be created.
includeParent boolean Yes false If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector?
Returns: Phaser.Types.Math.Vector2Like - The values stored in the output object.
Source: src/gameobjects/components/GetBounds.js#L132
Since: 3.0.0
Previous
Phaser.GameObjects.Components.Flip
Next
Phaser.GameObjects.Components.Mask
Static functions
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
