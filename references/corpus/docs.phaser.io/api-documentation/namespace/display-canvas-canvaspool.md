# Phaser.Display.Canvas.CanvasPool | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/display-canvas-canvaspool

Phaser API Documentation
Namespaces
Phaser.Display.Canvas.CanvasPool
Version: Phaser v3.90.0
On this page
Phaser.Display.Canvas.CanvasPool
Scope: static
Source: src/display/canvas/CanvasPool.js#L16
Since: 3.0.0
Static functions ​
create ​
<static> create(parent, [width], [height], [canvasType], [selfParent]) ​
Description:
Creates a new Canvas DOM element, or pulls one from the pool if free.
Parameters:
name type optional default description
parent * No The parent of the Canvas object.
width number Yes 1 The width of the Canvas.
height number Yes 1 The height of the Canvas.
canvasType number Yes "Phaser.CANVAS" The type of the Canvas. Either Phaser.CANVAS or Phaser.WEBGL .
selfParent boolean Yes false Use the generated Canvas element as the parent?
Returns: HTMLCanvasElement - The canvas element that was created or pulled from the pool
Source: src/display/canvas/CanvasPool.js#L29
Since: 3.0.0
create2D ​
<static> create2D(parent, [width], [height]) ​
Description:
Creates a new Canvas DOM element, or pulls one from the pool if free.
Parameters:
name type optional default description
parent * No The parent of the Canvas object.
width number Yes 1 The width of the Canvas.
height number Yes 1 The height of the Canvas.
Returns: HTMLCanvasElement - The created canvas.
Source: src/display/canvas/CanvasPool.js#L91
Since: 3.0.0
createWebGL ​
<static> createWebGL(parent, [width], [height]) ​
Description:
Creates a new Canvas DOM element, or pulls one from the pool if free.
Parameters:
name type optional default description
parent * No The parent of the Canvas object.
width number Yes 1 The width of the Canvas.
height number Yes 1 The height of the Canvas.
Returns: HTMLCanvasElement - The created WebGL canvas.
Source: src/display/canvas/CanvasPool.js#L108
Since: 3.0.0
disableSmoothing ​
<static> disableSmoothing() ​
Description:
Disable context smoothing on any new Canvas element created.
Source: src/display/canvas/CanvasPool.js#L218
Since: 3.0.0
enableSmoothing ​
<static> enableSmoothing() ​
Description:
Enable context smoothing on any new Canvas element created.
Source: src/display/canvas/CanvasPool.js#L229
Since: 3.0.0
first ​
<static> first([canvasType]) ​
Description:
Gets the first free canvas index from the pool.
Parameters:
name type optional default description
canvasType number Yes "Phaser.CANVAS" The type of the Canvas. Either Phaser.CANVAS or Phaser.WEBGL .
Returns: HTMLCanvasElement - The first free canvas, or null if a WebGL canvas was requested or if the pool doesn't have free canvases.
Source: src/display/canvas/CanvasPool.js#L125
Since: 3.0.0
free ​
<static> free() ​
Description:
Gets the total number of free canvas elements in the pool.
Returns: number - The number of free canvases.
Source: src/display/canvas/CanvasPool.js#L205
Since: 3.0.0
remove ​
<static> remove(parent) ​
Description:
Looks up a canvas based on its parent, and if found puts it back in the pool, freeing it up for re-use.
The canvas has its width and height set to 1, and its parent attribute nulled.
Parameters:
name type optional description
parent * No The canvas or the parent of the canvas to free.
Source: src/display/canvas/CanvasPool.js#L157
Since: 3.0.0
total ​
<static> total() ​
Description:
Gets the total number of used canvas elements in the pool.
Returns: number - The number of used canvases.
Source: src/display/canvas/CanvasPool.js#L182
Since: 3.0.0
Previous
Phaser.Display.Canvas.CanvasInterpolation
Next
Phaser.Display.Canvas.Smoothing
Static functions
create
create2D
createWebGL
disableSmoothing
enableSmoothing
first
free
remove
total
