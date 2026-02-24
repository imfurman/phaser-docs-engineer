# SceneManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/scenes-scenemanager

Phaser API Documentation
Class
SceneManager
Version: Phaser v3.90.0
On this page
SceneManager
The Scene Manager.
The Scene Manager is a Game level system, responsible for creating, processing and updating all of the
Scenes in a Game instance.
You should not usually interact directly with the Scene Manager at all. Instead, you should use
the Scene Plugin, which is available from every Scene in your game via the this.scene property.
Using methods in this Scene Manager directly will break queued operations and can cause runtime
errors. Instead, go via the Scene Plugin. Every feature this Scene Manager provides is also
available via the Scene Plugin.
Constructor
new SceneManager(game, sceneConfig)
Parameters
name type optional description
game Phaser.Game No The Phaser.Game instance this Scene Manager belongs to.
sceneConfig object No Scene specific configuration settings.
Scope : static
Source: src/scene/SceneManager.js#L17
Since: 3.0.0
Public Members ​
customViewports ​
customViewports: number ​
Description:
Do any of the Cameras in any of the Scenes require a custom viewport?
If not we can skip scissor tests.
Source: src/scene/SceneManager.js#L134
Since: 3.12.0
game ​
game: Phaser.Game ​
Description:
The Game that this SceneManager belongs to.
Source: src/scene/SceneManager.js#L45
Since: 3.0.0
isBooted ​
isBooted: boolean ​
Description:
Has the Scene Manager properly started?
Source: src/scene/SceneManager.js#L123
Since: 3.4.0
isProcessing ​
isProcessing: boolean ​
Description:
Is the Scene Manager actively processing the Scenes list?
Source: src/scene/SceneManager.js#L112
Since: 3.0.0
keys ​
keys: Record.<string, Phaser.Scene > ​
Description:
An object that maps the keys to the scene so we can quickly get a scene from a key without iteration.
Source: src/scene/SceneManager.js#L54
Since: 3.0.0
scenes ​
scenes: Array.< Phaser.Scene > ​
Description:
The array in which all of the scenes are kept.
Source: src/scene/SceneManager.js#L63
Since: 3.0.0
systemScene ​
systemScene: Phaser.Scene ​
Description:
This system Scene is created during bootQueue and is a default
empty Scene that lives outside of the Scene list, but can be used
by plugins and managers that need access to a live Scene, without
being tied to one.
Source: src/scene/SceneManager.js#L145
Since: 3.60.0
Public Methods ​
add ​
<instance> add(key, sceneConfig, [autoStart], [data]) ​
Description:
Adds a new Scene into the SceneManager.
You must give each Scene a unique key by which you'll identify it.
The sceneConfig can be:
A Phaser.Scene object, or an object that extends it.
A plain JavaScript object
A JavaScript ES6 Class that extends Phaser.Scene
A JavaScript ES5 prototype based Class
A JavaScript function
If a function is given then a new Scene will be created by calling it.
Parameters:
name type optional default description
key string No A unique key used to reference the Scene, i.e. MainMenu or Level1 .
sceneConfig Phaser.Types.Scenes.SceneType No The config for the Scene
autoStart boolean Yes false If true the Scene will be started immediately after being added.
data object Yes Optional data object. This will be set as Scene.settings.data and passed to Scene.init , and Scene.create .
Returns: Phaser.Scene - The added Scene, if it was added immediately, otherwise null .
Source: src/scene/SceneManager.js#L319
Since: 3.0.0
bringToTop ​
<instance> bringToTop(key) ​
Description:
Brings a Scene to the top of the Scenes list.
This means it will render above all other Scenes.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to move.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1381
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroy this Scene Manager and all of its systems.
This process cannot be reversed.
This method is called automatically when a Phaser Game instance is destroyed.
Source: src/scene/SceneManager.js#L1706
Since: 3.0.0
dump ​
<instance> dump() ​
Description:
Dumps debug information about each Scene to the developer console.
Source: src/scene/SceneManager.js#L1682
Since: 3.2.0
getAt ​
<instance> getAt(index) ​
Description:
Retrieves a Scene by numeric index.
Tags:
generic
genericUse
Parameters:
name type optional description
index number No The index of the Scene to retrieve.
Returns: Phaser.Scene , undefined - The Scene.
Source: src/scene/SceneManager.js#L1343
Since: 3.0.0
getIndex ​
<instance> getIndex(key) ​
Description:
Retrieves the numeric index of a Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The key of the Scene.
Returns: number - The index of the Scene.
Source: src/scene/SceneManager.js#L1361
Since: 3.0.0
getScene ​
<instance> getScene(key) ​
Description:
Retrieves a Scene based on the given key.
If an actual Scene is passed to this method, it can be used to check if
its currently within the Scene Manager, or not.
Tags:
generic
genericUse
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The key of the Scene to retrieve.
Returns: Phaser.Scene - The Scene, or null if no matching Scene was found.
Source: src/scene/SceneManager.js#L878
Since: 3.0.0
getScenes ​
<instance> getScenes([isActive], [inReverse]) ​
Description:
Returns an array of all the current Scenes being managed by this Scene Manager.
You can filter the output by the active state of the Scene and choose to have
the array returned in normal or reversed order.
Tags:
generic
genericUse
Parameters:
name type optional default description
isActive boolean Yes true Only include Scene's that are currently active?
inReverse boolean Yes false Return the array of Scenes in reverse?
Returns: Array.< Phaser.Scene > - An array containing all of the Scenes in the Scene Manager.
Source: src/scene/SceneManager.js#L840
Since: 3.16.0
isActive ​
<instance> isActive(key) ​
Description:
Determines whether a Scene is running.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to check.
Returns: boolean - Whether the Scene is running, or null if no matching Scene was found.
Source: src/scene/SceneManager.js#L918
Since: 3.0.0
isPaused ​
<instance> isPaused(key) ​
Description:
Determines whether a Scene is paused.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to check.
Returns: boolean - Whether the Scene is paused, or null if no matching Scene was found.
Source: src/scene/SceneManager.js#L943
Since: 3.17.0
isSleeping ​
<instance> isSleeping(key) ​
Description:
Determines whether a Scene is sleeping.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to check.
Returns: boolean - Whether the Scene is sleeping, or null if no matching Scene was found.
Source: src/scene/SceneManager.js#L993
Since: 3.0.0
isVisible ​
<instance> isVisible(key) ​
Description:
Determines whether a Scene is visible.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to check.
Returns: boolean - Whether the Scene is visible, or null if no matching Scene was found.
Source: src/scene/SceneManager.js#L968
Since: 3.0.0
moveAbove ​
<instance> moveAbove(keyA, keyB) ​
Description:
Moves a Scene so it is immediately above another Scene in the Scenes list.
If the Scene is already above the other, it isn't moved.
This means it will render over the top of the other Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
keyA string | Phaser.Scene No The Scene that Scene B will be moved above.
keyB string | Phaser.Scene No The Scene to be moved.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1522
Since: 3.2.0
moveBelow ​
<instance> moveBelow(keyA, keyB) ​
Description:
Moves a Scene so it is immediately below another Scene in the Scenes list.
If the Scene is already below the other, it isn't moved.
This means it will render behind the other Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
keyA string | Phaser.Scene No The Scene that Scene B will be moved below.
keyB string | Phaser.Scene No The Scene to be moved.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1568
Since: 3.2.0
moveDown ​
<instance> moveDown(key) ​
Description:
Moves a Scene down one position in the Scenes list.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to move.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1452
Since: 3.0.0
moveUp ​
<instance> moveUp(key) ​
Description:
Moves a Scene up one position in the Scenes list.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to move.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1487
Since: 3.0.0
pause ​
<instance> pause(key, [data]) ​
Description:
Pauses the given Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to pause.
data object Yes An optional data object that will be passed to the Scene and emitted by its pause event.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1018
Since: 3.0.0
processQueue ​
<instance> processQueue() ​
Description:
Process the Scene operations queue.
Source: src/scene/SceneManager.js#L268
Since: 3.0.0
remove ​
<instance> remove(key) ​
Description:
Removes a Scene from the SceneManager.
The Scene is removed from the local scenes array, it's key is cleared from the keys
cache and Scene.Systems.destroy is then called on it.
If the SceneManager is processing the Scenes when this method is called it will
queue the operation for the next update sequence.
Parameters:
name type optional description
key string No A unique key used to reference the Scene, i.e. MainMenu or Level1 .
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L410
Since: 3.2.0
render ​
<instance> render(renderer) ​
Description:
Renders the Scenes.
Parameters:
name type optional description
renderer Phaser.Renderer.Canvas.CanvasRenderer | Phaser.Renderer.WebGL.WebGLRenderer No The renderer to use.
Source: src/scene/SceneManager.js#L578
Since: 3.0.0
resume ​
<instance> resume(key, [data]) ​
Description:
Resumes the given Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to resume.
data object Yes An optional data object that will be passed to the Scene and emitted by its resume event.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1044
Since: 3.0.0
run ​
<instance> run(key, [data]) ​
Description:
Runs the given Scene.
If the given Scene is paused, it will resume it. If sleeping, it will wake it.
If not running at all, it will be started.
Use this if you wish to open a modal Scene by calling pause on the current
Scene, then run on the modal Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to run.
data object Yes A data object that will be passed to the Scene on start, wake, or resume.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1122
Since: 3.10.0
sendToBack ​
<instance> sendToBack(key) ​
Description:
Sends a Scene to the back of the Scenes list.
This means it will render below all other Scenes.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to move.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1417
Since: 3.0.0
sleep ​
<instance> sleep(key, [data]) ​
Description:
Puts the given Scene to sleep.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to put to sleep.
data object Yes An optional data object that will be passed to the Scene and emitted by its sleep event.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1070
Since: 3.0.0
start ​
<instance> start(key, [data]) ​
Description:
Starts the given Scene, if it is not starting, loading, or creating.
If the Scene is running, paused, or sleeping, it will be shutdown and then started.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to start.
data object Yes Optional data object to pass to Scene.Settings and Scene.init , and Scene.create .
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1176
Since: 3.0.0
stop ​
<instance> stop(key, [data]) ​
Description:
Stops the given Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to stop.
data object Yes Optional data object to pass to Scene.shutdown.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1272
Since: 3.0.0
swapPosition ​
<instance> swapPosition(keyA, keyB) ​
Description:
Swaps the positions of two Scenes in the Scenes list.
Tags:
generic
genericUse
Parameters:
name type optional description
keyA string | Phaser.Scene No The first Scene to swap.
keyB string | Phaser.Scene No The second Scene to swap.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1642
Since: 3.0.0
switch ​
<instance> switch(from, to, [data]) ​
Description:
Sleeps one one Scene and starts the other.
Tags:
generic
genericUse
Parameters:
name type optional description
from string | Phaser.Scene No The Scene to sleep.
to string | Phaser.Scene No The Scene to start.
data object Yes Optional data object to pass to Scene.Settings and Scene.init , and Scene.create . It is only passed when the scene starts for the first time.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1306
Since: 3.0.0
update ​
<instance> update(time, delta) ​
Description:
Updates the Scenes.
Parameters:
name type optional description
time number No Time elapsed.
delta number No Delta time from the last update.
Source: src/scene/SceneManager.js#L546
Since: 3.0.0
wake ​
<instance> wake(key, [data]) ​
Description:
Awakens the given Scene.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | Phaser.Scene No The Scene to wake up.
data object Yes An optional data object that will be passed to the Scene and emitted by its wake event.
Returns: Phaser.Scenes.SceneManager - This Scene Manager instance.
Source: src/scene/SceneManager.js#L1096
Since: 3.0.0
Previous
Scene
Next
ScenePlugin
Public Members
customViewports
game
isBooted
isProcessing
keys
scenes
systemScene
Public Methods
add
bringToTop
destroy
dump
getAt
getIndex
getScene
getScenes
isActive
isPaused
isSleeping
isVisible
moveAbove
moveBelow
moveDown
moveUp
pause
processQueue
remove
render
resume
run
sendToBack
sleep
start
stop
swapPosition
switch
update
wake
