# BaseSoundManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/sound-basesoundmanager

Phaser API Documentation
Class
BaseSoundManager
Version: Phaser v3.90.0
On this page
BaseSoundManager
Base class for other Sound Manager classes.
Constructor
new BaseSoundManager(game)
Parameters
name type optional description
game Phaser.Game No Reference to the current game instance.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/sound/BaseSoundManager.js#L18
Since: 3.0.0
Public Members ​
detune ​
detune: number ​
Description:
Global detuning of all sounds in cents .
The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Source: src/sound/BaseSoundManager.js#L805
Since: 3.0.0
game ​
game: Phaser.Game ​
Description:
Local reference to game.
Source: src/sound/BaseSoundManager.js#L44
Since: 3.0.0
gameLostFocus ​
gameLostFocus: boolean ​
Description:
Flag used to track if the game has lost focus.
Source: src/sound/BaseSoundManager.js#L152
Since: 3.60.0
jsonCache ​
jsonCache: Phaser.Cache.BaseCache ​
Description:
Local reference to the JSON Cache, as used by Audio Sprites.
Source: src/sound/BaseSoundManager.js#L54
Since: 3.7.0
listenerPosition ​
listenerPosition: Phaser.Math.Vector2 ​
Description:
The Spatial Audio listener position.
Only available with WebAudio.
You can modify the x/y properties of this Vec2 directly to
adjust the listener position within the game world.
Source: src/sound/BaseSoundManager.js#L162
Since: 3.60.0
locked ​
locked: boolean ​
Description:
Mobile devices require sounds to be triggered from an explicit user action,
such as a tap, before any sound can be loaded/played on a web page.
Set to true if the audio system is currently locked awaiting user interaction.
Source: src/sound/BaseSoundManager.js#L128
Since: 3.0.0
mute ​
mute: boolean ​
Description:
Global mute setting.
Source: src/sound/BaseSoundManager.js#L75
Since: 3.0.0
pauseOnBlur ​
pauseOnBlur: boolean ​
Description:
Flag indicating if sounds should be paused when game looses focus,
for instance when user switches to another tab/program/app.
Source: src/sound/BaseSoundManager.js#L95
Since: 3.0.0
rate ​
rate: number ​
Description:
Global playback rate at which all the sounds will be played.
Value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed
and 2.0 doubles the audio's playback speed.
Source: src/sound/BaseSoundManager.js#L755
Since: 3.0.0
volume ​
volume: number ​
Description:
Global volume setting.
Source: src/sound/BaseSoundManager.js#L85
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
Public Methods ​
add ​
<instance> add(key, [config]) ​
Description:
Adds a new sound into the sound manager.
Parameters:
name type optional description
key string No Asset key for the sound.
config Phaser.Types.Sound.SoundConfig Yes An optional config object containing default sound settings.
Returns: Phaser.Sound.BaseSound - The new sound instance.
Source: src/sound/BaseSoundManager.js#L184
Since: 3.0.0
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
Returns: Phaser.Sound.NoAudioSound , Phaser.Sound.HTML5AudioSound , Phaser.Sound.WebAudioSound - The new audio sprite sound instance.
Source: src/sound/BaseSoundManager.js#L198
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys all the sounds in the game and all associated events.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/sound/BaseSoundManager.js#L689
Since: 3.0.0
get ​
<instance> get(key) ​
Description:
Gets the first sound in this Sound Manager that matches the given key.
If none can be found it returns null .
Tags:
generic
genericUse
Parameters:
name type optional description
key string No Sound asset key.
Returns: Phaser.Sound.BaseSound - - The sound, or null.
Source: src/sound/BaseSoundManager.js#L243
Since: 3.23.0
getAll ​
<instance> getAll([key]) ​
Description:
Gets all sounds in this Sound Manager.
You can optionally specify a key, in which case only Sound instances that match the given key
will be returned.
Tags:
generic
genericUse
Parameters:
name type optional description
key string Yes Optional asset key. If given, only Sound instances with this key will be returned.
Returns: Array.< Phaser.Sound.BaseSound > - - The sounds, or an empty array.
Source: src/sound/BaseSoundManager.js#L262
Since: 3.23.0
getAllPlaying ​
<instance> getAllPlaying() ​
Description:
Returns all sounds from this Sound Manager that are currently
playing. That is, Sound instances that have their isPlaying
property set to true .
Tags:
generic
genericUse
Returns: Array.< Phaser.Sound.BaseSound > - - All currently playing sounds, or an empty array.
Source: src/sound/BaseSoundManager.js#L290
Since: 3.60.0
isPlaying ​
<instance> isPlaying(key) ​
Description:
When a key is given, returns true if any sound with that key is playing.
When no key is given, returns true if any sound is playing.
Parameters:
name type optional description
key string No Sound asset key.
Returns: boolean - - Per the key argument, true if any matching sound is playing, otherwise false.
Source: src/sound/BaseSoundManager.js#L538
Since: 3.85.0
onBlur ​
<instance> onBlur() ​
Description:
Method used internally for pausing sound manager if
Phaser.Sound.BaseSoundManager#pauseOnBlur is set to true.
Access: protected
Source: src/sound/BaseSoundManager.js#L597
Since: 3.0.0
onFocus ​
<instance> onFocus() ​
Description:
Method used internally for resuming sound manager if
Phaser.Sound.BaseSoundManager#pauseOnBlur is set to true.
Access: protected
Source: src/sound/BaseSoundManager.js#L608
Since: 3.0.0
pauseAll ​
<instance> pauseAll() ​
Description:
Pauses all the sounds in the game.
Fires: Phaser.Sound.Events#event:PAUSE_ALL
Source: src/sound/BaseSoundManager.js#L448
Since: 3.0.0
play ​
<instance> play(key, [extra]) ​
Description:
Adds a new sound to the sound manager and plays it.
The sound will be automatically removed (destroyed) once playback ends.
This lets you play a new sound on the fly without the need to keep a reference to it.
Parameters:
name type optional description
key string No Asset key for the sound.
extra Phaser.Types.Sound.SoundConfig | Phaser.Types.Sound.SoundMarker Yes An optional additional object containing settings to be applied to the sound. It could be either config or marker object.
Returns: boolean - Whether the sound started playing successfully.
Source: src/sound/BaseSoundManager.js#L308
Since: 3.0.0
playAudioSprite ​
<instance> playAudioSprite(key, spriteName, [config]) ​
Description:
Adds a new audio sprite sound to the sound manager and plays it.
The sprite will be automatically removed (destroyed) once playback ends.
This lets you play a new sound on the fly without the need to keep a reference to it.
Parameters:
name type optional description
key string No Asset key for the sound.
spriteName string No The name of the sound sprite to play.
config Phaser.Types.Sound.SoundConfig Yes An optional config object containing default sound settings.
Returns: boolean - Whether the audio sprite sound started playing successfully.
Source: src/sound/BaseSoundManager.js#L349
Since: 3.0.0
remove ​
<instance> remove(sound) ​
Description:
Removes a sound from the sound manager.
The removed sound is destroyed before removal.
Parameters:
name type optional description
sound Phaser.Sound.BaseSound No The sound object to remove.
Returns: boolean - True if the sound was removed successfully, otherwise false.
Source: src/sound/BaseSoundManager.js#L373
Since: 3.0.0
removeAll ​
<instance> removeAll() ​
Description:
Removes all sounds from the manager, destroying the sounds.
Source: src/sound/BaseSoundManager.js#L400
Since: 3.23.0
removeByKey ​
<instance> removeByKey(key) ​
Description:
Removes all sounds from the sound manager that have an asset key matching the given value.
The removed sounds are destroyed before removal.
Parameters:
name type optional description
key string No The key to match when removing sound objects.
Returns: number - The number of matching sound objects that were removed.
Source: src/sound/BaseSoundManager.js#L416
Since: 3.0.0
resumeAll ​
<instance> resumeAll() ​
Description:
Resumes all the sounds in the game.
Fires: Phaser.Sound.Events#event:RESUME_ALL
Source: src/sound/BaseSoundManager.js#L465
Since: 3.0.0
setDetune ​
<instance> setDetune(value) ​
Description:
Sets the global detuning of all sounds in cents .
The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Parameters:
name type optional description
value number No The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Returns: Phaser.Sound.BaseSoundManager - This Sound Manager.
Fires: Phaser.Sound.Events#event:GLOBAL_DETUNE
Source: src/sound/BaseSoundManager.js#L786
Since: 3.3.0
setListenerPosition ​
<instance> setListenerPosition([x], [y]) ​
Description:
Sets the X and Y position of the Spatial Audio listener on this Web Audios context.
If you call this method with no parameters it will default to the center-point of
the game canvas. Depending on the type of game you're making, you may need to call
this method constantly to reset the listener position as the camera scrolls.
Calling this method does nothing on HTML5Audio.
Parameters:
name type optional description
x number Yes The x position of the Spatial Audio listener.
y number Yes The y position of the Spatial Audio listener.
Source: src/sound/BaseSoundManager.js#L482
Since: 3.60.0
setRate ​
<instance> setRate(value) ​
Description:
Sets the global playback rate at which all the sounds will be played.
For example, a value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed
and 2.0 doubles the audios playback speed.
Parameters:
name type optional description
value number No Global playback rate at which all the sounds will be played.
Returns: Phaser.Sound.BaseSoundManager - This Sound Manager.
Fires: Phaser.Sound.Events#event:GLOBAL_RATE
Source: src/sound/BaseSoundManager.js#L734
Since: 3.3.0
stopAll ​
<instance> stopAll() ​
Description:
Stops all the sounds in the game.
Fires: Phaser.Sound.Events#event:STOP_ALL
Source: src/sound/BaseSoundManager.js#L499
Since: 3.0.0
stopByKey ​
<instance> stopByKey(key) ​
Description:
Stops any sounds matching the given key.
Parameters:
name type optional description
key string No Sound asset key.
Returns: number - - How many sounds were stopped.
Source: src/sound/BaseSoundManager.js#L516
Since: 3.23.0
unlock ​
<instance> unlock() ​
Description:
Method used internally for unlocking audio playback on devices that
require user interaction before any sound can be played on a web page.
Read more about how this issue is handled here in this article .
Access: protected
Source: src/sound/BaseSoundManager.js#L584
Since: 3.0.0
update ​
<instance> update(time, delta) ​
Description:
Update method called on every game step.
Removes destroyed sounds and updates every active sound in the game.
Access: protected
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time elapsed since the last frame.
Fires: Phaser.Sound.Events#event:UNLOCKED
Source: src/sound/BaseSoundManager.js#L653
Since: 3.0.0
Previous
BaseSound
Next
HTML5AudioSound
Public Members
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
Inherited Methods
Public Methods
add
addAudioSprite
destroy
get
getAll
getAllPlaying
isPlaying
onBlur
onFocus
pauseAll
play
playAudioSprite
remove
removeAll
removeByKey
resumeAll
setDetune
setListenerPosition
setRate
stopAll
stopByKey
unlock
update
