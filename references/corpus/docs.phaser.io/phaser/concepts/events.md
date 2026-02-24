# Events | Phaser Help

Source: https://docs.phaser.io/phaser/concepts/events

Concepts
Events
On this page
Events
Events are a way for one system to send a signal, that other systems may listen for and then act upon. For example, if the player clicks their mouse on your game, that will internally emit a sequence of events within Phaser. Or if the Loader finishes downloading a file, that will emit a related event.
Events are a core part of Phaser and you'll find them used throughout the framework. They are used both internally, for one system to talk to another, and externally, for your game code to listen for and respond to. There are hundreds of such events that Phaser will emit during the course of a game.
Events are always emitted by what is known as an Event Emitter. Most systems and Game Objects within Phaser are Event Emitters, meaning they can emit events directly and you can hook event handlers to them.
We adopted this practise because events are extremely common in the web browser. Most browser APIs are event-driven, so it made sense to follow this pattern. It also means that you can easily extend Phaser by adding your own events, or listening for existing ones and responding to them.
The Event Emitter ​
Phaser 3 uses a slightly modified eventemitter3 , as Phaser.Events.EventEmitter .
Event names are strings
The emitter chooses a default context ( this value), but listeners can override this
The emitter chooses the callback arguments
on() is the same as addListener()
off() is the same as removeListener()
off() with no arguments is the same as removeAllListeners()
off() can match event name; event name and listener; or event name, listener, and context; but no other combination
A listener added with once() is removed after its first call
All of Phaser's events (names, default context, arguments) are defined in the API.
Some Phaser classes (e.g., GameObject) extend Phaser.Events.EventEmitter directly, and some (e.g., Game, Scene) hold an emitter on their events property.
You can emit and listen to your own events on these objects, but don't use any of Phaser's event names (e.g., "update"), and never remove listeners that aren't yours. Be careful of removing more than you meant to with off() .
// NO (removes all listeners on all events)
this . game . events . off ( ) ;
// NO (removes all listeners to `step`)
this . game . events . off ( 'step' ) ;
// YES (same arguments used on `on()`)
this . game . events . off ( 'step' , this . onStep , this ) ;
Remember that event emitters just hook up functions to other functions. The emitter doesn't know or care about any state associated with the listener. It's up to you to remove listeners when appropriate.
Get event emitter ​
Scene:
var ee = scene . events ;
Game object:
var ee = gameObject ;
Attach listener ​
ee . on ( eventName , callback , scope ) ;
ee . once ( eventName , callback , scope ) ; // only fire listeners one time
Alias
ee . addListener ( eventName , callback , scope ) ;
ee . addListener ( eventName , callback , scope , true ) ; // only fire listeners one time
Fire event ​
ee . emit ( eventName , parameter0 , ... ) ;
Remove listeners ​
Remove a listener
ee . off ( eventName , callback , scope ) ;
ee . off ( eventName , callback , scope , true ) ; // only remove one-time listeners
or
ee . removeListener ( eventName , callback , scope ) ;
ee . removeListener ( eventName , callback , scope , true ) ; // only remove one-time listeners
Remove listeners of an event
ee . off ( eventName ) ;
or
ee . removeListener ( eventName ) ;
Remove listeners of all events
ee . removeAllListeners ( ) ;
Get listeners count ​
var count = ee . listenerCount ( eventName ) ;
//var noListener = (ee.listenerCount(eventName) === 0);
Get listeners ​
var listeners = ee . listeners ( eventName ) ;
Get event names ​
var names = ee . eventNames ( ) ;
Listener ​
{
fn : callback ,
context : scope ,
once : once
}
Custom event emitter class ​
class MyEventEmitter extends Phaser . Events . EventEmitter {
// construct() {
// super();
// }
// destroy() {
// super.destroy();
// }
}
Author Credits ​
Content on this page includes work by:
RexRainbow
samme
Previous
Display
Next
FX
The Event Emitter
Get event emitter
Attach listener
Fire event
Remove listeners
Get listeners count
Get listeners
Get event names
Listener
Custom event emitter class
Author Credits
