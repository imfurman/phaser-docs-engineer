# Phaser.Cache.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/cache-events

Phaser API Documentation
Namespaces
Phaser.Cache.Events
Version: Phaser v3.90.0
On this page
Phaser.Cache.Events
Scope: static
Source: src/cache/events/index.js#L7
Static functions ​
ADD ​
ADD ​
Description:
The Cache Add Event.
This event is dispatched by any Cache that extends the BaseCache each time a new object is added to it.
Parameters:
name type optional description
cache Phaser.Cache.BaseCache No The cache to which the object was added.
key string No The key of the object added to the cache.
object * No A reference to the object that was added to the cache.
Source: src/cache/events/ADD_EVENT.js#L7
Since: 3.0.0
REMOVE ​
REMOVE ​
Description:
The Cache Remove Event.
This event is dispatched by any Cache that extends the BaseCache each time an object is removed from it.
Parameters:
name type optional description
cache Phaser.Cache.BaseCache No The cache from which the object was removed.
key string No The key of the object removed from the cache.
object * No A reference to the object that was removed from the cache.
Source: src/cache/events/REMOVE_EVENT.js#L7
Since: 3.0.0
Previous
Phaser.BlendModes
Next
Phaser.Cache
Static functions
ADD
REMOVE
