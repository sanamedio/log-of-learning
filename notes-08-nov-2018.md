# 08-nov-2018


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




