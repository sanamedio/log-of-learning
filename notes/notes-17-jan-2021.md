# 17-jan-2021

### 9 - invert binary tree iterative

https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python

```python
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root
```

### 8 - adding comma separated values to list

probably it's converting the rhs to tuple first and then iterating, but seemed very weird for first time

```python
>>> s = []
>>> s += 1,2
>>> s
[1, 2]
>>> s += 3,4,5
>>> s
[1, 2, 3, 4, 5]
>>> s += 7,8,
>>> s
[1, 2, 3, 4, 5, 7, 8]
>>>
```

### 6 - LCA on a binary search tree

due to bst property its easier than the general tree problem
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/

```python
def lowestCommonAncestor(self, root, p, q):

    p_val = p.val
    q_val = q.val
    node = root

    while node:
        parent_val = node.val

        if p_val > parent_val and q_val > parent_val:    
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            node = node.left
        else:
            return node
```

### 5 - diameter of a binary tree

```python
def diameterOfBinaryTree(self, root):
    self.ans = 1
    def depth(node):
        if not node: return 0
        L = depth(node.left)
        R = depth(node.right)
        self.ans = max(self.ans, L+R+1)
        return max(L, R) + 1

    depth(root)
    return self.ans - 1
```

### 4 - find whether meeting can be scheduled

https://leetcode.com/discuss/interview-question/613816/Google-or-Onsite-or-Meeting-Rooms-3

the overall implementation by the author looks cool - using defaultdict, bisect_left, bisect_right etc.

```python
import bisect
class SegmentTree:
    def __init__(self, n):
        self.tree = [0]*(n*4+10)
        self.n = n

    def update(self, pos, left, right, idx, val):
        if idx < left or idx > right:
            return
        if left == right:
            self.tree[pos] = val
            return
        mid = (left+right)//2
        self.update(pos*2+1,left,mid,idx,val)
        self.update(pos*2+2,mid+1,right,idx,val)
        self.tree[pos] = max(self.tree[pos*2+1],self.tree[pos*2+2])
        return

    def query(self, pos, left, right, ql, qr):
        if qr < left or ql > right:
            return 0
        if ql <= left and qr >= right:
            return self.tree[pos]
        mid = (left+right)//2
        return max(self.query(pos*2+1,left,mid,ql,qr), self.query(pos*2+2,mid+1,right,ql,qr))


class Solution(object):
    def isAvaiblable(self, calender, rooms, queries):
        cnt = defaultdict(int)
        for start, end in calender:
            cnt[start] += 1
            cnt[end] -= 1
        times = sorted(cnt)
        intervals = [0]
        for t in times:
            intervals.append(cnt[t]+intervals[-1])

        # print(times,intervals)
        n = len(intervals)
        T = SegmentTree(n)
        for i, v in enumerate(intervals):
            T.update(0,0,n-1,i,v)
        res = []
        for start, end in queries:
            ql = bisect.bisect_right(times,start)
            qr = bisect.bisect_left(times,end)
            # print(start, end, ql,qr)
            # res.append(max([intervals[i] for i in range(ql,qr+1)]) < rooms)
            res.append(T.query(0,0,n-1,ql,qr) < rooms)

        return res


import unittest

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        calender = [[1, 2], [4, 5], [8, 10]]
        rooms = 1
        queries = [[2, 3], [3, 4]]
        output = [True, True]
        test = Solution()
        self.assertEqual(test.isAvaiblable(calender,rooms,queries), output)

    def test_2(self):
        calender = [[1, 2], [4, 5], [8, 10]]
        rooms = 1
        queries = [[4, 5], [5, 6]]
        output = [False, True]
        test = Solution()
        self.assertEqual(test.isAvaiblable(calender,rooms,queries), output)

    def test_3(self):
        calender = [[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]]
        rooms = 3
        queries = [[1, 9], [2, 6], [7, 9], [3, 5], [3, 9], [2, 4], [7, 10], [5, 9], [3, 10], [9, 10]]
        output = [False, True, False, True, False, True, False, False, False, True]
        test = Solution()
        self.assertEqual(test.isAvaiblable(calender,rooms,queries), output)


if __name__ == '__main__':
    unittest.main()
```

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
