# 13-may-2019


### 1 - Learning kubernetes by hands-on

What I learned
 - kubectl connects to any kubernete cluster
 - concept of contexts to switch between different clusters
 - cluster can be via minikube, raspberri, aws, gcloud or azure
 - kube-system namespace as k8s system level services
 - generally it's easier to setup a local registry inside kubernete for the images
 - helm is the package manager for k8s
 - replicaset(rs) helps the services scale
 - pod is a collection of containers which are scheduled together
 - k8s don't really do well if resources are less than what is requested(I guesss that's due to the scheduling algo ? )
 - k8s could use docker, rkt etc. both support OCI. but docker not been made from groundup for k8s whereas some others are
 - declarative yaml config, is what k8s tries to heal back for you. k8s makes sure that under failures the services heal themseslves back
 - ~/.minikube ~/.kube folders if you running local kubectl and minkube contains all the info
 - auto scaling can be done based on cpu/memory 
 - healthprobe | liveness probes are easy to configure
 - k8s help you utilize your computing resources to best and provides good biased choices towards microservices architecture
 - It kind of makes you cloud independent? kubernete is manager for your resources, so it comes in between your apps and the underlying infra

https://github.com/dgkanatsios/CKAD-exercises

https://www.linux.com/blog/learn/chapter/Intro-to-Kubernetes/2017/5/set-cicd-pipeline-kubernetes-part-1-overview

https://idursun.com/posts/zero_to_kubernetes/
