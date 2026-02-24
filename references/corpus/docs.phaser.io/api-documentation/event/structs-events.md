# Structs.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/event/structs-events

Phaser API Documentation
Events
Structs.Events
Version: Phaser v3.90.0
On this page
Structs.Events
PROCESS_QUEUE_ADD ​
Description: The Process Queue Add Event.
This event is dispatched by a Process Queue when a new item is successfully moved to its active list.
You will most commonly see this used by a Scene's Update List when a new Game Object has been added.
In that instance, listen to this event from within a Scene using: this.sys.updateList.on('add', listener) .
name type optional description
item * No The item that was added to the Process Queue.
Member of: Phaser.Structs.Events
Source: src/structs/events/PROCESS_QUEUE_ADD_EVENT.js#L7
Since: 3.20.0
PROCESS_QUEUE_REMOVE ​
Description: The Process Queue Remove Event.
This event is dispatched by a Process Queue when a new item is successfully removed from its active list.
You will most commonly see this used by a Scene's Update List when a Game Object has been removed.
In that instance, listen to this event from within a Scene using: this.sys.updateList.on('remove', listener) .
name type optional description
item * No The item that was removed from the Process Queue.
Member of: Phaser.Structs.Events
Source: src/structs/events/PROCESS_QUEUE_REMOVE_EVENT.js#L7
Since: 3.20.0
Previous
Sound.Events
Next
Textures.Events
PROCESS_QUEUE_ADD
PROCESS_QUEUE_REMOVE
