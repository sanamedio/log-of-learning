# 24-nov-2018

### 10 - class vs instance attribute(just for remembering)

```python
class Parrot:
   # class attribute
   species = "bird"

   # instance attribute
   def __init__(self, name, age):
      self.name = name
      self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
```

### 9 - Lifo queue

```python
import queue

q = queue.LifoQueue()

#add items at the head of the queue
for x in range(4):
   q.put("item-" + str(x))

#remove items from the head of the queue
while not q.empty():
   print( q.get())
```

### 8 - sys.exc_info

```python
import sys

randomList = ['a', 0, 2]

for entry in randomList:
   try:
      print("The entry is", entry)
      r = 1/int(entry)
      break
   except:
      print("Oops!",sys.exc_info()[0],"occured.")
      print("Next entry.")
      print()

print("The reciprocal of",entry,"is",r)
```
output:
```
import sys

randomList = ['a', 0, 2]

for entry in randomList:
   try:
      print("The entry is", entry)
      r = 1/int(entry)
      break
   except:
      print("Oops!",sys.exc_info()[0],"occured.")
      print("Next entry.")
      print()

print("The reciprocal of",entry,"is",r)
```

### 7 - Command pattern

```python
def demo(a,b,c):
   print 'a:',a
   print 'b:',b
   print 'c:',c

class Command:
   def __init__(self, cmd, *args):
      self._cmd=cmd
      self._args=args

   def __call__(self, *args):
      return apply(self._cmd, self._args+args)
cmd = Command(dir,__builtins__)
print cmd()

cmd = Command(demo,1,2)
cmd(3)
```

### 6 - Singleton pattern

```python
class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
s = Singleton()
print (s)

s = Singleton.getInstance()
print (s)

s = Singleton.getInstance()
print (s)
```

### 5 - State pattern

```python
class ComputerState():

   name = "state"
   allowed = []

   def switch(self, state):
      """ Switch to new state """
      if state.name in self.allowed:
         print( 'Current:',self,' => switched to new state',state.name)
         self.__class__ = state #wow dynamic changing of your own class!
      else:
         print( 'Current:',self,' => switching to',state.name,'not possible.')

   def __str__(self):
      return self.name

class Off(ComputerState):
   name = "off"
   allowed = ['on']

class On(ComputerState):
   """ State of being powered on and working """
   name = "on"
   allowed = ['off','suspend','hibernate']

class Suspend(ComputerState):
   """ State of being in suspended mode after switched on """
   name = "suspend"
   allowed = ['on']

class Hibernate(ComputerState):
   """ State of being in hibernation after powered on """
   name = "hibernate"
   allowed = ['on']

class Computer():
   """ A class representing a computer """
   
   def __init__(self, model='HP'):
      self.model = model
      # State of the computer - default is off.
      self.state = Off()
   
   def change(self, state):
      """ Change state """
      self.state.switch(state)

if __name__ == "__main__":
   comp = Computer()
   comp.change(On)
   comp.change(Off)
   comp.change(On)
   comp.change(Suspend)
   comp.change(Hibernate)
   comp.change(On)
   comp.change(Off)
```

### 4 - Strategy pattern

The strategy pattern is a type of behavioral pattern. The main goal of strategy pattern is to enable client to choose from different algorithms or procedures to complete the specified task. 

```python
import types

class StrategyExample:
   def __init__(self, func = None):
      self.name = 'Strategy Example 0'
      if func is not None:
         self.execute = types.MethodType(func, self)

   def execute(self):
      print(self.name)

def execute_replacement1(self): 
   print(self.name + 'from execute 1')

def execute_replacement2(self):
   print(self.name + 'from execute 2')

if __name__ == '__main__':
   strat0 = StrategyExample()
   strat1 = StrategyExample(execute_replacement1)
   strat1.name = 'Strategy Example 1'
   strat2 = StrategyExample(execute_replacement2)
   strat2.name = 'Strategy Example 2'
   strat0.execute()
   strat1.execute()
   strat2.execute()
```

### 3 - MVC 

from https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_model_view_controller.htm

```python
#model.py
import json

class Person():
   def __init__(self, first_name = None, last_name = None):
      self.first_name = first_name
      self.last_name = last_name
   #returns Person name, ex: John Doe
   def name(self):
      return ("%s %s" % (self.first_name,self.last_name))
   
   @classmethod
   #returns all people inside db.txt as list of Person objects
   def getAll(cls):
      database = open('db.txt', 'r')
      result = []
      json_list = json.loads(database.read())
      for i in json_list:
         item = json_list[i]
         person = Person(item['first_name'], item['last_name'])
         result.append(person)
      return result
```

