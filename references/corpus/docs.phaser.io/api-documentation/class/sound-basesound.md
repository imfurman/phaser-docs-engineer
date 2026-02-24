# BaseSound | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/sound-basesound

Phaser API Documentation
Class
BaseSound
Version: Phaser v3.90.0
On this page
BaseSound
Class containing all the shared state and behavior of a sound object, independent of the implementation.
Constructor
new BaseSound(manager, key, [config])
Parameters
name type optional description
manager Phaser.Sound.BaseSoundManager No Reference to the current sound manager instance.
key string No Asset key for the sound.
config Phaser.Types.Sound.SoundConfig Yes An optional config object containing default sound settings.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/sound/BaseSound.js#L14
Since: 3.0.0
Public Members ​
currentMarker ​
currentMarker: Phaser.Types.Sound.SoundMarker ​
Description:
Currently playing marker.
'null' if whole sound is playing.
Source: src/sound/BaseSound.js#L159
Since: 3.0.0
duration ​
duration: number ​
Description:
A value representing the duration, in seconds.
It could be total sound duration or a marker duration.
Source: src/sound/BaseSound.js#L92
Since: 3.0.0
isPaused ​
isPaused: boolean ​
Description:
Flag indicating if sound is currently paused.
Source: src/sound/BaseSound.js#L68
Since: 3.0.0
isPlaying ​
isPlaying: boolean ​
Description:
Flag indicating if sound is currently playing.
Source: src/sound/BaseSound.js#L57
Since: 3.0.0
key ​
key: string ​
Description:
Asset key for the sound.
Source: src/sound/BaseSound.js#L47
Since: 3.0.0
manager ​
manager: Phaser.Sound.BaseSoundManager ​
Description:
Local reference to the sound manager.
Source: src/sound/BaseSound.js#L38
Since: 3.0.0
markers ​
markers: Object.<string, Phaser.Types.Sound.SoundMarker > ​
Description:
Object containing markers definitions.
Source: src/sound/BaseSound.js#L148
Since: 3.0.0
pendingRemove ​
pendingRemove: boolean ​
Description:
Flag indicating if destroy method was called on this sound.
Source: src/sound/BaseSound.js#L171
Since: 3.0.0
totalDuration ​
totalDuration: number ​
Description:
The total duration of the sound in seconds.
Source: src/sound/BaseSound.js#L103
Since: 3.0.0
totalRate ​
totalRate: number ​
Description:
A property that holds the value of sound's actual playback rate,
after its rate and detune values has been combined with global
rate and detune values.
Source: src/sound/BaseSound.js#L79
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
Description:
Adds a marker into the current sound. A marker is represented by name, start time, duration, and optionally config object.
This allows you to bundle multiple sounds together into a single audio file and use markers to jump between them for playback.
Parameters:
name type optional description
marker Phaser.Types.Sound.SoundMarker No Marker object.
Returns: boolean - Whether the marker was added successfully.
Source: src/sound/BaseSound.js#L182
Since: 3.0.0
applyConfig ​
<instance> applyConfig() ​
Description:
Method used internally for applying config values to some of the sound properties.
Source: src/sound/BaseSound.js#L412
Since: 3.0.0
calculateRate ​
<instance> calculateRate() ​
Description:
Method used internally to calculate total playback rate of the sound.
Source: src/sound/BaseSound.js#L451
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys this sound and all associated events and marks it for removal from the sound manager.
Overrides: Phaser.Events.EventEmitter#destroy
Fires: Phaser.Sound.Events#event:DESTROY
Source: src/sound/BaseSound.js#L466
Since: 3.0.0
pause ​
<instance> pause() ​
Description:
Pauses the sound. This only works if the sound is currently playing.
You can inspect the isPlaying and isPaused properties to check the state.
Returns: boolean - Whether the sound was paused successfully.
Source: src/sound/BaseSound.js#L343
Since: 3.0.0
play ​
<instance> play([markerName], [config]) ​
Description:
Play this sound, or a marked section of it.
It always plays the sound from the start. If you want to start playback from a specific time
you can set 'seek' setting of the config object, provided to this call, to that value.
Parameters:
name type optional default description
markerName string | Phaser.Types.Sound.SoundConfig Yes "''" If you want to play a marker then provide the marker name here. Alternatively, this parameter can be a SoundConfig object.
config Phaser.Types.Sound.SoundConfig Yes Optional sound config object to be applied to this marker or entire sound if no marker name is provided. It gets memorized for future plays of current section of the sound.
Returns: boolean - Whether the sound started playing successfully.
Source: src/sound/BaseSound.js#L283
Since: 3.0.0
removeMarker ​
<instance> removeMarker(markerName) ​
Description:
Removes a marker from the sound.
Parameters:
name type optional description
markerName string No The name of the marker to remove.
Returns: Phaser.Types.Sound.SoundMarker - Removed marker object or 'null' if there was no marker with provided name.
Source: src/sound/BaseSound.js#L259
Since: 3.0.0
resetConfig ​
<instance> resetConfig() ​
Description:
Method used internally for resetting values of some of the config properties.
Source: src/sound/BaseSound.js#L428
Since: 3.0.0
resume ​
<instance> resume() ​
Description:
Resumes the sound. This only works if the sound is paused and not already playing.
You can inspect the isPlaying and isPaused properties to check the state.
Returns: boolean - Whether the sound was resumed successfully.
Source: src/sound/BaseSound.js#L366
Since: 3.0.0
stop ​
<instance> stop() ​
Description:
Stop playing this sound.
Returns: boolean - Whether the sound was stopped successfully.
Source: src/sound/BaseSound.js#L389
Since: 3.0.0
update ​
<instance> update(time, delta) ​
Description:
Update method called automatically by sound manager on every game step.
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time elapsed since the last frame.
Source: src/sound/BaseSound.js#L440
Since: 3.0.0
updateMarker ​
<instance> updateMarker(marker) ​
Description:
Updates previously added marker.
Parameters:
name type optional description
marker Phaser.Types.Sound.SoundMarker No Marker object with updated values.
Returns: boolean - Whether the marker was updated successfully.
Source: src/sound/BaseSound.js#L229
Since: 3.0.0
Previous
Systems
Next
BaseSoundManager
Public Members
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
stop
update
updateMarker
