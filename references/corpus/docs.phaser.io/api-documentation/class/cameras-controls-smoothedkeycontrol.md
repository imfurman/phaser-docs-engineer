# SmoothedKeyControl | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/cameras-controls-smoothedkeycontrol

Phaser API Documentation
Class
SmoothedKeyControl
Version: Phaser v3.90.0
On this page
SmoothedKeyControl
A Smoothed Key Camera Control.
This allows you to control the movement and zoom of a camera using the defined keys.
Unlike the Fixed Camera Control you can also provide physics values for acceleration, drag and maxSpeed for smoothing effects.
var controlConfig = {
camera : this . cameras . main ,
left : cursors . left ,
right : cursors . right ,
up : cursors . up ,
down : cursors . down ,
zoomIn : this . input . keyboard . addKey ( Phaser . Input . Keyboard . KeyCodes . Q ) ,
zoomOut : this . input . keyboard . addKey ( Phaser . Input . Keyboard . KeyCodes . E ) ,
zoomSpeed : 0.02 ,
acceleration : 0.06 ,
drag : 0.0005 ,
maxSpeed : 1.0
} ;
You must call the update method of this controller every frame.
Constructor
new SmoothedKeyControl(config)
Parameters
name type optional description
config Phaser.Types.Cameras.Controls.SmoothedKeyControlConfig No The Smoothed Key Control configuration object.
Scope : static
Source: src/cameras/controls/SmoothedKeyControl.js#L10
Since: 3.0.0
Public Members ​
accelX ​
accelX: number ​
Description:
The horizontal acceleration the camera will move.
Source: src/cameras/controls/SmoothedKeyControl.js#L148
Since: 3.0.0
accelY ​
accelY: number ​
Description:
The vertical acceleration the camera will move.
Source: src/cameras/controls/SmoothedKeyControl.js#L158
Since: 3.0.0
active ​
active: boolean ​
Description:
A flag controlling if the Controls will update the Camera or not.
Source: src/cameras/controls/SmoothedKeyControl.js#L280
Since: 3.0.0
camera ​
camera: Phaser.Cameras.Scene2D.Camera ​
Description:
The Camera that this Control will update.
Source: src/cameras/controls/SmoothedKeyControl.js#L48
Since: 3.0.0
down ​
down: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera down.
Source: src/cameras/controls/SmoothedKeyControl.js#L88
Since: 3.0.0
dragX ​
dragX: number ​
Description:
The horizontal drag applied to the camera when it is moving.
Source: src/cameras/controls/SmoothedKeyControl.js#L181
Since: 3.0.0
dragY ​
dragY: number ​
Description:
The vertical drag applied to the camera when it is moving.
Source: src/cameras/controls/SmoothedKeyControl.js#L191
Since: 3.0.0
left ​
left: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera left.
Source: src/cameras/controls/SmoothedKeyControl.js#L58
Since: 3.0.0
maxSpeedX ​
maxSpeedX: number ​
Description:
The maximum horizontal speed the camera will move.
Source: src/cameras/controls/SmoothedKeyControl.js#L214
Since: 3.0.0
maxSpeedY ​
maxSpeedY: number ​
Description:
The maximum vertical speed the camera will move.
Source: src/cameras/controls/SmoothedKeyControl.js#L224
Since: 3.0.0
maxZoom ​
maxZoom: number ​
Description:
The largest zoom value the camera will reach when zoomed in.
Source: src/cameras/controls/SmoothedKeyControl.js#L138
Since: 3.53.0
minZoom ​
minZoom: number ​
Description:
The smallest zoom value the camera will reach when zoomed out.
Source: src/cameras/controls/SmoothedKeyControl.js#L128
Since: 3.53.0
right ​
right: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera right.
Source: src/cameras/controls/SmoothedKeyControl.js#L68
Since: 3.0.0
up ​
up: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera up.
Source: src/cameras/controls/SmoothedKeyControl.js#L78
Since: 3.0.0
zoomIn ​
zoomIn: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will zoom the Camera in.
Source: src/cameras/controls/SmoothedKeyControl.js#L98
Since: 3.0.0
zoomOut ​
zoomOut: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will zoom the Camera out.
Source: src/cameras/controls/SmoothedKeyControl.js#L108
Since: 3.0.0
zoomSpeed ​
zoomSpeed: number ​
Description:
The speed at which the camera will zoom if the zoomIn or zoomOut keys are pressed.
Source: src/cameras/controls/SmoothedKeyControl.js#L118
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Key Control.
Source: src/cameras/controls/SmoothedKeyControl.js#L480
Since: 3.0.0
setCamera ​
<instance> setCamera(camera) ​
Description:
Binds this Key Control to a camera.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The camera to bind this Key Control to.
Returns: Phaser.Cameras.Controls.SmoothedKeyControl - This Key Control instance.
Source: src/cameras/controls/SmoothedKeyControl.js#L320
Since: 3.0.0
start ​
<instance> start() ​
Description:
Starts the Key Control running, providing it has been linked to a camera.
Returns: Phaser.Cameras.Controls.SmoothedKeyControl - This Key Control instance.
Source: src/cameras/controls/SmoothedKeyControl.js#L290
Since: 3.0.0
stop ​
<instance> stop() ​
Description:
Stops this Key Control from running. Call start to start it again.
Returns: Phaser.Cameras.Controls.SmoothedKeyControl - This Key Control instance.
Source: src/cameras/controls/SmoothedKeyControl.js#L305
Since: 3.0.0
update ​
<instance> update(delta) ​
Description:
Applies the results of pressing the control keys to the Camera.
You must call this every step, it is not called automatically.
Parameters:
name type optional description
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/cameras/controls/SmoothedKeyControl.js#L337
Since: 3.0.0
Previous
FixedKeyControl
Next
BaseCamera
Public Members
accelX
accelY
active
camera
down
dragX
dragY
left
maxSpeedX
maxSpeedY
maxZoom
minZoom
right
up
zoomIn
zoomOut
zoomSpeed
Public Methods
destroy
setCamera
start
stop
update
