# Phaser.Loader | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/loader

Phaser API Documentation
Namespaces
Phaser.Loader
Version: Phaser v3.90.0
On this page
Phaser.Loader
Scope: static
Source: src/loader/index.js#L10
Static functions ​
File
LoaderPlugin
MultiFile
Static functions ​
Events
FileTypes
FileTypesManager
Static functions ​
GetURL ​
<static> GetURL(file, baseURL) ​
Description:
Given a File and a baseURL value this returns the URL the File will use to download from.
Parameters:
name type optional description
file Phaser.Loader.File No The File object.
baseURL string No A default base URL.
Returns: string - The URL the File will use.
Source: src/loader/GetURL.js#L7
Since: 3.0.0
MergeXHRSettings ​
<static> MergeXHRSettings(global, local) ​
Description:
Takes two XHRSettings Objects and creates a new XHRSettings object from them.
The new object is seeded by the values given in the global settings, but any setting in
the local object overrides the global ones.
Parameters:
name type optional description
global Phaser.Types.Loader.XHRSettingsObject No The global XHRSettings object.
local Phaser.Types.Loader.XHRSettingsObject No The local XHRSettings object.
Returns: Phaser.Types.Loader.XHRSettingsObject - A newly formed XHRSettings object.
Source: src/loader/MergeXHRSettings.js#L10
Since: 3.0.0
XHRLoader ​
<static> XHRLoader(file, globalXHRSettings) ​
Description:
Creates a new XMLHttpRequest (xhr) object based on the given File and XHRSettings
and starts the download of it. It uses the Files own XHRSettings and merges them
with the global XHRSettings object to set the xhr values before download.
Parameters:
name type optional description
file Phaser.Loader.File No The File to download.
globalXHRSettings Phaser.Types.Loader.XHRSettingsObject No The global XHRSettings object.
Returns: XMLHttpRequest - The XHR object, or a FakeXHR Object in the base of base64 data.
Source: src/loader/XHRLoader.js#L9
Since: 3.0.0
XHRSettings ​
<static> XHRSettings([responseType], [async], [user], [password], [timeout], [withCredentials]) ​
Description:
Creates an XHRSettings Object with default values.
Parameters:
name type optional default description
responseType XMLHttpRequestResponseType Yes "''" The responseType, such as 'text'.
async boolean Yes true Should the XHR request use async or not?
user string Yes "''" Optional username for the XHR request.
password string Yes "''" Optional password for the XHR request.
timeout number Yes 0 Optional XHR timeout value.
withCredentials boolean Yes false Optional XHR withCredentials value.
Returns: Phaser.Types.Loader.XHRSettingsObject - The XHRSettings object as used by the Loader.
Source: src/loader/XHRSettings.js#L7
Since: 3.0.0
Static functions ​
FILE_COMPLETE ​
FILE_COMPLETE: number ​
Description:
File has finished processing.
Source: src/loader/const.js#L117
Since: 3.0.0
FILE_DESTROYED ​
FILE_DESTROYED: number ​
Description:
File has been destroyed.
Source: src/loader/const.js#L126
Since: 3.0.0
FILE_ERRORED ​
FILE_ERRORED: number ​
Description:
The File has errored somehow during processing.
Source: src/loader/const.js#L108
Since: 3.0.0
FILE_FAILED ​
FILE_FAILED: number ​
Description:
File failed to load.
Source: src/loader/const.js#L90
Since: 3.0.0
FILE_LOADED ​
FILE_LOADED: number ​
Description:
File has loaded successfully, awaiting processing.
Source: src/loader/const.js#L81
Since: 3.0.0
FILE_LOADING ​
FILE_LOADING: number ​
Description:
File has been started to load by the loader (onLoad called)
Source: src/loader/const.js#L72
Since: 3.0.0
FILE_PENDING ​
FILE_PENDING: number ​
Description:
File is in the load queue but not yet started.
Source: src/loader/const.js#L63
Since: 3.0.0
FILE_PENDING_DESTROY ​
FILE_PENDING_DESTROY: number ​
Description:
File is pending being destroyed.
Source: src/loader/const.js#L144
Since: 3.60.0
FILE_POPULATED ​
FILE_POPULATED: number ​
Description:
File was populated from local data and doesn't need an HTTP request.
Source: src/loader/const.js#L135
Since: 3.0.0
FILE_PROCESSING ​
FILE_PROCESSING: number ​
Description:
File is being processed (onProcess callback)
Source: src/loader/const.js#L99
Since: 3.0.0
LOADER_COMPLETE ​
LOADER_COMPLETE: number ​
Description:
The Loader has completed loading and processing.
Source: src/loader/const.js#L36
Since: 3.0.0
LOADER_DESTROYED ​
LOADER_DESTROYED: number ​
Description:
The Loader has been destroyed.
Source: src/loader/const.js#L54
Since: 3.0.0
LOADER_IDLE ​
LOADER_IDLE: number ​
Description:
The Loader is idle.
Source: src/loader/const.js#L9
Since: 3.0.0
LOADER_LOADING ​
LOADER_LOADING: number ​
Description:
The Loader is actively loading.
Source: src/loader/const.js#L18
Since: 3.0.0
LOADER_PROCESSING ​
LOADER_PROCESSING: number ​
Description:
The Loader is processing files is has loaded.
Source: src/loader/const.js#L27
Since: 3.0.0
LOADER_SHUTDOWN ​
LOADER_SHUTDOWN: number ​
Description:
The Loader is shutting down.
Source: src/loader/const.js#L45
Since: 3.0.0
Previous
Phaser.Loader.FileTypesManager
Next
Phaser.Math.Angle
Static functions
Static functions
Static functions
GetURL
MergeXHRSettings
XHRLoader
XHRSettings
Static functions
FILE_COMPLETE
FILE_DESTROYED
FILE_ERRORED
FILE_FAILED
FILE_LOADED
FILE_LOADING
FILE_PENDING
FILE_PENDING_DESTROY
FILE_POPULATED
FILE_PROCESSING
LOADER_COMPLETE
LOADER_DESTROYED
LOADER_IDLE
LOADER_LOADING
LOADER_PROCESSING
LOADER_SHUTDOWN
