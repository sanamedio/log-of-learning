# 29-dec-2020


### 1 - online sorted list using bisect

In this problem, we have to keep adding items to a DS and return online if there are any two in the DS which sum to val
bisect can be used to keep a sorted list, did not know that earlier

```python
class TwoSumOnline:
    def __init__(self):
        from collections import defaultdict
        self.m = defaultdict(int)
        self.d = []

    def add(self, val):
        self.m[val]+=1
        import bisect    
        self.d.insert(bisect.bisect(self.d,val),val)

    def find(self, val):
        
        d = self.d

        left = 0
        right = len(d)-1
        while left<right:
            if d[left] + d[right] == val:
                return True
            elif d[left] + d[right] > val:
                right-=1
            else:
                left+=1
        
        return False
```
