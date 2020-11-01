# 01-nov-2020

### 19 - deepcopy oneliner

```python
deepcopy = lambda x: cPickle.loads(cPickle.dumps(x))
```

### 18 - oneliner factorial

```python
fac=lambda(n):reduce(int.__mul__,range(1,n+1),1)
```

### 17 - emulating switch

```python
def a():
  print "a"

def b():
  print "b"

def default():
   print "default"

({1:a, 2:b}.get(x, default))()
```

### 16 - logging only library

- https://www.geeksforgeeks.org/python-add-logging-to-python-libraries/?ref=rp

```python
import logging 
  
logging.basicConfig(level = logging.ERROR) 
  
import abc 
print (abc.func()) 
  
Change the logging level for 'abc' only 
logging.getLogger('abc').level = logging.DEBUG 
print (abc.func()) 
```

### 15 - convex hull - jarvis algo

- https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/

```python
class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def Left_index(points): 
      
    ''' 
    Finding the left most point 
    '''
    minn = 0
    for i in range(1,len(points)): 
        if points[i].x < points[minn].x: 
            minn = i 
        elif points[i].x == points[minn].x: 
            if points[i].y > points[minn].y: 
                minn = i 
    return minn 
  
def orientation(p, q, r): 
    ''' 
    To find orientation of ordered triplet (p, q, r).  
    The function returns following values  
    0 --> p, q and r are colinear  
    1 --> Clockwise  
    2 --> Counterclockwise  
    '''
    val = (q.y - p.y) * (r.x - q.x) - \ 
          (q.x - p.x) * (r.y - q.y) 
  
    if val == 0: 
        return 0
    elif val > 0: 
        return 1
    else: 
        return 2
  
def convexHull(points, n): 
      
    # There must be at least 3 points  
    if n < 3: 
        return
  
    # Find the leftmost point 
    l = Left_index(points) 
  
    hull = [] 
      
    ''' 
    Start from leftmost point, keep moving counterclockwise  
    until reach the start point again. This loop runs O(h)  
    times where h is number of points in result or output.  
    '''
    p = l 
    q = 0
    while(True): 
          
        # Add current point to result  
        hull.append(p) 
  
        ''' 
        Search for a point 'q' such that orientation(p, x,  
        q) is counterclockwise for all points 'x'. The idea  
        is to keep track of last visited most counterclock-  
        wise point in q. If any point 'i' is more counterclock-  
        wise than q, then update q.  
        '''
        q = (p + 1) % n 
  
        for i in range(n): 
              
            # If i is more counterclockwise  
            # than current q, then update q  
            if(orientation(points[p],  
                           points[i], points[q]) == 2): 
                q = i 
  
        ''' 
        Now q is the most counterclockwise with respect to p  
        Set p as q for next iteration, so that q is added to  
        result 'hull'  
        '''
        p = q 
  
        # While we don't come to first point 
        if(p == l): 
            break
  
    # Print Result  
    for each in hull: 
        print(points[each].x, points[each].y) 
  
# Driver Code 
points = [] 
points.append(Point(0, 3)) 
points.append(Point(2, 2)) 
points.append(Point(1, 1)) 
points.append(Point(2, 1)) 
points.append(Point(3, 0)) 
points.append(Point(0, 0)) 
points.append(Point(3, 3)) 
  
convexHull(points, len(points)) 
```

### 14 - breesenham line generator

https://github.com/devAmoghS/Python-Interview-Problems-for-Practice/blob/master/bresenham_line_algorithm.py

```python
def lineGenerator(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1

	slope = 2*dy - dx

	x = x1
	y = y1
	while x < x2:

		#Print current coordinates
		print(x, y)

		#X increases any ways
		x+= 1

		# 2dy is always added in the slope. Do it.
		slope += 2*dy
		#Check for the current slope
		if slope >= 0:
			y += 1
			slope -= 2 * (x2-x1)

		elif slope <=0:
			#No changes are made.
			slope = slope
```

### 13 - isnumeric 

https://github.com/devAmoghS/Python-Interview-Problems-for-Practice/blob/master/is_numeric.py

```python
# Given a string, return True if it
# is a numeric data type, False otherwise


def is_numeric(input_str):

    data_types = [
        int,
        float,
        complex,
        lambda T: int(T, 2),  # binary
        lambda T: int(T, 8),  # octal
        lambda T: int(T, 16),  # hex
    ]

    for dtype in data_types:
        try:
            dtype(input_str)
            return True
        except ValueError:
            pass
    return False


tests = [
    "0",
    "0.",
    "00",
    "123",
    "0123",
    "+123",
    "-123",
    "-123.",
    "-123e-4",
    "-.8E-04",
    "0.123",
    "(5)",
    "-123+4.5j",
    "0b0101",
    " +0B101 ",
    "0o123",
    "-0xABC",
    "0x1a1",
    "12.5%",
    "1/2",
    "½",
    "3¼",
    "π",
    "Ⅻ",
    "1,000,000",
    "1 000",
    "- 001.20e+02",
    "NaN",
    "inf",
    "-Infinity",
]

for s in tests:
    print(s, "---", is_numeric(s))
```

### 12 - karatsuba multiplication

https://github.com/devAmoghS/Python-Interview-Problems-for-Practice/blob/master/karatsuba.py

