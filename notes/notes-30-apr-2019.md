# 30-apr-2019

### 2 - Python release vs. distribution

https://pydist.com/blog/distributions-vs-releases

Python is special in that it treats C extensions as a first-class feature of the language, and tries to insulate package users from having to compile C extensions. This means that distributions need to contain binary code compiled from the C extensions—such distributions (in their modern iteration) are called binary wheels. But C extensions usually need to be compiled for a specific target Python version and operating system, so to have any sort of wide support you need multiple wheels. Furthermore, since the package author can't anticipate all Python versions and operating systems (some of which don't exist yet!), it's also important to include a source distribution, which the package user is responsible for compiling.

### 1 - kubernetes autoscaling

On basis of load, more pods are launched in the scaling group. That's neat.

- https://learnk8s.io/blog/scaling-spring-boot-microservices/
- https://github.com/learnk8s/spring-boot-k8s-hpa
- https://classroom.udacity.com/courses/ud615
