# 31-dec-2018

### 5 - finding The first non repeating character in a string

```python
def firstNonRepChar(string):


    hashTable = {}

    for c in string:
        if c not in hashTable:
            hashTable[c] = 1
        else:
            hashTable[c] += 1



    for c in string:
        if hashTable[c] == 1 :
            return c


    return -1




if __name__ == '__main__':
    print(firstNonRepChar('gjsdfklgjsldjeiortioz'))
    print(firstNonRepChar(''))
    print(firstNonRepChar('aaaa'))

```


### 4 - isPrime

- the upper bound sqrt and ceil don't work when n is taken; and if you take too higher without thinking; it will give wrong answer for lower numbers. simple but error prone

```python
import math


def isprime(n):

    if n < 2 :
        return False



    for i in range(2, int(math.ceil(math.sqrt(n+1)))):
        print n, i
        if n % i == 0 :
            return False


    return True



if __name__ == '__main__':

    assert isprime(1) == False
    assert isprime(2) == True
    assert isprime(24) == False
    assert isprime(23) == True
    assert isprime(25) == True # failed
```

### 3 - clockAngle

- smaller angle between hour hand and minute hand of a clock at a particular instant

```python
def clockAngle(hours, mins):
    h = 0.5 * ( 60 * hours + mins );
    m = 6 * mins

    angle = abs(h-m)

    if angle > 180 :
        return 360 - angle
    else:
        return angle



if __name__ == '__main__':
    print (clockAngle(0,0))
    print (clockAngle(6,30))
    print (clockAngle(6,0))
    print (clockAngle(12,0))
```

### 2 - nestedSum
- take sum of nested arrays

```python
def sumNested(arr):

    result =  0


    for i in range(0,len(arr)):
        if type(arr[i]) is not int:
            result += sumNested(arr[i])
        else:
            result += arr[i]

    return result


if __name__ == '__main__':
    print(sumNested([1,1,1,1,1,[1,1,1,1,[1,1,1,1]]]))
    print(sumNested([[[[[]]]]]))

```

### 1 - twoSum

- find if a pair exists with a given sum

```python
def twoSum(arr, S):
    hashTable = {}
    for i in range(0, len(arr)):
        sumMinusElement = S - arr[i]
        if sumMinusElement in hashTable:
            return True
        hashTable[arr[i]] = True
    return False



print(twoSum([1,1,1,1,1,1],2))
print(twoSum([1,1],3))
print(twoSum([],10))
print(twoSum([-1,2],1))

```
