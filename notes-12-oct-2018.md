# notes-12-oct-2018

### 14 - actual print

```python 
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
```

### 13 - dictionary from list and tuple

```python
>>> dict([[1,2],[3,4]])
{1: 2, 3: 4}
>>> dict([(3,26),(4,44)])
{3: 26, 4: 44}
```

### 12 - nonlocal in python 3

```python
>>> def outside():
        msg = "Outside!"
        def inside():
            nonlocal msg
            msg = "Inside!"
            print(msg)
        inside()
        print(msg)

>>> outside()
Inside!
Inside!
```

### 11 - loops implementation

```python
for element in iterable:
    # do something with element
```
is actually
```python
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```


### 10 - operator overloading

```python
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag
```

### 9 - issubclass

```python
# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))
```

### 8 - Inheritence

```python
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

```

### 7 - Constructors

```python
class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)
```

### 6 - docstring

```python
class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)
```

### 5 - __new__ vs __init__

- https://stackoverflow.com/questions/4859129/python-and-python-c-api-new-versus-init

### 4 - C3 Linearization for Multiple Interitance

- https://en.wikipedia.org/wiki/C3_linearization
- Class.mro() 
- Class.\__mro__

### 3 - WSGI

- Web Server Gateway Interface
- Set of specs in Python to standardize interaction between Webserver and Web APP framework.

### 2 - built-in help

```python
help(object)
dir(object)
type(object)
#object? ipython
```

### 1 - Celery

- https://tests4geeks.com/python-celery-rabbitmq-tutorial/
- https://www.agiliq.com/blog/2015/07/getting-started-with-celery-and-redis/
- https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps
- Can work with redis, RabbitMQ and other brokers as well as databases


