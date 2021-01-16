# 16-jan-2021

### 1 - finding longest streak from an array

the idea is similar to traversal but somehow did not intutively clicked initially

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
