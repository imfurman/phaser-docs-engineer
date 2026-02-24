# Phaser.Loader.FileTypesManager | Phaser Help

Source: https://docs.phaser.io/api-documentation/namespace/loader-filetypesmanager

Phaser API Documentation
Namespaces
Phaser.Loader.FileTypesManager
Version: Phaser v3.90.0
On this page
Phaser.Loader.FileTypesManager
Scope: static
Source: src/loader/FileTypesManager.js#L9
Static functions ​
destroy ​
<static> destroy() ​
Description:
Removed all associated file types.
Source: src/loader/FileTypesManager.js#L50
Since: 3.0.0
install ​
<static> install(loader) ​
Description:
Static method called when a LoaderPlugin is created.
Loops through the local types object and injects all of them as
properties into the LoaderPlugin instance.
Parameters:
name type optional description
loader Phaser.Loader.LoaderPlugin No The LoaderPlugin to install the types into.
Source: src/loader/FileTypesManager.js#L15
Since: 3.0.0
register ​
<static> register(key, factoryFunction) ​
Description:
Static method called directly by the File Types.
The key is a reference to the function used to load the files via the Loader, i.e. image .
Parameters:
name type optional description
key string No The key that will be used as the method name in the LoaderPlugin.
factoryFunction function No The function that will be called when LoaderPlugin.key is invoked.
Source: src/loader/FileTypesManager.js#L34
Since: 3.0.0
Previous
Phaser.Loader.FileTypes
Next
Phaser.Loader
Static functions
destroy
install
register
