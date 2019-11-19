# 12-nov-2018

### 10 - Top down recursive parsing

- Just handles the priority of operators
- While the next tokens priority is higher, keep delegating computation to another recusive compute(), otherwise break and return yourself. Each compute frame in recursion will handle a level of priority and once it returns the previous level of compute() will continue processing.

```python
import re
token_regex = re.compile("\s*(?:(\d+)|(.))")

#simple
class literal_token:
    def __init__(self, value):
        self.value = int(value)
    def get_value(self):
        return self.value


class operator_add_token:
    priority = 10
    def action(self, current):
        return current + calculate(10)


class operator_sub_token:
    priority = 10
    def action(self, current):
        return current - calculate(10)

class operator_mul_token:
    priority = 20
    def action(self, current):
        return current * calculate(20)

class operator_div_token:
    priority = 20
    def action(self, current):
        return current / calculate(20)


class end_token:
    priority = 0


#initial priority is zero, every positive >0 priority action will finish
def calculate(current_priority=0):
    
    print 'calculate ' + str(current_priority)
    
    global token
    
    current = token
    result = current.get_value()
    
    token = next_token()
    
    while current_priority < token.priority: # if equal priority or more is found it will break the loop which means just send back results, otherwise keep delegating action to the next part of expression
        print current_priority, ' : ' , token.__class__, token.priority
        current = token
        token = next_token()
        print '>> prev_result' , current.__class__ , result
        result = current.action(result)
        print '>> result' , result
    return result

def tokenize(program):
    for number, operator in token_regex.findall(program):
        if number:
            yield literal_token(number)
        elif operator == "+":
            yield operator_add_token()
        elif operator == "-":
            yield operator_sub_token()
        elif operator == "*":
            yield operator_mul_token()
        elif operator == "/":
            yield operator_div_token()
        else:
            raise SyntaxError("unknown operator")
    yield end_token()


def parse(program):
    print(program)
    global token, next_token
    next_token = tokenize(program).next
    token = next_token()
    return calculate(0)


if __name__ == '__main__':
    import sys
    print(parse(sys.argv[1]))
```


### 9 - Autoshaping

```python
In [64]: a = np.arange(30)                                                                                                                                                                                         

In [67]: a.shape = 2, -1 , 3 # -1 means whatever is convinient sort of                                                                                                                                                                                      

In [68]: a                                                                                                                                                                                                         
Out[68]: 
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14]],

       [[15, 16, 17],
        [18, 19, 20],
        [21, 22, 23],
        [24, 25, 26],
        [27, 28, 29]]])
```


### 8 - Histogram plot of normal distribution

```python
In [40]: import numpy as np                                                                                                                                                                                        

In [41]: import matplotlib.pyplot as plt                                                                                                                                                                           
mu
In [42]: mu , sigma = 2, 0.5                                                                                                                                                                                       

In [43]: v = np.random.normal(mu, sigma, 10000)                                                                                                                                                                    

In [44]: plt.hist(v,  bins=50,  density = 1 )                                                                                                                                                                      
Out[44]: 
(array([0.00122371, 0.        , 0.        , 0.00122371, 0.        ,
        0.00244742, 0.00367113, 0.0110134 , 0.01223712, 0.01957938,
        0.0428299 , 0.06485671, 0.07097527, 0.11135775, 0.1382794 ,
        0.1590825 , 0.27166396, 0.28390107, 0.35487634, 0.45766811,
        0.53476194, 0.6265403 , 0.6901733 , 0.72810836, 0.80153105,
        0.83579497, 0.79541249, 0.79908363, 0.67304134, 0.69506815,
        0.59594751, 0.52741967, 0.44420729, 0.34875779, 0.30103304,
        0.23005777, 0.18355673, 0.11870002, 0.08810723, 0.063633  ,
        0.05384331, 0.03671135, 0.02202681, 0.01223712, 0.0110134 ,
        0.00367113, 0.00734227, 0.        , 0.00122371, 0.00122371]),
 array([-0.12123035, -0.03951175,  0.04220686,  0.12392546,  0.20564407,
         0.28736268,  0.36908128,  0.45079989,  0.53251849,  0.6142371 ,
         0.6959557 ,  0.77767431,  0.85939292,  0.94111152,  1.02283013,
         1.10454873,  1.18626734,  1.26798594,  1.34970455,  1.43142316,
         1.51314176,  1.59486037,  1.67657897,  1.75829758,  1.84001618,
         1.92173479,  2.0034534 ,  2.085172  ,  2.16689061,  2.24860921,
         2.33032782,  2.41204642,  2.49376503,  2.57548364,  2.65720224,
         2.73892085,  2.82063945,  2.90235806,  2.98407667,  3.06579527,
         3.14751388,  3.22923248,  3.31095109,  3.39266969,  3.4743883 ,
         3.55610691,  3.63782551,  3.71954412,  3.80126272,  3.88298133,
         3.96469993]),
 <a list of 50 Patch objects>)

In [45]: plt.show()   
```

