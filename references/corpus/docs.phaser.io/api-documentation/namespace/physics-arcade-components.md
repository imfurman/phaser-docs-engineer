# Phaser.Physics.Arcade.Components | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-components

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.Components
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.Components
Scope: static
Source: src/physics/arcade/components/index.js#L7
Static functions ​
Acceleration
Angular
Bounce
Collision
Debug
Drag
Enable
Friction
Gravity
Immovable
Mass
Pushable
Size
Velocity
Static functions ​
OverlapCirc ​
<static> OverlapCirc(x, y, radius, [includeDynamic], [includeStatic]) ​
Description:
This method will search the given circular area and return an array of all physics bodies that
overlap with it. It can return either Dynamic, Static bodies or a mixture of both.
A body only has to intersect with the search area to be considered, it doesn't have to be fully
contained within it.
If Arcade Physics is set to use the RTree (which it is by default) then the search is rather fast,
otherwise the search is O(N) for Dynamic Bodies.
Parameters:
name type optional default description
x number No The x coordinate of the center of the area to search within.
y number No The y coordinate of the center of the area to search within.
radius number No The radius of the area to search within.
includeDynamic boolean Yes true Should the search include Dynamic Bodies?
includeStatic boolean Yes false Should the search include Static Bodies?
Returns: Array.< Phaser.Physics.Arcade.Body >, Array.< Phaser.Physics.Arcade.StaticBody > - An array of bodies that overlap with the given area.
Source: src/physics/arcade/components/OverlapCirc.js#L6
Since: 3.21.0
OverlapRect ​
<static> OverlapRect(x, y, width, height, [includeDynamic], [includeStatic]) ​
Description:
This method will search the given rectangular area and return an array of all physics bodies that
overlap with it. It can return either Dynamic, Static bodies or a mixture of both.
A body only has to intersect with the search area to be considered, it doesn't have to be fully
contained within it.
If Arcade Physics is set to use the RTree (which it is by default) then the search for is extremely fast,
otherwise the search is O(N) for Dynamic Bodies.
Parameters:
name type optional default description
x number No The top-left x coordinate of the area to search within.
y number No The top-left y coordinate of the area to search within.
width number No The width of the area to search within.
height number No The height of the area to search within.
includeDynamic boolean Yes true Should the search include Dynamic Bodies?
includeStatic boolean Yes false Should the search include Static Bodies?
Returns: Array.< Phaser.Physics.Arcade.Body >, Array.< Phaser.Physics.Arcade.StaticBody > - An array of bodies that overlap with the given area.
Source: src/physics/arcade/components/OverlapRect.js#L1
Since: 3.17.0
Previous
Phaser.Physics.Arcade.Components.Velocity
Next
Phaser.Physics.Arcade.Events
Static functions
Static functions
OverlapCirc
OverlapRect
