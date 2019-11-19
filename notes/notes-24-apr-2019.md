# 24-apr-2019

### 7 - go basic simple programs

https://github.com/adonovan/gopl.io

### 6 - adding latency to network for testing

With a combination of toxiproxy and toxy - both TCP level and HTTP level throttling and latency control can be done. toxyproxy is written in golang. Nginx and haproxy require too much boilerplate setup.

- https://github.com/Shopify/toxiproxy
- https://stackoverflow.com/questions/14752943/using-nginx-to-simulate-slow-response-time-for-testing-purposes
- https://github.com/h2non/toxy


http://httpbin.org - nice endpoint with configurable behaviours

### 5 - python http logging

https://coderwall.com/p/z2_hwa/quick-and-dirty-http-logging-in-python

```python
import urllib2

# New lines begin here
http_logger = urllib2.HTTPHandler(debuglevel = 1)
opener = urllib2.build_opener(http_logger) # put your other handlers here too!
urllib2.install_opener(opener)
# End of new lines

request = urllib2.Request('http://jigsaw.w3.org/HTTP/300/302.html')
response = urllib2.urlopen(request)
print "Response code was: %d" % response.getcode()
```

output in python2:
```
send: 'GET /HTTP/300/302.html HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: jigsaw.w3.org\r\nConnection: close\r\nUser-Agent: Python-urllib/2.7\r\n\r\n'
reply: 'HTTP/1.1 302 Found\r\n'
header: Connection: close
header: Date: Tue, 23 Apr 2019 22:56:43 GMT
header: Content-Length: 389
header: Content-Type: text/html;charset=ISO-8859-1
header: Location: http://jigsaw.w3.org/HTTP/300/Overview.html
header: Server: Jigsaw/2.3.0-beta4
send: 'GET /HTTP/300/Overview.html HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: jigsaw.w3.org\r\nConnection: close\r\nUser-Agent: Python-urllib/2.7\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Connection: close
header: Date: Tue, 23 Apr 2019 22:56:43 GMT
header: Content-Length: 1651
header: Content-Type: text/html
header: Etag: "14u2rht:164ua3k6o"
header: Last-Modified: Mon, 18 Jul 2011 09:47:18 GMT
header: Server: Jigsaw/2.3.0-beta2
Response code was: 200
```


### 4 - golang now

```golang
package main
 
import (
    "github.com/jinzhu/now"
    "fmt"
)
 
func main() {
 
    fmt.Println("All the beginnings...")
    fmt.Println(now.BeginningOfMinute())
    fmt.Println(now.BeginningOfHour())
    fmt.Println(now.BeginningOfDay())
    fmt.Println(now.BeginningOfWeek())
    fmt.Println(now.BeginningOfMonth())
    fmt.Println(now.BeginningOfQuarter())
    fmt.Println(now.BeginningOfYear())
 
}
```

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
