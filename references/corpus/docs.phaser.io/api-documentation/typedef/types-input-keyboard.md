# Types.Input.Keyboard | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/types-input-keyboard

Phaser API Documentation
Typedefs
Types.Input.Keyboard
Version: Phaser v3.90.0
On this page
Types.Input.Keyboard
CursorKeys ​
<static> CursorKeys ​
name type optional description
up Phaser.Input.Keyboard.Key No A Key object mapping to the UP arrow key.
down Phaser.Input.Keyboard.Key No A Key object mapping to the DOWN arrow key.
left Phaser.Input.Keyboard.Key No A Key object mapping to the LEFT arrow key.
right Phaser.Input.Keyboard.Key No A Key object mapping to the RIGHT arrow key.
space Phaser.Input.Keyboard.Key No A Key object mapping to the SPACE BAR key.
shift Phaser.Input.Keyboard.Key No A Key object mapping to the SHIFT key.
Type : object
Member of : Phaser.Types.Input.Keyboard
Source: src/input/keyboard/typedefs/CursorKeys.js#L1
Since: 3.0.0
KeyComboConfig ​
<static> KeyComboConfig ​
name type optional default description
resetOnWrongKey boolean Yes true If they press the wrong key do we reset the combo?
maxKeyDelay number Yes 0 The max delay in ms between each key press. Above this the combo is reset. 0 means disabled.
resetOnMatch boolean Yes false If previously matched and they press the first key of the combo again, will it reset?
deleteOnMatch boolean Yes false If the combo matches, will it delete itself?
Type : object
Member of : Phaser.Types.Input.Keyboard
Source: src/input/keyboard/typedefs/KeyComboConfig.js#L1
Since: 3.0.0
KeyboardKeydownCallback ​
<static> KeyboardKeydownCallback ​
Type : function
Member of : Phaser.Types.Input.Keyboard
Source: src/input/keyboard/typedefs/KeyboardKeydownCallback.js#L1
Since: 3.0.0
Previous
Types.Input.Gamepad
Next
Types.Input
CursorKeys
<static> CursorKeys
KeyComboConfig
<static> KeyComboConfig
KeyboardKeydownCallback
<static> KeyboardKeydownCallback
