# DOMElement | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-domelement

Phaser API Documentation
Class
DOMElement
Version: Phaser v3.90.0
On this page
DOMElement
DOM Element Game Objects are a way to control and manipulate HTML Elements over the top of your game.
In order for DOM Elements to display you have to enable them by adding the following to your game
configuration object:
dom {
createContainer : true
}
You must also have a parent container for Phaser. This is specified by the parent property in the
game config.
When these two things are added, Phaser will automatically create a DOM Container div that is positioned
over the top of the game canvas. This div is sized to match the canvas, and if the canvas size changes,
as a result of settings within the Scale Manager, the dom container is resized accordingly.
If you have not already done so, you have to provide a parent in the Game Configuration, or the DOM
Container will fail to be created.
You can create a DOM Element by either passing in DOMStrings, or by passing in a reference to an existing
Element that you wish to be placed under the control of Phaser. For example:
this . add . dom ( x , y , 'div' , 'background-color: lime; width: 220px; height: 100px; font: 48px Arial' , 'Phaser' ) ;
The above code will insert a div element into the DOM Container at the given x/y coordinate. The DOMString in
the 4th argument sets the initial CSS style of the div and the final argument is the inner text. In this case,
it will create a lime colored div that is 220px by 100px in size with the text Phaser in it, in an Arial font.
You should nearly always, without exception, use explicitly sized HTML Elements, in order to fully control
alignment and positioning of the elements next to regular game content.
Rather than specify the CSS and HTML directly you can use the load.html File Loader to load it into the
cache and then use the createFromCache method instead. You can also use createFromHTML and various other
methods available in this class to help construct your elements.
Once the element has been created you can then control it like you would any other Game Object. You can set its
position, scale, rotation, alpha and other properties. It will move as the main Scene Camera moves and be clipped
at the edge of the canvas. It's important to remember some limitations of DOM Elements: The obvious one is that
they appear above or below your game canvas. You cannot blend them into the display list, meaning you cannot have
a DOM Element, then a Sprite, then another DOM Element behind it.
They also cannot be enabled for input. To do that, you have to use the addListener method to add native event
listeners directly. The final limitation is to do with cameras. The DOM Container is sized to match the game canvas
entirely and clipped accordingly. DOM Elements respect camera scrolling and scrollFactor settings, but if you
change the size of the camera so it no longer matches the size of the canvas, they won't be clipped accordingly.
DOM Game Objects can be added to a Phaser Container, however you should only nest them one level deep .
Any further down the chain and they will ignore all root container properties.
Also, all DOM Elements are inserted into the same DOM Container, regardless of which Scene they are created in.
Note that you should only have DOM Elements in a Scene with a single Camera. If you require multiple cameras,
use parallel scenes to achieve this.
DOM Elements are a powerful way to align native HTML with your Phaser Game Objects. For example, you can insert
a login form for a multiplayer game directly into your title screen. Or a text input box for a highscore table.
Or a banner ad from a 3rd party service. Or perhaps you'd like to use them for high resolution text display and
UI. The choice is up to you, just remember that you're dealing with standard HTML and CSS floating over the top
of your game, and should treat it accordingly.
Constructor
new DOMElement(scene, [x], [y], [element], [style], [innerText])
Parameters
name type optional default description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number Yes 0 The horizontal position of this DOM Element in the world.
y number Yes 0 The vertical position of this DOM Element in the world.
element Element | string Yes An existing DOM element, or a string. If a string starting with a # it will do a getElementById look-up on the string (minus the hash). Without a hash, it represents the type of element to create, i.e. 'div'.
style string | any Yes If a string, will be set directly as the elements style property value. If a plain object, will be iterated and the values transferred. In both cases the values replacing whatever CSS styles may have been previously set.
innerText string Yes If given, will be set directly as the elements innerText property value, replacing whatever was there before.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.AlphaSingle
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/domelement/DOMElement.js#L16
Since: 3.17.0
Inherited Members ​
From Phaser.GameObjects.Components.AlphaSingle :
alpha
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
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
cache ​
cache: Phaser.Cache.BaseCache ​
Description:
A reference to the HTML Cache.
Source: src/gameobjects/domelement/DOMElement.js#L138
Since: 3.17.0
displayHeight ​
displayHeight: number ​
Description:
The computed display height of this Game Object, based on the getBoundingClientRect DOM call.
The property height holds the un-scaled height of this DOM Element.
Source: src/gameobjects/domelement/DOMElement.js#L274
Since: 3.17.0
displayWidth ​
displayWidth: number ​
Description:
The computed display width of this Game Object, based on the getBoundingClientRect DOM call.
The property width holds the un-scaled width of this DOM Element.
Source: src/gameobjects/domelement/DOMElement.js#L262
Since: 3.17.0
height ​
height: number ​
Description:
The native (un-scaled) height of this Game Object.
For a DOM Element this property is read-only.
The property displayHeight holds the computed bounds of this DOM Element, factoring in scaling.
Source: src/gameobjects/domelement/DOMElement.js#L248
Since: 3.17.0
node ​
node: Element ​
Description:
The actual DOM Element that this Game Object is bound to. For example, if you've created a <div>
then this property is a direct reference to that element within the dom.
Source: src/gameobjects/domelement/DOMElement.js#L147
Since: 3.17.0
parent ​
parent: Element ​
Description:
A reference to the parent DOM Container that the Game instance created when it started.
Source: src/gameobjects/domelement/DOMElement.js#L124
Since: 3.17.0
perspective ​
perspective: number ​
Description:
The perspective CSS property value of the parent DOM Container . This determines the distance between the z=0
plane and the user in order to give a 3D-positioned element some perspective. Each 3D element with
z > 0 becomes larger; each 3D-element with z < 0 becomes smaller. The strength of the effect is determined
by the value of this property.
For more information see: https://developer.mozilla.org/en-US/docs/Web/CSS/perspective
Changing this value changes it globally for all DOM Elements, as they all share the same parent container.
Source: src/gameobjects/domelement/DOMElement.js#L388
Since: 3.17.0
pointerEvents ​
pointerEvents: string ​
Description:
Sets the CSS pointerEvents attribute on the DOM Element during rendering.
This is 'auto' by default. Changing it may have unintended side-effects with
internal Phaser input handling, such as dragging, so only change this if you
understand the implications.
Source: src/gameobjects/domelement/DOMElement.js#L221
Since: 3.55.0
rotate3d ​
rotate3d: Phaser.Math.Vector4 ​
Description:
A Vector4 that contains the 3D rotation of this DOM Element around a fixed axis in 3D space.
All values in the Vector4 are treated as degrees, unless the rotate3dAngle property is changed.
For more details see the following MDN page:
https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d
Source: src/gameobjects/domelement/DOMElement.js#L194
Since: 3.17.0
rotate3dAngle ​
rotate3dAngle: string ​
Description:
The unit that represents the 3D rotation values. By default this is deg for degrees, but can
be changed to any supported unit. See this page for further details:
https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d
Source: src/gameobjects/domelement/DOMElement.js#L209
Since: 3.17.0
skewX ​
skewX: number ​
Description:
The angle, in radians, by which to skew the DOM Element on the horizontal axis.
https://developer.mozilla.org/en-US/docs/Web/CSS/transform
Source: src/gameobjects/domelement/DOMElement.js#L172
Since: 3.17.0
skewY ​
skewY: number ​
Description:
The angle, in radians, by which to skew the DOM Element on the vertical axis.
https://developer.mozilla.org/en-US/docs/Web/CSS/transform
Source: src/gameobjects/domelement/DOMElement.js#L183
Since: 3.17.0
transformOnly ​
transformOnly: boolean ​
Description:
By default a DOM Element will have its transform, display, opacity, zIndex and blend mode properties
updated when its rendered. If, for some reason, you don't want any of these changed other than the
CSS transform, then set this flag to true . When true only the CSS Transform is applied and it's
up to you to keep track of and set the other properties as required.
This can be handy if, for example, you've a nested DOM Element and you don't want the opacity to be
picked-up by any of its children.
Source: src/gameobjects/domelement/DOMElement.js#L157
Since: 3.17.0
width ​
width: number ​
Description:
The native (un-scaled) width of this Game Object.
For a DOM Element this property is read-only.
The property displayWidth holds the computed bounds of this DOM Element, factoring in scaling.
Source: src/gameobjects/domelement/DOMElement.js#L234
Since: 3.17.0
Inherited Methods ​
From Phaser.Events.EventEmitter :
emit
eventNames
listenerCount
listeners
off
on
once
removeAllListeners
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
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
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
Public Methods ​
addListener ​
<instance> addListener(events) ​
Description:
Adds one or more native DOM event listeners onto the underlying Element of this Game Object.
The event is then dispatched via this Game Objects standard event emitter.
For example:
var div = this . add . dom ( x , y , element ) ;
div . addListener ( 'click' ) ;
div . on ( 'click' , handler ) ;
Parameters:
name type optional description
events string No The DOM event/s to listen for. You can specify multiple events by separating them with spaces.
Overrides: Phaser.GameObjects.GameObject#addListener
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L416
Since: 3.17.0
createElement ​
<instance> createElement(tagName, [style], [innerText]) ​
Description:
Creates a native DOM Element, adds it to the parent DOM Container and then binds it to this Game Object,
so you can control it. The tagName should be a string and is passed to document.createElement :
this . add . dom ( ) . createElement ( 'div' ) ;
For more details on acceptable tag names see: https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement
You can also pass in a DOMString or style object to set the CSS on the created element, and an optional innerText
value as well. Here is an example of a DOMString:
this . add . dom ( ) . createElement ( 'div' , 'background-color: lime; width: 220px; height: 100px; font: 48px Arial' , 'Phaser' ) ;
And using a style object:
var style = {
'background-color' : 'lime' ;
'width' : '200px' ;
'height' : '100px' ;
'font' : '48px Arial' ;
} ;
this . add . dom ( ) . createElement ( 'div' , style , 'Phaser' ) ;
If this Game Object already has an Element, it is removed from the DOM entirely first.
Any event listeners you may have previously created will need to be re-created after this call.
Parameters:
name type optional description
tagName string No A string that specifies the type of element to be created. The nodeName of the created element is initialized with the value of tagName. Don't use qualified names (like "html:a") with this method.
style string | any Yes Either a DOMString that holds the CSS styles to be applied to the created element, or an object the styles will be ready from.
innerText string Yes A DOMString that holds the text that will be set as the innerText of the created element.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L491
Since: 3.17.0
createFromCache ​
<instance> createFromCache(The, [tagName]) ​
Description:
Takes a block of html from the HTML Cache, that has previously been preloaded into the game, and then
creates a DOM Element from it. The loaded HTML is set as the innerHTML property of the created
element.
Assume the following html is stored in a file called loginform.html :
< input type = " text " name = " nameField " placeholder = " Enter your name " style = " font-size : 32 px " >
< input type = " button " name = " playButton " value = " Let's Play " style = " font-size : 32 px " >
Which is loaded into your game using the cache key 'login':
this . load . html ( 'login' , 'assets/loginform.html' ) ;
You can create a DOM Element from it using the cache key:
this . add . dom ( ) . createFromCache ( 'login' ) ;
The optional elementType argument controls the container that is created, into which the loaded html is inserted.
The default is a plain div object, but any valid tagName can be given.
If this Game Object already has an Element, it is removed from the DOM entirely first.
Any event listeners you may have previously created will need to be re-created after this call.
Parameters:
name type optional default description
The string No key of the html cache entry to use for this DOM Element.
tagName string Yes "'div'" The tag name of the element into which all of the loaded html will be inserted. Defaults to a plain div tag.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L653
Since: 3.17.0
createFromHTML ​
<instance> createFromHTML(html, [tagName]) ​
Description:
Takes a string of html and then creates a DOM Element from it. The HTML is set as the innerHTML
property of the created element.
let form = `
<input type="text" name="nameField" placeholder="Enter your name" style="font-size: 32px">
<input type="button" name="playButton" value="Let's Play" style="font-size: 32px">
` ;
You can create a DOM Element from it using the string:
this . add . dom ( ) . createFromHTML ( form ) ;
The optional elementType argument controls the type of container that is created, into which the html is inserted.
The default is a plain div object, but any valid tagName can be given.
If this Game Object already has an Element, it is removed from the DOM entirely first.
Any event listeners you may have previously created will need to be re-created after this call.
Parameters:
name type optional default description
html string No A string of html to be set as the innerHTML property of the created element.
tagName string Yes "'div'" The tag name of the element into which all of the html will be inserted. Defaults to a plain div tag.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L703
Since: 3.17.0
getChildByID ​
<instance> getChildByID(id) ​
Description:
Gets all children from this DOM Elements node, using querySelectorAll('*') and then iterates through
them, looking for the first one that has a matching id. It then returns this child if found, or null if not.
Be aware that class and id names are case-sensitive.
Parameters:
name type optional description
id string No The id to search the children for.
Returns: Element - The first matching child DOM Element, or null if not found.
Source: src/gameobjects/domelement/DOMElement.js#L836
Since: 3.17.0
getChildByName ​
<instance> getChildByName(name) ​
Description:
Gets all children from this DOM Elements node, using querySelectorAll('*') and then iterates through
them, looking for the first one that has a matching name. It then returns this child if found, or null if not.
Be aware that class and id names are case-sensitive.
Parameters:
name type optional description
name string No The name to search the children for.
Returns: Element - The first matching child DOM Element, or null if not found.
Source: src/gameobjects/domelement/DOMElement.js#L854
Since: 3.17.0
getChildByProperty ​
<instance> getChildByProperty(property, value) ​
Description:
Gets all children from this DOM Elements node, using querySelectorAll('*') and then iterates through
them, looking for the first one that has a property matching the given key and value. It then returns this child
if found, or null if not.
Parameters:
name type optional description
property string No The property to search the children for.
value string No The value the property must strictly equal.
Returns: Element - The first matching child DOM Element, or null if not found.
Source: src/gameobjects/domelement/DOMElement.js#L805
Since: 3.17.0
removeElement ​
<instance> removeElement() ​
Description:
Removes the current DOM Element bound to this Game Object from the DOM entirely and resets the
node property of this Game Object to be null .
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L760
Since: 3.17.0
removeListener ​
<instance> removeListener(events) ​
Description:
Removes one or more native DOM event listeners from the underlying Element of this Game Object.
Parameters:
name type optional description
events string No The DOM event/s to stop listening for. You can specify multiple events by separating them with spaces.
Overrides: Phaser.GameObjects.GameObject#removeListener
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L452
Since: 3.17.0
setClassName ​
<instance> setClassName(className) ​
Description:
Sets the className property of the DOM Element node and updates the internal sizes.
Parameters:
name type optional description
className string No A string representing the class or space-separated classes of the element.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L872
Since: 3.17.0
setElement ​
<instance> setElement(element, [style], [innerText]) ​
Description:
Binds a new DOM Element to this Game Object. If this Game Object already has an Element it is removed from the DOM
entirely first. Any event listeners you may have previously created will need to be re-created on the new element.
The element argument you pass to this method can be either a string tagName:
< h1 id = "heading" > Phaser < / h1 >
this . add . dom ( ) . setElement ( 'heading' ) ;
Or a reference to an Element instance:
< h1 id = "heading" > Phaser < / h1 >
var h1 = document . getElementById ( 'heading' ) ;
this . add . dom ( ) . setElement ( h1 ) ;
You can also pass in a DOMString or style object to set the CSS on the created element, and an optional innerText
value as well. Here is an example of a DOMString:
this . add . dom ( ) . setElement ( h1 , 'background-color: lime; width: 220px; height: 100px; font: 48px Arial' , 'Phaser' ) ;
And using a style object:
var style = {
'background-color' : 'lime' ;
'width' : '200px' ;
'height' : '100px' ;
'font' : '48px Arial' ;
} ;
this . add . dom ( ) . setElement ( h1 , style , 'Phaser' ) ;
Parameters:
name type optional description
element string | Element No If a string it is passed to getElementById() , or it should be a reference to an existing Element.
style string | any Yes Either a DOMString that holds the CSS styles to be applied to the created element, or an object the styles will be ready from.
innerText string Yes A DOMString that holds the text that will be set as the innerText of the created element.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L538
Since: 3.17.0
setHTML ​
<instance> setHTML(html) ​
Description:
Sets the innerHTML property of the DOM Element node and updates the internal sizes.
Parameters:
name type optional description
html string No A DOMString of html to be set as the innerHTML property of the element.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L918
Since: 3.17.0
setPerspective ​
<instance> setPerspective(value) ​
Description:
Sets the perspective CSS property of the parent DOM Container . This determines the distance between the z=0
plane and the user in order to give a 3D-positioned element some perspective. Each 3D element with
z > 0 becomes larger; each 3D-element with z < 0 becomes smaller. The strength of the effect is determined
by the value of this property.
For more information see: https://developer.mozilla.org/en-US/docs/Web/CSS/perspective
Changing this value changes it globally for all DOM Elements, as they all share the same parent container.
Parameters:
name type optional description
value number No The perspective value, in pixels, that determines the distance between the z plane and the user.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L364
Since: 3.17.0
setSkew ​
<instance> setSkew([x], [y]) ​
Description:
Sets the horizontal and vertical skew values of this DOM Element.
For more information see: https://developer.mozilla.org/en-US/docs/Web/CSS/transform
Parameters:
name type optional default description
x number Yes 0 The angle, in radians, by which to skew the DOM Element on the horizontal axis.
y number Yes "x" The angle, in radians, by which to skew the DOM Element on the vertical axis.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L340
Since: 3.17.0
setText ​
<instance> setText(text) ​
Description:
Sets the innerText property of the DOM Element node and updates the internal sizes.
Note that only certain types of Elements can have innerText set on them.
Parameters:
name type optional description
text string No A DOMString representing the rendered text content of the element.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L894
Since: 3.17.0
updateSize ​
<instance> updateSize() ​
Description:
Internal method that sets the displayWidth and displayHeight properties, and the clientWidth
and clientHeight values into the width and height properties respectively.
This is called automatically whenever a new element is created or set.
Returns: Phaser.GameObjects.DOMElement - This DOM Element instance.
Source: src/gameobjects/domelement/DOMElement.js#L781
Since: 3.17.0
willRender ​
<instance> willRender() ​
Description:
Compares the renderMask with the renderFlags to see if this Game Object will render or not.
DOMElements always return true as they need to still set values during the render pass, even if not visible.
Overrides: Phaser.GameObjects.GameObject#willRender
Returns: boolean - true if the Game Object should be rendered, otherwise false .
Source: src/gameobjects/domelement/DOMElement.js#L958
Since: 3.17.0
Previous
Curve
Next
DisplayList
Inherited Members
Public Members
cache
displayHeight
displayWidth
height
node
parent
perspective
pointerEvents
rotate3d
rotate3dAngle
skewX
skewY
transformOnly
width
Inherited Methods
Public Methods
addListener
createElement
createFromCache
createFromHTML
getChildByID
getChildByName
getChildByProperty
removeElement
removeListener
setClassName
setElement
setHTML
setPerspective
setSkew
setText
updateSize
willRender
