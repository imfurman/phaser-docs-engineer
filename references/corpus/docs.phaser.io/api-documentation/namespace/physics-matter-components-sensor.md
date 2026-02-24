# Phaser.Physics.Matter.Components.Sensor | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-components-sensor

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.Components.Sensor
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.Components.Sensor
Scope: static
Source: src/physics/matter-js/components/Sensor.js#L7
Since: 3.0.0
Static functions ​
isSensor ​
<instance> isSensor() ​
Description:
Is the body belonging to this Game Object a sensor or not?
Returns: boolean - true if the body is a sensor, otherwise false .
Source: src/physics/matter-js/components/Sensor.js#L33
Since: 3.0.0
setSensor ​
<instance> setSensor(value) ​
Description:
Set the body belonging to this Game Object to be a sensor.
Sensors trigger collision events, but don't react with colliding body physically.
Parameters:
name type optional description
value boolean No true to set the body as a sensor, or false to disable it.
Returns: Phaser.Physics.Matter.Components.Sensor - This Game Object instance.
Source: src/physics/matter-js/components/Sensor.js#L15
Since: 3.0.0
Previous
Phaser.Physics.Matter.Components.Mass
Next
Phaser.Physics.Matter.Components.SetBody
Static functions
isSensor
setSensor
