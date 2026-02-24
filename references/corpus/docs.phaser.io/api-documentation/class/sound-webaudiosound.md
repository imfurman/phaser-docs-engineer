# WebAudioSound | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/sound-webaudiosound

Phaser API Documentation
Class
WebAudioSound
Version: Phaser v3.90.0
On this page
WebAudioSound
Web Audio API implementation of the sound.
Constructor
new WebAudioSound(manager, key, [config])
Parameters
name type optional default description
manager Phaser.Sound.WebAudioSoundManager No Reference to the WebAudio Sound Manager that owns this Sound instance.
key string No Asset key for the sound.
config Phaser.Types.Sound.SoundConfig Yes "{}" An optional config object containing default sound settings.
Scope : static
Extends
Phaser.Sound.BaseSound
Source: src/sound/webaudio/WebAudioSound.js#L13
Since: 3.0.0
Inherited Members ​
From Phaser.Sound.BaseSound :
currentMarker
duration
isPaused
isPlaying
key
manager
markers
pendingRemove
totalDuration
totalRate
Public Members ​
audioBuffer ​
audioBuffer: AudioBuffer ​
Description:
Audio buffer containing decoded data of the audio asset to be played.
Source: src/sound/webaudio/WebAudioSound.js#L37
Since: 3.0.0
detune ​
detune: number ​
Description:
The detune value of this Sound, given in cents .
The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Fires: Phaser.Sound.Events#event:DETUNE
Source: src/sound/webaudio/WebAudioSound.js#L828
Since: 3.0.0
hasEnded ​
hasEnded: boolean ​
Description:
Used for keeping track when sound source playback has ended
so its state can be updated accordingly.
Source: src/sound/webaudio/WebAudioSound.js#L174
Since: 3.0.0
hasLooped ​
hasLooped: boolean ​
Description:
Used for keeping track when sound source has looped
so its state can be updated accordingly.
Source: src/sound/webaudio/WebAudioSound.js#L186
Since: 3.0.0
loop ​
loop: boolean ​
Description:
Flag indicating whether or not the sound or current sound marker will loop.
Fires: Phaser.Sound.Events#event:LOOP
Source: src/sound/webaudio/WebAudioSound.js#L1039
Since: 3.0.0
loopSource ​
loopSource: AudioBufferSourceNode ​
Description:
A reference to a second audio source used for gapless looped playback.
Source: src/sound/webaudio/WebAudioSound.js#L62
Since: 3.0.0
loopTime ​
loopTime: number ​
Description:
The time at which the sound loop source should actually start playback.
Based on BaseAudioContext.currentTime value.
Source: src/sound/webaudio/WebAudioSound.js#L148
Since: 3.0.0
mute ​
mute: boolean ​
Description:
Boolean indicating whether the sound is muted or not.
Gets or sets the muted state of this sound.
Fires: Phaser.Sound.Events#event:MUTE
Source: src/sound/webaudio/WebAudioSound.js#L875
Since: 3.0.0
muteNode ​
muteNode: GainNode ​
Description:
Gain node responsible for controlling this sound's muting.
Source: src/sound/webaudio/WebAudioSound.js#L72
Since: 3.0.0
pan ​
pan: number ​
Description:
Gets or sets the pan of this sound, a value between -1 (full left pan) and 1 (full right pan).
Always returns zero on iOS / Safari as it doesn't support the stereo panner node.
Fires: Phaser.Sound.Events#event:PAN
Source: src/sound/webaudio/WebAudioSound.js#L1091
Since: 3.50.0
pannerNode ​
pannerNode: StereoPannerNode ​
Description:
Panner node responsible for controlling this sound's pan.
Doesn't work on iOS / Safari.
Source: src/sound/webaudio/WebAudioSound.js#L90
Since: 3.50.0
playTime ​
playTime: number ​
Description:
The time at which the sound should have started playback from the beginning.
Treat this property as read-only.
Based on BaseAudioContext.currentTime value.
Source: src/sound/webaudio/WebAudioSound.js#L120
Since: 3.0.0
rate ​
rate: number ​
Description:
Rate at which this Sound will be played.
Value of 1.0 plays the audio at full speed, 0.5 plays the audio at half speed
and 2.0 doubles the audios playback speed.
Fires: Phaser.Sound.Events#event:RATE
Source: src/sound/webaudio/WebAudioSound.js#L778
Since: 3.0.0
rateUpdates ​
rateUpdates: array ​
Description:
An array where we keep track of all rate updates during playback.
Treat this property as read-only.
Array of object types: { time: number, rate: number }
Source: src/sound/webaudio/WebAudioSound.js#L160
Since: 3.0.0
seek ​
seek: number ​
Description:
Property representing the position of playback for this sound, in seconds.
Setting it to a specific value moves current playback to that position.
The value given is clamped to the range 0 to current marker duration.
Setting seek of a stopped sound has no effect.
Fires: Phaser.Sound.Events#event:SEEK
Source: src/sound/webaudio/WebAudioSound.js#L963
Since: 3.0.0
source ​
source: AudioBufferSourceNode ​
Description:
A reference to an audio source node used for playing back audio from
audio data stored in Phaser.Sound.WebAudioSound#audioBuffer.
Source: src/sound/webaudio/WebAudioSound.js#L51
Since: 3.0.0
spatialNode ​
spatialNode: PannerNode ​
Description:
The Stereo Spatial Panner node.
Source: src/sound/webaudio/WebAudioSound.js#L101
Since: 3.60.0
spatialSource ​
spatialSource: Phaser.Types.Math.Vector2Like ​
Description:
If the Spatial Panner node has been set to track a vector or
Game Object, this retains a reference to it.
Source: src/sound/webaudio/WebAudioSound.js#L110
Since: 3.60.0
startTime ​
startTime: number ​
Description:
The time at which the sound source should have actually started playback.
Treat this property as read-only.
Based on BaseAudioContext.currentTime value.
Source: src/sound/webaudio/WebAudioSound.js#L134
Since: 3.0.0
volume ​
volume: number ​
Description:
Gets or sets the volume of this sound, a value between 0 (silence) and 1 (full volume).
Fires: Phaser.Sound.Events#event:VOLUME
Source: src/sound/webaudio/WebAudioSound.js#L920
Since: 3.0.0
volumeNode ​
volumeNode: GainNode ​
Description:
Gain node responsible for controlling this sound's volume.
Source: src/sound/webaudio/WebAudioSound.js#L81
Since: 3.0.0
x ​
x: number ​
Description:
Sets the x position of this Sound in Spatial Audio space.
This only has any effect if the sound was created with a SpatialSoundConfig object.
Also see the WebAudioSoundManager.setListenerPosition method.
If you find that the sound becomes too quiet, too quickly, as it moves away from
the listener, then try different refDistance property values when configuring
the spatial sound.
Source: src/sound/webaudio/WebAudioSound.js#L528
Since: 3.60.0
y ​
y: number ​
Description:
Sets the y position of this Sound in Spatial Audio space.
This only has any effect if the sound was created with a SpatialSoundConfig object.
Also see the WebAudioSoundManager.setListenerPosition method.
If you find that the sound becomes too quiet, too quickly, as it moves away from
the listener, then try different refDistance property values when configuring
the spatial sound.
Source: src/sound/webaudio/WebAudioSound.js#L566
Since: 3.60.0
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
From Phaser.Sound.BaseSound :
addMarker
removeMarker
resetConfig
updateMarker
Public Methods ​
applyConfig ​
<instance> applyConfig() ​
Description:
Method used internally for applying config values to some of the sound properties.
Overrides: Phaser.Sound.BaseSound#applyConfig
Source: src/sound/webaudio/WebAudioSound.js#L482
Since: 3.0.0
calculateRate ​
<instance> calculateRate() ​
Description:
Method used internally to calculate total playback rate of the sound.
Overrides: Phaser.Sound.BaseSound#calculateRate
Source: src/sound/webaudio/WebAudioSound.js#L696
Since: 3.0.0
createAndStartLoopBufferSource ​
<instance> createAndStartLoopBufferSource() ​
Description:
This method is only used internally and it creates a looping buffer source.
Source: src/sound/webaudio/WebAudioSound.js#L381
Since: 3.0.0
createBufferSource ​
<instance> createBufferSource() ​
Description:
This method is only used internally and it creates a buffer source.
Returns: AudioBufferSourceNode - undefined
Source: src/sound/webaudio/WebAudioSound.js#L399
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Calls Phaser.Sound.BaseSound#destroy method
and cleans up all Web Audio API related stuff.
Overrides: Phaser.Sound.BaseSound#destroy
Source: src/sound/webaudio/WebAudioSound.js#L656
Since: 3.0.0
getCurrentTime ​
<instance> getCurrentTime() ​
Description:
Method used internally for calculating current playback time of a playing sound.
Source: src/sound/webaudio/WebAudioSound.js#L728
Since: 3.0.0
getLoopTime ​
<instance> getLoopTime() ​
Description:
Method used internally for calculating the time
at witch the loop source should start playing.
Source: src/sound/webaudio/WebAudioSound.js#L757
Since: 3.0.0
pause ​
<instance> pause() ​
Description:
Pauses the sound.
Overrides: Phaser.Sound.BaseSound#pause
Returns: boolean - Whether the sound was paused successfully.
Fires: Phaser.Sound.Events#event:PAUSE
Source: src/sound/webaudio/WebAudioSound.js#L272
Since: 3.0.0
play ​
<instance> play([markerName], [config]) ​
Description:
Play this sound, or a marked section of it.
It always plays the sound from the start. If you want to start playback from a specific time
you can set 'seek' setting of the config object, provided to this call, to that value.
If you want to play the same sound simultaneously, then you need to create another instance
of it and play that Sound.
Parameters:
name type optional default description
markerName string | Phaser.Types.Sound.SoundConfig Yes "''" If you want to play a marker then provide the marker name here. Alternatively, this parameter can be a SoundConfig object.
config Phaser.Types.Sound.SoundConfig Yes Optional sound config object to be applied to this marker or entire sound if no marker name is provided. It gets memorized for future plays of current section of the sound.
Overrides: Phaser.Sound.BaseSound#play
Returns: boolean - Whether the sound started playing successfully.
Fires: Phaser.Sound.Events#event:PLAY
Source: src/sound/webaudio/WebAudioSound.js#L238
Since: 3.0.0
resume ​
<instance> resume() ​
Description:
Resumes the sound.
Overrides: Phaser.Sound.BaseSound#resume
Returns: boolean - Whether the sound was resumed successfully.
Fires: Phaser.Sound.Events#event:RESUME
Source: src/sound/webaudio/WebAudioSound.js#L302
Since: 3.0.0
setDetune ​
<instance> setDetune(value) ​
Description:
Sets the detune value of this Sound, given in cents .
The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Parameters:
name type optional description
value number No The range of the value is -1200 to 1200, but we recommend setting it to 50 .
Returns: Phaser.Sound.WebAudioSound - This Sound instance.
Fires: Phaser.Sound.Events#event:DETUNE
Source: src/sound/webaudio/WebAudioSound.js#L856
Since: 3.3.0
setLoop ​
<instance> setLoop(value) ​
Description:
Sets the loop state of this Sound.
Parameters:
name type optional description
value boolean No true to loop this sound, false to not loop it.
Returns: Phaser.Sound.WebAudioSound - This Sound instance.
Fires: Phaser.Sound.Events#event:LOOP
Source: src/sound/webaudio/WebAudioSound.js#L1073
Since: 3.4.0
setMute ​
<instance> setMute(value) ​
Description:
Sets the muted state of this Sound.
Parameters:
name type optional description
value boolean No true to mute this sound, false to unmute it.
Returns: Phaser.Sound.WebAudioSound - This Sound instance.
Fires: Phaser.Sound.Events#event:MUTE
Source: src/sound/webaudio/WebAudioSound.js#L902
Since: 3.4.0
setPan ​
<instance> setPan(value) ​
Description:
Sets the pan of this sound, a value between -1 (full left pan) and 1 (full right pan).
Note: iOS / Safari doesn't support the stereo panner node.
Parameters:
name type optional description
value number No The pan of the sound. A value between -1 (full left pan) and 1 (full right pan).
Returns: Phaser.Sound.WebAudioSound - This Sound instance.
Fires: Phaser.Sound.Events#event:PAN
Source: src/sound/webaudio/WebAudioSound.js#L1129
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
Returns: Phaser.Sound.WebAudioSound - This Sound instance.
Fires: Phaser.Sound.Events#event:RATE
Source: src/sound/webaudio/WebAudioSound.js#L807
Since: 3.3.0
setSeek ​
<instance> setSeek(value) ​
Description:
Seeks to a specific point in this sound.
Parameters:
name type optional description
value number No The point in the sound to seek to.
Returns: Phaser.Sound.WebAudioSound - This Sound instance.
Fires: Phaser.Sound.Events#event:SEEK
Source: src/sound/webaudio/WebAudioSound.js#L1021
Since: 3.4.0
setVolume ​
<instance> setVolume(value) ​
Description:
Sets the volume of this Sound.
Parameters:
name type optional description
value number No The volume of the sound.
Returns: Phaser.Sound.WebAudioSound - This Sound instance.
Fires: Phaser.Sound.Events#event:VOLUME
Source: src/sound/webaudio/WebAudioSound.js#L945
Since: 3.4.0
stop ​
<instance> stop() ​
Description:
Stop playing this sound.
Overrides: Phaser.Sound.BaseSound#stop
Returns: boolean - Whether the sound was stopped successfully.
Fires: Phaser.Sound.Events#event:STOP
Source: src/sound/webaudio/WebAudioSound.js#L331
Since: 3.0.0
stopAndRemoveBufferSource ​
<instance> stopAndRemoveBufferSource() ​
Description:
This method is only used internally and it stops and removes a buffer source.
Source: src/sound/webaudio/WebAudioSound.js#L439
Since: 3.0.0
stopAndRemoveLoopBufferSource ​
<instance> stopAndRemoveLoopBufferSource() ​
Description:
This method is only used internally and it stops and removes a looping buffer source.
Source: src/sound/webaudio/WebAudioSound.js#L464
Since: 3.0.0
update ​
<instance> update() ​
Description:
Update method called automatically by sound manager on every game step.
Overrides: Phaser.Sound.BaseSound#update
Fires: Phaser.Sound.Events#event:COMPLETE , Phaser.Sound.Events#event:LOOPED
Source: src/sound/webaudio/WebAudioSound.js#L604
Since: 3.0.0
Previous
NoAudioSoundManager
Next
WebAudioSoundManager
Inherited Members
Public Members
audioBuffer
detune
hasEnded
hasLooped
loop
loopSource
loopTime
mute
muteNode
pan
pannerNode
playTime
rate
rateUpdates
seek
source
spatialNode
spatialSource
startTime
volume
volumeNode
x
y
Inherited Methods
Public Methods
applyConfig
calculateRate
createAndStartLoopBufferSource
createBufferSource
destroy
getCurrentTime
getLoopTime
pause
play
resume
setDetune
setLoop
setMute
setPan
setRate
setSeek
setVolume
stop
stopAndRemoveBufferSource
stopAndRemoveLoopBufferSource
update
