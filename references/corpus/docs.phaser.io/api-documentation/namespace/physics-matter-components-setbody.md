# Phaser.Physics.Matter.Components.SetBody | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-components-setbody

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.Components.SetBody
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.Components.SetBody
Scope: static
Source: src/physics/matter-js/components/SetBody.js#L15
Since: 3.0.0
Static functions ​
setBody ​
<instance> setBody(config, [options]) ​
Description:
Set this Game Object to create and use a new Body based on the configuration object given.
Calling this methods resets all previous properties you may have set on the body, including
plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.
Parameters:
name type optional description
config string | Phaser.Types.Physics.Matter.MatterSetBodyConfig No Either a string, such as circle , or a Matter Set Body Configuration object.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: Phaser.Physics.Matter.Components.SetBody - This Game Object instance.
Source: src/physics/matter-js/components/SetBody.js#L175
Since: 3.0.0
setCircle ​
<instance> setCircle(radius, [options]) ​
Description:
Set this Game Objects Matter physics body to be a circle shape.
Calling this methods resets all previous properties you may have set on the body, including
plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.
Parameters:
name type optional description
radius number No The radius of the circle.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: Phaser.Physics.Matter.Components.SetBody - This Game Object instance.
Source: src/physics/matter-js/components/SetBody.js#L43
Since: 3.0.0
setExistingBody ​
<instance> setExistingBody(body, [addToWorld]) ​
Description:
Set this Game Object to use the given existing Matter Body.
The body is first removed from the world before being added to this Game Object.
Parameters:
name type optional default description
body MatterJS.BodyType No The Body this Game Object should use.
addToWorld boolean Yes true Should the body be immediately added to the World?
Returns: Phaser.Physics.Matter.Components.SetBody - This Game Object instance.
Source: src/physics/matter-js/components/SetBody.js#L103
Since: 3.0.0
setPolygon ​
<instance> setPolygon(radius, sides, [options]) ​
Description:
Set this Game Objects Matter physics body to be a polygon shape.
Calling this methods resets all previous properties you may have set on the body, including
plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.
Parameters:
name type optional description
radius number No The "radius" of the polygon, i.e. the distance from its center to any vertex. This is also the radius of its circumcircle.
sides number No The number of sides the polygon will have.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: Phaser.Physics.Matter.Components.SetBody - This Game Object instance.
Source: src/physics/matter-js/components/SetBody.js#L62
Since: 3.0.0
setRectangle ​
<instance> setRectangle(width, height, [options]) ​
Description:
Set this Game Objects Matter physics body to be a rectangle shape.
Calling this methods resets all previous properties you may have set on the body, including
plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.
Parameters:
name type optional description
width number No Width of the rectangle.
height number No Height of the rectangle.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: Phaser.Physics.Matter.Components.SetBody - This Game Object instance.
Source: src/physics/matter-js/components/SetBody.js#L23
Since: 3.0.0
setTrapezoid ​
<instance> setTrapezoid(width, height, slope, [options]) ​
Description:
Set this Game Objects Matter physics body to be a trapezoid shape.
Calling this methods resets all previous properties you may have set on the body, including
plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.
Parameters:
name type optional description
width number No The width of the trapezoid Body.
height number No The height of the trapezoid Body.
slope number No The slope of the trapezoid. 0 creates a rectangle, while 1 creates a triangle. Positive values make the top side shorter, while negative values make the bottom side shorter.
options Phaser.Types.Physics.Matter.MatterBodyConfig Yes An optional Body configuration object that is used to set initial Body properties on creation.
Returns: Phaser.Physics.Matter.Components.SetBody - This Game Object instance.
Source: src/physics/matter-js/components/SetBody.js#L82
Since: 3.0.0
Previous
Phaser.Physics.Matter.Components.Sensor
Next
Phaser.Physics.Matter.Components.Sleep
Static functions
setBody
setCircle
setExistingBody
setPolygon
setRectangle
setTrapezoid
