# 18-apr-2019


### 1 - golang syntax

```golang```
package main

import "fmt"


// global variable declaration
var (m int // see there is no comma here
    n int)


func main() {
    var x int = 1
    var y int
    //nosemincolon


    fmt.Println(x)
    fmt.Println(y)

    var a,b,c = 5.25, 25.25, 14.15 // multiple float32 variable declations
    fmt.Println(a,b,c)


    city:= "Berlin" // string variable declation
    Country:= "Germany"


    fmt.Println(city)
    fmt.Println(Country) //case sensitive


    food,drink,price := "Piziza" , "Pepsi", 123

    fmt.Println(food,drink, price)
    m,n = 1,2
    fmt.Println(m,n)

}
```
- for different processors, will it fail at compile time if the size of int is not there or will it emulate that behaviour at program level to make it portable?


```golang
package main
 
import "fmt"
 
func main(){
    var n1 uint8 // Unsigned 8-bit integers (0 to 255)
    n1 = 200
    fmt.Println(n1)
     
    var n2 uint16 // Unsigned 16-bit integers (0 to 65535)
    n2 = 54200
    fmt.Println(n2)
     
    var n3 uint32 // Unsigned 32-bit integers (0 to 4294967295)
    n3 = 98765214
    fmt.Println(n3)
     
    var n4 uint64 // Unsigned 64-bit integers (0 to 18446744073709551615)
    n4 = 1844674073709551615
    fmt.Println(n4)
     
    var n5 int8 //Signed 8-bit integers (-128 to 127)
    n5 = -52
    fmt.Println(n5)
    fmt.Println(n5*-1)
     
    var n6 int16 // Signed 16-bit integers (-32768 to 32767)
    n6 = -32552
    fmt.Println(n6)
    fmt.Println(n6*-1)
     
    var n7 int32 // Signed 32-bit integers (-2147483648 to 2147483647)
    n7 = -98658754
    fmt.Println(n7)
    fmt.Println(n7*-1)
     
    var n8 int64 // Signed 64-bit integers (-9223372036854775808 to 9223372036854775807)
    n8 = -92211111111111111
    fmt.Println(n8)
    fmt.Println(n8*-1)
}
```

