# FixedKeyControl | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/cameras-controls-fixedkeycontrol

Phaser API Documentation
Class
FixedKeyControl
Version: Phaser v3.90.0
On this page
FixedKeyControl
A Fixed Key Camera Control.
This allows you to control the movement and zoom of a camera using the defined keys.
var camControl = new FixedKeyControl ( {
camera : this . cameras . main ,
left : cursors . left ,
right : cursors . right ,
speed : float OR { x : 0 , y : 0 }
} ) ;
Movement is precise and has no 'smoothing' applied to it.
You must call the update method of this controller every frame.
Constructor
new FixedKeyControl(config)
Parameters
name type optional description
config Phaser.Types.Cameras.Controls.FixedKeyControlConfig No The Fixed Key Control configuration object.
Scope : static
Source: src/cameras/controls/FixedKeyControl.js#L10
Since: 3.0.0
Public Members ​
active ​
active: boolean ​
Description:
A flag controlling if the Controls will update the Camera or not.
Source: src/cameras/controls/FixedKeyControl.js#L186
Since: 3.0.0
camera ​
camera: Phaser.Cameras.Scene2D.Camera ​
Description:
The Camera that this Control will update.
Source: src/cameras/controls/FixedKeyControl.js#L42
Since: 3.0.0
down ​
down: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera down.
Source: src/cameras/controls/FixedKeyControl.js#L82
Since: 3.0.0
left ​
left: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera left.
Source: src/cameras/controls/FixedKeyControl.js#L52
Since: 3.0.0
maxZoom ​
maxZoom: number ​
Description:
The largest zoom value the camera will reach when zoomed in.
Source: src/cameras/controls/FixedKeyControl.js#L132
Since: 3.53.0
minZoom ​
minZoom: number ​
Description:
The smallest zoom value the camera will reach when zoomed out.
Source: src/cameras/controls/FixedKeyControl.js#L122
Since: 3.53.0
right ​
right: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera right.
Source: src/cameras/controls/FixedKeyControl.js#L62
Since: 3.0.0
speedX ​
speedX: number ​
Description:
The horizontal speed the camera will move.
Source: src/cameras/controls/FixedKeyControl.js#L142
Since: 3.0.0
speedY ​
speedY: number ​
Description:
The vertical speed the camera will move.
Source: src/cameras/controls/FixedKeyControl.js#L152
Since: 3.0.0
up ​
up: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will move the Camera up.
Source: src/cameras/controls/FixedKeyControl.js#L72
Since: 3.0.0
zoomIn ​
zoomIn: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will zoom the Camera in.
Source: src/cameras/controls/FixedKeyControl.js#L92
Since: 3.0.0
zoomOut ​
zoomOut: Phaser.Input.Keyboard.Key ​
Description:
The Key to be pressed that will zoom the Camera out.
Source: src/cameras/controls/FixedKeyControl.js#L102
Since: 3.0.0
zoomSpeed ​
zoomSpeed: number ​
Description:
The speed at which the camera will zoom if the zoomIn or zoomOut keys are pressed.
Source: src/cameras/controls/FixedKeyControl.js#L112
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Key Control.
Source: src/cameras/controls/FixedKeyControl.js#L304
Since: 3.0.0
setCamera ​
<instance> setCamera(camera) ​
Description:
Binds this Key Control to a camera.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The camera to bind this Key Control to.
Returns: Phaser.Cameras.Controls.FixedKeyControl - This Key Control instance.
Source: src/cameras/controls/FixedKeyControl.js#L226
Since: 3.0.0
start ​
<instance> start() ​
Description:
Starts the Key Control running, providing it has been linked to a camera.
Returns: Phaser.Cameras.Controls.FixedKeyControl - This Key Control instance.
Source: src/cameras/controls/FixedKeyControl.js#L196
Since: 3.0.0
stop ​
<instance> stop() ​
Description:
Stops this Key Control from running. Call start to start it again.
Returns: Phaser.Cameras.Controls.FixedKeyControl - This Key Control instance.
Source: src/cameras/controls/FixedKeyControl.js#L211
Since: 3.0.0
update ​
<instance> update(delta) ​
Description:
Applies the results of pressing the control keys to the Camera.
You must call this every step, it is not called automatically.
Parameters:
name type optional description
delta number No The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate.
Source: src/cameras/controls/FixedKeyControl.js#L243
Since: 3.0.0
Previous
CacheManager
Next
SmoothedKeyControl
Public Members
active
camera
down
left
maxZoom
minZoom
right
speedX
speedY
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