```python
#view.py
from model import Person
def showAllView(items):
   print( 'In our db we have %i users. Here they are:' % len(items))
   for item in items:
      print( item.name())
def startView():
   print( 'MVC - the simplest example')
   print( 'Do you want to see everyone in my db?[y/n]')
def endView():
   print( 'Goodbye!')
```

```python
#controller.py
from model import Person
import view

def showAll():
   people_in_db = Person.getAll()
   return view.showAllView(people_in_db)

def start():
   view.startView()
   input_ = input()
   if input_ == 'y':
      return showAll()
   else:
      return view.endView()

if __name__ == "__main__":
   start()
```

```json
{
"item1": { "first_name" : "loki",  "last_name" : "s"},
"item2" : { "first_name" : "sas",  "last_name" : "t"}
}
```



### 2 - Generating magic squares

```python
def permutations(t,i):
    if i == len(t)-1:
        yield tuple(t)
    else:
        for j in range(i,len(t)):
            t[i],t[j] = t[j],t[i]
            yield from permutations(t,i+1)
            t[i],t[j] = t[j],t[i]


def check_magic(t):
    a = [ [None for i in range(3) ] for j in range(3) ]

    for i in range(3):
        for j in range(3):
            a[i][j] = t[i*3+j]

    for row in a:
        if sum(row) != 15:
            return False

    for row in zip(*a):
        if sum(row) != 15:
            return False

    if sum([ a[i][i] for i in range(3) ]) != 15:
        return False

    if sum([ a[2-i][i] for i in range(3) ]) != 15:
        return False

    return True




m_squares = set()

for m in permutations([1,2,3,4,5,6,7,8,9],0):
    if check_magic(m) :
        m_squares.add(m)


class Matrix:
    def __init__(self,l): # I know this is wrong, and should not do this in init
        self.m = [ [None for x in range(3) ] for y in range(3) ] 
        for i in range(3):
            print('')
            for j in range(3):
                print(l[i*3+j],end=' ')
        print('')





for m in m_squares:
   Matrix(m)
```

### 1 - brainfuck interpreter

- https://en.wikipedia.org/wiki/Brainfuck
- works on simple addition example of wikipedia, but failing on others!

```python
import sys


def cmpile(source_code):


    DATA_SIZE=10 + len(source_code)
    memory = [0 for x in range(DATA_SIZE)]
    memory = source_code + memory

    code_pointer= 0
    data_pointer=len(source_code)


    while True:

        print( code_pointer, data_pointer )
        if memory[code_pointer] == '>':
            data_pointer = data_pointer+1
        elif memory[code_pointer] == '<':
            data_pointer = data_pointer-1
        elif memory[code_pointer] == '+':
            memory[data_pointer] += 1
        elif memory[code_pointer] == '-' :
            memory[data_pointer] -= 1
        elif memory[code_pointer] == '.':
            print(ascii(memory[data_pointer]),end='')
        elif memory[code_pointer] == ',':
            memory[data_pointer] = int(input())
        elif memory[code_pointer] == '[':
            if memory[data_pointer] == 0:
                f = code_pointer
                match_bracket = 1
                while True:
                    if match_bracket ==0:
                        break
                    if memory[f] == '[':
                        match_bracket+=1
                    elif memory[f] == ']':
                        match_bracket-=1
                    f = f+1
                code_pointer = f
        elif memory[code_pointer] == ']':
            if memory[data_pointer] != 0:
                f = code_pointer
                match_bracket = 1
                while True:
                    f = f-1
                    if memory[f] == ']':
                        match_bracket+=1
                    elif memory[f] == '[':
                        match_bracket-=1
                    if match_bracket == 0:
                        break
                code_pointer = f



        code_pointer+= 1

        if code_pointer == len(source_code):
            print("\bprogram ended")
            print(code_pointer, data_pointer, source_code,memory,sep='\n')
            return

        if (code_pointer> DATA_SIZE-1) or (data_pointer > DATA_SIZE-1)  or (code_pointer < 0) or (data_pointer < 0):
            raise Exception("Out of memory read or write")



cmpile(list('++>+++++[<+>-]'))
```
