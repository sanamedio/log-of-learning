# 24-apr-2019


### 3 - colorful text in golang

https://code.tutsplus.com/tutorials/12-indispensable-go-packages-and-libraries--cms-29008

```golang
package main
 
import (
    "github.com/fatih/color"
)
 
func main() {
    color.Red("Roses are red")
    color.Blue("Violets are blue")
}
```

```golang
package main
 
import (
    "github.com/fatih/color"
    "fmt"
)
 
func main() {
    minion := color.New(color.FgBlack).Add(color.BgYellow).Add(color.Bold)
    minion.Println("Minion says: banana!!!!!!")
 
    m := minion.PrintlnFunc()
    m("I want another banana!!!!!")
 
    slantedRed := color.New(color.FgRed, color.BgWhite, color.Italic).SprintFunc()
    fmt.Println("I've made a huge", slantedRed("mistake"))
}
```

### 2 - golang-set

```golang
package main
 
import (
    "fmt"
    "github.com/deckarep/golang-set"
)
 
 
func main() {
    basicColors := mapset.NewSet()
    basicColors.Add("Red")
    basicColors.Add("Blue")
    basicColors.Add("Green")
 
    if basicColors.Contains("Green") {
        fmt.Println("Yay! 'Green' is a basic color")
    } else {
        fmt.Println("What a disappointment! 'Green' is not a basic color")
    }
 
 
    if basicColors.Contains("Yellow") {
        fmt.Println("Yay! 'Yellow' is a basic color")
    } else {
        fmt.Println("What a disappointment! 'Yellow' is not a basic color")
    }
}
```

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
