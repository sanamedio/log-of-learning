# 18-apr-2019


### 3 - golang variadic functions


```golang
package main
 
import "fmt"
 
func main() {
    variadicExample("red", "blue", "green", "yellow")
}
 
func variadicExample(s ...string) {
    fmt.Println(s[0])
    fmt.Println(s[3])
}
```


```golang
package main

import "fmt"

func main() {

    variadicExample()
    variadicExample("red", "blue")
    variadicExample("red", "blue", "green")
    variadicExample("red", "blue", "green", "yellow")
}

func variadicExample(s ...string) {
    fmt.Println(s)
}
```


```golang
package main

import "fmt"

func main() {
    fmt.Println(calculation("Rectangle", 20, 30))
    fmt.Println(calculation("Square", 20))
}

func calculation(str string, y ...int) int {

    area := 1

    for _, val := range y {
        if str == "Rectangle" {
            area *= val
        } else if str == "Square" {
            area = val * val
        }
    }
    return area
}
```


```golang
package main

import (
    "fmt"
    "reflect"
)

func main() {
    variadicExample(1, "red", true, 10.5, []string{"foo", "bar", "baz"},
        map[string]int{"apple": 23, "tomato": 13})
}

func variadicExample(i ...interface{}) {
    for _, v := range i {
        fmt.Println(v, "--", reflect.ValueOf(v).Kind())
    }
}
```


### 2 - golang defer

- how does defer internally works? does it do it in reversed order ?

```golang
package main
import "fmt"

/*
A defer statement is often used with paired operations like open and close, connect and disconnect, or lock and unlock to ensure that resources are released in all cases, no matter how complex the control flow. The right place for a defer statement that releases a resource is immediately after the resource has been successfully acquired.
*/


func first(){
    fmt.Println("First")
}

func second() {
    fmt.Println("Secondd")
}


func main() {
    defer second()
    first()
}
```

without defer :
```golang
func ReadWrite() bool {
    file.Open("file")
 
    if failureX {
    file.Close()   //And here...
    return false
    }
    if failureY {
    file.Close()  //And here...
    return false
    }
    file.Close()  //And here...
    return true
}
```
with defer
```golang
func ReadWrite() bool {
file.Open("file")
defer file.Close()   //file.Close() is added to defer list
// Do your thing
if failureX {
return false   // Close() is now done automatically
}
if failureY {
return false   // And here too
}
return true   // And here
}
```
- It keeps our Close call near our Open call so it's easier to understand.
- If our function had multiple return statements (perhaps one in an if and one in an else), Close will happen before both of them.
- Deferred Functions are run even if a runtime panic occurs.
- Deferred functions are executed in LIFO order, so the above code prints: 4 3 2 1 0.
- You can put multiple functions on the "deferred list", like this example.

```golang
package main
import "fmt"
func main() {
    for i := 0; i < 5; i++ {
        defer fmt.Printf("%d ", i)
    }
}
```
### 1 - golang syntax

http://www.golangprograms.com

```golang
package main
 
import "fmt"
 
func main() {
    fmt.Println(add(20, 30))
}
 
func add(x int, y int) (total int) {
    total = x + y
    return total
}
```

```golang
package main
 
import "fmt"
 
func main() {
    add(20, 30)
}
 
func add(x int, y int) {
    total := 0
    total = x + y
    fmt.Println(total)
}
```

```golang
package main
 
import "fmt"
 
func main() {
    fmt.Println(add(20, 30))
}
 
func add(x int, y int) int {
    total := 0
    total = x + y
    return total
}
```


```golang
package main
 
import "fmt"
 
func main() {
	i := 5
	for {
		fmt.Println("Hello")
		if i == 10 {
			break
		}
		i++
	}
}
```

```golang
package main
 
import "fmt"
 
func main() {
	for range "Hello" {
		fmt.Println("Hello")
	}
}
```

