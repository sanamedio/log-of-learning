# 21-nov-2018

### 1 - Determine if a string contains unique characters

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
