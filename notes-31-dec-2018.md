# 31-dec-2018

### 1 - twoSum

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
