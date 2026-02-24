# EventEmitter | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/events-eventemitter

Phaser API Documentation
Class
EventEmitter
Version: Phaser v3.90.0
On this page
EventEmitter
EventEmitter is a Scene Systems plugin compatible version of eventemitter3.
Scope : static
Source: src/events/EventEmitter.js#L11
Since: 3.0.0
Public Methods ​
addListener ​
<instance> addListener(event, fn, [context]) ​
Description:
Add a listener for a given event.
Parameters:
name type optional default description
event string | symbol No The event name.
fn function No The listener function.
context * Yes "this" The context to invoke the listener with.
Returns: Phaser.Events.EventEmitter - this .
Source: src/events/EventEmitter.js#L111
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Removes all listeners.
Source: src/events/EventEmitter.js#L42
Since: 3.0.0
emit ​
<instance> emit(event, [args]) ​
Description:
Calls each of the listeners registered for a given event.
Parameters:
name type optional description
event string | symbol No The event name.
args * Yes Additional arguments that will be passed to the event handler.
Returns: boolean - true if the event had listeners, else false .
Source: src/events/EventEmitter.js#L86
Since: 3.0.0
eventNames ​
<instance> eventNames() ​
Description:
Return an array listing the events for which the emitter has registered listeners.
Returns: Array.<(string | symbol)> - undefined
Source: src/events/EventEmitter.js#L55
Since: 3.0.0
listenerCount ​
<instance> listenerCount(event) ​
Description:
Return the number of listeners listening to a given event.
Parameters:
name type optional description
event string | symbol No The event name.
Returns: number - The number of listeners.
Source: src/events/EventEmitter.js#L75
Since: 3.0.0
listeners ​
<instance> listeners(event) ​
Description:
Return the listeners registered for a given event.
Parameters:
name type optional description
event string | symbol No The event name.
Returns: Array.<function()> - The registered listeners.
Source: src/events/EventEmitter.js#L64
Since: 3.0.0
off ​
<instance> off(event, [fn], [context], [once]) ​
Description:
Remove the listeners of a given event.
Parameters:
name type optional description
event string | symbol No The event name.
fn function Yes Only remove the listeners that match this function.
context * Yes Only remove the listeners that have this context.
once boolean Yes Only remove one-time listeners.
Returns: Phaser.Events.EventEmitter - this .
Source: src/events/EventEmitter.js#L151
Since: 3.0.0
on ​
<instance> on(event, fn, [context]) ​
Description:
Add a listener for a given event.
Parameters:
name type optional default description
event string | symbol No The event name.
fn function No The listener function.
context * Yes "this" The context to invoke the listener with.
Returns: Phaser.Events.EventEmitter - this .
Source: src/events/EventEmitter.js#L98
Since: 3.0.0
once ​
<instance> once(event, fn, [context]) ​
Description:
Add a one-time listener for a given event.
Parameters:
name type optional default description
event string | symbol No The event name.
fn function No The listener function.
context * Yes "this" The context to invoke the listener with.
Returns: Phaser.Events.EventEmitter - this .
Source: src/events/EventEmitter.js#L124
Since: 3.0.0
removeAllListeners ​
<instance> removeAllListeners([event]) ​
Description:
Remove all listeners, or those of the specified event.
Parameters:
name type optional description
event string | symbol Yes The event name.
Returns: Phaser.Events.EventEmitter - this .
Source: src/events/EventEmitter.js#L165
Since: 3.0.0
removeListener ​
<instance> removeListener(event, [fn], [context], [once]) ​
Description:
Remove the listeners of a given event.
Parameters:
name type optional description
event string | symbol No The event name.
fn function Yes Only remove the listeners that match this function.
context * Yes Only remove the listeners that have this context.
once boolean Yes Only remove one-time listeners.
Returns: Phaser.Events.EventEmitter - this .
Source: src/events/EventEmitter.js#L137
Since: 3.0.0
shutdown ​
<instance> shutdown() ​
Description:
Removes all listeners.
Source: src/events/EventEmitter.js#L31
Since: 3.0.0
Previous
RGB
Next
Barrel
Public Methods
addListener
destroy
emit
eventNames
listenerCount
listeners
off
on
once
removeAllListeners
removeListener
shutdown
