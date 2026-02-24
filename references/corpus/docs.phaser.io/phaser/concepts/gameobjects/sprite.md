# Sprite | Phaser Help

Source: https://docs.phaser.io/phaser/concepts/gameobjects/sprite

Concepts
Game Objects
Sprite
On this page
Sprite
A Sprite Game Object is used for the display of both static and animated images in your game. Sprites can have input events and physics bodies. They can also be tweened, tinted, scrolled and animated.
The main difference between a Sprite and an Image Game Object is that you cannot animate Images. As such, Sprites take a fraction longer to process and have a larger API footprint due to the Animation Component. If you do not require animation then you can safely use Images to replace Sprites in all cases.
Load texture ​
Texture for static image
this . load . image ( key , url ) ;
Reference: load image
Load atlas ​
Atlas for animation images
this . load . atlas ( key , textureURL , atlasURL ) ;
Reference: load atlas
Add sprite object ​
var sprite = this . add . sprite ( x , y , key ) ;
// var sprite = this.add.sprite(x, y, key, frame);
Add sprite from JSON
var sprite = this . make . sprite ( {
x : 0 ,
y : 0 ,
key : '' ,
// frame: '',
// angle: 0,
// alpha: 1
// flipX: true,
// flipY: true,
// scale : {
// x: 1,
// y: 1
//},
// anims: {
// key: ,
// repeat: ,
// ...
// },
// origin: {x: 0.5, y: 0.5},
add : true
} ) ;
key :
A string
An array of string to pick one element at random
x , y , scale.x , scale.y :
A number
A callback to get return value
function ( ) { return 0 ; }
Random integer between min and max
{ randInt : [ min , max ] }
Random float between min and max
{ randFloat : [ min , max ] }
Custom class ​
Define class
class MySprite extends Phaser . GameObjects . Sprite {
constructor ( scene , x , y , texture , frame ) {
super ( scene , x , y , texture , frame ) ;
// ...
this . add . existing ( this ) ;
}
// ...
// preUpdate(time, delta) {
// super.preUpdate(time, delta);
// }
}
this.add.existing(gameObject) : Adds an existing Game Object to this Scene.
If the Game Object renders, it will be added to the Display List.
If it has a preUpdate method, it will be added to the Update List.
Create instance
var sprite = new MySprite ( scene , x , y , key ) ;
Texture ​
See game object - texture
Other properties ​
See game object
Create mask ​
var mask = sprite . createBitmapMask ( ) ;
See mask
Shader effects ​
Support preFX and postFX effects
Animation ​
Create animation ​
Global animation for all sprites
this . anims . create ( config ) ;
Private animation for this sprite
sprite . anims . create ( config ) ;
config : See Add animation section .
Create Aseprite animation ​
Global Aseprite animation for all sprites
this . anims . createFromAseprite ( key , tags ) ;
Private Aseprite animation for this sprite
sprite . anims . createFromAseprite ( key , tags ) ;
Remove animation ​
Remove from global animation manager
this . anims . remove ( key ) ;
or
sprite . anims . globalRemove ( key ) ;
Remove from private animation state
sprite . anims . remove ( key ) ;
Get animation ​
Get global animation object
var anim = this . anims . get ( key ) ;
Get private animation object
var anim = sprite . anims . get ( key ) ;
Has animation ​
Has global animation object
var hasAnim = this . anims . exists ( key ) ;
Get private animation object
var hasAnim = sprite . anims . exists ( key ) ;
Play animation ​
Play
sprite . play ( key ) ;
// sprite.play(key, ignoreIfPlaying);
key : Animation key string, or animation config
String key of animation
Animation config, to override default config
{
key ,
frameRate ,
duration ,
delay ,
repeat ,
repeatDelay ,
yoyo ,
showOnStart ,
hideOnComplete ,
startFrame ,
timeScale
}
Play in reverse
sprite . playReverse ( key ) ;
// sprite.playReverse(key, ignoreIfPlaying);
key : Animation key string, or animation config
Play after delay
sprite . playAfterDelay ( key , delay ) ;
key : Animation key string, or animation config
Play after repeat
sprite . playAfterRepeat ( key , repeatCount ) ;
key : Animation key string, or animation config
Chain ​
Chain next animation
sprite . chain ( key ) ;
key : Animation key string, or animation config
Chain next and next animation
sprite . chain ( key0 ) . chain ( key1 ) ;
key0 , key1 : Animation key string, or animation config
Stop ​
Immediately stop
sprite . stop ( ) ;
Stop after delay
sprite . stopAfterDelay ( delay ) ;
Stop at frame
sprite . stopOnFrame ( frame ) ;
frame : Frame object in current animation.
var currentAnim = sprite . anims . currentAnim ;
var frame = currentAnim . getFrameAt ( index ) ;
Stop after repeat
sprite . stopAfterRepeat ( repeatCount ) ;
Restart ​
sprite . anims . restart ( ) ;
// sprite.anims.restart(includeDelay, resetRepeats);
Time scale ​
Get
var timeScale = sprite . anims . globalTimeScale ;
Set
sprite . anims . globalTimeScale = timeScale ;
See also Global time scale
Properties ​
Has started
var hasStarted = sprite . anims . hasStarted ;
Is playing
var isPlaying = sprite . anims . isPlaying ;
Is paused
var isPaused = sprite . anims . isPaused ;
Total frames count
var frameCount = sprite . anims . getTotalFrames ( ) ;
Delay
var delay = sprite . anims . delay ;
Repeat
Total repeat count
var repeatCount = sprite . anims . repeat ;
Repeat counter
var repeatCount = sprite . anims . repeatCounter ;
Repeat delay
var repeatDelay = sprite . anims . repeatDelay ;
Yoyo
var repeatDelay = sprite . anims . yoyo ;
Current animation key
var key = sprite . anims . getName ( ) ;
key : Return '' if not playing any animation.
Current frame name
var frameName = sprite . anims . getFrameName ( ) ;
frameName : Return '' if not playing any animation.
Current animation
var currentAnim = sprite . anims . currentAnim ;
Current frame
var currentFrame = sprite . anims . currentFrame ;
Events ​
On start
sprite . on ( 'animationstart' , function ( currentAnim , currentFrame , sprite ) { } ) ;
sprite . on ( 'animationstart-' + key , function ( currentAnim , currentFrame , sprite ) { } ) ;
On restart
sprite . on ( 'animationrestart' , function ( currentAnim , currentFrame , sprite ) { } ) ;
sprite . on ( 'animationrestart-' + key , function ( currentAnim , currentFrame , sprite ) { } ) ;
On complete
sprite . on ( 'animationcomplete' , function ( currentAnim , currentFramee , sprite ) { } ) ;
sprite . on ( 'animationcomplete-' + key , function ( currentAnim , currentFramee , sprite ) { } ) ;
On stop
sprite . on ( 'animationstop' , function ( currentAnim , currentFrame , sprite ) { } ) ;
sprite . on ( 'animationstop-' + key , function ( currentAnim , currentFrame , sprite ) { } ) ;
On update
sprite . on ( 'animationupdate' , function ( currentAnim , currentFrame , sprite ) { } ) ;
sprite . on ( 'animationupdate-' + key , function ( currentAnim , currentFrame , sprite ) { } ) ;
On repeat
sprite . on ( 'animationrepeat' , function ( currentAnim , currentFrame , sprite ) { } ) ;
sprite . on ( 'animationrepeat-' + key , function ( currentAnim , currentFrame , sprite ) { } ) ;
Author Credits ​
Content on this page includes work by:
RexRainbow
Previous
Shader
Next
Text
Load texture
Load atlas
Add sprite object
Custom class
Texture
Other properties
Create mask
Shader effects
Animation
Create animation
Create Aseprite animation
Play animation
Chain
Stop
Restart
Time scale
Properties
Events
Author Credits
