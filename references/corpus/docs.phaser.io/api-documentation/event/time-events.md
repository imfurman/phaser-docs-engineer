# Time.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/event/time-events

Phaser API Documentation
Events
Time.Events
Version: Phaser v3.90.0
On this page
Time.Events
COMPLETE ​
Description: The Timeline Complete Event.
This event is dispatched by timeline when all timeline events complete.
Listen to it from a Timeline instance using Timeline.on('complete', listener) , i.e.:
const timeline = this . add . timeline ( ) ;
timeline . on ( 'complete' , listener ) ;
timeline . play ( ) ;
name type optional description
timeline Phaser.Time.Timeline No A reference to the Timeline that emitted the event.
Member of: Phaser.Time.Events
Source: src/time/events/COMPLETE_EVENT.js#L7
Since: 3.70.0
Previous
Textures.Events
Next
Tweens.Events
COMPLETE
