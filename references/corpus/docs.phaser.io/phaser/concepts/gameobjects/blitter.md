# Blitter | Phaser Help

Source: https://docs.phaser.io/phaser/concepts/gameobjects/blitter

Concepts
Game Objects
Blitter
On this page
Blitter
The Blitter Game Object is a special kind of container that creates, updates and manages Bob objects. Bobs are designed for rendering speed rather than flexibility. They consist of a texture, or frame from a texture, a position and an alpha value. You cannot scale or rotate them. They use a batched drawing method for speed during rendering.
A Blitter Game Object has one texture bound to it. Bobs created by the Blitter can use any Frame from this Texture to render with, but they cannot use any other Texture. It is this single texture-bind that allows them their speed.
If you have a need to blast a large volume of frames around the screen then Blitter objects are well worth investigating. They are especially useful for using as a base for your own special effects systems.
Load texture ​
this . load . image ( key , url ) ;
Reference: load image
Add blitter container ​
Add blitter container
var blitter = this . add . blitter ( x , y , key ) ;
key : The key of the texture this Game Object will use for rendering. The Texture must already exist in the Texture Manager.
Add blitter container from JSON
var blitter = this . make . blitter ( {
x : 0 ,
y : 0 ,
key : '' ,
// angle: 0,
// alpha: 1
// flipX: true,
// flipY: true,
// origin: {x: 0.5, y: 0.5},
add : true
} ) ;
Custom class ​
class MyBlitter extends Phaser . GameObjects . Blitter {
constructor ( scene , x , y , texture , frame ) {
super ( scene , x , y , texture , frame ) ;
// ...
this . add . existing ( this ) ;
}
// ...
// preUpdate(time, delta) {}
}
this.add.existing(gameObject) : Adds an existing Game Object to this Scene.
If the Game Object renders, it will be added to the Display List.
If it has a preUpdate method, it will be added to the Update List.
Example
var blitter = new MyBlitter ( scene , x , y , key ) ;
Add bob object ​
var bob = blitter . create ( x , y ) ;
// var bob = blitter.create(x, y, frame, visible, index);
frame : The Frame the Bob will use. It must be part of the Texture the parent Blitter object is using.
visible : Should the created Bob render or not?
index : The position in the Blitters Display List to add the new Bob at. Defaults to the top of the list.
Add mutiple bob objects ​
var bobs = blitter . createMultiple ( quantity , frame , visible ) ;
quantity : The quantity of Bob objects to create.
Add bob object from callback ​
var bobs = blitter . createFromCallback ( callback , quantity , frame , visible ) ;
// var callback = function(bob, i){};
Get bob objects ​
var bobs = blitter . children . list ;
Clear all bob objects ​
blitter . clear ( ) ;
Bob object ​
A Bob has a position, alpha value and a frame from a texture that it uses to render with. You can also toggle the flipped and visible state of the Bob.
Position ​
Get
var x = bob . x ;
var y = bob . y ;
Set
bob . setPosition ( x , y ) ;
// bob.x = 0;
// bob.y = 0;
or
bob . reset ( x , y ) ;
// bob.reset(x, y, frame);
Frame ​
Get
var frame = bob . frame ;
frame : Frame object .
Set
bob . setFrame ( frame ) ;
Flip ​
Get
var flipX = bob . flipX ;
var flipY = bob . flipY ;
Set
bob . setFlip ( boolX , boolY ) ;
// bob.setFlipX(boolean);
// bob.setFlipY(boolean);
// bob.flipX = flipX;
// bob.flipY = flipY;
or
bob . resetFlip ( ) ; // bob.setFlip(false, false)
Visible ​
Get
var visible = bob . visible ;
Set
bob . setVisible ( boolean ) ;
// bob.visible = v;
Alpha ​
Get
var alpha = bob . alpha ;
Set
bob . setAlpha ( v ) ;
// bob.aplha = v;
Tint ​
Get
var tint = bob . tint ;
Set
bob . setTint ( tint ) ;
// bob.tint = tint;
tint : Tint value, between 0 and 0xffffff .
Destroy ​
bob . destroy ( ) ;
Data ​
var data = bob . data ; // {}
Other properties ​
See game object
Create mask ​
var mask = bob . createBitmapMask ( ) ;
See mask
Shader effects ​
Support postFX effects
!!! note No preFX effect support
Author Credits ​
Content on this page includes work by:
RexRainbow
Previous
Bitmap Text
Next
Container
Load texture
Add blitter container
Custom class
Add bob object
Add mutiple bob objects
Add bob object from callback
Get bob objects
Clear all bob objects
Bob object
Position
Frame
Flip
Visible
Alpha
Tint
Destroy
Data
Other properties
Create mask
Shader effects
Author Credits
