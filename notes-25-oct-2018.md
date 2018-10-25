# 25-oct-2018

### 2 - Accessing memory using CPython

- ctypes module gives ability to read memory directly ( only true for CPython)

```python
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ctypes
>>> ctypes.c_ubyte.from_address(id(10)).value
16
>>> ctypes.c_ubyte.from_address(id(10)).value
16
>>> ctypes.c_ubyte.from_address(id(10) + 24).value
10
>>> ctypes.c_ubyte.from_address(id(10) + 24).value
10
>>> ctypes.c_ubyte.from_address(id(10) + 24).value is 10
True
>>> ctypes.c_ubyte.from_address(id(10) + 24).value = 11
>>> 10 == 11
True
>>> 10 is 11
True
>>> 
```

### 1 - Dynamic array class

- (ctypes.py_object * N) returns py_object_Array_N of type. (ctypes.pyobject * N)() creates a instance of it.
- Dynamic sizing for arrays created like this needs to be handled externally as they are of fixed size.

```python
import ctypes

class DynamicArray:
	"""A dynamic array class akin to a simpliified python list"""

	def __init__(self):
		"""Create an empty array"""
		self._n = 0 #count actual elements
		self._capacity = 1 # default array capacity
		self._A = self._make_array(self._capacity) #low level array

	def __len__(self):
		"""Return number of elements stored in the array"""
		return self._n


	def __getitem__(self,k):
		"""Return element at index k"""
		if not 0 <= k < self._n:
			raise IndexError('Invalid index')
		return self._A[k]


	def append(self,obj): #public method
		"""Add object to end of the array"""
		if self._n == self._capacity:
			self._resize(2*self._capacity)
		self._A[self._n] = obj
		self._n += 1


	def _resize(self, c):
		"""Resize internal array to capcity c"""
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]

		self._A = B
		self._capacity = c

	def _make_array(self,c):
		"""Return new array iwth capcity c"""
		return ( c * ctypes.py_object)() #



d = DynamicArray()
d.append(10)

for x in d:
	print x
```
