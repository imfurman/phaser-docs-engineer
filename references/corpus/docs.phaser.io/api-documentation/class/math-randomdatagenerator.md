# RandomDataGenerator | Phaser Help

Source: https://docs.phaser.io/api-documentation/class/math-randomdatagenerator

Phaser API Documentation
Class
RandomDataGenerator
Version: Phaser v3.90.0
On this page
RandomDataGenerator
A seeded Random Data Generator.
Access via Phaser.Math.RND which is an instance of this class pre-defined
by Phaser. Or, create your own instance to use as you require.
The Math.RND generator is seeded by the Game Config property value seed .
If no such config property exists, a random number is used.
If you create your own instance of this class you should provide a seed for it.
If no seed is given it will use a 'random' one based on Date.now.
Constructor
new RandomDataGenerator([seeds])
Parameters
name type optional description
seeds string | Array.<string> Yes The seeds to use for the random number generator.
Scope : static
Source: src/math/random-data-generator/RandomDataGenerator.js#L9
Since: 3.0.0
Public Members ​
signs ​
signs: Array.<number> ​
Description:
Signs to choose from.
Source: src/math/random-data-generator/RandomDataGenerator.js#L92
Since: 3.0.0
Public Methods ​
angle ​
<instance> angle() ​
Description:
Returns a random angle between -180 and 180.
Returns: number - A random number between -180 and 180.
Source: src/math/random-data-generator/RandomDataGenerator.js#L412
Since: 3.0.0
between ​
<instance> between(min, max) ​
Description:
Returns a random integer between and including min and max.
This method is an alias for RandomDataGenerator.integerInRange.
Parameters:
name type optional description
min number No The minimum value in the range.
max number No The maximum value in the range.
Returns: number - A random number between min and max.
Source: src/math/random-data-generator/RandomDataGenerator.js#L278
Since: 3.0.0
frac ​
<instance> frac() ​
Description:
Returns a random real number between 0 and 1.
Returns: number - A random real number between 0 and 1.
Source: src/math/random-data-generator/RandomDataGenerator.js#L235
Since: 3.0.0
init ​
<instance> init(seeds) ​
Description:
Initialize the state of the random data generator.
Parameters:
name type optional description
seeds string | Array.<string> No The seeds to initialize the random data generator with.
Source: src/math/random-data-generator/RandomDataGenerator.js#L163
Since: 3.0.0
integer ​
<instance> integer() ​
Description:
Returns a random integer between 0 and 2^32.
Returns: number - A random integer between 0 and 2^32.
Source: src/math/random-data-generator/RandomDataGenerator.js#L221
Since: 3.0.0
integerInRange ​
<instance> integerInRange(min, max) ​
Description:
Returns a random integer between and including min and max.
Parameters:
name type optional description
min number No The minimum value in the range.
max number No The maximum value in the range.
Returns: number - A random number between min and max.
Source: src/math/random-data-generator/RandomDataGenerator.js#L262
Since: 3.0.0
normal ​
<instance> normal() ​
Description:
Returns a random real number between -1 and 1.
Returns: number - A random real number between -1 and 1.
Source: src/math/random-data-generator/RandomDataGenerator.js#L311
Since: 3.0.0
pick ​
<instance> pick(array) ​
Description:
Returns a random element from within the given array.
Tags:
generic
genericUse
genericUse
Parameters:
name type optional description
array Array.<T> No The array to pick a random element from.
Returns: T - A random member of the array.
Source: src/math/random-data-generator/RandomDataGenerator.js#L345
Since: 3.0.0
real ​
<instance> real() ​
Description:
Returns a random real number between 0 and 2^32.
Returns: number - A random real number between 0 and 2^32.
Source: src/math/random-data-generator/RandomDataGenerator.js#L249
Since: 3.0.0
realInRange ​
<instance> realInRange(min, max) ​
Description:
Returns a random real number between min and max.
Parameters:
name type optional description
min number No The minimum value in the range.
max number No The maximum value in the range.
Returns: number - A random number between min and max.
Source: src/math/random-data-generator/RandomDataGenerator.js#L295
Since: 3.0.0
rotation ​
<instance> rotation() ​
Description:
Returns a random rotation in radians, between -3.141 and 3.141
Returns: number - A random number between -3.141 and 3.141
Source: src/math/random-data-generator/RandomDataGenerator.js#L425
Since: 3.0.0
shuffle ​
<instance> shuffle([array]) ​
Description:
Shuffles the given array, using the current seed.
Tags:
generic
genericUse
Parameters:
name type optional description
array Array.<T> Yes The array to be shuffled.
Returns: Array.<T> - The shuffled array.
Source: src/math/random-data-generator/RandomDataGenerator.js#L473
Since: 3.7.0
sign ​
<instance> sign() ​
Description:
Returns a sign to be used with multiplication operator.
Returns: number - -1 or +1.
Source: src/math/random-data-generator/RandomDataGenerator.js#L364
Since: 3.0.0
sow ​
<instance> sow(seeds) ​
Description:
Reset the seed of the random data generator.
Note : the seed array is only processed up to the first undefined (or null ) value, should such be present.
Parameters:
name type optional description
seeds Array.<string> No The array of seeds: the toString() of each value is used.
Source: src/math/random-data-generator/RandomDataGenerator.js#L183
Since: 3.0.0
state ​
<instance> state([state]) ​
Description:
Gets or Sets the state of the generator. This allows you to retain the values
that the generator is using between games, i.e. in a game save file.
To seed this generator with a previously saved state you can pass it as the
seed value in your game config, or call this method directly after Phaser has booted.
Call this method with no parameters to return the current state.
If providing a state it should match the same format that this method
returns, which is a string with a header !rnd followed by the c ,
s0 , s1 and s2 values respectively, each comma-delimited.
Parameters:
name type optional description
state string Yes Generator state to be set.
Returns: string - The current state of the generator.
Source: src/math/random-data-generator/RandomDataGenerator.js#L438
Since: 3.0.0
timestamp ​
<instance> timestamp(min, max) ​
Description:
Returns a random timestamp between min and max, or between the beginning of 2000 and the end of 2020 if min and max aren't specified.
Parameters:
name type optional description
min number No The minimum value in the range.
max number No The maximum value in the range.
Returns: number - A random timestamp between min and max.
Source: src/math/random-data-generator/RandomDataGenerator.js#L396
Since: 3.0.0
uuid ​
<instance> uuid() ​
Description:
Returns a valid RFC4122 version4 ID hex string from https://gist.github.com/1308368
Returns: string - A valid RFC4122 version4 ID hex string
Source: src/math/random-data-generator/RandomDataGenerator.js#L324
Since: 3.0.0
weightedPick ​
<instance> weightedPick(array) ​
Description:
Returns a random element from within the given array, favoring the earlier entries.
Tags:
generic
genericUse
genericUse
Parameters:
name type optional description
array Array.<T> No The array to pick a random element from.
Returns: T - A random member of the array.
Source: src/math/random-data-generator/RandomDataGenerator.js#L377
Since: 3.0.0
Previous
Quaternion
Next
Vector2
Public Members
signs
Public Methods
angle
between
frac
init
integer
integerInRange
normal
pick
real
realInRange
rotation
shuffle
sign
sow
state
timestamp
uuid
weightedPick
