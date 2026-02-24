# Particle | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-particles-particle

Phaser API Documentation
Class
Particle
Version: Phaser v3.90.0
On this page
Particle
A Particle is a simple object owned and controlled by a Particle Emitter.
It encapsulates all of the properties required to move and update according
to the Emitters operations.
Constructor
new Particle(emitter)
Parameters
name type optional description
emitter Phaser.GameObjects.Particles.ParticleEmitter No The Emitter to which this Particle belongs.
Scope : static
Source: src/gameobjects/particles/Particle.js#L15
Since: 3.0.0
Public Members ​
accelerationX ​
accelerationX: number ​
Description:
The x acceleration of this Particle.
Source: src/gameobjects/particles/Particle.js#L117
Since: 3.0.0
accelerationY ​
accelerationY: number ​
Description:
The y acceleration of this Particle.
Source: src/gameobjects/particles/Particle.js#L127
Since: 3.0.0
alpha ​
alpha: number ​
Description:
The alpha value of this Particle.
Source: src/gameobjects/particles/Particle.js#L187
Since: 3.0.0
angle ​
angle: number ​
Description:
The angle of this Particle in degrees.
Source: src/gameobjects/particles/Particle.js#L197
Since: 3.0.0
anims ​
anims: Phaser.Animations.AnimationState ​
Description:
The Animation State component of this Particle.
This component provides features to apply animations to this Particle.
It is responsible for playing, loading, queuing animations for later playback,
mixing between animations and setting the current animation frame to this Particle.
It is created only if the Particle's Emitter has at least one Animation.
Source: src/gameobjects/particles/Particle.js#L326
Since: 3.60.0
bounce ​
bounce: number ​
Description:
The bounciness, or restitution, of this Particle.
Source: src/gameobjects/particles/Particle.js#L157
Since: 3.0.0
bounds ​
bounds: Phaser.Geom.Rectangle ​
Description:
A rectangle that holds the bounds of this Particle after a call to
the Particle.getBounds method has been made.
Source: src/gameobjects/particles/Particle.js#L347
Since: 3.60.0
data ​
data: Phaser.Types.GameObjects.Particles.ParticleData ​
Description:
The data used by the ease equation.
Source: src/gameobjects/particles/Particle.js#L277
Since: 3.0.0
delayCurrent ​
delayCurrent: number ​
Description:
The delay applied to this Particle upon emission, in ms.
Source: src/gameobjects/particles/Particle.js#L247
Since: 3.0.0
emitter ​
emitter: Phaser.GameObjects.Particles.ParticleEmitter ​
Description:
The Emitter to which this Particle belongs.
A Particle can only belong to a single Emitter and is created, updated and destroyed by it.
Source: src/gameobjects/particles/Particle.js#L35
Since: 3.0.0
frame ​
frame: Phaser.Textures.Frame ​
Description:
The texture frame used by this Particle when it renders.
Source: src/gameobjects/particles/Particle.js#L56
Since: 3.0.0
holdCurrent ​
holdCurrent: number ​
Description:
The hold applied to this Particle before it expires, in ms.
Source: src/gameobjects/particles/Particle.js#L257
Since: 3.60.0
life ​
life: number ​
Description:
The lifespan of this Particle in ms.
Source: src/gameobjects/particles/Particle.js#L227
Since: 3.0.0
lifeCurrent ​
lifeCurrent: number ​
Description:
The current life of this Particle in ms.
Source: src/gameobjects/particles/Particle.js#L237
Since: 3.0.0
lifeT ​
lifeT: number ​
Description:
The normalized lifespan T value, where 0 is the start and 1 is the end.
Source: src/gameobjects/particles/Particle.js#L267
Since: 3.0.0
maxVelocityX ​
maxVelocityX: number ​
Description:
The maximum horizontal velocity this Particle can travel at.
Source: src/gameobjects/particles/Particle.js#L137
Since: 3.0.0
maxVelocityY ​
maxVelocityY: number ​
Description:
The maximum vertical velocity this Particle can travel at.
Source: src/gameobjects/particles/Particle.js#L147
Since: 3.0.0
rotation ​
rotation: number ​
Description:
The angle of this Particle in radians.
Source: src/gameobjects/particles/Particle.js#L207
Since: 3.0.0
scaleX ​
scaleX: number ​
Description:
The horizontal scale of this Particle.
Source: src/gameobjects/particles/Particle.js#L167
Since: 3.0.0
scaleY ​
scaleY: number ​
Description:
The vertical scale of this Particle.
Source: src/gameobjects/particles/Particle.js#L177
Since: 3.0.0
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene to which this Game Object belongs.
Game Objects can only belong to one Scene.
You should consider this property as being read-only. You cannot move a
Game Object to another Scene by simply changing it.
Source: src/gameobjects/particles/Particle.js#L312
Since: 3.60.0
texture ​
texture: Phaser.Textures.Texture ​
Description:
The texture used by this Particle when it renders.
Source: src/gameobjects/particles/Particle.js#L46
Since: 3.60.0
tint ​
tint: number ​
Description:
The tint applied to this Particle.
Tags:
webglOnly
Source: src/gameobjects/particles/Particle.js#L217
Since: 3.0.0
velocityX ​
velocityX: number ​
Description:
The x velocity of this Particle.
Source: src/gameobjects/particles/Particle.js#L97
Since: 3.0.0
velocityY ​
velocityY: number ​
Description:
The y velocity of this Particle.
Source: src/gameobjects/particles/Particle.js#L107
Since: 3.0.0
worldPosition ​
worldPosition: Phaser.Math.Vector2 ​
Description:
The coordinates of this Particle in world space.
Updated as part of computeVelocity .
Source: src/gameobjects/particles/Particle.js#L86
Since: 3.60.0
x ​
x: number ​
Description:
The x coordinate of this Particle.
Source: src/gameobjects/particles/Particle.js#L66
Since: 3.0.0
y ​
y: number ​
Description:
The y coordinate of this Particle.
Source: src/gameobjects/particles/Particle.js#L76
Since: 3.0.0
Public Methods ​
computeVelocity ​
<instance> computeVelocity(emitter, delta, step, processors, t) ​
Description:
An internal method that calculates the velocity of the Particle and
its world position. It also runs it against any active Processors
that are set on the Emitter.
Parameters:
name type optional description
emitter Phaser.GameObjects.Particles.ParticleEmitter No The Emitter that is updating this Particle.
delta number No The delta time in ms.
step number No The delta value divided by 1000.
processors Array.< Phaser.GameObjects.Particles.ParticleProcessor > No An array of all active Particle Processors.
t number No The current normalized lifetime of the particle, between 0 (birth) and 1 (death).
Source: src/gameobjects/particles/Particle.js#L668
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Particle.
Source: src/gameobjects/particles/Particle.js#L789
Since: 3.60.0
emit ​
<instance> emit(event, [a1], [a2], [a3], [a4], [a5]) ​
Description:
The Event Emitter proxy.
Passes on all parameters to the ParticleEmitter to emit directly.
Parameters:
name type optional description
event string | Symbol No The event name.
a1 any Yes Optional argument 1.
a2 any Yes Optional argument 2.
a3 any Yes Optional argument 3.
a4 any Yes Optional argument 4.
a5 any Yes Optional argument 5.
Returns: boolean - true if the event had listeners, else false .
Source: src/gameobjects/particles/Particle.js#L358
Since: 3.60.0
fire ​
<instance> fire([x], [y]) ​
Description:
Starts this Particle from the given coordinates.
Parameters:
name type optional description
x number Yes The x coordinate to launch this Particle from.
y number Yes The y coordinate to launch this Particle from.
Returns: boolean - true if the Particle is alive, or false if it was spawned inside a DeathZone.
Source: src/gameobjects/particles/Particle.js#L425
Since: 3.0.0
getBounds ​
<instance> getBounds([matrix]) ​
Description:
Gets the bounds of this particle as a Geometry Rectangle, factoring in any
transforms of the parent emitter and anything else above it in the display list.
Once calculated the bounds can be accessed via the Particle.bounds property.
Parameters:
name type optional description
matrix Phaser.GameObjects.Components.TransformMatrix Yes Optional transform matrix to apply to this particle.
Returns: Phaser.Geom.Rectangle - A Rectangle containing the transformed bounds of this particle.
Source: src/gameobjects/particles/Particle.js#L735
Since: 3.60.0
isAlive ​
<instance> isAlive() ​
Description:
Checks to see if this Particle is alive and updating.
Returns: boolean - true if this Particle is alive and updating, otherwise false .
Source: src/gameobjects/particles/Particle.js#L380
Since: 3.0.0
kill ​
<instance> kill() ​
Description:
Kills this particle. This sets the lifeCurrent value to 0, which forces
the Particle to be removed the next time its parent Emitter runs an update.
Source: src/gameobjects/particles/Particle.js#L393
Since: 3.60.0
setPosition ​
<instance> setPosition([x], [y]) ​
Description:
Sets the position of this particle to the given x/y coordinates.
If the parameters are left undefined, it resets the particle back to 0x0.
Parameters:
name type optional default description
x number Yes 0 The x coordinate to set this Particle to.
y number Yes 0 The y coordinate to set this Particle to.
Source: src/gameobjects/particles/Particle.js#L405
Since: 3.60.0
setSizeToFrame ​
<instance> setSizeToFrame() ​
Description:
This is a NOOP method and does nothing when called.
Source: src/gameobjects/particles/Particle.js#L724
Since: 3.60.0
update ​
<instance> update(delta, step, processors) ​
Description:
The main update method for this Particle.
Updates its life values, computes the velocity and repositions the Particle.
Parameters:
name type optional description
delta number No The delta time in ms.
step number No The delta value divided by 1000.
processors Array.< Phaser.GameObjects.Particles.ParticleProcessor > No An array of all active Particle Processors.
Returns: boolean - Returns true if this Particle has now expired and should be removed, otherwise false if still active.
Source: src/gameobjects/particles/Particle.js#L563
Since: 3.0.0
Previous
GravityWell
Next
ParticleBounds
Public Members
accelerationX
accelerationY
alpha
angle
anims
bounce
bounds
data
delayCurrent
emitter
frame
holdCurrent
life
lifeCurrent
lifeT
maxVelocityX
maxVelocityY
rotation
scaleX
scaleY
scene
texture
tint
velocityX
velocityY
worldPosition
x
y
Public Methods
computeVelocity
destroy
emit
fire
getBounds
isAlive
kill
setPosition
setSizeToFrame
update
