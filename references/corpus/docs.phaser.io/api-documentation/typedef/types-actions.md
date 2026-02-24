# Types.Actions | Phaser Help

Source: https://docs.phaser.io/api-documentation/typedef/types-actions

Phaser API Documentation
Typedefs
Types.Actions
Version: Phaser v3.90.0
On this page
Types.Actions
CallCallback ​
<static> CallCallback ​
Type : function
Member of : Phaser.Types.Actions
Source: src/actions/typedefs/CallCallback.js#L1
Since: 3.0.0
GridAlignConfig ​
<static> GridAlignConfig ​
name type optional default description
width number Yes -1 The width of the grid in items (not pixels). -1 means lay all items out horizontally, regardless of quantity. If both this value and height are set to -1 then this value overrides it and the height value is ignored.
height number Yes -1 The height of the grid in items (not pixels). -1 means lay all items out vertically, regardless of quantity. If both this value and width are set to -1 then width overrides it and this value is ignored.
cellWidth number Yes 1 The width of the cell, in pixels, in which the item is positioned.
cellHeight number Yes 1 The height of the cell, in pixels, in which the item is positioned.
position number Yes 0 The alignment position. One of the Phaser.Display.Align consts such as TOP_LEFT or RIGHT_CENTER .
x number Yes 0 Optionally place the top-left of the final grid at this coordinate.
y number Yes 0 Optionally place the top-left of the final grid at this coordinate.
Type : object
Member of : Phaser.Types.Actions
Source: src/actions/typedefs/GridAlignConfig.js#L1
Since: 3.0.0
Previous
Tweens
Next
Types.Animations
CallCallback
<static> CallCallback
GridAlignConfig
<static> GridAlignConfig
