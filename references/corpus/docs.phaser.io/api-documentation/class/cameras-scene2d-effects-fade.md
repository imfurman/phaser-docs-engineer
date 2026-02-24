# Fade | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/cameras-scene2d-effects-fade

Phaser API Documentation
Class
Fade
Version: Phaser v3.90.0
On this page
Fade
A Camera Fade effect.
This effect will fade the camera viewport to the given color, over the duration specified.
Only the camera viewport is faded. None of the objects it is displaying are impacted, i.e. their colors do
not change.
The effect will dispatch several events on the Camera itself and you can also specify an onUpdate callback,
which is invoked each frame for the duration of the effect, if required.
Constructor
new Fade(camera)
Parameters
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The camera this effect is acting upon.
Scope : static
Source: src/cameras/2d/effects/Fade.js#L11
Since: 3.5.0
Public Members ​
camera ​
camera: Phaser.Cameras.Scene2D.Camera ​
Description:
The Camera this effect belongs to.
Source: src/cameras/2d/effects/Fade.js#L36
Since: 3.5.0
direction ​
direction: boolean ​
Description:
The direction of the fade.
true = fade out (transparent to color), false = fade in (color to transparent)
Source: src/cameras/2d/effects/Fade.js#L71
Since: 3.5.0
duration ​
duration: number ​
Description:
The duration of the effect, in milliseconds.
Source: src/cameras/2d/effects/Fade.js#L82
Since: 3.5.0
isComplete ​
isComplete: boolean ​
Description:
Has this effect finished running?
This is different from isRunning because it remains set to true when the effect is over,
until the effect is either reset or started again.
Source: src/cameras/2d/effects/Fade.js#L57
Since: 3.5.0
isRunning ​
isRunning: boolean ​
Description:
Is this effect actively running?
Source: src/cameras/2d/effects/Fade.js#L46
Since: 3.5.0
progress ​
progress: number ​
Description:
If this effect is running this holds the current percentage of the progress, a value between 0 and 1.
Source: src/cameras/2d/effects/Fade.js#L137
Since: 3.5.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this effect, releasing it from the Camera.
Source: src/cameras/2d/effects/Fade.js#L367
Since: 3.5.0
effectComplete ​
<instance> effectComplete() ​
Description:
Called internally when the effect completes.
Fires: Phaser.Cameras.Scene2D.Events#event:FADE_IN_COMPLETE , Phaser.Cameras.Scene2D.Events#event:FADE_OUT_COMPLETE
Source: src/cameras/2d/effects/Fade.js#L330
Since: 3.5.0
postRenderCanvas ​
<instance> postRenderCanvas(ctx) ​
Description:
Called internally by the Canvas Renderer.
Parameters:
name type optional description
ctx CanvasRenderingContext2D No The Canvas context to render to.
Returns: boolean - true if the effect drew to the renderer, otherwise false .
Source: src/cameras/2d/effects/Fade.js#L273
Since: 3.5.0
postRenderWebGL ​
<instance> postRenderWebGL(pipeline, getTintFunction) ​
Description:
Called internally by the WebGL Renderer.
Parameters:
name type optional description
pipeline Phaser.Renderer.WebGL.Pipelines.MultiPipeline No The WebGL Pipeline to render to. Must provide the drawFillRect method.
getTintFunction function No A function that will return the gl safe tint colors.
Returns: boolean - true if the effect drew to the renderer, otherwise false .
Source: src/cameras/2d/effects/Fade.js#L298
Since: 3.5.0
reset ​
<instance> reset() ​
Description:
Resets this camera effect.
If it was previously running, it stops instantly without calling its onComplete callback or emitting an event.
Source: src/cameras/2d/effects/Fade.js#L351
Since: 3.5.0
start ​
<instance> start([direction], [duration], [red], [green], [blue], [force], [callback], [context]) ​
Description:
Fades the Camera to or from the given color over the duration specified.
Parameters:
name type optional default description
direction boolean Yes true The direction of the fade. true = fade out (transparent to color), false = fade in (color to transparent)
duration number Yes 1000 The duration of the effect in milliseconds.
red number Yes 0 The amount to fade the red channel towards. A value between 0 and 255.
green number Yes 0 The amount to fade the green channel towards. A value between 0 and 255.
blue number Yes 0 The amount to fade the blue channel towards. A value between 0 and 255.
force boolean Yes false Force the effect to start immediately, even if already running.
callback Phaser.Types.Cameras.Scene2D.CameraFadeCallback Yes This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is.
context any Yes The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs.
Returns: Phaser.Cameras.Scene2D.Camera - The Camera on which the effect was started.
Fires: Phaser.Cameras.Scene2D.Events#event:FADE_IN_START , Phaser.Cameras.Scene2D.Events#event:FADE_OUT_START
Source: src/cameras/2d/effects/Fade.js#L178
Since: 3.5.0
update ​
<instance> update(time, delta) ​
Description:
The main update loop for this effect. Called automatically by the Camera.
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time, in ms, elapsed since the last frame.
Source: src/cameras/2d/effects/Fade.js#L237
Since: 3.5.0
Previous
CameraManager
Next
Flash
Public Members
camera
direction
duration
isComplete
isRunning
progress
Public Methods
destroy
effectComplete
postRenderCanvas
postRenderWebGL
reset
start
update
