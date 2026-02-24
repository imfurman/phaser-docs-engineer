# Phaser.Types.Input | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/types-input

Phaser API Documentation
Namespaces
Phaser.Types.Input
Version: Phaser v3.90.0
On this page
Phaser.Types.Input
Scope: static
Source: src/input/typedefs/index.js#L7
Static functions ​
Gamepad
Keyboard
Static functions ​
EventData ​
EventData ​
Description:
A Phaser Input Event Data object.
This object is passed to the registered event listeners and allows you to stop any further propagation.
Source: src/input/typedefs/EventData.js#L7
Since: 3.15.1
HitAreaCallback ​
HitAreaCallback ​
Parameters:
name type optional description
hitArea any No The hit area object.
x number No The translated x coordinate of the hit test event.
y number No The translated y coordinate of the hit test event.
gameObject Phaser.GameObjects.GameObject No The Game Object that invoked the hit test.
Returns: boolean - true if the coordinates fall within the space of the hitArea, otherwise false .
Source: src/input/typedefs/HitAreaCallback.js#L1
Since: 3.0.0
InputConfiguration ​
InputConfiguration ​
Source: src/input/typedefs/InputConfiguration.js#L1
Since: 3.0.0
InputPluginContainer ​
InputPluginContainer ​
Source: src/input/typedefs/InputPluginContainer.js#L1
Since: 3.0.0
InteractiveObject ​
InteractiveObject ​
Source: src/input/typedefs/InteractiveObject.js#L1
Since: 3.0.0
Previous
Phaser.Types.Input.Keyboard
Next
Phaser.Types.Loader.FileTypes
Static functions
Static functions
EventData
HitAreaCallback
InputConfiguration
InputPluginContainer
InteractiveObject
