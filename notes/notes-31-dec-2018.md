# 31-dec-2018


### 8 - threesum

```python
def threeSum(arr,S):

    # scanning plus two poitners

    arr = sorted(arr)



    for i in range(0, len(arr)-2):


        ptr_start , ptr_end = i+1, len(arr) - 1



        while ptr_start < ptr_end:


            total = arr[i]  + arr[ptr_start]  + arr[ptr_end]


            if total == S:
                return True
            elif total < S:
                ptr_start += 1
            else:
                ptr_end -= 1

    return False



if __name__ == '__main__':

    print(threeSum([1,1,1,1,1,1,1,1,2,3,1,12,2,3,23,1,2,2,34,12,12],3))
```

### 7 - finding majority element in linear time without extra space


```python
import math



def majorityElement(arr):


    candidate = None
    count = 0



    for i in range(len(arr)):

        if candidate is None or count ==0 :
            candidate = arr[i]
            count = 1
        elif arr[i] == candidate:
            count += 1
        else:
            count -= 1



    count = 0


    for el in arr:
        if el == candidate:
            count += 1


    if count > math.floor(len(arr) / 2 ):
        return candidate
    else:
        return None



if __name__ == '__main__':

    print(majorityElement([1,2,3,4,1,2,3,4,1]))
    print(majorityElement([]))
    print(majorityElement([2,1,1,1,1,1,1,2,2,2,2,2,2]))
```

### 6 - words with vowel trigram from setence

```python
import re


def threeVowels(string):


    arr = string.split(' ')

    count = 0




    for word in arr:
        if re.search(r'[aeiou]{3,}', word ) != None:
            count += 1


    return count


if __name__ == '__main__' :


    print(threeVowels('this is a funny thing hahahah aeiou'))
```

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
