# Pointer | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-pointer

Phaser API Documentation
Class
Pointer
Version: Phaser v3.90.0
On this page
Pointer
A Pointer object encapsulates both mouse and touch input within Phaser.
By default, Phaser will create 2 pointers for your game to use. If you require more, i.e. for a multi-touch
game, then use the InputPlugin.addPointer method to do so, rather than instantiating this class directly,
otherwise it won't be managed by the input system.
You can reference the current active pointer via InputPlugin.activePointer . You can also use the properties
InputPlugin.pointer1 through to pointer10 , for each pointer you have enabled in your game.
The properties of this object are set by the Input Plugin during processing. This object is then sent in all
input related events that the Input Plugin emits, so you can reference properties from it directly in your
callbacks.
Constructor
new Pointer(manager, id)
Parameters
name type optional description
manager Phaser.Input.InputManager No A reference to the Input Manager.
id number No The internal ID of this Pointer.
Scope : static
Source: src/input/Pointer.js#L15
Since: 3.0.0
Public Members ​
active ​
active: boolean ​
Description:
An active Pointer is one that is currently pressed down on the display.
A Mouse is always considered as active.
Source: src/input/Pointer.js#L438
Since: 3.10.0
angle ​
angle: number ​
Description:
The current angle the Pointer is moving, in radians, based on its previous and current position.
The angle is based on the old position facing to the current position.
This property is updated whenever the Pointer moves, regardless of any button states. In other words,
it changes based on movement alone - a button doesn't have to be pressed first.
Source: src/input/Pointer.js#L192
Since: 3.16.0
button ​
button: number ​
Description:
A read-only property that indicates which button was pressed, or released, on the pointer
during the most recent event. It is only set during up and down events.
On Touch devices the value is always 0.
Users may change the configuration of buttons on their pointing device so that if an event's button property
is zero, it may not have been caused by the button that is physically left–most on the pointing device;
however, it should behave as if the left button was clicked in the standard button layout.
Source: src/input/Pointer.js#L107
Since: 3.18.0
buttons ​
buttons: number ​
Description:
0: No button or un-initialized
1: Left button
2: Right button
4: Wheel button or middle button
8: 4th button (typically the "Browser Back" button)
16: 5th button (typically the "Browser Forward" button)
For a mouse configured for left-handed use, the button actions are reversed.
In this case, the values are read from right to left.
Source: src/input/Pointer.js#L125
Since: 3.0.0
camera ​
camera: Phaser.Cameras.Scene2D.Camera ​
Description:
The camera the Pointer interacted with during its last update.
A Pointer can only ever interact with one camera at once, which will be the top-most camera
in the list should multiple cameras be positioned on-top of each other.
Source: src/input/Pointer.js#L94
Since: 3.0.0
deltaX ​
deltaX: number ​
Description:
The horizontal scroll amount that occurred due to the user moving a mouse wheel or similar input device.
Source: src/input/Pointer.js#L464
Since: 3.18.0
deltaY ​
deltaY: number ​
Description:
The vertical scroll amount that occurred due to the user moving a mouse wheel or similar input device.
This value will typically be less than 0 if the user scrolls up and greater than zero if scrolling down.
Source: src/input/Pointer.js#L474
Since: 3.18.0
deltaZ ​
deltaZ: number ​
Description:
The z-axis scroll amount that occurred due to the user moving a mouse wheel or similar input device.
Source: src/input/Pointer.js#L485
Since: 3.18.0
distance ​
distance: number ​
Description:
The distance the Pointer has moved, based on its previous and current position.
This value is smoothed out each frame, according to the motionFactor property.
This property is updated whenever the Pointer moves, regardless of any button states. In other words,
it changes based on movement alone - a button doesn't have to be pressed first.
If you need the total distance travelled since the primary buttons was pressed down,
then use the Pointer.getDistance method.
Source: src/input/Pointer.js#L207
Since: 3.16.0
downElement ​
downElement: any ​
Description:
The DOM element the Pointer was pressed down on, taken from the DOM event.
In a default set-up this will be the Canvas that Phaser is rendering to, or the Window element.
Source: src/input/Pointer.js#L72
Since: 3.16.0
downTime ​
downTime: number ​
Description:
The Event timestamp when the first button, or Touch input, was pressed. Used for dragging objects.
Source: src/input/Pointer.js#L317
Since: 3.0.0
downX ​
downX: number ​
Description:
X coordinate of the Pointer when Button 1 (left button), or Touch, was pressed, used for dragging objects.
Source: src/input/Pointer.js#L297
Since: 3.0.0
downY ​
downY: number ​
Description:
Y coordinate of the Pointer when Button 1 (left button), or Touch, was pressed, used for dragging objects.
Source: src/input/Pointer.js#L307
Since: 3.0.0
event ​
event: TouchEvent, MouseEvent, WheelEvent ​
Description:
The most recent native DOM Event this Pointer has processed.
Source: src/input/Pointer.js#L63
Since: 3.0.0
id ​
id: number ​
Description:
The internal ID of this Pointer.
Source: src/input/Pointer.js#L53
Since: 3.0.0
identifier ​
identifier: number ​
Description:
The identifier property of the Pointer as set by the DOM event when this Pointer is started.
Source: src/input/Pointer.js#L419
Since: 3.10.0
isDown ​
isDown: boolean ​
Description:
Is any button on this pointer considered as being down?
Source: src/input/Pointer.js#L367
Since: 3.0.0
locked ​
locked: boolean ​
Description:
Is this pointer Pointer Locked?
Only a mouse pointer can be locked and it only becomes locked when requested via
the browsers Pointer Lock API.
You can request this by calling the this.input.mouse.requestPointerLock() method from
a pointerdown or pointerup event handler.
Source: src/input/Pointer.js#L448
Since: 3.19.0
manager ​
manager: Phaser.Input.InputManager ​
Description:
A reference to the Input Manager.
Source: src/input/Pointer.js#L44
Since: 3.0.0
motionFactor ​
motionFactor: number ​
Description:
The factor applied to the motion smoothing each frame.
This value is passed to the Smooth Step Interpolation that is used to calculate the velocity,
angle and distance of the Pointer. It's applied every frame, until the midPoint reaches the current
position of the Pointer. 0.2 provides a good average but can be increased if you need a
quicker update and are working in a high performance environment. Never set this value to
zero.
Source: src/input/Pointer.js#L245
Since: 3.16.0
movementX ​
movementX: number ​
Description:
If the mouse is locked, the horizontal relative movement of the Pointer in pixels since last frame.
Source: src/input/Pointer.js#L399
Since: 3.0.0
movementY ​
movementY: number ​
Description:
If the mouse is locked, the vertical relative movement of the Pointer in pixels since last frame.
Source: src/input/Pointer.js#L409
Since: 3.0.0
moveTime ​
moveTime: number ​
Description:
Time when this Pointer was most recently moved (regardless of the state of its buttons, if any)
Source: src/input/Pointer.js#L287
Since: 3.0.0
pointerId ​
pointerId: number ​
Description:
The pointerId property of the Pointer as set by the DOM event when this Pointer is started.
The browser can and will recycle this value.
Source: src/input/Pointer.js#L428
Since: 3.10.0
position ​
position: Phaser.Math.Vector2 ​
Description:
The position of the Pointer in screen space.
Source: src/input/Pointer.js#L143
Since: 3.0.0
prevPosition ​
prevPosition: Phaser.Math.Vector2 ​
Description:
The previous position of the Pointer in screen space.
The old x and y values are stored in here during the InputManager.transformPointer call.
Use the properties velocity , angle and distance to create your own gesture recognition.
Source: src/input/Pointer.js#L153
Since: 3.11.0
primaryDown ​
primaryDown: boolean ​
Description:
Is the primary button down? (usually button 0, the left mouse button)
Source: src/input/Pointer.js#L357
Since: 3.0.0
smoothFactor ​
smoothFactor: number ​
Description:
The smoothing factor to apply to the Pointer position.
Due to their nature, pointer positions are inherently noisy. While this is fine for lots of games, if you need cleaner positions
then you can set this value to apply an automatic smoothing to the positions as they are recorded.
The default value of zero means 'no smoothing'.
Set to a small value, such as 0.2, to apply an average level of smoothing between positions. You can do this by changing this
value directly, or by setting the input.smoothFactor property in the Game Config.
Positions are only smoothed when the pointer moves. If the primary button on this Pointer enters an Up or Down state, then the position
is always precise, and not smoothed.
Source: src/input/Pointer.js#L225
Since: 3.16.0
time ​
time: number ​
Description:
Time when this Pointer was most recently updated by a DOM Event.
This comes directly from the event.timeStamp property.
If no event has yet taken place, it will return zero.
Source: src/input/Pointer.js#L1304
Since: 3.16.0
upElement ​
upElement: any ​
Description:
The DOM element the Pointer was released on, taken from the DOM event.
In a default set-up this will be the Canvas that Phaser is rendering to, or the Window element.
Source: src/input/Pointer.js#L83
Since: 3.16.0
upTime ​
upTime: number ​
Description:
The Event timestamp when the final button, or Touch input, was released. Used for dragging objects.
Source: src/input/Pointer.js#L347
Since: 3.0.0
upX ​
upX: number ​
Description:
X coordinate of the Pointer when Button 1 (left button), or Touch, was released, used for dragging objects.
Source: src/input/Pointer.js#L327
Since: 3.0.0
upY ​
upY: number ​
Description:
Y coordinate of the Pointer when Button 1 (left button), or Touch, was released, used for dragging objects.
Source: src/input/Pointer.js#L337
Since: 3.0.0
velocity ​
velocity: Phaser.Math.Vector2 ​
Description:
The current velocity of the Pointer, based on its current and previous positions.
This value is smoothed out each frame, according to the motionFactor property.
This property is updated whenever the Pointer moves, regardless of any button states. In other words,
it changes based on movement alone - a button doesn't have to be pressed first.
Source: src/input/Pointer.js#L177
Since: 3.16.0
wasCanceled ​
wasCanceled: boolean ​
Description:
Did this Pointer get canceled by a touchcancel event?
Note: "canceled" is the American-English spelling of "cancelled". Please don't submit PRs correcting it!
Source: src/input/Pointer.js#L387
Since: 3.15.0
wasTouch ​
wasTouch: boolean ​
Description:
Did the previous input event come from a Touch input (true) or Mouse? (false)
Source: src/input/Pointer.js#L377
Since: 3.0.0
worldX ​
worldX: number ​
Description:
The x position of this Pointer, translated into the coordinate space of the most recent Camera it interacted with.
If you wish to use this value outside of an input event handler then you should update it first by calling
the Pointer.updateWorldPoint method.
Source: src/input/Pointer.js#L261
Since: 3.10.0
worldY ​
worldY: number ​
Description:
The y position of this Pointer, translated into the coordinate space of the most recent Camera it interacted with.
If you wish to use this value outside of an input event handler then you should update it first by calling
the Pointer.updateWorldPoint method.
Source: src/input/Pointer.js#L274
Since: 3.10.0
x ​
x: number ​
Description:
The x position of this Pointer.
The value is in screen space.
See worldX to get a camera converted position.
Source: src/input/Pointer.js#L1258
Since: 3.0.0
y ​
y: number ​
Description:
The y position of this Pointer.
The value is in screen space.
See worldY to get a camera converted position.
Source: src/input/Pointer.js#L1281
Since: 3.0.0
Public Methods ​
backButtonDown ​
<instance> backButtonDown() ​
Description:
Checks to see if the back button is being held down on this Pointer.
Returns: boolean - true if the back button is being held down.
Source: src/input/Pointer.js#L930
Since: 3.0.0
backButtonReleased ​
<instance> backButtonReleased() ​
Description:
Checks to see if the release of the back button was the most recent activity on this Pointer.
Returns: boolean - true if the release of the back button was the most recent activity on this Pointer.
Source: src/input/Pointer.js#L995
Since: 3.18.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Pointer instance and resets its external references.
Source: src/input/Pointer.js#L1245
Since: 3.0.0
forwardButtonDown ​
<instance> forwardButtonDown() ​
Description:
Checks to see if the forward button is being held down on this Pointer.
Returns: boolean - true if the forward button is being held down.
Source: src/input/Pointer.js#L943
Since: 3.0.0
forwardButtonReleased ​
<instance> forwardButtonReleased() ​
Description:
Checks to see if the release of the forward button was the most recent activity on this Pointer.
Returns: boolean - true if the release of the forward button was the most recent activity on this Pointer.
Source: src/input/Pointer.js#L1008
Since: 3.18.0
getAngle ​
<instance> getAngle() ​
Description:
If the Pointer has a button pressed down at the time this method is called, it will return the
angle between the Pointer's downX and downY values and the current position.
If no button is held down, it will return the last recorded angle, based on where
the Pointer was when the button was released.
The angle is based on the old position facing to the current position.
If you wish to get the current angle, based on the velocity of the Pointer, then
see the Pointer.angle property.
Returns: number - The angle between the Pointer's coordinates in radians.
Source: src/input/Pointer.js#L1120
Since: 3.16.0
getDistance ​
<instance> getDistance() ​
Description:
If the Pointer has a button pressed down at the time this method is called, it will return the
distance between the Pointer's downX and downY values and the current position.
If no button is held down, it will return the last recorded distance, based on where
the Pointer was when the button was released.
If you wish to get the distance being travelled currently, based on the velocity of the Pointer,
then see the Pointer.distance property.
Returns: number - The distance the Pointer moved.
Source: src/input/Pointer.js#L1021
Since: 3.13.0
getDistanceX ​
<instance> getDistanceX() ​
Description:
If the Pointer has a button pressed down at the time this method is called, it will return the
horizontal distance between the Pointer's downX and downY values and the current position.
If no button is held down, it will return the last recorded horizontal distance, based on where
the Pointer was when the button was released.
Returns: number - The horizontal distance the Pointer moved.
Source: src/input/Pointer.js#L1048
Since: 3.16.0
getDistanceY ​
<instance> getDistanceY() ​
Description:
If the Pointer has a button pressed down at the time this method is called, it will return the
vertical distance between the Pointer's downX and downY values and the current position.
If no button is held down, it will return the last recorded vertical distance, based on where
the Pointer was when the button was released.
Returns: number - The vertical distance the Pointer moved.
Source: src/input/Pointer.js#L1072
Since: 3.16.0
getDuration ​
<instance> getDuration() ​
Description:
If the Pointer has a button pressed down at the time this method is called, it will return the
duration since the button was pressed down.
If no button is held down, it will return the last recorded duration, based on the time
the last button on the Pointer was released.
Returns: number - The duration the Pointer was held down for in milliseconds.
Source: src/input/Pointer.js#L1096
Since: 3.16.0
getInterpolatedPosition ​
<instance> getInterpolatedPosition([steps], [out]) ​
Description:
Takes the previous and current Pointer positions and then generates an array of interpolated values between
the two. The array will be populated up to the size of the steps argument.
var points = pointer . getInterpolatedPosition ( 4 ) ;
// points[0] = { x: 0, y: 0 }
// points[1] = { x: 2, y: 1 }
// points[2] = { x: 3, y: 2 }
// points[3] = { x: 6, y: 3 }
Use this if you need to get smoothed values between the previous and current pointer positions. DOM pointer
events can often fire faster than the main browser loop, and this will help you avoid janky movement
especially if you have an object following a Pointer.
Note that if you provide an output array it will only be populated up to the number of steps provided.
It will not clear any previous data that may have existed beyond the range of the steps count.
Internally it uses the Smooth Step interpolation calculation.
Parameters:
name type optional default description
steps number Yes 10 The number of interpolation steps to use.
out array Yes An array to store the results in. If not provided a new one will be created.
Returns: array - An array of interpolated values.
Source: src/input/Pointer.js#L1149
Since: 3.11.0
leftButtonDown ​
<instance> leftButtonDown() ​
Description:
Checks to see if the left button is being held down on this Pointer.
Returns: boolean - true if the left button is being held down.
Source: src/input/Pointer.js#L891
Since: 3.0.0
leftButtonReleased ​
<instance> leftButtonReleased() ​
Description:
Checks to see if the release of the left button was the most recent activity on this Pointer.
Returns: boolean - true if the release of the left button was the most recent activity on this Pointer.
Source: src/input/Pointer.js#L956
Since: 3.18.0
middleButtonDown ​
<instance> middleButtonDown() ​
Description:
Checks to see if the middle button is being held down on this Pointer.
Returns: boolean - true if the middle button is being held down.
Source: src/input/Pointer.js#L917
Since: 3.0.0
middleButtonReleased ​
<instance> middleButtonReleased() ​
Description:
Checks to see if the release of the middle button was the most recent activity on this Pointer.
Returns: boolean - true if the release of the middle button was the most recent activity on this Pointer.
Source: src/input/Pointer.js#L982
Since: 3.18.0
noButtonDown ​
<instance> noButtonDown() ​
Description:
Checks to see if any buttons are being held down on this Pointer.
Returns: boolean - true if no buttons are being held down.
Source: src/input/Pointer.js#L878
Since: 3.0.0
positionToCamera ​
<instance> positionToCamera(camera, [output]) ​
Description:
Takes a Camera and returns a Vector2 containing the translated position of this Pointer
within that Camera. This can be used to convert this Pointers position into camera space.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The Camera to use for the translation.
output Phaser.Math.Vector2 | object Yes A Vector2-like object in which to store the translated position.
Returns: Phaser.Math.Vector2 , object - A Vector2 containing the translated coordinates of this Pointer, based on the given camera.
Source: src/input/Pointer.js#L521
Since: 3.0.0
reset ​
<instance> reset() ​
Description:
Fully reset this Pointer back to its unitialized state.
Source: src/input/Pointer.js#L1200
Since: 3.60.0
rightButtonDown ​
<instance> rightButtonDown() ​
Description:
Checks to see if the right button is being held down on this Pointer.
Returns: boolean - true if the right button is being held down.
Source: src/input/Pointer.js#L904
Since: 3.0.0
rightButtonReleased ​
<instance> rightButtonReleased() ​
Description:
Checks to see if the release of the right button was the most recent activity on this Pointer.
Returns: boolean - true if the release of the right button was the most recent activity on this Pointer.
Source: src/input/Pointer.js#L969
Since: 3.18.0
updateWorldPoint ​
<instance> updateWorldPoint(camera) ​
Description:
Takes a Camera and updates this Pointer's worldX and worldY values so they are
the result of a translation through the given Camera.
Note that the values will be automatically replaced the moment the Pointer is
updated by an input event, such as a mouse move, so should be used immediately.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The Camera which is being tested against.
Returns: Phaser.Input.Pointer - This Pointer object.
Source: src/input/Pointer.js#L496
Since: 3.19.0
Previous
MouseManager
Next
TouchManager
Public Members
active
angle
button
buttons
camera
deltaX
deltaY
deltaZ
distance
downElement
downTime
downX
downY
event
id
identifier
isDown
locked
manager
motionFactor
movementX
movementY
moveTime
pointerId
position
prevPosition
primaryDown
smoothFactor
time
upElement
upTime
upX
upY
velocity
wasCanceled
wasTouch
worldX
worldY
x
y
Public Methods
backButtonDown
backButtonReleased
destroy
forwardButtonDown
forwardButtonReleased
getAngle
getDistance
getDistanceX
getDistanceY
getDuration
getInterpolatedPosition
leftButtonDown
leftButtonReleased
middleButtonDown
middleButtonReleased
noButtonDown
positionToCamera
reset
rightButtonDown
rightButtonReleased
updateWorldPoint
