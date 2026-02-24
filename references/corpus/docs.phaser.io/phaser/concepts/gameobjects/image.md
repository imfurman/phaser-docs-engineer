# Image | Phaser Help

Source: https://docs.phaser.io/phaser/concepts/gameobjects/image

Concepts
Game Objects
Image
On this page
Image
An Image is a light-weight Game Object useful for the display of static images in your game, such as logos, backgrounds, scenery or other non-animated elements. Images can have input events and physics bodies, or be tweened, tinted or scrolled. The main difference between an Image and a Sprite is that you cannot animate an Image as they do not have the Animation component.
Load texture ​
this . load . image ( key , url ) ;
Reference: load image
Add image object ​
var image = this . add . image ( x , y , key ) ;
// var image = this.add.image(x, y, key, frame);
Add image from JSON
var image = this . make . image ( {
x : 0 ,
y : 0 ,
key : '' ,
// frame: '',
// angle: 0,
// alpha: 1,
// flipX: true,
// flipY: true,
// scale : {
// x: 1,
// y: 1
//},
// origin: {x: 0.5, y: 0.5},
add : true
} ) ;
key , frame :
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
class MyImage extends Phaser . GameObjects . Image {
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
var image = new MyImage ( scene , x , y , key ) ;
Texture ​
See game object - texture
Other properties ​
See game object
Create mask ​
var mask = image . createBitmapMask ( ) ;
See mask
Shader effects ​
Support preFX and postFX effects
Author Credits ​
Content on this page includes work by:
RexRainbow
Previous
Group
Next
Layer
Load texture
Add image object
Custom class
Texture
Other properties
Create mask
Shader effects
Author Credits
