# KeyCombo | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/input-keyboard-keycombo

Phaser API Documentation
Class
KeyCombo
Version: Phaser v3.90.0
On this page
KeyCombo
A KeyCombo will listen for a specific string of keys from the Keyboard, and when it receives them
it will emit a keycombomatch event from the Keyboard Manager.
The keys to be listened for can be defined as:
A string (i.e. 'ATARI')
An array of either integers (key codes) or strings, or a mixture of both
An array of objects (such as Key objects) with a public 'keyCode' property
For example, to listen for the Konami code (up, up, down, down, left, right, left, right, b, a, enter)
you could pass the following array of key codes:
this . input . keyboard . createCombo ( [ 38 , 38 , 40 , 40 , 37 , 39 , 37 , 39 , 66 , 65 , 13 ] , { resetOnMatch : true } ) ;
this . input . keyboard . on ( 'keycombomatch' , function ( event ) {
console . log ( 'Konami Code entered!' ) ;
} ) ;
Or, to listen for the user entering the word PHASER:
this . input . keyboard . createCombo ( 'PHASER' ) ;
Constructor
new KeyCombo(keyboardPlugin, keys, [config])
Parameters
name type optional description
keyboardPlugin Phaser.Input.Keyboard.KeyboardPlugin No A reference to the Keyboard Plugin.
keys string | Array.<number> Array.<object> No
config Phaser.Types.Input.Keyboard.KeyComboConfig Yes A Key Combo configuration object.
Scope : static
Source: src/input/keyboard/combo/KeyCombo.js#L13
Since: 3.0.0
Public Members ​
current ​
current: number ​
Description:
The current keyCode the combo is waiting for.
Source: src/input/keyboard/combo/KeyCombo.js#L114
Since: 3.0.0
deleteOnMatch ​
deleteOnMatch: boolean ​
Description:
If the combo matches, will it delete itself?
Source: src/input/keyboard/combo/KeyCombo.js#L202
Since: 3.0.0
enabled ​
enabled: boolean ​
Description:
A flag that controls if this Key Combo is actively processing keys or not.
Source: src/input/keyboard/combo/KeyCombo.js#L74
Since: 3.0.0
index ​
index: number ​
Description:
The current index of the key being waited for in the 'keys' string.
Source: src/input/keyboard/combo/KeyCombo.js#L123
Since: 3.0.0
keyCodes ​
keyCodes: array ​
Description:
An array of the keycodes that comprise this combo.
Source: src/input/keyboard/combo/KeyCombo.js#L84
Since: 3.0.0
manager ​
manager: Phaser.Input.Keyboard.KeyboardPlugin ​
Description:
A reference to the Keyboard Manager
Source: src/input/keyboard/combo/KeyCombo.js#L65
Since: 3.0.0
matched ​
matched: boolean ​
Description:
Has this Key Combo been matched yet?
Source: src/input/keyboard/combo/KeyCombo.js#L152
Since: 3.0.0
maxKeyDelay ​
maxKeyDelay: number ​
Description:
The max delay in ms between each key press. Above this the combo is reset. 0 means disabled.
Source: src/input/keyboard/combo/KeyCombo.js#L182
Since: 3.0.0
progress ​
progress: number ​
Description:
How far complete is this combo? A value between 0 and 1.
Source: src/input/keyboard/combo/KeyCombo.js#L252
Since: 3.0.0
resetOnMatch ​
resetOnMatch: boolean ​
Description:
If previously matched and they press the first key of the combo again, will it reset?
Source: src/input/keyboard/combo/KeyCombo.js#L192
Since: 3.0.0
resetOnWrongKey ​
resetOnWrongKey: boolean ​
Description:
If they press the wrong key do we reset the combo?
Source: src/input/keyboard/combo/KeyCombo.js#L172
Since: 3.0.0
size ​
size: number ​
Description:
The length of this combo (in keycodes)
Source: src/input/keyboard/combo/KeyCombo.js#L133
Since: 3.0.0
timeLastMatched ​
timeLastMatched: number ​
Description:
The time the previous key in the combo was matched.
Source: src/input/keyboard/combo/KeyCombo.js#L142
Since: 3.0.0
timeMatched ​
timeMatched: number ​
Description:
The time the entire combo was matched.
Source: src/input/keyboard/combo/KeyCombo.js#L162
Since: 3.0.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroys this Key Combo and all of its references.
Source: src/input/keyboard/combo/KeyCombo.js#L269
Since: 3.0.0
Previous
Key
Next
KeyboardManager
Public Members
current
deleteOnMatch
enabled
index
keyCodes
manager
matched
maxKeyDelay
progress
resetOnMatch
resetOnWrongKey
size
timeLastMatched
timeMatched
Public Methods
destroy
