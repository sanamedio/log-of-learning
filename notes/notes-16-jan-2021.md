# 16-jan-2021

### 2 - making ranges non-overlapping

minimum number of ranges to remove to make the set non-overlapping
https://www.geeksforgeeks.org/minimum-removals-required-to-make-ranges-non-overlapping/

```python
def minRemovels(ranges):

    size = len(ranges)
    rem = 0

    ranges.sort()

    end = ranges[0][1]
    for i in range(1, size):

        if ranges[i][0] < end:

            rem += 1

            end = min(ranges[i][1], end)

        else:
            end = ranges[i][1]

    return rem
```


### 1 - finding longest streak from an array

the idea is similar to traversal but somehow did not intutively clicked initially
https://afteracademy.com/blog/longest-consecutive-sequence

```cpp
int longestConsecutiveSequence(int A[], int n)
{
    int longest_streak = 0
    Create HashTable H of size n
    for( i = 0 to n-1 )
        H.add(A[i])
    for( i = 0 to n-1 )
    {
       // This checks if the current element is the first
       // element of a sequence
        if( H.search(A[i]-1) == False )
        {
            int curr_streak = 1
            int curr_num = A[i]+1
            while( H.search(A, curr_num) == True )
            {
               curr_streak = curr_streak + 1
               curr_num = curr_num + 1
            }
            longest_streak = max(longest_streak, curr_streak)
        }
    }
   return longest_streak
}
```
