# WebAudioSoundManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/sound-webaudiosoundmanager

Phaser API Documentation
Class
WebAudioSoundManager
Version: Phaser v3.90.0
On this page
WebAudioSoundManager
Web Audio API implementation of the Sound Manager.
Not all browsers can play all audio formats.
There is a good guide to what's supported: Cross-browser audio basics: Audio codec support .
Constructor
new WebAudioSoundManager(game)
Parameters
name type optional description
game Phaser.Game No Reference to the current game instance.
Scope : static
Extends
Phaser.Sound.BaseSoundManager
Source: src/sound/webaudio/WebAudioSoundManager.js#L16
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
context ​
context: AudioContext ​
Description:
The AudioContext being used for playback.
Source: src/sound/webaudio/WebAudioSoundManager.js#L40
Since: 3.0.0
destination ​
destination: AudioNode ​
Description:
Destination node for connecting individual sounds to.
Source: src/sound/webaudio/WebAudioSoundManager.js#L71
Since: 3.0.0
masterMuteNode ​
masterMuteNode: GainNode ​
Description:
Gain node responsible for controlling global muting.
Source: src/sound/webaudio/WebAudioSoundManager.js#L49
Since: 3.0.0
masterVolumeNode ​
masterVolumeNode: GainNode ​
Description:
Gain node responsible for controlling global volume.
Source: src/sound/webaudio/WebAudioSoundManager.js#L58
Since: 3.0.0
mute ​
mute: boolean ​
Overrides: Phaser.Sound.BaseSoundManager#mute
Fires: Phaser.Sound.Events#event:GLOBAL_MUTE
Source: src/sound/webaudio/WebAudioSoundManager.js#L528
Since: 3.0.0
volume ​
volume: number ​
Overrides: Phaser.Sound.BaseSoundManager#volume
Fires: Phaser.Sound.Events#event:GLOBAL_VOLUME
Source: src/sound/webaudio/WebAudioSoundManager.js#L568
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
setRate
stopAll
stopByKey
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
Returns: Phaser.Sound.WebAudioSound - The new sound instance.
Source: src/sound/webaudio/WebAudioSoundManager.js#L205
Since: 3.0.0
createAudioContext ​
<instance> createAudioContext(game) ​
Description:
Method responsible for instantiating and returning AudioContext instance.
If an instance of an AudioContext class was provided through the game config,
that instance will be returned instead. This can come in handy if you are reloading
a Phaser game on a page that never properly refreshes (such as in an SPA project)
and you want to reuse already instantiated AudioContext.
Parameters:
name type optional description
game Phaser.Game No Reference to the current game instance.
Returns: AudioContext - The AudioContext instance to be used for playback.
Source: src/sound/webaudio/WebAudioSoundManager.js#L126
Since: 3.0.0
decodeAudio ​
<instance> decodeAudio([audioKey], [audioData]) ​
Description:
Decode audio data into a format ready for playback via Web Audio.
The audio data can be a base64 encoded string, an audio media-type data uri, or an ArrayBuffer instance.
The audioKey is the key that will be used to save the decoded audio to the audio cache.
Instead of passing a single entry you can instead pass an array of Phaser.Types.Sound.DecodeAudioConfig
objects as the first and only argument.
Decoding is an async process, so be sure to listen for the events to know when decoding has completed.
Once the audio has decoded it can be added to the Sound Manager or played via its key.
Parameters:
name type optional description
audioKey Array.< Phaser.Types.Sound.DecodeAudioConfig > | string Yes The string-based key to be used to reference the decoded audio in the audio cache, or an array of audio config objects.
audioData ArrayBuffer | string Yes The audio data, either a base64 encoded string, an audio media-type data uri, or an ArrayBuffer instance.
Fires: Phaser.Sound.Events#event:DECODED , Phaser.Sound.Events#event:DECODED_ALL
Source: src/sound/webaudio/WebAudioSoundManager.js#L225
Since: 3.18.0
destroy ​
<instance> destroy() ​
Description:
Calls Phaser.Sound.BaseSoundManager#destroy method
and cleans up all Web Audio API related stuff.
Overrides: Phaser.Sound.BaseSoundManager#destroy
Source: src/sound/webaudio/WebAudioSoundManager.js#L476
Since: 3.0.0
onBlur ​
<instance> onBlur() ​
Description:
Method used internally for pausing sound manager if
Phaser.Sound.WebAudioSoundManager#pauseOnBlur is set to true.
Access: protected
Overrides: Phaser.Sound.BaseSoundManager#onBlur
Source: src/sound/webaudio/WebAudioSoundManager.js#L382
Since: 3.0.0
onFocus ​
<instance> onFocus() ​
Description:
Method used internally for resuming sound manager if
Phaser.Sound.WebAudioSoundManager#pauseOnBlur is set to true.
Access: protected
Overrides: Phaser.Sound.BaseSoundManager#onFocus
Source: src/sound/webaudio/WebAudioSoundManager.js#L398
Since: 3.0.0
setAudioContext ​
<instance> setAudioContext(context) ​
Description:
This method takes a new AudioContext reference and then sets
this Sound Manager to use that context for all playback.
As part of this call it also disconnects the master mute and volume
nodes and then re-creates them on the new given context.
Parameters:
name type optional description
context AudioContext No Reference to an already created AudioContext instance.
Returns: Phaser.Sound.WebAudioSoundManager - The WebAudioSoundManager instance.
Source: src/sound/webaudio/WebAudioSoundManager.js#L161
Since: 3.21.0
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
Overrides: Phaser.Sound.BaseSoundManager#setListenerPosition
Source: src/sound/webaudio/WebAudioSoundManager.js#L306
Since: 3.60.0
setMute ​
<instance> setMute(value) ​
Description:
Sets the muted state of all this Sound Manager.
Parameters:
name type optional description
value boolean No true to mute all sounds, false to unmute them.
Returns: Phaser.Sound.WebAudioSoundManager - This Sound Manager.
Fires: Phaser.Sound.Events#event:GLOBAL_MUTE
Source: src/sound/webaudio/WebAudioSoundManager.js#L510
Since: 3.3.0
setVolume ​
<instance> setVolume(value) ​
Description:
Sets the volume of this Sound Manager.
Parameters:
name type optional description
value number No The global volume of this Sound Manager.
Returns: Phaser.Sound.WebAudioSoundManager - This Sound Manager.
Fires: Phaser.Sound.Events#event:GLOBAL_VOLUME
Source: src/sound/webaudio/WebAudioSoundManager.js#L550
Since: 3.3.0
unlock ​
<instance> unlock() ​
Description:
Unlocks Web Audio API on the initial input event.
Read more about how this issue is handled here in this article .
Overrides: Phaser.Sound.BaseSoundManager#unlock
Source: src/sound/webaudio/WebAudioSoundManager.js#L331
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
Overrides: Phaser.Sound.BaseSoundManager#update
Fires: Phaser.Sound.Events#event:UNLOCKED
Source: src/sound/webaudio/WebAudioSoundManager.js#L416
Since: 3.0.0
Previous
WebAudioSound
Next
List
Inherited Members
Public Members
context
destination
masterMuteNode
masterVolumeNode
mute
volume
Inherited Methods
Public Methods
add
createAudioContext
decodeAudio
destroy
onBlur
onFocus
setAudioContext
setListenerPosition
setMute
setVolume
unlock
update
