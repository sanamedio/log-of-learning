### 29-apr-2019

### 1 - go exit value, is not same as what is returned

- what if return is before exit
- what if exit is after return

```golang
// Use `os.Exit` to immediately exit with a given
// status.

package main

import "fmt"
import "os"

func main() {

    // `defer`s will _not_ be run when using `os.Exit`, so
    // this `fmt.Println` will never be called.
    defer fmt.Println("!")

    // Exit with status 3.
    os.Exit(3)
}

// Note that unlike e.g. C, Go does not use an integer
// return value from `main` to indicate exit status. If
// you'd like to exit with a non-zero status you should
// use `os.Exit`.
```
