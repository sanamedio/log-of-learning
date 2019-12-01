# 01-dec-2019

### 3 - Command line app with axios to show jokes

From https://developer.okta.com/blog/2019/06/18/command-line-app-with-nodejs

package.json
```
{
  "name": "cli-tuts",
  "version": "1.0.0",
  "description": "",
  "main": "bin/index.js",
  "bin" : {
	  "hello" : "./bin/index.js"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```
bin/index.js
```js
#!/usr/bin/env node


/*
const chalk = require("chalk");
const boxen = require("boxen");

const greeting = chalk.white.bold("Hello!");


const boxenOptions = {

	padding: 1,
	margin: 1,
	borderStype: "round",
	borderColor: "green",
	backgroundColor: "#555555"
};


const msgBox = boxen(greeting, boxenOptions);

console.log(msgBox);
*/


const yargs = require("yargs");
const axios = require("axios");


const options = yargs
	.usage("Usage: -n <name>")
	.option("n", {
		alias: "name",
		describe: "Your name",
		type: "string",
		demandOption: true
	})
	.option("s", {
		alias: "search",
		describe: "Search term",
		type: "string"})
	.argv;

const greeting = `Hello, ${options.name}!`;

console.log(greeting);


if( options.search ) {
	console.log(`Searching for jokes about ${options.search}...`)
}else{
	console.log("Here's a random joke for you:");
}



const url = options.search ? `https://icanhazdadjoke.com/search?term=${escape(options.search)}` : "https://icanhazdadjoke.com/";

axios.get(url, { headers: { Accept: "application/json" } })
 .then(res => {
   if (options.search) {
     // if searching for jokes, loop over the results
     res.data.results.forEach( j => {
       console.log("\n" + j.joke);
     });
     if (res.data.results.length === 0) {
       console.log("no jokes found :'(");
     }
   } else {
     console.log(res.data.joke);
   }
 });


```





### 2 - Pretty boxes and colors while making node CLI tools

From https://developer.okta.com/blog/2019/06/18/command-line-app-with-nodejs

```bash
npm install chalk@2.4 boxen@4.0
```

```js
#!/usr/bin/env node

const chalk = require("chalk");
const boxen = require("boxen");

const greeting = chalk.white.bold("Hello!");


const boxenOptions = {

	padding: 1,
	margin: 1,
	borderStype: "round",
	borderColor: "green",
	backgroundColor: "#555555"
};


const msgBox = boxen(greeting, boxenOptions);

console.log(msgBox);
```




### 1 - Listing global npm modules

```bash
$ npm ls -g --depth=0
/usr/local/lib
└── hexo-cli@3.1.0
```
