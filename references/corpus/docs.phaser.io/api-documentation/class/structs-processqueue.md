# ProcessQueue | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/structs-processqueue

Phaser API Documentation
Class
ProcessQueue
Version: Phaser v3.90.0
On this page
ProcessQueue
A Process Queue maintains three internal lists.
The pending list is a selection of items which are due to be made 'active' in the next update.
The active list is a selection of items which are considered active and should be updated.
The destroy list is a selection of items that were active and are awaiting being destroyed in the next update.
When new items are added to a Process Queue they are put in the pending list, rather than being added
immediately the active list. Equally, items that are removed are put into the destroy list, rather than
being destroyed immediately. This allows the Process Queue to carefully process each item at a specific, fixed
time, rather than at the time of the request from the API.
Scope : static
Extends
Phaser.Events.EventEmitter
Source: src/structs/ProcessQueue.js#L11
Since: 3.0.0
Public Members ​
checkQueue ​
checkQueue: boolean ​
Description:
If true only unique objects will be allowed in the queue.
Source: src/structs/ProcessQueue.js#L92
Since: 3.50.0
length ​
length: number ​
Description:
The number of entries in the active list.
Source: src/structs/ProcessQueue.js#L343
Since: 3.20.0
Inherited Methods ​
From Phaser.Events.EventEmitter :
addListener
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
Public Methods ​
add ​
<instance> add(item) ​
Description:
Adds a new item to the Process Queue.
The item is added to the pending list and made active in the next update.
Tags:
genericUse
genericUse
Parameters:
name type optional description
item * No The item to add to the queue.
Returns: * - The item that was added.
Source: src/structs/ProcessQueue.js#L156
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Immediately destroys this process queue, clearing all of its internal arrays and resetting the process totals.
Overrides: Phaser.Events.EventEmitter#destroy
Source: src/structs/ProcessQueue.js#L360
Since: 3.0.0
getActive ​
<instance> getActive() ​
Description:
Returns the current list of active items.
This method returns a reference to the active list array, not a copy of it.
Therefore, be careful to not modify this array outside of the ProcessQueue.
Tags:
genericUse
Returns: Array.<*> - A list of active items.
Source: src/structs/ProcessQueue.js#L325
Since: 3.0.0
isActive ​
<instance> isActive(item) ​
Description:
Checks the given item to see if it is already active within this Process Queue.
Tags:
genericUse
genericUse
Parameters:
name type optional description
item * No The item to check.
Returns: boolean - true if the item is active, otherwise false .
Source: src/structs/ProcessQueue.js#L102
Since: 3.60.0
isDestroying ​
<instance> isDestroying(item) ​
Description:
Checks the given item to see if it is already pending destruction from this Process Queue.
Tags:
genericUse
genericUse
Parameters:
name type optional description
item * No The item to check.
Returns: boolean - true if the item is pending destruction, otherwise false .
Source: src/structs/ProcessQueue.js#L138
Since: 3.60.0
isPending ​
<instance> isPending(item) ​
Description:
Checks the given item to see if it is already pending addition to this Process Queue.
Tags:
genericUse
genericUse
Parameters:
name type optional description
item * No The item to check.
Returns: boolean - true if the item is pending insertion, otherwise false .
Source: src/structs/ProcessQueue.js#L120
Since: 3.60.0
remove ​
<instance> remove(item) ​
Description:
Removes an item from the Process Queue.
The item is added to the 'destroy' list and is fully removed in the next update.
Tags:
genericUse
genericUse
Parameters:
name type optional description
item * No The item to be removed from the queue.
Returns: * - The item that was removed.
Source: src/structs/ProcessQueue.js#L186
Since: 3.0.0
removeAll ​
<instance> removeAll() ​
Description:
Removes all active items from this Process Queue.
All the items are marked as 'pending destroy' and fully removed in the next update.
Returns: Phaser.Structs.ProcessQueue - This Process Queue object.
Source: src/structs/ProcessQueue.js#L230
Since: 3.20.0
update ​
<instance> update() ​
Description:
Update this queue. First it will process any items awaiting destruction, and remove them.
Then it will check to see if there are any items pending insertion, and move them to an
active state. Finally, it will return a list of active items for further processing.
Tags:
genericUse
Returns: Array.<*> - A list of active items.
Source: src/structs/ProcessQueue.js#L256
Since: 3.0.0
Previous
Map
Next
RTree
Public Members
checkQueue
length
Inherited Methods
Public Methods
add
destroy
getActive
isActive
isDestroying
isPending
remove
removeAll
update
