# Input.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/event/input-events

Phaser API Documentation
Events
Input.Events
Version: Phaser v3.90.0
On this page
Input.Events
BOOT ​
Description: The Input Plugin Boot Event.
This internal event is dispatched by the Input Plugin when it boots, signalling to all of its systems to create themselves.
Member of: Phaser.Input.Events
Source: src/input/events/BOOT_EVENT.js#L7
Since: 3.0.0
DESTROY ​
Description: The Input Plugin Destroy Event.
This internal event is dispatched by the Input Plugin when it is destroyed, signalling to all of its systems to destroy themselves.
Member of: Phaser.Input.Events
Source: src/input/events/DESTROY_EVENT.js#L7
Since: 3.0.0
DRAG_END ​
Description: The Pointer Drag End Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer stops dragging a Game Object.
Listen to this event from within a Scene using: this.input.on('dragend', listener) .
To listen for this event from a specific Game Object, use the [GAMEOBJECT_DRAG_END]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DRAG_END} event instead.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The interactive Game Object that this pointer stopped dragging.
dropped boolean No Whether the Game Object was dropped onto a target.
Member of: Phaser.Input.Events
Source: src/input/events/DRAG_END_EVENT.js#L7
Since: 3.0.0
DRAG_ENTER ​
Description: The Pointer Drag Enter Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer drags a Game Object into a Drag Target.
Listen to this event from within a Scene using: this.input.on('dragenter', listener) .
A Pointer can only drag a single Game Object at once.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_DRAG_ENTER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DRAG_ENTER} event instead.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The interactive Game Object that this pointer is dragging.
target Phaser.GameObjects.GameObject No The drag target that this pointer has moved into.
Member of: Phaser.Input.Events
Source: src/input/events/DRAG_ENTER_EVENT.js#L7
Since: 3.0.0
DRAG ​
Description: The Pointer Drag Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves while dragging a Game Object.
Listen to this event from within a Scene using: this.input.on('drag', listener) .
A Pointer can only drag a single Game Object at once.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_DRAG]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DRAG} event instead.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The interactive Game Object that this pointer is dragging.
dragX number No The x coordinate where the Pointer is currently dragging the Game Object, in world space.
dragY number No The y coordinate where the Pointer is currently dragging the Game Object, in world space.
Member of: Phaser.Input.Events
Source: src/input/events/DRAG_EVENT.js#L7
Since: 3.0.0
DRAG_LEAVE ​
Description: The Pointer Drag Leave Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer drags a Game Object out of a Drag Target.
Listen to this event from within a Scene using: this.input.on('dragleave', listener) .
A Pointer can only drag a single Game Object at once.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_DRAG_LEAVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DRAG_LEAVE} event instead.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The interactive Game Object that this pointer is dragging.
target Phaser.GameObjects.GameObject No The drag target that this pointer has left.
Member of: Phaser.Input.Events
Source: src/input/events/DRAG_LEAVE_EVENT.js#L7
Since: 3.0.0
DRAG_OVER ​
Description: The Pointer Drag Over Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer drags a Game Object over a Drag Target.
When the Game Object first enters the drag target it will emit a dragenter event. If it then moves while within
the drag target, it will emit this event instead.
Listen to this event from within a Scene using: this.input.on('dragover', listener) .
A Pointer can only drag a single Game Object at once.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_DRAG_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DRAG_OVER} event instead.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The interactive Game Object that this pointer is dragging.
target Phaser.GameObjects.GameObject No The drag target that this pointer has moved over.
Member of: Phaser.Input.Events
Source: src/input/events/DRAG_OVER_EVENT.js#L7
Since: 3.0.0
DRAG_START ​
Description: The Pointer Drag Start Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer starts to drag any Game Object.
Listen to this event from within a Scene using: this.input.on('dragstart', listener) .
A Pointer can only drag a single Game Object at once.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_DRAG_START]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DRAG_START} event instead.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The interactive Game Object that this pointer is dragging.
Member of: Phaser.Input.Events
Source: src/input/events/DRAG_START_EVENT.js#L7
Since: 3.0.0
DROP ​
Description: The Pointer Drop Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer drops a Game Object on a Drag Target.
Listen to this event from within a Scene using: this.input.on('drop', listener) .
To listen for this event from a specific Game Object, use the [GAMEOBJECT_DROP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DROP} event instead.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The interactive Game Object that this pointer was dragging.
target Phaser.GameObjects.GameObject No The Drag Target the gameObject has been dropped on.
Member of: Phaser.Input.Events
Source: src/input/events/DROP_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DOWN ​
Description: The Game Object Down Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is pressed down on any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('gameobjectdown', listener) .
To receive this event, the Game Objects must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_POINTER_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_DOWN} event instead.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_DOWN}
[GAMEOBJECT_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DOWN}
[POINTER_DOWN]{@linkcode Phaser.Input.Events#event:POINTER_DOWN} or [POINTER_DOWN_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_DOWN_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The Game Object the pointer was pressed down on.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DOWN_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DRAG_END ​
Description: The Game Object Drag End Event.
This event is dispatched by an interactive Game Object if a pointer stops dragging it.
Listen to this event from a Game Object using: gameObject.on('dragend', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive and enabled for drag.
See GameObject.setInteractive for more details.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
dragX number No The x coordinate where the Pointer stopped dragging the Game Object, in world space.
dragY number No The y coordinate where the Pointer stopped dragging the Game Object, in world space.
dropped boolean No Whether the Game Object was dropped onto a target.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DRAG_END_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DRAG_ENTER ​
Description: The Game Object Drag Enter Event.
This event is dispatched by an interactive Game Object if a pointer drags it into a drag target.
Listen to this event from a Game Object using: gameObject.on('dragenter', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive and enabled for drag.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
target Phaser.GameObjects.GameObject No The drag target that this pointer has moved into.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DRAG_ENTER_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DRAG ​
Description: The Game Object Drag Event.
This event is dispatched by an interactive Game Object if a pointer moves while dragging it.
Listen to this event from a Game Object using: gameObject.on('drag', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive and enabled for drag.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
dragX number No The x coordinate where the Pointer is currently dragging the Game Object, in world space.
dragY number No The y coordinate where the Pointer is currently dragging the Game Object, in world space.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DRAG_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DRAG_LEAVE ​
Description: The Game Object Drag Leave Event.
This event is dispatched by an interactive Game Object if a pointer drags it out of a drag target.
Listen to this event from a Game Object using: gameObject.on('dragleave', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive and enabled for drag.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
target Phaser.GameObjects.GameObject No The drag target that this pointer has left.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DRAG_LEAVE_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DRAG_OVER ​
Description: The Game Object Drag Over Event.
This event is dispatched by an interactive Game Object if a pointer drags it over a drag target.
When the Game Object first enters the drag target it will emit a dragenter event. If it then moves while within
the drag target, it will emit this event instead.
Listen to this event from a Game Object using: gameObject.on('dragover', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive and enabled for drag.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
target Phaser.GameObjects.GameObject No The drag target that this pointer has moved over.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DRAG_OVER_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DRAG_START ​
Description: The Game Object Drag Start Event.
This event is dispatched by an interactive Game Object if a pointer starts to drag it.
Listen to this event from a Game Object using: gameObject.on('dragstart', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive and enabled for drag.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
There are lots of useful drag related properties that are set within the Game Object when dragging occurs.
For example, gameObject.input.dragStartX , dragStartY and so on.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
dragX number No The x coordinate where the Pointer is currently dragging the Game Object, in world space.
dragY number No The y coordinate where the Pointer is currently dragging the Game Object, in world space.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DRAG_START_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_DROP ​
Description: The Game Object Drop Event.
This event is dispatched by an interactive Game Object if a pointer drops it on a Drag Target.
Listen to this event from a Game Object using: gameObject.on('drop', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive and enabled for drag.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
target Phaser.GameObjects.GameObject No The Drag Target the gameObject has been dropped on.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_DROP_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_MOVE ​
Description: The Game Object Move Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is moved across any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('gameobjectmove', listener) .
To receive this event, the Game Objects must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_POINTER_MOVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_MOVE} event instead.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_MOVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_MOVE}
[GAMEOBJECT_MOVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_MOVE}
[POINTER_MOVE]{@linkcode Phaser.Input.Events#event:POINTER_MOVE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The Game Object the pointer was moved on.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_MOVE_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_OUT ​
Description: The Game Object Out Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves out of any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('gameobjectout', listener) .
To receive this event, the Game Objects must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_POINTER_OUT]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OUT} event instead.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_OUT]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OUT}
[GAMEOBJECT_OUT]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_OUT}
[POINTER_OUT]{@linkcode Phaser.Input.Events#event:POINTER_OUT}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
If the pointer leaves the game canvas itself, it will not trigger an this event. To handle those cases,
please listen for the [GAME_OUT]{@linkcode Phaser.Input.Events#event:GAME_OUT} event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The Game Object the pointer moved out of.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_OUT_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_OVER ​
Description: The Game Object Over Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves over any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('gameobjectover', listener) .
To receive this event, the Game Objects must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_POINTER_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OVER} event instead.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OVER}
[GAMEOBJECT_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_OVER}
[POINTER_OVER]{@linkcode Phaser.Input.Events#event:POINTER_OVER}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The Game Object the pointer moved over.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_OVER_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_POINTER_DOWN ​
Description: The Game Object Pointer Down Event.
This event is dispatched by an interactive Game Object if a pointer is pressed down on it.
Listen to this event from a Game Object using: gameObject.on('pointerdown', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_DOWN}
[GAMEOBJECT_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DOWN}
[POINTER_DOWN]{@linkcode Phaser.Input.Events#event:POINTER_DOWN} or [POINTER_DOWN_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_DOWN_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
localX number No The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
localY number No The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_POINTER_DOWN_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_POINTER_MOVE ​
Description: The Game Object Pointer Move Event.
This event is dispatched by an interactive Game Object if a pointer is moved while over it.
Listen to this event from a Game Object using: gameObject.on('pointermove', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_MOVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_MOVE}
[GAMEOBJECT_MOVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_MOVE}
[POINTER_MOVE]{@linkcode Phaser.Input.Events#event:POINTER_MOVE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
localX number No The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
localY number No The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_POINTER_MOVE_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_POINTER_OUT ​
Description: The Game Object Pointer Out Event.
This event is dispatched by an interactive Game Object if a pointer moves out of it.
Listen to this event from a Game Object using: gameObject.on('pointerout', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_OUT]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OUT}
[GAMEOBJECT_OUT]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_OUT}
[POINTER_OUT]{@linkcode Phaser.Input.Events#event:POINTER_OUT}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
If the pointer leaves the game canvas itself, it will not trigger an this event. To handle those cases,
please listen for the [GAME_OUT]{@linkcode Phaser.Input.Events#event:GAME_OUT} event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_POINTER_OUT_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_POINTER_OVER ​
Description: The Game Object Pointer Over Event.
This event is dispatched by an interactive Game Object if a pointer moves over it.
Listen to this event from a Game Object using: gameObject.on('pointerover', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OVER}
[GAMEOBJECT_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_OVER}
[POINTER_OVER]{@linkcode Phaser.Input.Events#event:POINTER_OVER}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
localX number No The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
localY number No The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_POINTER_OVER_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_POINTER_UP ​
Description: The Game Object Pointer Up Event.
This event is dispatched by an interactive Game Object if a pointer is released while over it.
Listen to this event from a Game Object using: gameObject.on('pointerup', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_UP}
[GAMEOBJECT_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_UP}
[POINTER_UP]{@linkcode Phaser.Input.Events#event:POINTER_UP} or [POINTER_UP_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_UP_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
localX number No The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
localY number No The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_POINTER_UP_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_POINTER_WHEEL ​
Description: The Game Object Pointer Wheel Event.
This event is dispatched by an interactive Game Object if a pointer has its wheel moved while over it.
Listen to this event from a Game Object using: gameObject.on('wheel', listener) .
Note that the scope of the listener is automatically set to be the Game Object instance itself.
To receive this event, the Game Object must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_WHEEL]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_WHEEL}
[GAMEOBJECT_WHEEL]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_WHEEL}
[POINTER_WHEEL]{@linkcode Phaser.Input.Events#event:POINTER_WHEEL}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
deltaX number No The horizontal scroll amount that occurred due to the user moving a mouse wheel or similar input device.
deltaY number No The vertical scroll amount that occurred due to the user moving a mouse wheel or similar input device. This value will typically be less than 0 if the user scrolls up and greater than zero if scrolling down.
deltaZ number No The z-axis scroll amount that occurred due to the user moving a mouse wheel or similar input device.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_POINTER_WHEEL_EVENT.js#L7
Since: 3.18.0
GAMEOBJECT_UP ​
Description: The Game Object Up Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is released while over any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('gameobjectup', listener) .
To receive this event, the Game Objects must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_POINTER_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_UP} event instead.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_UP}
[GAMEOBJECT_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_UP}
[POINTER_UP]{@linkcode Phaser.Input.Events#event:POINTER_UP} or [POINTER_UP_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_UP_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The Game Object the pointer was over when released.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_UP_EVENT.js#L7
Since: 3.0.0
GAMEOBJECT_WHEEL ​
Description: The Game Object Wheel Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer has its wheel moved while over any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('gameobjectwheel', listener) .
To receive this event, the Game Objects must have been set as interactive.
See [GameObject.setInteractive]{@link Phaser.GameObjects.GameObject#setInteractive} for more details.
To listen for this event from a specific Game Object, use the [GAMEOBJECT_POINTER_WHEEL]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_WHEEL} event instead.
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_WHEEL]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_WHEEL}
[GAMEOBJECT_WHEEL]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_WHEEL}
[POINTER_WHEEL]{@linkcode Phaser.Input.Events#event:POINTER_WHEEL}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
gameObject Phaser.GameObjects.GameObject No The Game Object the pointer was over when the wheel changed.
deltaX number No The horizontal scroll amount that occurred due to the user moving a mouse wheel or similar input device.
deltaY number No The vertical scroll amount that occurred due to the user moving a mouse wheel or similar input device. This value will typically be less than 0 if the user scrolls up and greater than zero if scrolling down.
deltaZ number No The z-axis scroll amount that occurred due to the user moving a mouse wheel or similar input device.
event Phaser.Types.Input.EventData No The Phaser input event. You can call stopPropagation() to halt it from going any further in the event flow.
Member of: Phaser.Input.Events
Source: src/input/events/GAMEOBJECT_WHEEL_EVENT.js#L7
Since: 3.18.0
GAME_OUT ​
Description: The Input Plugin Game Out Event.
This event is dispatched by the Input Plugin if the active pointer leaves the game canvas and is now
outside of it, elsewhere on the web page.
Listen to this event from within a Scene using: this.input.on('gameout', listener) .
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
event MouseEvent | TouchEvent No The DOM Event that triggered the canvas out.
Member of: Phaser.Input.Events
Source: src/input/events/GAME_OUT_EVENT.js#L7
Since: 3.16.1
GAME_OVER ​
Description: The Input Plugin Game Over Event.
This event is dispatched by the Input Plugin if the active pointer enters the game canvas and is now
over of it, having previously been elsewhere on the web page.
Listen to this event from within a Scene using: this.input.on('gameover', listener) .
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
event MouseEvent | TouchEvent No The DOM Event that triggered the canvas over.
Member of: Phaser.Input.Events
Source: src/input/events/GAME_OVER_EVENT.js#L7
Since: 3.16.1
MANAGER_BOOT ​
Description: The Input Manager Boot Event.
This internal event is dispatched by the Input Manager when it boots.
Member of: Phaser.Input.Events
Source: src/input/events/MANAGER_BOOT_EVENT.js#L7
Since: 3.0.0
MANAGER_PROCESS ​
Description: The Input Manager Process Event.
This internal event is dispatched by the Input Manager when not using the legacy queue system,
and it wants the Input Plugins to update themselves.
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Member of: Phaser.Input.Events
Source: src/input/events/MANAGER_PROCESS_EVENT.js#L7
Since: 3.0.0
MANAGER_UPDATE ​
Description: The Input Manager Update Event.
This internal event is dispatched by the Input Manager as part of its update step.
Member of: Phaser.Input.Events
Source: src/input/events/MANAGER_UPDATE_EVENT.js#L7
Since: 3.0.0
POINTERLOCK_CHANGE ​
Description: The Input Manager Pointer Lock Change Event.
This event is dispatched by the Input Manager when it is processing a native Pointer Lock Change DOM Event.
name type optional description
event Event No The native DOM Event.
locked boolean No The locked state of the Mouse Pointer.
Member of: Phaser.Input.Events
Source: src/input/events/POINTERLOCK_CHANGE_EVENT.js#L7
Since: 3.0.0
POINTER_DOWN ​
Description: The Pointer Down Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is pressed down anywhere.
Listen to this event from within a Scene using: this.input.on('pointerdown', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_DOWN}
[GAMEOBJECT_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DOWN}
[POINTER_DOWN]{@linkcode Phaser.Input.Events#event:POINTER_DOWN} or [POINTER_DOWN_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_DOWN_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
currentlyOver Array.< Phaser.GameObjects.GameObject > No An array containing all interactive Game Objects that the pointer was over when the event was created.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_DOWN_EVENT.js#L7
Since: 3.0.0
POINTER_DOWN_OUTSIDE ​
Description: The Pointer Down Outside Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is pressed down anywhere outside of the game canvas.
Listen to this event from within a Scene using: this.input.on('pointerdownoutside', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_DOWN}
[GAMEOBJECT_DOWN]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_DOWN}
[POINTER_DOWN]{@linkcode Phaser.Input.Events#event:POINTER_DOWN} or [POINTER_DOWN_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_DOWN_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_DOWN_OUTSIDE_EVENT.js#L7
Since: 3.16.1
POINTER_MOVE ​
Description: The Pointer Move Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is moved anywhere.
Listen to this event from within a Scene using: this.input.on('pointermove', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_MOVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_MOVE}
[GAMEOBJECT_MOVE]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_MOVE}
[POINTER_MOVE]{@linkcode Phaser.Input.Events#event:POINTER_MOVE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
currentlyOver Array.< Phaser.GameObjects.GameObject > No An array containing all interactive Game Objects that the pointer was over when the event was created.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_MOVE_EVENT.js#L7
Since: 3.0.0
POINTER_OUT ​
Description: The Pointer Out Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves out of any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('pointerout', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_OUT]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OUT}
[GAMEOBJECT_OUT]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_OUT}
[POINTER_OUT]{@linkcode Phaser.Input.Events#event:POINTER_OUT}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
If the pointer leaves the game canvas itself, it will not trigger an this event. To handle those cases,
please listen for the [GAME_OUT]{@linkcode Phaser.Input.Events#event:GAME_OUT} event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
justOut Array.< Phaser.GameObjects.GameObject > No An array containing all interactive Game Objects that the pointer moved out of when the event was created.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_OUT_EVENT.js#L7
Since: 3.0.0
POINTER_OVER ​
Description: The Pointer Over Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves over any interactive Game Object.
Listen to this event from within a Scene using: this.input.on('pointerover', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_OVER}
[GAMEOBJECT_OVER]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_OVER}
[POINTER_OVER]{@linkcode Phaser.Input.Events#event:POINTER_OVER}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
justOver Array.< Phaser.GameObjects.GameObject > No An array containing all interactive Game Objects that the pointer moved over when the event was created.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_OVER_EVENT.js#L7
Since: 3.0.0
POINTER_UP ​
Description: The Pointer Up Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is released anywhere.
Listen to this event from within a Scene using: this.input.on('pointerup', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_UP}
[GAMEOBJECT_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_UP}
[POINTER_UP]{@linkcode Phaser.Input.Events#event:POINTER_UP} or [POINTER_UP_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_UP_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
currentlyOver Array.< Phaser.GameObjects.GameObject > No An array containing all interactive Game Objects that the pointer was over when the event was created.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_UP_EVENT.js#L7
Since: 3.0.0
POINTER_UP_OUTSIDE ​
Description: The Pointer Up Outside Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer is released anywhere outside of the game canvas.
Listen to this event from within a Scene using: this.input.on('pointerupoutside', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_UP}
[GAMEOBJECT_UP]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_UP}
[POINTER_UP]{@linkcode Phaser.Input.Events#event:POINTER_UP} or [POINTER_UP_OUTSIDE]{@linkcode Phaser.Input.Events#event:POINTER_UP_OUTSIDE}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_UP_OUTSIDE_EVENT.js#L7
Since: 3.16.1
POINTER_WHEEL ​
Description: The Pointer Wheel Input Event.
This event is dispatched by the Input Plugin belonging to a Scene if a pointer has its wheel updated.
Listen to this event from within a Scene using: this.input.on('wheel', listener) .
The event hierarchy is as follows:
[GAMEOBJECT_POINTER_WHEEL]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_POINTER_WHEEL}
[GAMEOBJECT_WHEEL]{@linkcode Phaser.Input.Events#event:GAMEOBJECT_WHEEL}
[POINTER_WHEEL]{@linkcode Phaser.Input.Events#event:POINTER_WHEEL}
With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop
the propagation of this event.
name type optional description
pointer Phaser.Input.Pointer No The Pointer responsible for triggering this event.
currentlyOver Array.< Phaser.GameObjects.GameObject > No An array containing all interactive Game Objects that the pointer was over when the event was created.
deltaX number No The horizontal scroll amount that occurred due to the user moving a mouse wheel or similar input device.
deltaY number No The vertical scroll amount that occurred due to the user moving a mouse wheel or similar input device. This value will typically be less than 0 if the user scrolls up and greater than zero if scrolling down.
deltaZ number No The z-axis scroll amount that occurred due to the user moving a mouse wheel or similar input device.
Member of: Phaser.Input.Events
Source: src/input/events/POINTER_WHEEL_EVENT.js#L7
Since: 3.18.0
PRE_UPDATE ​
Description: The Input Plugin Pre-Update Event.
This internal event is dispatched by the Input Plugin at the start of its preUpdate method.
This hook is designed specifically for input plugins, but can also be listened to from user-land code.
Member of: Phaser.Input.Events
Source: src/input/events/PRE_UPDATE_EVENT.js#L7
Since: 3.0.0
SHUTDOWN ​
Description: The Input Plugin Shutdown Event.
This internal event is dispatched by the Input Plugin when it shuts down, signalling to all of its systems to shut themselves down.
Member of: Phaser.Input.Events
Source: src/input/events/SHUTDOWN_EVENT.js#L7
Since: 3.0.0
START ​
Description: The Input Plugin Start Event.
This internal event is dispatched by the Input Plugin when it has finished setting-up,
signalling to all of its internal systems to start.
Member of: Phaser.Input.Events
Source: src/input/events/START_EVENT.js#L7
Since: 3.0.0
UPDATE ​
Description: The Input Plugin Update Event.
This internal event is dispatched by the Input Plugin at the start of its update method.
This hook is designed specifically for input plugins, but can also be listened to from user-land code.
name type optional description
time number No The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout.
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Member of: Phaser.Input.Events
Source: src/input/events/UPDATE_EVENT.js#L7
Since: 3.0.0
Previous
GameObjects.Particles.Events
Next
Input.Gamepad.Events
BOOT
DESTROY
DRAG_END
DRAG_ENTER
DRAG
DRAG_LEAVE
DRAG_OVER
DRAG_START
DROP
GAMEOBJECT_DOWN
GAMEOBJECT_DRAG_END
GAMEOBJECT_DRAG_ENTER
GAMEOBJECT_DRAG
GAMEOBJECT_DRAG_LEAVE
GAMEOBJECT_DRAG_OVER
GAMEOBJECT_DRAG_START
GAMEOBJECT_DROP
GAMEOBJECT_MOVE
GAMEOBJECT_OUT
GAMEOBJECT_OVER
GAMEOBJECT_POINTER_DOWN
GAMEOBJECT_POINTER_MOVE
GAMEOBJECT_POINTER_OUT
GAMEOBJECT_POINTER_OVER
GAMEOBJECT_POINTER_UP
GAMEOBJECT_POINTER_WHEEL
GAMEOBJECT_UP
GAMEOBJECT_WHEEL
GAME_OUT
GAME_OVER
MANAGER_BOOT
MANAGER_PROCESS
MANAGER_UPDATE
POINTERLOCK_CHANGE
POINTER_DOWN
POINTER_DOWN_OUTSIDE
POINTER_MOVE
POINTER_OUT
POINTER_OVER
POINTER_UP
POINTER_UP_OUTSIDE
POINTER_WHEEL
PRE_UPDATE
SHUTDOWN
START
UPDATE
