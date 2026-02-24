# Phaser.Core | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/core

Phaser API Documentation
Namespaces
Phaser.Core
Version: Phaser v3.90.0
On this page
Phaser.Core
Scope: static
Source: src/core/index.js#L7
Static functions ​
Config
TimeStep
Static functions ​
CreateRenderer ​
<static> CreateRenderer(game) ​
Description:
Called automatically by Phaser.Game and responsible for creating the renderer it will use.
Relies upon two webpack global flags to be defined: WEBGL_RENDERER and CANVAS_RENDERER during build time, but not at run-time.
Parameters:
name type optional description
game Phaser.Game No The Phaser.Game instance on which the renderer will be set.
Source: src/core/CreateRenderer.js#L12
Since: 3.0.0
DebugHeader ​
<static> DebugHeader(game) ​
Description:
Called automatically by Phaser.Game and responsible for creating the console.log debug header.
You can customize or disable the header via the Game Config object.
Parameters:
name type optional description
game Phaser.Game No The Phaser.Game instance which will output this debug header.
Source: src/core/DebugHeader.js#L9
Since: 3.0.0
VisibilityHandler ​
<static> VisibilityHandler(game) ​
Description:
The Visibility Handler is responsible for listening out for document level visibility change events.
This includes visibilitychange if the browser supports it, and blur and focus events. It then uses
the provided Event Emitter and fires the related events.
Parameters:
name type optional description
game Phaser.Game No The Game instance this Visibility Handler is working on.
Fires: Phaser.Core.Events#event:BLUR , Phaser.Core.Events#event:FOCUS , Phaser.Core.Events#event:HIDDEN , Phaser.Core.Events#event:VISIBLE
Source: src/core/VisibilityHandler.js#L9
Since: 3.0.0
Static functions ​
Events
Previous
Phaser.Core.Events
Next
Phaser.Create.Palettes
Static functions
Static functions
CreateRenderer
DebugHeader
VisibilityHandler
Static functions
