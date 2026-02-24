# ParticleBounds | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-particles-particlebounds

Phaser API Documentation
Class
ParticleBounds
Version: Phaser v3.90.0
On this page
ParticleBounds
The Particle Bounds Processor.
Defines a rectangular region, in world space, within which particle movement
is restrained.
Use the properties collideLeft , collideRight , collideTop and
collideBottom to control if a particle will rebound off the sides
of this boundary, or not.
This happens when the particles worldPosition x/y coordinate hits the boundary.
The strength of the rebound is determined by the Particle.bounce property.
Constructor
new ParticleBounds(x, y, width, height, [collideLeft], [collideRight], [collideTop], [collideBottom])
Parameters
name type optional default description
x number No The x position (top-left) of the bounds, in world space.
y number No The y position (top-left) of the bounds, in world space.
width number No The width of the bounds.
height number No The height of the bounds.
collideLeft boolean Yes true Whether particles interact with the left edge of the bounds.
collideRight boolean Yes true Whether particles interact with the right edge of the bounds.
collideTop boolean Yes true Whether particles interact with the top edge of the bounds.
collideBottom boolean Yes true Whether particles interact with the bottom edge of the bounds.
Scope : static
Extends
Phaser.GameObjects.Particles.ParticleProcessor
Source: src/gameobjects/particles/ParticleBounds.js#L11
Since: 3.60.0
Inherited Members ​
From Phaser.GameObjects.Particles.ParticleProcessor :
active
manager
x
y
Public Members ​
bounds ​
bounds: Phaser.Geom.Rectangle ​
Description:
A rectangular boundary constraining particle movement. Use the Emitter properties collideLeft ,
collideRight , collideTop and collideBottom to control if a particle will rebound off
the sides of this boundary, or not. This happens when the particles x/y coordinate hits
the boundary.
Source: src/gameobjects/particles/ParticleBounds.js#L56
Since: 3.60.0
collideBottom ​
collideBottom: boolean ​
Description:
Whether particles interact with the bottom edge of the emitter Phaser.GameObjects.Particles.ParticleBounds#bounds .
Source: src/gameobjects/particles/ParticleBounds.js#L98
Since: 3.60.0
collideLeft ​
collideLeft: boolean ​
Description:
Whether particles interact with the left edge of the emitter Phaser.GameObjects.Particles.ParticleEmitter#bounds .
Source: src/gameobjects/particles/ParticleBounds.js#L68
Since: 3.60.0
collideRight ​
collideRight: boolean ​
Description:
Whether particles interact with the right edge of the emitter Phaser.GameObjects.Particles.ParticleBounds#bounds .
Source: src/gameobjects/particles/ParticleBounds.js#L78
Since: 3.60.0
collideTop ​
collideTop: boolean ​
Description:
Whether particles interact with the top edge of the emitter Phaser.GameObjects.Particles.ParticleBounds#bounds .
Source: src/gameobjects/particles/ParticleBounds.js#L88
Since: 3.60.0
Inherited Methods ​
From Phaser.GameObjects.Particles.ParticleProcessor :
destroy
Public Methods ​
update ​
<instance> update(particle) ​
Description:
Takes a Particle and updates it against the bounds.
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The Particle to update.
Overrides: Phaser.GameObjects.Particles.ParticleProcessor#update
Source: src/gameobjects/particles/ParticleBounds.js#L109
Since: 3.0.0
Previous
Particle
Next
ParticleEmitter
Inherited Members
Public Members
bounds
collideBottom
collideLeft
collideRight
collideTop
Inherited Methods
Public Methods
update