```python
import random
from math import ceil
from math import log10


def get_digits(n):
    if n > 0:
        digits = int(log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(log10(-n)) + 2
    return digits


def karatsuba(x, y):
    # the base case for recursion
    if x < 10 and y < 10:
        return x * y

    # n is the number of digits in the highest input number
    n = max(get_digits(x), get_digits(y))

    n_2 = int(ceil(n / 2.0))
    n = n if n % 2 == 0 else n + 1

    # split the input numbers
    a, b = divmod(x, 10 ** n_2)
    c, d = divmod(y, 10 ** n_2)

    # applying the recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    # performs the multiplication
    z2 = (10 ** n) * ac
    z1 = (10 ** n_2) * ad_bc
    z0 = bd
    return z2 + z1 + z0


def test():
    for i in range(1000):
        x = random.randint(1, 10 ** 5)
        y = random.randint(1, 10 ** 5)
        expected = x * y
        result = karatsuba(x, y)
        if result != expected:
            return print("failed")
    return print("ok")


if __name__ == "__main__":
    test()
```


### 11 - simple method overriding

```python
class A:
    def sayhello(self):
        print("Hello, I'm A")
class B(A):
    def sayhello(self):
        print("Hello, I'm B")
a=A()
b=B()
a.sayhello()
```

### 10 - always forget about namedtuples

https://github.com/learning-zone/python-interview-questions

```python
from collections import namedtuple
result=namedtuple('result','Physics Chemistry Maths') #format
Ramayan=result(Physics=86,Chemistry=95,Maths=86) #declaring the tuple
Ramayan.Chemistry
```

### 9 - useless titlecase check

```python
'Pro Development'.istitle()
```

### 8 - multithreading with thread subclassess

```python
import threading
class x (threading.Thread):
      def run(self):
         for p in range(1, 101):
              print(p)
class y (threading.Thread):
      def run(self):
           for q in range(1, 101):
              print(q)
x1=x()
y1=y()
x1.start()
y1.start()
```

### 7 - mysql with python

```python
#import MySQLdb module as : 
import MySQLdb

#establish a connection to the database.
db = MySQLdb.connect("host"="local host", "database-user"="user-name", "password"="password","database-name"="database")

#initialize the cursor variable upon the established connection: 
c1 = db.cursor()

#retrieve the information by defining a required query string.
s = "Select * from dept"

#fetch the data using fetch() methods and print it. 
data = c1.fetch(s)

#close the database connection. 
db.close()
```

### 6 - trivia


PYTHONSTARTUP − It contains the path of an initialization file containing Python source code. It is executed every time you start the interpreter. It is named as .pythonrc.py in Unix and it contains commands that load utilities or modify PYTHONPATH.

PYTHONCASEOK − It is used in Windows to instruct Python to find the first case-insensitive match in an import statement. Set this variable to any value to activate it.

PYTHONHOME − It is an alternative module search path. It is usually embedded in the PYTHONSTARTUP or PYTHONPATH directories to make switching module libraries easy.

PYTHONPATH − It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by the Python installer.

### 5 - what one liners should not be

```python
(lambda a,b:a if a>b else b)(3,3.5)
```

### 4 - capturing emails using regex

- regex is very clean thing, just like sql 

```
>>> import re
>>> e = re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','test@gmail.com')
>>> e
<_sre.SRE_Match object; span=(0, 22), match='test@gmail.com'>
>>>
```

### 3 - simple way to make variable mock

```python
>>> from unittest.mock import Mock
>>> mock = Mock()
>>> mock.side_effect = { "input1" : "output1" , "input2": "output2" }.get
>>> mock
<Mock id='4331355160'>
>>> mock("input1")
'output1'
>>>
```

also,

```python
def my_side_effect(*args, **kwargs):
    if args[0] == 42:
        return "Called with 42"
    elif args[0] == 43:
        return "Called with 43"
    elif kwargs['foo'] == 7:
        return "Foo is seven"

mockobj.mockmethod.side_effect = my_side_effect
```
or,

```python
m = MagicMock(side_effect=(lambda x: x+1))
```

### 2 - python shaped by leaky abstractions

- nice talk to dig into and understand how decisions took initially have now chained python interpreter

https://www.youtube.com/watch?v=qCGofLIzX6g

### 1 - lsm-db transactions

- https://charlesleifer.com/blog/using-sqlite4-s-lsm-storage-engine-as-a-stand-alone-nosql-database-with-python/

```bash
>>> with db.transaction() as txn:
...     db['k1'] = '1-mod'
...     with db.transaction() as txn2:
...         db['k2'] = '2-mod'
...         txn2.rollback()
...
True
>>> print db['k1'], db['k2']
1-mod 2
```

```bash
>>> with db.transaction() as txn:
...    db['k1'] = 'outer txn'
...    txn.commit()  # The write is preserved.
...
...    db['k1'] = 'outer txn-2'
...    with db.transaction() as txn2:
...        db['k1'] = 'inner-txn'  # This is commited after the block ends.
...    print db['k1']  # Prints "inner-txn".
...    txn.rollback()  # Rolls back both the changes from txn2 and the preceding write.
...    print db['k1']
...
1              <- Return value from call to commit().
inner-txn      <- Printed after end of txn2.
True           <- Return value of call to rollback().
outer txn      <- Printed after rollback.
```

```
>> db.begin()
>>> db['foo'] = 'baze'
>>> print db['foo']
baze
>>> db.rollback()
True
>>> print db['foo']
bar
```
