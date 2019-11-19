# 08-nov-2018

### 15 - RingBuffer

```python
class RingBuffer:

    def __init__(self, size):
        self.data = [ None for x in range(size)]
        self.size = size

    
    def get_content(self):
        return self.data

    def append(self, x):
        self.data.pop(0) #pop from 0th position
        self.data.append(x) #push at the end
        return True

rb = RingBuffer(4)

for i in range(10):
    rb.append(i)
    print(rb.get_content())
```

### 14 - Easier to Ask for Forgiveness than Permission ( EAFP style )

- Pythonic programming style that determines an object's type by inspection of its method or attribute signature rather than by explicit relationship to some type object 
- "If it looks like a duck and quacks like a duck, it must be a duck."
- By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitution. 
- Duck-typing avoids tests using type() or isinstance(). 
- Instead, it typically employs the ```EAFP (Easier to Ask Forgiveness than Permission)``` style of programming.

```python
try:
   _ = (e for e in my_object)
except TypeError:
   print my_object, 'is not iterable'
```

- from this https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable


### 13 - checking if object is iterable

```python
In [8]: def test(func): 
   ...:     try: 
   ...:         iter(func) 
   ...:     except TypeError as te: 
   ...:         print( func, ' is not iterable') 
   ...:         return False 
   ...:     return True 
   ...:                                                                   

In [9]: test([])                                                          
Out[9]: True

In [10]: test('a')                                                        
Out[10]: True

In [11]: test(123)                                                        
123  is not iterable
Out[11]: False
```

```python
In [20]: isinstance([], collections.Iterable)                             
Out[20]: True

In [21]: isinstance('aasd', collections.Iterable)                         
Out[21]: True

In [22]: isinstance(12345, collections.Iterable)                          
Out[22]: False
```




### 12 - itertools product

```python
In [1]: import itertools                                                  

In [2]: from pprint import pprint                                         

In [3]: inputdata = [ 
   ...:     [ 'a','b', 'c' ] 
   ...:     , 
   ...:     ['d'] 
   ...:     , 
   ...:     ['e','f'], 
   ...:     ]                                                             

In [4]: *inputdata                                                        
  File "<ipython-input-4-826bef7464dd>", line 1
    *inputdata
              ^
SyntaxError: can't use starred expression here


In [5]: (*inputdata)                                                      
  File "<ipython-input-5-90123e56c144>", line 1
    (*inputdata)
    ^
SyntaxError: can't use starred expression here


In [6]: itertools.product(*inputdata)                                     
Out[6]: <itertools.product at 0x7fe7e2d4ba20>

In [7]: list(itertools.product(*inputdata))                               
Out[7]: 
[('a', 'd', 'e'),
 ('a', 'd', 'f'),
 ('b', 'd', 'e'),
 ('b', 'd', 'f'),
 ('c', 'd', 'e'),
 ('c', 'd', 'f')]

In [8]: pprint( list( itertools.product(*inputdata)))                     
[('a', 'd', 'e'),
 ('a', 'd', 'f'),
 ('b', 'd', 'e'),
 ('b', 'd', 'f'),
 ('c', 'd', 'e'),
 ('c', 'd', 'f')]
```


### 11 - IPython start from python -c

```bash
$ python3 -c "import IPython; IPython.embed()"
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]:  
```

### 10 - Timeout function as a decorator

```python
import signal

class TimeoutError(Exception):
    def __init__(self, value = "Timed Out"):
        self.value = value
    def __str__(self):
        return repr(self.value) #repr returns the __repr__ of that datatype, for strings it's the content




#decorator
def timeout(seconds_before_timeout):
    def decorate(f):
        def handler(signum, frame):
            raise TimeoutError()

        def new_f(*args , **kwargs):
            old = signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds_before_timeout)

            try:
                result = f(*args, **kwargs)
            finally:
                signal.signal(signal.SIGALRM, old)
                signal.alarm(0) #cancels the alarm , this is intentionally inside your finally block
            return result 

        new_f.__name__ = f.__name__ # sorts out that naming problem in trace

        return new_f
    return decorate


import time

@timeout(5)
def mytest():
    print ("Start")
    for i in range(1,10):
        time.sleep(1)
        print("{} seconds have passed".format(i))

if __name__ == '__main__':
    mytest()


```



```
python timeout_deco.py 
Start
1 seconds have passed
2 seconds have passed
3 seconds have passed
4 seconds have passed
Traceback (most recent call last):
  File "timeout_deco.py", line 45, in <module>
    mytest()
    └ <function timeout.<locals>.decorate.<locals>.new_f at 0x7f472b316ae8>
  File "timeout_deco.py", line 23, in new_f
    result = f(*args, **kwargs)
             │  │       └ {}
             │  └ ()
             └ <function mytest at 0x7f472b3169d8>
  File "timeout_deco.py", line 41, in mytest
    time.sleep(1)
    └ <module 'time' (built-in)>
  File "timeout_deco.py", line 16, in handler
    raise TimeoutError()
          └ <class '__main__.TimeoutError'>
TimeoutError: 'Timed Out'
```


