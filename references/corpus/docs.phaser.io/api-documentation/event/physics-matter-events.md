# Physics.Matter.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/event/physics-matter-events

Phaser API Documentation
Events
Physics.Matter.Events
Version: Phaser v3.90.0
On this page
Physics.Matter.Events
AFTER_ADD ​
Description: The Matter Physics After Add Event.
This event is dispatched by a Matter Physics World instance at the end of the process when a new Body
or Constraint has just been added to the world.
Listen to it from a Scene using: this.matter.world.on('afteradd', listener) .
name type optional description
event Phaser.Physics.Matter.Events.AfterAddEvent No The Add Event object.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/AFTER_ADD_EVENT.js#L15
Since: 3.22.0
AFTER_REMOVE ​
Description: The Matter Physics After Remove Event.
This event is dispatched by a Matter Physics World instance at the end of the process when a
Body or Constraint was removed from the world.
Listen to it from a Scene using: this.matter.world.on('afterremove', listener) .
name type optional description
event Phaser.Physics.Matter.Events.AfterRemoveEvent No The Remove Event object.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L15
Since: 3.22.0
AFTER_UPDATE ​
Description: The Matter Physics After Update Event.
This event is dispatched by a Matter Physics World instance after the engine has updated and all collision events have resolved.
Listen to it from a Scene using: this.matter.world.on('afterupdate', listener) .
name type optional description
event Phaser.Physics.Matter.Events.AfterUpdateEvent No The Update Event object.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L15
Since: 3.0.0
BEFORE_ADD ​
Description: The Matter Physics Before Add Event.
This event is dispatched by a Matter Physics World instance at the start of the process when a new Body
or Constraint is being added to the world.
Listen to it from a Scene using: this.matter.world.on('beforeadd', listener) .
name type optional description
event Phaser.Physics.Matter.Events.BeforeAddEvent No The Add Event object.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L15
Since: 3.22.0
BEFORE_REMOVE ​
Description: The Matter Physics Before Remove Event.
This event is dispatched by a Matter Physics World instance at the start of the process when a
Body or Constraint is being removed from the world.
Listen to it from a Scene using: this.matter.world.on('beforeremove', listener) .
name type optional description
event Phaser.Physics.Matter.Events.BeforeRemoveEvent No The Remove Event object.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L15
Since: 3.22.0
BEFORE_UPDATE ​
Description: The Matter Physics Before Update Event.
This event is dispatched by a Matter Physics World instance right before all the collision processing takes place.
Listen to it from a Scene using: this.matter.world.on('beforeupdate', listener) .
name type optional description
event Phaser.Physics.Matter.Events.BeforeUpdateEvent No The Update Event object.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L15
Since: 3.0.0
COLLISION_ACTIVE ​
Description: The Matter Physics Collision Active Event.
This event is dispatched by a Matter Physics World instance after the engine has updated.
It provides a list of all pairs that are colliding in the current tick (if any).
Listen to it from a Scene using: this.matter.world.on('collisionactive', listener) .
name type optional description
event Phaser.Physics.Matter.Events.CollisionActiveEvent No The Collision Event object.
bodyA MatterJS.BodyType No The first body of the first colliding pair. The event.pairs array may contain more colliding bodies.
bodyB MatterJS.BodyType No The second body of the first colliding pair. The event.pairs array may contain more colliding bodies.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L16
Since: 3.0.0
COLLISION_END ​
Description: The Matter Physics Collision End Event.
This event is dispatched by a Matter Physics World instance after the engine has updated.
It provides a list of all pairs that have finished colliding in the current tick (if any).
Listen to it from a Scene using: this.matter.world.on('collisionend', listener) .
name type optional description
event Phaser.Physics.Matter.Events.CollisionEndEvent No The Collision Event object.
bodyA MatterJS.BodyType No The first body of the first colliding pair. The event.pairs array may contain more colliding bodies.
bodyB MatterJS.BodyType No The second body of the first colliding pair. The event.pairs array may contain more colliding bodies.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/COLLISION_END_EVENT.js#L16
Since: 3.0.0
COLLISION_START ​
Description: The Matter Physics Collision Start Event.
This event is dispatched by a Matter Physics World instance after the engine has updated.
It provides a list of all pairs that have started to collide in the current tick (if any).
Listen to it from a Scene using: this.matter.world.on('collisionstart', listener) .
name type optional description
event Phaser.Physics.Matter.Events.CollisionStartEvent No The Collision Event object.
bodyA MatterJS.BodyType No The first body of the first colliding pair. The event.pairs array may contain more colliding bodies.
bodyB MatterJS.BodyType No The second body of the first colliding pair. The event.pairs array may contain more colliding bodies.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/COLLISION_START_EVENT.js#L16
Since: 3.0.0
DRAG_END ​
Description: The Matter Physics Drag End Event.
This event is dispatched by a Matter Physics World instance when a Pointer Constraint
stops dragging a body.
Listen to it from a Scene using: this.matter.world.on('dragend', listener) .
name type optional description
body MatterJS.BodyType No The Body that has stopped being dragged. This is a Matter Body, not a Phaser Game Object.
constraint Phaser.Physics.Matter.PointerConstraint No The Pointer Constraint that was dragging the body.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/DRAG_END_EVENT.js#L7
Since: 3.16.2
DRAG ​
Description: The Matter Physics Drag Event.
This event is dispatched by a Matter Physics World instance when a Pointer Constraint
is actively dragging a body. It is emitted each time the pointer moves.
Listen to it from a Scene using: this.matter.world.on('drag', listener) .
name type optional description
body MatterJS.BodyType No The Body that is being dragged. This is a Matter Body, not a Phaser Game Object.
constraint Phaser.Physics.Matter.PointerConstraint No The Pointer Constraint that is dragging the body.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/DRAG_EVENT.js#L7
Since: 3.16.2
DRAG_START ​
Description: The Matter Physics Drag Start Event.
This event is dispatched by a Matter Physics World instance when a Pointer Constraint
starts dragging a body.
Listen to it from a Scene using: this.matter.world.on('dragstart', listener) .
name type optional description
body MatterJS.BodyType No The Body that has started being dragged. This is a Matter Body, not a Phaser Game Object.
part MatterJS.BodyType No The part of the body that was clicked on.
constraint Phaser.Physics.Matter.PointerConstraint No The Pointer Constraint that is dragging the body.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/DRAG_START_EVENT.js#L7
Since: 3.16.2
PAUSE ​
Description: The Matter Physics World Pause Event.
This event is dispatched by an Matter Physics World instance when it is paused.
Listen to it from a Scene using: this.matter.world.on('pause', listener) .
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/PAUSE_EVENT.js#L7
Since: 3.0.0
RESUME ​
Description: The Matter Physics World Resume Event.
This event is dispatched by an Matter Physics World instance when it resumes from a paused state.
Listen to it from a Scene using: this.matter.world.on('resume', listener) .
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/RESUME_EVENT.js#L7
Since: 3.0.0
SLEEP_END ​
Description: The Matter Physics Sleep End Event.
This event is dispatched by a Matter Physics World instance when a Body stop sleeping.
Listen to it from a Scene using: this.matter.world.on('sleepend', listener) .
name type optional description
event Phaser.Physics.Matter.Events.SleepEndEvent No The Sleep Event object.
body MatterJS.BodyType No The body that has stopped sleeping.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/SLEEP_END_EVENT.js#L14
Since: 3.0.0
SLEEP_START ​
Description: The Matter Physics Sleep Start Event.
This event is dispatched by a Matter Physics World instance when a Body goes to sleep.
Listen to it from a Scene using: this.matter.world.on('sleepstart', listener) .
name type optional description
event Phaser.Physics.Matter.Events.SleepStartEvent No The Sleep Event object.
body MatterJS.BodyType No The body that has gone to sleep.
Member of: Phaser.Physics.Matter.Events
Source: src/physics/matter-js/events/SLEEP_START_EVENT.js#L14
Since: 3.0.0
Previous
Physics.Arcade.Events
Next
Renderer.Events
AFTER_ADD
AFTER_REMOVE
AFTER_UPDATE
BEFORE_ADD
BEFORE_REMOVE
BEFORE_UPDATE
COLLISION_ACTIVE
COLLISION_END
COLLISION_START
DRAG_END
DRAG
DRAG_START
PAUSE
RESUME
SLEEP_END
SLEEP_START
