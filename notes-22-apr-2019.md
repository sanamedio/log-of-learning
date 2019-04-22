### 22-apr-2019


### 2 - golang tcp-server and client

- This is a tcp server and client. Interesting thing to observe is both sides we use buffer reader abstraction - whether it's a tcp stream or a input stream. I love the "dial" nomenclature.
- I think error need to handled better as when server is not on, client gets this weird memory error if server is not started , that looks so anti-patternish

https://systembash.com/a-simple-go-tcp-server-and-tcp-client/

server:
```golang
package main


import (

    "net"
    "fmt"
    "bufio"
    "strings"
)


func main(){

    fmt.Println("starting segver...")


    ln, _ := net.Listen("tcp", ":8081")


    conn, _ := ln.Accept()


    for {
        message , _ := bufio.NewReader(conn).ReadString('\n')
        fmt.Print("Mesasge erceived:", string(message))
        newmessage := strings.ToUpper(message)
        conn.Write([]byte(newmessage + "\n" ))
    }
}
```

client:
```golang
package main


import (
    "net"
    "fmt"
    "bufio"
    "os"
)


func main(){


    conn, _ := net.Dial("tcp", "127.0.0.1:8081" )

    for {
        reader  := bufio.NewReader(os.Stdin)
        fmt.Print("Text to send: ")

        text, _ := reader.ReadString('\n')

        fmt.Fprintf(conn, text + "\n" )


        message, _ := bufio.NewReader(conn).ReadString('\n')
        fmt.Print("Message from server : " + message)
    }
}
```

### 1 - pysnooper for logging injection

- this is awesome

```python
import pysnooper

@pysnooper.snoop()
def number_to_bits(number):

    if number:
        bits = []
        while number:
            number, remainder = divmod(number,2)
            bits.insert(0,remainder)
        return bits
    else:
        return [0]


number_to_bits(6)
```

```bash
$ python3 test.py
Starting var:.. number = 6
21:38:03.719596 call         3 @pysnooper.snoop()
21:38:03.720241 line         6     if number:
21:38:03.720443 line         7         bits = []
New var:....... bits = []
21:38:03.720680 line         8         while number:
21:38:03.720829 line         9             number, remainder = divmod(number,2)
New var:....... remainder = 0
Modified var:.. number = 3
21:38:03.721072 line        10             bits.insert(0,remainder)
Modified var:.. bits = [0]
21:38:03.721224 line         8         while number:
21:38:03.721316 line         9             number, remainder = divmod(number,2)
Modified var:.. number = 1
Modified var:.. remainder = 1
21:38:03.721477 line        10             bits.insert(0,remainder)
Modified var:.. bits = [1, 0]
21:38:03.721602 line         8         while number:
21:38:03.721688 line         9             number, remainder = divmod(number,2)
Modified var:.. number = 0
21:38:03.721811 line        10             bits.insert(0,remainder)
Modified var:.. bits = [1, 1, 0]
21:38:03.721935 line         8         while number:
21:38:03.722022 line        11         return bits
21:38:03.722112 return      11         return bits
```
