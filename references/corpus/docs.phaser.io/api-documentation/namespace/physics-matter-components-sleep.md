# Phaser.Physics.Matter.Components.Sleep | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-matter-components-sleep

Phaser API Documentation
Namespaces
Phaser.Physics.Matter.Components.Sleep
Version: Phaser v3.90.0
On this page
Phaser.Physics.Matter.Components.Sleep
Scope: static
Source: src/physics/matter-js/components/Sleep.js#L11
Since: 3.0.0
Static functions ​
setAwake ​
<instance> setAwake() ​
Description:
Wakes this Body if asleep.
Returns: Phaser.Physics.Matter.Components.Sleep - This Game Object instance.
Source: src/physics/matter-js/components/Sleep.js#L34
Since: 3.22.0
setSleepEndEvent ​
<instance> setSleepEndEvent(value) ​
Description:
Enables or disables the Sleep End event for this body.
Parameters:
name type optional description
value boolean No true to enable the sleep event, or false to disable it.
Returns: Phaser.Physics.Matter.Components.Sleep - This Game Object instance.
Source: src/physics/matter-js/components/Sleep.js#L121
Since: 3.0.0
setSleepEvents ​
<instance> setSleepEvents(start, end) ​
Description:
Enable sleep and wake events for this body.
By default when a body goes to sleep, or wakes up, it will not emit any events.
The events are emitted by the Matter World instance and can be listened to via
the SLEEP_START and SLEEP_END events.
Parameters:
name type optional description
start boolean No true if you want the sleep start event to be emitted for this body.
end boolean No true if you want the sleep end event to be emitted for this body.
Returns: Phaser.Physics.Matter.Components.Sleep - This Game Object instance.
Source: src/physics/matter-js/components/Sleep.js#L68
Since: 3.0.0
setSleepStartEvent ​
<instance> setSleepStartEvent(value) ​
Description:
Enables or disables the Sleep Start event for this body.
Parameters:
name type optional description
value boolean No true to enable the sleep event, or false to disable it.
Returns: Phaser.Physics.Matter.Components.Sleep - This Game Object instance.
Source: src/physics/matter-js/components/Sleep.js#L92
Since: 3.0.0
setSleepThreshold ​
<instance> setSleepThreshold([value]) ​
Description:
Sets the number of updates in which this body must have near-zero velocity before it is set as sleeping (if sleeping is enabled by the engine).
Parameters:
name type optional default description
value number Yes 60 A Number that defines the number of updates in which this body must have near-zero velocity before it is set as sleeping.
Returns: Phaser.Physics.Matter.Components.Sleep - This Game Object instance.
Source: src/physics/matter-js/components/Sleep.js#L49
Since: 3.0.0
setToSleep ​
<instance> setToSleep() ​
Description:
Sets this Body to sleep.
Returns: Phaser.Physics.Matter.Components.Sleep - This Game Object instance.
Source: src/physics/matter-js/components/Sleep.js#L19
Since: 3.22.0
Previous
Phaser.Physics.Matter.Components.SetBody
Next
Phaser.Physics.Matter.Components.Static
Static functions
setAwake
setSleepEndEvent
setSleepEvents
setSleepStartEvent
setSleepThreshold
setToSleep
