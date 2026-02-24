# Phaser | Phaser Help

Source: https://docs.phaser.io/api-documentation/constant/phaser

Phaser API Documentation
Constants
Phaser
Version: Phaser v3.90.0
On this page
Phaser
VERSION ​
VERSION: string ​
Description:
Phaser Release Version
Source: src/const.js#L15
Since: 3.0.0
LOG_VERSION ​
LOG_VERSION: string ​
Description:
Phaser Release Version as displayed in the console.log header URL.
Source: src/const.js#L25
Since: 3.87.0
AUTO ​
AUTO: number ​
Description:
This setting will auto-detect if the browser is capable of suppporting WebGL.
If it is, it will use the WebGL Renderer. If not, it will fall back to the Canvas Renderer.
Source: src/const.js#L39
Since: 3.0.0
CANVAS ​
CANVAS: number ​
Description:
Forces Phaser to only use the Canvas Renderer, regardless if the browser supports
WebGL or not.
Source: src/const.js#L50
Since: 3.0.0
WEBGL ​
WEBGL: number ​
Description:
Forces Phaser to use the WebGL Renderer. If the browser does not support it, there is
no fallback to Canvas with this setting, so you should trap it and display a suitable
message to the user.
Source: src/const.js#L61
Since: 3.0.0
HEADLESS ​
HEADLESS: number ​
Description:
A Headless Renderer doesn't create either a Canvas or WebGL Renderer. However, it still
absolutely relies on the DOM being present and available. This mode is meant for unit testing,
not for running Phaser on the server, which is something you really shouldn't do.
Source: src/const.js#L73
Since: 3.0.0
FOREVER ​
FOREVER: number ​
Description:
In Phaser the value -1 means 'forever' in lots of cases, this const allows you to use it instead
to help you remember what the value is doing in your code.
Source: src/const.js#L85
Since: 3.0.0
NONE ​
NONE: number ​
Description:
Direction constant.
Source: src/const.js#L96
Since: 3.0.0
UP ​
UP: number ​
Description:
Direction constant.
Source: src/const.js#L106
Since: 3.0.0
DOWN ​
DOWN: number ​
Description:
Direction constant.
Source: src/const.js#L116
Since: 3.0.0
LEFT ​
LEFT: number ​
Description:
Direction constant.
Source: src/const.js#L126
Since: 3.0.0
RIGHT ​
RIGHT: number ​
Description:
Direction constant.
Source: src/const.js#L136
Since: 3.0.0
Previous
Tweens
Next
Constants
VERSION
LOG_VERSION
AUTO
CANVAS
WEBGL
HEADLESS
FOREVER
NONE
UP
DOWN
LEFT
RIGHT
