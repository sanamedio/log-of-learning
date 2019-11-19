# 03-oct-2018

### 27 - try except else finally

```python
try:
    print("try something here")
except:
    print("this happens only if it fails")
else:
    print("this happens only if it succeeds")
finally:
    print("this happens no matter what")

try something here
this happens only if it succeeds
this happens no matter what
```

### 26 - Custom exceptions
```python
class MySpecialError(ValueError):
    pass

raise MySpecialError("here's the message")
```

```python
try:
    print("do something")
    raise MySpecialError("[informative error message here]")
except MySpecialError:
    print("do something else")
```

### 25 - Accessing Exception 

```python
try:
    x = 1 / 0
except ZeroDivisionError as err:
    print("Error class is:  ", type(err))
    print("Error message is:", err)
```

### 24 - Raising errors

```python
raise RuntimeError("my error message")
```

```python
def fibonacci(N):
    if N < 0:
        raise ValueError("N must be non-negative")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

fibonacci(-10)
```

### 23 - try except

```python
try:
    print("let's try something:")
    x = 1 / 0 # ZeroDivisionError
except:
    print("something bad happened!")
```

```python
def safe_divide(a, b):
    try:
        return a / b
    except:
        return 1E100
```

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 1E100
```

### 22 - types of errors

* Syntax errors: Errors where the code is not valid Python (generally easy to fix)
* Runtime errors: Errors where syntactically valid code fails to execute, perhaps due to invalid user input (sometimes easy to fix)
* Semantic errors: Errors in logic: code executes without a problem, but the result is not what you expect (often very difficult to track-down and fix)

### 21 - lambda

```python
add = lambda x, y: x + y
add(1, 2)
```

```python
sorted(data, key=lambda item: item['first'])
```

### 20 - data types and built-in data structures


| Type |  Example |  Description |
|-------|----------|------------------|
| int  |	x = 1 	|   integers (i.e., whole numbers)|
| float| 	x = 1.0 |	floating-point numbers (i.e., real numbers)|
| complex | 	x = 1 + 2j |	Complex numbers (i.e., numbers with real and imaginary part)|
| bool |	x = True |	Boolean: True/False values|
| str |	x = 'abc' |	String: characters or text|
| NoneType |	x = None |	Special object indicating nulls|

| Type Name| 	Example | 	Description|
|----------|------------|--------------|
|list |	[1, 2, 3] |	Ordered collection|
| tuple  |	(1, 2, 3) |	Immutable ordered collection| 
| dict | 	{'a':1, 'b':2, 'c':3} |	Unordered (key,value) mapping |
| set | 	{1, 2, 3} |	Unordered collection of unique values |


### 19 - set algebra

```python
primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}

# union: items appearing in either
primes | odds      # with an operator
primes.union(odds) # equivalently with a method

# intersection: items appearing in both
primes & odds             # with an operator
primes.intersection(odds) # equivalently with a method

# difference: items in primes but not in odds
primes - odds           # with an operator
primes.difference(odds) # equivalently with a method

# symmetric difference: items appearing in only one set
primes ^ odds                     # with an operator
primes.symmetric_difference(odds) # equivalently with a method
```

### 18 - as integer ratio

```python
x = 0.125
x.as_integer_ratio()
```

```python
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)
```

### 17 - list appending in python

list in python is a variable length array which automatically resizes on appending if needed and give a linear time overall.

```python
def f(n):
    l = []
    for i in range(n):
        l.append(i)
    l.reverse()
    return l

# this is very slow compared to the one above
def g(n):
    l = []
    for i in range(n):
        l.insert(0, i)
    return l
```

### 16 - zip( \*iterable )

```python
>>> a=[[1,2,3],[4,5,6]]
>>> zip(*a)
    [(1, 4), (2, 5), (3, 6)]

>>> d={"a":1,"b":2,"c":3}
>>> zip(*d.iteritems())
[('a', 'c', 'b'), (1, 3, 2)]
```

### 15 - 2d array correct initialization

```python
lst_2d = [[0] * 3 for i in xrange(3)]
# lst_2d = [[0]*3]*3 is WRONG
```

### 14 - string <> datetime

```python
from datetime import datetime

