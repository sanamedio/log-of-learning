# 01-nov-2020

### 35 - alwaays forget about interact

- during pdb session, to have a full fleged python env just have to type interact

https://www.youtube.com/watch?v=5AYIe-3cD-s&ab_channel=PyCon2020

### 34 - capping x

```python
x = sorted([0.0, x, 1.0])[1]
```

### 33 - qsort one-liner

```python
qsort = lambda l : l if len(l)<=1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]]) 
qsort([1,2,5,7,8,2,6,8]) 
```

### 32 - codegolf005

lookup tables for boolean can be saved as a simple number

https://codegolf.stackexchange.com/a/41742/70636

### 31 - codegolf004

```python
a=lambda b:lambda c:lambda d:lambda e:lambda f:0   # 48 bytes  (plain)
exec"a=`b:`c:`d:`e:`f:0".replace('`','lambda ')    # 47 bytes  (replace)
exec"a=%sb:%sc:%sd:%se:%sf:0"%(('lambda ',)*5)     # 46 bytes  (%)
```

### 30 - codegolf003

```python
r=range
for x in r(10):
 for y in r(100):print x,y
```

### 29 - codegolf002

if a<b:return a
else:return b

can be written as(though not exact same)

return(b,a)[a<b]

### 28 - codegolf001

https://codegolf.stackexchange.com/questions/54/tips-for-golfing-in-python

Use a=b=c=0 instead of a,b,c=0,0,0.

Use a,b,c='123' instead of a,b,c='1','2','3'.


### 27 - heirarchical state machine pattern

https://milovantomasevic.com/courses/python-design-patterns-hsm/

```python
"""
Implementation of the HSM (hierarchical state machine) or
NFSM (nested finite state machine) C++ example from
http://www.eventhelix.com/RealtimeMantra/HierarchicalStateMachine.htm#.VwqLVEL950w
in Python

- single source 'message type' for state transition changes
- message type considered, messages (comment) not considered to avoid complexity
"""


class UnsupportedMessageType(BaseException):
    pass


class UnsupportedState(BaseException):
    pass


class UnsupportedTransition(BaseException):
    pass


class HierachicalStateMachine:
    def __init__(self):
        self._active_state = Active(self)  # Unit.Inservice.Active()
        self._standby_state = Standby(self)  # Unit.Inservice.Standby()
        self._suspect_state = Suspect(self)  # Unit.OutOfService.Suspect()
        self._failed_state = Failed(self)  # Unit.OutOfService.Failed()
        self._current_state = self._standby_state
        self.states = {
            "active": self._active_state,
            "standby": self._standby_state,
            "suspect": self._suspect_state,
            "failed": self._failed_state,
        }
        self.message_types = {
            "fault trigger": self._current_state.on_fault_trigger,
            "switchover": self._current_state.on_switchover,
            "diagnostics passed": self._current_state.on_diagnostics_passed,
            "diagnostics failed": self._current_state.on_diagnostics_failed,
            "operator inservice": self._current_state.on_operator_inservice,
        }

    def _next_state(self, state):
        try:
            self._current_state = self.states[state]
        except KeyError:
            raise UnsupportedState

    def _send_diagnostics_request(self):
        return "send diagnostic request"

    def _raise_alarm(self):
        return "raise alarm"

    def _clear_alarm(self):
        return "clear alarm"

    def _perform_switchover(self):
        return "perform switchover"

    def _send_switchover_response(self):
        return "send switchover response"

    def _send_operator_inservice_response(self):
        return "send operator inservice response"

    def _send_diagnostics_failure_report(self):
        return "send diagnostics failure report"

    def _send_diagnostics_pass_report(self):
        return "send diagnostics pass report"

    def _abort_diagnostics(self):
        return "abort diagnostics"

    def _check_mate_status(self):
        return "check mate status"

    def on_message(self, message_type):  # message ignored
        if message_type in self.message_types.keys():
            self.message_types[message_type]()
        else:
            raise UnsupportedMessageType


class Unit:
    def __init__(self, HierachicalStateMachine):
        self.hsm = HierachicalStateMachine

    def on_switchover(self):
        raise UnsupportedTransition

    def on_fault_trigger(self):
        raise UnsupportedTransition

    def on_diagnostics_failed(self):
        raise UnsupportedTransition

    def on_diagnostics_passed(self):
        raise UnsupportedTransition

    def on_operator_inservice(self):
        raise UnsupportedTransition


