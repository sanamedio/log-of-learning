# 01-nov-2020

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
