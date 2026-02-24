# NoAudioSound | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/sound-noaudiosound

Phaser API Documentation
Class
NoAudioSound
Version: Phaser v3.90.0
On this page
NoAudioSound
No audio implementation of the sound. It is used if audio has been
disabled in the game config or the device doesn't support any audio.
It represents a graceful degradation of sound logic that provides
minimal functionality and prevents Phaser projects that use audio from
breaking on devices that don't support any audio playback technologies.
Constructor
new NoAudioSound(manager, key, [config])
Parameters
name type optional default description
manager Phaser.Sound.NoAudioSoundManager No Reference to the current sound manager instance.
key string No Asset key for the sound.
config Phaser.Types.Sound.SoundConfig Yes "{}" An optional config object containing default sound settings.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/sound/noaudio/NoAudioSound.js#L29
Since: 3.0.0
Public Members ​
config ​
config: Phaser.Types.Sound.SoundConfig ​
Description:
A config object used to store default sound settings' values.
Default values will be set by properties' setters.
Source: src/sound/noaudio/NoAudioSound.js#L135
Since: 3.0.0
currentConfig ​
currentConfig: Phaser.Types.Sound.SoundConfig ​
Description:
Reference to the currently used config.
It could be default config or marker config.
Source: src/sound/noaudio/NoAudioSound.js#L154
Since: 3.0.0
currentMarker ​
currentMarker: Phaser.Types.Sound.SoundMarker ​
Description:
Currently playing marker.
'null' if whole sound is playing.
Source: src/sound/noaudio/NoAudioSound.js#L260
Since: 3.0.0
detune ​
detune: number ​
Description:
The detune value of this Sound, given in cents .
The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Fires: Phaser.Sound.Events#event:DETUNE
Source: src/sound/noaudio/NoAudioSound.js#L200
Since: 3.0.0
duration ​
duration: number ​
Description:
A value representing the duration, in seconds.
It could be total sound duration or a marker duration.
Source: src/sound/noaudio/NoAudioSound.js#L114
Since: 3.0.0
isPaused ​
isPaused: boolean ​
Description:
Flag indicating if sound is currently paused.
Source: src/sound/noaudio/NoAudioSound.js#L90
Since: 3.0.0
isPlaying ​
isPlaying: boolean ​
Description:
Flag indicating if sound is currently playing.
Source: src/sound/noaudio/NoAudioSound.js#L79
Since: 3.0.0
key ​
key: string ​
Description:
Asset key for the sound.
Source: src/sound/noaudio/NoAudioSound.js#L69
Since: 3.0.0
loop ​
loop: boolean ​
Description:
Flag indicating whether or not the sound or current sound marker will loop.
Fires: Phaser.Sound.Events#event:LOOP
Source: src/sound/noaudio/NoAudioSound.js#L225
Since: 3.0.0
manager ​
manager: Phaser.Sound.BaseSoundManager ​
Description:
Local reference to the sound manager.
Source: src/sound/noaudio/NoAudioSound.js#L60
Since: 3.0.0
markers ​
markers: Object.<string, Phaser.Types.Sound.SoundMarker > ​
Description:
Object containing markers definitions.
Source: src/sound/noaudio/NoAudioSound.js#L249
Since: 3.0.0
mute ​
mute: boolean ​
Description:
Boolean indicating whether the sound is muted or not.
Gets or sets the muted state of this sound.
Fires: Phaser.Sound.Events#event:MUTE
Source: src/sound/noaudio/NoAudioSound.js#L164
Since: 3.0.0
pan ​
pan: number ​
Description:
Gets or sets the pan of this sound, a value between -1 (full left pan) and 1 (full right pan).
Always returns zero on iOS / Safari as it doesn't support the stereo panner node.
Fires: Phaser.Sound.Events#event:PAN
Source: src/sound/noaudio/NoAudioSound.js#L236
Since: 3.50.0
pendingRemove ​
pendingRemove: boolean ​
Description:
Flag indicating if destroy method was called on this sound.
Source: src/sound/noaudio/NoAudioSound.js#L272
Since: 3.0.0
rate ​
rate: number ​
Description:
Rate at which this Sound will be played.
Value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed
and 2.0 doubles the audios playback speed.
Fires: Phaser.Sound.Events#event:RATE
Source: src/sound/noaudio/NoAudioSound.js#L187
Since: 3.0.0
seek ​
seek: number ​
Description:
Property representing the position of playback for this sound, in seconds.
Setting it to a specific value moves current playback to that position.
The value given is clamped to the range 0 to current marker duration.
Setting seek of a stopped sound has no effect.
Fires: Phaser.Sound.Events#event:SEEK
Source: src/sound/noaudio/NoAudioSound.js#L212
Since: 3.0.0
totalDuration ​
totalDuration: number ​
Description:
The total duration of the sound in seconds.
Source: src/sound/noaudio/NoAudioSound.js#L125
Since: 3.0.0
totalRate ​
totalRate: number ​
Description:
A property that holds the value of sound's actual playback rate,
after its rate and detune values has been combined with global
rate and detune values.
Source: src/sound/noaudio/NoAudioSound.js#L101
Since: 3.0.0
volume ​
volume: number ​
Description:
Gets or sets the volume of this sound, a value between 0 (silence) and 1 (full volume).
Fires: Phaser.Sound.Events#event:VOLUME
Source: src/sound/noaudio/NoAudioSound.js#L176
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
addMarker ​
<instance> addMarker(marker) ​
Parameters:
name type optional description
marker Phaser.Types.Sound.SoundMarker No Marker object.
Returns: boolean - false
Source: src/sound/noaudio/NoAudioSound.js#L283
Since: 3.0.0
applyConfig ​
<instance> applyConfig() ​
Description:
Method used internally for applying config values to some of the sound properties.
Source: src/sound/noaudio/NoAudioSound.js#L442
Since: 3.0.0
calculateRate ​
<instance> calculateRate() ​
Description:
Method used internally to calculate total playback rate of the sound.
Source: src/sound/noaudio/NoAudioSound.js#L470
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys this sound and all associated events and marks it for removal from the sound manager.
Overrides: Phaser.Events.EventEmitter#destroy
Fires: Phaser.Sound.Events#event:DESTROY
Source: src/sound/noaudio/NoAudioSound.js#L478
Since: 3.0.0
pause ​
<instance> pause() ​
Returns: boolean - false
Source: src/sound/noaudio/NoAudioSound.js#L324
Since: 3.0.0
play ​
<instance> play([markerName], [config]) ​
Parameters:
name type optional default description
markerName string | Phaser.Types.Sound.SoundConfig Yes "''" If you want to play a marker then provide the marker name here. Alternatively, this parameter can be a SoundConfig object.
config Phaser.Types.Sound.SoundConfig Yes Optional sound config object to be applied to this marker or entire sound if no marker name is provided. It gets memorized for future plays of current section of the sound.
Returns: boolean - false
Source: src/sound/noaudio/NoAudioSound.js#L313
Since: 3.0.0
removeMarker ​
<instance> removeMarker(markerName) ​
Parameters:
name type optional description
markerName string No The name of the marker to remove.
Returns: null - null
Source: src/sound/noaudio/NoAudioSound.js#L303
Since: 3.0.0
resetConfig ​
<instance> resetConfig() ​
Description:
Method used internally for resetting values of some of the config properties.
Source: src/sound/noaudio/NoAudioSound.js#L450
Since: 3.0.0
resume ​
<instance> resume() ​
Description:
Resumes the sound.
Returns: boolean - false
Source: src/sound/noaudio/NoAudioSound.js#L332
Since: 3.0.0
setDetune ​
<instance> setDetune(value) ​
Description:
Sets the detune value of this Sound, given in cents .
The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Parameters:
name type optional description
value number No The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Returns: Phaser.Sound.NoAudioSound - This Sound instance.
Source: src/sound/noaudio/NoAudioSound.js#L391
Since: 3.3.0
setLoop ​
<instance> setLoop(value) ​
Description:
Sets the loop state of this Sound.
Parameters:
name type optional description
value boolean No true to loop this sound, false to not loop it.
Returns: Phaser.Sound.NoAudioSound - This Sound instance.
Source: src/sound/noaudio/NoAudioSound.js#L416
Since: 3.4.0
setMute ​
<instance> setMute(value) ​
Description:
Sets the muted state of this Sound.
Parameters:
name type optional description
value boolean No true to mute this sound, false to unmute it.
Returns: Phaser.Sound.NoAudioSound - This Sound instance.
Source: src/sound/noaudio/NoAudioSound.js#L352
Since: 3.4.0
setPan ​
<instance> setPan(value) ​
Description:
Sets the pan of this sound, a value between -1 (full left pan) and 1 (full right pan).
Note: iOS / Safari doesn't support the stereo panner node.
Parameters:
name type optional description
value number No The pan of the sound. A value between -1 (full left pan) and 1 (full right pan).
Returns: Phaser.Sound.NoAudioSound - This Sound instance.
Source: src/sound/noaudio/NoAudioSound.js#L428
Since: 3.50.0
setRate ​
<instance> setRate(value) ​
Description:
Sets the playback rate of this Sound.
For example, a value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed
and 2.0 doubles the audios playback speed.
Parameters:
name type optional description
value number No The playback rate at of this Sound.
Returns: Phaser.Sound.NoAudioSound - This Sound instance.
Source: src/sound/noaudio/NoAudioSound.js#L376
Since: 3.3.0
setSeek ​
<instance> setSeek(value) ​
Description:
Seeks to a specific point in this sound.
Parameters:
name type optional description
value number No The point in the sound to seek to.
Returns: Phaser.Sound.NoAudioSound - This Sound instance.
Source: src/sound/noaudio/NoAudioSound.js#L404
Since: 3.4.0
setVolume ​
<instance> setVolume(value) ​
Description:
Sets the volume of this Sound.
Parameters:
name type optional description
value number No The volume of the sound.
Returns: Phaser.Sound.NoAudioSound - This Sound instance.
Source: src/sound/noaudio/NoAudioSound.js#L364
Since: 3.4.0
stop ​
<instance> stop() ​
Description:
Stop playing this sound.
Returns: boolean - false
Source: src/sound/noaudio/NoAudioSound.js#L342
Since: 3.0.0
update ​
<instance> update(time, delta) ​
Description:
Update method called automatically by sound manager on every game step.
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time elapsed since the last frame.
Source: src/sound/noaudio/NoAudioSound.js#L458
Since: 3.0.0
updateMarker ​
<instance> updateMarker(marker) ​
Parameters:
name type optional description
marker Phaser.Types.Sound.SoundMarker No Marker object with updated values.
Returns: boolean - false
Source: src/sound/noaudio/NoAudioSound.js#L293
Since: 3.0.0
Previous
HTML5AudioSoundManager
Next
NoAudioSoundManager
Public Members
config
currentConfig
currentMarker
detune
duration
isPaused
isPlaying
key
loop
manager
markers
mute
pan
pendingRemove
rate
seek
totalDuration
totalRate
volume
Inherited Methods
Public Methods
addMarker
applyConfig
calculateRate
destroy
pause
play
removeMarker
resetConfig
resume
setDetune
setLoop
setMute
setPan
setRate
setSeek
setVolume
stop
update
updateMarker
