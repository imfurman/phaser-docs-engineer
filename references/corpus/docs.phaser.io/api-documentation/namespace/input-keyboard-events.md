# Phaser.Input.Keyboard.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/input-keyboard-events

Phaser API Documentation
Namespaces
Phaser.Input.Keyboard.Events
Version: Phaser v3.90.0
On this page
Phaser.Input.Keyboard.Events
Scope: static
Source: src/input/keyboard/events/index.js#L7
Static functions ​
ANY_KEY_DOWN ​
ANY_KEY_DOWN ​
Description:
The Global Key Down Event.
This event is dispatched by the Keyboard Plugin when any key on the keyboard is pressed down.
Listen to this event from within a Scene using: this.input.keyboard.on('keydown', listener) .
You can also listen for a specific key being pressed. See Keyboard.Events.KEY_DOWN for details.
Finally, you can create Key objects, which you can also listen for events from. See Keyboard.Events.DOWN for details.
Note : Many keyboards are unable to process certain combinations of keys due to hardware limitations known as ghosting.
Read [this article on ghosting]{@link http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/ } for details.
Also, please be aware that some browser extensions can disable or override Phaser keyboard handling.
For example, the Chrome extension vimium is known to disable Phaser from using the D key, while EverNote disables the backtick key.
There are others. So, please check your extensions if you find you have specific keys that don't work.
Parameters:
name type optional description
event KeyboardEvent No The native DOM Keyboard Event. You can inspect this to learn more about the key that was pressed, any modifiers, etc.
Source: src/input/keyboard/events/ANY_KEY_DOWN_EVENT.js#L7
Since: 3.0.0
ANY_KEY_UP ​
ANY_KEY_UP ​
Description:
The Global Key Up Event.
This event is dispatched by the Keyboard Plugin when any key on the keyboard is released.
Listen to this event from within a Scene using: this.input.keyboard.on('keyup', listener) .
You can also listen for a specific key being released. See Keyboard.Events.KEY_UP for details.
Finally, you can create Key objects, which you can also listen for events from. See Keyboard.Events.UP for details.
Parameters:
name type optional description
event KeyboardEvent No The native DOM Keyboard Event. You can inspect this to learn more about the key that was released, any modifiers, etc.
Source: src/input/keyboard/events/ANY_KEY_UP_EVENT.js#L7
Since: 3.0.0
COMBO_MATCH ​
COMBO_MATCH ​
Description:
The Key Combo Match Event.
This event is dispatched by the Keyboard Plugin when a Key Combo is matched.
Listen for this event from the Key Plugin after a combo has been created:
this . input . keyboard . createCombo ( [ 38 , 38 , 40 , 40 , 37 , 39 , 37 , 39 , 66 , 65 , 13 ] , { resetOnMatch : true } ) ;
this . input . keyboard . on ( 'keycombomatch' , function ( event ) {
console . log ( 'Konami Code entered!' ) ;
} ) ;
Parameters:
name type optional description
keycombo Phaser.Input.Keyboard.KeyCombo No The Key Combo object that was matched.
event KeyboardEvent No The native DOM Keyboard Event of the final key in the combo. You can inspect this to learn more about any modifiers, etc.
Source: src/input/keyboard/events/COMBO_MATCH_EVENT.js#L7
Since: 3.0.0
DOWN ​
DOWN ​
Description:
The Key Down Event.
This event is dispatched by a Key object when it is pressed.
Listen for this event from the Key object instance directly:
var spaceBar = this . input . keyboard . addKey ( Phaser . Input . Keyboard . KeyCodes . SPACE ) ;
spaceBar . on ( 'down' , listener )
You can also create a generic 'global' listener. See Keyboard.Events.ANY_KEY_DOWN for details.
Parameters:
name type optional description
key Phaser.Input.Keyboard.Key No The Key object that was pressed.
event KeyboardEvent No The native DOM Keyboard Event. You can inspect this to learn more about any modifiers, etc.
Source: src/input/keyboard/events/DOWN_EVENT.js#L7
Since: 3.0.0
KEY_DOWN ​
KEY_DOWN ​
Description:
The Key Down Event.
This event is dispatched by the Keyboard Plugin when any key on the keyboard is pressed down.
Unlike the ANY_KEY_DOWN event, this one has a special dynamic event name. For example, to listen for the A key being pressed
use the following from within a Scene: this.input.keyboard.on('keydown-A', listener) . You can replace the -A part of the event
name with any valid Key Code string . For example, this will listen for the space bar:
this.input.keyboard.on('keydown-SPACE', listener) .
You can also create a generic 'global' listener. See Keyboard.Events.ANY_KEY_DOWN for details.
Finally, you can create Key objects, which you can also listen for events from. See Keyboard.Events.DOWN for details.
Note : Many keyboards are unable to process certain combinations of keys due to hardware limitations known as ghosting.
Read [this article on ghosting]{@link http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/} for details.
Also, please be aware that some browser extensions can disable or override Phaser keyboard handling.
For example, the Chrome extension vimium is known to disable Phaser from using the D key, while EverNote disables the backtick key.
There are others. So, please check your extensions if you find you have specific keys that don't work.
Parameters:
name type optional description
event KeyboardEvent No The native DOM Keyboard Event. You can inspect this to learn more about the key that was pressed, any modifiers, etc.
Source: src/input/keyboard/events/KEY_DOWN_EVENT.js#L7
Since: 3.0.0
KEY_UP ​
KEY_UP ​
Description:
The Key Up Event.
This event is dispatched by the Keyboard Plugin when any key on the keyboard is released.
Unlike the ANY_KEY_UP event, this one has a special dynamic event name. For example, to listen for the A key being released
use the following from within a Scene: this.input.keyboard.on('keyup-A', listener) . You can replace the -A part of the event
name with any valid Key Code string . For example, this will listen for the space bar:
this.input.keyboard.on('keyup-SPACE', listener) .
You can also create a generic 'global' listener. See Keyboard.Events.ANY_KEY_UP for details.
Finally, you can create Key objects, which you can also listen for events from. See Keyboard.Events.UP for details.
Parameters:
name type optional description
event KeyboardEvent No The native DOM Keyboard Event. You can inspect this to learn more about the key that was released, any modifiers, etc.
Source: src/input/keyboard/events/KEY_UP_EVENT.js#L7
Since: 3.0.0
UP ​
UP ​
Description:
The Key Up Event.
This event is dispatched by a Key object when it is released.
Listen for this event from the Key object instance directly:
var spaceBar = this . input . keyboard . addKey ( Phaser . Input . Keyboard . KeyCodes . SPACE ) ;
spaceBar . on ( 'up' , listener )
You can also create a generic 'global' listener. See Keyboard.Events.ANY_KEY_UP for details.
Parameters:
name type optional description
key Phaser.Input.Keyboard.Key No The Key object that was released.
event KeyboardEvent No The native DOM Keyboard Event. You can inspect this to learn more about any modifiers, etc.
Source: src/input/keyboard/events/UP_EVENT.js#L7
Since: 3.0.0
Previous
Phaser.Input.InputPluginCache
Next
Phaser.Input.Keyboard.KeyCodes
Static functions
ANY_KEY_DOWN
ANY_KEY_UP
COMBO_MATCH
DOWN
KEY_DOWN
KEY_UP
UP
