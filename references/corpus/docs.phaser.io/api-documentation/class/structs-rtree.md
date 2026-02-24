# RTree | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/structs-rtree

Phaser API Documentation
Class
RTree
Version: Phaser v3.90.0
RTree
RBush is a high-performance JavaScript library for 2D spatial indexing of points and rectangles.
It's based on an optimized R-tree data structure with bulk insertion support.
Spatial index is a special data structure for points and rectangles that allows you to perform queries like
"all items within this bounding box" very efficiently (e.g. hundreds of times faster than looping over all items).
This version of RBush uses a fixed min/max accessor structure of [ '.left', '.top', '.right', '.bottom' ] .
This is to avoid the eval like function creation that the original library used, which caused CSP policy violations.
rbush is forked from https://github.com/mourner/rbush by Vladimir Agafonkin
Scope : static
Source: src/structs/RTree.js#L10
Since: 3.0.0
Previous
ProcessQueue
Next
Set