### 7 - Code from numpy quickstart

```python
In [1]: import numpy as np                                                                                                                                                                                         

In [2]: a = np.arange(15).reshape(3,5)                                                                                                                                                                             

In [3]: a                                                                                                                                                                                                          
Out[3]: 
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

In [4]: a.shape                                                                                                                                                                                                    
Out[4]: (3, 5)

In [5]: a.ndim                                                                                                                                                                                                     
Out[5]: 2

In [6]: a.dtype.name                                                                                                                                                                                               
Out[6]: 'int64'

In [7]: a.size                                                                                                                                                                                                     
Out[7]: 15

In [8]: type(a)                                                                                                                                                                                                    
Out[8]: numpy.ndarray

In [9]: b = np.array([1,2,34,5])                                                                                                                                                                                   

In [10]: type(b)                                                                                                                                                                                                   
Out[10]: numpy.ndarray

```
```python
In [9]: b = np.array([1,2,34,5])                                                                                                                                                                                   

In [10]: type(b)                                                                                                                                                                                                   
Out[10]: numpy.ndarray

In [11]: a = np.array([2,3,4])                                                                                                                                                                                     

In [12]: a                                                                                                                                                                                                         
Out[12]: array([2, 3, 4])

In [13]: a.dtype                                                                                                                                                                                                   
Out[13]: dtype('int64')

In [14]: b = np.array([1.2, 3.5, 5.1] )                                                                                                                                                                            

In [15]: b.dtype                                                                                                                                                                                                   
Out[15]: dtype('float64')
```

```python
In [17]: b = np.array( [ [1,2] , [3,4] ] )                                                                                                                                                                         

In [18]: b                                                                                                                                                                                                         
Out[18]: 
array([[1, 2],
       [3, 4]])

In [19]: b = np.array( [ (1,2)  , (3,4) ] )                                                                                                                                                                        

In [20]: b                                                                                                                                                                                                         
Out[20]: 
array([[1, 2],
       [3, 4]])
```
```python
In [21]: c = np.array( [ [ 1,2] , [3,4] ] , dtype=complex)                                                                                                                                                         

In [22]: c                                                                                                                                                                                                         
Out[22]: 
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])

In [23]: np.zeros(( 3,4 ) )                                                                                                                                                                                        
Out[23]: 
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])

In [24]: np.ones( (2,3,4), dtype=np.int16 )                                                                                                                                                                        
Out[24]: 
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)

In [25]: np.empty( ( 2,3 ) )                                                                                                                                                                                       
Out[25]: 
array([[2.67473386e-316, 0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000, 0.00000000e+000]])
```

