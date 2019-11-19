# 26-apr-2019

### 5 - AWS 

- https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/
- https://www.airpair.com/aws/posts/building-a-scalable-web-app-on-amazon-web-services-p1?wed

### 4 - getting links from text

```golang
package main

import "fmt"
import "gitlab.com/golang-commonmark/linkify"

func main() {
	input := `
	Check out this link to http://google.com
You can also email support@example.com to view more.

Some more links: fsf.org http://www.gnu.org/licenses/gpl-3.0.en.html 127.0.0.1
                 localhost:80	github.com/trending?l=Go	//reddit.com/r/golang
mailto:r@golang.org some.nonexistent.host.name flibustahezeous3.onion
`
	for _, l := range linkify.Links(input) {
		fmt.Printf("Scheme: %-8s  URL: %s\n", l.Scheme, input[l.Start:l.End])
	}

}
```

### 3 - go routine

running a function in goroutine, makes it run parallely

```golang
package main


import "fmt"
import "net/http"
import "time"

func log(msg string){


    fmt.Println(msg)
}


func main(){


    http.HandleFunc("/", HelloServer)
    http.ListenAndServe(":8080", nil )


}



func HelloServer(w http.ResponseWriter, r *http.Request) {

    go log("Hello " + time.Now().String())
    fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:] )

}
```

### 2 - sentry with golang

- https://docs.sentry.io/clients/go/ 

```golang
package main

import "github.com/getsentry/raven-go"
import "os"
import "log"
import "fmt"


func init() {
    raven.SetDSN("https://c10f4d3a8d6eXXXXXXXXXf830bc9ef:8bd45cXXXXXXXXd3154db8f6a2b@sentry.io/000000")
}


func main(){
    
    f, err := os.Open("filename.ext")
    if err != nil {
        raven.CaptureErrorAndWait(err, nil)
        log.Panic(err)
    }

    fmt.Println(f)


}
```

### 1 - server/client in bash for quick use


client:
```bash
#!/bin/sh

while true; do
  msg="$(date '+%Y-%m-%d %H:%M:%S') hello from ${HOSTNAME}"
  echo ${msg}
  echo ${msg} | nc -w 1 localhost 4242
  sleep 1
done;
```


server:
```bash
#!/bin/sh

port="4242"
echo "starting server on ${port}"

while true; do 
  nc -l -p ${port} -vv -k -q 60
done;
```
