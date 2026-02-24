# Light | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-light

Phaser API Documentation
Class
Light
Version: Phaser v3.90.0
On this page
Light
A 2D Light.
These are created by the Phaser.GameObjects.LightsManager , available from within a scene via this.lights .
Any Game Objects using the Light2D pipeline will then be affected by these Lights as long as they have a normal map.
They can also simply be used to represent a point light for your own purposes.
Lights cannot be added to Containers. They are designed to exist in the root of a Scene.
Constructor
new Light(x, y, radius, r, g, b, intensity)
Parameters
name type optional description
x number No The horizontal position of the light.
y number No The vertical position of the light.
radius number No The radius of the light.
r number No The red color of the light. A value between 0 and 1.
g number No The green color of the light. A value between 0 and 1.
b number No The blue color of the light. A value between 0 and 1.
intensity number No The intensity of the light.
Scope : static
Extends
Phaser.Geom.Circle
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/lights/Light.js#L13
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
From Phaser.GameObjects.Components.Visible :
visible
From Phaser.Geom.Circle :
bottom
diameter
left
radius
right
top
type
x
y
Public Members ​
cameraFilter ​
cameraFilter: number ​
Description:
A bitmask that controls if this Game Object is drawn by a Camera or not.
Not usually set directly, instead call Camera.ignore , however you can
set this property directly using the Camera.id property:
Source: src/gameobjects/lights/Light.js#L89
Since: 3.0.0
color ​
color: Phaser.Display.RGB ​
Description:
The color of the light.
Source: src/gameobjects/lights/Light.js#L59
Since: 3.50.0
displayHeight ​
displayHeight: number ​
Description:
The height of this Light Game Object. This is the same as Light.diameter .
Source: src/gameobjects/lights/Light.js#L130
Since: 3.60.0
displayWidth ​
displayWidth: number ​
Description:
The width of this Light Game Object. This is the same as Light.diameter .
Source: src/gameobjects/lights/Light.js#L109
Since: 3.60.0
height ​
height: number ​
Description:
The height of this Light Game Object. This is the same as Light.diameter .
Source: src/gameobjects/lights/Light.js#L172
Since: 3.60.0
intensity ​
intensity: number ​
Description:
The intensity of the light.
Source: src/gameobjects/lights/Light.js#L68
Since: 3.50.0
renderFlags ​
renderFlags: number ​
Description:
The flags that are compared against RENDER_MASK to determine if this Game Object will render or not.
The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.
If those components are not used by your custom class then you can use this bitmask as you wish.
Source: src/gameobjects/lights/Light.js#L77
Since: 3.0.0
width ​
width: number ​
Description:
The width of this Light Game Object. This is the same as Light.diameter .
Source: src/gameobjects/lights/Light.js#L151
Since: 3.60.0
Inherited Methods ​
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
From Phaser.GameObjects.Components.Visible :
setVisible
From Phaser.Geom.Circle :
contains
getPoint
getPoints
getRandomPoint
isEmpty
setEmpty
setPosition
setTo
Public Methods ​
setColor ​
<instance> setColor(rgb) ​
Description:
Set the color of the light from a single integer RGB value.
Parameters:
name type optional description
rgb number No The integer RGB color of the light.
Returns: Phaser.GameObjects.Light - This Light object.
Source: src/gameobjects/lights/Light.js#L209
Since: 3.0.0
setIntensity ​
<instance> setIntensity(intensity) ​
Description:
Set the intensity of the light.
Parameters:
name type optional description
intensity number No The intensity of the light.
Returns: Phaser.GameObjects.Light - This Light object.
Source: src/gameobjects/lights/Light.js#L228
Since: 3.0.0
setRadius ​
<instance> setRadius(radius) ​
Description:
Set the radius of the light.
Parameters:
name type optional description
radius number No The radius of the light.
Returns: Phaser.GameObjects.Light - This Light object.
Source: src/gameobjects/lights/Light.js#L245
Since: 3.0.0
willRender ​
<instance> willRender(camera) ​
Description:
Compares the renderMask with the renderFlags to see if this Game Object will render or not.
Also checks the Game Object against the given Cameras exclusion list.
Parameters:
name type optional description
camera Phaser.Cameras.Scene2D.Camera No The Camera to check against this Game Object.
Returns: boolean - True if the Game Object should be rendered, otherwise false.
Source: src/gameobjects/lights/Light.js#L193
Since: 3.50.0
Constants: ​
Public Members ​
RENDER_MASK ​
RENDER_MASK: number ​
Description:
The bitmask that GameObject.renderFlags is compared against to determine if the Game Object will render or not.
Source: src/gameobjects/lights/Light.js#L264
Previous
Layer
Next
LightsManager
Inherited Members
Public Members
cameraFilter
color
displayHeight
displayWidth
height
intensity
renderFlags
width
Inherited Methods
Public Methods
setColor
setIntensity
setRadius
willRender
Constants:
Public Members
RENDER_MASK
