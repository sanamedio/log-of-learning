# 02-nov-2018

### 5 - Copying data from numpy to ctypes

```python
import numpy as np
import ctypes


# Preparing example

class TransferData(ctypes.Structure):
    _fields_ = [
        ('statusReady', ctypes.c_bool),
        ('velocity', ctypes.c_double * 4),
        ('pressure', ctypes.c_double * 4)
    ]


data = TransferData()
output = np.array([12., 13., 11., 10.])


# Actual code

# Both values should be equal but there could be problems with alignment settings
assert ctypes.sizeof(data.pressure) == output.nbytes

ctypes.memmove(ctypes.byref(data.pressure), output.ctypes.data, output.nbytes)


print(list(data.pressure))
```

### 4 - How to design a class

- https://stackoverflow.com/questions/4203163/how-do-i-design-a-class-in-python?noredirect=1&lq=1


### 3 - staticmethods and classmethods (cls variable)

- PEP8
  - Always use self for the first argument to instance methods.
  - Always use cls for the first argument to class methods.

```python
class Rectangle:
  def __init__(self,height,width):
    self.height = height
    self.width = width
    
  @staticmethod
  def area(height,width):
    return width * height
    
  @classmethod
  def print_class_name(cls):
    print("classname: {0}".format(cls))
```

### 2 - method could be a function

```python
class Rectangle:
  def __init__(self,height, width):
    self.height = height
    self.width = width
    self.area = width * height
  
  def area(height,width):
    return height*width
```

- This doesn't work and raises exception, prioritizing area not area(), why no overloading ? How to call area() now

### 1 - misplaced future

```python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print(8/7)
1
>>> from __future__ import division
>>> print(8/7)
1.14285714286
```
