# Phaser.Sound | Phaser Help

Source: https://docs.phaser.io/api-documentation/function/sound

Phaser API Documentation
Functions
Phaser.Sound
Version: Phaser v3.90.0
On this page
Phaser.Sound
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
Previous
Phaser.Scenes
Next
Phaser.Textures
SoundManagerCreator
