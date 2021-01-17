# 17-jan-2021

### 19 - LIS nlogn

https://www.youtube.com/watch?v=1RpMc3fv0y4

https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation

```python
def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
```

### 18 - maximum product subarray

https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity

```python
int maxProduct(int A[], int n) {
    int r = A[0];

    for (int i = 1, imax = r, imin = r; i < n; i++) {
        // multiplied by a negative makes big number smaller, small number bigger
        // so we redefine the extremums by swapping them
        if (A[i] < 0)
            swap(imax, imin);

        // max/min product for the current number is either the current number itself
        // or the max/min by the previous number times the current one
        imax = max(A[i], imax * A[i]);
        imin = min(A[i], imin * A[i]);

        r = max(r, imax);
    }
    return r;
}
```

### 17 - subset sum while removing duplicates

sorting plus handling duplicates reduces the memory usage. no need of separate set to avoid overcounting

https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments

```python
def combinationSum2(self, candidates, target):
    candidates.sort()                      
    result = []
    self.combine_sum_2(candidates, 0, [], result, target)
    return result
    
def combine_sum_2(self, nums, start, path, result, target):
    if not target:
        result.append(path)
        return
    
    for i in xrange(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue

        if nums[i] > target:
            break

        self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                           result, target - nums[i])
```

### 16 - rotating matrix in different ways

https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

```python
class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]
```

```python
class Solution:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
```

```python
class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for j in range(n/2):
                row[j], row[~j] = row[~j], row[j]
```

### 15 - matrix spiral order

this is so elegant one-liner in python
https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby

```python
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
```

### 14 - set row col zero

set-matrix-zero from leetcode

a general theme accross space optimization is to use the same input structure to store state

https://leetcode.com/problems/set-matrix-zeroes/discuss/26014/Any-shorter-O(1)-space-solution

```python
void setZeroes(vector<vector<int> > &matrix) {
    int col0 = 1, rows = matrix.size(), cols = matrix[0].size();

    for (int i = 0; i < rows; i++) {
        if (matrix[i][0] == 0) col0 = 0;
        for (int j = 1; j < cols; j++)
            if (matrix[i][j] == 0)
                matrix[i][0] = matrix[0][j] = 0;
    }

    for (int i = rows - 1; i >= 0; i--) {
        for (int j = cols - 1; j >= 1; j--)
            if (matrix[i][0] == 0 || matrix[0][j] == 0)
                matrix[i][j] = 0;
        if (col0 == 0) matrix[i][0] = 0;
    }
}
```

### 13 - majority element in many ways

https://leetcode.com/problems/majority-element/solution/

bayers moore algo
```python
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```

divide and conquer
```python
def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
```

randomized algo with o(inf)
```python
import random

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
```


### 12 - longest word trie

This is just black magic; how the fuck someone came with this short approach to build trie

https://leetcode.com/problems/longest-word-in-dictionary/solution/

```python
def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
```

### 11 - backspaced strings compare

liked how reduce is used to apply backspace operation to both strings

https://leetcode.com/problems/backspace-string-compare/discuss/135603/JavaC%2B%2BPython-O(N)-time-and-O(1)-space

```python
# $ denotes deletion operation
def backspaceCompare(self, S, T):
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
return reduce(back, S, []) == reduce(back, T, [])
```


### 10 - sorted squares 

use of two points to keep a sorted list even after squaring

initial input can be -2, -1, 3 , 4

output will be like 1 3 4 4

https://leetcode.com/problems/squares-of-a-sorted-array/discuss/221922/Java-two-pointers-O(N)
```java
public int[] sortedSquares(int[] A) {
        int n = A.length;
        int[] result = new int[n];
        int i = 0, j = n - 1;
        for (int p = n - 1; p >= 0; p--) {
            if (Math.abs(A[i]) > Math.abs(A[j])) {
                result[p] = A[i] * A[i];
                i++;
            } else {
                result[p] = A[j] * A[j];
                j--;
            }
        }
        return result;
    }
```

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
