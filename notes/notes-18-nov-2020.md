# 18-nov-2020


### 1 - strict modules concept

- High loading time can happen with large codebases due to the way python works
- lot of unpredictability when config and imports are done from another service
- concept of strict modules used by instagram to solve these problems in their python system

https://instagram-engineering.com/python-at-scale-strict-modules-c0bb9245c834

### 2 - disabling GC to improve performance

- Cpython code hacks to remove GC out of equation and getting more perf. memory out of the system
- "Try simple things first"
- COW happening at reads, weird if true
- "Prove your theory first"

https://instagram-engineering.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172
