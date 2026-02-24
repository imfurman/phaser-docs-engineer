# Phaser.Input | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/input

Phaser API Documentation
Namespaces
Phaser.Input
Version: Phaser v3.90.0
On this page
Phaser.Input
Scope: static
Source: src/input/index.js#L10
Static functions ​
InputManager
InputPlugin
Pointer
Static functions ​
CreateInteractiveObject ​
<static> CreateInteractiveObject(gameObject, hitArea, hitAreaCallback) ​
Description:
Creates a new Interactive Object.
This is called automatically by the Input Manager when you enable a Game Object for input.
The resulting Interactive Object is mapped to the Game Object's input property.
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object to which this Interactive Object is bound.
hitArea any No The hit area for this Interactive Object. Typically a geometry shape, like a Rectangle or Circle.
hitAreaCallback Phaser.Types.Input.HitAreaCallback No The 'contains' check callback that the hit area shape will use for all hit tests.
Returns: Phaser.Types.Input.InteractiveObject - The new Interactive Object.
Source: src/input/CreateInteractiveObject.js#L7
Since: 3.0.0
CreatePixelPerfectHandler ​
<static> CreatePixelPerfectHandler(textureManager, alphaTolerance) ​
Description:
Creates a new Pixel Perfect Handler function.
Access via InputPlugin.makePixelPerfect rather than calling it directly.
Parameters:
name type optional description
textureManager Phaser.Textures.TextureManager No A reference to the Texture Manager.
alphaTolerance number No The alpha level that the pixel should be above to be included as a successful interaction.
Returns: function - The new Pixel Perfect Handler function.
Source: src/input/CreatePixelPerfectHandler.js#L7
Since: 3.10.0
Static functions ​
Events
Gamepad
InputPluginCache
Keyboard
Mouse
Touch
Static functions ​
MOUSE_DOWN ​
MOUSE_DOWN: number ​
Description:
The mouse pointer is being held down.
Source: src/input/const.js#L9
Since: 3.10.0
MOUSE_MOVE ​
MOUSE_MOVE: number ​
Description:
The mouse pointer is being moved.
Source: src/input/const.js#L18
Since: 3.10.0
MOUSE_UP ​
MOUSE_UP: number ​
Description:
The mouse pointer is released.
Source: src/input/const.js#L27
Since: 3.10.0
MOUSE_WHEEL ​
MOUSE_WHEEL: number ​
Description:
The mouse wheel changes.
Source: src/input/const.js#L81
Since: 3.18.0
POINTER_LOCK_CHANGE ​
POINTER_LOCK_CHANGE: number ​
Description:
The pointer lock has changed.
Source: src/input/const.js#L63
Since: 3.10.0
TOUCH_CANCEL ​
TOUCH_CANCEL: number ​
Description:
A touch pointer has been been cancelled by the browser.
Source: src/input/const.js#L72
Since: 3.15.0
TOUCH_END ​
TOUCH_END: number ​
Description:
A touch pointer has been started.
Source: src/input/const.js#L54
Since: 3.10.0
TOUCH_MOVE ​
TOUCH_MOVE: number ​
Description:
A touch pointer has been started.
Source: src/input/const.js#L45
Since: 3.10.0
TOUCH_START ​
TOUCH_START: number ​
Description:
A touch pointer has been started.
Source: src/input/const.js#L36
Since: 3.10.0
Previous
Phaser.Input.Touch
Next
Phaser.Loader.Events
Static functions
Static functions
CreateInteractiveObject
CreatePixelPerfectHandler
Static functions
Static functions
MOUSE_DOWN
MOUSE_MOVE
MOUSE_UP
MOUSE_WHEEL
POINTER_LOCK_CHANGE
TOUCH_CANCEL
TOUCH_END
TOUCH_MOVE
TOUCH_START
