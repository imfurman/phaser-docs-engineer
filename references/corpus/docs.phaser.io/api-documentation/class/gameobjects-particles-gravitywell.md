# GravityWell | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-particles-gravitywell

Phaser API Documentation
Class
GravityWell
Version: Phaser v3.90.0
On this page
GravityWell
The Gravity Well Particle Processor applies a force on the particles to draw
them towards, or repel them from, a single point.
The force applied is inversely proportional to the square of the distance
from the particle to the point, in accordance with Newton's law of gravity.
This simulates the effect of gravity over large distances (as between planets, for example).
Constructor
new GravityWell([x], [y], [power], [epsilon], [gravity])
Parameters
name type optional default description
x number | Phaser.Types.GameObjects.Particles.GravityWellConfig Yes 0 The x coordinate of the Gravity Well, in world space.
y number Yes 0 The y coordinate of the Gravity Well, in world space.
power number Yes 0 The strength of the gravity force - larger numbers produce a stronger force.
epsilon number Yes 100 The minimum distance for which the gravity force is calculated.
gravity number Yes 50 The gravitational force of this Gravity Well.
Scope : static
Extends
Phaser.GameObjects.Particles.ParticleProcessor
Source: src/gameobjects/particles/GravityWell.js#L11
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Particles.ParticleProcessor :
active
manager
x
y
Public Members ​
epsilon ​
epsilon: number ​
Description:
The minimum distance for which the gravity force is calculated.
Defaults to 100.
Source: src/gameobjects/particles/GravityWell.js#L129
Since: 3.0.0
gravity ​
gravity: number ​
Description:
The gravitational force of this Gravity Well.
Defaults to 50.
Source: src/gameobjects/particles/GravityWell.js#L175
Since: 3.0.0
power ​
power: number ​
Description:
The strength of the gravity force - larger numbers produce a stronger force.
Defaults to 0.
Source: src/gameobjects/particles/GravityWell.js#L152
Since: 3.0.0
Inherited Methods ​
From Phaser.GameObjects.Particles.ParticleProcessor :
destroy
Public Methods ​
update ​
<instance> update(particle, delta, step) ​
Description:
Takes a Particle and updates it based on the properties of this Gravity Well.
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The Particle to update.
delta number No The delta time in ms.
step number No The delta value divided by 1000.
Overrides: Phaser.GameObjects.Particles.ParticleProcessor#update
Source: src/gameobjects/particles/GravityWell.js#L95
Since: 3.0.0
Previous
EmitterOp
Next
Particle
Inherited Members
Public Members
epsilon
gravity
power
Inherited Methods
Public Methods
update
