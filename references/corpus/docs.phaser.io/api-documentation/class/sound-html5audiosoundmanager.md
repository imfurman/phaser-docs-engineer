# HTML5AudioSoundManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/sound-html5audiosoundmanager

Phaser API Documentation
Class
HTML5AudioSoundManager
Version: Phaser v3.90.0
On this page
HTML5AudioSoundManager
HTML5AudioSoundManager
Constructor
new HTML5AudioSoundManager(game)
Parameters
name type optional description
game Phaser.Game No Reference to the current game instance.
Scope : static
Extends
Phaser.Sound.BaseSoundManager
Source: src/sound/html5/HTML5AudioSoundManager.js#L37
Since: 3.0.0
Inherited Members ​
From Phaser.Sound.BaseSoundManager :
detune
game
gameLostFocus
jsonCache
listenerPosition
locked
pauseOnBlur
rate
Public Members ​
audioPlayDelay ​
audioPlayDelay: number ​
Description:
Value representing time difference, in seconds, between calling
play method on an audio tag and when it actually starts playing.
It is used to achieve more accurate delayed sound playback.
You might need to tweak this value to get the desired results
since audio play delay varies depending on the browser/platform.
Source: src/sound/html5/HTML5AudioSoundManager.js#L58
Since: 3.0.0
loopEndOffset ​
loopEndOffset: number ​
Description:
A value by which we should offset the loop end marker of the
looping sound to compensate for lag, caused by changing audio
tag playback position, in order to achieve gapless looping.
You might need to tweak this value to get the desired results
since loop lag varies depending on the browser/platform.
Source: src/sound/html5/HTML5AudioSoundManager.js#L73
Since: 3.0.0
mute ​
mute: boolean ​
Overrides: Phaser.Sound.BaseSoundManager#mute
Fires: Phaser.Sound.Events#event:GLOBAL_MUTE
Source: src/sound/html5/HTML5AudioSoundManager.js#L389
Since: 3.0.0
override ​
override: boolean ​
Description:
Flag indicating whether if there are no idle instances of HTML5 Audio tag,
for any particular sound, if one of the used tags should be hijacked and used
for succeeding playback or if succeeding Phaser.Sound.HTML5AudioSound#play
call should be ignored.
Source: src/sound/html5/HTML5AudioSoundManager.js#L45
Since: 3.0.0
volume ​
volume: number ​
Overrides: Phaser.Sound.BaseSoundManager#volume
Fires: Phaser.Sound.Events#event:GLOBAL_VOLUME
Source: src/sound/html5/HTML5AudioSoundManager.js#L434
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
addAudioSprite
get
getAll
getAllPlaying
isPlaying
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
update
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
Returns: Phaser.Sound.HTML5AudioSound - The new sound instance.
Source: src/sound/html5/HTML5AudioSoundManager.js#L142
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Calls Phaser.Sound.BaseSoundManager#destroy method
and cleans up all HTML5 Audio related stuff.
Overrides: Phaser.Sound.BaseSoundManager#destroy
Source: src/sound/html5/HTML5AudioSoundManager.js#L325
Since: 3.0.0
isLocked ​
<instance> isLocked(sound, prop, [value]) ​
Description:
Method used internally by Phaser.Sound.HTML5AudioSound class methods and property setters
to check if sound manager is locked and then either perform action immediately or queue it
to be performed once the sound manager gets unlocked.
Access: protected
Parameters:
name type optional description
sound Phaser.Sound.HTML5AudioSound No Sound object on which to perform queued action.
prop string No Name of the method to be called or property to be assigned a value to.
value * Yes An optional parameter that either holds an array of arguments to be passed to the method call or value to be set to the property.
Returns: boolean - Whether the sound manager is locked.
Source: src/sound/html5/HTML5AudioSoundManager.js#L340
Since: 3.0.0
onBlur ​
<instance> onBlur() ​
Description:
Method used internally for pausing sound manager if
Phaser.Sound.HTML5AudioSoundManager#pauseOnBlur is set to true.
Access: protected
Overrides: Phaser.Sound.BaseSoundManager#onBlur
Source: src/sound/html5/HTML5AudioSoundManager.js#L287
Since: 3.0.0
onFocus ​
<instance> onFocus() ​
Description:
Method used internally for resuming sound manager if
Phaser.Sound.HTML5AudioSoundManager#pauseOnBlur is set to true.
Access: protected
Overrides: Phaser.Sound.BaseSoundManager#onFocus
Source: src/sound/html5/HTML5AudioSoundManager.js#L307
Since: 3.0.0
setMute ​
<instance> setMute(value) ​
Description:
Sets the muted state of all this Sound Manager.
Parameters:
name type optional description
value boolean No true to mute all sounds, false to unmute them.
Returns: Phaser.Sound.HTML5AudioSoundManager - This Sound Manager.
Fires: Phaser.Sound.Events#event:GLOBAL_MUTE
Source: src/sound/html5/HTML5AudioSoundManager.js#L371
Since: 3.3.0
setVolume ​
<instance> setVolume(value) ​
Description:
Sets the volume of this Sound Manager.
Parameters:
name type optional description
value number No The global volume of this Sound Manager.
Returns: Phaser.Sound.HTML5AudioSoundManager - This Sound Manager.
Fires: Phaser.Sound.Events#event:GLOBAL_VOLUME
Source: src/sound/html5/HTML5AudioSoundManager.js#L416
Since: 3.3.0
unlock ​
<instance> unlock() ​
Description:
Unlocks HTML5 Audio loading and playback on mobile
devices on the initial explicit user interaction.
Overrides: Phaser.Sound.BaseSoundManager#unlock
Source: src/sound/html5/HTML5AudioSoundManager.js#L162
Since: 3.0.0
Previous
HTML5AudioSound
Next
NoAudioSound
Inherited Members
Public Members
audioPlayDelay
loopEndOffset
mute
override
volume
Inherited Methods
Public Methods
add
destroy
isLocked
onBlur
onFocus
setMute
setVolume
unlock
