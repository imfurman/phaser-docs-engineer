# EmitterColorOp | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-particles-emittercolorop

Phaser API Documentation
Class
EmitterColorOp
Version: Phaser v3.90.0
On this page
EmitterColorOp
This class is responsible for taking control over the color property
in the Particle class and managing its emission and updating functions.
See the ParticleEmitter class for more details on emitter op configuration.
Constructor
new EmitterColorOp(key)
Parameters
name type optional description
key string No The name of the property.
Scope : static
Extends
Phaser.GameObjects.Particles.EmitterOp
Source: src/gameobjects/particles/EmitterColorOp.js#L14
Since: 3.60.0
Inherited Members ​
From Phaser.GameObjects.Particles.EmitterOp :
active
counter
current
defaultValue
direction
ease
emitOnly
end
interpolation
method
onEmit
onUpdate
propertyKey
propertyValue
start
steps
yoyo
Public Members ​
b ​
b: Array.<number> ​
Description:
An array containing the blue color values.
Populated during the setMethods method.
Source: src/gameobjects/particles/EmitterColorOp.js#L65
Since: 3.60.0
g ​
g: Array.<number> ​
Description:
An array containing the green color values.
Populated during the setMethods method.
Source: src/gameobjects/particles/EmitterColorOp.js#L54
Since: 3.60.0
r ​
r: Array.<number> ​
Description:
An array containing the red color values.
Populated during the setMethods method.
Source: src/gameobjects/particles/EmitterColorOp.js#L43
Since: 3.60.0
Inherited Methods ​
From Phaser.GameObjects.Particles.EmitterOp :
defaultEmit
defaultUpdate
destroy
has
hasBoth
hasEither
loadConfig
onChange
proxyEmit
proxyUpdate
randomRangedIntEmit
randomRangedValueEmit
randomStaticValueEmit
staticValueEmit
staticValueUpdate
steppedEmit
toJSON
Public Methods ​
easedValueEmit ​
<instance> easedValueEmit(particle, key) ​
Description:
An onEmit callback for an eased property.
It prepares the particle for easing by Phaser.GameObjects.Particles.EmitterColorOp#easeValueUpdate .
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The particle.
key string No The name of the property.
Overrides: Phaser.GameObjects.Particles.EmitterOp#easedValueEmit
Returns: number - {@link Phaser.GameObjects.Particles.EmitterColorOp#start}, as the new value of the property.
Source: src/gameobjects/particles/EmitterColorOp.js#L157
Since: 3.60.0
easeValueUpdate ​
<instance> easeValueUpdate(particle, key, t) ​
Description:
An onUpdate callback that returns an eased value between the
Phaser.GameObjects.Particles.EmitterColorOp#start and Phaser.GameObjects.Particles.EmitterColorOp#end
range.
Parameters:
name type optional description
particle Phaser.GameObjects.Particles.Particle No The particle.
key string No The name of the property.
t number No The current normalized lifetime of the particle, between 0 (birth) and 1 (death).
Overrides: Phaser.GameObjects.Particles.EmitterOp#easeValueUpdate
Returns: number - The new value of the property.
Source: src/gameobjects/particles/EmitterColorOp.js#L177
Since: 3.60.0
getMethod ​
<instance> getMethod() ​
Description:
Checks the type of EmitterOp.propertyValue to determine which
method is required in order to return values from this op function.
Overrides: Phaser.GameObjects.Particles.EmitterOp#getMethod
Returns: number - A number between 0 and 9 which should be passed to setMethods .
Source: src/gameobjects/particles/EmitterColorOp.js#L77
Since: 3.60.0
setEase ​
<instance> setEase(ease) ​
Description:
Sets the Ease function to use for Color interpolation.
Parameters:
name type optional description
ease string No The string-based name of the Ease function to use.
Source: src/gameobjects/particles/EmitterColorOp.js#L142
Since: 3.60.0
setMethods ​
<instance> setMethods() ​
Description:
Sets the EmitterColorOp method values, if in use.
Overrides: Phaser.GameObjects.Particles.EmitterOp#setMethods
Returns: Phaser.GameObjects.Particles.EmitterColorOp - This Emitter Op object.
Source: src/gameobjects/particles/EmitterColorOp.js#L91
Since: 3.60.0
Previous
NineSlice
Next
EmitterOp
Inherited Members
Public Members
b
g
r
Inherited Methods
Public Methods
easedValueEmit
easeValueUpdate
getMethod
setEase
setMethods
