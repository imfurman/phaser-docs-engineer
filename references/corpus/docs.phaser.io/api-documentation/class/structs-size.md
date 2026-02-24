# Size | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/structs-size

Phaser API Documentation
Class
Size
Version: Phaser v3.90.0
On this page
Size
The Size component allows you to set width and height properties and define the relationship between them.
The component can automatically maintain the aspect ratios between the two values, and clamp them
to a defined min-max range. You can also control the dominant axis. When dimensions are given to the Size component
that would cause it to exceed its min-max range, the dimensions are adjusted based on the dominant axis.
Constructor
new Size([width], [height], [aspectMode], [parent])
Parameters
name type optional default description
width number Yes 0 The width of the Size component.
height number Yes "width" The height of the Size component. If not given, it will use the width .
aspectMode number Yes 0 The aspect mode of the Size component. Defaults to 0, no mode.
parent any Yes null The parent of this Size component. Can be any object with public width and height properties. Dimensions are clamped to keep them within the parent bounds where possible.
Scope : static
Source: src/structs/Size.js#L12
Since: 3.16.0
Public Members ​
aspectMode ​
aspectMode: number ​
Description:
The aspect mode this Size component will use when calculating its dimensions.
This property is read-only. To change it use the setAspectMode method.
Source: src/structs/Size.js#L71
Since: 3.16.0
aspectRatio ​
aspectRatio: number ​
Description:
The proportional relationship between the width and height.
This property is read-only and is updated automatically when either the width or height properties are changed,
depending on the aspect mode.
Source: src/structs/Size.js#L82
Since: 3.16.0
height ​
height: number ​
Description:
The height of this Size component.
This value is clamped to the range specified by minHeight and maxHeight , if enabled.
A height can never be less than zero.
Changing this value will automatically update the width if the aspect ratio lock is enabled.
You can also use the setHeight and getHeight methods.
Source: src/structs/Size.js#L692
Since: 3.16.0
maxHeight ​
maxHeight: number ​
Description:
The maximum allowed height.
This value is read-only. To change it see the setMax method.
Source: src/structs/Size.js#L130
Since: 3.16.0
maxWidth ​
maxWidth: number ​
Description:
The maximum allowed width.
This value is read-only. To change it see the setMax method.
Source: src/structs/Size.js#L119
Since: 3.16.0
minHeight ​
minHeight: number ​
Description:
The minimum allowed height.
Cannot be less than zero.
This value is read-only. To change it see the setMin method.
Source: src/structs/Size.js#L107
Since: 3.16.0
minWidth ​
minWidth: number ​
Description:
The minimum allowed width.
Cannot be less than zero.
This value is read-only. To change it see the setMin method.
Source: src/structs/Size.js#L95
Since: 3.16.0
snapTo ​
snapTo: Phaser.Math.Vector2 ​
Description:
A Vector2 containing the horizontal and vertical snap values, which the width and height are snapped to during resizing.
By default this is disabled.
This property is read-only. To change it see the setSnap method.
Source: src/structs/Size.js#L141
Since: 3.16.0
width ​
width: number ​
Description:
The width of this Size component.
This value is clamped to the range specified by minWidth and maxWidth , if enabled.
A width can never be less than zero.
Changing this value will automatically update the height if the aspect ratio lock is enabled.
You can also use the setWidth and getWidth methods.
Source: src/structs/Size.js#L664
Since: 3.16.0
Public Methods ​
constrain ​
<instance> constrain([width], [height], [fit]) ​
Description:
The current width and height are adjusted to fit inside the given dimensions, while keeping the aspect ratio.
If fit is true there may be some space inside the target area which is not covered if its aspect ratio differs.
If fit is false the size may extend further out than the target area if the aspect ratios differ.
If this Size component has a parent set, then the width and height passed to this method will be clamped so
it cannot exceed that of the parent.
Parameters:
name type optional default description
width number Yes 0 The new width of the Size component.
height number Yes The new height of the Size component. If not given, it will use the width value.
fit boolean Yes true Perform a fit (true) constraint, or an envelop (false) constraint.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L452
Since: 3.16.0
copy ​
<instance> copy(destination) ​
Description:
Copies the aspect mode, aspect ratio, width and height from this Size component
to the given Size component. Note that the parent, if set, is not copied across.
Parameters:
name type optional description
destination Phaser.Structs.Size No The Size component to copy the values to.
Returns: Phaser.Structs.Size - The updated destination Size component.
Source: src/structs/Size.js#L628
Since: 3.16.0
destroy ​
<instance> destroy() ​
Description:
Destroys this Size component.
This clears the local properties and any parent object, if set.
A destroyed Size component cannot be re-used.
Source: src/structs/Size.js#L648
Since: 3.16.0
envelop ​
<instance> envelop([width], [height]) ​
Description:
The current width and height are adjusted so that they fully envelope the given dimensions, while keeping the aspect ratio.
The size may extend further out than the target area if the aspect ratios differ.
If this Size component has a parent set, then the values are clamped so that it never exceeds the parent
on the longest axis.
Parameters:
name type optional default description
width number Yes 0 The new width of the Size component.
height number Yes The new height of the Size component. If not given, it will use the width value.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L542
Since: 3.16.0
fitTo ​
<instance> fitTo([width], [height]) ​
Description:
The current width and height are adjusted to fit inside the given dimensions, while keeping the aspect ratio.
There may be some space inside the target area which is not covered if its aspect ratio differs.
If this Size component has a parent set, then the width and height passed to this method will be clamped so
it cannot exceed that of the parent.
Parameters:
name type optional default description
width number Yes 0 The new width of the Size component.
height number Yes The new height of the Size component. If not given, it will use the width value.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L521
Since: 3.16.0
getNewHeight ​
<instance> getNewHeight(value, [checkParent]) ​
Description:
Takes a new height and passes it through the min/max clamp and then checks it doesn't exceed the parent height.
Parameters:
name type optional default description
value number No The value to clamp and check.
checkParent boolean Yes true Check the given value against the parent, if set.
Returns: number - The modified height value.
Source: src/structs/Size.js#L427
Since: 3.16.0
getNewWidth ​
<instance> getNewWidth(value, [checkParent]) ​
Description:
Takes a new width and passes it through the min/max clamp and then checks it doesn't exceed the parent width.
Parameters:
name type optional default description
value number No The value to clamp and check.
checkParent boolean Yes true Check the given value against the parent, if set.
Returns: number - The modified width value.
Source: src/structs/Size.js#L402
Since: 3.16.0
resize ​
<instance> resize(width, [height]) ​
Description:
Sets a new width and height for this Size component and updates the aspect ratio based on them.
It doesn't change the aspectMode and still factors in size limits such as the min max and parent bounds.
Parameters:
name type optional default description
width number No The new width of the Size component.
height number Yes "width" The new height of the Size component. If not given, it will use the width .
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L380
Since: 3.16.0
setAspectMode ​
<instance> setAspectMode([value]) ​
Description:
Sets the aspect mode of this Size component.
The aspect mode controls what happens when you modify the width or height properties, or call setSize .
It can be a number from 0 to 4, or a Size constant:
NONE = Do not make the size fit the aspect ratio. Change the ratio when the size changes.
WIDTH_CONTROLS_HEIGHT = The height is automatically adjusted based on the width.
HEIGHT_CONTROLS_WIDTH = The width is automatically adjusted based on the height.
FIT = The width and height are automatically adjusted to fit inside the given target area, while keeping the aspect ratio. Depending on the aspect ratio there may be some space inside the area which is not covered.
ENVELOP = The width and height are automatically adjusted to make the size cover the entire target area while keeping the aspect ratio. This may extend further out than the target size.
Calling this method automatically recalculates the width and the height , if required.
Parameters:
name type optional default description
value number Yes 0 The aspect mode value.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L156
Since: 3.16.0
setAspectRatio ​
<instance> setAspectRatio(ratio) ​
Description:
Sets a new aspect ratio, overriding what was there previously.
It then calls setSize immediately using the current dimensions.
Parameters:
name type optional description
ratio number No The new aspect ratio.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L361
Since: 3.16.0
setCSS ​
<instance> setCSS(element) ​
Description:
Sets the values of this Size component to the element.style.width and height
properties of the given DOM Element. The properties are set as px values.
Parameters:
name type optional description
element HTMLElement No The DOM Element to set the CSS style on.
Source: src/structs/Size.js#L610
Since: 3.17.0
setHeight ​
<instance> setHeight(height) ​
Description:
Sets the height of this Size component.
Depending on the aspect mode, changing the height may also update the width and aspect ratio.
Parameters:
name type optional description
height number No The new height of the Size component.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L580
Since: 3.16.0
setMax ​
<instance> setMax([width], [height]) ​
Description:
Set the maximum width and height values this Size component will allow.
Setting this will automatically adjust both the width and height properties to ensure they are within range.
Note that based on the aspect mode, and if this Size component has a parent set or not, the maximums set here
can be exceed in some situations.
Parameters:
name type optional default description
width number Yes "Number.MAX_VALUE" The maximum allowed width of the Size component.
height number Yes "width" The maximum allowed height of the Size component. If not given, it will use the width .
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L276
Since: 3.16.0
setMin ​
<instance> setMin([width], [height]) ​
Description:
Set the minimum width and height values this Size component will allow.
The minimum values can never be below zero, or greater than the maximum values.
Setting this will automatically adjust both the width and height properties to ensure they are within range.
Note that based on the aspect mode, and if this Size component has a parent set or not, the minimums set here
can be exceed in some situations.
Parameters:
name type optional default description
width number Yes 0 The minimum allowed width of the Size component.
height number Yes "width" The minimum allowed height of the Size component. If not given, it will use the width .
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L247
Since: 3.16.0
setParent ​
<instance> setParent([parent]) ​
Description:
Sets, or clears, the parent of this Size component.
To clear the parent call this method with no arguments.
The parent influences the maximum extents to which this Size component can expand,
based on the aspect mode:
NONE - The parent clamps both the width and height.
WIDTH_CONTROLS_HEIGHT - The parent clamps just the width.
HEIGHT_CONTROLS_WIDTH - The parent clamps just the height.
FIT - The parent clamps whichever axis is required to ensure the size fits within it.
ENVELOP - The parent is used to ensure the size fully envelops the parent.
Calling this method automatically calls setSize .
Parameters:
name type optional description
parent any Yes Sets the parent of this Size component. Don't provide a value to clear an existing parent.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L217
Since: 3.16.0
setSize ​
<instance> setSize([width], [height]) ​
Description:
Sets the width and height of this Size component based on the aspect mode.
If the aspect mode is 'none' then calling this method will change the aspect ratio, otherwise the current
aspect ratio is honored across all other modes.
If snapTo values have been set then the given width and height are snapped first, prior to any further
adjustment via min/max values, or a parent.
If minimum and/or maximum dimensions have been specified, the values given to this method will be clamped into
that range prior to adjustment, but may still exceed them depending on the aspect mode.
If this Size component has a parent set, and the aspect mode is fit or envelop , then the given sizes will
be clamped to the range specified by the parent.
Parameters:
name type optional default description
width number Yes 0 The new width of the Size component.
height number Yes "width" The new height of the Size component. If not given, it will use the width .
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L303
Since: 3.16.0
setSnap ​
<instance> setSnap([snapWidth], [snapHeight]) ​
Description:
By setting snap values, when this Size component is modified its dimensions will automatically
be snapped to the nearest grid slice, using floor. For example, if you have snap value of 16,
and the width changes to 68, then it will snap down to 64 (the closest multiple of 16 when floored)
Note that snapping takes place before adjustments by the parent, or the min / max settings. If these
values are not multiples of the given snap values, then this can result in un-snapped dimensions.
Call this method with no arguments to reset the snap values.
Calling this method automatically recalculates the width and the height , if required.
Parameters:
name type optional default description
snapWidth number Yes 0 The amount to snap the width to. If you don't want to snap the width, pass a value of zero.
snapHeight number Yes "snapWidth" The amount to snap the height to. If not provided it will use the snapWidth value. If you don't want to snap the height, pass a value of zero.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L187
Since: 3.16.0
setWidth ​
<instance> setWidth(width) ​
Description:
Sets the width of this Size component.
Depending on the aspect mode, changing the width may also update the height and aspect ratio.
Parameters:
name type optional description
width number No The new width of the Size component.
Returns: Phaser.Structs.Size - This Size component instance.
Source: src/structs/Size.js#L563
Since: 3.16.0
toString ​
<instance> toString() ​
Description:
Returns a string representation of this Size component.
Returns: string - A string representation of this Size component.
Source: src/structs/Size.js#L597
Since: 3.16.0
Constants: ​
Public Members ​
ENVELOP ​
ENVELOP: number ​
Description:
The width and height are automatically adjusted to make the size cover the entire target area while keeping the aspect ratio. This may extend further out than the target size.
Source: src/structs/Size.js#L762
Since: 3.16.0
FIT ​
FIT: number ​
Description:
The width and height are automatically adjusted to fit inside the given target area, while keeping the aspect ratio. Depending on the aspect ratio there may be some space inside the area which is not covered.
Source: src/structs/Size.js#L752
Since: 3.16.0
HEIGHT_CONTROLS_WIDTH ​
HEIGHT_CONTROLS_WIDTH: number ​
Description:
The width is automatically adjusted based on the height.
Source: src/structs/Size.js#L742
Since: 3.16.0
NONE ​
NONE: number ​
Description:
Do not make the size fit the aspect ratio. Change the ratio when the size changes.
Source: src/structs/Size.js#L722
Since: 3.16.0
WIDTH_CONTROLS_HEIGHT ​
WIDTH_CONTROLS_HEIGHT: number ​
Description:
The height is automatically adjusted based on the width.
Source: src/structs/Size.js#L732
Since: 3.16.0
Previous
Set
Next
CanvasTexture
Public Members
aspectMode
aspectRatio
height
maxHeight
maxWidth
minHeight
minWidth
snapTo
width
Public Methods
constrain
copy
destroy
envelop
fitTo
getNewHeight
getNewWidth
resize
setAspectMode
setAspectRatio
setCSS
setHeight
setMax
setMin
setParent
setSize
setSnap
setWidth
toString
Constants:
Public Members
ENVELOP
FIT
HEIGHT_CONTROLS_WIDTH
NONE
WIDTH_CONTROLS_HEIGHT
