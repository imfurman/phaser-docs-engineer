# Phaser.Structs.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/structs-events

Phaser API Documentation
Namespaces
Phaser.Structs.Events
Version: Phaser v3.90.0
On this page
Phaser.Structs.Events
Scope: static
Source: src/structs/events/index.js#L7
Static functions ​
PROCESS_QUEUE_ADD ​
PROCESS_QUEUE_ADD ​
Description:
The Process Queue Add Event.
This event is dispatched by a Process Queue when a new item is successfully moved to its active list.
You will most commonly see this used by a Scene's Update List when a new Game Object has been added.
In that instance, listen to this event from within a Scene using: this.sys.updateList.on('add', listener) .
Parameters:
name type optional description
item * No The item that was added to the Process Queue.
Source: src/structs/events/PROCESS_QUEUE_ADD_EVENT.js#L7
Since: 3.20.0
PROCESS_QUEUE_REMOVE ​
PROCESS_QUEUE_REMOVE ​
Description:
The Process Queue Remove Event.
This event is dispatched by a Process Queue when a new item is successfully removed from its active list.
You will most commonly see this used by a Scene's Update List when a Game Object has been removed.
In that instance, listen to this event from within a Scene using: this.sys.updateList.on('remove', listener) .
Parameters:
name type optional description
item * No The item that was removed from the Process Queue.
Source: src/structs/events/PROCESS_QUEUE_REMOVE_EVENT.js#L7
Since: 3.20.0
Previous
Phaser.Sound
Next
Phaser.Structs
Static functions
PROCESS_QUEUE_ADD
PROCESS_QUEUE_REMOVE
