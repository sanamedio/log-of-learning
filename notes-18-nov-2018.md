# 18-nov-2018

### 5 - clipping list to n elements of each type

```python

import collections

def delete_all_nth_slow(array,n):


    result = []

    for i in array:

        if result.count(i) < n:
            result.append(i)
    return result




def delete_all_nth(array,n):

    result = []

    counts = collections.defaultdict(int)


    for i in array:

        if counts[i] <n:
            result.append(i)
            counts[i] += 1


    return result


if __name__ == '__main__':
                
    print( delete_all_nth_slow([1,1,1,1,2,2,2],2))
    print( delete_all_nth([1,1,1,1,2,2,2],2))
```


### 4 - Common stuff between dicts

- doesnt work for python2

```python

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

print('Common keys:', a.keys() & b.keys())
print('Keys in a not in b:', a.keys() - b.keys())
print('(key,value) pairs in common:', a.items() & b.items())
```

### 3 - list filter with clipping

```python
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
print(neg_clip)

# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print(pos_clip)

# Compressing example

addresses = [
    '5412 N CLARK',
    '5148 N CLARK', 
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [ n > 5 for n in counts ]
a = list(compress(addresses, more5))
print(a)
```

### 2 - subdict

```python
# example of extracting a subset from a dictionary
from pprint import pprint

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }

print("All prices over 200")
pprint(p1)

# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }

print("All techs")
pprint(p2)
```

### 1 - calculating with dictionaries

- zip values and keys and apply operations of min, max  and sorted on them (pycookbook)
```python
 Example of calculating with dictionaries

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
print('    ', name, price)
```
