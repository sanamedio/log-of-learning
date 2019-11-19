### 02-may-2019

### 3 - knight closure

```python

visited = []

def knight_closure(x,y):
    global visited

    print(x,y)
    visited = visited + [ (x, y) ]

    for i in range(-2,3):
        for j in range(-2,3):
            if (abs(i) + abs(j)) == 3 and (0<= x+i < 8) and (0 <= y+j < 8) and (x+i,y+j) not in visited:
                knight_closure(x+i,y+j)



knight_closure(0,0)
```

### 2 - Python disable warnings

some ways to disable insecure requests warning

```
export PYTHONWARNINGS="ignore:Unverified HTTPS request"
```


```python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```

```python
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

### 1 - embedded etcd3 server in golang

https://godoc.org/github.com/coreos/etcd/embed

```golang
import (
	"log"
	"time"

	"go.etcd.io/etcd/embed"
)

func main() {
	cfg := embed.NewConfig()
	cfg.Dir = "default.etcd"
	e, err := embed.StartEtcd(cfg)
	if err != nil {
		log.Fatal(err)
	}
	defer e.Close()
	select {
	case <-e.Server.ReadyNotify():
		log.Printf("Server is ready!")
	case <-time.After(60 * time.Second):
		e.Server.Stop() // trigger a shutdown
		log.Printf("Server took too long to start!")
	}
	log.Fatal(<-e.Err())
}
```