```python
In [26]: np.arange(10,50,5)                                                                                                                                                                                        
Out[26]: array([10, 15, 20, 25, 30, 35, 40, 45])

In [27]: np.arange(10,11,0.1)                                                                                                                                                                                      
Out[27]: array([10. , 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9])

In [28]: np.linspace(0,2,9)                                                                                                                                                                                        
Out[28]: array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])

In [31]: from numpy import pi                                                                                                                                                                                      

In [32]: np.linspace(0,2,9)                                                                                                                                                                                        
Out[32]: array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])

In [33]: x  = np.linspace( 0 , 2*pi, 100 )                                                                                                                                                                         

In [34]: f = np.sin(x)                                                                                                                                                                                             

In [35]: f                                                                                                                                                                                                         
Out[35]: 
array([ 0.00000000e+00,  6.34239197e-02,  1.26592454e-01,  1.89251244e-01,
        2.51147987e-01,  3.12033446e-01,  3.71662456e-01,  4.29794912e-01,
        4.86196736e-01,  5.40640817e-01,  5.92907929e-01,  6.42787610e-01,
        6.90079011e-01,  7.34591709e-01,  7.76146464e-01,  8.14575952e-01,
        8.49725430e-01,  8.81453363e-01,  9.09631995e-01,  9.34147860e-01,
        9.54902241e-01,  9.71811568e-01,  9.84807753e-01,  9.93838464e-01,
        9.98867339e-01,  9.99874128e-01,  9.96854776e-01,  9.89821442e-01,
        9.78802446e-01,  9.63842159e-01,  9.45000819e-01,  9.22354294e-01,
        8.95993774e-01,  8.66025404e-01,  8.32569855e-01,  7.95761841e-01,
        7.55749574e-01,  7.12694171e-01,  6.66769001e-01,  6.18158986e-01,
        5.67059864e-01,  5.13677392e-01,  4.58226522e-01,  4.00930535e-01,
        3.42020143e-01,  2.81732557e-01,  2.20310533e-01,  1.58001396e-01,
        9.50560433e-02,  3.17279335e-02, -3.17279335e-02, -9.50560433e-02,
       -1.58001396e-01, -2.20310533e-01, -2.81732557e-01, -3.42020143e-01,
       -4.00930535e-01, -4.58226522e-01, -5.13677392e-01, -5.67059864e-01,
       -6.18158986e-01, -6.66769001e-01, -7.12694171e-01, -7.55749574e-01,
       -7.95761841e-01, -8.32569855e-01, -8.66025404e-01, -8.95993774e-01,
       -9.22354294e-01, -9.45000819e-01, -9.63842159e-01, -9.78802446e-01,
       -9.89821442e-01, -9.96854776e-01, -9.99874128e-01, -9.98867339e-01,
       -9.93838464e-01, -9.84807753e-01, -9.71811568e-01, -9.54902241e-01,
       -9.34147860e-01, -9.09631995e-01, -8.81453363e-01, -8.49725430e-01,
       -8.14575952e-01, -7.76146464e-01, -7.34591709e-01, -6.90079011e-01,
       -6.42787610e-01, -5.92907929e-01, -5.40640817e-01, -4.86196736e-01,
       -4.29794912e-01, -3.71662456e-01, -3.12033446e-01, -2.51147987e-01,
       -1.89251244e-01, -1.26592454e-01, -6.34239197e-02, -2.44929360e-16])

In [36]: x                                                                                                                                                                                                         
Out[36]: 
array([0.        , 0.06346652, 0.12693304, 0.19039955, 0.25386607,
       0.31733259, 0.38079911, 0.44426563, 0.50773215, 0.57119866,
       0.63466518, 0.6981317 , 0.76159822, 0.82506474, 0.88853126,
       0.95199777, 1.01546429, 1.07893081, 1.14239733, 1.20586385,
       1.26933037, 1.33279688, 1.3962634 , 1.45972992, 1.52319644,
       1.58666296, 1.65012947, 1.71359599, 1.77706251, 1.84052903,
       1.90399555, 1.96746207, 2.03092858, 2.0943951 , 2.15786162,
       2.22132814, 2.28479466, 2.34826118, 2.41172769, 2.47519421,
       2.53866073, 2.60212725, 2.66559377, 2.72906028, 2.7925268 ,
       2.85599332, 2.91945984, 2.98292636, 3.04639288, 3.10985939,
       3.17332591, 3.23679243, 3.30025895, 3.36372547, 3.42719199,
       3.4906585 , 3.55412502, 3.61759154, 3.68105806, 3.74452458,
       3.8079911 , 3.87145761, 3.93492413, 3.99839065, 4.06185717,
       4.12532369, 4.1887902 , 4.25225672, 4.31572324, 4.37918976,
       4.44265628, 4.5061228 , 4.56958931, 4.63305583, 4.69652235,
       4.75998887, 4.82345539, 4.88692191, 4.95038842, 5.01385494,
       5.07732146, 5.14078798, 5.2042545 , 5.26772102, 5.33118753,
       5.39465405, 5.45812057, 5.52158709, 5.58505361, 5.64852012,
       5.71198664, 5.77545316, 5.83891968, 5.9023862 , 5.96585272,
       6.02931923, 6.09278575, 6.15625227, 6.21971879, 6.28318531])
```


