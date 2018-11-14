# 15-nov-2018

### 6 - Write your own square root function

```python

In [12]:  
    ...: def sqroot(n , eps ,mx): 
    ...:    x = 1.0 
    ...:    itr = 0 
    ...:    while abs( x*x - n ) > eps and itr < mx: 
    ...:       x = x - (x*x-n)/2*x 
    ...:       itr = itr + 1 
    ...:    return x 
    ...:     
    ...:     
    ...:     
    ...:                                                                        

In [13]: sqroot(2,0.0001, 10)                                                   
Out[13]: 1.3351578377717581

In [14]: sqroot(2,0.0001, 100)                                                  
Out[14]: 1.3801553432658384

In [15]: sqroot(2,0.0001, 1000)                                                 
Out[15]: 1.403003973690669

In [16]: sqroot(2,0.0001, 10000)                                                
Out[16]: 1.4106685607006662

In [17]: sqroot(2,0.0001, 100000)                                               
Out[17]: 1.4130943389174646

In [18]: sqroot(2,0.0001, 10000000)                                             
Out[18]: 1.4141017458848133
```
   

### 5 - Multiple inheritence differs between 2 and 3

```python

Python3 : 
In [6]: class A(): 
   ...:     def foo1(self): 
   ...:         print( "A") 
   ...: class B(A): 
   ...:     def foo2(self): 
   ...:         pass 
   ...: class C(A): 
   ...:     def foo1(self): 
   ...:         print( "C" ) 
   ...: class D(B, C): 
   ...:     pass 
   ...:  
   ...: d = D() 
   ...: d.foo1()                                                                
C
```

Python2 :
```python
In [2]: class A():
   ...:     def foo1(self):
   ...:         print "A"
   ...: class B(A):
   ...:     def foo2(self):
   ...:         pass
   ...: class C(A):
   ...:     def foo1(self):
   ...:         print "C"
   ...: class D(B, C):
   ...:     pass
   ...: 
   ...: d = D()
   ...: d.foo1()
   ...: 
A
```

### 4 - Class variable

```python
class Test():  
    num_of_instance = 0  
    def __init__(self, name):  
        self.name = name  
        Test.num_of_instance += 1  
  
if __name__ == '__main__':  
    print (Test.num_of_instance)   # 0
    t1 = Test('jack')  
    print (Test.num_of_instance )  # 1
    t2 = Test('lucy')  
    print (t1.name , t1.num_of_instance)  # jack 2
    print (t2.name , t2.num_of_instance ) # lucy 2
```

```python
class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print (p1.name)  # bbb
print (p2.name)  # aaa
print (Person.name)  # aaa

## so counter intituive 

class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print (p1.name)  # [1]
print (p2.name)  # [1]
print (Person.name)  # [1]
```

### 3 - method types example

```python
def foo(x):
    print "executing foo(%s)"%(x)

class A():
    def foo(self,x):
        print( "executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print( "executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print( "executing static_foo(%s)"%x)

a=A()

a.foo('bar')
A.class_foo('bar')
A.static_foo('bar')
foo('bar')
```

- static method don't have access to cls

### 2 - Seemingly weird

- Immutables and Mutables can behave quite differently
- How can I combine id and python inspection capability to map state of python interpreter; to help me see scope changes and other stuff better?

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1
>>> def Foo(a):
...     a = 2
... 
>>> Foo(a)
>>> a
1
>>> b = []
>>> def Foo(b):
...     b.append(1)
... 
>>> Foo(b)
>>> b
[1]
>>> 
```



- https://stackoverflow.com/questions/633127/viewing-all-defined-variables

```python
>>> from pprint import pprint
>>> pprint(vars())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x7f4c0e8b7598>}
>>> pprint(dir())
['__annotations__',
 '__builtins__',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'pprint']
>>> pprint(globals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x7f4c0e8b7598>}
>>> pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x7f4c0e8b7598>}
>>> 
```



### 1 - Some tricks with list,set and maps

- from [here](https://github.com/taizilongxu/interview_python)

- unique without set directly
```python
>>> l1 = ['b','c','d','b','c','a','a']
>>> l2 = {}.fromkeys(l1).keys()
>>> print( l2)
dict_keys(['b', 'c', 'd', 'a'])
>>> 
```

- Maintaining order
```python
>>> l1 = ['b','c','d','b','c','a','a']
>>> l2 = list(set(l1))
>>> l2
['d', 'c', 'b', 'a']
>>> l2.sort(key=l1.index)
>>> l2
['b', 'c', 'd', 'a']
>>> 
```

- doing unique using list comprehension
```python
>>> l1 = ['b', 'c' , 'd' , 'b', 'c', 'a', 'a']
>>> l2 = []
>>> [ l2.append(i) for i in l1 if not i in l2 ]
[None, None, None, None]
>>> l2
['b', 'c', 'd', 'a']
>>> 
```
- from keys
```python
>>> dict1={}.fromkeys(('x','y'),-1)
>>> dict={'x':-1,'y':-1}
>>> dict2={}.fromkeys(('x','y'))
>>> dict2={'x':None, 'y':None}
>>> dict
{'x': -1, 'y': -1}
>>> dict1
{'x': -1, 'y': -1}
>>> dict2
{'x': None, 'y': None}
>>> 
```
