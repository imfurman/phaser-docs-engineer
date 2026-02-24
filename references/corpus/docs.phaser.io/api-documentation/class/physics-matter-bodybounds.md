# BodyBounds | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-matter-bodybounds

Phaser API Documentation
Class
BodyBounds
Version: Phaser v3.90.0
On this page
BodyBounds
The Body Bounds class contains methods to help you extract the world coordinates from various points around
the bounds of a Matter Body. Because Matter bodies are positioned based on their center of mass, and not a
dimension based center, you often need to get the bounds coordinates in order to properly align them in the world.
You can access this class via the MatterPhysics class from a Scene, i.e.:
this . matter . bodyBounds . getTopLeft ( body ) ;
See also the MatterPhysics.alignBody method.
Scope : static
Source: src/physics/matter-js/BodyBounds.js#L10
Since: 3.22.0
Public Members ​
boundsCenter ​
boundsCenter: Phaser.Math.Vector2 ​
Description:
A Vector2 that stores the temporary bounds center value during calculations by methods in this class.
Source: src/physics/matter-js/BodyBounds.js#L36
Since: 3.22.0
centerDiff ​
centerDiff: Phaser.Math.Vector2 ​
Description:
A Vector2 that stores the temporary center diff values during calculations by methods in this class.
Source: src/physics/matter-js/BodyBounds.js#L45
Since: 3.22.0
Public Methods ​
getBottomCenter ​
<instance> getBottomCenter(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the bottom-center of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L330
Since: 3.22.0
getBottomLeft ​
<instance> getBottomLeft(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the bottom-left of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L296
Since: 3.22.0
getBottomRight ​
<instance> getBottomRight(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the bottom-right of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L364
Since: 3.22.0
getCenter ​
<instance> getCenter(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the center of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L229
Since: 3.22.0
getLeftCenter ​
<instance> getLeftCenter(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the left-center of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L195
Since: 3.22.0
getRightCenter ​
<instance> getRightCenter(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the right-center of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L262
Since: 3.22.0
getTopCenter ​
<instance> getTopCenter(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the top-center of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L127
Since: 3.22.0
getTopLeft ​
<instance> getTopLeft(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the top-left of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L93
Since: 3.22.0
getTopRight ​
<instance> getTopRight(body, [x], [y]) ​
Description:
Takes a Body and returns the world coordinates of the top-right of its bounds .
Body bounds are updated by Matter each step and factor in scale and rotation.
This will return the world coordinate based on the bodies current position and bounds.
Parameters:
name type optional default description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the position from.
x number Yes 0 Optional horizontal offset to add to the returned coordinates.
y number Yes 0 Optional vertical offset to add to the returned coordinates.
Returns: Phaser.Math.Vector2 , false - A Vector2 containing the coordinates, or false if it was unable to parse the body.
Source: src/physics/matter-js/BodyBounds.js#L161
Since: 3.22.0
parseBody ​
<instance> parseBody(body) ​
Description:
Parses the given body to get the bounds diff values from it.
They're stored in this class in the temporary properties boundsCenter and centerDiff .
This method is called automatically by all other methods in this class.
Parameters:
name type optional description
body Phaser.Types.Physics.Matter.MatterBody No The Body to get the bounds position from.
Returns: boolean - true if it was able to get the bounds, otherwise false .
Source: src/physics/matter-js/BodyBounds.js#L55
Since: 3.22.0
Previous
World
Next
Factory
Public Members
boundsCenter
centerDiff
Public Methods
getBottomCenter
getBottomLeft
getBottomRight
getCenter
getLeftCenter
getRightCenter
getTopCenter
getTopLeft
getTopRight
parseBody
