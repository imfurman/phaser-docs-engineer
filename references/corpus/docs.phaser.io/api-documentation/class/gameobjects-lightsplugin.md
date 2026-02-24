# LightsPlugin | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-lightsplugin

Phaser API Documentation
Class
LightsPlugin
Version: Phaser v3.90.0
On this page
LightsPlugin
A Scene plugin that provides a Phaser.GameObjects.LightsManager for the Light2D pipeline.
Available from within a Scene via this.lights .
Add Lights using the Phaser.GameObjects.LightsManager#addLight method:
// Enable the Lights Manager because it is disabled by default
this . lights . enable ( ) ;
// Create a Light at [400, 300] with a radius of 200
this . lights . addLight ( 400 , 300 , 200 ) ;
For Game Objects to be affected by the Lights when rendered, you will need to set them to use the Light2D pipeline like so:
sprite . setPipeline ( 'Light2D' ) ;
Note that you cannot use this pipeline on Graphics Game Objects or Shape Game Objects.
Constructor
new LightsPlugin(scene)
Parameters
name type optional description
scene Phaser.Scene No The Scene that this Lights Plugin belongs to.
Scope : static
Extends
Phaser.GameObjects.LightsManager
Source: src/gameobjects/lights/LightsPlugin.js#L12
Since: 3.0.0
Inherited Members ​
From Phaser.GameObjects.LightsManager :
active
ambientColor
lights
maxLights
visibleLights
Public Members ​
scene ​
scene: Phaser.Scene ​
Description:
A reference to the Scene that this Lights Plugin belongs to.
Source: src/gameobjects/lights/LightsPlugin.js#L52
Since: 3.0.0
systems ​
systems: Phaser.Scenes.Systems ​
Description:
A reference to the Scene's systems.
Source: src/gameobjects/lights/LightsPlugin.js#L61
Since: 3.0.0
Inherited Methods ​
From Phaser.GameObjects.LightsManager :
addLight
addPointLight
disable
enable
getLightCount
getLights
getMaxVisibleLights
removeLight
setAmbientColor
shutdown
Public Methods ​
boot ​
<instance> boot() ​
Description:
Boot the Lights Plugin.
Source: src/gameobjects/lights/LightsPlugin.js#L78
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroy the Lights Plugin.
Cleans up all references.
Overrides: Phaser.GameObjects.LightsManager#destroy
Source: src/gameobjects/lights/LightsPlugin.js#L92
Since: 3.0.0
Previous
LightsManager
Next
Line
Inherited Members
Public Members
scene
systems
Inherited Methods
Public Methods
boot
destroy
