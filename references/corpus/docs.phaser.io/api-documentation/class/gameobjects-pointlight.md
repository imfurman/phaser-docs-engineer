# PointLight | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-pointlight

Phaser API Documentation
Class
PointLight
Version: Phaser v3.90.0
On this page
PointLight
The Point Light Game Object provides a way to add a point light effect into your game,
without the expensive shader processing requirements of the traditional Light Game Object.
The difference is that the Point Light renders using a custom shader, designed to give the
impression of a point light source, of variable radius, intensity and color, in your game.
However, unlike the Light Game Object, it does not impact any other Game Objects, or use their
normal maps for calcuations. This makes them extremely fast to render compared to Lights
and perfect for special effects, such as flickering torches or muzzle flashes.
For maximum performance you should batch Point Light Game Objects together. This means
ensuring they follow each other consecutively on the display list. Ideally, use a Layer
Game Object and then add just Point Lights to it, so that it can batch together the rendering
of the lights. You don't have to do this, and if you've only a handful of Point Lights in
your game then it's perfectly safe to mix them into the display list as normal. However, if
you're using a large number of them, please consider how they are mixed into the display list.
The renderer will automatically cull Point Lights. Those with a radius that does not intersect
with the Camera will be skipped in the rendering list. This happens automatically and the
culled state is refreshed every frame, for every camera.
The origin of a Point Light is always 0.5 and it cannot be changed.
Point Lights are a WebGL only feature and do not have a Canvas counterpart.
Constructor
new PointLight(scene, x, y, [color], [radius], [intensity], [attenuation])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Point Light belongs. A Point Light can only belong to one Scene at a time.
x number No The horizontal position of this Point Light in the world.
y number No The vertical position of this Point Light in the world.
color number Yes "0xffffff" The color of the Point Light, given as a hex value.
radius number Yes 128 The radius of the Point Light.
intensity number Yes 1 The intensity, or color blend, of the Point Light.
attenuation number Yes 0.1 The attenuation of the Point Light. This is the reduction of light from the center point.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/pointlight/PointLight.js#L14
Since: 3.50.0
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
attenuation ​
attenuation: number ​
Description:
The attenuation of the Point Light.
This value controls the force with which the light falls-off from the center of the light.
Use small float-based values, i.e. 0.1.
Source: src/gameobjects/pointlight/PointLight.js#L120
Since: 3.50.0
color ​
color: Phaser.Display.Color ​
Description:
The color of this Point Light. This property is an instance of a
Color object, so you can use the methods within it, such as setTo(r, g, b)
to change the color value.
Source: src/gameobjects/pointlight/PointLight.js#L98
Since: 3.50.0
intensity ​
intensity: number ​
Description:
The intensity of the Point Light.
The colors of the light are multiplied by this value during rendering.
Source: src/gameobjects/pointlight/PointLight.js#L109
Since: 3.50.0
radius ​
radius: number ​
Description:
The radius of the Point Light.
Source: src/gameobjects/pointlight/PointLight.js#L140
Since: 3.50.0
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
From Phaser.GameObjects.Components.GetBounds :
getBottomCenter
getBottomLeft
getBottomRight
getBounds
getCenter
getLeftCenter
getRightCenter
getTopCenter
getTopLeft
getTopRight
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
toJSON
update
willRender
Previous
Plane
Next
Polygon
Inherited Members
Public Members
attenuation
color
intensity
radius
Inherited Methods
