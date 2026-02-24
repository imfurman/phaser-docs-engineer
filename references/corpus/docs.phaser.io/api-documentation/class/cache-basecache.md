# BaseCache | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/cache-basecache

Phaser API Documentation
Class
BaseCache
Version: Phaser v3.90.0
On this page
BaseCache
The BaseCache is a base Cache class that can be used for storing references to any kind of data.
Data can be added, retrieved and removed based on the given keys.
Keys are string-based.
Scope : static
Source: src/cache/BaseCache.js#L12
Since: 3.0.0
Public Members ​
entries ​
entries: Phaser.Structs.Map.<String, *> ​
Description:
The Map in which the cache objects are stored.
You can query the Map directly or use the BaseCache methods.
Source: src/cache/BaseCache.js#L31
Since: 3.0.0
events ​
events: Phaser.Events.EventEmitter ​
Description:
An instance of EventEmitter used by the cache to emit related events.
Source: src/cache/BaseCache.js#L42
Since: 3.0.0
Public Methods ​
add ​
<instance> add(key, data) ​
Description:
Adds an item to this cache. The item is referenced by a unique string, which you are responsible
for setting and keeping track of. The item can only be retrieved by using this string.
Parameters:
name type optional description
key string No The unique key by which the data added to the cache will be referenced.
data * No The data to be stored in the cache.
Returns: Phaser.Cache.BaseCache - This BaseCache object.
Fires: Phaser.Cache.Events#event:ADD
Source: src/cache/BaseCache.js#L52
Since: 3.0.0
destroy ​
<instance> destroy() ​
Description:
Destroys this cache and all items within it.
Source: src/cache/BaseCache.js#L163
Since: 3.0.0
exists ​
<instance> exists(key) ​
Description:
Checks if this cache contains an item matching the given key.
This performs the same action as BaseCache.has and is called directly by the Loader.
Parameters:
name type optional description
key string No The unique key of the item to be checked in this cache.
Returns: boolean - Returns true if the cache contains an item matching the given key, otherwise false .
Source: src/cache/BaseCache.js#L90
Since: 3.7.0
get ​
<instance> get(key) ​
Description:
Gets an item from this cache based on the given key.
Parameters:
name type optional description
key string No The unique key of the item to be retrieved from this cache.
Returns: * - The item in the cache, or null if no item matching the given key was found.
Source: src/cache/BaseCache.js#L106
Since: 3.0.0
getKeys ​
<instance> getKeys() ​
Description:
Returns all keys in use in this cache.
Returns: Array.<string> - Array containing all the keys.
Source: src/cache/BaseCache.js#L150
Since: 3.17.0
has ​
<instance> has(key) ​
Description:
Checks if this cache contains an item matching the given key.
This performs the same action as BaseCache.exists .
Parameters:
name type optional description
key string No The unique key of the item to be checked in this cache.
Returns: boolean - Returns true if the cache contains an item matching the given key, otherwise false .
Source: src/cache/BaseCache.js#L74
Since: 3.0.0
remove ​
<instance> remove(key) ​
Description:
Removes and item from this cache based on the given key.
If an entry matching the key is found it is removed from the cache and a remove event emitted.
No additional checks are done on the item removed. If other systems or parts of your game code
are relying on this item, it is up to you to sever those relationships prior to removing the item.
Parameters:
name type optional description
key string No The unique key of the item to remove from the cache.
Returns: Phaser.Cache.BaseCache - This BaseCache object.
Fires: Phaser.Cache.Events#event:REMOVE
Source: src/cache/BaseCache.js#L121
Since: 3.0.0
Previous
AnimationState
Next
CacheManager
Public Members
entries
events
Public Methods
add
destroy
exists
get
getKeys
has
remove
