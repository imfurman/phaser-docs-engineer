# Phaser.Textures.Parsers | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/textures-parsers

Phaser API Documentation
Namespaces
Phaser.Textures.Parsers
Version: Phaser v3.90.0
On this page
Phaser.Textures.Parsers
Scope: static
Source: src/textures/parsers/index.js#L7
Static functions ​
KTXParser ​
<static> KTXParser(data) ​
Description:
Parses a KTX format Compressed Texture file and generates texture data suitable for WebGL from it.
Parameters:
name type optional description
data ArrayBuffer No The data object created by the Compressed Texture File Loader.
Returns: Phaser.Types.Textures.CompressedTextureData - The Compressed Texture data.
Source: src/textures/parsers/KTXParser.js#L7
Since: 3.60.0
PVRParser ​
<static> PVRParser(data) ​
Description:
Parses a PVR format Compressed Texture file and generates texture data suitable for WebGL from it.
Parameters:
name type optional description
data ArrayBuffer No The data object created by the Compressed Texture File Loader.
Returns: Phaser.Types.Textures.CompressedTextureData - The Compressed Texture data.
Source: src/textures/parsers/PVRParser.js#L236
Since: 3.60.0
verifyCompressedTexture ​
<static> verifyCompressedTexture(data) ​
Description:
Verify whether the given compressed texture data is valid.
Compare the dimensions of each mip layer to the rules for that
specific format.
Mip layer size is assumed to have been calculated correctly during parsing.
Parameters:
name type optional description
data Phaser.Types.Textures.CompressedTextureData No The compressed texture data to verify.
Returns: boolean - Whether the compressed texture data is valid.
Source: src/textures/parsers/VerifyCompressedTexture.js#L9
Since: 3.80.0
Previous
Phaser.Textures.FilterMode
Next
Phaser.Textures
Static functions
KTXParser
PVRParser
verifyCompressedTexture
