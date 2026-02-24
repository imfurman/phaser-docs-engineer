# Audio | Phaser Help

Source: https://docs.phaser.io/phaser/concepts/audio

Concepts
Audio
On this page
Audio
Web Browsers offer the ability to play audio in two different ways. The first is known as the Audio Tag. This is an HTML tag you can put on a web page that offers UI controls to play and pause/resume audio files. The second is known as the Web Audio API. This is a JavaScript API that allows you to create and control audio files directly from your code. It's a much more powerful system than the Audio Tag, but is not supported by all browsers.
Phaser has a built-in Sound Manager that allows you to play audio files in your game. It will automatically detect if the browser supports the Web Audio API and if it does, it will use that. If not, it will fall back to the Audio Tag. This means that you can use the same API to play audio files in all browsers, regardless of their support for the Web Audio API.
As with WebGL vs. Canvas, there are things that only Web Audio can do. Such as positional audio, i.e. having sounds 'follow' a player across the game world. It's also much better suited to playing lots of short duration sound effects in quick succession, i.e. "gunshots" or "explosions".
You can pick which audio system you'd like to use via the Game Configuration, or even disable audio entirely. Not all games need audio, after all.
The Phaser Sound Manager is a global system. This means that it belongs to the Game instance, and if you start to play a sound in one Scene, it won't automatically stop just because you change to another Scene. This gives you a lot of control, but also means you need to be careful to stop looping sounds when you're done with them, or they'll keep playing.
Autoplay ​
Most browsers won't play sound until the user clicks/taps on the game. You can check the sound manager's locked property for this.
Chrome gives a console warning if the game boots using Web Audio:
The AudioContext was not allowed to start. It must be resumed (or created) after a user gesture on the page
That's normal. Phaser will try to resume the audio context after the first user gesture (click/tap). If you don't need sound in your game, disable audio and you won't see this warning.
You can also create the game from a click/tap to avoid this problem.
Some browsers give a console error when playing a locked sound fails, and some don't.
Autoplay guide for media and Web Audio APIs
Configuration ​
Web audio ​
Web audio is the default audio context.
Disable web audio ​
var config = {
// ....
audio : {
disableWebAudio : true ,
} ,
// ....
} ;
var game = new Phaser . Game ( config ) ;
Disable all audio ​
var config = {
// ....
audio : {
noAudio : true ,
} ,
// ....
} ;
var game = new Phaser . Game ( config ) ;
Loading audio files ​
See details in Media container formats and Web audio codec guide . If you're publishing a game you should probably support at least MP3 .
When loading audio, Phaser matches the media type (inferred from the URL or given by you) with the device's support for that type. If there's no match, nothing is downloaded and if you try to create or play a sound with that key it will fail with an error.
this . load . audio ( key , urls , config , xhrSettings ) ;
key : The key to use for this file, or a file configuration object, or array of them.
urls : The absolute or relative URL to load the audio files from.
config : An object containing an instances property for HTML5Audio. Defaults to 1.
xhrSettings : An XHR Settings configuration object. Used in replacement of the Loaders default XHR Settings.
Decode audio ​
Decode audio data into a format ready for playback via Web Audio. The audio data can be a base64 encoded string, an audio media-type data uri, or an ArrayBuffer instance.
this . sound . decodeAudio ( key , audioData ) ;
audioData : Audio data
A base64 encoded string
An audio media-type data uri
An ArrayBuffer instance
Or
this . sound . decodeAudio ( audioFiles ) ;
audioFiles : An array of {key, data}
data : Audio data
A base64 encoded string
An audio media-type data uri
An ArrayBuffer instance
Decoded events ​
Finished decoding an audio data
this . sound . on ( "decoded" , key ) ;
Finished decoding all audio data
this . sound . on ( "decodedall" ) ;
Unlock audio ​
Unlocks Web Audio API/HTML5 Audio loading on the initial input event.
this . sound . unlock ( ) ;
Play sound ​
Sound instance will be destroyed when playback ends.
this . sound . play ( key ) ;
or
this . sound . play ( key , config ) ;
/*
var sound = this.sound.add(key);
sound.play(config);
*/
Position of the Spatial Audio listener ​
Sets the x and y position of the Spatial Audio listener on this Web Audios context.
this . sound . setListenerPosition ( x , y ) ;
x , y : The x/y position of the Spatial Audio listener. Default value is center of the game canvas.
!!! note Web audio only
Sound instance ​
Create sound instance ​
Adds a new sound into the sound manager.
var music = this . sound . add ( key ) ;
var music = this . sound . add ( key , config ) ;
config : An optional config object containing default sound settings.
Sound instance configuration ​
{
mute : false ,
volume : 1 ,
rate : 1 ,
detune : 0 ,
seek : 0 ,
loop : false ,
delay : 0 ,
// source of the spatial sound
source : {
x : 0 ,
y : 0 ,
z : 0 ,
panningModel : 'equalpower' ,
distanceModel : 'inverse' ,
orientationX : 0 ,
orientationY : 0 ,
orientationZ : - 1 ,
refDistance : 1 ,
maxDistance : 10000 ,
rolloffFactor : 1 ,
coneInnerAngle : 360 ,
coneOuterAngle : 0 ,
coneOuterGain : 0 ,
follow : undefined
}
}
source : Source of the spatial sound
x , y : The horizontal/vertical position of the audio in a right-hand Cartesian coordinate system.
z : Represents the longitudinal (back and forth) position of the audio in a right-hand Cartesian coordinate system.
panningModel : An enumerated value determining which spatialization algorithm to use to position the audio in 3D space.
'equalpower'
'HRTF'
orientationX , orientationY : The horizontal/vertical position of the audio source's vector in a right-hand Cartesian coordinate system.
orientationZ : Represents the longitudinal (back and forth) position of the audio source's vector in a right-hand Cartesian coordinate system.
refDistance : A double value representing the reference distance for reducing volume as the audio source moves further from the listener. For distances greater than this the volume will be reduced based on rolloffFactor and distanceModel .
maxDistance : The maximum distance between the audio source and the listener, after which the volume is not reduced any further.
rolloffFactor : A double value describing how quickly the volume is reduced as the source moves away from the listener. This value is used by all distance models.
coneInnerAngle : The angle, in degrees, of a cone inside of which there will be no volume reduction.
coneOuterAngle : The angle, in degrees, of a cone outside of which the volume will be reduced by a constant value, defined by the coneOuterGain property.
coneOuterGain : The amount of volume reduction outside the cone defined by the coneOuterAngle attribute. Its default value is 0 , meaning that no sound can be heard. A value between 0 and 1 .
follow : Set this Sound object to automatically track the x/y position of this object. Can be a Phaser Game Object, Vec2 or anything that exposes public x/y properties.
Play sound instance ​
Start playing
music . play ( ) ;
Start playing with configuration
music . play ( config ) ;
config
Stop
music . stop ( ) ;
Pause
music . pause ( ) ;
Resume
music . resume ( ) ;
Methods ​
Mute ​
Set
music . setMute ( mute ) ; // mute: true/false
// music.mute = mute;
Get
var mute = music . mute ;
Volume ​
Set
music . setVolume ( volume ) ; // volume: 0 to 1
// music.volume = volume;
Get
var volume = music . volume ;
Detune ​
Sets global detuning of all sounds in cents . The range of the value is -1200 to 1200, but we recommend setting it to 50.
Set
music . setDetune ( detune ) ; // detune: -1200 to 1200
// music.detune = detune;
Get
var detune = music . detune ;
Playback rate ​
Set
music . setRate ( rate ) ; // rate: 1.0(normal speed), 0.5(half speed), 2.0(double speed)
// music.rate = rate;
Get
var rate = music . rate ;
Seek to ​
Seek to
music . setSeek ( time ) ; // seek: playback time
// music.seek = seek;
Get current playback time
var time = music . seek ; // return 0 when playback ends
Loop ​
Set
music . setLoop ( loop ) ; // loop: true/false
// music.loop = loop;
Get
var loop = music . loop ;
Properties ​
Duration : duration of this sound
var duration = music . duration ;
Is playing
var isPlaying = music . isPlaying ;
Is paused
var isPaused = music . isPaused ;
Asset key
var key = music . key ;
Events ​
Start playing
music . once ( "play" , function ( music ) { } ) ;
Playback end
music . once ( "complete" , function ( music ) { } ) ;
Looping
music . once ( "looped" , function ( music ) { } ) ;
Pause
music . once ( "pause" , function ( music ) { } ) ;
Resume
music . once ( "resume" , function ( music ) { } ) ;
Stop
music . once ( "stop" , function ( music ) { } ) ;
Set mute
music . once ( "mute" , function ( music , mute ) { } ) ;
Set volume
music . once ( "volume" , function ( music , volume ) { } ) ;
Set detune
music . once ( "detune" , function ( music , detune ) { } ) ;
Set play-rate
music . once ( "rate" , function ( music , rate ) { } ) ;
Seek to
music . once ( "seek" , function ( music , time ) { } ) ;
set loop
music . once ( "loop" , function ( music , loop ) { } ) ;
Play marked sound ​
Sound instance will be destroyed when playback ends.
this . sound . play ( key , marker ) ;
marker : Marked section of a sound represented by name, and optionally start time, duration, and config object.
Marker ​
{
name : '' ,
start : 0 ,
duration : music . duration ,
config : {
mute : false ,
volume : 1 ,
rate : 1 ,
detune : 0 ,
seek : 0 ,
loop : false ,
delay : 0
}
}
Markers in sound instance ​
Add marker ​
music . addMarker ( marker ) ;
Marker
Play marked sound ​
music . play ( markerName ) ;
music . play ( markerName , config ) ;
config
Audio sprite ​
Load audio sprite ​
scene . load . audioSprite ( key , urls , markersConfig , config ) ;
See loader
Format of markersConfig
{
resources : urls , // an array of audio files
spritemap : {
markerName0 : {
start : 0 ,
end : 0
} ,
markerName1 : {
start : 0 ,
end : 0
}
// ...
}
}
Play sound ​
Create a sound instance then play the marked section, this sound instance will be destroyed when playback ends.
this . sound . playAudioSprite ( key , markerName , config ) ;
config
Sound instance ​
Create a sound instance with markers.
var music = this . sound . addAudioSprite ( key , config ) ;
config
Play sound instance ​
music . play ( markerName ) ;
music . play ( markerName , config ) ;
config
Sound manager ​
Mute ​
Set
this . sound . setMute ( mute ) ; // mute: true/false
// this.sound.mute = mute;
Get
var mute = this . sound . mute ;
Volume ​
Set
this . sound . setVolume ( volume ) ; // volume: 0 to 1
// this.sound.volume = volume;
Get
var volume = this . sound . volume ;
Detune ​
Set
this . sound . setDetune ( detune ) ; // detune: -1200 to 1200
// this.sound.detune = detune;
Get
var detune = this . sound . detune ;
Playback rate ​
Set
this . sound . setRate ( rate ) ; // rate: 1.0(normal speed), 0.5(half speed), 2.0(double speed)
// this.sound.rate = rate;
Get
var rate = this . sound . rate ;
Get music instance ​
Get first by key
var music = this . sound . get ( key ) ; // music instance, or null
Get all by key
var musicArray = this . sound . getAll ( key ) ; // music instance, or null
Get all
var musicArray = this . sound . getAll ( ) ;
Get all playing
var musicArray = this . sound . getAllPlaying ( ) ;
Remove music instance ​
Remove by key
var removed = this . sound . removeByKey ( key ) ;
removed : The number of matching sound objects that were removed.
Remove all
this . sound . removeAll ( ) ;
Stop music instance ​
Stop by key
var stopped = this . sound . stopByKey ( key ) ;
stopped : How many sounds were stopped.
Stop all
this . sound . stopAll ( ) ;
Analyser ​
Web Audio API has the ability to extract frequency, waveform, and other data from your audio source, which can then be used to create visualizations .
Create analyser node
var analyser = this . sound . context . createAnalyser ( ) ;
Configure analyser node
analyser . smoothingTimeConstant = 1 ;
analyser . fftSize = 8192 ;
analyser . minDecibels = - 90 ;
analyser . maxDecibels = - 10 ;
smoothingTimeConstant : Averaging constant with the last analysis frame.
0 (no time averaging) ~ 1 . Default value is 0.8 .
fftSize : Window size.
32 , 64 , 128 , 256 , 512 , 1024 , 2048 , 4096 , 8192 , 16384 , and 32768 . Defaults to 2048 .
minDecibels : Minimum decibel value for scaling the FFT analysis data.
0 dB is the loudest possible sound, -10 dB is a 10th of that, etc. The default value is -100 dB
maxDecibels : Maximum decibel value for scaling the FFT analysis data.
The default value is -30 dB.
Set source of analyser node
Global volume nodee -> analyser node
this . sound . masterVolumeNode . connect ( analyser ) ;
A sound instance -> analyser node
music . volumeNode . connect ( analyser ) ;
Ouput analyser node to audio context
analyser . connect ( this . sound . context . destination ) ;
Create output data array
var dataArrayLength = analyser . frequencyBinCount ;
var dataArray = new Uint8Array ( dataArrayLength ) ;
Get output data
analyser . getByteTimeDomainData ( dataArray ) ;
Retrieve output data
for ( var i = 0 ; i < dataArrayLength ; i ++ ) {
var data = dataArray [ i ] ;
}
Author Credits ​
Content on this page includes work by:
RexRainbow
samme
Previous
Animations
Next
Cameras
Autoplay
Configuration
Web audio
Disable web audio
Disable all audio
Loading audio files
Decode audio
Decoded events
Unlock audio
Play sound
Position of the Spatial Audio listener
Sound instance
Create sound instance
Play sound instance
Methods
Properties
Events
Play marked sound
Marker
Markers in sound instance
Add marker
Play marked sound
Audio sprite
Load audio sprite
Play sound
Sound instance
Play sound instance
Sound manager
Mute
Volume
Detune
Playback rate
Get music instance
Remove music instance
Stop music instance
Analyser
Author Credits
