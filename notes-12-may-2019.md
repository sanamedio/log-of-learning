# 12-may-2019


### 1 - golang file server and http server

file server
```golang
package main

import "net/http"

func main() {
    http.Handle("/", http.FileServer(http.Dir("/")))
    if err := http.ListenAndServe(":8080", nil); err != nil {
        panic(err)
    }

}
```

http server
```golang
package main


import (
    "net/http"
)


func sayHello(w http.ResponseWriter, r *http.Request ){
    w.Write([]byte("hello world"))
}


func main(){

    http.HandleFunc("/", sayHello)

    if err := http.ListenAndServe(":8080", nil); err != nil {
        panic(err)
    }
}

```