class Inservice(Unit):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_fault_trigger(self):
        self._hsm._next_state("suspect")
        self._hsm._send_diagnostics_request()
        self._hsm._raise_alarm()

    def on_switchover(self):
        self._hsm._perform_switchover()
        self._hsm._check_mate_status()
        self._hsm._send_switchover_response()


class Active(Inservice):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_fault_trigger(self):
        super().perform_switchover()
        super().on_fault_trigger()

    def on_switchover(self):
        self._hsm.on_switchover()  # message ignored
        self._hsm.next_state("standby")


class Standby(Inservice):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_switchover(self):
        super().on_switchover()  # message ignored
        self._hsm._next_state("active")


class OutOfService(Unit):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_operator_inservice(self):
        self._hsm.on_switchover()  # message ignored
        self._hsm.send_operator_inservice_response()
        self._hsm.next_state("suspect")


class Suspect(OutOfService):
    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine

    def on_diagnostics_failed(self):
        super().send_diagnostics_failure_report()
        super().next_state("failed")

    def on_diagnostics_passed(self):
        super().send_diagnostics_pass_report()
        super().clear_alarm()  # loss of redundancy alarm
        super().next_state("standby")

    def on_operator_inservice(self):
        super().abort_diagnostics()
        super().on_operator_inservice()  # message ignored


class Failed(OutOfService):
    """No need to override any method."""

    def __init__(self, HierachicalStateMachine):
        self._hsm = HierachicalStateMachine
```

### 26 - blackboard pattern

https://github.com/faif/python-patterns/blob/master/patterns/other/blackboard.py

```python
"""
@author: Eugene Duboviy <eugene.dubovoy@gmail.com> | github.com/duboviy

In Blackboard pattern several specialised sub-systems (knowledge sources)
assemble their knowledge to build a possibly partial or approximate solution.
In this way, the sub-systems work together to solve the problem,
where the solution is the sum of its parts.

https://en.wikipedia.org/wiki/Blackboard_system
"""

import abc
import random


class Blackboard:
    def __init__(self):
        self.experts = []
        self.common_state = {
            "problems": 0,
            "suggestions": 0,
            "contributions": [],
            "progress": 0,  # percentage, if 100 -> task is finished
        }

    def add_expert(self, expert):
        self.experts.append(expert)


class Controller:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def run_loop(self):
        while self.blackboard.common_state["progress"] < 100:
            for expert in self.blackboard.experts:
                if expert.is_eager_to_contribute:
                    expert.contribute()
        return self.blackboard.common_state["contributions"]


class AbstractExpert(metaclass=abc.ABCMeta):
    def __init__(self, blackboard):
        self.blackboard = blackboard

    @property
    @abc.abstractmethod
    def is_eager_to_contribute(self):
        raise NotImplementedError("Must provide implementation in subclass.")

    @abc.abstractmethod
    def contribute(self):
        raise NotImplementedError("Must provide implementation in subclass.")


