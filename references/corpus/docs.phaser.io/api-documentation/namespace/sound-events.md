# Phaser.Sound.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/sound-events

Phaser API Documentation
Namespaces
Phaser.Sound.Events
Version: Phaser v3.90.0
On this page
Phaser.Sound.Events
Scope: static
Source: src/sound/events/index.js#L7
Static functions ​
COMPLETE ​
COMPLETE ​
Description:
The Sound Complete Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they complete playback.
Listen to it from a Sound instance using Sound.on('complete', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'complete' , listener ) ;
music . play ( ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
Source: src/sound/events/COMPLETE_EVENT.js#L7
Since: 3.16.1
DECODED ​
DECODED ​
Description:
The Audio Data Decoded Event.
This event is dispatched by the Web Audio Sound Manager as a result of calling the decodeAudio method.
Listen to it from the Sound Manager in a Scene using this.sound.on('decoded', listener) , i.e.:
this . sound . on ( 'decoded' , handler ) ;
this . sound . decodeAudio ( key , audioData ) ;
Parameters:
name type optional description
key string No The key of the audio file that was decoded and added to the audio cache.
Source: src/sound/events/DECODED_EVENT.js#L7
Since: 3.18.0
DECODED_ALL ​
DECODED_ALL ​
Description:
The Audio Data Decoded All Event.
This event is dispatched by the Web Audio Sound Manager as a result of calling the decodeAudio method,
once all files passed to the method have been decoded (or errored).
Use Phaser.Sound.Events#DECODED to listen for single sounds being decoded, and DECODED_ALL to
listen for them all completing.
Listen to it from the Sound Manager in a Scene using this.sound.on('decodedall', listener) , i.e.:
this . sound . once ( 'decodedall' , handler ) ;
this . sound . decodeAudio ( [ audioFiles ] ) ;
Source: src/sound/events/DECODED_ALL_EVENT.js#L7
Since: 3.18.0
DESTROY ​
DESTROY ​
Description:
The Sound Destroy Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are destroyed, either
directly or via a Sound Manager.
Listen to it from a Sound instance using Sound.on('destroy', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'destroy' , listener ) ;
music . destroy ( ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
Source: src/sound/events/DESTROY_EVENT.js#L7
Since: 3.0.0
DETUNE ​
DETUNE ​
Description:
The Sound Detune Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their detune value changes.
Listen to it from a Sound instance using Sound.on('detune', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'detune' , listener ) ;
music . play ( ) ;
music . setDetune ( 200 ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
detune number No The new detune value of the Sound.
Source: src/sound/events/DETUNE_EVENT.js#L7
Since: 3.0.0
GLOBAL_DETUNE ​
GLOBAL_DETUNE ​
Description:
The Sound Manager Global Detune Event.
This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,
or the HTML5 Audio Manager. It is dispatched when the detune property of the Sound Manager is changed, which globally
adjusts the detuning of all active sounds.
Listen to it from a Scene using: this.sound.on('rate', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.BaseSoundManager No A reference to the sound manager that emitted the event.
detune number No The updated detune value.
Source: src/sound/events/GLOBAL_DETUNE_EVENT.js#L7
Since: 3.0.0
GLOBAL_MUTE ​
GLOBAL_MUTE ​
Description:
The Sound Manager Global Mute Event.
This event is dispatched by the Sound Manager when its mute property is changed, either directly
or via the setMute method. This changes the mute state of all active sounds.
Listen to it from a Scene using: this.sound.on('mute', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.WebAudioSoundManager | Phaser.Sound.HTML5AudioSoundManager No A reference to the Sound Manager that emitted the event.
mute boolean No The mute value. true if the Sound Manager is now muted, otherwise false .
Source: src/sound/events/GLOBAL_MUTE_EVENT.js#L7
Since: 3.0.0
GLOBAL_RATE ​
GLOBAL_RATE ​
Description:
The Sound Manager Global Rate Event.
This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,
or the HTML5 Audio Manager. It is dispatched when the rate property of the Sound Manager is changed, which globally
adjusts the playback rate of all active sounds.
Listen to it from a Scene using: this.sound.on('rate', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.BaseSoundManager No A reference to the sound manager that emitted the event.
rate number No The updated rate value.
Source: src/sound/events/GLOBAL_RATE_EVENT.js#L7
Since: 3.0.0
GLOBAL_VOLUME ​
GLOBAL_VOLUME ​
Description:
The Sound Manager Global Volume Event.
This event is dispatched by the Sound Manager when its volume property is changed, either directly
or via the setVolume method. This changes the volume of all active sounds.
Listen to it from a Scene using: this.sound.on('volume', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.WebAudioSoundManager | Phaser.Sound.HTML5AudioSoundManager No A reference to the sound manager that emitted the event.
volume number No The new global volume of the Sound Manager.
Source: src/sound/events/GLOBAL_VOLUME_EVENT.js#L7
Since: 3.0.0
LOOP ​
LOOP ​
Description:
The Sound Loop Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their loop state is changed.
Listen to it from a Sound instance using Sound.on('loop', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'loop' , listener ) ;
music . setLoop ( true ) ;
This is not to be confused with the LOOPED event, which emits each time a Sound loops during playback.
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
loop boolean No The new loop value. true if the Sound will loop, otherwise false .
Source: src/sound/events/LOOP_EVENT.js#L7
Since: 3.0.0
LOOPED ​
LOOPED ​
Description:
The Sound Looped Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they loop during playback.
Listen to it from a Sound instance using Sound.on('looped', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'looped' , listener ) ;
music . setLoop ( true ) ;
music . play ( ) ;
This is not to be confused with the LOOP event, which only emits when the loop state of a Sound is changed.
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
Source: src/sound/events/LOOPED_EVENT.js#L7
Since: 3.0.0
MUTE ​
MUTE ​
Description:
The Sound Mute Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their mute state changes.
Listen to it from a Sound instance using Sound.on('mute', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'mute' , listener ) ;
music . play ( ) ;
music . setMute ( true ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
mute boolean No The mute value. true if the Sound is now muted, otherwise false .
Source: src/sound/events/MUTE_EVENT.js#L7
Since: 3.0.0
PAN ​
PAN ​
Description:
The Sound Pan Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their pan changes.
Listen to it from a Sound instance using Sound.on('pan', listener) , i.e.:
var sound = this . sound . add ( 'key' ) ;
sound . on ( 'pan' , listener ) ;
sound . play ( ) ;
sound . setPan ( 0.5 ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
pan number No The new pan of the Sound.
Source: src/sound/events/PAN_EVENT.js#L7
Since: 3.50.0
PAUSE ​
PAUSE ​
Description:
The Sound Pause Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are paused.
Listen to it from a Sound instance using Sound.on('pause', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'pause' , listener ) ;
music . play ( ) ;
music . pause ( ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
Source: src/sound/events/PAUSE_EVENT.js#L7
Since: 3.0.0
PAUSE_ALL ​
PAUSE_ALL ​
Description:
The Pause All Sounds Event.
This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,
or the HTML5 Audio Manager. It is dispatched when the pauseAll method is invoked and after all current Sounds
have been paused.
Listen to it from a Scene using: this.sound.on('pauseall', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.BaseSoundManager No A reference to the sound manager that emitted the event.
Source: src/sound/events/PAUSE_ALL_EVENT.js#L7
Since: 3.0.0
PLAY ​
PLAY ​
Description:
The Sound Play Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are played.
Listen to it from a Sound instance using Sound.on('play', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'play' , listener ) ;
music . play ( ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
Source: src/sound/events/PLAY_EVENT.js#L7
Since: 3.0.0
RATE ​
RATE ​
Description:
The Sound Rate Change Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their rate changes.
Listen to it from a Sound instance using Sound.on('rate', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'rate' , listener ) ;
music . play ( ) ;
music . setRate ( 0.5 ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
rate number No The new rate of the Sound.
Source: src/sound/events/RATE_EVENT.js#L7
Since: 3.0.0
RESUME ​
RESUME ​
Description:
The Sound Resume Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are resumed from a paused state.
Listen to it from a Sound instance using Sound.on('resume', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'resume' , listener ) ;
music . play ( ) ;
music . pause ( ) ;
music . resume ( ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
Source: src/sound/events/RESUME_EVENT.js#L7
Since: 3.0.0
RESUME_ALL ​
RESUME_ALL ​
Description:
The Resume All Sounds Event.
This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,
or the HTML5 Audio Manager. It is dispatched when the resumeAll method is invoked and after all current Sounds
have been resumed.
Listen to it from a Scene using: this.sound.on('resumeall', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.BaseSoundManager No A reference to the sound manager that emitted the event.
Source: src/sound/events/RESUME_ALL_EVENT.js#L7
Since: 3.0.0
SEEK ​
SEEK ​
Description:
The Sound Seek Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are seeked to a new position.
Listen to it from a Sound instance using Sound.on('seek', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'seek' , listener ) ;
music . play ( ) ;
music . setSeek ( 5000 ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
detune number No The new detune value of the Sound.
Source: src/sound/events/SEEK_EVENT.js#L7
Since: 3.0.0
STOP ​
STOP ​
Description:
The Sound Stop Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when they are stopped.
Listen to it from a Sound instance using Sound.on('stop', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'stop' , listener ) ;
music . play ( ) ;
music . stop ( ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
Source: src/sound/events/STOP_EVENT.js#L7
Since: 3.0.0
STOP_ALL ​
STOP_ALL ​
Description:
The Stop All Sounds Event.
This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,
or the HTML5 Audio Manager. It is dispatched when the stopAll method is invoked and after all current Sounds
have been stopped.
Listen to it from a Scene using: this.sound.on('stopall', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.BaseSoundManager No A reference to the sound manager that emitted the event.
Source: src/sound/events/STOP_ALL_EVENT.js#L7
Since: 3.0.0
UNLOCKED ​
UNLOCKED ​
Description:
The Sound Manager Unlocked Event.
This event is dispatched by the Base Sound Manager, or more typically, an instance of the Web Audio Sound Manager,
or the HTML5 Audio Manager. It is dispatched during the update loop when the Sound Manager becomes unlocked. For
Web Audio this is on the first user gesture on the page.
Listen to it from a Scene using: this.sound.on('unlocked', listener) .
Parameters:
name type optional description
soundManager Phaser.Sound.BaseSoundManager No A reference to the sound manager that emitted the event.
Source: src/sound/events/UNLOCKED_EVENT.js#L7
Since: 3.0.0
VOLUME ​
VOLUME ​
Description:
The Sound Volume Event.
This event is dispatched by both Web Audio and HTML5 Audio Sound objects when their volume changes.
Listen to it from a Sound instance using Sound.on('volume', listener) , i.e.:
var music = this . sound . add ( 'key' ) ;
music . on ( 'volume' , listener ) ;
music . play ( ) ;
music . setVolume ( 0.5 ) ;
Parameters:
name type optional description
sound Phaser.Sound.WebAudioSound | Phaser.Sound.HTML5AudioSound No A reference to the Sound that emitted the event.
volume number No The new volume of the Sound.
Source: src/sound/events/VOLUME_EVENT.js#L7
Since: 3.0.0
Previous
Phaser.Scenes
Next
Phaser.Sound
Static functions
COMPLETE
DECODED
DECODED_ALL
DESTROY
DETUNE
GLOBAL_DETUNE
GLOBAL_MUTE
GLOBAL_RATE
GLOBAL_VOLUME
LOOP
LOOPED
MUTE
PAN
PAUSE
PAUSE_ALL
PLAY
RATE
RESUME
RESUME_ALL
SEEK
STOP
STOP_ALL
UNLOCKED
VOLUME
