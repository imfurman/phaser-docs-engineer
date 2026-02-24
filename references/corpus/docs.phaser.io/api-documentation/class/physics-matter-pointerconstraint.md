# PointerConstraint | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/physics-matter-pointerconstraint

Phaser API Documentation
Class
PointerConstraint
Version: Phaser v3.90.0
On this page
PointerConstraint
A Pointer Constraint is a special type of constraint that allows you to click
and drag bodies in a Matter World. It monitors the active Pointers in a Scene,
and when one is pressed down it checks to see if that hit any part of any active
body in the world. If it did, and the body has input enabled, it will begin to
drag it until either released, or you stop it via the stopDrag method.
You can adjust the stiffness, length and other properties of the constraint via
the options object on creation.
Constructor
new PointerConstraint(scene, world, [options])
Parameters
name type optional description
scene Phaser.Scene No A reference to the Scene to which this Pointer Constraint belongs.
world Phaser.Physics.Matter.World No A reference to the Matter World instance to which this Constraint belongs.
options object Yes A Constraint configuration object.
Scope : static
Source: src/physics/matter-js/PointerConstraint.js#L19
Since: 3.0.0
Public Members ​
active ​
active: boolean ​
Description:
Is this Constraint active or not?
An active constraint will be processed each update. An inactive one will be skipped.
Use this to toggle a Pointer Constraint on and off.
Source: src/physics/matter-js/PointerConstraint.js#L102
Since: 3.0.0
body ​
body: MatterJS.BodyType ​
Description:
The body that is currently being dragged, if any.
Source: src/physics/matter-js/PointerConstraint.js#L124
Since: 3.16.2
camera ​
camera: Phaser.Cameras.Scene2D.Camera ​
Description:
The Camera the Pointer was interacting with when the input
down event was processed.
Source: src/physics/matter-js/PointerConstraint.js#L81
Since: 3.0.0
constraint ​
constraint: MatterJS.ConstraintType ​
Description:
The native Matter Constraint that is used to attach to bodies.
Source: src/physics/matter-js/PointerConstraint.js#L142
Since: 3.0.0
part ​
part: MatterJS.BodyType ​
Description:
The part of the body that was clicked on to start the drag.
Source: src/physics/matter-js/PointerConstraint.js#L133
Since: 3.16.2
pointer ​
pointer: Phaser.Input.Pointer ​
Description:
A reference to the Input Pointer that activated this Constraint.
This is set in the onDown handler.
Source: src/physics/matter-js/PointerConstraint.js#L91
Since: 3.0.0
position ​
position: Phaser.Math.Vector2 ​
Description:
The internal transformed position.
Source: src/physics/matter-js/PointerConstraint.js#L115
Since: 3.0.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene to which this Pointer Constraint belongs.
This is the same Scene as the Matter World instance.
Source: src/physics/matter-js/PointerConstraint.js#L62
Since: 3.0.0
world ​
world: Phaser.Physics.Matter.World ​
Description:
A reference to the Matter World instance to which this Constraint belongs.
Source: src/physics/matter-js/PointerConstraint.js#L72
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Pointer Constraint instance and all of its references.
Source: src/physics/matter-js/PointerConstraint.js#L359
Since: 3.0.0
getBody ​
<instance> getBody() ​
Description:
Scans all active bodies in the current Matter World to see if any of them
are hit by the Pointer. The first one found to hit is set as the active contraint
body.
Returns: boolean - true if a body was found and set, otherwise false .
Fires: Phaser.Physics.Matter.Events#event:DRAG_START
Source: src/physics/matter-js/PointerConstraint.js#L194
Since: 3.16.2
hitTestBody ​
<instance> hitTestBody(body, position) ​
Description:
Scans the current body to determine if a part of it was clicked on.
If a part is found the body is set as the constraint.bodyB property,
as well as the body property of this class. The part is also set.
Parameters:
name type optional description
body MatterJS.BodyType No The Matter Body to check.
position Phaser.Math.Vector2 No A translated hit test position.
Returns: boolean - true if a part of the body was hit, otherwise false .
Source: src/physics/matter-js/PointerConstraint.js#L234
Since: 3.16.2
onDown ​
<instance> onDown(pointer) ​
Description:
A Pointer has been pressed down onto the Scene.
If this Constraint doesn't have an active Pointer then a hit test is set to
run against all active bodies in the world during the next call to update .
If a body is found, it is bound to this constraint and the drag begins.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No A reference to the Pointer that was pressed.
Source: src/physics/matter-js/PointerConstraint.js#L157
Since: 3.0.0
onUp ​
<instance> onUp(pointer) ​
Description:
A Pointer has been released from the Scene. If it was the one this constraint was using, it's cleared.
Parameters:
name type optional description
pointer Phaser.Input.Pointer No A reference to the Pointer that was pressed.
Source: src/physics/matter-js/PointerConstraint.js#L178
Since: 3.22.0
stopDrag ​
<instance> stopDrag() ​
Description:
Stops the Pointer Constraint from dragging the body any further.
This is called automatically if the Pointer is released while actively
dragging a body. Or, you can call it manually to release a body from a
constraint without having to first release the pointer.
Fires: Phaser.Physics.Matter.Events#event:DRAG_END
Source: src/physics/matter-js/PointerConstraint.js#L330
Since: 3.16.2
update ​
<instance> update() ​
Description:
Internal update handler. Called in the Matter BEFORE_UPDATE step.
Fires: Phaser.Physics.Matter.Events#event:DRAG
Source: src/physics/matter-js/PointerConstraint.js#L278
Since: 3.0.0
Previous
MatterPhysics
Next
Sprite
Public Members
active
body
camera
constraint
part
pointer
position
scene
world
Public Methods
destroy
getBody
hitTestBody
onDown
onUp
stopDrag
update