### 6 - Difference between cls and self

```python

In [36]: class Test: 
    ...:     def __new__(cls): 
    ...:         print(cls) 
    ...:                                                                                                                                                                                                           

In [37]: Test()                                                                                                                                                                                                    
<class '__main__.Test'>

In [38]: class Test: 
    ...:     def __init__(self): 
    ...:         print(self) 
    ...:                                                                                                                                                                                                           

In [39]: Test()                                                                                                                                                                                                    
<__main__.Test object at 0x7f46bf69e470>
Out[39]: <__main__.Test at 0x7f46bf69e470>
```

### 5 - Self or call it anything, doesnt matter

```python
In [29]: class Test: 
    ...:     def __init__(elf, x ): 
    ...:         elf.x = x 
    ...:                                                                                                                                                                                                           

In [30]: Test(2)                                                                                                                                                                                                   
Out[30]: <__main__.Test at 0x7f46bf6016d8>
```

### 4 - Numpy reshaping

```python
In [1]: import numpy                                                                                                                                                                                               

In [2]: numpy.arange(15)                                                                                                                                                                                           
Out[2]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

In [3]: numpy.arange(15).reshape(3,5)                                                                                                                                                                              
Out[3]: 
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```

### 3 - @total_ordering to do less work

- no need to implement all of the comparators

```python
from functools import total_ordering

@total_ordering
class Account:


    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return 'Account({}, {})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount : {}'.format(self.owner, self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount , int ):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance



acc = Account('gigs',10)


acc2 = Account('loki', 100)
acc2.add_transaction(20)
acc2.add_transaction(30)


print(acc.balance)
print(acc2.balance)


print ( acc2 > acc)
```

### 2 - dir() and dunder dict

- dir() doesn't just look up an object's ```__dict__``` (which sometimes doesn't even exist), it will use the object's heritage (its class or type, and any superclasses, or parents, of that class or type) to give you a complete picture of all available attributes.

- An instance ```__dict__``` is just the 'local' set of attributes on that instance, and does not contain every attribute available on the instance. Instead, you need to look at the class and the class's inheritance tree too.

### 1 - Async decorator


```python
from Queue import Queue
from threading import Thread


class asynchronous():

    def __init__(self, func):
        self.func = func

        def threaded(*args, **kwargs):
            self.queue.put(self.func(*args, **kwargs))


        self.threaded = threaded




    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


    def start(self, *args, **kwargs):
        self.queue = Queue()
        thread = Thread(target=self.threaded, args=args,kwargs = kwargs)
        thread.start()
        return asynchronous.Result(self.queue, thread)



    class NotYetDoneException(Exception):
        def __init__(self, message):
            self.message = message


    class Result():
        def __init__(self, queue, thread):
            self.queue = queue
            self.thread = thread

        def is_done(self):
            return not self.thread.is_alive()


        def get_result(self):
            if not self.is_done():
                raise asynchronous.NotYetDoneException('the call has not completed yet')

            if not hasattr(self, 'result'):
                self.result = self.queue.get()


            return self.result




if __name__ == '__main__':


    import time


    @asynchronous
    def long_process(num):
        time.sleep(10)
        return num*num


    result = long_process.start(12)


    for i in range(20):
        print(i)
        time.sleep(1)


        if result.is_done():
            print "result {0}".format(result.get_result())





    result2 = long_process.start(13)



    try:
        print ( "result2 {0}".format(result2.get_result()))


    except asynchronous.NotYetDoneException as ex:
        print ex.message
```
