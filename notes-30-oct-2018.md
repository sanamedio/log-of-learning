# 30-oct-2018

### 1 - Checking if a object is iterable

```python
def iterable(obj):
     try:
         iter(obj)
         return True
     except TypeError:
         return False 
```

can check it over a simple class like this:

```python
class Reverse:
    """
    Creates Iterators for looping over a sequence backwards.
    """
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
