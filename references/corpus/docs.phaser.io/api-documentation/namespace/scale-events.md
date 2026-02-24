# Phaser.Scale.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/scale-events

Phaser API Documentation
Namespaces
Phaser.Scale.Events
Version: Phaser v3.90.0
On this page
Phaser.Scale.Events
Scope: static
Source: src/scale/events/index.js#L7
Static functions ​
ENTER_FULLSCREEN ​
ENTER_FULLSCREEN ​
Description:
The Scale Manager has successfully entered fullscreen mode.
Source: src/scale/events/ENTER_FULLSCREEN_EVENT.js#L7
Since: 3.16.1
FULLSCREEN_FAILED ​
FULLSCREEN_FAILED ​
Description:
The Scale Manager tried to enter fullscreen mode but failed.
Source: src/scale/events/FULLSCREEN_FAILED_EVENT.js#L7
Since: 3.17.0
FULLSCREEN_UNSUPPORTED ​
FULLSCREEN_UNSUPPORTED ​
Description:
The Scale Manager tried to enter fullscreen mode, but it is unsupported by the browser.
Source: src/scale/events/FULLSCREEN_UNSUPPORTED_EVENT.js#L7
Since: 3.16.1
LEAVE_FULLSCREEN ​
LEAVE_FULLSCREEN ​
Description:
The Scale Manager was in fullscreen mode, but has since left, either directly via game code,
or via a user gestured, such as pressing the ESC key.
Source: src/scale/events/LEAVE_FULLSCREEN_EVENT.js#L7
Since: 3.16.1
ORIENTATION_CHANGE ​
ORIENTATION_CHANGE ​
Description:
The Scale Manager Orientation Change Event.
This event is dispatched whenever the Scale Manager detects an orientation change event from the browser.
Parameters:
name type optional description
orientation string No The new orientation value. Either Phaser.Scale.Orientation.LANDSCAPE or Phaser.Scale.Orientation.PORTRAIT .
Source: src/scale/events/ORIENTATION_CHANGE_EVENT.js#L7
Since: 3.16.1
RESIZE ​
RESIZE ​
Description:
The Scale Manager Resize Event.
This event is dispatched whenever the Scale Manager detects a resize event from the browser.
It sends three parameters to the callback, each of them being Size components. You can read
the width , height , aspectRatio and other properties of these components to help with
scaling your own game content.
Parameters:
name type optional description
gameSize Phaser.Structs.Size No A reference to the Game Size component. This is the un-scaled size of your game canvas.
baseSize Phaser.Structs.Size No A reference to the Base Size component. This is the game size.
displaySize Phaser.Structs.Size No A reference to the Display Size component. This is the scaled canvas size, after applying zoom and scale mode.
previousWidth number No If the gameSize has changed, this value contains its previous width, otherwise it contains the current width.
previousHeight number No If the gameSize has changed, this value contains its previous height, otherwise it contains the current height.
Source: src/scale/events/RESIZE_EVENT.js#L7
Since: 3.16.1
Previous
Phaser.Scale.Center
Next
Phaser.Scale.Orientation
Static functions
ENTER_FULLSCREEN
FULLSCREEN_FAILED
FULLSCREEN_UNSUPPORTED
LEAVE_FULLSCREEN
ORIENTATION_CHANGE
RESIZE
