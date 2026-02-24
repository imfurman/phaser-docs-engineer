# Installing | Phaser Help

Source: https://docs.phaser.io/phaser/getting-started/installation

Getting Started
Installing
On this page
Installing
Create Phaser Game App ​
The easiest way to get started quickly with Phaser is our create-phaser-game app. This CLI tool presents an interactive selection of official project templates and demo games. Issue the command, answer some questions and the app will download and configure the right package for you.
npm create @phaserjs/game@latest
npx @phaserjs/create-game@latest
yarn create @phaserjs/game
pnpm create @phaserjs/game@latest
bun create @phaserjs/game@latest
We have a create game app tutorial you can read to learn more about this tool and what it offers.
Installing Phaser from NPM ​
Install via npm :
npm install phaser
Cloning Phaser from GitHub ​
Phaser is available on GitHub at https://github.com/phaserjs/phaser
You can clone it via git with either:
https://github.com/phaserjs/phaser.git
# or
[email protected] :phaserjs/phaser.git
Or, you can use GitHub Desktop. See the Phaser GitHub page for details.
Using Phaser from a CDN ​
Phaser is on jsDelivr which is a "super-fast CDN for developers". Include either of the following in your html:
< script src = " //cdn.jsdelivr.net/npm/ [email protected] /dist/phaser.js " > </ script >
< script src = " //cdn.jsdelivr.net/npm/ [email protected] /dist/phaser.min.js " > </ script >
It is also available from Cloudflare's cdnjs :
< script src = " https://cdnjs.cloudflare.com/ajax/libs/phaser/3.86.0/phaser.js " > </ script >
< script src = " https://cdnjs.cloudflare.com/ajax/libs/phaser/3.86.0/phaser.min.js " > </ script >
Phaser TypeScript Definitions ​
Full TypeScript definitions can be found inside the types folder . They are also referenced in the types entry in package.json , meaning modern editors such as VSCode will detect them automatically.
Depending on your project, you may need to add the following to your tsconfig.json file:
"lib" : [ "es6" , "dom" , "dom.iterable" , "scripthost" ] ,
"typeRoots" : [ "./node_modules/phaser/types" ] ,
"types" : [ "Phaser" ]
Previous
What is Phaser?
Next
Working with Phaser
Create Phaser Game App
Installing Phaser from NPM
Cloning Phaser from GitHub
Using Phaser from a CDN
Phaser TypeScript Definitions
