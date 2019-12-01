# 01-dec-2019

### 2 - Preety boxes and colors while making node CLI tools

From https://developer.okta.com/blog/2019/06/18/command-line-app-with-nodejs

```bash
npm install chalk@2.4 boxen@4.0
```

```
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
