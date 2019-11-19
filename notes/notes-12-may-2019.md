# 12-may-2019

### 2 - simple random numbers example in golang

```golang
package main


import "math/rand"

const MaxRnd = 16

func StatRandomNumbers(n int) (int, int) {

    var a,b int

    for i := 0; i < n; i++ {

        if rand.Intn(MaxRnd) < MaxRnd/2 {
            a = a + 1
        } else {
            b++
        }
    }


    return a,b
}
```

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
