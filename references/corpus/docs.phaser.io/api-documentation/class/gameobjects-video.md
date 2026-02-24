# Video | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/gameobjects-video

Phaser API Documentation
Class
Video
Version: Phaser v3.90.0
On this page
Video
A Video Game Object.
This Game Object is capable of handling playback of a video file, video stream or media stream.
You can optionally 'preload' the video into the Phaser Video Cache:
preload ( ) {
this . load . video ( 'ripley' , 'assets/aliens.mp4' ) ;
}
create ( ) {
this . add . video ( 400 , 300 , 'ripley' ) ;
}
You don't have to 'preload' the video. You can also play it directly from a URL:
create ( ) {
this . add . video ( 400 , 300 ) . loadURL ( 'assets/aliens.mp4' ) ;
}
To all intents and purposes, a video is a standard Game Object, just like a Sprite. And as such, you can do
all the usual things to it, such as scaling, rotating, cropping, tinting, making interactive, giving a
physics body, etc.
Transparent videos are also possible via the WebM file format. Providing the video file has was encoded with
an alpha channel, and providing the browser supports WebM playback (not all of them do), then it will render
in-game with full transparency.
Playback is handled entirely via the Request Video Frame API, which is supported by most modern browsers.
A polyfill is provided for older browsers.
Autoplaying Videos ​
Videos can only autoplay if the browser has been unlocked with an interaction, or satisfies the MEI settings.
The policies that control autoplaying are vast and vary between browser. You can, and should, read more about
it here: https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide
If your video doesn't contain any audio, then set the noAudio parameter to true when the video is loaded ,
and it will often allow the video to play immediately:
preload ( ) {
this . load . video ( 'pixar' , 'nemo.mp4' , true ) ;
}
The 3rd parameter in the load call tells Phaser that the video doesn't contain any audio tracks. Video without
audio can autoplay without requiring a user interaction. Video with audio cannot do this unless it satisfies
the browsers MEI settings. See the MDN Autoplay Guide for further details.
Or:
create ( ) {
this . add . video ( 400 , 300 ) . loadURL ( 'assets/aliens.mp4' , true ) ;
}
You can set the noAudio parameter to true even if the video does contain audio. It will still allow the video
to play immediately, but the audio will not start.
Note that due to a bug in IE11 you cannot play a video texture to a Sprite in WebGL. For IE11 force Canvas mode.
More details about video playback and the supported media formats can be found on MDN:
https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement
https://developer.mozilla.org/en-US/docs/Web/Media/Formats
Constructor
new Video(scene, x, y, [key])
Parameters
name type optional description
scene Phaser.Scene No The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time.
x number No The horizontal position of this Game Object in the world.
y number No The vertical position of this Game Object in the world.
key string Yes Optional key of the Video this Game Object will play, as stored in the Video Cache.
Scope : static
Extends
Phaser.GameObjects.GameObject
Phaser.GameObjects.Components.Alpha
Phaser.GameObjects.Components.BlendMode
Phaser.GameObjects.Components.ComputedSize
Phaser.GameObjects.Components.Depth
Phaser.GameObjects.Components.Flip
Phaser.GameObjects.Components.GetBounds
Phaser.GameObjects.Components.Mask
Phaser.GameObjects.Components.Origin
Phaser.GameObjects.Components.Pipeline
Phaser.GameObjects.Components.PostPipeline
Phaser.GameObjects.Components.ScrollFactor
Phaser.GameObjects.Components.TextureCrop
Phaser.GameObjects.Components.Tint
Phaser.GameObjects.Components.Transform
Phaser.GameObjects.Components.Visible
Source: src/gameobjects/video/Video.js#L18
Since: 3.20.0
Inherited Members ​
From Phaser.GameObjects.Components.Alpha :
alpha
alphaBottomLeft
alphaBottomRight
alphaTopLeft
alphaTopRight
From Phaser.GameObjects.Components.BlendMode :
blendMode
From Phaser.GameObjects.Components.ComputedSize :
displayHeight
displayWidth
height
width
From Phaser.GameObjects.Components.Depth :
depth
From Phaser.GameObjects.Components.Flip :
flipX
From Phaser.GameObjects.Components.Mask :
mask
From Phaser.GameObjects.Components.Origin :
displayOriginX
displayOriginY
originX
originY
From Phaser.GameObjects.Components.Pipeline :
defaultPipeline
pipeline
pipelineData
From Phaser.GameObjects.Components.PostPipeline :
hasPostPipeline
postFX
postPipelineData
postPipelines
preFX
From Phaser.GameObjects.Components.ScrollFactor :
scrollFactorX
scrollFactorY
From Phaser.GameObjects.Components.TextureCrop :
frame
isCropped
texture
From Phaser.GameObjects.Components.Tint :
isTinted
tint
tintBottomLeft
tintBottomRight
tintFill
tintTopLeft
tintTopRight
From Phaser.GameObjects.Components.Transform :
angle
hasTransformComponent
rotation
scale
scaleX
scaleY
w
x
y
z
From Phaser.GameObjects.Components.Visible :
visible
From Phaser.GameObjects.GameObject :
active
body
cameraFilter
data
displayList
ignoreDestroy
input
name
parentContainer
renderFlags
scene
state
tabIndex
type
Public Members ​
cacheKey ​
cacheKey: string ​
Description:
The key of the current video as stored in the Video cache.
If the video did not come from the cache this will be an empty string.
Source: src/gameobjects/video/Video.js#L461
Since: 3.60.0
failedPlayAttempts ​
failedPlayAttempts: number ​
Description:
Records the number of times the video has failed to play,
typically because the user hasn't interacted with the page yet.
Source: src/gameobjects/video/Video.js#L272
Since: 3.60.0
flipY ​
flipY: boolean ​
Description:
If you have saved this video to a texture via the saveTexture method, this controls if the video
is rendered with flipY in WebGL or not. You often need to set this if you wish to use the video texture
as the input source for a shader. If you find your video is appearing upside down within a shader or
custom pipeline, flip this property.
Overrides: Phaser.GameObjects.Components.Flip#flipY
Source: src/gameobjects/video/Video.js#L194
Since: 3.20.0
frameReady ​
frameReady: boolean ​
Description:
Has the video created its texture and populated it with the first frame of video?
Source: src/gameobjects/video/Video.js#L236
Since: 3.60.0
isSeeking ​
isSeeking: boolean ​
Description:
Is the video currently seeking?
This is set to true when the seeking event is fired,
and set to false when the seeked event is fired.
Source: src/gameobjects/video/Video.js#L473
Since: 3.60.0
isStalled ​
isStalled: boolean ​
Description:
This read-only property returns true if the video is currently stalled, i.e. it has stopped
playing due to a lack of data, or too much data, but hasn't yet reached the end of the video.
This is set if the Video DOM element emits any of the following events:
stalled
suspend
waiting
And is cleared if the Video DOM element emits the playing event, or handles
a requestVideoFrame call.
Listen for the Phaser Event VIDEO_STALLED to be notified and inspect the event
to see which DOM event caused it.
Note that being stalled isn't always a negative thing. A video can be stalled if it
has downloaded enough data in to its buffer to not need to download any more until
the current batch of frames have rendered.
Source: src/gameobjects/video/Video.js#L245
Since: 3.60.0
markers ​
markers: any ​
Description:
An object containing in and out markers for sequence playback.
Source: src/gameobjects/video/Video.js#L412
Since: 3.20.0
metadata ​
metadata: VideoFrameCallbackMetadata ​
Description:
If the browser supports the Request Video Frame API then this
property will hold the metadata that is returned from
the callback each time it is invoked.
See https://wicg.github.io/video-rvfc/#video-frame-metadata-callback
for a complete list of all properties that will be in this object.
Likely of most interest is the mediaTime property:
The media presentation timestamp (PTS) in seconds of the frame presented
(e.g. its timestamp on the video.currentTime timeline). MAY have a zero
value for live-streams or WebRTC applications.
If the browser doesn't support the API then this property will be undefined.
Source: src/gameobjects/video/Video.js#L282
Since: 3.60.0
playWhenUnlocked ​
playWhenUnlocked: boolean ​
Description:
Should the video auto play when document interaction is required and happens?
Source: src/gameobjects/video/Video.js#L227
Since: 3.20.0
retry ​
retry: number ​
Description:
The current retry elapsed time.
Source: src/gameobjects/video/Video.js#L303
Since: 3.20.0
retryInterval ​
retryInterval: number ​
Description:
If a video fails to play due to a lack of user interaction, this is the
amount of time, in ms, that the video will wait before trying again to
play. The default is 500ms.
Source: src/gameobjects/video/Video.js#L312
Since: 3.20.0
snapshotTexture ​
snapshotTexture: Phaser.Textures.CanvasTexture ​
Description:
A Phaser CanvasTexture instance that holds the most recent snapshot taken from the video.
This will only be set if the snapshot or snapshotArea methods have been called.
Until those methods are called, this property will be undefined .
Source: src/gameobjects/video/Video.js#L181
Since: 3.20.0
touchLocked ​
touchLocked: boolean ​
Description:
An internal flag holding the current state of the video lock, should document interaction be required
before playback can begin.
Source: src/gameobjects/video/Video.js#L216
Since: 3.20.0
video ​
video: HTMLVideoElement ​
Description:
A reference to the HTML Video Element this Video Game Object is playing.
Will be undefined until a video is loaded for playback.
Source: src/gameobjects/video/Video.js#L148
Since: 3.20.0
videoTexture ​
videoTexture: Phaser.Textures.Texture ​
Description:
The Phaser Texture this Game Object is using to render the video to.
Will be undefined until a video is loaded for playback.
Source: src/gameobjects/video/Video.js#L159
Since: 3.20.0
videoTextureSource ​
videoTextureSource: Phaser.Textures.TextureSource ​
Description:
A reference to the TextureSource backing the videoTexture Texture object.
Will be undefined until a video is loaded for playback.
Source: src/gameobjects/video/Video.js#L170
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
From Phaser.GameObjects.Components.Alpha :
clearAlpha
setAlpha
From Phaser.GameObjects.Components.BlendMode :
setBlendMode
From Phaser.GameObjects.Components.ComputedSize :
setDisplaySize
setSize
From Phaser.GameObjects.Components.Depth :
setAbove
setBelow
setDepth
setToBack
setToTop
From Phaser.GameObjects.Components.Flip :
resetFlip
setFlip
setFlipX
setFlipY
toggleFlipX
toggleFlipY
From Phaser.GameObjects.Components.GetBounds :
getBottomCenter
getBottomLeft
getBottomRight
getBounds
getCenter
getLeftCenter
getRightCenter
getTopCenter
getTopLeft
getTopRight
From Phaser.GameObjects.Components.Mask :
clearMask
createBitmapMask
createGeometryMask
setMask
From Phaser.GameObjects.Components.Origin :
setDisplayOrigin
setOrigin
setOriginFromFrame
updateDisplayOrigin
From Phaser.GameObjects.Components.Pipeline :
getPipelineName
initPipeline
resetPipeline
setPipeline
setPipelineData
From Phaser.GameObjects.Components.PostPipeline :
clearFX
getPostPipeline
initPostPipeline
removePostPipeline
resetPostPipeline
setPostPipeline
setPostPipelineData
From Phaser.GameObjects.Components.ScrollFactor :
setScrollFactor
From Phaser.GameObjects.Components.TextureCrop :
setCrop
setFrame
setTexture
From Phaser.GameObjects.Components.Tint :
clearTint
setTint
setTintFill
From Phaser.GameObjects.Components.Transform :
copyPosition
getLocalPoint
getLocalTransformMatrix
getParentRotation
getWorldPoint
getWorldTransformMatrix
setAngle
setPosition
setRandomPosition
setRotation
setScale
setW
setX
setY
setZ
From Phaser.GameObjects.Components.Visible :
setVisible
From Phaser.GameObjects.GameObject :
addedToScene
addToDisplayList
addToUpdateList
destroy
disableInteractive
getData
getDisplayList
getIndexList
incData
removedFromScene
removeFromDisplayList
removeFromUpdateList
removeInteractive
setActive
setData
setDataEnabled
setInteractive
setName
setState
toggleData
toJSON
update
willRender
Public Methods ​
addEventHandlers ​
<instance> addEventHandlers() ​
Description:
Adds the playback specific event handlers to the video element.
Source: src/gameobjects/video/Video.js#L1103
Since: 3.60.0
addLoadEventHandlers ​
<instance> addLoadEventHandlers() ​
Description:
Adds the loading specific event handlers to the video element.
Source: src/gameobjects/video/Video.js#L1068
Since: 3.60.0
addMarker ​
<instance> addMarker(key, markerIn, markerOut) ​
Description:
Adds a sequence marker to this video.
Markers allow you to split a video up into sequences, delineated by a start and end time, given in seconds.
You can then play back specific markers via the playMarker method.
Note that marker timing is not frame-perfect. You should construct your videos in such a way that you allow for
plenty of extra padding before and after each sequence to allow for discrepancies in browser seek and currentTime accuracy.
See https://github.com/w3c/media-and-entertainment/issues/4 for more details about this issue.
Parameters:
name type optional description
key string No A unique name to give this marker.
markerIn number No The time, in seconds, representing the start of this marker.
markerOut number No The time, in seconds, representing the end of this marker.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1198
Since: 3.20.0
changeSource ​
<instance> changeSource(key, [autoplay], [loop], [markerIn], [markerOut]) ​
Description:
This method allows you to change the source of the current video element. It works by first stopping the
current video, if playing. Then deleting the video texture, if one has been created. Finally, it makes a
new video texture and starts playback of the new source through the existing video element.
The reason you may wish to do this is because videos that require interaction to unlock, remain in an unlocked
state, even if you change the source of the video. By changing the source to a new video you avoid having to
go through the unlock process again.
Parameters:
name type optional default description
key string No The key of the Video this Game Object will swap to playing, as stored in the Video Cache.
autoplay boolean Yes true Should the video start playing immediately, once the swap is complete?
loop boolean Yes false Should the video loop automatically when it reaches the end? Please note that not all browsers support seamless video looping for all encoding formats.
markerIn number Yes Optional in marker time, in seconds, for playback of a sequence of the video.
markerOut number Yes Optional out marker time, in seconds, for playback of a sequence of the video.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L596
Since: 3.20.0
completeHandler ​
<instance> completeHandler() ​
Description:
Called when the video completes playback, i.e. reaches an ended state.
This will never happen if the video is coming from a live stream, where the duration is Infinity .
Fires: Phaser.GameObjects.Events#event:VIDEO_COMPLETE
Source: src/gameobjects/video/Video.js#L1609
Since: 3.20.0
createPlayPromise ​
<instance> createPlayPromise([catchError]) ​
Description:
Creates the video.play promise and adds the success and error handlers to it.
Not all browsers support the video.play promise, so this method will fall back to
the old-school way of handling the video.play call.
See https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play#browser_compatibility for details.
Parameters:
name type optional default description
catchError boolean Yes true Should the error be caught and the video marked as failed to play?
Source: src/gameobjects/video/Video.js#L1148
Since: 3.60.0
getCurrentTime ​
<instance> getCurrentTime() ​
Description:
A double-precision floating-point value indicating the current playback time in seconds.
If the media has not started to play and has not been seeked, this value is the media's initial playback time.
For a more accurate value, use the Video.metadata.mediaTime property instead.
Returns: number - A double-precision floating-point value indicating the current playback time in seconds.
Source: src/gameobjects/video/Video.js#L1697
Since: 3.20.0
getDuration ​
<instance> getDuration() ​
Description:
A double-precision floating-point value which indicates the duration (total length) of the media in seconds,
on the media's timeline. If no media is present on the element, or the media is not valid, the returned value is NaN.
If the media has no known end (such as for live streams of unknown duration, web radio, media incoming from WebRTC,
and so forth), this value is +Infinity.
If no video has been loaded, this method will return 0.
Returns: number - A double-precision floating-point value indicating the duration of the media in seconds.
Source: src/gameobjects/video/Video.js#L1822
Since: 3.20.0
getFirstFrame ​
<instance> getFirstFrame() ​
Description:
Attempts to get the first frame of the video by running the requestVideoFrame callback once,
then stopping. This is useful if you need to grab the first frame of the video to display behind
a 'play' button, without actually calling the 'play' method.
If the video is already playing, or has been queued to play with changeSource then this method just returns.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1030
Since: 3.85.0
getLoop ​
<instance> getLoop() ​
Description:
Returns a boolean which indicates whether the media element should start over when it reaches the end.
Returns: boolean - A boolean which indicates whether the media element will start over when it reaches the end.
Source: src/gameobjects/video/Video.js#L2098
Since: 3.20.0
getPlaybackRate ​
<instance> getPlaybackRate() ​
Description:
Returns a double that indicates the rate at which the media is being played back.
Returns: number - A double that indicates the rate at which the media is being played back.
Source: src/gameobjects/video/Video.js#L2063
Since: 3.20.0
getProgress ​
<instance> getProgress() ​
Description:
Returns the current progress of the video as a float.
Progress is defined as a value between 0 (the start) and 1 (the end).
Progress can only be returned if the video has a duration. Some videos,
such as those coming from a live stream, do not have a duration. In this
case the method will return -1.
Returns: number - The current progress of playback. If the video has no duration, will always return -1.
Source: src/gameobjects/video/Video.js#L1791
Since: 3.20.0
getVideoKey ​
<instance> getVideoKey() ​
Description:
Returns the key of the currently played video, as stored in the Video Cache.
If the video did not come from the cache this will return an empty string.
Returns: string - The key of the video being played from the Video Cache, if any.
Source: src/gameobjects/video/Video.js#L632
Since: 3.20.0
getVolume ​
<instance> getVolume() ​
Description:
Returns a double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).
Returns: number - A double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).
Source: src/gameobjects/video/Video.js#L2026
Since: 3.20.0
isMuted ​
<instance> isMuted() ​
Description:
Returns a boolean indicating if this Video is currently muted.
Returns: boolean - A boolean indicating if this Video is currently muted, or not.
Source: src/gameobjects/video/Video.js#L1867
Since: 3.20.0
isPaused ​
<instance> isPaused() ​
Description:
Returns a boolean which indicates whether the video is currently paused.
Returns: boolean - A boolean which indicates whether the video is paused, or not.
Source: src/gameobjects/video/Video.js#L2152
Since: 3.20.0
isPlaying ​
<instance> isPlaying() ​
Description:
Returns a boolean which indicates whether the video is currently playing.
Returns: boolean - A boolean which indicates whether the video is playing, or not.
Source: src/gameobjects/video/Video.js#L2139
Since: 3.20.0
legacyPlayHandler ​
<instance> legacyPlayHandler() ​
Description:
Called when the video emits a playing event.
This is the legacy handler for browsers that don't support Promise based playback.
Source: src/gameobjects/video/Video.js#L1483
Since: 3.60.0
load ​
<instance> load(key) ​
Description:
Loads a Video from the Video Cache, ready for playback with the Video.play method.
If a video is already playing, this method allows you to change the source of the current video element.
It works by first stopping the current video and then starts playback of the new source through the existing video element.
The reason you may wish to do this is because videos that require interaction to unlock, remain in an unlocked
state, even if you change the source of the video. By changing the source to a new video you avoid having to
go through the unlock process again.
Parameters:
name type optional description
key string No The key of the Video this Game Object will play, as stored in the Video Cache.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L561
Since: 3.60.0
loadErrorHandler ​
<instance> loadErrorHandler(event) ​
Description:
This internal method is called automatically if the video fails to load.
Parameters:
name type optional description
event Event No The error Event.
Fires: Phaser.GameObjects.Events#event:VIDEO_ERROR
Source: src/gameobjects/video/Video.js#L1517
Since: 3.20.0
loadHandler ​
<instance> loadHandler([url], [noAudio], [crossOrigin], [stream]) ​
Description:
Internal method that loads a Video from the given URL, ready for playback with the
Video.play method.
Normally you don't call this method directly, but instead use the Video.loadURL method,
or the Video.load method if you have preloaded the video.
Calling this method will skip checking if the browser supports the given format in
the URL, where-as the other two methods enforce these checks.
Parameters:
name type optional description
url string Yes The absolute or relative URL to load the video file from. Set to null if passing in a MediaStream object.
noAudio boolean Yes Does the video have an audio track? If not you can enable auto-playing on it.
crossOrigin string Yes The value to use for the crossOrigin property in the video load request. Either undefined, anonymous or use-credentials . If no value is given, crossorigin will not be set in the request.
stream string Yes A MediaStream object if this is playing a stream instead of a file.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L703
Since: 3.60.0
loadMediaStream ​
<instance> loadMediaStream(stream, [noAudio], [crossOrigin]) ​
Description:
Loads a Video from the given MediaStream object, ready for playback with the Video.play method.
Parameters:
name type optional default description
stream MediaStream No The MediaStream object.
noAudio boolean Yes false Does the video have an audio track? If not you can enable auto-playing on it.
crossOrigin string Yes The value to use for the crossOrigin property in the video load request. Either undefined, anonymous or use-credentials . If no value is given, crossorigin will not be set in the request.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L686
Since: 3.50.0
loadURL ​
<instance> loadURL([urls], [noAudio], [crossOrigin]) ​
Description:
Loads a Video from the given URL, ready for playback with the Video.play method.
If a video is already playing, this method allows you to change the source of the current video element.
It works by first stopping the current video and then starts playback of the new source through the existing video element.
The reason you may wish to do this is because videos that require interaction to unlock, remain in an unlocked
state, even if you change the source of the video. By changing the source to a new video you avoid having to
go through the unlock process again.
Parameters:
name type optional default description
urls string | Array.<string> Phaser.Types.Loader.FileTypes.VideoFileURLConfig Array.< Phaser.Types.Loader.FileTypes.VideoFileURLConfig > Yes
noAudio boolean Yes false Does the video have an audio track? If not you can enable auto-playing on it.
crossOrigin string Yes The value to use for the crossOrigin property in the video load request. Either undefined, anonymous or use-credentials . If no value is given, crossorigin will not be set in the request.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L647
Since: 3.60.0
metadataHandler ​
<instance> metadataHandler(event) ​
Description:
This internal method is called automatically when the video metadata is available.
Parameters:
name type optional description
event Event No The loadedmetadata Event.
Fires: Phaser.GameObjects.Events#event:VIDEO_METADATA
Source: src/gameobjects/video/Video.js#L1533
Since: 3.80.0
pause ​
<instance> pause() ​
Description:
Pauses the current Video, if one is playing.
If no video is loaded, this method does nothing.
Call Video.resume to resume playback.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1992
Since: 3.60.0
play ​
<instance> play([loop], [markerIn], [markerOut]) ​
Description:
Starts this video playing.
If the video is already playing, or has been queued to play with changeSource then this method just returns.
Videos can only autoplay if the browser has been unlocked. This happens if you have interacted with the browser, i.e.
by clicking on it or pressing a key, or due to server settings. The policies that control autoplaying are vast and
vary between browser. You can read more here: https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide
If your video doesn't contain any audio, then set the noAudio parameter to true when the video is loaded,
and it will often allow the video to play immediately:
preload ( ) {
this . load . video ( 'pixar' , 'nemo.mp4' , true ) ;
}
The 3rd parameter in the load call tells Phaser that the video doesn't contain any audio tracks. Video without
audio can autoplay without requiring a user interaction. Video with audio cannot do this unless it satisfies
the browsers MEI settings. See the MDN Autoplay Guide for details.
If you need audio in your videos, then you'll have to consider the fact that the video cannot start playing until the
user has interacted with the browser, into your game flow.
Parameters:
name type optional default description
loop boolean Yes false Should the video loop automatically when it reaches the end? Please note that not all browsers support seamless video looping for all encoding formats.
markerIn number Yes Optional in marker time, in seconds, for playback of a sequence of the video.
markerOut number Yes Optional out marker time, in seconds, for playback of a sequence of the video.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L953
Since: 3.20.0
playError ​
<instance> playError(error) ​
Description:
This internal method is called automatically if the playback Promise fails to resolve.
Parameters:
name type optional description
error DOMException No The Promise DOM Exception error.
Fires: Phaser.GameObjects.Events#event:VIDEO_ERROR , Phaser.GameObjects.Events#event:VIDEO_UNSUPPORTED , Phaser.GameObjects.Events#event:VIDEO_LOCKED
Source: src/gameobjects/video/Video.js#L1446
Since: 3.60.0
playingHandler ​
<instance> playingHandler() ​
Description:
Called when the video emits a playing event.
Fires: Phaser.GameObjects.Events#event:VIDEO_PLAYING
Source: src/gameobjects/video/Video.js#L1503
Since: 3.60.0
playMarker ​
<instance> playMarker(key, [loop]) ​
Description:
Plays a pre-defined sequence in this video.
Markers allow you to split a video up into sequences, delineated by a start and end time, given in seconds and
specified via the addMarker method.
Note that marker timing is not frame-perfect. You should construct your videos in such a way that you allow for
plenty of extra padding before and after each sequence to allow for discrepancies in browser seek and currentTime accuracy.
See https://github.com/w3c/media-and-entertainment/issues/4 for more details about this issue.
Parameters:
name type optional default description
key string No The name of the marker sequence to play.
loop boolean Yes false Should the video loop automatically when it reaches the end? Please note that not all browsers support seamless video looping for all encoding formats.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1229
Since: 3.20.0
playSuccess ​
<instance> playSuccess() ​
Description:
This internal method is called automatically if the playback Promise resolves successfully.
Fires: Phaser.GameObjects.Events#event:VIDEO_UNLOCKED
Source: src/gameobjects/video/Video.js#L1405
Since: 3.60.0
removeEventHandlers ​
<instance> removeEventHandlers() ​
Description:
Removes the playback specific event handlers from the video element.
Source: src/gameobjects/video/Video.js#L1127
Since: 3.60.0
removeLoadEventHandlers ​
<instance> removeLoadEventHandlers() ​
Description:
Removes the loading specific event handlers from the video element.
Source: src/gameobjects/video/Video.js#L1086
Since: 3.60.0
removeMarker ​
<instance> removeMarker(key) ​
Description:
Removes a previously set marker from this video.
If the marker is currently playing it will not stop playback.
Parameters:
name type optional description
key string No The name of the marker to remove.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1260
Since: 3.20.0
removeVideoElement ​
<instance> removeVideoElement() ​
Description:
Removes the Video element from the DOM by calling parentNode.removeChild on itself.
Also removes the autoplay and src attributes and nulls the Video.video reference.
If you loaded an external video via Video.loadURL then you should call this function
to clear up once you are done with the instance, but don't want to destroy this
Video Game Object.
This method is called automatically by Video.destroy .
Source: src/gameobjects/video/Video.js#L2274
Since: 3.20.0
requestVideoFrame ​
<instance> requestVideoFrame(now, metadata) ​
Description:
This method handles the Request Video Frame callback.
It is called by the browser when a new video frame is ready to be displayed.
It's also responsible for the creation of the video texture, if it doesn't
already exist. If it does, it updates the texture as required.
For more details about the Request Video Frame callback, see:
https://web.dev/requestvideoframecallback-rvfc
Parameters:
name type optional description
now DOMHighResTimeStamp No The current time in milliseconds.
metadata VideoFrameCallbackMetadata No Useful metadata about the video frame that was most recently presented for composition. See https://wicg.github.io/video-rvfc/#video-frame-metadata-callback
Fires: Phaser.GameObjects.Events#event:VIDEO_CREATED , Phaser.GameObjects.Events#event:VIDEO_LOOP , Phaser.GameObjects.Events#event:VIDEO_COMPLETE , Phaser.GameObjects.Events#event:VIDEO_PLAY , Phaser.GameObjects.Events#event:VIDEO_TEXTURE
Source: src/gameobjects/video/Video.js#L816
Since: 3.60.0
resume ​
<instance> resume() ​
Description:
Resumes the current Video, if one was previously playing and has been paused.
If no video is loaded, this method does nothing.
Call Video.pause to pause playback.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L2009
Since: 3.60.0
saveSnapshotTexture ​
<instance> saveSnapshotTexture(key) ​
Description:
Stores a copy of this Videos snapshotTexture in the Texture Manager using the given key.
This texture is created when the snapshot or snapshotArea methods are called.
After doing this, any texture based Game Object, such as a Sprite, can use the contents of the
snapshot by using the texture key:
var vid = this . add . video ( 0 , 0 , 'intro' ) ;
vid . snapshot ( ) ;
vid . saveSnapshotTexture ( 'doodle' ) ;
this . add . image ( 400 , 300 , 'doodle' ) ;
Updating the contents of the snapshotTexture , for example by calling snapshot again,
will automatically update any Game Object that is using it as a texture.
Calling saveSnapshotTexture again will not save another copy of the same texture,
it will just rename the existing one.
By default it will create a single base texture. You can add frames to the texture
by using the Texture.add method. After doing this, you can then allow Game Objects
to use a specific frame.
Parameters:
name type optional description
key string No The unique key to store the texture as within the global Texture Manager.
Returns: Phaser.Textures.CanvasTexture - The Texture that was saved.
Source: src/gameobjects/video/Video.js#L1357
Since: 3.20.0
saveTexture ​
<instance> saveTexture(key, [flipY]) ​
Description:
Stores this Video in the Texture Manager using the given key as a dynamic texture,
which any texture-based Game Object, such as a Sprite, can use as its source:
const vid = this . add . video ( 0 , 0 , 'intro' ) ;
vid . play ( ) ;
vid . saveTexture ( 'doodle' ) ;
this . add . image ( 400 , 300 , 'doodle' ) ;
If the video is not yet playing then you need to listen for the TEXTURE_READY event before
you can use this texture on a Game Object:
const vid = this . add . video ( 0 , 0 , 'intro' ) ;
vid . play ( ) ;
vid . once ( 'textureready' , ( video , texture , key ) => {
this . add . image ( 400 , 300 , key ) ;
} ) ;
vid . saveTexture ( 'doodle' ) ;
The saved texture is automatically updated as the video plays. If you pause this video,
or change its source, then the saved texture updates instantly.
Calling saveTexture again will not save another copy of the same texture, it will just rename the existing one.
By default it will create a single base texture. You can add frames to the texture
by using the Texture.add method. After doing this, you can then allow Game Objects
to use a specific frame.
If you intend to save the texture so you can use it as the input for a Shader, you may need to set the
flipY parameter to true if you find the video renders upside down in your shader.
Parameters:
name type optional default description
key string No The unique key to store the texture as within the global Texture Manager.
flipY boolean Yes false Should the WebGL Texture set UNPACK_MULTIPLY_FLIP_Y during upload?
Returns: boolean - Returns true if the texture is available immediately, otherwise returns false and you should listen for the TEXTURE_READY event.
Source: src/gameobjects/video/Video.js#L2165
Since: 3.20.0
seekTo ​
<instance> seekTo(value) ​
Description:
Seeks to a given point in the video. The value is given as a float between 0 and 1,
where 0 represents the start of the video and 1 represents the end.
Seeking only works if the video has a duration, so will not work for live streams.
When seeking begins, this video will emit a seeking event. When the video completes
seeking (i.e. reaches its designated timestamp) it will emit a seeked event.
If you wish to seek based on time instead, use the Video.setCurrentTime method.
Unfortunately, the DOM video element does not guarantee frame-accurate seeking.
This has been an ongoing subject of discussion: https://github.com/w3c/media-and-entertainment/issues/4
Parameters:
name type optional description
value number No The point in the video to seek to. A value between 0 and 1.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1657
Since: 3.20.0
setCurrentTime ​
<instance> setCurrentTime(value) ​
Description:
Seeks to a given playback time in the video. The value is given in seconds or as a string.
Seeking only works if the video has a duration, so will not work for live streams.
When seeking begins, this video will emit a seeking event. When the video completes
seeking (i.e. reaches its designated timestamp) it will emit a seeked event.
You can provide a string prefixed with either a + or a - , such as +2.5 or -2.5 .
In this case it will seek to +/- the value given, relative to the current time .
If you wish to seek based on a duration percentage instead, use the Video.seekTo method.
Parameters:
name type optional description
value string | number No The playback time to seek to in seconds. Can be expressed as a string, such as +2 to seek 2 seconds ahead from the current time.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1714
Since: 3.20.0
setLoop ​
<instance> setLoop([value]) ​
Description:
Sets the loop state of the current video.
The value given is a boolean which indicates whether the media element will start over when it reaches the end.
Not all videos can loop, for example live streams.
Please note that not all browsers support seamless video looping for all encoding formats.
Parameters:
name type optional default description
value boolean Yes true A boolean which indicates whether the media element will start over when it reaches the end.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L2111
Since: 3.20.0
setMute ​
<instance> setMute([value]) ​
Description:
Sets the muted state of the currently playing video, if one is loaded.
Parameters:
name type optional default description
value boolean Yes true The mute value. true if the video should be muted, otherwise false .
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1841
Since: 3.20.0
setPaused ​
<instance> setPaused([value]) ​
Description:
Sets the paused state of the currently loaded video.
If the video is playing, calling this method with true will pause playback.
If the video is paused, calling this method with false will resume playback.
If no video is loaded, this method does nothing.
If the video has not yet been played, Video.play will be called with no parameters.
If the video has ended, this method will do nothing.
Parameters:
name type optional default description
value boolean Yes true The paused value. true if the video should be paused, false to resume it.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L1938
Since: 3.20.0
setPlaybackRate ​
<instance> setPlaybackRate([rate]) ​
Description:
Sets the playback rate of the current video.
The value given is a double that indicates the rate at which the media is being played back.
Parameters:
name type optional description
rate number Yes A double that indicates the rate at which the media is being played back.
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L2076
Since: 3.20.0
setSizeToFrame ​
<instance> setSizeToFrame([frame]) ​
Description:
Sets the size of this Game Object to be that of the given Frame.
This will not change the size that the Game Object is rendered in-game.
For that you need to either set the scale of the Game Object ( setScale ) or call the
setDisplaySize method, which is the same thing as changing the scale but allows you
to do so by giving pixel values.
If you have enabled this Game Object for input, changing the size will not change the
size of the hit area. To do this you should adjust the input.hitArea object directly.
Parameters:
name type optional description
frame Phaser.Textures.Frame | boolean Yes The frame to base the size of this Game Object on.
Returns: Phaser.GameObjects.Video - This Game Object instance.
Source: src/gameobjects/video/Video.js#L1547
Since: 3.0.0
setVolume ​
<instance> setVolume([value]) ​
Description:
Sets the volume of the currently playing video.
The value given is a double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).
Parameters:
name type optional default description
value number Yes 1 A double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Source: src/gameobjects/video/Video.js#L2039
Since: 3.20.0
snapshot ​
<instance> snapshot([width], [height]) ​
Description:
Takes a snapshot of the current frame of the video and renders it to a CanvasTexture object,
which is then returned. You can optionally resize the grab by passing a width and height.
This method returns a reference to the Video.snapshotTexture object. Calling this method
multiple times will overwrite the previous snapshot with the most recent one.
Parameters:
name type optional description
width number Yes The width of the resulting CanvasTexture.
height number Yes The height of the resulting CanvasTexture.
Returns: Phaser.Textures.CanvasTexture - undefined
Source: src/gameobjects/video/Video.js#L1279
Since: 3.20.0
snapshotArea ​
<instance> snapshotArea([x], [y], [srcWidth], [srcHeight], [destWidth], [destHeight]) ​
Description:
Takes a snapshot of the specified area of the current frame of the video and renders it to a CanvasTexture object,
which is then returned. You can optionally resize the grab by passing a different destWidth and destHeight .
This method returns a reference to the Video.snapshotTexture object. Calling this method
multiple times will overwrite the previous snapshot with the most recent one.
Parameters:
name type optional default description
x number Yes 0 The horizontal location of the top-left of the area to grab from.
y number Yes 0 The vertical location of the top-left of the area to grab from.
srcWidth number Yes The width of area to grab from the video. If not given it will grab the full video dimensions.
srcHeight number Yes The height of area to grab from the video. If not given it will grab the full video dimensions.
destWidth number Yes The destination width of the grab, allowing you to resize it.
destHeight number Yes The destination height of the grab, allowing you to resize it.
Returns: Phaser.Textures.CanvasTexture - undefined
Source: src/gameobjects/video/Video.js#L1302
Since: 3.20.0
stalledHandler ​
<instance> stalledHandler(event) ​
Description:
This internal method is called automatically if the video stalls, for whatever reason.
Parameters:
name type optional description
event Event No The error Event.
Fires: Phaser.GameObjects.Events#event:VIDEO_STALLED
Source: src/gameobjects/video/Video.js#L1593
Since: 3.60.0
stop ​
<instance> stop([emitStopEvent]) ​
Description:
Stops the video playing and clears all internal event listeners.
If you only wish to pause playback of the video, and resume it a later time, use the Video.pause method instead.
If the video hasn't finished downloading, calling this method will not abort the download. To do that you need to
call destroy instead.
Parameters:
name type optional default description
emitStopEvent boolean Yes true Should the VIDEO_STOP event be emitted?
Returns: Phaser.GameObjects.Video - This Video Game Object for method chaining.
Fires: Phaser.GameObjects.Events#event:VIDEO_STOP
Source: src/gameobjects/video/Video.js#L2232
Since: 3.20.0
Previous
UpdateList
Next
Zone
Autoplaying Videos
Inherited Members
Public Members
cacheKey
failedPlayAttempts
flipY
frameReady
isSeeking
isStalled
markers
metadata
playWhenUnlocked
retry
retryInterval
snapshotTexture
touchLocked
video
videoTexture
videoTextureSource
Inherited Methods
Public Methods
addEventHandlers
addLoadEventHandlers
addMarker
changeSource
completeHandler
createPlayPromise
getCurrentTime
getDuration
getFirstFrame
getLoop
getPlaybackRate
getProgress
getVideoKey
getVolume
isMuted
isPaused
isPlaying
legacyPlayHandler
load
loadErrorHandler
loadHandler
loadMediaStream
loadURL
metadataHandler
pause
play
playError
playingHandler
playMarker
playSuccess
removeEventHandlers
removeLoadEventHandlers
removeMarker
removeVideoElement
requestVideoFrame
resume
saveSnapshotTexture
saveTexture
seekTo
setCurrentTime
setLoop
setMute
setPaused
setPlaybackRate
setSizeToFrame
setVolume
snapshot
snapshotArea
stalledHandler
stop
