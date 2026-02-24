# ImageCollection | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/tilemaps-imagecollection

Phaser API Documentation
Class
ImageCollection
Version: Phaser v3.90.0
On this page
ImageCollection
An Image Collection is a special Tile Set containing multiple images, with no slicing into each image.
Image Collections are normally created automatically when Tiled data is loaded.
Constructor
new ImageCollection(name, firstgid, [width], [height], [margin], [spacing], [properties])
Parameters
name type optional default description
name string No The name of the image collection in the map data.
firstgid number No The first image index this image collection contains.
width number Yes 32 Width of widest image (in pixels).
height number Yes 32 Height of tallest image (in pixels).
margin number Yes 0 The margin around all images in the collection (in pixels).
spacing number Yes 0 The spacing between each image in the collection (in pixels).
properties object Yes "{}" Custom Image Collection properties.
Scope : static
Source: src/tilemaps/ImageCollection.js#L9
Since: 3.0.0
Public Members ​
firstgid ​
firstgid: number ​
Description:
The Tiled firstgid value.
This is the starting index of the first image index this Image Collection contains.
Source: src/tilemaps/ImageCollection.js#L48
Since: 3.0.0
imageHeight ​
imageHeight: number ​
Description:
The height of the tallest image (in pixels).
Source: src/tilemaps/ImageCollection.js#L68
Since: 3.0.0
imageMarge ​
imageMarge: number ​
Description:
The margin around the images in the collection (in pixels).
Use setSpacing to change.
Source: src/tilemaps/ImageCollection.js#L78
Since: 3.0.0
images ​
images: array ​
Description:
The cached images that are a part of this collection.
Source: src/tilemaps/ImageCollection.js#L109
Since: 3.0.0
imageSpacing ​
imageSpacing: number ​
Description:
The spacing between each image in the collection (in pixels).
Use setSpacing to change.
Source: src/tilemaps/ImageCollection.js#L89
Since: 3.0.0
imageWidth ​
imageWidth: number ​
Description:
The width of the widest image (in pixels).
Source: src/tilemaps/ImageCollection.js#L58
Since: 3.0.0
name ​
name: string ​
Description:
The name of the Image Collection.
Source: src/tilemaps/ImageCollection.js#L39
Since: 3.0.0
properties ​
properties: object ​
Description:
Image Collection-specific properties that are typically defined in the Tiled editor.
Source: src/tilemaps/ImageCollection.js#L100
Since: 3.0.0
total ​
total: number ​
Description:
The total number of images in the image collection.
Source: src/tilemaps/ImageCollection.js#L119
Since: 3.0.0
Public Methods ​
addImage ​
<instance> addImage(gid, image, width, height) ​
Description:
Add an image to this Image Collection.
Parameters:
name type optional description
gid number No The gid of the image in the Image Collection.
image string No The the key of the image in the Image Collection and in the cache.
width number No The width of the image in the Image Collection.
height number No The height of the image in the Image Collection.
Returns: Phaser.Tilemaps.ImageCollection - This ImageCollection object.
Source: src/tilemaps/ImageCollection.js#L145
Since: 3.0.0
containsImageIndex ​
<instance> containsImageIndex(imageIndex) ​
Description:
Returns true if and only if this image collection contains the given image index.
Parameters:
name type optional description
imageIndex number No The image index to search for.
Returns: boolean - True if this Image Collection contains the given index.
Source: src/tilemaps/ImageCollection.js#L130
Since: 3.0.0
Previous
TextureSource
Next
LayerData
Public Members
firstgid
imageHeight
imageMarge
images
imageSpacing
imageWidth
name
properties
total
Public Methods
addImage
containsImageIndex
