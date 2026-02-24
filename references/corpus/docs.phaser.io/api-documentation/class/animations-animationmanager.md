# AnimationManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/animations-animationmanager

Phaser API Documentation
Class
AnimationManager
Version: Phaser v3.90.0
On this page
AnimationManager
The Animation Manager.
Animations are managed by the global Animation Manager. This is a singleton class that is
responsible for creating and delivering animations and their corresponding data to all Game Objects.
Unlike plugins it is owned by the Game instance, not the Scene.
Sprites and other Game Objects get the data they need from the AnimationManager.
Constructor
new AnimationManager(game)
Parameters
name type optional description
game Phaser.Game No A reference to the Phaser.Game instance.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/animations/AnimationManager.js#L19
Since: 3.0.0
Public Members ​
anims ​
anims: Phaser.Structs.Map.<string, Phaser.Animations.Animation > ​
Description:
The Animations registered in the Animation Manager.
This map should be modified with the #add and #create methods of the Animation Manager.
Access: protected
Source: src/animations/AnimationManager.js#L79
Since: 3.0.0
game ​
game: Phaser.Game ​
Description:
A reference to the Phaser.Game instance.
Access: protected
Source: src/animations/AnimationManager.js#L47
Since: 3.0.0
globalTimeScale ​
globalTimeScale: number ​
Description:
The global time scale of the Animation Manager.
This scales the time delta between two frames, thus influencing the speed of time for the Animation Manager.
Source: src/animations/AnimationManager.js#L67
Since: 3.0.0
mixes ​
mixes: Phaser.Structs.Map.<string, Phaser.Animations.Animation > ​
Description:
A list of animation mix times.
See the #setMix method for more details.
Source: src/animations/AnimationManager.js#L91
Since: 3.50.0
name ​
name: string ​
Description:
The name of this Animation Manager.
Source: src/animations/AnimationManager.js#L112
Since: 3.0.0
paused ​
paused: boolean ​
Description:
Whether the Animation Manager is paused along with all of its Animations.
Source: src/animations/AnimationManager.js#L102
Since: 3.0.0
textureManager ​
textureManager: Phaser.Textures.TextureManager ​
Description:
A reference to the Texture Manager.
Access: protected
Source: src/animations/AnimationManager.js#L57
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
<instance> add(key, animation) ​
Description:
Adds an existing Animation to the Animation Manager.
Parameters:
name type optional description
key string No The key under which the Animation should be added. The Animation will be updated with it. Must be unique.
animation Phaser.Animations.Animation No The Animation which should be added to the Animation Manager.
Returns: Phaser.Animations.AnimationManager - This Animation Manager.
Fires: Phaser.Animations.Events#event:ADD_ANIMATION
Source: src/animations/AnimationManager.js#L276
Since: 3.0.0
addMix ​
<instance> addMix(animA, animB, delay) ​
Description:
Adds a mix between two animations.
Mixing allows you to specify a unique delay between a pairing of animations.
When playing Animation A on a Game Object, if you then play Animation B, and a
mix exists, it will wait for the specified delay to be over before playing Animation B.
This allows you to customise smoothing between different types of animation, such
as blending between an idle and a walk state, or a running and a firing state.
Note that mixing is only applied if you use the Sprite.play method. If you opt to use
playAfterRepeat or playAfterDelay instead, those will take priority and the mix
delay will not be used.
To update an existing mix, just call this method with the new delay.
To remove a mix pairing, see the removeMix method.
Parameters:
name type optional description
animA string | Phaser.Animations.Animation No The string-based key, or instance of, Animation A.
animB string | Phaser.Animations.Animation No The string-based key, or instance of, Animation B.
delay number No The delay, in milliseconds, to wait when transitioning from Animation A to B.
Returns: Phaser.Animations.AnimationManager - This Animation Manager.
Source: src/animations/AnimationManager.js#L138
Since: 3.50.0
boot ​
<instance> boot() ​
Description:
Registers event listeners after the Game boots.
Source: src/animations/AnimationManager.js#L124
Since: 3.0.0
create ​
<instance> create(config) ​
Description:
Creates a new Animation and adds it to the Animation Manager.
Animations are global. Once created, you can use them in any Scene in your game. They are not Scene specific.
If an invalid key is given this method will return false .
If you pass the key of an animation that already exists in the Animation Manager, that animation will be returned.
A brand new animation is only created if the key is valid and not already in use.
If you wish to re-use an existing key, call AnimationManager.remove first, then this method.
Parameters:
name type optional description
config Phaser.Types.Animations.Animation No The configuration settings for the Animation.
Returns: Phaser.Animations.Animation , false - The Animation that was created, or false if the key is already in use.
Fires: Phaser.Animations.Events#event:ADD_ANIMATION
Source: src/animations/AnimationManager.js#L492
Since: 3.0.0
createFromAseprite ​
<instance> createFromAseprite(key, [tags], [target]) ​
Description:
Create one, or more animations from a loaded Aseprite JSON file.
Aseprite is a powerful animated sprite editor and pixel art tool.
You can find more details at https://www.aseprite.org/
To export a compatible JSON file in Aseprite, please do the following:
Go to "File - Export Sprite Sheet"
On the Layout tab:
2a. Set the "Sheet type" to "Packed"
2b. Set the "Constraints" to "None"
2c. Check the "Merge Duplicates" checkbox
On the Sprite tab:
3a. Set "Layers" to "Visible layers"
3b. Set "Frames" to "All frames", unless you only wish to export a sub-set of tags
On the Borders tab:
4a. Check the "Trim Sprite" and "Trim Cells" options
4b. Ensure "Border Padding", "Spacing" and "Inner Padding" are all > 0 (1 is usually enough)
On the Output tab:
5a. Check "Output File", give your image a name and make sure you choose "png files" as the file type
5b. Check "JSON Data" and give your json file a name
5c. The JSON Data type can be either a Hash or Array, Phaser doesn't mind.
5d. Make sure "Tags" is checked in the Meta options
5e. In the "Item Filename" input box, make sure it says just "{frame}" and nothing more.
Click export
This was tested with Aseprite 1.2.25.
This will export a png and json file which you can load using the Aseprite Loader, i.e.:
function preload ( )
{
this . load . path = 'assets/animations/aseprite/' ;
this . load . aseprite ( 'paladin' , 'paladin.png' , 'paladin.json' ) ;
}
Once loaded, you can call this method from within a Scene with the 'atlas' key:
this . anims . createFromAseprite ( 'paladin' ) ;
Any animations defined in the JSON will now be available to use in Phaser and you play them
via their Tag name. For example, if you have an animation called 'War Cry' on your Aseprite timeline,
you can play it in Phaser using that Tag name:
this . add . sprite ( 400 , 300 ) . play ( 'War Cry' ) ;
When calling this method you can optionally provide an array of tag names, and only those animations
will be created. For example:
this . anims . createFromAseprite ( 'paladin' , [ 'step' , 'War Cry' , 'Magnum Break' ] ) ;
This will only create the 3 animations defined. Note that the tag names are case-sensitive.
Parameters:
name type optional description
key string No The key of the loaded Aseprite atlas. It must have been loaded prior to calling this method.
tags Array.<string> Yes An array of Tag names. If provided, only animations found in this array will be created.
target Phaser.Animations.AnimationManager | Phaser.GameObjects.GameObject Yes Create the animations on this target Sprite. If not given, they will be created globally in this Animation Manager.
Returns: Array.< Phaser.Animations.Animation > - An array of Animation instances that were successfully created.
Source: src/animations/AnimationManager.js#L323
Since: 3.50.0
destroy ​
<instance> destroy() ​
Description:
Destroy this Animation Manager and clean up animation definitions and references to other objects.
This method should not be called directly. It will be called automatically as a response to a destroy event from the Phaser.Game instance.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/animations/AnimationManager.js#L1045
Since: 3.0.0
exists ​
<instance> exists(key) ​
Description:
Checks to see if the given key is already in use within the Animation Manager or not.
Animations are global. Keys created in one scene can be used from any other Scene in your game. They are not Scene specific.
Parameters:
name type optional description
key string No The key of the Animation to check.
Returns: boolean - true if the Animation already exists in the Animation Manager, or false if the key is available.
Source: src/animations/AnimationManager.js#L306
Since: 3.16.0
fromJSON ​
<instance> fromJSON(data, [clearCurrentAnimations]) ​
Description:
Loads this Animation Manager's Animations and settings from a JSON object.
Parameters:
name type optional default description
data string | Phaser.Types.Animations.JSONAnimations Phaser.Types.Animations.JSONAnimation No
clearCurrentAnimations boolean Yes false If set to true , the current animations will be removed ( anims.clear() ). If set to false (default), the animations in data will be added.
Returns: Array.< Phaser.Animations.Animation > - An array containing all of the Animation objects that were created as a result of this call.
Source: src/animations/AnimationManager.js#L540
Since: 3.0.0
generateFrameNames ​
<instance> generateFrameNames(key, [config]) ​
Description:
Generate an array of Phaser.Types.Animations.AnimationFrame objects from a texture key and configuration object.
Generates objects with string based frame names, as configured by the given Phaser.Types.Animations.GenerateFrameNames .
It's a helper method, designed to make it easier for you to extract all of the frame names from texture atlases.
If you're working with a sprite sheet, see the generateFrameNumbers method instead.
Example:
If you have a texture atlases loaded called gems and it contains 6 frames called ruby_0001 , ruby_0002 , and so on,
then you can call this method using: this.anims.generateFrameNames('gems', { prefix: 'ruby_', start: 1, end: 6, zeroPad: 4 }) .
The end value tells it to select frames 1 through 6, incrementally numbered, all starting with the prefix ruby_ . The zeroPad
value tells it how many zeroes pad out the numbers. To create an animation using this method, you can do:
this . anims . create ( {
key : 'ruby' ,
repeat : - 1 ,
frames : this . anims . generateFrameNames ( 'gems' , {
prefix : 'ruby_' ,
end : 6 ,
zeroPad : 4
} )
} ) ;
Please see the animation examples for further details.
Parameters:
name type optional description
key string No The key for the texture containing the animation frames.
config Phaser.Types.Animations.GenerateFrameNames Yes The configuration object for the animation frame names.
Returns: Array.< Phaser.Types.Animations.AnimationFrame > - The array of {@link Phaser.Types.Animations.AnimationFrame} objects.
Source: src/animations/AnimationManager.js#L589
Since: 3.0.0
generateFrameNumbers ​
<instance> generateFrameNumbers(key, [config]) ​
Description:
Generate an array of Phaser.Types.Animations.AnimationFrame objects from a texture key and configuration object.
Generates objects with numbered frame names, as configured by the given Phaser.Types.Animations.GenerateFrameNumbers .
If you're working with a texture atlas, see the generateFrameNames method instead.
It's a helper method, designed to make it easier for you to extract frames from sprite sheets.
Example:
If you have a sprite sheet loaded called explosion and it contains 12 frames, then you can call this method using:
this.anims.generateFrameNumbers('explosion', { start: 0, end: 11 }) .
The end value of 11 tells it to stop after the 12th frame has been added, because it started at zero.
To create an animation using this method, you can do:
this . anims . create ( {
key : 'boom' ,
frames : this . anims . generateFrameNumbers ( 'explosion' , {
start : 0 ,
end : 11
} )
} ) ;
Note that start is optional and you don't need to include it if the animation starts from frame 0.
To specify an animation in reverse, swap the start and end values.
If the frames are not sequential, you may pass an array of frame numbers instead, for example:
this.anims.generateFrameNumbers('explosion', { frames: [ 0, 1, 2, 1, 2, 3, 4, 0, 1, 2 ] })
Please see the animation examples and GenerateFrameNumbers config docs for further details.
Parameters:
name type optional description
key string No The key for the texture containing the animation frames.
config Phaser.Types.Animations.GenerateFrameNumbers Yes The configuration object for the animation frames.
Returns: Array.< Phaser.Types.Animations.AnimationFrame > - The array of {@link Phaser.Types.Animations.AnimationFrame} objects.
Source: src/animations/AnimationManager.js#L689
Since: 3.0.0
get ​
<instance> get(key) ​
Description:
Get an Animation.
Parameters:
name type optional description
key string No The key of the Animation to retrieve.
Returns: Phaser.Animations.Animation - The Animation.
Source: src/animations/AnimationManager.js#L793
Since: 3.0.0
getAnimsFromTexture ​
<instance> getAnimsFromTexture(key) ​
Description:
Returns an array of all Animation keys that are using the given
Texture. Only Animations that have at least one AnimationFrame
entry using this texture will be included in the result.
Parameters:
name type optional description
key string | Phaser.Textures.Texture Phaser.Textures.Frame No
Returns: Array.<string> - An array of Animation keys that feature the given Texture.
Source: src/animations/AnimationManager.js#L808
Since: 3.60.0
getMix ​
<instance> getMix(animA, animB) ​
Description:
Returns the mix delay between two animations.
If no mix has been set-up, this method will return zero.
If you wish to create, or update, a new mix, call the addMix method.
If you wish to remove a mix, call the removeMix method.
Parameters:
name type optional description
animA string | Phaser.Animations.Animation No The string-based key, or instance of, Animation A.
animB string | Phaser.Animations.Animation No The string-based key, or instance of, Animation B.
Returns: number - The mix duration, or zero if no mix exists.
Source: src/animations/AnimationManager.js#L241
Since: 3.50.0
pauseAll ​
<instance> pauseAll() ​
Description:
Pause all animations.
Returns: Phaser.Animations.AnimationManager - This Animation Manager.
Fires: Phaser.Animations.Events#event:PAUSE_ALL
Source: src/animations/AnimationManager.js#L848
Since: 3.0.0
play ​
<instance> play(key, children) ​
Description:
Play an animation on the given Game Objects that have an Animation Component.
Parameters:
name type optional description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
children Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to play the animation on. They must have an Animation Component.
Returns: Phaser.Animations.AnimationManager - This Animation Manager.
Source: src/animations/AnimationManager.js#L869
Since: 3.0.0
remove ​
<instance> remove(key) ​
Description:
Removes an Animation from this Animation Manager, based on the given key.
This is a global action. Once an Animation has been removed, no Game Objects
can carry on using it.
Parameters:
name type optional description
key string No The key of the animation to remove.
Returns: Phaser.Animations.Animation - The Animation instance that was removed from the Animation Manager.
Fires: Phaser.Animations.Events#event:REMOVE_ANIMATION
Source: src/animations/AnimationManager.js#L961
Since: 3.0.0
removeMix ​
<instance> removeMix(animA, [animB]) ​
Description:
Removes a mix between two animations.
Mixing allows you to specify a unique delay between a pairing of animations.
Calling this method lets you remove those pairings. You can either remove
it between animA and animB , or if you do not provide the animB parameter,
it will remove all animA mixes.
If you wish to update an existing mix instead, call the addMix method with the
new delay.
Parameters:
name type optional description
animA string | Phaser.Animations.Animation No The string-based key, or instance of, Animation A.
animB string | Phaser.Animations.Animation Yes The string-based key, or instance of, Animation B. If not given, all mixes for Animation A will be removed.
Returns: Phaser.Animations.AnimationManager - This Animation Manager.
Source: src/animations/AnimationManager.js#L191
Since: 3.50.0
resumeAll ​
<instance> resumeAll() ​
Description:
Resume all paused animations.
Returns: Phaser.Animations.AnimationManager - This Animation Manager.
Fires: Phaser.Animations.Events#event:RESUME_ALL
Source: src/animations/AnimationManager.js#L991
Since: 3.0.0
staggerPlay ​
<instance> staggerPlay(key, children, stagger, [staggerFirst]) ​
Description:
Takes an array of Game Objects that have an Animation Component and then
starts the given animation playing on them. The start time of each Game Object
is offset, incrementally, by the stagger amount.
For example, if you pass an array with 4 children and a stagger time of 1000,
the delays will be:
child 1: 1000ms delay
child 2: 2000ms delay
child 3: 3000ms delay
child 4: 4000ms delay
If you set the staggerFirst parameter to false they would be:
child 1: 0ms delay
child 2: 1000ms delay
child 3: 2000ms delay
child 4: 3000ms delay
You can also set stagger to be a negative value. If it was -1000, the above would be:
child 1: 3000ms delay
child 2: 2000ms delay
child 3: 1000ms delay
child 4: 0ms delay
Tags:
generic
Parameters:
name type optional default description
key string | Phaser.Animations.Animation Phaser.Types.Animations.PlayAnimationConfig No
children Phaser.GameObjects.GameObject | Array.< Phaser.GameObjects.GameObject > No An array of Game Objects to play the animation on. They must have an Animation Component.
stagger number No The amount of time, in milliseconds, to offset each play time by. If a negative value is given, it's applied to the children in reverse order.
staggerFirst boolean Yes true Should the first child be staggered as well?
Returns: Phaser.Animations.AnimationManager - This Animation Manager.
Source: src/animations/AnimationManager.js#L895
Since: 3.0.0
toJSON ​
<instance> toJSON([key]) ​
Description:
Returns the Animation data as JavaScript object based on the given key.
Or, if not key is defined, it will return the data of all animations as array of objects.
Parameters:
name type optional description
key string Yes The animation to get the JSONAnimation data from. If not provided, all animations are returned as an array.
Returns: Phaser.Types.Animations.JSONAnimations - The resulting JSONAnimations formatted object.
Source: src/animations/AnimationManager.js#L1012
Since: 3.0.0
Previous
AnimationFrame
Next
AnimationState
Public Members
anims
game
globalTimeScale
mixes
name
paused
textureManager
Inherited Methods
Public Methods
add
addMix
boot
create
createFromAseprite
destroy
exists
fromJSON
generateFrameNames
generateFrameNumbers
get
getAnimsFromTexture
getMix
pauseAll
play
remove
removeMix
resumeAll
staggerPlay
toJSON
