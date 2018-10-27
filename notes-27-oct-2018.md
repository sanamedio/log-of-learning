# 27-oct-2018

### 7 - heapq

```python
import heapq

nums = [ 1, 8 , 2 , 23, 7 , -4 , 18 , 23, 42 , 37, 2 ]
print( heapq.nlargest(3, nums))
print( heapq.nsmallest(3,nums))


portfolio = [
	{'name' : 'IBM' , 'price' : 91.1 },
	{'name' : 'Oracle' , 'price' : 22.2 }
]


cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)
```
```python
nums = [1,2,33,3,5]
import heapq
heap = list(nums)
heapq.heapify(heap) # still heap is list, then where is the information about structure stored ?
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap) # raises exception if can't pop anymore
print(heap)
heapq.heappop(heap)
print(heap)
```


### 6 - deque and yield pattern

```python
from collections import deque
import sys


def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)

	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)



if __name__ == '__main__':
	with sys.stdin as f:
		for line, prevlines in search(f, 'python', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)


```

### 5 - Permutations

```python
def permute(seq):
	'''generator based'''
	if not seq:
		yield seq
	else:
		for i in xrange(len(seq)):
			rest = seq[:i] + seq[i+1:]
			for x in permute(rest):
				yield seq[i:i+1] + x





def permute1( seq ):
	''' normal return based '''
	if not seq:
		return [seq]

	else:
		res= []
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:]
			for x in permute1(rest):
				res.append(seq[i:i+1] + x )
	return res
```

### 4 - StringIO and sys.out

```python
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys, io
>>> save = sys.stdout
>>> new_stream = io.StringIO()
>>> sys.stdout = new_stream
>>> print("hello world")
>>> sys.stdout = save
>>> print("this is me")
this is me
>>> new_stream.getvalue()
'hello world\n'
>>> 
```


### 3 - Elements of style

- https://github.com/crista/exercises-in-programming-style
- Different ways of writing the same python program; with different trade-offs

### 2 - Call source code for function object

```c
PyObject *
PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw)
{
    ternaryfunc call;

    if ((call = func->ob_type->tp_call) != NULL) {
        PyObject *result;
        if (Py_EnterRecursiveCall(" while calling a Python object"))
            return NULL;
        result = (*call)(func, arg, kw);
        Py_LeaveRecursiveCall();
        if (result == NULL && !PyErr_Occurred())
            PyErr_SetString(
                PyExc_SystemError,
                "NULL result without error in PyObject_Call");
        return result;
    }
    PyErr_Format(PyExc_TypeError, "'%.200s' object is not callable",
                 func->ob_type->tp_name);
    return NULL;
}
```

### 1 - PEP 3148 concurrent futures

```python
from concurrent import futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime,
                                                      PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()
```
  
