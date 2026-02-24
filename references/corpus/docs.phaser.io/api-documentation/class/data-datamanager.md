# DataManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/data-datamanager

Phaser API Documentation
Class
DataManager
Version: Phaser v3.90.0
On this page
DataManager
The Data Manager Component features a means to store pieces of data specific to a Game Object, System or Plugin.
You can then search, query it, and retrieve the data. The parent must either extend EventEmitter,
or have a property called events that is an instance of it.
Constructor
new DataManager(parent, [eventEmitter])
Parameters
name type optional description
parent object No The object that this DataManager belongs to.
eventEmitter Phaser.Events.EventEmitter Yes The DataManager's event emitter.
Scope : static
Source: src/data/DataManager.js#L19
Since: 3.0.0
Public Members ​
count ​
count: number ​
Description:
Return the total number of entries in this Data Manager.
Source: src/data/DataManager.js#L677
Since: 3.0.0
events ​
events: Phaser.Events.EventEmitter ​
Description:
The DataManager's event emitter.
Source: src/data/DataManager.js#L48
Since: 3.0.0
freeze ​
freeze: boolean ​
Description:
Gets or sets the frozen state of this Data Manager.
A frozen Data Manager will block all attempts to create new values or update existing ones.
Source: src/data/DataManager.js#L655
Since: 3.0.0
list ​
list: Object.<string, *> ​
Description:
The data list.
Source: src/data/DataManager.js#L62
Since: 3.0.0
parent ​
parent: * ​
Description:
The object that this DataManager belongs to.
Source: src/data/DataManager.js#L39
Since: 3.0.0
values ​
values: Object.<string, *> ​
Description:
The public values list. You can use this to access anything you have stored
in this Data Manager. For example, if you set a value called gold you can
access it via:
this . data . values . gold ;
You can also modify it directly:
this . data . values . gold += 1000 ;
Doing so will emit a setdata event from the parent of this Data Manager.
Do not modify this object directly. Adding properties directly to this object will not
emit any events. Always use DataManager.set to create new items the first time around.
Source: src/data/DataManager.js#L72
Since: 3.10.0
Public Methods ​
destroy ​
<instance> destroy() ​
Description:
Destroy this data manager.
Source: src/data/DataManager.js#L638
Since: 3.0.0
each ​
<instance> each(callback, [context], [args]) ​
Description:
Passes all data entries to the given callback.
Parameters:
name type optional description
callback DataEachCallback No The function to call.
context * Yes Value to use as this when executing callback.
args * Yes Additional arguments that will be passed to the callback, after the game object, key, and data.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Source: src/data/DataManager.js#L419
Since: 3.0.0
get ​
<instance> get(key) ​
Description:
Retrieves the value for the given key, or undefined if it doesn't exist.
You can also access values via the values object. For example, if you had a key called gold you can do either:
this . data . get ( 'gold' ) ;
Or access the value directly:
this . data . values . gold ;
You can also pass in an array of keys, in which case an array of values will be returned:
this . data . get ( [ 'gold' , 'armor' , 'health' ] ) ;
This approach is useful for destructuring arrays in ES6.
Parameters:
name type optional description
key string | Array.<string> No The key of the value to retrieve, or an array of keys.
Returns: * - The value belonging to the given key, or an array of values, the order of which will match the input array.
Source: src/data/DataManager.js#L116
Since: 3.0.0
getAll ​
<instance> getAll() ​
Description:
Retrieves all data values in a new object.
Returns: Object.<string, *> - All data values.
Source: src/data/DataManager.js#L167
Since: 3.0.0
has ​
<instance> has(key) ​
Description:
Determines whether the given key is set in this Data Manager.
Please note that the keys are case-sensitive and must be valid JavaScript Object property strings.
This means the keys gold and Gold are treated as two unique values within the Data Manager.
Parameters:
name type optional description
key string No The key to check.
Returns: boolean - Returns true if the key exists, otherwise false .
Source: src/data/DataManager.js#L581
Since: 3.0.0
inc ​
<instance> inc(key, [amount]) ​
Description:
Increase a value for the given key. If the key doesn't already exist in the Data Manager then it is increased from 0.
When the value is first set, a setdata event is emitted.
Parameters:
name type optional default description
key string No The key to change the value for.
amount number Yes 1 The amount to increase the given key by. Pass a negative value to decrease the key.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Fires: Phaser.Data.Events#event:SET_DATA , Phaser.Data.Events#event:CHANGE_DATA , Phaser.Data.Events#event:CHANGE_DATA_KEY
Source: src/data/DataManager.js#L285
Since: 3.23.0
merge ​
<instance> merge(data, [overwrite]) ​
Description:
Merge the given object of key value pairs into this DataManager.
Any newly created values will emit a setdata event. Any updated values (see the overwrite argument)
will emit a changedata event.
Parameters:
name type optional default description
data Object.<string, *> No The data to merge.
overwrite boolean Yes true Whether to overwrite existing data. Defaults to true.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Fires: Phaser.Data.Events#event:SET_DATA , Phaser.Data.Events#event:CHANGE_DATA , Phaser.Data.Events#event:CHANGE_DATA_KEY
Source: src/data/DataManager.js#L451
Since: 3.0.0
pop ​
<instance> pop(key) ​
Description:
Retrieves the data associated with the given 'key', deletes it from this Data Manager, then returns it.
Parameters:
name type optional description
key string No The key of the value to retrieve and delete.
Returns: * - The value of the given key.
Fires: Phaser.Data.Events#event:REMOVE_DATA
Source: src/data/DataManager.js#L553
Since: 3.0.0
query ​
<instance> query(search) ​
Description:
Queries the DataManager for the values of keys matching the given regular expression.
Parameters:
name type optional description
search RegExp No A regular expression object. If a non-RegExp object obj is passed, it is implicitly converted to a RegExp by using new RegExp(obj).
Returns: Object.<string, *> - The values of the keys matching the search string.
Source: src/data/DataManager.js#L190
Since: 3.0.0
remove ​
<instance> remove(key) ​
Description:
Remove the value for the given key.
If the key is found in this Data Manager it is removed from the internal lists and a
removedata event is emitted.
You can also pass in an array of keys, in which case all keys in the array will be removed:
this . data . remove ( [ 'gold' , 'armor' , 'health' ] ) ;
Parameters:
name type optional description
key string | Array.<string> No The key to remove, or an array of keys to remove.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Fires: Phaser.Data.Events#event:REMOVE_DATA
Source: src/data/DataManager.js#L484
Since: 3.0.0
reset ​
<instance> reset() ​
Description:
Delete all data in this Data Manager and unfreeze it.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Source: src/data/DataManager.js#L617
Since: 3.0.0
set ​
<instance> set(key, [data]) ​
Description:
Sets a value for the given key. If the key doesn't already exist in the Data Manager then it is created.
data . set ( 'name' , 'Red Gem Stone' ) ;
You can also pass in an object of key value pairs as the first argument:
data . set ( { name : 'Red Gem Stone' , level : 2 , owner : 'Link' , gold : 50 } ) ;
To get a value back again you can call get :
data . get ( 'gold' ) ;
Or you can access the value directly via the values property, where it works like any other variable:
data . values . gold += 50 ;
When the value is first set, a setdata event is emitted.
If the key already exists, a changedata event is emitted instead, along an event named after the key.
For example, if you updated an existing key called PlayerLives then it would emit the event changedata-PlayerLives .
These events will be emitted regardless if you use this method to set the value, or the direct values setter.
Please note that the data keys are case-sensitive and must be valid JavaScript Object property strings.
This means the keys gold and Gold are treated as two unique values within the Data Manager.
Tags:
generic
genericUse
Parameters:
name type optional description
key string | object No The key to set the value for. Or an object of key value pairs. If an object the data argument is ignored.
data * Yes The value to set for the given key. If an object is provided as the key this argument is ignored.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Fires: Phaser.Data.Events#event:SET_DATA , Phaser.Data.Events#event:CHANGE_DATA , Phaser.Data.Events#event:CHANGE_DATA_KEY
Source: src/data/DataManager.js#L215
Since: 3.0.0
setFreeze ​
<instance> setFreeze(value) ​
Description:
Freeze or unfreeze this Data Manager. A frozen Data Manager will block all attempts
to create new values or update existing ones.
Parameters:
name type optional description
value boolean No Whether to freeze or unfreeze the Data Manager.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Source: src/data/DataManager.js#L599
Since: 3.0.0
toggle ​
<instance> toggle(key) ​
Description:
Toggle a boolean value for the given key. If the key doesn't already exist in the Data Manager then it is toggled from false.
When the value is first set, a setdata event is emitted.
Parameters:
name type optional description
key string No The key to toggle the value for.
Returns: Phaser.Data.DataManager - This Data Manager instance.
Fires: Phaser.Data.Events#event:SET_DATA , Phaser.Data.Events#event:CHANGE_DATA , Phaser.Data.Events#event:CHANGE_DATA_KEY
Source: src/data/DataManager.js#L325
Since: 3.23.0
Previous
RequestAnimationFrame
Next
DataManagerPlugin
Public Members
count
events
freeze
list
parent
values
Public Methods
destroy
each
get
getAll
has
inc
merge
pop
query
remove
reset
set
setFreeze
toggle
