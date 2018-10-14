# 15-oct-2018

### 2 - Context With

```python
class ManagedFile:
  def __init__(self,name):
    self.name= name
  
  def __enter__(self):
    self.file = open(self.name,"w")
    return self.file
    
  def __exit__(self,exc_type, exc_val , exc_tb):
    if self.file:
      self.file.close()

with ManagedFile('hello.txt') as f:
  f.write('hello world')
  f.write('bye now')
```


### 1 - assertions

- Assertions can be disabled globally, so don't use them for any real validations
- Assertions are good way to handle the remaining if-elif-else condition
- Assertions are to check internal consistencies, and cannot be handled
- assert <assert condition>
