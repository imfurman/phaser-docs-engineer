# Physics.Matter.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/physics-matter-events

Phaser API Documentation
Typedefs
Physics.Matter.Events
Version: Phaser v3.90.0
On this page
Physics.Matter.Events
AfterAddEvent ​
<static> AfterAddEvent ​
name type optional description
object Array.<any> No An array of the object(s) that have been added. May be a single body, constraint, composite or a mixture of these.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/AFTER_ADD_EVENT.js#L7
AfterRemoveEvent ​
<static> AfterRemoveEvent ​
name type optional description
object Array.<any> No An array of the object(s) that were removed. May be a single body, constraint, composite or a mixture of these.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L7
AfterUpdateEvent ​
<static> AfterUpdateEvent ​
name type optional description
timestamp number No The Matter Engine timing.timestamp value for the event.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L7
BeforeAddEvent ​
<static> BeforeAddEvent ​
name type optional description
object Array.<any> No An array of the object(s) to be added. May be a single body, constraint, composite or a mixture of these.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L7
BeforeRemoveEvent ​
<static> BeforeRemoveEvent ​
name type optional description
object Array.<any> No An array of the object(s) to be removed. May be a single body, constraint, composite or a mixture of these.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L7
BeforeUpdateEvent ​
<static> BeforeUpdateEvent ​
name type optional description
timestamp number No The Matter Engine timing.timestamp value for the event.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L7
CollisionActiveEvent ​
<static> CollisionActiveEvent ​
name type optional description
pairs Array.< Phaser.Types.Physics.Matter.MatterCollisionPair > No A list of all affected pairs in the collision.
timestamp number No The Matter Engine timing.timestamp value for the event.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L7
CollisionEndEvent ​
<static> CollisionEndEvent ​
name type optional description
pairs Array.< Phaser.Types.Physics.Matter.MatterCollisionPair > No A list of all affected pairs in the collision.
timestamp number No The Matter Engine timing.timestamp value for the event.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/COLLISION_END_EVENT.js#L7
CollisionStartEvent ​
<static> CollisionStartEvent ​
name type optional description
pairs Array.< Phaser.Types.Physics.Matter.MatterCollisionPair > No A list of all affected pairs in the collision.
timestamp number No The Matter Engine timing.timestamp value for the event.
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/COLLISION_START_EVENT.js#L7
SleepEndEvent ​
<static> SleepEndEvent ​
name type optional description
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/SLEEP_END_EVENT.js#L7
SleepStartEvent ​
<static> SleepStartEvent ​
name type optional description
source any No The source object of the event.
name string No The name of the event.
Type : object
Member of : Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/SLEEP_START_EVENT.js#L7
Previous
Device
Next
Scale
AfterAddEvent
<static> AfterAddEvent
AfterRemoveEvent
<static> AfterRemoveEvent
AfterUpdateEvent
<static> AfterUpdateEvent
BeforeAddEvent
<static> BeforeAddEvent
BeforeRemoveEvent
<static> BeforeRemoveEvent
BeforeUpdateEvent
<static> BeforeUpdateEvent
CollisionActiveEvent
<static> CollisionActiveEvent
CollisionEndEvent
<static> CollisionEndEvent
CollisionStartEvent
<static> CollisionStartEvent
SleepEndEvent
<static> SleepEndEvent
SleepStartEvent
<static> SleepStartEvent
