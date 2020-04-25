# 25-apr-2020

### 3 - cgit for better exceptions

```python
import cgitb
cgitb.enable(format='text')

def func1(arg1):
    local_var = arg1 * 2
    return func2(local_var)

def func2(arg2):
    local_var = arg2 + 2
    return func3(local_var)

def func3(arg3):
    local_var = arg2 / 2
    return local_var

func1(1)
```


### 2 - writing a file context manager

```python
class ManagedFile:
  def __init__(self,name):
    self.name = name
  
  def __enter__(self):
    self.file = open(self.name, "w")
    return self.file
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    if self.file:
      self.file.close()

with ManagedFile("hello.txt") as f:
  f.write("hello world!")
```

### 1 - strings without commas

```python
my_str =( "asdasddadasd"
"assdasdasd"
"asdasfgdfgdfg")

print(my_str)
```
