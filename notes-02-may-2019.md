### 02-may-2019


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
