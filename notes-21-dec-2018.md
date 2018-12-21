# 21-dec-2018

### 3 - Methods of saving state

- taken from https://github.com/pzelnip/MiscPython

```python

# method 1: a global
myGlobal = 0

def usingglobal():
    # in order to access a global variable, you need to use the global
    # keyword to explicitly indicate that the variable is globally defined
    global myGlobal

    myGlobal += 1
    print "myGlobal is %d" % myGlobal


# method 2: function attributes.  This has the benefit of not using a global
# variable (which is generally bad practice)
def usingfnattr():
    usingfnattr.val += 1
    print "usingfnattr.val is %d" % usingfnattr.val 
usingfnattr.val = 0

# method 3: generators.  This avoids a global, and the need for a declaration 
# outside a function, but isn't always applicable depending on how the value
# is being used
def usinggenerators():
    val = 0
    while True:
        val += 1
        yield val

# method 4: using classes

class UsingClass(object):
    counter = 0

    def __call__(self):
        self.counter += 1
        print "using class: %d" % self.counter

if __name__ == "__main__":
    usingglobal()  # prints 1 
    usingglobal()  # prints 2


    usingfnattr()  # prints 1
    usingfnattr()  # prints 2


    # generators are a bit different:
    foo = usinggenerators().next
    print( foo()) # prints 1
    print( foo()) # prints 2

    # using classes, a bit odd.
    f = UsingClass()
    f()
    f()
```

### 2 - Timer example

```python
from timeit import Timer

def byhand(lst):
    res = []
    for elt in lst:
        if elt % 2 == 0:
            res.append(elt)

if __name__ == "__main__":

    # method 1: by using filter()
    filtertimer = Timer("""filter(lambda x: x % 2 == 0, range(1000))""")

    # method 2: by user-written function
    userfntimer = Timer("""byhand(range(1000))""", "from __main__ import byhand")

    # method 3: by list comprehension
    listcomptimer = Timer("""[ elt for elt in range(1000) if elt % 2 == 0 ]""")


    # spit out results:
    num_iterations = 10000
    print (filtertimer.timeit(num_iterations)) # 1000 iterations
    print (userfntimer.timeit(num_iterations))
    print (listcomptimer.timeit(num_iterations))
```

### 1 - default arguments check

```python
# you can also inspect the default values given to a function
def showing_func_defaults(b=99):
    print ("b is %s, and the default value for b is %s" % (b, showing_func_defaults.func_defaults[0]))

showing_func_defaults(88)
# prints 'b is 88, and the default value for b is 99'

# this trick can be used to test if a value was given to a default parameter
def did_i_get_default(b=object()):
    if b is did_i_get_default.func_defaults[0]:
        print ("No value was passed for b")
    else:
        print("a value of %s was passed for b" % b)

did_i_get_default() # prints "no value was passed for b"
did_i_get_default(b=88) # prints "a value of 88 was passed for b
```