```golang
package main
 
import "fmt"
 
func main() {
 
	// Example 1
	strDict := map[string]string{"Japan": "Tokyo", "China": "Beijing", "Canada": "Ottawa"}
	for index, element := range strDict {
		fmt.Println("Index :", index, " Element :", element)
	}
 
	// Example 2
	for key := range strDict {
		fmt.Println(key)
	}
 
	// Example 3
	for _, value := range strDict {
		fmt.Println(value)
	}
}
```


```golang
package main
 
import "fmt"
 
func main() {
 
	k := 1
	for ; k <= 10; k++ {
		fmt.Println(k)
	}
 
	k = 1
	for k <= 10 {
		fmt.Println(k)
		k++
	}
 
	for k := 1; ; k++ {
		fmt.Println(k)
		if k == 10 {
			break
		}
	}
}
```

```golang
package main
 
import (
	"fmt"
	"time"
)
 
func main() {
	today := time.Now()
 
	switch today.Day() {
	case 5:
		fmt.Println("Today is 5th. Clean your house.")
	case 10:
		fmt.Println("Today is 10th. Buy some wine.")
	case 15:
		fmt.Println("Today is 15th. Visit a doctor.")
	case 25:
		fmt.Println("Today is 25th. Buy some food.")
	case 31:
		fmt.Println("Party tonight.")
	default:
		fmt.Println("No information available for that day.")
	}
}
```

failthrough

```golang
package main
 
import (
	"fmt"
	"time"
)
 
func main() {
	today := time.Now()
 
	switch today.Day() {
	case 5:
		fmt.Println("Clean your house.")
		fallthrough
	case 10:
		fmt.Println("Buy some wine.")
		fallthrough
	case 15:
		fmt.Println("Visit a doctor.")
		fallthrough
	case 25:
		fmt.Println("Buy some food.")
		fallthrough
	case 31:
		fmt.Println("Party tonight.")
	default:
		fmt.Println("No information available for that day.")
	}
}
```
- conditional initializers in case

```golang
package main
 
import (
	"fmt"
	"time"
)
 
func main() {
	today := time.Now()
 
	switch {
	case today.Day() < 5:
		fmt.Println("Clean your house.")
	case today.Day() <= 10:
		fmt.Println("Buy some wine.")
	case today.Day() > 15:
		fmt.Println("Visit a doctor.")
	case today.Day() == 25:
		fmt.Println("Buy some food.")
	default:
		fmt.Println("No information available for that day.")
	}
}
```

- switch statement with initialization

```golang
package main
 
import (
	"fmt"
	"time"
)
 
func main() {
	switch today := time.Now(); {
	case today.Day() < 5:
		fmt.Println("Clean your house.")
	case today.Day() <= 10:
		fmt.Println("Buy some wine.")
	case today.Day() > 15:
		fmt.Println("Visit a doctor.")
	case today.Day() == 25:
		fmt.Println("Buy some food.")
	default:
		fmt.Println("No information available for that day.")
	}
}
```


```golang
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

```golang
package main
 
import (
    "fmt"
)
 
func main() {
    var i int = 10
    var s string = "Japan"
    fmt.Println(i)
    fmt.Println(s)
}
```


```golang
package main
 
import (
    "fmt"
)
 
func main() {
    var intVar int
    var strVar string
 
    intVar = 10
    strVar = "Australia"
 
    fmt.Println(intVar)
    fmt.Println(strVar)
}
```

```golang
package main
 
import (
	"fmt"
)
 
func main() {
	s := "Japan"
	fmt.Println(s)
}
```


```golang
package main
 
import (
	"fmt"
)
 
var s = "Japan"
 
func main() {
	fmt.Println(s)
	x := true
 
	if x {
		y := 1
		if x != false {
			fmt.Println(s)
			fmt.Println(x)
			fmt.Println(y)
		}
	}
	fmt.Println(x)
}
```

```golang
package main
import "fmt"
const (
        x=10
        y=20
        z=30
    )
func main(){
    const name string ="John Carry" // Constant with data type
    fmt.Println(name)
    const age = 35 // Constant without data type
    fmt.Println(age)
    fmt.Println(x,y,z)
}
```









