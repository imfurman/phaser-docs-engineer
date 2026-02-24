# Types.Cameras.Controls | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/types-cameras-controls

Phaser API Documentation
Typedefs
Types.Cameras.Controls
Version: Phaser v3.90.0
On this page
Types.Cameras.Controls
FixedKeyControlConfig ​
<static> FixedKeyControlConfig ​
name type optional default description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera that this Control will update.
left Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera left.
right Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera right.
up Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera up.
down Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera down.
zoomIn Phaser.Input.Keyboard.Key Yes The Key to be pressed that will zoom the Camera in.
zoomOut Phaser.Input.Keyboard.Key Yes The Key to be pressed that will zoom the Camera out.
zoomSpeed number Yes 0.01 The speed at which the camera will zoom if the zoomIn or zoomOut keys are pressed.
speed number | Object Yes 0 The horizontal and vertical speed the camera will move.
minZoom number Yes 0.001 The smallest zoom value the camera will reach when zoomed out.
maxZoom number Yes 1000 The largest zoom value the camera will reach when zoomed in.
Type : object
Member of : Phaser.Types.Cameras.Controls
Source: src/cameras/controls/typedefs/FixedKeyControlConfig.js#L1
Since: 3.0.0
SmoothedKeyControlConfig ​
<static> SmoothedKeyControlConfig ​
name type optional default description
camera Phaser.Cameras.Scene2D.Camera Yes The Camera that this Control will update.
left Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera left.
right Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera right.
up Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera up.
down Phaser.Input.Keyboard.Key Yes The Key to be pressed that will move the Camera down.
zoomIn Phaser.Input.Keyboard.Key Yes The Key to be pressed that will zoom the Camera in.
zoomOut Phaser.Input.Keyboard.Key Yes The Key to be pressed that will zoom the Camera out.
zoomSpeed number Yes 0.01 The speed at which the camera will zoom if the zoomIn or zoomOut keys are pressed.
acceleration number | Object Yes 0 The horizontal and vertical acceleration the camera will move.
drag number | Object Yes 0 The horizontal and vertical drag applied to the camera when it is moving.
maxSpeed number | Object Yes 0 The maximum horizontal and vertical speed the camera will move.
minZoom number Yes 0.001 The smallest zoom value the camera will reach when zoomed out.
maxZoom number Yes 1000 The largest zoom value the camera will reach when zoomed in.
Type : object
Member of : Phaser.Types.Cameras.Controls
Source: src/cameras/controls/typedefs/SmoothedKeyControlConfig.js#L1
Since: 3.0.0
Previous
Types.Animations
Next
Types.Cameras.Scene2D
FixedKeyControlConfig
<static> FixedKeyControlConfig
SmoothedKeyControlConfig
<static> SmoothedKeyControlConfig
