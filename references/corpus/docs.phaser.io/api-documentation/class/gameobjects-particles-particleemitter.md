# ParticleEmitter | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-particles-particleemitter

Phaser API Documentation
Class
ParticleEmitter
Version: Phaser v3.90.0
On this page
ParticleEmitter
A Particle Emitter is a special kind of Game Object that controls a pool of Particles .
Particle Emitters are created via a configuration object. The properties of this object
can be specified in a variety of formats, given you plenty of scope over the values they
return, leading to complex visual effects. Here are the different forms of configuration
value you can give:
An explicit static value: ​
x : 400
The x value will always be 400 when the particle is spawned.
A random value: ​
x : [ 100 , 200 , 300 , 400 ]
The x value will be one of the 4 elements in the given array, picked at random on emission.
A custom callback: ​
x : ( particle , key , t , value ) => {
return value + 50 ;
}
The x value is the result of calling this function. This is only used when the
particle is emitted, so it provides it's initial starting value. It is not used
when the particle is updated (see the onUpdate callback for that)
A start / end object: ​
This allows you to control the change in value between the given start and
end parameters over the course of the particles lifetime:
scale : { start : 0 , end : 1 }
The particle scale will start at 0 when emitted and ease to a scale of 1
over the course of its lifetime. You can also specify the ease function
used for this change (the default is Linear):
scale : { start : 0 , end : 1 , ease : 'bounce.out' }
A start / end random object: ​
The start and end object can have an optional random parameter.
This forces it to pick a random value between the two values and use
this as the starting value, then easing to the 'end' parameter over
its lifetime.
scale : { start : 4 , end : 0.5 , random : true }
The particle will start with a random scale between 0.5 and 4 and then
scale to the end value over its lifetime. You can combine the above
with the ease parameter as well to control the value easing.
An interpolation object: ​
You can provide an array of values which will be used for interpolation
during the particles lifetime. You can also define the interpolation
function to be used. There are three provided: linear (the default),
bezier and catmull , or you can provide your own function.
x : { values : [ 50 , 500 , 200 , 800 ] , interpolation : 'catmull' }
The particle scale will interpolate from 50 when emitted to 800 via the other
points over the course of its lifetime. You can also specify an ease function
used to control the rate of change through the values (the default is Linear):
x : { values : [ 50 , 500 , 200 , 800 ] , interpolation : 'catmull' , ease : 'bounce . out }
A stepped emitter object: ​
The steps parameter allows you to control the placement of sequential
particles across the start-end range:
x : { steps : 32 , start : 0 , end : 576 }
Here we have a range of 576 (start to end). This is divided into 32 steps.
The first particle will emit at the x position of 0. The next will emit
at the next 'step' along, which would be 18. The following particle will emit
at the next step, which is 36, and so on. Because the range of 576 has been
divided by 32, creating 18 pixels steps. When a particle reaches the 'end'
value the next one will start from the beginning again.
A stepped emitter object with yoyo: ​
You can add the optional yoyo property to a stepped object:
x : { steps : 32 , start : 0 , end : 576 , yoyo : true }
As with the stepped emitter, particles are emitted in sequence, from 'start'
to 'end' in step sized jumps. Normally, when a stepped emitter reaches the
end it snaps around to the start value again. However, if you provide the 'yoyo'
parameter then when it reaches the end it will reverse direction and start
emitting back down to 'start' again. Depending on the effect you require this
can often look better.
A min / max object: ​
This allows you to pick a random float value between the min and max properties:
x : { min : 100 , max : 700 }
The x value will be a random float between min and max.
You can force it select an integer by setting the 'int' flag:
x : { min : 100 , max : 700 , int : true }
Or, you could use the 'random' array approach (see below)
A random object: ​
This allows you to pick a random integer value between the first and second array elements:
x : { random : [ 100 , 700 ] }
The x value will be a random integer between 100 and 700 as it takes the first
element in the 'random' array as the 'min' value and the 2nd element as the 'max' value.
Custom onEmit and onUpdate callbacks: ​
If the above won't give you the effect you're after, you can provide your own
callbacks that will be used when the particle is both emitted and updated:
x : {
onEmit : ( particle , key , t , value ) => {
return value ;
} ,
onUpdate : ( particle , key , t , value ) => {
return value ;
}
}
You can provide either one or both functions. The onEmit is called at the
start of the particles life and defines the value of the property on birth.
The onUpdate function is called every time the Particle Emitter updates
until the particle dies. Both must return a value.
The properties are:
particle - A reference to the Particle instance.
key - The string based key of the property, i.e. 'x' or 'lifespan'.
t - The current normalized lifetime of the particle, between 0 (birth) and 1 (death).
value - The current property value. At a minimum you should return this.
By using the above configuration options you have an unlimited about of
control over how your particles behave.
v3.55 Differences ​
Prior to v3.60 Phaser used a ParticleEmitterManager . This was removed in v3.60
and now calling this.add.particles returns a ParticleEmitter instance instead.
In order to streamline memory and the display list we have removed the
ParticleEmitterManager entirely. When you call this.add.particles you're now
creating a ParticleEmitter instance, which is being added directly to the
display list and can be manipulated just like any other Game Object, i.e.
scaled, rotated, positioned, added to a Container, etc. It now extends the
GameObject base class, meaning it's also an event emitter, which allowed us
to create some handy new events for particles.
So, to create an emitter, you now give it an xy coordinate, a texture and an
emitter configuration object (you can also set this later, but most commonly
you'd do it on creation). I.e.:
const emitter = this . add . particles ( 100 , 300 , 'flares' , {
frame : 'red' ,
angle : { min : - 30 , max : 30 } ,
speed : 150
} ) ;
This will create a 'red flare' emitter at 100 x 300.
Please update your code to ensure it adheres to the new function signatures.
Constructor
new ParticleEmitter(scene, [x], [y], [texture], [config])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes The horizontal position of this Game Object in the world.
y number Yes The vertical position of this Game Object in the world.
texture string | Phaser.Textures.Texture Yes The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager.
config Phaser.Types.GameObjects.Particles.ParticleEmitterConfig Yes Settings for this emitter.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Texture
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/particles/ParticleEmitter.js#L105
Since: 3.60.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Pipeline :
defaultPipeline
pipeline
pipelineData
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
From Phaser.GameObjects.Components.Texture :
frame
texture
From Phaser.GameObjects.Components.Transform :
angle
hasTransformComponent
rotation
scale
scaleX
scaleY
w
x
y
z
From Phaser.GameObjects.Components.Visible :
visible
From Phaser.GameObjects.GameObject :
active
body
cameraFilter
data
displayList
ignoreDestroy
input
name
parentContainer
renderFlags
scene
state
tabIndex
type
Public Members ​
acceleration ​
acceleration: boolean ​
Description:
Whether accelerationX and accelerationY are non-zero. Set automatically during configuration.
Source: src/gameobjects/particles/ParticleEmitter.js#L459
Since: 3.0.0
accelerationX ​
accelerationX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The horizontal acceleration applied to emitted particles, in pixels per second squared.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3097
Since: 3.60.0
accelerationY ​
accelerationY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The vertical acceleration applied to emitted particles, in pixels per second squared.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3121
Since: 3.60.0
animCounter ​
animCounter: number ​
Description:
The internal animation counter.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3739
Since: 3.60.0
animQuantity ​
animQuantity: number ​
Description:
The number of consecutive particles that receive a single animation (per frame cycle).
Source: src/gameobjects/particles/ParticleEmitter.js#L785
Since: 3.60.0
anims ​
anims: Array.<string> ​
Description:
The animations assigned to particles.
Source: src/gameobjects/particles/ParticleEmitter.js#L765
Since: 3.60.0
bounce ​
bounce: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The amount of velocity particles will use when rebounding off the
emitter bounds, if set. A value of 0 means no bounce. A value of 1
means a full rebound.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3321
Since: 3.60.0
colorEase ​
colorEase: string ​
Description:
Controls the easing function used when you have created an
Emitter that uses the color property to interpolate the
tint of Particles over their lifetime.
Setting this has no effect if you haven't also applied a
particleColor to this Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L3438
Since: 3.60.0
completeFlag ​
completeFlag: boolean ​
Description:
The internal complete flag.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3808
Since: 3.60.0
config ​
config: Phaser.Types.GameObjects.Particles.ParticleEmitterConfig ​
Description:
An internal object holding the configuration for the Emitter.
These are populated as part of the Emitter configuration parsing.
You typically do not access them directly, but instead use the
ParticleEmitter.setConfig or ParticleEmitter.updateConfig methods.
Source: src/gameobjects/particles/ParticleEmitter.js#L373
Since: 3.85.0
currentAnim ​
currentAnim: number ​
Description:
The current animation index.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3900
Since: 3.60.0
currentFrame ​
currentFrame: number ​
Description:
The current frame index.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3877
Since: 3.60.0
deathCallback ​
deathCallback: Phaser.Types.GameObjects.Particles.ParticleDeathCallback ​
Description:
A function to call when a particle dies.
Source: src/gameobjects/particles/ParticleEmitter.js#L502
Since: 3.0.0
deathCallbackScope ​
deathCallbackScope: * ​
Description:
The calling context for Phaser.GameObjects.Particles.ParticleEmitter#deathCallback .
Source: src/gameobjects/particles/ParticleEmitter.js#L512
Since: 3.0.0
deathZones ​
deathZones: Array.< Phaser.GameObjects.Particles.Zones.DeathZone > ​
Description:
An array containing Particle Death Zone objects. A particle is immediately killed as soon as its x/y coordinates
intersect with any of the configured Death Zones.
Prior to Phaser v3.60 an Emitter could only have one single Death Zone.
In 3.60 they can now have an array of Death Zones.
Source: src/gameobjects/particles/ParticleEmitter.js#L661
Since: 3.60.0
delay ​
delay: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The number of milliseconds to wait after emission before
the particles start updating. This allows you to emit particles
that appear 'static' or still on-screen and then, after this value,
begin to move.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3636
Since: 3.60.0
duration ​
duration: number ​
Description:
The number of milliseconds this emitter will emit particles for when in flow mode,
before it stops emission. A value of 0 (the default) means there is no duration.
When the duration expires the STOP event is emitted. Note that entering a
stopped state doesn't mean all the particles have finished, just that it's
not emitting any further ones.
To know when the final particle expires, listen for the COMPLETE event.
The counter is reset each time the ParticleEmitter.start method is called.
0 means the emitter will not stop based on duration.
Source: src/gameobjects/particles/ParticleEmitter.js#L572
Since: 3.60.0
elapsed ​
elapsed: number ​
Description:
The internal elasped counter.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3762
Since: 3.60.0
emitCallback ​
emitCallback: Phaser.Types.GameObjects.Particles.ParticleEmitterCallback ​
Description:
A function to call when a particle is emitted.
Source: src/gameobjects/particles/ParticleEmitter.js#L482
Since: 3.0.0
emitCallbackScope ​
emitCallbackScope: * ​
Description:
The calling context for Phaser.GameObjects.Particles.ParticleEmitter#emitCallback .
Source: src/gameobjects/particles/ParticleEmitter.js#L492
Since: 3.0.0
emitting ​
emitting: boolean ​
Description:
Controls if the emitter is currently emitting a particle flow (when frequency >= 0).
Already alive particles will continue to update until they expire.
Controlled by Phaser.GameObjects.Particles.ParticleEmitter#start and Phaser.GameObjects.Particles.ParticleEmitter#stop .
Source: src/gameobjects/particles/ParticleEmitter.js#L608
Since: 3.0.0
emitZones ​
emitZones: Array.< Phaser.Types.GameObjects.Particles.EmitZoneObject > ​
Description:
An array containing Particle Emission Zones. These can be either EdgeZones or RandomZones.
Particles are emitted from a randomly selected zone from this array.
Prior to Phaser v3.60 an Emitter could only have one single Emission Zone.
In 3.60 they can now have an array of Emission Zones.
Source: src/gameobjects/particles/ParticleEmitter.js#L646
Since: 3.60.0
flowCounter ​
flowCounter: number ​
Description:
The internal flow counter.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3693
Since: 3.60.0
follow ​
follow: Phaser.Types.Math.Vector2Like ​
Description:
A Game Object whose position is used as the particle origin.
Source: src/gameobjects/particles/ParticleEmitter.js#L700
Since: 3.0.0
followOffset ​
followOffset: Phaser.Math.Vector2 ​
Description:
The offset of the particle origin from the Phaser.GameObjects.Particles.ParticleEmitter#follow target.
Source: src/gameobjects/particles/ParticleEmitter.js#L712
Since: 3.0.0
frameCounter ​
frameCounter: number ​
Description:
The internal frame counter.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3716
Since: 3.60.0
frameQuantity ​
frameQuantity: number ​
Description:
The number of consecutive particles that receive a single texture frame (per frame cycle).
Source: src/gameobjects/particles/ParticleEmitter.js#L754
Since: 3.0.0
frames ​
frames: Array.< Phaser.Textures.Frame > ​
Description:
The texture frames assigned to particles.
Source: src/gameobjects/particles/ParticleEmitter.js#L734
Since: 3.0.0
frequency ​
frequency: number ​
Description:
For a flow emitter, the time interval (>= 0) between particle flow cycles in ms.
A value of 0 means there is one particle flow cycle for each logic update (the maximum flow frequency). This is the default setting.
For an exploding emitter, this value will be -1.
Calling Phaser.GameObjects.Particles.ParticleEmitter#flow also puts the emitter in flow mode (frequency >= 0).
Calling Phaser.GameObjects.Particles.ParticleEmitter#explode also puts the emitter in explode mode (frequency = -1).
Source: src/gameobjects/particles/ParticleEmitter.js#L593
Since: 3.0.0
gravityX ​
gravityX: number ​
Description:
Horizontal acceleration applied to emitted particles, in pixels per second squared.
Source: src/gameobjects/particles/ParticleEmitter.js#L437
Since: 3.0.0
gravityY ​
gravityY: number ​
Description:
Vertical acceleration applied to emitted particles, in pixels per second squared.
Source: src/gameobjects/particles/ParticleEmitter.js#L448
Since: 3.0.0
hold ​
hold: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The number of milliseconds to wait after a particle has finished
its life before it will be removed. This allows you to 'hold' a
particle on the screen once it has reached its final state
before it then vanishes.
Note that all particle updates will cease, including changing
alpha, scale, movement or animation.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3663
Since: 3.60.0
lifespan ​
lifespan: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The lifespan of the emitted particles. This value is given
in milliseconds and defaults to 1000ms (1 second). When a
particle reaches this amount it is killed.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3527
Since: 3.60.0
maxAliveParticles ​
maxAliveParticles: number ​
Description:
The maximum number of alive and rendering particles this emitter will update.
When this limit is reached, a particle needs to die before another can be emitted.
0 means no limits.
Source: src/gameobjects/particles/ParticleEmitter.js#L536
Since: 3.60.0
maxParticles ​
maxParticles: number ​
Description:
Set to hard limit the amount of particle objects this emitter is allowed to create
in total. This is the number of Particle instances it can create, not the number
of 'alive' particles.
0 means unlimited.
Source: src/gameobjects/particles/ParticleEmitter.js#L522
Since: 3.0.0
maxVelocityX ​
maxVelocityX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The maximum horizontal velocity emitted particles can reach, in pixels per second squared.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3145
Since: 3.60.0
maxVelocityY ​
maxVelocityY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The maximum vertical velocity emitted particles can reach, in pixels per second squared.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3170
Since: 3.60.0
moveTo ​
moveTo: boolean ​
Description:
Whether moveToX and moveToY are set. Set automatically during configuration.
When true the particles move toward the moveToX and moveToY coordinates and arrive at the end of their life.
Emitter angle, speedX, and speedY are ignored.
Source: src/gameobjects/particles/ParticleEmitter.js#L469
Since: 3.0.0
moveToX ​
moveToX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The x coordinate emitted particles move toward, when Phaser.GameObjects.Particles.ParticleEmitter#moveTo is true.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3273
Since: 3.60.0
moveToY ​
moveToY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The y coordinate emitted particles move toward, when Phaser.GameObjects.Particles.ParticleEmitter#moveTo is true.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3297
Since: 3.60.0
ops ​
ops: Phaser.Types.GameObjects.Particles.ParticleEmitterOps ​
Description:
An internal object holding all of the EmitterOp instances.
These are populated as part of the Emitter configuration parsing.
You typically do not access them directly, but instead use the
provided getters and setters on this class, such as ParticleEmitter.speedX etc.
Source: src/gameobjects/particles/ParticleEmitter.js#L387
Since: 3.60.0
particleAlpha ​
particleAlpha: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The alpha value of the emitted particles. This is a value
between 0 and 1. Particles with alpha zero are invisible
and are therefore not rendered, but are still processed
by the Emitter.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3500
Since: 3.60.0
particleAngle ​
particleAngle: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The angle at which the particles are emitted. The values are
given in degrees. This allows you to control the direction
of the emitter. If you wish instead to change the rotation
of the particles themselves, see the particleRotate property.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3553
Since: 3.60.0
particleBringToTop ​
particleBringToTop: boolean ​
Description:
Newly emitted particles are added to the top of the particle list, i.e. rendered above those already alive.
Set to false to send them to the back.
Also see the sortOrder property for more complex particle sorting.
Source: src/gameobjects/particles/ParticleEmitter.js#L622
Since: 3.0.0
particleClass ​
particleClass: function ​
Description:
The Particle Class which will be emitted by this Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L362
Since: 3.0.0
particleColor ​
particleColor: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
A color tint value that is applied to the texture of the emitted
particle. The value should be given in hex format, i.e. 0xff0000
for a red tint, and should not include the alpha channel.
Tints are additive, meaning a tint value of white (0xffffff) will
effectively reset the tint to nothing.
Modify the ParticleEmitter.tintFill property to change between
an additive and replacement tint mode.
When you define the color via the Emitter config you should give
it as an array of color values. The Particle will then interpolate
through these colors over the course of its lifespan. Setting this
will override any tint value that may also be given.
This is a WebGL only feature.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3399
Since: 3.60.0
particleRotate ​
particleRotate: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The rotation (or angle) of each particle when it is emitted.
The value is given in degrees and uses a right-handed
coordinate system, where 0 degrees points to the right, 90 degrees
points down and -90 degrees points up.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3580
Since: 3.60.0
particleScaleX ​
particleScaleX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The horizontal scale of emitted particles.
This is relative to the Emitters scale and that of any parent.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3347
Since: 3.60.0
particleScaleY ​
particleScaleY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The vertical scale of emitted particles.
This is relative to the Emitters scale and that of any parent.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3373
Since: 3.60.0
particleTint ​
particleTint: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
A color tint value that is applied to the texture of the emitted
particle. The value should be given in hex format, i.e. 0xff0000
for a red tint, and should not include the alpha channel.
Tints are additive, meaning a tint value of white (0xffffff) will
effectively reset the tint to nothing.
Modify the ParticleEmitter.tintFill property to change between
an additive and replacement tint mode.
The tint value will be overriden if a color array is provided.
This is a WebGL only feature.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3464
Since: 3.60.0
particleX ​
particleX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType , Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType ​
Description:
The x coordinate the particles are emitted from.
This is relative to the Emitters x coordinate and that of any parent.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3045
Since: 3.60.0
particleY ​
particleY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType , Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType ​
Description:
The y coordinate the particles are emitted from.
This is relative to the Emitters x coordinate and that of any parent.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3071
Since: 3.60.0
processors ​
processors: Phaser.Structs.List.<Phaser.GameObjects.Particles.ParticleProcessor> ​
Description:
A list of Particle Processors being managed by this Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L891
Since: 3.60.0
quantity ​
quantity: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The number of particles that are emitted each time an emission
occurs, i.e. from one 'explosion' or each frame in a 'flow' cycle.
The default is 1.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3607
Since: 3.60.0
radial ​
radial: boolean ​
Description:
A radial emitter will emit particles in all directions between angle min and max,
using Phaser.GameObjects.Particles.ParticleEmitter#speed as the value. If set to false then this acts as a point Emitter.
A point emitter will emit particles only in the direction derived from the speedX and speedY values.
Source: src/gameobjects/particles/ParticleEmitter.js#L424
Since: 3.0.0
randomAnim ​
randomAnim: boolean ​
Description:
Whether animations Phaser.GameObjects.Particles.ParticleEmitter#anims are selected at random.
Source: src/gameobjects/particles/ParticleEmitter.js#L774
Since: 3.60.0
randomFrame ​
randomFrame: boolean ​
Description:
Whether texture Phaser.GameObjects.Particles.ParticleEmitter#frames are selected at random.
Source: src/gameobjects/particles/ParticleEmitter.js#L743
Since: 3.0.0
skipping ​
skipping: boolean ​
Description:
An internal property used to tell when the emitter is in fast-forwarc mode.
Source: src/gameobjects/particles/ParticleEmitter.js#L837
Since: 3.60.0
sortCallback ​
sortCallback: Phaser.Types.GameObjects.Particles.ParticleSortCallback ​
Description:
The callback used to sort the particles. Only used if sortProperty
has been set. Set this via the setSortCallback method.
Source: src/gameobjects/particles/ParticleEmitter.js#L881
Since: 3.60.0
sortOrderAsc ​
sortOrderAsc: boolean ​
Description:
When sortProperty is defined this controls the sorting order,
either ascending or descending. Toggle to control the visual effect.
Source: src/gameobjects/particles/ParticleEmitter.js#L871
Since: 3.60.0
sortProperty ​
sortProperty: string ​
Description:
Optionally sort the particles before they render based on this
property. The property must exist on the Particle class, such
as y , lifeT , scaleX , etc.
When set this overrides the particleBringToTop setting.
To reset this and disable sorting, so this property to an empty string.
Source: src/gameobjects/particles/ParticleEmitter.js#L856
Since: 3.60.0
speed ​
speed: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The initial speed of emitted particles, in pixels per second.
If using this as a getter it will return the speedX value.
If using it as a setter it will update both speedX and speedY to the
given value.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3195
Since: 3.60.0
speedX ​
speedX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The initial horizontal speed of emitted particles, in pixels per second.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3225
Since: 3.60.0
speedY ​
speedY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType ​
Description:
The initial vertical speed of emitted particles, in pixels per second.
Accessing this property should typically return a number.
However, it can be set to any valid EmitterOp onEmit type.
Source: src/gameobjects/particles/ParticleEmitter.js#L3249
Since: 3.60.0
stopAfter ​
stopAfter: number ​
Description:
If set, either via the Emitter config, or by directly setting this property,
the Particle Emitter will stop emitting particles once this total has been
reached. It will then enter a 'stopped' state, firing the STOP
event. Note that entering a stopped state doesn't mean all the particles
have finished, just that it's not emitting any further ones.
To know when the final particle expires, listen for the COMPLETE event.
Use this if you wish to launch an exact number of particles and then stop
your emitter afterwards.
The counter is reset each time the ParticleEmitter.start method is called.
0 means the emitter will not stop based on total emitted particles.
Source: src/gameobjects/particles/ParticleEmitter.js#L549
Since: 3.60.0
stopCounter ​
stopCounter: number ​
Description:
The internal stop counter.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3785
Since: 3.60.0
timeScale ​
timeScale: number ​
Description:
The time rate applied to active particles, affecting lifespan, movement, and tweens. Values larger than 1 are faster than normal.
Source: src/gameobjects/particles/ParticleEmitter.js#L636
Since: 3.0.0
tintFill ​
tintFill: boolean ​
Description:
The tint fill mode used by the Particles in this Emitter.
false = An additive tint (the default), where vertices colors are blended with the texture.
true = A fill tint, where the vertices colors replace the texture, but respects texture alpha.
Source: src/gameobjects/particles/ParticleEmitter.js#L900
Since: 3.60.0
trackVisible ​
trackVisible: boolean ​
Description:
Whether the emitter's Phaser.GameObjects.Particles.ParticleEmitter#visible state will track
the Phaser.GameObjects.Particles.ParticleEmitter#follow target's visibility state.
Source: src/gameobjects/particles/ParticleEmitter.js#L722
Since: 3.0.0
viewBounds ​
viewBounds: Phaser.Geom.Rectangle ​
Description:
An optional Rectangle object that is used during rendering to cull Particles from
display. For example, if your particles are limited to only move within a 300x300
sized area from their origin, then you can set this Rectangle to those dimensions.
The renderer will check to see if the viewBounds Rectangle intersects with the
Camera bounds during the render step and if not it will skip rendering the Emitter
entirely.
This allows you to create many emitters in a Scene without the cost of
rendering if the contents aren't visible.
Note that the Emitter will not perform any checks to see if the Particles themselves
are outside of these bounds, or not. It will simply check the bounds against the
camera. Use the getBounds method with the advance parameter to help define
the location and placement of the view bounds.
Source: src/gameobjects/particles/ParticleEmitter.js#L675
Since: 3.60.0
worldMatrix ​
worldMatrix: Phaser.GameObjects.Components.TransformMatrix ​
Description:
An internal Transform Matrix used to cache this emitters world matrix.
Source: src/gameobjects/particles/ParticleEmitter.js#L847
Since: 3.60.0
zoneIndex ​
zoneIndex: number ​
Description:
The internal zone index.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3831
Since: 3.60.0
zoneTotal ​
zoneTotal: number ​
Description:
The internal zone total.
Treat this property as read-only.
Source: src/gameobjects/particles/ParticleEmitter.js#L3854
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
From Phaser.GameObjects.Components.AlphaSingle :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.Pipeline :
getPipelineName
initPipeline
resetPipeline
setPipeline
setPipelineData
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
From Phaser.GameObjects.Components.Texture :
setFrame
setTexture
From Phaser.GameObjects.Components.Transform :
copyPosition
getLocalPoint
getLocalTransformMatrix
getParentRotation
getWorldPoint
getWorldTransformMatrix
setAngle
setPosition
setRandomPosition
setRotation
setScale
setW
setX
setY
setZ
From Phaser.GameObjects.Components.Visible :
setVisible
From Phaser.GameObjects.GameObject :
addedToScene
addToDisplayList
addToUpdateList
destroy
disableInteractive
getData
getDisplayList
getIndexList
incData
removedFromScene
removeFromDisplayList
removeFromUpdateList
removeInteractive
setActive
setData
setDataEnabled
setInteractive
setName
setState
toggleData
update
willRender
Public Methods ​
addDeathZone ​
<instance> addDeathZone(config) ​
Description:
Adds a new Particle Death Zone to this Emitter.
A particle is immediately killed as soon as its x/y coordinates intersect
with any of the configured Death Zones.
The source can be a Geometry Shape, such as a Circle, Rectangle or Triangle.
Any valid object from the Phaser.Geometry namespace is allowed, as long as
it supports a contains function. You can set the type to be either onEnter
or onLeave .
A single Death Zone instance can only exist once within this Emitter, but can belong
to multiple Emitters.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Particles.DeathZoneObject | Array.< Phaser.Types.GameObjects.Particles.DeathZoneObject > No A Death Zone configuration object, a Death Zone instance, a valid Geometry object or an array of them.
Returns: Array.< Phaser.GameObjects.Particles.Zones.DeathZone > - An array of the Death Zones that were added to this Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1706
Since: 3.60.0
addEmitZone ​
<instance> addEmitZone(zone) ​
Description:
Adds a new Particle Emission Zone to this Emitter.
An EdgeZone places particles on its edges.
Its source can be a Curve, Path, Circle, Ellipse, Line, Polygon, Rectangle, or Triangle;
or any object with a suitable getPoints method.
A RandomZone places the particles randomly within its interior.
Its source can be a Circle, Ellipse, Line, Polygon, Rectangle, or Triangle; or any object with a suitable getRandomPoint method.
An Emission Zone can only exist once within this Emitter.
Parameters:
name type optional description
zone Phaser.Types.GameObjects.Particles.EmitZoneData | Array.< Phaser.Types.GameObjects.Particles.EmitZoneData > No An Emission Zone configuration object, a RandomZone or EdgeZone instance, or an array of them.
Returns: Array.< Phaser.Types.GameObjects.Particles.EmitZoneObject > - An array of the Emission Zones that were added to this Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1804
Since: 3.60.0
addParticleBounds ​
<instance> addParticleBounds(x, [y], [width], [height], [collideLeft], [collideRight], [collideTop], [collideBottom]) ​
Description:
Creates a Particle Bounds processor and adds it to this Emitter.
This processor will check to see if any of the active Particles hit
the defined boundary, as specified by a Rectangle shape in world-space.
If so, they are 'rebounded' back again by having their velocity adjusted.
The strength of the rebound is controlled by the Particle.bounce
property.
You should be careful to ensure that you emit particles within a bounds,
if set, otherwise it will lead to unpredictable visual results as the
particles are hastily repositioned.
The Particle Bounds processor is returned from this method. If you wish
to modify the area you can directly change its bounds property, along
with the collideLeft etc values.
To disable the bounds you can either set its active property to false ,
or if you no longer require it, call ParticleEmitter.removeParticleProcessor .
Parameters:
name type optional default description
x number | Phaser.Types.GameObjects.Particles.ParticleEmitterBounds Phaser.Types.GameObjects.Particles.ParticleEmitterBoundsAlt No
y number Yes The y-coordinate of the top edge of the boundary.
width number Yes The width of the boundary.
height number Yes The height of the boundary.
collideLeft boolean Yes true Whether particles interact with the left edge of the bounds.
collideRight boolean Yes true Whether particles interact with the right edge of the bounds.
collideTop boolean Yes true Whether particles interact with the top edge of the bounds.
collideBottom boolean Yes true Whether particles interact with the bottom edge of the bounds.
Returns: Phaser.GameObjects.Particles.ParticleBounds - The Particle Bounds processor.
Source: src/gameobjects/particles/ParticleEmitter.js#L1460
Since: 3.60.0
addParticleProcessor ​
<instance> addParticleProcessor(processor) ​
Description:
Adds a Particle Processor, such as a Gravity Well, to this Emitter.
It will start processing particles from the next update as long as its active
property is set.
Tags:
generic
Parameters:
name type optional description
processor T No The Particle Processor to add to this Emitter Manager.
Returns: T - The Particle Processor that was added to this Emitter Manager.
Source: src/gameobjects/particles/ParticleEmitter.js#L2035
Since: 3.60.0
atLimit ​
<instance> atLimit() ​
Description:
Whether this emitter is at either its hard-cap limit (maxParticles), if set, or
the max allowed number of 'alive' particles (maxAliveParticles).
Returns: boolean - Returns true if this Emitter is at its limit, or false if no limit, or below the maxParticles level.
Source: src/gameobjects/particles/ParticleEmitter.js#L2196
Since: 3.0.0
clearDeathZones ​
<instance> clearDeathZones() ​
Description:
Clear all Death Zones from this Particle Emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1789
Since: 3.70.0
clearEmitZones ​
<instance> clearEmitZones() ​
Description:
Clear all Emission Zones from this Particle Emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1899
Since: 3.70.0
createEmitter ​
<instance> createEmitter() ​
Description:
Prints a warning to the console if you mistakenly call this function
thinking it works the same way as Phaser v3.55.
Source: src/gameobjects/particles/ParticleEmitter.js#L3033
Since: 3.60.0
createGravityWell ​
<instance> createGravityWell(config) ​
Description:
Creates a new Gravity Well, adds it to this Emitter and returns a reference to it.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Particles.GravityWellConfig No Configuration settings for the Gravity Well to create.
Returns: Phaser.GameObjects.Particles.GravityWell - The Gravity Well that was created.
Source: src/gameobjects/particles/ParticleEmitter.js#L2107
Since: 3.60.0
depthSort ​
<instance> depthSort() ​
Description:
Sorts active particles with Phaser.GameObjects.Particles.ParticleEmitter#depthSortCallback .
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2533
Since: 3.0.0
depthSortCallback ​
<instance> depthSortCallback(a, b) ​
Description:
Calculates the difference of two particles, for sorting them by depth.
Parameters:
name type optional description
a object No The first particle.
b object No The second particle.
Returns: number - The difference of a and b's y coordinates.
Source: src/gameobjects/particles/ParticleEmitter.js#L2548
Since: 3.0.0
emitParticle ​
<instance> emitParticle([count], [x], [y]) ​
Description:
Emits particles at a given position (or the emitters current position).
Parameters:
name type optional default description
count number Yes "this.quantity" The number of Particles to emit.
x number Yes "this.x" The x coordinate to emit the Particles from.
y number Yes "this.x" The y coordinate to emit the Particles from.
Returns: Phaser.GameObjects.Particles.Particle , undefined - The most recently emitted Particle, or undefined if the emitter is at its limit.
Source: src/gameobjects/particles/ParticleEmitter.js#L2649
Since: 3.0.0
emitParticleAt ​
<instance> emitParticleAt([x], [y], [count]) ​
Description:
Emits particles at the given position. If no position is given, it will
emit from this Emitters current location.
Parameters:
name type optional default description
x number Yes "this.x" The x coordinate to emit the Particles from.
y number Yes "this.x" The y coordinate to emit the Particles from.
count number Yes "this.quantity" The number of Particles to emit.
Returns: Phaser.GameObjects.Particles.Particle , undefined - The most recently emitted Particle, or undefined if the emitter is at its limit.
Source: src/gameobjects/particles/ParticleEmitter.js#L2631
Since: 3.0.0
explode ​
<instance> explode([count], [x], [y]) ​
Description:
Puts the emitter in explode mode (frequency = -1), stopping any current particle flow, and emits several particles all at once.
Parameters:
name type optional default description
count number Yes "this.quantity" The number of Particles to emit.
x number Yes "this.x" The x coordinate to emit the Particles from.
y number Yes "this.x" The y coordinate to emit the Particles from.
Returns: Phaser.GameObjects.Particles.Particle , undefined - The most recently emitted Particle, or undefined if the emitter is at its limit.
Fires: Phaser.GameObjects.Particles.Events#event:EXPLODE
Source: src/gameobjects/particles/ParticleEmitter.js#L2605
Since: 3.0.0
fastForward ​
<instance> fastForward(time, [delta]) ​
Description:
Fast forwards this Particle Emitter and all of its particles.
Works by running the Emitter preUpdate handler in a loop until the time
has been reached at delta steps per loop.
All callbacks and emitter related events that would normally be fired
will still be invoked.
You can make an emitter 'fast forward' via the emitter config using the
advance property. Set this value to the number of ms you wish the
emitter to be fast-forwarded by. Or, call this method post-creation.
Parameters:
name type optional description
time number No The number of ms to advance the Particle Emitter by.
delta number Yes The amount of delta to use for each step. Defaults to 1000 / 60.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2730
Since: 3.60.0
flow ​
<instance> flow(frequency, [count], [stopAfter]) ​
Description:
Puts the emitter in flow mode (frequency >= 0) and starts (or restarts) a particle flow.
To resume a flow at the current frequency and quantity, use Phaser.GameObjects.Particles.ParticleEmitter#start instead.
Parameters:
name type optional default description
frequency number No The time interval (>= 0) of each flow cycle, in ms.
count Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType Yes 1 The number of particles to emit at each flow cycle.
stopAfter number Yes Stop this emitter from firing any more particles once this value is reached. Set to zero for unlimited. Setting this parameter will override any stopAfter value already set in the Emitter configuration object.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Fires: Phaser.GameObjects.Particles.Events#event:START
Source: src/gameobjects/particles/ParticleEmitter.js#L2573
Since: 3.0.0
forEachAlive ​
<instance> forEachAlive(callback, context) ​
Description:
Calls a function for each active particle in this emitter. The function is
sent two parameters: a reference to the Particle instance and to this Emitter.
Parameters:
name type optional description
callback Phaser.Types.GameObjects.Particles.ParticleEmitterCallback No The function.
context * No The functions calling context.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2302
Since: 3.0.0
forEachDead ​
<instance> forEachDead(callback, context) ​
Description:
Calls a function for each inactive particle in this emitter.
Parameters:
name type optional description
callback Phaser.Types.GameObjects.Particles.ParticleEmitterCallback No The function.
context * No The functions calling context.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2328
Since: 3.0.0
getAliveParticleCount ​
<instance> getAliveParticleCount() ​
Description:
Gets the number of active (in-use) particles in this emitter.
Returns: number - The number of particles with active=true .
Source: src/gameobjects/particles/ParticleEmitter.js#L2157
Since: 3.0.0
getAnim ​
<instance> getAnim() ​
Description:
Chooses an animation from Phaser.GameObjects.Particles.ParticleEmitter#anims , if populated.
Returns: string - The animation to play, or null if there aren't any.
Source: src/gameobjects/particles/ParticleEmitter.js#L1333
Since: 3.60.0
getBounds ​
<instance> getBounds([padding], [advance], [delta], [output]) ​
Description:
Returns a bounds Rectangle calculated from the bounds of all currently
active Particles in this Emitter. If this Emitter has only just been
created and not yet rendered, then calling this method will return a Rectangle
with a max safe integer for dimensions. Use the advance parameter to
avoid this.
Typically it takes a few seconds for a flow Emitter to 'warm up'. You can
use the advance and delta parameters to force the Emitter to
'fast forward' in time to try and allow the bounds to be more accurate,
as it will calculate the bounds based on the particle bounds across all
timesteps, giving a better result.
You can also use the padding parameter to increase the size of the
bounds. Emitters with a lot of randomness in terms of direction or lifespan
can often return a bounds smaller than their possible maximum. By using
the padding (and advance if needed) you can help limit this.
Parameters:
name type optional description
padding number Yes The amount of padding, in pixels, to add to the bounds Rectangle.
advance number Yes The number of ms to advance the Particle Emitter by. Defaults to 0, i.e. not used.
delta number Yes The amount of delta to use for each step. Defaults to 1000 / 60.
output Phaser.Geom.Rectangle Yes The Rectangle to store the results in. If not given a new one will be created.
Returns: Phaser.Geom.Rectangle - A Rectangle containing the calculated bounds of this Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2931
Since: 3.60.0
getDeadParticleCount ​
<instance> getDeadParticleCount() ​
Description:
Gets the number of inactive (available) particles in this emitter.
Returns: number - The number of particles with active=false .
Source: src/gameobjects/particles/ParticleEmitter.js#L2170
Since: 3.0.0
getDeathZone ​
<instance> getDeathZone(particle) ​
Description:
Takes the given particle and checks to see if any of the configured Death Zones
will kill it and returns the result. This method is called automatically as part
of the Particle.update process.
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The particle to test against the Death Zones.
Returns: boolean - true if the particle should be killed, otherwise false .
Fires: Phaser.GameObjects.Particles.Events#event:DEATH_ZONE
Source: src/gameobjects/particles/ParticleEmitter.js#L1963
Since: 3.60.0
getEmitZone ​
<instance> getEmitZone(particle) ​
Description:
Takes the given particle and sets its x/y coordinates to match the next available
emission zone, if any have been configured. This method is called automatically
as part of the Particle.fire process.
The Emit Zones are iterated in sequence. Once a zone has had a particle emitted
from it, then the next zone is used and so on, in a loop.
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The particle to set the emission zone for.
Source: src/gameobjects/particles/ParticleEmitter.js#L1916
Since: 3.60.0
getFrame ​
<instance> getFrame() ​
Description:
Chooses a texture frame from Phaser.GameObjects.Particles.ParticleEmitter#frames .
Returns: Phaser.Textures.Frame - The texture frame.
Source: src/gameobjects/particles/ParticleEmitter.js#L1222
Since: 3.0.0
getParticleCount ​
<instance> getParticleCount() ​
Description:
Gets the total number of particles in this emitter.
Returns: number - The number of particles, including both alive and dead.
Source: src/gameobjects/particles/ParticleEmitter.js#L2183
Since: 3.0.0
getProcessors ​
<instance> getProcessors() ​
Description:
Gets all active Particle Processors.
Returns: Array.< Phaser.GameObjects.Particles.ParticleProcessor > - - An array of active Particle Processors.
Source: src/gameobjects/particles/ParticleEmitter.js#L2094
Since: 3.60.0
killAll ​
<instance> killAll() ​
Description:
Deactivates every particle in this emitter immediately.
This particles are killed but do not emit an event or callback.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2279
Since: 3.0.0
onParticleDeath ​
<instance> onParticleDeath(callback, [context]) ​
Description:
Sets a function to call for each particle death.
Parameters:
name type optional description
callback Phaser.Types.GameObjects.Particles.ParticleDeathCallback No The function.
context * Yes The function's calling context.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2247
Since: 3.0.0
onParticleEmit ​
<instance> onParticleEmit(callback, [context]) ​
Description:
Sets a function to call for each newly emitted particle.
Parameters:
name type optional description
callback Phaser.Types.GameObjects.Particles.ParticleEmitterCallback No The function.
context * Yes The calling context.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2215
Since: 3.0.0
overlap ​
<instance> overlap(target) ​
Description:
Takes either a Rectangle Geometry object or an Arcade Physics Body and tests
to see if it intersects with any currently alive Particle in this Emitter.
Overlapping particles are returned in an array, where you can perform further
processing on them. If nothing overlaps then the array will be empty.
Parameters:
name type optional description
target Phaser.Geom.Rectangle | Phaser.Physics.Arcade.Body No A Rectangle or Arcade Physics Body to check for intersection against all alive particles.
Returns: Array.< Phaser.GameObjects.Particles.Particle > - An array of Particles that overlap with the given target.
Source: src/gameobjects/particles/ParticleEmitter.js#L2895
Since: 3.60.0
pause ​
<instance> pause() ​
Description:
Deactivates the emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2432
Since: 3.0.0
preDestroy ​
<instance> preDestroy() ​
Description:
Destroys this Particle Emitter and all Particles it owns.
Source: src/gameobjects/particles/ParticleEmitter.js#L3923
Since: 3.60.0
preUpdate ​
<instance> preUpdate(time, delta) ​
Description:
Updates this emitter and its particles.
Parameters:
name type optional description
time number No The current timestamp as generated by the Request Animation Frame or SetTimeout.
delta number No The delta time, in ms, elapsed since the last frame.
Fires: Phaser.GameObjects.Particles.Events#event:COMPLETE
Source: src/gameobjects/particles/ParticleEmitter.js#L2771
Since: 3.0.0
removeDeathZone ​
<instance> removeDeathZone(zone) ​
Description:
Removes the given Particle Death Zone from this Emitter.
Parameters:
name type optional description
zone Phaser.GameObjects.Particles.Zones.DeathZone No The Death Zone that should be removed from this Emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1772
Since: 3.60.0
removeEmitZone ​
<instance> removeEmitZone(zone) ​
Description:
Removes the given Particle Emission Zone from this Emitter.
Parameters:
name type optional description
zone Phaser.GameObjects.Particles.Zones.EdgeZone | Phaser.GameObjects.Particles.Zones.RandomZone No The Emission Zone that should be removed from this Emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1880
Since: 3.60.0
removeParticleProcessor ​
<instance> removeParticleProcessor(processor) ​
Description:
Removes a Particle Processor from this Emitter.
The Processor must belong to this Emitter to be removed.
It is not destroyed when removed, allowing you to move it to another Emitter Manager,
so if you no longer require it you should call its destroy method directly.
Tags:
generic
Parameters:
name type optional description
processor T No The Particle Processor to remove from this Emitter Manager.
Returns: T - The Particle Processor that was removed, or null if it could not be found.
Source: src/gameobjects/particles/ParticleEmitter.js#L2066
Since: 3.60.0
reserve ​
<instance> reserve(count) ​
Description:
Creates inactive particles and adds them to this emitter's pool.
If ParticleEmitter.maxParticles is set it will limit the
value passed to this method to make sure it's not exceeded.
Parameters:
name type optional description
count number No The number of particles to create.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2122
Since: 3.0.0
resetCounters ​
<instance> resetCounters(frequency, on) ​
Description:
Resets the internal counter trackers.
You shouldn't ever need to call this directly.
Parameters:
name type optional description
frequency number No The frequency counter.
on boolean No Set the complete flag.
Source: src/gameobjects/particles/ParticleEmitter.js#L1154
Since: 3.60.0
resume ​
<instance> resume() ​
Description:
Activates the emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2447
Since: 3.0.0
setAnim ​
<instance> setAnim(anims, [pickRandom], [quantity]) ​
Description:
Sets a pattern for assigning animations to emitted particles. The anims configuration can be any of:
anim: 'red'
anim: [ 'red', 'green', 'blue', 'pink', 'white' ]
anim: { anims: [ 'red', 'green', 'blue', 'pink', 'white' ], [cycle: bool], [quantity: int] }
Call this method at least once before any particles are created, or set anim in the Particle Emitter's configuration when creating the Emitter.
Parameters:
name type optional default description
anims string | Array.<string> Phaser.Types.GameObjects.Particles.ParticleEmitterAnimConfig No
pickRandom boolean Yes true Whether animations should be assigned at random from anims . If a config object is given, this parameter is ignored.
quantity number Yes 1 The number of consecutive particles that will receive each animation. If a config object is given, this parameter is ignored.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1374
Since: 3.60.0
setConfig ​
<instance> setConfig(config) ​
Description:
Takes an Emitter Configuration file and resets this Emitter, using any
properties defined in the config to then set it up again.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Particles.ParticleEmitterConfig No Settings for this emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L937
Since: 3.60.0
setEmitterAngle ​
<instance> setEmitterAngle(value) ​
Description:
Sets the angle of a Phaser.GameObjects.Particles.ParticleEmitter#radial particle stream.
The value is given in degrees using Phaser's right-handed coordinate system.
Parameters:
name type optional description
value Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType No The angle of the initial velocity of emitted particles, in degrees.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1627
Since: 3.0.0
setEmitterFrame ​
<instance> setEmitterFrame(frames, [pickRandom], [quantity]) ​
Description:
Sets a pattern for assigning texture frames to emitted particles. The frames configuration can be any of:
frame: 0
frame: 'red'
frame: [ 0, 1, 2, 3 ]
frame: [ 'red', 'green', 'blue', 'pink', 'white' ]
frame: { frames: [ 'red', 'green', 'blue', 'pink', 'white' ], [cycle: bool], [quantity: int] }
Parameters:
name type optional default description
frames array | string number Phaser.Types.GameObjects.Particles.ParticleEmitterFrameConfig No
pickRandom boolean Yes true Whether frames should be assigned at random from frames .
quantity number Yes 1 The number of consecutive particles that will receive each frame.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1266
Since: 3.0.0
setEmitZone ​
<instance> setEmitZone(zone) ​
Description:
Changes the currently active Emission Zone. The zones should have already
been added to this Emitter either via the emitter config, or the
addEmitZone method.
Call this method by passing either a numeric zone index value, or
the zone instance itself.
Prior to v3.60 an Emitter could only have a single Emit Zone and this
method was how you set it. From 3.60 and up it now performs a different
function and swaps between all available active zones.
Parameters:
name type optional description
zone number | Phaser.GameObjects.Particles.Zones.EdgeZone Phaser.GameObjects.Particles.Zones.RandomZone No
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1995
Since: 3.0.0
setFrequency ​
<instance> setFrequency(frequency, [quantity]) ​
Description:
Sets the emitter's Phaser.GameObjects.Particles.ParticleEmitter#frequency
and Phaser.GameObjects.Particles.ParticleEmitter#quantity .
Parameters:
name type optional description
frequency number No The time interval (>= 0) of each flow cycle, in ms; or -1 to put the emitter in explosion mode.
quantity Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType Yes The number of particles to release at each flow cycle or explosion.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1680
Since: 3.0.0
setParticleAlpha ​
<instance> setParticleAlpha(value) ​
Description:
Sets the opacity (alpha) of emitted particles.
You can also set the alpha of the entire emitter via setAlpha .
Parameters:
name type optional description
value Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType | Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType No A value between 0 (transparent) and 1 (opaque).
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1588
Since: 3.60.0
setParticleGravity ​
<instance> setParticleGravity(x, y) ​
Description:
Sets the gravity applied to emitted particles.
Parameters:
name type optional description
x number No Horizontal acceleration due to gravity, in pixels per second squared. Set to zero for no gravity.
y number No Vertical acceleration due to gravity, in pixels per second squared. Set to zero for no gravity.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1569
Since: 3.60.0
setParticleLifespan ​
<instance> setParticleLifespan(value) ​
Description:
Sets the lifespan of newly emitted particles in milliseconds.
Parameters:
name type optional description
value Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType No The lifespan of a particle, in ms.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1646
Since: 3.60.0
setParticleScale ​
<instance> setParticleScale([x], [y]) ​
Description:
Sets the vertical and horizontal scale of the emitted particles.
You can also set the scale of the entire emitter via setScale .
Parameters:
name type optional default description
x number Yes 1 The horizontal scale of the emitted Particles.
y number Yes "x" The vertical scale of emitted Particles. If not set it will use the x value.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1545
Since: 3.60.0
setParticleSpeed ​
<instance> setParticleSpeed(x, [y]) ​
Description:
Sets the initial radial speed of emitted particles.
Changes the emitter to radial mode.
Parameters:
name type optional default description
x number No The horizontal speed of the emitted Particles.
y number Yes "x" The vertical speed of emitted Particles. If not set it will use the x value.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1511
Since: 3.60.0
setParticleTint ​
<instance> setParticleTint(value) ​
Description:
Sets the color tint of emitted particles.
This is a WebGL only feature.
Tags:
webglOnly
Parameters:
name type optional description
value Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType | Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType No A value between 0 and 0xffffff.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1607
Since: 3.60.0
setQuantity ​
<instance> setQuantity(quantity) ​
Description:
Sets the number of particles released at each flow cycle or explosion.
Parameters:
name type optional description
quantity Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType No The number of particles to release at each flow cycle or explosion.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1663
Since: 3.0.0
setRadial ​
<instance> setRadial([value]) ​
Description:
Turns Phaser.GameObjects.Particles.ParticleEmitter#radial particle movement on or off.
Parameters:
name type optional default description
value boolean Yes true Radial mode (true) or point mode (true).
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1441
Since: 3.0.0
setSortCallback ​
<instance> setSortCallback([callback]) ​
Description:
Sets a callback to be used to sort the particles before rendering each frame.
This allows you to define your own logic and behavior in the callback.
The callback will be sent two parameters: the two Particles being compared,
and must adhere to the criteria of the compareFn in Array.sort :
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description
Call this method with no parameters to reset the sort callback.
Setting your own callback will override both the particleBringToTop and
sortProperty settings of this Emitter.
Parameters:
name type optional description
callback Phaser.Types.GameObjects.Particles.ParticleSortCallback Yes The callback to invoke when the particles are sorted. Leave undefined to reset to the default.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2495
Since: 3.60.0
setSortProperty ​
<instance> setSortProperty([property], [ascending]) ​
Description:
Set the property by which active particles are sorted prior to be rendered.
It allows you to control the rendering order of the particles.
This can be any valid property of the Particle class, such as y , alpha
or lifeT .
The 'alive' particles array is sorted in place each game frame. Setting a
sort property will override the particleBringToTop setting.
If you wish to use your own sorting function, see setSortCallback instead.
Parameters:
name type optional default description
property string Yes The property on the Particle class to sort by.
ascending boolean Yes true Should the particles be sorted in ascending or descending order?
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L2462
Since: 3.60.0
start ​
<instance> start([advance], [duration]) ​
Description:
Turns Phaser.GameObjects.Particles.ParticleEmitter#on the emitter and resets the flow counter.
If this emitter is in flow mode (frequency >= 0; the default), the particle flow will start (or restart).
If this emitter is in explode mode (frequency = -1), nothing will happen.
Use Phaser.GameObjects.Particles.ParticleEmitter#explode or Phaser.GameObjects.Particles.ParticleEmitter#flow instead.
Calling this method will emit the START event.
Parameters:
name type optional default description
advance number Yes 0 Advance this number of ms in time through the emitter.
duration number Yes 0 Limit this emitter to only emit particles for the given number of ms. Setting this parameter will override any duration already set in the Emitter configuration object.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Fires: Phaser.GameObjects.Particles.Events#event:START
Source: src/gameobjects/particles/ParticleEmitter.js#L2352
Since: 3.0.0
startFollow ​
<instance> startFollow(target, [offsetX], [offsetY], [trackVisible]) ​
Description:
Continuously moves the particle origin to follow a Game Object's position.
Parameters:
name type optional default description
target Phaser.Types.Math.Vector2Like No The Object to follow.
offsetX number Yes 0 Horizontal offset of the particle origin from the Game Object.
offsetY number Yes 0 Vertical offset of the particle origin from the Game Object.
trackVisible boolean Yes false Whether the emitter's visible state will track the target's visible state.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1179
Since: 3.0.0
stop ​
<instance> stop([kill]) ​
Description:
Turns off the emitter and
stops it from emitting further particles. Currently alive particles will remain
active until they naturally expire unless you set the kill parameter to true .
Calling this method will emit the STOP event. When the final particle has
expired the COMPLETE event will be emitted.
Parameters:
name type optional default description
kill boolean Yes false Kill all particles immediately (true), or leave them to die after their lifespan expires? (false, the default)
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Fires: Phaser.GameObjects.Particles.Events#event:STOP
Source: src/gameobjects/particles/ParticleEmitter.js#L2397
Since: 3.11.0
stopFollow ​
<instance> stopFollow() ​
Description:
Stops following a Game Object.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1205
Since: 3.0.0
toJSON ​
<instance> toJSON() ​
Description:
Creates a description of this emitter suitable for JSON serialization.
Overrides: Phaser.GameObjects.GameObject#toJSON
Returns: Phaser.Types.GameObjects.JSONGameObject - A JSON representation of the Game Object.
Source: src/gameobjects/particles/ParticleEmitter.js#L1103
Since: 3.0.0
updateConfig ​
<instance> updateConfig(config) ​
Description:
Takes an existing Emitter Configuration file and updates this Emitter.
Existing properties are overriden while new properties are added. The
updated configuration is then passed to the setConfig method to reset
the Emitter with the updated configuration.
Parameters:
name type optional description
config Phaser.Types.GameObjects.Particles.ParticleEmitterConfig No Settings for this emitter.
Returns: Phaser.GameObjects.Particles.ParticleEmitter - This Particle Emitter.
Source: src/gameobjects/particles/ParticleEmitter.js#L1073
Since: 3.85.0
Previous
ParticleBounds
Next
ParticleProcessor
An explicit static value:
A random value:
A custom callback:
A start / end object:
A start / end random object:
An interpolation object:
A stepped emitter object:
A stepped emitter object with yoyo:
A min / max object:
A random object:
Custom onEmit and onUpdate callbacks:
v3.55 Differences
Inherited Members
Public Members
acceleration
accelerationX
accelerationY
animCounter
animQuantity
anims
bounce
colorEase
completeFlag
config
currentAnim
currentFrame
deathCallback
deathCallbackScope
deathZones
delay
duration
elapsed
emitCallback
emitCallbackScope
emitting
emitZones
flowCounter
follow
followOffset
frameCounter
frameQuantity
frames
frequency
gravityX
gravityY
hold
lifespan
maxAliveParticles
maxParticles
maxVelocityX
maxVelocityY
moveTo
moveToX
moveToY
ops
particleAlpha
particleAngle
particleBringToTop
particleClass
particleColor
particleRotate
particleScaleX
particleScaleY
particleTint
particleX
particleY
processors
quantity
radial
randomAnim
randomFrame
skipping
sortCallback
sortOrderAsc
sortProperty
speed
speedX
speedY
stopAfter
stopCounter
timeScale
tintFill
trackVisible
viewBounds
worldMatrix
zoneIndex
zoneTotal
Inherited Methods
Public Methods
addDeathZone
addEmitZone
addParticleBounds
addParticleProcessor
atLimit
clearDeathZones
clearEmitZones
createEmitter
createGravityWell
depthSort
depthSortCallback
emitParticle
emitParticleAt
explode
fastForward
flow
forEachAlive
forEachDead
getAliveParticleCount
getAnim
getBounds
getDeadParticleCount
getDeathZone
getEmitZone
getFrame
getParticleCount
getProcessors
killAll
onParticleDeath
onParticleEmit
overlap
pause
preDestroy
preUpdate
removeDeathZone
removeEmitZone
removeParticleProcessor
reserve
resetCounters
resume
setAnim
setConfig
setEmitterAngle
setEmitterFrame
setEmitZone
setFrequency
setParticleAlpha
setParticleGravity
setParticleLifespan
setParticleScale
setParticleSpeed
setParticleTint
setQuantity
setRadial
setSortCallback
setSortProperty
start
startFollow
stop
stopFollow
toJSON
updateConfig
