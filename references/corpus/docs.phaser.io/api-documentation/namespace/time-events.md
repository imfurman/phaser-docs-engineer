# Phaser.Time.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/time-events

Phaser API Documentation
Namespaces
Phaser.Time.Events
Version: Phaser v3.90.0
On this page
Phaser.Time.Events
Scope: static
Source: src/time/events/index.js#L7
Static functions ​
COMPLETE ​
COMPLETE ​
Description:
The Timeline Complete Event.
This event is dispatched by timeline when all timeline events complete.
Listen to it from a Timeline instance using Timeline.on('complete', listener) , i.e.:
const timeline = this . add . timeline ( ) ;
timeline . on ( 'complete' , listener ) ;
timeline . play ( ) ;
Parameters:
name type optional description
timeline Phaser.Time.Timeline No A reference to the Timeline that emitted the event.
Source: src/time/events/COMPLETE_EVENT.js#L7
Since: 3.70.0
Previous
Phaser.Tilemaps
Next
Phaser.Time
Static functions
COMPLETE
