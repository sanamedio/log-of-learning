# 24-apr-2019


### 1 - golang cmd prompt

run go get first, and then go run

```golang
package main

import "github.com/segmentio/go-prompt"

var langs = []string{
  "c",
  "c++",
  "lua",
  "go",
  "js",
  "ruby",
  "python",
}

func main() {
  i := prompt.Choose("What's your favorite language?", langs)
  println("picked: " + langs[i])
}
```
