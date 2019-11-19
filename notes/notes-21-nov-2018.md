# 21-nov-2018

### 5 - primes

```python
def primes(n):
    result = []
    for x in range(2,n):
        if not any([x%y==0 for y in result]):
            result.append(x)
    return result 

if __name__ == '__main__':
    print(primes(100))
```

Prime numbers between root(n) to n(not included)
```python
>>> n = 100
>>> reduce(lambda a,x: [i for i in a if i%x!=0],range(2,int(sqrt(n))),range(2,n))
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> 
```

### 4 - Treeset implementation 

```python
import random


class Node:

    def __init__(self, value= None,left = None, right =None):
        self.left = left
        self.right = right
        self.value = value
        self.deleted = False


    def __str__(self):
        return str([self.value,self.left,self.right])

def insert(s , val ):
    if s == None:
        return Node(val, None, None)
    else:
        if   s.value < val:
             s.right = insert(s.right, val)
        elif s.value > val:
             s.left = insert(s.left, val)
    return s


def find(s,x):
    if s is None:
        return None
    else:
        if s.value > x:
            return find(s.left,x)
        elif s.value < x:
            return find(s.right,x)
        elif s.value == x:
            return s
    return s



def inorder(s):
    if s is not None:
        yield from inorder(s.left)
        if not s.deleted:
            yield (s.value)
        yield from inorder(s.right)


def count(s):
    if s == None:
        return 0
    else:
        return 1+ count(s.left) + count(s.right)

class TreeSet:

    def __init__(self):
        self.tree = None

    def add(self,x):
        if self.tree is None:
            self.tree = Node(x,None,None)
        else:
            self.tree = insert(self.tree,x)
        return self

    def remove(self,x):
        z = find(self.tree,x)
        z.deleted = True

    def __len__(self):
        return count(self.tree)
    
    def __repr__(self):
        return list(inorder(self.tree))

    def __str__(self):
        return str(self.__repr__())

if __name__ == '__main__':
    
    ts = TreeSet()

    for i in range(100):
        ts.add(i%5)

    ts.remove(0)
    ts.remove(1)

    print(ts)
```

### 3 - binary tree traversals

```python
class Node:
    def __init__(self, value= None,left = None, right =None):
        self.left = left
        self.right = right
        self.value = value

def insert(s , val ):
    if s == None:
        return Node(val, None, None)
    else:
        if   s.value < val:
             s.right = insert(s.right, val)
        elif s.value >= val:
             s.left = insert(s.left, val)
    return s

def traverse(s, t, f):
    if s:
        (t == 0 and f(s.value))
        traverse(s.left,t,f)
        (t == 1 and f(s.value))
        traverse(s.right,t,f)
        (t == 2 and f(s.value))

root = Node(1,None,None)

for i in range(2,10):
    root = insert(root,i)


def print_(*args):
    print(*args,end=' ')

traverse(root,0,print_)
print('')
traverse(root,1,print_)
print('')
traverse(root,2,print_)
```

### 2 - Determine if a string is a permutation of another

```python
# determine if a string is permuation of another or not
# each character will have same count in both, so frequency table shsould match
# if we can write a position indepdent hash function, that would be same for both
# if we sort them both will be equal
# 

def check_perm_sorting(x,y):
    return sorted(x) == sorted(y)

def check_perm_counter(x,y):
    from collections import Counter
    x_ = Counter(x)
    y_ = Counter(y)
    return x_ == y_


TO_CHECK = [check_perm_sorting, check_perm_counter
        ]

for check in TO_CHECK:
    print("Running check for "+ check.__name__,end=" ")
    assert check("abcd", "dcba") == True
    assert check("aaa", "aaa") == True
    assert check("abab","baba") == True
    assert check("","") == True
    assert check("a","a") == True
    assert check("aasdsds", "asdasd") == False
    assert check("aaabbb", "bbaaac") == False
    print("succesful !")
~                             
```


### 1 - Determine if a string contains unique characters

from [here](https://github.com/donnemartin/interactive-coding-challenges)

```python

#i should try implementing set, 

def check_uniqueness_of_list_naive(s):

    for x in s:
        if s.count(x) > 1:
            return False
    return True

def check_uniqueness_of_list_naive2(s):
    return not any([ s.count(x) > 1 for x in s ])


def check_uniqueness_of_list_pythonic(s):

    if len(s) < 2: return True

    s_ = sorted(s)
    return all([a!=b for a,b in zip(s_[0:-1],s_[1:])])


def check_uniqueness_of_list_sorting(s):
   
    if len(s) < 2: return True

    s_ = sorted(s)
    for i in range(len(s_)-1):
        if s_[i] == s_[i+1]:
            return False
    return True



def check_uniqueness_of_list_basics(s):
    """ time complxity? can be linear or linear logn based on iplementation of set"""
    t = set()

    for x in s:
        if x in t:
            return False
        t.add(x)
    return True


def check_uniqueness_of_list(s):
    return len(set(s)) == len(s)



TO_CHECK = [ check_uniqueness_of_list_sorting, 
             check_uniqueness_of_list_basics,
             check_uniqueness_of_list,
             check_uniqueness_of_list_pythonic,
             check_uniqueness_of_list_naive,
             check_uniqueness_of_list_naive2
        ]

for check in TO_CHECK:
    print("Running check for "+ check.__name__,end=" ")
    assert check("abcd") == True
    assert check("aaa") == False
    assert check("abab") == False
    assert check("") == True
    assert check("a") == True
    print("succesful !")
```
