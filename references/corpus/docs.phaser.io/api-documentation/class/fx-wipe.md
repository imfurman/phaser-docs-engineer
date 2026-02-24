# Wipe | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/fx-wipe

Phaser API Documentation
Class
Wipe
Version: Phaser v3.90.0
On this page
Wipe
The Wipe FX Controller.
This FX controller manages the wipe effect for a Game Object.
The wipe or reveal effect is a visual technique that gradually uncovers or conceals elements
in the game, such as images, text, or scene transitions. This effect is often used to create
a sense of progression, reveal hidden content, or provide a smooth and visually appealing transition
between game states.
You can set both the direction and the axis of the wipe effect. The following combinations are possible:
left to right: direction 0, axis 0
right to left: direction 1, axis 0
top to bottom: direction 1, axis 1
bottom to top: direction 1, axis 0
It is up to you to set the progress value yourself, i.e. via a Tween, in order to transition the effect.
A Wipe effect is added to a Game Object via the FX component:
const sprite = this . add . sprite ( ) ;
sprite . preFX . addWipe ( ) ;
sprite . postFX . addWipe ( ) ;
sprite . preFX . addReveal ( ) ;
sprite . postFX . addReveal ( ) ;
Constructor
new Wipe(gameObject, [wipeWidth], [direction], [axis], [reveal])
Parameters
name type optional default description
gameObject Phaser.GameObjects.GameObject No A reference to the Game Object that has this fx.
wipeWidth number Yes 0.1 The width of the wipe effect. This value is normalized in the range 0 to 1.
direction number Yes 0 The direction of the wipe effect. Either 0 or 1. Set in conjunction with the axis property.
axis number Yes 0 The axis of the wipe effect. Either 0 or 1. Set in conjunction with the direction property.
reveal boolean Yes false Is this a reveal (true) or a fade (false) effect?
Scope : static
Extends
Phaser.FX.Controller
Source: src/fx/Wipe.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.FX.Controller :
active
gameObject
type
Public Members ​
axis ​
axis: number ​
Description:
The axis of the wipe effect. Either 0 or 1. Set in conjunction with the direction property.
Source: src/fx/Wipe.js#L98
Since: 3.60.0
direction ​
direction: number ​
Description:
The direction of the wipe effect. Either 0 or 1. Set in conjunction with the axis property.
Source: src/fx/Wipe.js#L89
Since: 3.60.0
progress ​
progress: number ​
Description:
The progress of the Wipe effect. This value is normalized to the range 0 to 1.
Adjust this value to make the wipe transition (i.e. via a Tween)
Source: src/fx/Wipe.js#L69
Since: 3.60.0
reveal ​
reveal: boolean ​
Description:
Is this a reveal (true) or a fade (false) effect?
Source: src/fx/Wipe.js#L107
Since: 3.60.0
wipeWidth ​
wipeWidth: number ​
Description:
The width of the wipe effect. This value is normalized in the range 0 to 1.
Source: src/fx/Wipe.js#L80
Since: 3.60.0
Inherited Methods ​
From Phaser.FX.Controller :
destroy
setActive
Previous
Vignette
Next
Game
Inherited Members
Public Members
axis
direction
progress
reveal
wipeWidth
Inherited Methods
