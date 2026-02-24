# Phaser.Physics.Arcade.ProcessX | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-processx

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.ProcessX
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.ProcessX
Scope: static
Source: src/physics/arcade/ProcessX.js#L403
Static functions ​
BlockCheck ​
<static> BlockCheck() ​
Description:
Blocked Direction checks, because it doesn't matter if an object can be pushed
or not, blocked is blocked.
Returns: number - The BlockCheck result. 0 = not blocked. 1 = Body 1 blocked. 2 = Body 2 blocked.
Source: src/physics/arcade/ProcessX.js#L71
Since: 3.50.0
Check ​
<static> Check() ​
Description:
The main check function. Runs through one of the four possible tests and returns the results.
Returns: boolean - true if a check passed, otherwise false .
Source: src/physics/arcade/ProcessX.js#L118
Since: 3.50.0
Run ​
<static> Run(side) ​
Description:
The main check function. Runs through one of the four possible tests and returns the results.
Parameters:
name type optional description
side number No The side to test. As passed in by the Check function.
Returns: boolean - Always returns true .
Source: src/physics/arcade/ProcessX.js#L169
Since: 3.50.0
RunImmovableBody1 ​
<static> RunImmovableBody1(blockedState) ​
Description:
This function is run when Body1 is Immovable and Body2 is not.
Parameters:
name type optional description
blockedState number No The block state value.
Source: src/physics/arcade/ProcessX.js#L331
Since: 3.50.0
RunImmovableBody2 ​
<static> RunImmovableBody2(blockedState) ​
Description:
This function is run when Body2 is Immovable and Body1 is not.
Parameters:
name type optional description
blockedState number No The block state value.
Source: src/physics/arcade/ProcessX.js#L367
Since: 3.50.0
Set ​
<static> Set(b1, b2, ov) ​
Description:
Sets all of the local processing values and calculates the velocity exchanges.
Then runs BlockCheck and returns the value from it.
This method is called by Phaser.Physics.Arcade.SeparateX and should not be
called directly.
Parameters:
name type optional description
b1 Phaser.Physics.Arcade.Body No The first Body to separate.
b2 Phaser.Physics.Arcade.Body No The second Body to separate.
ov number No The overlap value.
Returns: number - The BlockCheck result. 0 = not blocked. 1 = Body 1 blocked. 2 = Body 2 blocked.
Source: src/physics/arcade/ProcessX.js#L25
Since: 3.50.0
Previous
Phaser.Physics.Arcade.Events
Next
Phaser.Physics.Arcade.ProcessY
Static functions
BlockCheck
Check
Run
RunImmovableBody1
RunImmovableBody2
Set
