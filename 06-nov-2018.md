# 06-nov-2018

### 1 - Factorial in three ways

```python
def factorialR(N):
	"""Recursive function"""
	assert isinstance(N, int) and N >= 1
	return 1 if N <= 1 else N * factorialR(N-1)




def factorialI(N):
	"""Iterative Funtion"""
	assert isinstance(N, int) and N >= 1
	product = 1
	while N >= 1:
		product *= N
		N -= 1
	return product



from functools import reduce
from operator import mul

def factorialHOF(n):
	"""Higher order functions"""
	return reduce(mul, range(1,n+1), 1)
		
	


print(factorialR(5))
print(factorialI(5))
print(factorialHOF(5))
```
