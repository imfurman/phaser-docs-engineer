# Phaser.Sound | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/sound

Phaser API Documentation
Namespaces
Phaser.Sound
Version: Phaser v3.90.0
On this page
Phaser.Sound
Scope: static
Source: src/sound/index.js#L8
Static functions ​
BaseSound
BaseSoundManager
HTML5AudioSound
HTML5AudioSoundManager
NoAudioSound
NoAudioSoundManager
WebAudioSound
WebAudioSoundManager
Static functions ​
SoundManagerCreator ​
<static> SoundManagerCreator(game) ​
Description:
Creates a Web Audio, HTML5 Audio or No Audio Sound Manager based on config and device settings.
Be aware of https://developers.google.com/web/updates/2017/09/autoplay-policy-changes
Parameters:
name type optional description
game Phaser.Game No Reference to the current game instance.
Returns: Phaser.Sound.HTML5AudioSoundManager , Phaser.Sound.WebAudioSoundManager , Phaser.Sound.NoAudioSoundManager - The Sound Manager instance that was created.
Source: src/sound/SoundManagerCreator.js#L12
Since: 3.0.0
Static functions ​
Events
Previous
Phaser.Sound.Events
Next
Phaser.Structs.Events
Static functions
Static functions
SoundManagerCreator
Static functions
