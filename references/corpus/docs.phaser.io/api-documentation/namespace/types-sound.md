# Phaser.Types.Sound | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/types-sound

Phaser API Documentation
Namespaces
Phaser.Types.Sound
Version: Phaser v3.90.0
On this page
Phaser.Types.Sound
Scope: static
Source: src/sound/typedefs/index.js#L7
Static functions ​
AudioSpriteSound ​
AudioSpriteSound ​
Description:
Audio sprite sound type.
Source: src/sound/typedefs/AudioSpriteSound.js#L1
Since: 3.0.0
DecodeAudioConfig ​
DecodeAudioConfig ​
Description:
A Audio Data object.
You can pass an array of these objects to the WebAudioSoundManager decodeAudio method to have it decode
them all at once.
Source: src/sound/typedefs/DecodeAudioConfig.js#L1
Since: 3.18.0
EachActiveSoundCallback ​
EachActiveSoundCallback ​
Parameters:
name type optional description
manager Phaser.Sound.BaseSoundManager No The SoundManager
sound Phaser.Sound.BaseSound No The current active Sound
index number No The index of the current active Sound
sounds Array.< Phaser.Sound.BaseSound > No All sounds
Source: src/sound/typedefs/EachActiveSoundCallback.js#L1
Since: 3.0.0
SoundConfig ​
SoundConfig ​
Description:
Config object containing various sound settings.
Source: src/sound/typedefs/SoundConfig.js#L1
Since: 3.0.0
SoundMarker ​
SoundMarker ​
Description:
Marked section of a sound represented by name, and optionally start time, duration, and config object.
Source: src/sound/typedefs/SoundMarker.js#L1
Since: 3.0.0
SpatialSoundConfig ​
SpatialSoundConfig ​
Description:
Config object containing settings for the source of the spatial sound.
See https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics
Source: src/sound/typedefs/SpatialSoundConfig.js#L1
Since: 3.60.0
WebAudioDecodeEntry ​
WebAudioDecodeEntry ​
Description:
An entry in the Web Audio Decoding Queue.
Source: src/sound/typedefs/WebAudioDecodeEntry.js#L1
Since: 3.60.0
Previous
Phaser.Types.Scenes
Next
Phaser.Types.Textures
Static functions
AudioSpriteSound
DecodeAudioConfig
EachActiveSoundCallback
SoundConfig
SoundMarker
SpatialSoundConfig
WebAudioDecodeEntry
