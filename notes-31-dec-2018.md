# 31-dec-2018

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
