# Phaser.Types.GameObjects.Particles | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/types-gameobjects-particles

Phaser API Documentation
Namespaces
Phaser.Types.GameObjects.Particles
Version: Phaser v3.90.0
On this page
Phaser.Types.GameObjects.Particles
Scope: static
Source: src/gameobjects/particles/typedefs/index.js#L7
Static functions ​
DeathZoneObject ​
DeathZoneObject ​
Source: src/gameobjects/particles/typedefs/DeathZoneObject.js#L1
Since: 3.60.0
DeathZoneSource ​
DeathZoneSource ​
Source: src/gameobjects/particles/typedefs/DeathZoneSource.js#L1
Since: 3.0.0
DeathZoneSourceCallback ​
DeathZoneSourceCallback ​
Parameters:
name type optional description
x number No The x coordinate of the particle to check against this source area.
y number No The y coordinate of the particle to check against this source area.
Returns: boolean - - True if the coordinates are within the source area.
Source: src/gameobjects/particles/typedefs/DeathZoneSourceCallback.js#L1
Since: 3.0.0
EdgeZoneSource ​
EdgeZoneSource ​
Source: src/gameobjects/particles/typedefs/EdgeZoneSource.js#L1
Since: 3.0.0
EdgeZoneSourceCallback ​
EdgeZoneSourceCallback ​
Parameters:
name type optional description
quantity number No The number of particles to place on the source edge. If 0, stepRate should be used instead.
stepRate number Yes The distance between each particle. When set, quantity is implied and should be set to 0 .
Returns: Array.< Phaser.Types.Math.Vector2Like > - - The points placed on the source edge.
Source: src/gameobjects/particles/typedefs/EdgeZoneSourceCallback.js#L1
Since: 3.0.0
EmitterOpCustomEmitConfig ​
EmitterOpCustomEmitConfig ​
Source: src/gameobjects/particles/typedefs/EmitterOpCustomEmitConfig.js#L1
Since: 3.0.0
EmitterOpCustomUpdateConfig ​
EmitterOpCustomUpdateConfig ​
Source: src/gameobjects/particles/typedefs/EmitterOpCustomUpdateConfig.js#L1
Since: 3.0.0
EmitterOpEaseConfig ​
EmitterOpEaseConfig ​
Description:
Defines an operation yielding a value incremented continuously across a range.
Source: src/gameobjects/particles/typedefs/EmitterOpEaseConfig.js#L1
Since: 3.0.0
EmitterOpInterpolationConfig ​
EmitterOpInterpolationConfig ​
Description:
Defines an operation yielding a value incremented continuously across an interpolated data set.
Source: src/gameobjects/particles/typedefs/EmitterOpInterpolationConfig.js#L1
Since: 3.60.0
EmitterOpOnEmitCallback ​
EmitterOpOnEmitCallback ​
Description:
The returned value sets what the property will be at the START of the particle's life, on emit.
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle Yes The particle.
key string Yes The name of the property.
value number Yes The current value of the property.
Returns: number - The new value of the property.
Source: src/gameobjects/particles/typedefs/EmitterOpOnEmitCallback.js#L1
Since: 3.0.0
EmitterOpOnEmitType ​
EmitterOpOnEmitType ​
Source: src/gameobjects/particles/typedefs/EmitterOpOnEmitType.js#L1
Since: 3.18.0
EmitterOpOnUpdateCallback ​
EmitterOpOnUpdateCallback ​
Description:
The returned value updates the property for the duration of the particle's life.
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The particle.
key string No The name of the property.
t number No The normalized lifetime of the particle, between 0 (start) and 1 (end).
value number No The current value of the property.
Returns: number - The new value of the property.
Source: src/gameobjects/particles/typedefs/EmitterOpOnUpdateCallback.js#L1
Since: 3.0.0
EmitterOpOnUpdateType ​
EmitterOpOnUpdateType ​
Source: src/gameobjects/particles/typedefs/EmitterOpOnUpdateType.js#L1
Since: 3.18.0
EmitterOpRandomConfig ​
EmitterOpRandomConfig ​
Description:
Defines an operation yielding a random value within a range.
Source: src/gameobjects/particles/typedefs/EmitterOpRandomConfig.js#L1
Since: 3.0.0
EmitterOpRandomMinMaxConfig ​
EmitterOpRandomMinMaxConfig ​
Description:
Defines an operation yielding a random value within a range.
Source: src/gameobjects/particles/typedefs/EmitterOpRandomMinMaxConfig.js#L1
Since: 3.0.0
EmitterOpSteppedConfig ​
EmitterOpSteppedConfig ​
Description:
Defines an operation yielding a value incremented by steps across a range.
Source: src/gameobjects/particles/typedefs/EmitterOpSteppedConfig.js#L1
Since: 3.0.0
EmitZoneData ​
EmitZoneData ​
Source: src/gameobjects/particles/typedefs/EmitZoneData.js#L1
Since: 3.60.0
EmitZoneObject ​
EmitZoneObject ​
Source: src/gameobjects/particles/typedefs/EmitZoneObject.js#L1
Since: 3.60.0
GravityWellConfig ​
GravityWellConfig ​
Source: src/gameobjects/particles/typedefs/GravityWellConfig.js#L1
Since: 3.0.0
ParticleClassConstructor ​
ParticleClassConstructor ​
Parameters:
name type optional description
emitter Phaser.GameObjects.Particles.ParticleEmitter No The Emitter to which this Particle belongs.
Source: src/gameobjects/particles/typedefs/ParticleClassConstructor.js#L1
Since: 3.0.0
ParticleData ​
ParticleData ​
Source: src/gameobjects/particles/typedefs/ParticleData.js#L1
Since: 3.60.0
ParticleDataValue ​
ParticleDataValue ​
Source: src/gameobjects/particles/typedefs/ParticleDataValue.js#L1
Since: 3.60.0
ParticleDeathCallback ​
ParticleDeathCallback ​
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The particle that died.
Source: src/gameobjects/particles/typedefs/ParticleDeathCallback.js#L1
Since: 3.0.0
ParticleEmitterAnimConfig ​
ParticleEmitterAnimConfig ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterAnimConfig.js#L1
Since: 3.60.0
ParticleEmitterBounds ​
ParticleEmitterBounds ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterBounds.js#L1
Since: 3.0.0
ParticleEmitterBoundsAlt ​
ParticleEmitterBoundsAlt ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterBoundsAlt.js#L1
Since: 3.0.0
ParticleEmitterCallback ​
ParticleEmitterCallback ​
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The particle associated with the call.
emitter Phaser.GameObjects.Particles.ParticleEmitter No This particle emitter associated with the call.
Source: src/gameobjects/particles/typedefs/ParticleEmitterCallback.js#L1
Since: 3.0.0
ParticleEmitterConfig ​
ParticleEmitterConfig ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterConfig.js#L1
Since: 3.0.0
ParticleEmitterCreatorConfig ​
ParticleEmitterCreatorConfig ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterCreatorConfig.js#L1
Since: 3.60.0
ParticleEmitterDeathZoneConfig ​
ParticleEmitterDeathZoneConfig ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterDeathZoneConfig.js#L1
Since: 3.0.0
ParticleEmitterEdgeZoneConfig ​
ParticleEmitterEdgeZoneConfig ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterEdgeZoneConfig.js#L1
Since: 3.0.0
ParticleEmitterFrameConfig ​
ParticleEmitterFrameConfig ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterFrameConfig.js#L1
Since: 3.0.0
ParticleEmitterOps ​
ParticleEmitterOps ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterOps.js#L1
Since: 3.60.0
ParticleEmitterRandomZoneConfig ​
ParticleEmitterRandomZoneConfig ​
Source: src/gameobjects/particles/typedefs/ParticleEmitterRandomZoneConfig.js#L1
Since: 3.0.0
ParticleSortCallback ​
ParticleSortCallback ​
Parameters:
name type optional description
a Phaser.GameObjects.Particles.Particle No The first Particle being compared.
b Phaser.GameObjects.Particles.Particle No The second Particle being compared.
Source: src/gameobjects/particles/typedefs/ParticleSortCallback.js#L1
Since: 3.60.0
RandomZoneSource ​
RandomZoneSource ​
Source: src/gameobjects/particles/typedefs/RandomZoneSource.js#L1
Since: 3.0.0
RandomZoneSourceCallback ​
RandomZoneSourceCallback ​
Parameters:
name type optional description
point Phaser.Types.Math.Vector2Like No A point to modify.
Source: src/gameobjects/particles/typedefs/RandomZoneSourceCallback.js#L1
Since: 3.0.0
Previous
Phaser.Types.GameObjects.NineSlice
Next
Phaser.Types.GameObjects.PathFollower
Static functions
DeathZoneObject
DeathZoneSource
DeathZoneSourceCallback
EdgeZoneSource
EdgeZoneSourceCallback
EmitterOpCustomEmitConfig
EmitterOpCustomUpdateConfig
EmitterOpEaseConfig
EmitterOpInterpolationConfig
EmitterOpOnEmitCallback
EmitterOpOnEmitType
EmitterOpOnUpdateCallback
EmitterOpOnUpdateType
EmitterOpRandomConfig
EmitterOpRandomMinMaxConfig
EmitterOpSteppedConfig
EmitZoneData
EmitZoneObject
GravityWellConfig
ParticleClassConstructor
ParticleData
ParticleDataValue
ParticleDeathCallback
ParticleEmitterAnimConfig
ParticleEmitterBounds
ParticleEmitterBoundsAlt
ParticleEmitterCallback
ParticleEmitterConfig
ParticleEmitterCreatorConfig
ParticleEmitterDeathZoneConfig
ParticleEmitterEdgeZoneConfig
ParticleEmitterFrameConfig
ParticleEmitterOps
ParticleEmitterRandomZoneConfig
ParticleSortCallback
RandomZoneSource
RandomZoneSourceCallback