date_obj = datetime.strptime('May 29 2015  2:45PM', '%B %d %Y %I:%M%p')

date_string = date_obj.strftime('%B %d %Y %I:%M%p')
```

### 13 - parallel iteration in two collections

```python
a = [1, 2, 3]
b = [4, 5, 6]
for (a_val, b_val) in zip(a, b):
    print(a_val, b_val)
```

### 12 - variable/attr exist  ?

```python
if 'myVar' in locals():
    # myVar exists.
```
```python
if 'myVar' in globals():
    # myVar exists.
```
```python
if hasattr(obj, 'attr_name'):
    # obj.attr_name exists.
```

### 11 - Index for loop

```python
for idx, val in enumerate(ints):
    print idx, val
```

### 10 - Datetime
```python
import datetime

now = datetime.datetime.now()

print
print "Current date and time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

print
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")
```

### 9 - inspect to get call stack

```python
import inspect  # gives us access to the stack
from datetime import datetime

LOG = True  # set to False to suppress output

def log(message):
    if LOG:
    	n = datetime.utcnow()
    	f = inspect.stack()[1][3]
        print("{} - {}: {}".format(n, f, message))
```

### 8 - Tree

```python
from collections import defaultdict
def Tree():
  return defaultdict(Tree)

fs = Tree()
fs['a']['b']['c']['d']='wtf'
```

### 7 - versions 

```python
>>> from distutils.version import StrictVersion
>>> versions = ['1.3.12', '1.3.3', '1.2.5', '1.2.15', '1.2.3', '1.2.1']
>>> versions.sort(key=StrictVersion)
>>> print versions
['1.2.1', '1.2.3', '1.2.5', '1.2.15', '1.3.3', '1.3.12']
```

```python
>> l = ['v1.3.12', 'v1.3.3', 'v1.2.5', 'v1.2.15', 'v1.2.3', 'v1.2.1']
>>> l.sort(key=LooseVersion)
>>> l
['v1.2.1', 'v1.2.3', 'v1.2.5', 'v1.2.15', 'v1.3.3', 'v1.3.12']
```

### 6 - Python HTTP and SMTP servers

```bash
 python3 -m http.server
 ```
 ```bash
 python -m SimpleHTTPServer
 ```
 ```bash
 python -m smtpd -c DebuggingServer -n
 ```

### 5 - Removes duplicates while maintaining order

```python
from collections import OrderedDict
x = [1, 8, 4, 5, 5, 5, 8, 1, 8]
list(OrderedDict.fromkeys(x))
```

### 4 - itertools groupby

```python
from itertools import groupby

data = [
    {'animal': 'dog', 'name': 'Roxie', 'age': 5},
    {'animal': 'dog', 'name': 'Zeus', 'age': 6},
    {'animal': 'dog', 'name': 'Spike', 'age': 9},
    {'animal': 'dog', 'name': 'Scooby', 'age': 7},
    {'animal': 'cat', 'name': 'Fluffy', 'age': 3},
    {'animal': 'cat', 'name': 'Oreo', 'age': 5},
    {'animal': 'cat', 'name': 'Bella', 'age': 4}   
    ]

for key, group in groupby(data, lambda x: x['animal']):
    for thing in group:
        print(thing['name'] + " is a " + key)
```

### 3 - pprint

```python
import pprint as pp
animals = [{'animal': 'dog', 'legs': 4, 'breeds': ['Border Collie', 'Pit Bull', 'Huskie']}, {'animal': 'cat', 'legs': 4, 'breeds': ['Siamese', 'Persian', 'Sphynx']}]
pp.pprint(animals, width=1)
```

### 2 - Calling external command in python

```python
import subprocess
subprocess.call(['mkdir', 'empty_folder'])
```
```python
import subprocess
output = subprocess.check_output(['ls', '-l'])
```
```python
import subprocess
output = subprocess.call(['cd', '/'], shell=True)
```

### 1 - Flask simple app

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there!"
if __name__ == '__main__':
    app.run(debug=True)
```





