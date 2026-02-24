# Phaser.GameObjects.Components.PathFollower | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/gameobjects-components-pathfollower

Phaser API Documentation
Namespaces
Phaser.GameObjects.Components.PathFollower
Version: Phaser v3.90.0
On this page
Phaser.GameObjects.Components.PathFollower
Scope: static
Source: src/gameobjects/components/PathFollower.js#L13
Since: 3.17.0
Static functions ​
path ​
path: Phaser.Curves.Path ​
Description:
The Path this PathFollower is following. It can only follow one Path at a time.
Source: src/gameobjects/components/PathFollower.js#L23
Since: 3.0.0
rotateToPath ​
rotateToPath: boolean ​
Description:
Should the PathFollower automatically rotate to point in the direction of the Path?
Source: src/gameobjects/components/PathFollower.js#L32
Since: 3.0.0
Static functions ​
isFollowing ​
<instance> isFollowing() ​
Description:
Is this PathFollower actively following a Path or not?
To be considered as isFollowing it must be currently moving on a Path, and not paused.
Returns: boolean - true is this PathFollower is actively following a Path, otherwise false .
Source: src/gameobjects/components/PathFollower.js#L167
Since: 3.0.0
pathUpdate ​
<instance> pathUpdate() ​
Description:
Internal update handler that advances this PathFollower along the path.
Called automatically by the Scene step, should not typically be called directly.
Source: src/gameobjects/components/PathFollower.js#L350
Since: 3.17.0
pauseFollow ​
<instance> pauseFollow() ​
Description:
Pauses this PathFollower. It will still continue to render, but it will remain motionless at the
point on the Path at which you paused it.
Returns: Phaser.GameObjects.Components.PathFollower - This Game Object.
Source: src/gameobjects/components/PathFollower.js#L285
Since: 3.3.0
resumeFollow ​
<instance> resumeFollow() ​
Description:
Resumes a previously paused PathFollower.
If the PathFollower was not paused this has no effect.
Returns: Phaser.GameObjects.Components.PathFollower - This Game Object.
Source: src/gameobjects/components/PathFollower.js#L306
Since: 3.3.0
setPath ​
<instance> setPath(path, [config]) ​
Description:
Set the Path that this PathFollower should follow.
Optionally accepts Phaser.Types.GameObjects.PathFollower.PathConfig settings.
Parameters:
name type optional description
path Phaser.Curves.Path No The Path this PathFollower is following. It can only follow one Path at a time.
config number | Phaser.Types.GameObjects.PathFollower.PathConfig Phaser.Types.Tweens.NumberTweenBuilderConfig Yes
Returns: Phaser.GameObjects.Components.PathFollower - This Game Object.
Source: src/gameobjects/components/PathFollower.js#L111
Since: 3.0.0
setRotateToPath ​
<instance> setRotateToPath(value, [offset]) ​
Description:
Set whether the PathFollower should automatically rotate to point in the direction of the Path.
Parameters:
name type optional default description
value boolean No Whether the PathFollower should automatically rotate to point in the direction of the Path.
offset number Yes 0 Rotation offset in degrees.
Returns: Phaser.GameObjects.Components.PathFollower - This Game Object.
Source: src/gameobjects/components/PathFollower.js#L145
Since: 3.0.0
startFollow ​
<instance> startFollow([config], [startAt]) ​
Description:
Starts this PathFollower following its given Path.
Parameters:
name type optional default description
config number | Phaser.Types.GameObjects.PathFollower.PathConfig Phaser.Types.Tweens.NumberTweenBuilderConfig Yes "{}"
startAt number Yes 0 Optional start position of the follow, between 0 and 1.
Returns: Phaser.GameObjects.Components.PathFollower - This Game Object.
Source: src/gameobjects/components/PathFollower.js#L184
Since: 3.3.0
stopFollow ​
<instance> stopFollow() ​
Description:
Stops this PathFollower from following the path any longer.
This will invoke any 'stop' conditions that may exist on the Path, or for the follower.
Returns: Phaser.GameObjects.Components.PathFollower - This Game Object.
Source: src/gameobjects/components/PathFollower.js#L328
Since: 3.3.0
Previous
Phaser.GameObjects.Components.Origin
Next
Phaser.GameObjects.Components.Pipeline
Static functions
path
rotateToPath
Static functions
isFollowing
pathUpdate
pauseFollow
resumeFollow
setPath
setRotateToPath
startFollow
stopFollow