class Student(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return True

    def contribute(self):
        self.blackboard.common_state["problems"] += random.randint(1, 10)
        self.blackboard.common_state["suggestions"] += random.randint(1, 10)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(1, 2)


class Scientist(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state["problems"] += random.randint(10, 20)
        self.blackboard.common_state["suggestions"] += random.randint(10, 20)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(10, 30)


class Professor(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return True if self.blackboard.common_state["problems"] > 100 else False

    def contribute(self):
        self.blackboard.common_state["problems"] += random.randint(1, 2)
        self.blackboard.common_state["suggestions"] += random.randint(10, 20)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(10, 100)


def main():
    """
    >>> blackboard = Blackboard()
    >>> blackboard.add_expert(Student(blackboard))
    >>> blackboard.add_expert(Scientist(blackboard))
    >>> blackboard.add_expert(Professor(blackboard))

    >>> c = Controller(blackboard)
    >>> contributions = c.run_loop()

    >>> from pprint import pprint
    >>> pprint(contributions)
    ['Student',
     'Student',
     'Student',
     'Student',
     'Scientist',
     'Student',
     'Student',
     'Student',
     'Scientist',
     'Student',
     'Scientist',
     'Student',
     'Student',
     'Scientist',
     'Professor']
    """


if __name__ == "__main__":
    random.seed(1234)  # for deterministic doctest outputs
    import doctest

    doctest.testmod()
```


### 25 - memento pattern

https://raw.githubusercontent.com/faif/python-patterns/master/patterns/behavioral/memento.py

```python
"""
http://code.activestate.com/recipes/413838-memento-closure/

*TL;DR
Provides the ability to restore an object to its previous state.
"""

from copy import copy, deepcopy


def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:
    """A transaction guard.

    This is, in fact, just syntactic sugar around a memento closure.
    """

    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()


class Transactional:
    """Adds transactional semantics to methods. Methods decorated  with

    @Transactional will rollback to entry-state upon exceptions.
    """

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transaction


class NumObj:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "<%s: %r>" % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = "1111"  # <- invalid value
        self.increment()  # <- will fail and rollback


def main():
    """
    >>> num_obj = NumObj(-1)
    >>> print(num_obj)
    <NumObj: -1>

    >>> a_transaction = Transaction(True, num_obj)

    >>> try:
    ...    for i in range(3):
    ...        num_obj.increment()
    ...        print(num_obj)
    ...    a_transaction.commit()
    ...    print('-- committed')
    ...    for i in range(3):
    ...        num_obj.increment()
    ...        print(num_obj)
    ...    num_obj.value += 'x'  # will fail
    ...    print(num_obj)
    ... except Exception:
    ...    a_transaction.rollback()
    ...    print('-- rolled back')
    <NumObj: 0>
    <NumObj: 1>
    <NumObj: 2>
    -- committed
    <NumObj: 3>
    <NumObj: 4>
    <NumObj: 5>
    -- rolled back

    >>> print(num_obj)
    <NumObj: 2>

    >>> print('-- now doing stuff ...')
    -- now doing stuff ...

    >>> try:
    ...    num_obj.do_stuff()
    ... except Exception:
    ...    print('-> doing stuff failed!')
    ...    import sys
    ...    import traceback
    ...    traceback.print_exc(file=sys.stdout)
    -> doing stuff failed!
    Traceback (most recent call last):
    ...
    TypeError: ...str...int...

    >>> print(num_obj)
    <NumObj: 2>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
```


### 24 - borg pattern

- shouldn't this be a anti-pattern?
https://github.com/faif/python-patterns/blob/master/patterns/creational/borg.py

### 23 - unittest samples from popular projects

```
https://github.com/django/django/blob/master/tests/admin_filters/tests.py
https://github.com/pallets/flask/blob/master/tests/test_cli.py
https://github.com/httpie/httpie/blob/master/tests/test_binary.py
https://github.com/psf/requests/blob/master/tests/test_hooks.py
https://github.com/numpy/numpy/blob/master/numpy/core/tests/test_datetime.py
https://github.com/celery/celery/blob/master/t/unit/security/test_certificate.py
```

The code structure in numpy is nice, having tests follow the same heirarchical structure in repo as the source tree.

### 22 - hashing binary as decimal

```python
if __name__ == '__main__':

	M = [
		[0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0]
	]

	s = set()

	# do for each row i
	for i in range(len(M)):
		decimal = 0

		# convert binary row i into its decimal equivalent
		for j in range(len(M[i])):
			decimal += M[i][j] * pow(2, j)

		# if decimal value is seen before
		if decimal in s:
			print("Duplicate row found : Row", (i + 1))
		else:
			s.add(decimal)
```

### 21 - duplicate finding using trie

- generally hash table only comes into mind, but trie also a good option

```python
# A class representing a node:
class Trie:
	# Constructor
	def __init__(self):

		self.character = [None] * 2

		# set when node is a leaf node
		self.isLeaf = False


# Iterative function to insert list in Trie.
def insert(head, A):

	# start from root node
	curr = head

	for i in A:
		# create a node if path doesn't exists
		if curr.character[i] is None:
			curr.character[i] = Trie()

		# go to next node
		curr = curr.character[i]

	# if row is inserted before, return false
	if curr.isLeaf:
		return False

	# mark leaf node and return True
	curr.isLeaf = True
	return True


if __name__ == '__main__':

	mat = [
		[1, 0, 0, 1, 0],
		[0, 1, 1, 0, 0],
		[1, 0, 0, 1, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0]
	]

	# insert all rows of into trie
	head = Trie()
	for i, e in enumerate(mat):
		if not insert(head, e):
			print(f"Duplicate row found: Row #{i+1}")

```

### 20 - word break dp

```python
class Solution(object):
   def wordBreak(self, s, wordDict):
      dp = [[False for i in range(len(s))] for x in range(len(s))]
      for i in range(1,len(s)+1):
         for j in range(len(s)-i+1):
            #print(s[j:j+i])
            if s[j:j+i] in wordDict:
               dp[j][j+i-1] = True
            else:
               for k in range(j+1,j+i):
                  if dp[j][k-1] and dp[k][j+i-1]:
                     dp[j][j+i-1]= True
      return dp[0][len(s) - 1]
ob1 = Solution()
print(ob1.wordBreak("applepenapple", ["apple", "pen"]))
```

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
