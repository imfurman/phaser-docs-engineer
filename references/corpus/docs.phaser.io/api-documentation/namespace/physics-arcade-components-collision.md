# Phaser.Physics.Arcade.Components.Collision | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/physics-arcade-components-collision

Phaser API Documentation
Namespaces
Phaser.Physics.Arcade.Components.Collision
Version: Phaser v3.90.0
On this page
Phaser.Physics.Arcade.Components.Collision
Scope: static
Source: src/physics/arcade/components/Collision.js#L9
Since: 3.70.0
Static functions ​
addCollidesWith ​
<instance> addCollidesWith(category) ​
Description:
Adds the given Collision Category to the list of those that this
Arcade Physics Body will collide with.
Parameters:
name type optional description
category number No The collision category to add.
Returns: Phaser.Physics.Arcade.Components.Collision - This Game Object.
Source: src/physics/arcade/components/Collision.js#L60
Since: 3.70.0
removeCollidesWith ​
<instance> removeCollidesWith(category) ​
Description:
Removes the given Collision Category from the list of those that this
Arcade Physics Body will collide with.
Parameters:
name type optional description
category number No The collision category to add.
Returns: Phaser.Physics.Arcade.Components.Collision - This Game Object.
Source: src/physics/arcade/components/Collision.js#L80
Since: 3.70.0
resetCollisionCategory ​
<instance> resetCollisionCategory() ​
Description:
Resets the Collision Category and Mask back to the defaults,
which is to collide with everything.
Returns: Phaser.Physics.Arcade.Components.Collision - This Game Object.
Source: src/physics/arcade/components/Collision.js#L130
Since: 3.70.0
setCollidesWith ​
<instance> setCollidesWith(categories) ​
Description:
Sets all of the Collision Categories that this Arcade Physics Body
will collide with. You can either pass a single category value, or
an array of them.
Calling this method will reset all of the collision categories,
so only those passed to this method are enabled.
If you wish to add a new category to the existing mask, call
the addCollisionCategory method.
If you wish to reset the collision category and mask, call
the resetCollisionCategory method.
Parameters:
name type optional description
categories number | Array.<number> No The collision category to collide with, or an array of them.
Returns: Phaser.Physics.Arcade.Components.Collision - This Game Object.
Source: src/physics/arcade/components/Collision.js#L100
Since: 3.70.0
setCollisionCategory ​
<instance> setCollisionCategory(category) ​
Description:
Sets the Collision Category that this Arcade Physics Body
will use in order to determine what it can collide with.
It can only have one single category assigned to it.
If you wish to reset the collision category and mask, call
the resetCollisionCategory method.
Parameters:
name type optional description
category number No The collision category.
Returns: Phaser.Physics.Arcade.Components.Collision - This Game Object.
Source: src/physics/arcade/components/Collision.js#L17
Since: 3.70.0
willCollideWith ​
<instance> willCollideWith(category) ​
Description:
Checks to see if the given Collision Category will collide with
this Arcade Physics object or not.
Parameters:
name type optional description
category number No Collision category value to test.
Returns: boolean - true if the given category will collide with this object, otherwise false .
Source: src/physics/arcade/components/Collision.js#L42
Since: 3.70.0
Previous
Phaser.Physics.Arcade.Components.Bounce
Next
Phaser.Physics.Arcade.Components.Debug
Static functions
addCollidesWith
removeCollidesWith
resetCollisionCategory
setCollidesWith
setCollisionCategory
willCollideWith
