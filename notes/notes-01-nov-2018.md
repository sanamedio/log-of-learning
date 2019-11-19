# 01-nov-2018

### 7 - return from dunder init antipattern

```python
class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.area = width * height
		#causes "should return None erro"
		return self.area




#### correct way 

class Rectangle:
		
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self._area = width * height

	@property
	def area(self):
		return self._area


```


### 6 - with exit semantics antipattern

incorrect dunder exit:
```python
class Rectangle:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __enter__(self):
		print("in __enter__")
		return self

	def __exit__(self):
		#never called from 'with' because
		# semantics are wrong

	def divide_by_zero(self):
		return self.width / 0

with Rectangle(3,4) ass r:
	r.divide_by_zero()
	# __exit__ should be called but isn't
```

correct dunder exit:
```python
class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __enter__(self):
		print("in __enter__")
		return self

	def __exit__(self, exception_type, exception_value, traceback):
		print("in __exit__")

	def divide_by_zero(self):
		# causes ZeroDivisionError exception
		return self.width / 0 

with Rectangle(3,4) as r:
	# exception successfully pass to __exit__
	r.divide_by_zero()
```




### 5 - with behind the scenes

```python
with EXPRESSION:
        BLOCK
```
is equivalent to:
```python
EXPRESSION.__enter__()
try:
        BLOCK
finally:
        EXPRESSION.__exit__(exception_type, exception_value, traceback)
```

### 4 - unintended for else

```python

def magic_number(lst, x):
        for i in lst:
                if x == i:
                        print("magic number appeared")
        else:
                print("List does not contain magic number"

```

- The problem here is that without breaking the first if , it will print both prints, hence a break needs to be put in the first if

### 3- bad super call antipattern

```python
class Rectangle:
        def __init__(self, height, width):
                self.height = height
                self.width = width
                self.area = height * width

class Square(Rectangle):
        def __init__(self,length):
                super(self, Square).__init__(length,length)

s = Square(5)
print(s.area)
```

 - In python2 call to super, first argument is the class name itself, and not self
 - In python3 no need to put any arguments to super






### 2 - Antipatterns in python

- Accessing private variabls directly from outside
```python
def Rectangle:

        def __init__(self, height, weight):
                self._height = height
                self._weight = weight


r = Rectangle(5,6)
print(r._width)
```

- Assigning lambda expression to a variable
```python
def f(x): return 2+x

f = lamda x: 2+x 
```

- Assigning a built in module 
```python
list = [1,2,3] # list() is a builtin, pllease dont mess that up xce
```
- Catching exceptions in the right order

wrong:
```python
try:
  5/0
except Exception as e:
  print("Exception")
except ZeroDivisionError as e:
  print("ZeroDivisionError")
```
right:
```python
try:
  5/0
except ZeroDivisionError as e:
  print("ZeroDivisionErro")
except Exception as e:
  print("Eception")
```


### 1 - Django tutorial

- https://docs.djangoproject.com/en/2.1/intro/tutorial01  
- Key Points
  - You write your classes, containing fields with defined types
  - Django converts them to SQL tables and does the sync thing  ( by default it uses sqlite, but there is a MongoDB version out there too)
  - views are written in a template language with DSL embeeded for if and for loops ( quite similar to Meteor in this )
  - Admin panel is provided beforehand
  - There was no client side discussion in tutorial. I am assuming to provide rich interface, JS needs to get invovled. May be some different frontend framework than it's using by default.
  - There was no dynamic reactivity in the tutorial. Request stuff- Response stuff: server side rendering.
  - Good for quick development of simple Apps
- Files(default)
  - urls.py: Contains the routing and stuff, multiple present in the project
  - from urls.py(not literally) it goes to views.py which contains views which refer to templates
  - while rendering template or doing other stuff, models.py models are updated,queried
  - manage.py is control center during development, can be used to runserver and get shell directly into application and running tests
