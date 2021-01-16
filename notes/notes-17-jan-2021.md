# 17-jan-2021

### 3 - divide and conquer approach for maxSubarraySum 

https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/

```python
def maxCrossingSum(arr, l, m, h) : 
      
    sm = 0; left_sum = -10000
      
    for i in range(m, l-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > left_sum) : 
            left_sum = sm 
      
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 
          
        if (sm > right_sum) : 
            right_sum = sm 
      
  
    return max(left_sum + right_sum, left_sum, right_sum) 
  
def maxSubArraySum(arr, l, h) : 
      
    if (l == h) : 
        return arr[l] 
  
    # Find middle point 
    m = (l + h) // 2
  
    return max(maxSubArraySum(arr, l, m), 
               maxSubArraySum(arr, m+1, h), 
               maxCrossingSum(arr, l, m, h)) 
```


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
