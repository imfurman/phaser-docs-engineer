# NoAudioSoundManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/sound-noaudiosoundmanager

Phaser API Documentation
Class
NoAudioSoundManager
Version: Phaser v3.90.0
On this page
NoAudioSoundManager
No-audio implementation of the Sound Manager. It is used if audio has been
disabled in the game config or the device doesn't support any audio.
It represents a graceful degradation of Sound Manager logic that provides
minimal functionality and prevents Phaser projects that use audio from
breaking on devices that don't support any audio playback technologies.
Constructor
new NoAudioSoundManager(game)
Parameters
name type optional description
game Phaser.Game No Reference to the current game instance.
Scope : static
Extends
Phaser.Sound.BaseSoundManager
Source: src/sound/noaudio/NoAudioSoundManager.js#L14
Since: 3.0.0
Inherited Methods ​
From Phaser.Events.EventEmitter :
addListener
emit
eventNames
listenerCount
listeners
off
on
once
removeAllListeners
removeListener
shutdown
From Phaser.Sound.BaseSoundManager :
getAllPlaying
isPlaying
setListenerPosition
Public Methods ​
add ​
<instance> add(key, [config]) ​
Description:
Adds a new sound into the sound manager.
Parameters:
name type optional description
key string No Asset key for the sound.
config Phaser.Types.Sound.SoundConfig Yes An optional config object containing default sound settings.
Overrides: Phaser.Sound.BaseSoundManager#add
Returns: Phaser.Sound.NoAudioSound - The new sound instance.
Source: src/sound/noaudio/NoAudioSoundManager.js#L51
Since: 3.60.0
addAudioSprite ​
<instance> addAudioSprite(key, [config]) ​
Description:
Adds a new audio sprite sound into the sound manager.
Audio Sprites are a combination of audio files and a JSON configuration.
The JSON follows the format of that created by https://github.com/tonistiigi/audiosprite
Parameters:
name type optional description
key string No Asset key for the sound.
config Phaser.Types.Sound.SoundConfig Yes An optional config object containing default sound settings.
Overrides: Phaser.Sound.BaseSoundManager#addAudioSprite
Returns: Phaser.Sound.NoAudioSound - The new audio sprite sound instance.
Source: src/sound/noaudio/NoAudioSoundManager.js#L71
Since: 3.60.0
destroy ​
<instance> destroy() ​
Description:
Destroys all the sounds in the game and all associated events.
Overrides: Phaser.Sound.BaseSoundManager#destroy
Source: src/sound/noaudio/NoAudioSoundManager.js#L347
Since: 3.0.0
get ​
<instance> get(key) ​
Description:
Gets the first sound in the manager matching the given key, if any.
Tags:
generic
genericUse
Parameters:
name type optional description
key string No Sound asset key.
Overrides: Phaser.Sound.BaseSoundManager#get
Returns: Phaser.Sound.BaseSound - - The sound, or null.
Source: src/sound/noaudio/NoAudioSoundManager.js#L93
Since: 3.23.0
getAll ​
<instance> getAll(key) ​
Description:
Gets any sounds in the manager matching the given key.
Tags:
generic
genericUse
Parameters:
name type optional description
key string No Sound asset key.
Overrides: Phaser.Sound.BaseSoundManager#getAll
Returns: Array.< Phaser.Sound.BaseSound > - - The sounds, or an empty array.
Source: src/sound/noaudio/NoAudioSoundManager.js#L111
Since: 3.23.0
onBlur ​
<instance> onBlur() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#onBlur
Source: src/sound/noaudio/NoAudioSoundManager.js#L224
Since: 3.0.0
onFocus ​
<instance> onFocus() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#onFocus
Source: src/sound/noaudio/NoAudioSoundManager.js#L232
Since: 3.0.0
onGameBlur ​
<instance> onGameBlur() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#onGameBlur
Source: src/sound/noaudio/NoAudioSoundManager.js#L240
Since: 3.0.0
onGameFocus ​
<instance> onGameFocus() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#onGameFocus
Source: src/sound/noaudio/NoAudioSoundManager.js#L248
Since: 3.0.0
pauseAll ​
<instance> pauseAll() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#pauseAll
Source: src/sound/noaudio/NoAudioSoundManager.js#L256
Since: 3.0.0
play ​
<instance> play(key, [extra]) ​
Description:
This method does nothing but return 'false' for the No Audio Sound Manager, to maintain
compatibility with the other Sound Managers.
Parameters:
name type optional description
key string No Asset key for the sound.
extra Phaser.Types.Sound.SoundConfig | Phaser.Types.Sound.SoundMarker Yes An optional additional object containing settings to be applied to the sound. It could be either config or marker object.
Overrides: Phaser.Sound.BaseSoundManager#play
Returns: boolean - Always 'false' for the No Audio Sound Manager.
Source: src/sound/noaudio/NoAudioSoundManager.js#L129
Since: 3.0.0
playAudioSprite ​
<instance> playAudioSprite(key, spriteName, [config]) ​
Description:
This method does nothing but return 'false' for the No Audio Sound Manager, to maintain
compatibility with the other Sound Managers.
Parameters:
name type optional description
key string No Asset key for the sound.
spriteName string No The name of the sound sprite to play.
config Phaser.Types.Sound.SoundConfig Yes An optional config object containing default sound settings.
Overrides: Phaser.Sound.BaseSoundManager#playAudioSprite
Returns: boolean - Always 'false' for the No Audio Sound Manager.
Source: src/sound/noaudio/NoAudioSoundManager.js#L147
Since: 3.0.0
remove ​
<instance> remove(sound) ​
Description:
Removes a sound from the sound manager.
The removed sound is destroyed before removal.
Parameters:
name type optional description
sound Phaser.Sound.BaseSound No The sound object to remove.
Overrides: Phaser.Sound.BaseSoundManager#remove
Returns: boolean - True if the sound was removed successfully, otherwise false.
Source: src/sound/noaudio/NoAudioSoundManager.js#L166
Since: 3.0.0
removeAll ​
<instance> removeAll() ​
Description:
Removes all sounds from the manager, destroying the sounds.
Overrides: Phaser.Sound.BaseSoundManager#removeAll
Source: src/sound/noaudio/NoAudioSoundManager.js#L182
Since: 3.23.0
removeByKey ​
<instance> removeByKey(key) ​
Description:
Removes all sounds from the sound manager that have an asset key matching the given value.
The removed sounds are destroyed before removal.
Parameters:
name type optional description
key string No The key to match when removing sound objects.
Overrides: Phaser.Sound.BaseSoundManager#removeByKey
Returns: number - The number of matching sound objects that were removed.
Source: src/sound/noaudio/NoAudioSoundManager.js#L193
Since: 3.0.0
resumeAll ​
<instance> resumeAll() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#resumeAll
Source: src/sound/noaudio/NoAudioSoundManager.js#L264
Since: 3.0.0
setDetune ​
<instance> setDetune() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#setDetune
Returns: Phaser.Sound.NoAudioSoundManager - This Sound Manager.
Source: src/sound/noaudio/NoAudioSoundManager.js#L298
Since: 3.0.0
setMute ​
<instance> setMute() ​
Description:
Empty function for the No Audio Sound Manager.
Source: src/sound/noaudio/NoAudioSoundManager.js#L308
Since: 3.0.0
setRate ​
<instance> setRate() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#setRate
Returns: Phaser.Sound.NoAudioSoundManager - This Sound Manager.
Source: src/sound/noaudio/NoAudioSoundManager.js#L288
Since: 3.0.0
setVolume ​
<instance> setVolume() ​
Description:
Empty function for the No Audio Sound Manager.
Source: src/sound/noaudio/NoAudioSoundManager.js#L316
Since: 3.0.0
stopAll ​
<instance> stopAll() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#stopAll
Source: src/sound/noaudio/NoAudioSoundManager.js#L272
Since: 3.0.0
stopByKey ​
<instance> stopByKey(key) ​
Description:
Stops any sounds matching the given key.
Parameters:
name type optional description
key string No Sound asset key.
Overrides: Phaser.Sound.BaseSoundManager#stopByKey
Returns: number - - How many sounds were stopped.
Source: src/sound/noaudio/NoAudioSoundManager.js#L209
Since: 3.23.0
unlock ​
<instance> unlock() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#unlock
Source: src/sound/noaudio/NoAudioSoundManager.js#L324
Since: 3.0.0
update ​
<instance> update() ​
Description:
Empty function for the No Audio Sound Manager.
Overrides: Phaser.Sound.BaseSoundManager#update
Source: src/sound/noaudio/NoAudioSoundManager.js#L280
Since: 3.0.0
Inherited Members ​
From Phaser.Sound.BaseSoundManager :
detune
game
gameLostFocus
jsonCache
listenerPosition
locked
mute
pauseOnBlur
rate
volume
Previous
NoAudioSound
Next
WebAudioSound
Inherited Methods
Public Methods
add
addAudioSprite
destroy
get
getAll
onBlur
onFocus
onGameBlur
onGameFocus
pauseAll
play
playAudioSprite
remove
removeAll
removeByKey
resumeAll
setDetune
setMute
setRate
setVolume
stopAll
stopByKey
unlock
update
Inherited Members