### 9 - Timeout a function using SIGALRM

- One important fact to note when using signal module is that it doesn’t work well in a multi-threaded flow. The callback has to be registered in main thread, and the alarm will also be received by the main thread. (from http://chamilad.github.io/blog/2015/11/26/timing-out-of-long-running-methods-in-python/ )

```python
import signal


# signal.alarm can raise SIGALRM after t seconds and that's used here

class TimeoutFunctionException(Exception):
    pass


class TimeoutFunction:

    def __init__(self, function, timeout):
        self.timeout = timeout
        self.function = function


    def handle_timeout(self, signum, frame):
        raise TimeoutFunctionException()



    def __call__(self, *args):
        old = signal.signal(signal.SIGALRM, self.handle_timeout) # setting signal handler as handle_timeout function of SIGALRM, and saving the old signal handler into old varialbe
        signal.alarm( self.timeout)

        try:
            result = self.function(*args) # calling the function and saving result but why not **kwargs, i think those are also needed
        finally:
            signal.signal(signal.SIGALRM, old) # finally reset the old signal handler
        signal.alarm(0) #this probably should be inside finally block, it cancels the alarm in case of function gets an exception
        return result # return result




if __name__ == '__main__':

    import sys
    stdin_read = TimeoutFunction(sys.stdin.readline, 1 ) # 1 second timeout
    try:
        line = stdin_read()
    except TimeoutFunctionException:
        print( "Too slow!!")
    else:
        print("You worked it out")

```

### 8 - Using sys.\_getframe to get filename and lineno's 

```python
def _functionId(nFramesUp):
    import sys
    co = sys._getframe(nFramesUp+1).f_code
    return "{} ({} @ {})".format( co.co_name, co.co_filename, co.co_firstlineno)

def notImplementedYet():
    raise Exception("Not yet implemmeted : {} ".format( _functionId(1)))

def funcyou():
    notImplementedYet()

if __name__ == '__main__':
    funcyou()
```

### 7 - Traversing a tree ( predefined structure with children attribute )

- TODO improve the below implementation to print out any kind of nested structure using iterable check and cycle checks

```python
tree = {'count': 2,
        'text': '1',
        'kids': [{'count': 3,
                  'text': '1.1',
                  'kids': [{'count': 1,
                            'text': '1.1.1',
                            'kids': [{'count':0,
                                      'text': '1.1.1.1',
                                      'kids': []}]},
                           {'count': 0,
                            'text': '1.1.2',
                            'kids': []},
                           {'count': 0,
                            'text': '1.1.3',
                            'kids': []}]},
                 {'count': 0,
                  'text': '1.2',
                  'kids': []}]}


def traverse(data):

    print( ' ' * traverse.level + data['text'])


    for kid in data['kids']:
        traverse.level += 1
        traverse(kid)
        traverse.level -= 1


if __name__ == '__main__':
    traverse.level = 1
    traverse(tree)                        
```

### 6 - Time complexity of python list, deque, set etc.

- https://wiki.python.org/moin/TimeComplexity
- Surprisingly set union takes linear worst case time. I guess union-find gives better complexity but may be limited in other operations. Also many of the other data structures present in python are not present in the list.( not sure when this list was last updated. somewhere in 2017)

### 5 - http.server and SimpleHTTPServer in python program

```bash
python -c "import SimpleHTTPServer; SimpleHTTPServer.test()"
python3 -c "from http import server; server.test()"
```

### 4 - What if I want to pass arguments to the decorator itself (not the decorated function)?

- use another layer to pass the argument, and due to scoping it will avaialble in side the original decorator and returns will pass-through the internal one like earlier

```python
def mydecorator_not_really(count):

    def true_decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            print("Count ", count, sep=':')
            r = f(*args, **kwargs)
            print("Count ", count, sep=':')
            return r
        return wrapped
    return true_decorator



@mydecorator_not_really(count=123)
def myfunc(myarg):
    print("my func : " , myarg)
    return "me"


r = myfunc('asdasda')
print(r)
```

### 3 - Svn file downloader in python using yield and subprocess

- What I learned 
  - yield is really useful with subprocess output
  - hashlib.md5 hexdigest helped in keeping same named files unique
  - reading subprocess output line by line not hard
  - ```bash -c``` really useful in embedding piped linux commands inside a script 


```python
import os
import subprocess
import hashlib
import sys
import ntpath


BASEPATH = 'https://svn.abcdef.com/svn/svnfolder/' 
REGEX = '\.cpp$'
OUTPUT_DIR = 'temp'
FILE_EXT = '.cpp'


cmdscript = 'svn list --recursive '+ BASEPATH +  ' | grep ' + REGEX

def run_process(s):
    p = subprocess.Popen(s, stdout=subprocess.PIPE)
    return p.communicate()[0]



def run_process_iter(s):
    proc = subprocess.Popen(s, stdout=subprocess.PIPE, bufsize=1)
    while True:
        line = proc.stdout.readline()
        yield line



g = run_process_iter(['/bin/bash', '-c', cmdscript] ) 


def get_hash(s):
    result = hashlib.md5(s.encode())
    return result.hexdigest()




def start_download():
    for x in g:
        t= BASEPATH + x.strip()
        print('downloading from svn : ' + t.strip())

        output = run_process(['svn','cat',t])

        with open(OUTPUT_DIR + '/' +  get_hash(t)+ FILE_EXT, 'wb') as f:
            f.write('//content from : '+ t+ '\n')
            f.write(output)


def safe_create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


if __name__ == '__main__':
    try:
        safe_create_dir(OUTPUT_DIR)
    except:
        print("Failed while creating the output directory")


    try:
        start_download()
    except KeyboardInterrupt:
        print("User stopped the download process")
```


### 2 - Cellular Automta Game for Learning and practicing thinking

```python
from random import randint
from time import sleep

def get_next_row_partial(binary_rule,windo):
    for i,v in enumerate(reversed(binary_rule)):
        if v  == '1':
            prec = format(i,'03b')
            if prec == windo:
                return '1'
    return '0'




def get_next_row(rule,current_row ):
    binary_rule = format(rule, '08b')
    result = ""
    for i in range(len(current_row)):
        temp_str = current_row
        if i ==0 :
            result = result + get_next_row_partial(binary_rule,temp_str[-1] + temp_str[0] + temp_str[1] )
        elif i == len(current_row)-1:
            result = result + get_next_row_partial(binary_rule,temp_str[i-1] + temp_str[i] + temp_str[0] )
        else:
            result  = result +  get_next_row_partial(binary_rule,temp_str[i-1:i+2])
    return result

def print_rules(rule):
    binary_rule = format(rule, '08b')
    print('RULE ' + str(rule) + " : " +   binary_rule)
    
    for i,v in enumerate(reversed(binary_rule)):
        print(  format(i,'03b') + "=>" + v, end='  ' )
    print("\n")


def play_single_game():

    question = format(randint(1,255), '08b')
    rule = randint(1,255)
    print_rules(rule)
    print('Current State : ' +question)
    answer = str(input('Next State : '))

    if answer.strip() == str(get_next_row(rule, question)):
        return 1
    else:
        print('Wrong, correct is : ' + get_next_row(rule, question))
        sleep(1)
        return 0


def game():
    score = 0
    games = 0


    while True:
        games = games + 1
        print("## ROUND %d ##"%games)
        score += play_single_game()
        print( "%d / %d Wins\n\n\n" % (score,games))

def banner():
    print("https://en.wikipedia.org/wiki/Elementary_cellular_automaton\n")
    print("Game is about to predict next generation of the cellular automata,\n but rules and initial state keep changing randomly\n")


if __name__ == '__main__':

    banner()
    game()
```


### 1 - Cyclomatic complexity with radon

- https://en.wikipedia.org/wiki/Cyclomatic_complexity
- ```pip install radon```

Code with high cyclometic complexity:
```python
#old.py
class Bird(object):
  name = ''
  flightless = False
  extinct = False

  def get_speed(self):
    if self.extinct:
      return -1 # we do not care about extinct bird speeds
    else:
      if self.flightless:
        if self.name == 'Ostrich':
          return 15
        elif self.name == 'Chicken':
          return 7
        elif self.name == 'Flamingo':
          return 8
        else:
          return -1 # bird name not implemented
      else:
        if self.name == 'Gold Finch':
          return 12
        elif self.name == 'Bluejay':
          return 10
        elif self.name == 'Robin':
          return 14
        elif self.name == 'Hummingbird':
          return 16
        else:
          return -1 # bird not implemented
```
output with radon:
```bash
$ python -m radon cc -s old.py
old.py
    C 1:0 Bird - B (10)
    M 6:2 Bird.get_speed - B (10)
```

Refactored new code with low cyclomatic complexity:
```python
#new.py
class Bird(object):
  name = ''
  flightless = False
  extinct = False

  def get_speed(self):
    raise NotImplementedError

class Robin(Bird):
  name = 'Robin'

  def get_speed(self):
    return 14

class GoldFinch(Bird):
  name = 'Gold Finch'

  def get_speed(self):
    return 12

class Ostrich(Bird):
  name = 'Ostrich'
  flightless = True

  def get_speed(self):
    return 15

class Pterodactyl(Bird):
  name = 'Pterodactyl'
  extinct = True

  def get_speed(self):
    return -1
```
Output of radon on new code:
```bash
$ python -m radon cc -s new.py
new.py
    C 1:0 Bird - A (1)
    M 6:2 Bird.get_speed - A (1)
    C 9:0 Robin - A (1)
    M 12:2 Robin.get_speed - A (1)
    C 15:0 GoldFinch - A (1)
    M 18:2 GoldFinch.get_speed - A (1)
    C 21:0 Ostrich - A (1)
    M 25:2 Ostrich.get_speed - A (1)
    C 28:0 Pterodactyl - A (1)
    M 32:2 Pterodactyl.get_speed - A (1)
```




