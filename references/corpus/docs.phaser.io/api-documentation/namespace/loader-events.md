# Phaser.Loader.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/loader-events

Phaser API Documentation
Namespaces
Phaser.Loader.Events
Version: Phaser v3.90.0
On this page
Phaser.Loader.Events
Scope: static
Source: src/loader/events/index.js#L7
Static functions ​
ADD ​
ADD ​
Description:
The Loader Plugin Add File Event.
This event is dispatched when a new file is successfully added to the Loader and placed into the load queue.
Listen to it from a Scene using: this.load.on('addfile', listener) .
If you add lots of files to a Loader from a preload method, it will dispatch this event for each one of them.
Parameters:
name type optional description
key string No The unique key of the file that was added to the Loader.
type string No The [file type]{@link Phaser.Loader.File#type} string of the file that was added to the Loader, i.e. image .
loader Phaser.Loader.LoaderPlugin No A reference to the Loader Plugin that dispatched this event.
file Phaser.Loader.File No A reference to the File which was added to the Loader.
Source: src/loader/events/ADD_EVENT.js#L7
Since: 3.0.0
COMPLETE ​
COMPLETE ​
Description:
The Loader Plugin Complete Event.
This event is dispatched when the Loader has fully processed everything in the load queue.
By this point every loaded file will now be in its associated cache and ready for use.
Listen to it from a Scene using: this.load.on('complete', listener) .
Parameters:
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader Plugin that dispatched this event.
totalComplete number No The total number of files that successfully loaded.
totalFailed number No The total number of files that failed to load.
Source: src/loader/events/COMPLETE_EVENT.js#L7
Since: 3.0.0
FILE_COMPLETE ​
FILE_COMPLETE ​
Description:
The File Load Complete Event.
This event is dispatched by the Loader Plugin when any file in the queue finishes loading.
Listen to it from a Scene using: this.load.on('filecomplete', listener) .
Make sure you remove this listener when you have finished, or it will continue to fire if the Scene reloads.
You can also listen for the completion of a specific file. See the FILE_KEY_COMPLETE event.
Parameters:
name type optional description
key string No The key of the file that just loaded and finished processing.
type string No The [file type]{@link Phaser.Loader.File#type} of the file that just loaded, i.e. image .
data any Yes The raw data the file contained. If the file was a multi-file, like an atlas or bitmap font, this parameter will be undefined.
Source: src/loader/events/FILE_COMPLETE_EVENT.js#L7
Since: 3.0.0
FILE_KEY_COMPLETE ​
FILE_KEY_COMPLETE ​
Description:
The File Load Complete Event.
This event is dispatched by the Loader Plugin when any file in the queue finishes loading.
It uses a special dynamic event name constructed from the key and type of the file.
For example, if you have loaded an image with a key of monster , you can listen for it
using the following:
this . load . on ( 'filecomplete-image-monster' , function ( key , type , data ) {
// Your handler code
} ) ;
Or, if you have loaded a texture atlas with a key of Level1 :
this . load . on ( 'filecomplete-atlasjson-Level1' , function ( key , type , data ) {
// Your handler code
} ) ;
Or, if you have loaded a sprite sheet with a key of Explosion and a prefix of GAMEOVER :
this . load . on ( 'filecomplete-spritesheet-GAMEOVERExplosion' , function ( key , type , data ) {
// Your handler code
} ) ;
Make sure you remove your listeners when you have finished, or they will continue to fire if the Scene reloads.
You can also listen for the generic completion of files. See the FILE_COMPLETE event.
Parameters:
name type optional description
key string No The key of the file that just loaded and finished processing.
type string No The [file type]{@link Phaser.Loader.File#type} of the file that just loaded, i.e. image .
data any Yes The raw data the file contained. If the file was a multi-file, like an atlas or bitmap font, this parameter will be undefined.
Source: src/loader/events/FILE_KEY_COMPLETE_EVENT.js#L7
Since: 3.0.0
FILE_LOAD ​
FILE_LOAD ​
Description:
The File Load Event.
This event is dispatched by the Loader Plugin when a file finishes loading,
but before it is processed and added to the internal Phaser caches.
Listen to it from a Scene using: this.load.on('load', listener) .
Parameters:
name type optional description
file Phaser.Loader.File No A reference to the File which just finished loading.
Source: src/loader/events/FILE_LOAD_EVENT.js#L7
Since: 3.0.0
FILE_LOAD_ERROR ​
FILE_LOAD_ERROR ​
Description:
The File Load Error Event.
This event is dispatched by the Loader Plugin when a file fails to load.
Listen to it from a Scene using: this.load.on('loaderror', listener) .
Parameters:
name type optional description
file Phaser.Loader.File No A reference to the File which errored during load.
Source: src/loader/events/FILE_LOAD_ERROR_EVENT.js#L7
Since: 3.0.0
FILE_PROGRESS ​
FILE_PROGRESS ​
Description:
The File Load Progress Event.
This event is dispatched by the Loader Plugin during the load of a file, if the browser receives a DOM ProgressEvent and
the lengthComputable event property is true. Depending on the size of the file and browser in use, this may, or may not happen.
Listen to it from a Scene using: this.load.on('fileprogress', listener) .
Parameters:
name type optional description
file Phaser.Loader.File No A reference to the File which errored during load.
percentComplete number No A value between 0 and 1 indicating how 'complete' this file is.
Source: src/loader/events/FILE_PROGRESS_EVENT.js#L7
Since: 3.0.0
POST_PROCESS ​
POST_PROCESS ​
Description:
The Loader Plugin Post Process Event.
This event is dispatched by the Loader Plugin when the Loader has finished loading everything in the load queue.
It is dispatched before the internal lists are cleared and each File is destroyed.
Use this hook to perform any last minute processing of files that can only happen once the
Loader has completed, but prior to it emitting the complete event.
Listen to it from a Scene using: this.load.on('postprocess', listener) .
Parameters:
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader Plugin that dispatched this event.
Source: src/loader/events/POST_PROCESS_EVENT.js#L7
Since: 3.0.0
PROGRESS ​
PROGRESS ​
Description:
The Loader Plugin Progress Event.
This event is dispatched when the Loader updates its load progress, typically as a result of a file having completed loading.
Listen to it from a Scene using: this.load.on('progress', listener) .
Parameters:
name type optional description
progress number No The current progress of the load. A value between 0 and 1.
Source: src/loader/events/PROGRESS_EVENT.js#L7
Since: 3.0.0
START ​
START ​
Description:
The Loader Plugin Start Event.
This event is dispatched when the Loader starts running. At this point load progress is zero.
This event is dispatched even if there aren't any files in the load queue.
Listen to it from a Scene using: this.load.on('start', listener) .
Parameters:
name type optional description
loader Phaser.Loader.LoaderPlugin No A reference to the Loader Plugin that dispatched this event.
Source: src/loader/events/START_EVENT.js#L7
Since: 3.0.0
Previous
Phaser.Input
Next
Phaser.Loader.FileTypes
Static functions
ADD
COMPLETE
FILE_COMPLETE
FILE_KEY_COMPLETE
FILE_LOAD
FILE_LOAD_ERROR
FILE_PROGRESS
POST_PROCESS
PROGRESS
START
