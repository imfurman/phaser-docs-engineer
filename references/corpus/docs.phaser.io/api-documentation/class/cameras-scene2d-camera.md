# Camera | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/cameras-scene2d-camera

Phaser API Documentation
Class
Camera
Version: Phaser v3.90.0
On this page
Camera
A Camera.
The Camera is the way in which all games are rendered in Phaser. They provide a view into your game world,
and can be positioned, rotated, zoomed and scrolled accordingly.
A Camera consists of two elements: The viewport and the scroll values.
The viewport is the physical position and size of the Camera within your game. Cameras, by default, are
created the same size as your game, but their position and size can be set to anything. This means if you
wanted to create a camera that was 320x200 in size, positioned in the bottom-right corner of your game,
you'd adjust the viewport to do that (using methods like setViewport and setSize ).
If you wish to change where the Camera is looking in your game, then you scroll it. You can do this
via the properties scrollX and scrollY or the method setScroll . Scrolling has no impact on the
viewport, and changing the viewport has no impact on the scrolling.
By default a Camera will render all Game Objects it can see. You can change this using the ignore method,
allowing you to filter Game Objects out on a per-Camera basis.
A Camera also has built-in special effects including Fade, Flash and Camera Shake.
Constructor
new Camera(x, y, width, height)
Parameters
name type optional description
x number No The x position of the Camera, relative to the top-left of the game canvas.
y number No The y position of the Camera, relative to the top-left of the game canvas.
width number No The width of the Camera, in pixels.
height number No The height of the Camera, in pixels.
Scope : static
Extends
Phaser.Cameras.Scene2D.BaseCamera
Phaser.GameObjects.Components.PostPipeline
Source: src/cameras/2d/Camera.js#L18
Since: 3.0.0
Inherited Members ​
From Phaser.Cameras.Scene2D.BaseCamera :
alpha
backgroundColor
cameraManager
centerX
centerY
dirty
disableCull
displayHeight
displayWidth
height
id
isSceneCamera
mask
midPoint
name
originX
originY
renderList
renderRoundPixels
roundPixels
scaleManager
scene
sceneManager
scrollX
scrollY
transparent
useBounds
visible
width
worldView
x
y
zoom
zoomX
zoomY
From Phaser.GameObjects.Components.Alpha :
alphaBottomLeft
alphaBottomRight
alphaTopLeft
alphaTopRight
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
Public Members ​
deadzone ​
deadzone: Phaser.Geom.Rectangle ​
Description:
The Camera dead zone.
The deadzone is only used when the camera is following a target.
It defines a rectangular region within which if the target is present, the camera will not scroll.
If the target moves outside of this area, the camera will begin scrolling in order to follow it.
The lerp values that you can set for a follower target also apply when using a deadzone.
You can directly set this property to be an instance of a Rectangle. Or, you can use the
setDeadzone method for a chainable approach.
The rectangle you provide can have its dimensions adjusted dynamically, however, please
note that its position is updated every frame, as it is constantly re-centered on the cameras mid point.
Calling setDeadzone with no arguments will reset an active deadzone, as will setting this property
to null .
Source: src/cameras/2d/Camera.js#L169
Since: 3.11.0
fadeEffect ​
fadeEffect: Phaser.Cameras.Scene2D.Effects.Fade ​
Description:
The Camera Fade effect handler.
To fade this camera see the Camera.fade methods.
Source: src/cameras/2d/Camera.js#L80
Since: 3.5.0
flashEffect ​
flashEffect: Phaser.Cameras.Scene2D.Effects.Flash ​
Description:
The Camera Flash effect handler.
To flash this camera see the Camera.flash method.
Source: src/cameras/2d/Camera.js#L90
Since: 3.5.0
followOffset ​
followOffset: Phaser.Math.Vector2 ​
Description:
The values stored in this property are subtracted from the Camera targets position, allowing you to
offset the camera from the actual target x/y coordinates by this amount.
Can also be set via setFollowOffset or as part of the startFollow call.
Source: src/cameras/2d/Camera.js#L158
Since: 3.9.0
inputEnabled ​
inputEnabled: boolean ​
Description:
Does this Camera allow the Game Objects it renders to receive input events?
Source: src/cameras/2d/Camera.js#L70
Since: 3.0.0
lerp ​
lerp: Phaser.Math.Vector2 ​
Description:
The linear interpolation value to use when following a target.
Can also be set via setLerp or as part of the startFollow call.
The default values of 1 means the camera will instantly snap to the target coordinates.
A lower value, such as 0.1 means the camera will more slowly track the target, giving
a smooth transition. You can set the horizontal and vertical values independently, and also
adjust this value in real-time during your game.
Be sure to keep the value between 0 and 1. A value of zero will disable tracking on that axis.
Source: src/cameras/2d/Camera.js#L140
Since: 3.9.0
panEffect ​
panEffect: Phaser.Cameras.Scene2D.Effects.Pan ​
Description:
The Camera Pan effect handler.
To pan this camera see the Camera.pan method.
Source: src/cameras/2d/Camera.js#L110
Since: 3.11.0
rotateToEffect ​
rotateToEffect: Phaser.Cameras.Scene2D.Effects.RotateTo ​
Description:
The Camera Rotate To effect handler.
To rotate this camera see the Camera.rotateTo method.
Source: src/cameras/2d/Camera.js#L120
Since: 3.23.0
shakeEffect ​
shakeEffect: Phaser.Cameras.Scene2D.Effects.Shake ​
Description:
The Camera Shake effect handler.
To shake this camera see the Camera.shake method.
Source: src/cameras/2d/Camera.js#L100
Since: 3.5.0
zoomEffect ​
zoomEffect: Phaser.Cameras.Scene2D.Effects.Zoom ​
Description:
The Camera Zoom effect handler.
To zoom this camera see the Camera.zoom method.
Source: src/cameras/2d/Camera.js#L130
Since: 3.11.0
Inherited Methods ​
From Phaser.Cameras.Scene2D.BaseCamera :
addToRenderList
centerOn
centerOnX
centerOnY
centerToBounds
centerToSize
clampX
clampY
clearMask
cull
getBounds
getScroll
getWorldPoint
ignore
removeBounds
setAlpha
setAngle
setBackgroundColor
setBounds
setIsSceneCamera
setMask
setName
setOrigin
setPosition
setRotation
setRoundPixels
setScene
setScroll
setSize
setViewport
setVisible
setZoom
toJSON
From Phaser.Events.EventEmitter :
addListener
emit
eventNames
listenerCount
listeners
off
on
once
removeAllListeners
removeListener
shutdown
From Phaser.GameObjects.Components.Alpha :
clearAlpha
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Camera instance. You rarely need to call this directly.
Called by the Camera Manager. If you wish to destroy a Camera please use CameraManager.remove as
cameras are stored in a pool, ready for recycling later, and calling this directly will prevent that.
Overrides: Phaser.Cameras.Scene2D.BaseCamera#destroy
Fires: Phaser.Cameras.Scene2D.Events#event:DESTROY
Source: src/cameras/2d/Camera.js#L779
Since: 3.0.0
fade ​
<instance> fade([duration], [red], [green], [blue], [force], [callback], [context]) ​
Description:
Fades the Camera from transparent to the given color over the duration specified.
Parameters:
name type optional default description
duration number Yes 1000 The duration of the effect in milliseconds.
red number Yes 0 The amount to fade the red channel towards. A value between 0 and 255.
green number Yes 0 The amount to fade the green channel towards. A value between 0 and 255.
blue number Yes 0 The amount to fade the blue channel towards. A value between 0 and 255.
force boolean Yes false Force the effect to start immediately, even if already running.
callback function Yes This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:FADE_OUT_START , Phaser.Cameras.Scene2D.Events#event:FADE_OUT_COMPLETE
Source: src/cameras/2d/Camera.js#L339
Since: 3.0.0
fadeFrom ​
<instance> fadeFrom([duration], [red], [green], [blue], [force], [callback], [context]) ​
Description:
Fades the Camera from the given color to transparent over the duration specified.
Parameters:
name type optional default description
duration number Yes 1000 The duration of the effect in milliseconds.
red number Yes 0 The amount to fade the red channel towards. A value between 0 and 255.
green number Yes 0 The amount to fade the green channel towards. A value between 0 and 255.
blue number Yes 0 The amount to fade the blue channel towards. A value between 0 and 255.
force boolean Yes false Force the effect to start immediately, even if already running.
callback function Yes This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:FADE_IN_START , Phaser.Cameras.Scene2D.Events#event:FADE_IN_COMPLETE
Source: src/cameras/2d/Camera.js#L315
Since: 3.5.0
fadeIn ​
<instance> fadeIn([duration], [red], [green], [blue], [callback], [context]) ​
Description:
Fades the Camera in from the given color over the duration specified.
Parameters:
name type optional default description
duration number Yes 1000 The duration of the effect in milliseconds.
red number Yes 0 The amount to fade the red channel towards. A value between 0 and 255.
green number Yes 0 The amount to fade the green channel towards. A value between 0 and 255.
blue number Yes 0 The amount to fade the blue channel towards. A value between 0 and 255.
callback function Yes This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:FADE_IN_START , Phaser.Cameras.Scene2D.Events#event:FADE_IN_COMPLETE
Source: src/cameras/2d/Camera.js#L268
Since: 3.3.0
fadeOut ​
<instance> fadeOut([duration], [red], [green], [blue], [callback], [context]) ​
Description:
Fades the Camera out to the given color over the duration specified.
This is an alias for Camera.fade that forces the fade to start, regardless of existing fades.
Parameters:
name type optional default description
duration number Yes 1000 The duration of the effect in milliseconds.
red number Yes 0 The amount to fade the red channel towards. A value between 0 and 255.
green number Yes 0 The amount to fade the green channel towards. A value between 0 and 255.
blue number Yes 0 The amount to fade the blue channel towards. A value between 0 and 255.
callback function Yes This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:FADE_OUT_START , Phaser.Cameras.Scene2D.Events#event:FADE_OUT_COMPLETE
Source: src/cameras/2d/Camera.js#L291
Since: 3.3.0
flash ​
<instance> flash([duration], [red], [green], [blue], [force], [callback], [context]) ​
Description:
Flashes the Camera by setting it to the given color immediately and then fading it away again quickly over the duration specified.
Parameters:
name type optional default description
duration number Yes 250 The duration of the effect in milliseconds.
red number Yes 255 The amount to fade the red channel towards. A value between 0 and 255.
green number Yes 255 The amount to fade the green channel towards. A value between 0 and 255.
blue number Yes 255 The amount to fade the blue channel towards. A value between 0 and 255.
force boolean Yes false Force the effect to start immediately, even if already running.
callback function Yes This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:FLASH_START , Phaser.Cameras.Scene2D.Events#event:FLASH_COMPLETE
Source: src/cameras/2d/Camera.js#L363
Since: 3.0.0
pan ​
<instance> pan(x, y, [duration], [ease], [force], [callback], [context]) ​
Description:
This effect will scroll the Camera so that the center of its viewport finishes at the given destination,
over the duration and with the ease specified.
Parameters:
name type optional default description
x number No The destination x coordinate to scroll the center of the Camera viewport to.
y number No The destination y coordinate to scroll the center of the Camera viewport to.
duration number Yes 1000 The duration of the effect in milliseconds.
ease string | function Yes "'Linear'" The ease to use for the pan. Can be any of the Phaser Easing constants or a custom function.
force boolean Yes false Force the pan effect to start immediately, even if already running.
callback Phaser.Types.Cameras.Scene2D.CameraPanCallback Yes This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera scroll x coordinate and the current camera scroll y coordinate.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:PAN_START , Phaser.Cameras.Scene2D.Events#event:PAN_COMPLETE
Source: src/cameras/2d/Camera.js#L409
Since: 3.11.0
preRender ​
<instance> preRender() ​
Description:
Updates camera matrix. Also resets any active effects on this Camera (such as shake, flash and fade) and quickly clears them all.
Source: src/cameras/2d/Camera.js#L483
Since: 3.0.0
resetFX ​
<instance> resetFX() ​
Description:
Resets any active FX, such as a fade, flash or shake. Useful to call after a fade in order to
remove the fade.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Source: src/cameras/2d/Camera.js#L736
Since: 3.0.0
rotateTo ​
<instance> rotateTo(radians, [shortestPath], [duration], [ease], [force], [callback], [context]) ​
Description:
This effect will rotate the Camera so that the viewport finishes at the given angle in radians,
over the duration and with the ease specified.
Parameters:
name type optional default description
radians number No The destination angle in radians to rotate the Camera viewport to. If the angle is positive then the rotation is clockwise else anticlockwise
shortestPath boolean Yes false If shortest path is set to true the camera will rotate in the quickest direction clockwise or anti-clockwise.
duration number Yes 1000 The duration of the effect in milliseconds.
ease string | function Yes "'Linear'" The ease to use for the rotation. Can be any of the Phaser Easing constants or a custom function.
force boolean Yes false Force the rotation effect to start immediately, even if already running.
callback CameraRotateCallback Yes This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera rotation angle in radians.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Source: src/cameras/2d/Camera.js#L435
Since: 3.23.0
setDeadzone ​
<instance> setDeadzone([width], [height]) ​
Description:
Sets the Camera dead zone.
The deadzone is only used when the camera is following a target.
It defines a rectangular region within which if the target is present, the camera will not scroll.
If the target moves outside of this area, the camera will begin scrolling in order to follow it.
The deadzone rectangle is re-positioned every frame so that it is centered on the mid-point
of the camera. This allows you to use the object for additional game related checks, such as
testing if an object is within it or not via a Rectangle.contains call.
The lerp values that you can set for a follower target also apply when using a deadzone.
Calling this method with no arguments will reset an active deadzone.
Parameters:
name type optional description
width number Yes The width of the deadzone rectangle in pixels. If not specified the deadzone is removed.
height number Yes The height of the deadzone rectangle in pixels.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Source: src/cameras/2d/Camera.js#L206
Since: 3.11.0
setFollowOffset ​
<instance> setFollowOffset([x], [y]) ​
Description:
Sets the horizontal and vertical offset of the camera from its follow target.
The values are subtracted from the targets position during the Cameras update step.
Parameters:
name type optional default description
x number Yes 0 The horizontal offset from the camera follow target.x position.
y number Yes 0 The vertical offset from the camera follow target.y position.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Source: src/cameras/2d/Camera.js#L634
Since: 3.9.0
setLerp ​
<instance> setLerp([x], [y]) ​
Description:
Sets the linear interpolation value to use when following a target.
The default values of 1 means the camera will instantly snap to the target coordinates.
A lower value, such as 0.1 means the camera will more slowly track the target, giving
a smooth transition. You can set the horizontal and vertical values independently, and also
adjust this value in real-time during your game.
Be sure to keep the value between 0 and 1. A value of zero will disable tracking on that axis.
Parameters:
name type optional default description
x number Yes 1 The amount added to the horizontal linear interpolation of the follow target.
y number Yes 1 The amount added to the vertical linear interpolation of the follow target.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Source: src/cameras/2d/Camera.js#L606
Since: 3.9.0
shake ​
<instance> shake([duration], [intensity], [force], [callback], [context]) ​
Description:
Shakes the Camera by the given intensity over the duration specified.
Parameters:
name type optional default description
duration number Yes 100 The duration of the effect in milliseconds.
intensity number | Phaser.Math.Vector2 Yes 0.05 The intensity of the shake.
force boolean Yes false Force the shake effect to start immediately, even if already running.
callback function Yes This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:SHAKE_START , Phaser.Cameras.Scene2D.Events#event:SHAKE_COMPLETE
Source: src/cameras/2d/Camera.js#L387
Since: 3.0.0
startFollow ​
<instance> startFollow(target, [roundPixels], [lerpX], [lerpY], [offsetX], [offsetY]) ​
Description:
Sets the Camera to follow a Game Object.
When enabled the Camera will automatically adjust its scroll position to keep the target Game Object
in its center.
You can set the linear interpolation value used in the follow code.
Use low lerp values (such as 0.1) to automatically smooth the camera motion.
If you find you're getting a slight "jitter" effect when following an object it's probably to do with sub-pixel
rendering of the targets position. This can be rounded by setting the roundPixels argument to true to
force full pixel rounding rendering. Note that this can still be broken if you have specified a non-integer zoom
value on the camera. So be sure to keep the camera zoom to integers.
Parameters:
name type optional default description
target Phaser.GameObjects.GameObject | object No The target for the Camera to follow.
roundPixels boolean Yes false Round the camera position to whole integers to avoid sub-pixel rendering?
lerpX number Yes 1 A value between 0 and 1. This value specifies the amount of linear interpolation to use when horizontally tracking the target. The closer the value to 1, the faster the camera will track.
lerpY number Yes 1 A value between 0 and 1. This value specifies the amount of linear interpolation to use when vertically tracking the target. The closer the value to 1, the faster the camera will track.
offsetX number Yes 0 The horizontal offset from the camera follow target.x position.
offsetY number Yes 0 The vertical offset from the camera follow target.y position.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Source: src/cameras/2d/Camera.js#L656
Since: 3.0.0
stopFollow ​
<instance> stopFollow() ​
Description:
Stops a Camera from following a Game Object, if previously set via Camera.startFollow .
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Source: src/cameras/2d/Camera.js#L721
Since: 3.0.0
update ​
<instance> update(time, delta) ​
Description:
Internal method called automatically by the Camera Manager.
Access: protected
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time, in ms, elapsed since the last frame.
Overrides: Phaser.Cameras.Scene2D.BaseCamera#update
Source: src/cameras/2d/Camera.js#L756
Since: 3.0.0
zoomTo ​
<instance> zoomTo(zoom, [duration], [ease], [force], [callback], [context]) ​
Description:
This effect will zoom the Camera to the given scale, over the duration and with the ease specified.
Parameters:
name type optional default description
zoom number No The target Camera zoom value.
duration number Yes 1000 The duration of the effect in milliseconds.
ease string | function Yes "'Linear'" The ease to use for the pan. Can be any of the Phaser Easing constants or a custom function.
force boolean Yes false Force the pan effect to start immediately, even if already running.
callback Phaser.Types.Cameras.Scene2D.CameraPanCallback Yes This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera scroll x coordinate and the current camera scroll y coordinate.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - This Camera instance.
Fires: Phaser.Cameras.Scene2D.Events#event:ZOOM_START , Phaser.Cameras.Scene2D.Events#event:ZOOM_COMPLETE
Source: src/cameras/2d/Camera.js#L459
Since: 3.11.0
Previous
BaseCamera
Next
CameraManager
Inherited Members
Public Members
deadzone
fadeEffect
flashEffect
followOffset
inputEnabled
lerp
panEffect
rotateToEffect
shakeEffect
zoomEffect
Inherited Methods
Public Methods
destroy
fade
fadeFrom
fadeIn
fadeOut
flash
pan
preRender
resetFX
rotateTo
setDeadzone
setFollowOffset
setLerp
shake
startFollow
stopFollow
update
zoomTo
