# 17-jan-2021

### 2 - climbing stairs

you can take one or two steps at a time. number of ways to climb n stairs

problem from this list:- https://seanprashad.com/leetcode-patterns/

```python
#https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.
def climbStairs(int n):
    dp = [ 0 for _ in range(n + 1)]
    if (n == 1) :
        return 1

    if (n == 2) :
        return 2

    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    for i in range(3,n+1):
      dp[i] = dp[i-1] + dp[i - 2];

    return dp[n];
```

### 1 - find numbers missing from array

if array is containing duplicate elements between 1 to n; and size of array is n

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92955/Python-4-lines-with-short-explanation

```python
def findDisappearedNumbers(self, nums):

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
```
