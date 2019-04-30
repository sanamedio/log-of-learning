### 29-apr-2019

### 6 - kubernetes

katacoda.com/courses/kubernetes

key points :-

1. Kubernete makes container management easier
2. concept of deployment, replication controllers,services, secrets, persistent volumes etc.
3. Tooling around kubernete for pakage management, recovery etc.
4. Kubeless to deploy serverless functions

some handy commands:

```
kubectl cluster-info

kubectl get nodes

Use "kubectl api-resources" for a complete list of supported resources.


Examples:
  # List all pods in ps output format.
  kubectl get pods
  
  # List a single replication controller with specified NAME in ps output format.
  kubectl get replicationcontroller web
  
  # List deployments in JSON output format, in the "v1" version of the "apps" API group:
  kubectl get deployments.v1.apps -o json
  
  # List a single pod in JSON output format.
  kubectl get -o json pod web-pod-13je7
  
  # List a pod identified by type and name specified in "pod.yaml" in JSON output format.
  kubectl get -f pod.yaml -o json
  
  # List all replication controllers and services together in ps output format.
  kubectl get rc,services
  
  # List one or more resources by their type and names.
  kubectl get rc/web service/frontend pods/web-pod-13je7

```

kubectl can manage entities like :-

```  
  * certificatesigningrequests (aka 'csr')  
  * clusterrolebindings  
  * clusterroles  
  * componentstatuses (aka 'cs')  
  * configmaps (aka 'cm')  
  * controllerrevisions  
  * cronjobs  
  * customresourcedefinition (aka 'crd')  
  * daemonsets (aka 'ds')  
  * deployments (aka 'deploy')  
  * endpoints (aka 'ep')  
  * events (aka 'ev')  
  * horizontalpodautoscalers (aka 'hpa')  
  * ingresses (aka 'ing')  
  * jobs  
  * limitranges (aka 'limits')  
  * namespaces (aka 'ns')  
  * networkpolicies (aka 'netpol')  
  * nodes (aka 'no')  
  * persistentvolumeclaims (aka 'pvc')  
  * persistentvolumes (aka 'pv')  
  * poddisruptionbudgets (aka 'pdb')  
  * podpreset  
  * pods (aka 'po')  
  * podsecuritypolicies (aka 'psp')  
  * podtemplates  
  * replicasets (aka 'rs')  
  * replicationcontrollers (aka 'rc')  
  * resourcequotas (aka 'quota')  
  * rolebindings  
  * roles  
  * secrets  
  * serviceaccounts (aka 'sa')  
  * services (aka 'svc')  
  * statefulsets (aka 'sts')  
  * storageclasses (aka 'sc')
```


### 5 - spawining processes in golang

somehow looks more understandable than other languages

```golang
package main

import "fmt"
import "io/ioutil"
import "os/exec"


func main() {

    dateCmd := exec.Command("date")

    dateOut, err := dateCmd.Output()
    if err != nil {
        panic(err)
    }


    fmt.Println("> date")
    fmt.Println(string(dateOut))


    grepCmd := exec.Command("grep", "hello" )


    grepIn, _ := grepCmd.StdinPipe()
    grepOut, _ := grepCmd.StdoutPipe()


    grepCmd.Start()
    grepIn.Write([]byte("hello grep\ngoodbyegrep"))
    grepIn.Close()

    grepBytes, _ := ioutil.ReadAll(grepOut)
    grepCmd.Wait()

    fmt.Println("> grep hello")
    fmt.Println(string(grepBytes))

    lsCmd := exec.Command("bash", "-c" ,"ls -lah")
    lsOut, err := lsCmd.Output()
    if err != nil {

        panic(err)
    }

    fmt.Println("> ls -lah")
    fmt.Println(string(lsOut))


}
```

### 4 - TCP puzzler

- TCP work as state machine on both sides. There are states which both client and server might not agree on.
https://www.joyent.com/blog/tcp-puzzlers
- strace can be used with netcat to study the way both end points behave at system call level. Also netstat can be used to see the state of connection on each of them.

```
 strace -e trace=connect,poll,read,write,close  nc -l -p 8080 
 ```

### 3 - Running binaries as processes

https://gobyexample.com/

this completely replaces the original go application. Anything ran after the exec won't actually execute from go program.

```golang
// In the previous example we looked at
// [spawning external processes](spawning-processes). We
// do this when we need an external process accessible to
// a running Go process. Sometimes we just want to
// completely replace the current Go process with another
// (perhaps non-Go) one. To do this we'll use Go's
// implementation of the classic
// <a href="http://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>
// function.

package main

import "syscall"
import "os"
import "os/exec"

func main() {

    // For our example we'll exec `ls`. Go requires an
    // absolute path to the binary we want to execute, so
    // we'll use `exec.LookPath` to find it (probably
    // `/bin/ls`).
    binary, lookErr := exec.LookPath("ls")
    if lookErr != nil {
        panic(lookErr)
    }

    // `Exec` requires arguments in slice form (as
    // apposed to one big string). We'll give `ls` a few
    // common arguments. Note that the first argument should
    // be the program name.
    args := []string{"ls", "-alh"}

    // `Exec` also needs a set of [environment variables](environment-variables)
    // to use. Here we just provide our current
    // environment.
    env := os.Environ()

    // Here's the actual `syscall.Exec` call. If this call is
    // successful, the execution of our process will end
    // here and be replaced by the `/bin/ls -a -l -h`
    // process. If there is an error we'll get a return
    // value.
    execErr := syscall.Exec(binary, args, env)
    if execErr != nil {
        panic(execErr)
    }
}
```

### 2 - handling sys signals in golang

what if I remove SIGINT from list?
what if I remove SIGTERM from list ?
how to send these signals to these processes kill -s SIGINT PID

```golang
// Sometimes we'd like our Go programs to intelligently
// handle [Unix signals](http://en.wikipedia.org/wiki/Unix_signal).
// For example, we might want a server to gracefully
// shutdown when it receives a `SIGTERM`, or a command-line
// tool to stop processing input if it receives a `SIGINT`.
// Here's how to handle signals in Go with channels.

package main

import "fmt"
import "os"
import "os/signal"
import "syscall"

func main() {

    // Go signal notification works by sending `os.Signal`
    // values on a channel. We'll create a channel to
    // receive these notifications (we'll also make one to
    // notify us when the program can exit).
    sigs := make(chan os.Signal, 1)
    done := make(chan bool, 1)

    // `signal.Notify` registers the given channel to
    // receive notifications of the specified signals.
    signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

    // This goroutine executes a blocking receive for
    // signals. When it gets one it'll print it out
    // and then notify the program that it can finish.
    go func() {
        sig := <-sigs
        fmt.Println()
        fmt.Println(sig)
        done <- true
    }()

    // The program will wait here until it gets the
    // expected signal (as indicated by the goroutine
    // above sending a value on `done`) and then exit.
    fmt.Println("awaiting signal")
    <-done
    fmt.Println("exiting")
}

```

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
