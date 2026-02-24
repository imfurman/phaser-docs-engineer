# Phaser.GameObjects.Events | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-events

Phaser API Documentation
Namespaces
Phaser.GameObjects.Events
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Events
Scope: static
Source: src/gameobjects/events/index.js#L7
Static functions ​
ADDED_TO_SCENE ​
ADDED_TO_SCENE ​
Description:
The Game Object Added to Scene Event.
This event is dispatched when a Game Object is added to a Scene.
Listen for it on a Game Object instance using GameObject.on('addedtoscene', listener) .
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that was added to the Scene.
scene Phaser.Scene No The Scene to which the Game Object was added.
Source: src/gameobjects/events/ADDED_TO_SCENE_EVENT.js#L7
Since: 3.50.0
DESTROY ​
DESTROY ​
Description:
The Game Object Destroy Event.
This event is dispatched when a Game Object instance is being destroyed.
Listen for it on a Game Object instance using GameObject.on('destroy', listener) .
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object which is being destroyed.
fromScene boolean No True if this Game Object is being destroyed by the Scene, false if not.
Source: src/gameobjects/events/DESTROY_EVENT.js#L7
Since: 3.0.0
REMOVED_FROM_SCENE ​
REMOVED_FROM_SCENE ​
Description:
The Game Object Removed from Scene Event.
This event is dispatched when a Game Object is removed from a Scene.
Listen for it on a Game Object instance using GameObject.on('removedfromscene', listener) .
Parameters:
name type optional description
gameObject Phaser.GameObjects.GameObject No The Game Object that was removed from the Scene.
scene Phaser.Scene No The Scene from which the Game Object was removed.
Source: src/gameobjects/events/REMOVED_FROM_SCENE_EVENT.js#L7
Since: 3.50.0
VIDEO_COMPLETE ​
VIDEO_COMPLETE ​
Description:
The Video Game Object Complete Event.
This event is dispatched when a Video finishes playback by reaching the end of its duration. It
is also dispatched if a video marker sequence is being played and reaches the end.
Note that not all videos can fire this event. Live streams, for example, have no fixed duration,
so never technically 'complete'.
If a video is stopped from playback, via the Video.stop method, it will emit the
VIDEO_STOP event instead of this one.
Listen for it from a Video Game Object instance using Video.on('complete', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which completed playback.
Source: src/gameobjects/events/VIDEO_COMPLETE_EVENT.js#L7
Since: 3.20.0
VIDEO_CREATED ​
VIDEO_CREATED ​
Description:
The Video Game Object Created Event.
This event is dispatched when the texture for a Video has been created. This happens
when enough of the video source has been loaded that the browser is able to render a
frame from it.
Listen for it from a Video Game Object instance using Video.on('created', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which raised the event.
width number No The width of the video.
height number No The height of the video.
Source: src/gameobjects/events/VIDEO_CREATED_EVENT.js#L7
Since: 3.20.0
VIDEO_ERROR ​
VIDEO_ERROR ​
Description:
The Video Game Object Error Event.
This event is dispatched when a Video tries to play a source that does not exist, or is the wrong file type.
Listen for it from a Video Game Object instance using Video.on('error', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which threw the error.
event DOMException | string No The native DOM event the browser raised during playback.
Source: src/gameobjects/events/VIDEO_ERROR_EVENT.js#L7
Since: 3.20.0
VIDEO_LOCKED ​
VIDEO_LOCKED ​
Description:
The Video Game Object Locked Event.
This event is dispatched when a Video was attempted to be played, but the browser prevented it
from doing so due to the Media Engagement Interaction policy.
If you get this event you will need to wait for the user to interact with the browser before
the video will play. This is a browser security measure to prevent autoplaying videos with
audio. An interaction includes a mouse click, a touch, or a key press.
Listen for it from a Video Game Object instance using Video.on('locked', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which raised the event.
Source: src/gameobjects/events/VIDEO_LOCKED_EVENT.js#L7
Since: 3.60.0
VIDEO_LOOP ​
VIDEO_LOOP ​
Description:
The Video Game Object Loop Event.
This event is dispatched when a Video that is currently playing has looped. This only
happens if the loop parameter was specified, or the setLoop method was called,
and if the video has a fixed duration. Video streams, for example, cannot loop, as
they have no duration.
Looping is based on the result of the Video timeupdate event. This event is not
frame-accurate, due to the way browsers work, so please do not rely on this loop
event to be time or frame precise.
Listen for it from a Video Game Object instance using Video.on('loop', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which has looped.
Source: src/gameobjects/events/VIDEO_LOOP_EVENT.js#L7
Since: 3.20.0
VIDEO_METADATA ​
VIDEO_METADATA ​
Description:
The Video Game Object Metadata Event.
This event is dispatched when a Video has access to the metadata.
Listen for it from a Video Game Object instance using Video.on('metadata', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which fired the event.
event DOMException | string No The native DOM event the browser raised during playback.
Source: src/gameobjects/events/VIDEO_METADATA_EVENT.js#L7
Since: 3.80.0
VIDEO_PLAY ​
VIDEO_PLAY ​
Description:
The Video Game Object Play Event.
This event is dispatched when a Video begins playback. For videos that do not require
interaction unlocking, this is usually as soon as the Video.play method is called.
However, for videos that require unlocking, it is fired once playback begins after
they've been unlocked.
Listen for it from a Video Game Object instance using Video.on('play', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which started playback.
Source: src/gameobjects/events/VIDEO_PLAY_EVENT.js#L7
Since: 3.20.0
VIDEO_PLAYING ​
VIDEO_PLAYING ​
Description:
The Video Game Object Playing Event.
The playing event is fired after playback is first started,
and whenever it is restarted. For example it is fired when playback
resumes after having been paused or delayed due to lack of data.
Listen for it from a Video Game Object instance using Video.on('playing', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which started playback.
Source: src/gameobjects/events/VIDEO_PLAYING_EVENT.js#L7
Since: 3.60.0
VIDEO_SEEKED ​
VIDEO_SEEKED ​
Description:
The Video Game Object Seeked Event.
This event is dispatched when a Video completes seeking to a new point in its timeline.
Listen for it from a Video Game Object instance using Video.on('seeked', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which completed seeking.
Source: src/gameobjects/events/VIDEO_SEEKED_EVENT.js#L7
Since: 3.20.0
VIDEO_SEEKING ​
VIDEO_SEEKING ​
Description:
The Video Game Object Seeking Event.
This event is dispatched when a Video begins seeking to a new point in its timeline.
When the seek is complete, it will dispatch the VIDEO_SEEKED event to conclude.
Listen for it from a Video Game Object instance using Video.on('seeking', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which started seeking.
Source: src/gameobjects/events/VIDEO_SEEKING_EVENT.js#L7
Since: 3.20.0
VIDEO_STALLED ​
VIDEO_STALLED ​
Description:
The Video Game Object Stalled Event.
This event is dispatched by a Video Game Object when the video playback stalls.
This can happen if the video is buffering.
If will fire for any of the following native DOM events:
stalled
suspend
waiting
Listen for it from a Video Game Object instance using Video.on('stalled', listener) .
Note that being stalled isn't always a negative thing. A video can be stalled if it
has downloaded enough data in to its buffer to not need to download any more until
the current batch of frames have rendered.
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which threw the error.
event Event No The native DOM event the browser raised during playback.
Source: src/gameobjects/events/VIDEO_STALLED_EVENT.js#L7
Since: 3.60.0
VIDEO_STOP ​
VIDEO_STOP ​
Description:
The Video Game Object Stopped Event.
This event is dispatched when a Video is stopped from playback via a call to the Video.stop method,
either directly via game code, or indirectly as the result of changing a video source or destroying it.
Listen for it from a Video Game Object instance using Video.on('stop', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which stopped playback.
Source: src/gameobjects/events/VIDEO_STOP_EVENT.js#L7
Since: 3.20.0
VIDEO_TEXTURE ​
VIDEO_TEXTURE ​
Description:
The Video Game Object Texture Ready Event.
This event is dispatched by a Video Game Object when it has finished creating its texture.
This happens when the video has finished loading enough data for its first frame.
If you wish to use the Video texture elsewhere in your game, such as as a Sprite texture,
then you should listen for this event first, before creating the Sprites that use it.
Listen for it from a Video Game Object instance using Video.on('textureready', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object that emitted the event.
texture Phaser.Textures.Texture No The Texture that was created.
Source: src/gameobjects/events/VIDEO_TEXTURE_EVENT.js#L7
Since: 3.60.0
VIDEO_UNLOCKED ​
VIDEO_UNLOCKED ​
Description:
The Video Game Object Unlocked Event.
This event is dispatched when a Video that was prevented from playback due to the browsers
Media Engagement Interaction policy, is unlocked by a user gesture.
Listen for it from a Video Game Object instance using Video.on('unlocked', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which raised the event.
Source: src/gameobjects/events/VIDEO_UNLOCKED_EVENT.js#L7
Since: 3.20.0
VIDEO_UNSUPPORTED ​
VIDEO_UNSUPPORTED ​
Description:
The Video Game Object Unsupported Event.
This event is dispatched by a Video Game Object if the media source
(which may be specified as a MediaStream, MediaSource, Blob, or File,
for example) doesn't represent a supported media format.
Listen for it from a Video Game Object instance using Video.on('unsupported', listener) .
Parameters:
name type optional description
video Phaser.GameObjects.Video No The Video Game Object which started playback.
event DOMException | string No The native DOM event the browser raised during playback.
Source: src/gameobjects/events/VIDEO_UNSUPPORTED_EVENT.js#L7
Since: 3.60.0
Previous
Phaser.GameObjects.Components
Next
Phaser.GameObjects.Particles.Events
Static functions
ADDED_TO_SCENE
DESTROY
REMOVED_FROM_SCENE
VIDEO_COMPLETE
VIDEO_CREATED
VIDEO_ERROR
VIDEO_LOCKED
VIDEO_LOOP
VIDEO_METADATA
VIDEO_PLAY
VIDEO_PLAYING
VIDEO_SEEKED
VIDEO_SEEKING
VIDEO_STALLED
VIDEO_STOP
VIDEO_TEXTURE
VIDEO_UNLOCKED
VIDEO_UNSUPPORTED
