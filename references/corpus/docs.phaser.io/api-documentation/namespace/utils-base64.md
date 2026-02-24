# Phaser.Utils.Base64 | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/utils-base64

Phaser API Documentation
Namespaces
Phaser.Utils.Base64
Version: Phaser v3.90.0
On this page
Phaser.Utils.Base64
Scope: static
Source: src/utils/base64/index.js#L7
Static functions ​
ArrayBufferToBase64 ​
<static> ArrayBufferToBase64(arrayBuffer, [mediaType]) ​
Description:
Converts an ArrayBuffer into a base64 string.
The resulting string can optionally be a data uri if the mediaType argument is provided.
See https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs for more details.
Parameters:
name type optional description
arrayBuffer ArrayBuffer No The Array Buffer to encode.
mediaType string Yes An optional media type, i.e. audio/ogg or image/jpeg . If included the resulting string will be a data URI.
Returns: string - The base64 encoded Array Buffer.
Source: src/utils/base64/ArrayBufferToBase64.js#L10
Since: 3.18.0
Base64ToArrayBuffer ​
<static> Base64ToArrayBuffer(base64) ​
Description:
Converts a base64 string, either with or without a data uri, into an Array Buffer.
Parameters:
name type optional description
base64 string No The base64 string to be decoded. Can optionally contain a data URI header, which will be stripped out prior to decoding.
Returns: ArrayBuffer - An ArrayBuffer decoded from the base64 data.
Source: src/utils/base64/Base64ToArrayBuffer.js#L18
Since: 3.18.0
Previous
Phaser.Utils.Array
Next
Phaser.Utils.Objects
Static functions
ArrayBufferToBase64
Base64ToArrayBuffer
