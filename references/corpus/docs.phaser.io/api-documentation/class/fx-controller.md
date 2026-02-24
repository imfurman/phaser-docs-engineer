# Controller | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-controller

Phaser API Documentation
Class
Controller
Version: Phaser v3.90.0
On this page
Controller
FX Controller is the base class that all built-in FX use.
You should not normally create an instance of this class directly, but instead use one of the built-in FX that extend it.
Constructor
new Controller(type, gameObject)
Parameters
name type optional description
type number No The FX Type constant.
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
Scope : static
Source: src/fx/Controller.js#L9
Since: 3.60.0
Public Members ​
active ​
active: boolean ​
Description:
Toggle this boolean to enable or disable this effect,
without removing and adding it from the Game Object.
Only works for Pre FX.
Post FX are always active.
Source: src/fx/Controller.js#L47
Since: 3.60.0
gameObject ​
gameObject: Phaser.GameObjects.GameObject ​
Description:
A reference to the Game Object that owns this effect.
Source: src/fx/Controller.js#L38
Since: 3.60.0
type ​
type: number ​
Description:
The FX_CONST type of this effect.
Source: src/fx/Controller.js#L29
Since: 3.60.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this FX Controller.
Source: src/fx/Controller.js#L81
Since: 3.60.0
setActive ​
<instance> setActive(value) ​
Description:
Sets the active state of this FX Controller.
A disabled FX Controller will not be updated.
Parameters:
name type optional description
value boolean No true to enable this FX Controller, or false to disable it.
Returns: Phaser.FX.Controller - This FX Controller instance.
Source: src/fx/Controller.js#L62
Since: 3.60.0
Previous
ColorMatrix
Next
Displacement
Public Members
active
gameObject
type
Public Methods
destroy
setActive
