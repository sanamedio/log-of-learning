# 02-nov-2018

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
