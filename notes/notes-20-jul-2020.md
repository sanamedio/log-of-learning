# 20-jul-2020

### 2 - bottom view of binary tree

https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

```python
def bottomView(root):
    '''
    :param root: root of the binary tree
    :return: list containing the bottom view from left to right
    '''
    if not root:
        return []
    # code here
    m = {}
    def x(s,y,level):
        if not s:
            return
        
        if y not in m or ( y in m and m[y][1] <= level):
            m[y]=(s.data,level)
        
        x(s.left,y-1,level+1)
        x(s.right,y+1,level+1)
    
    x(root,0,0)
    result = []
    mn = min(m.keys())
    mx = max(m.keys())

    for i in range(mn,mx+1):
        result+= [m[i][0]]
    return result
```

### 1 - usefulness of comparators

- https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

```python
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return (( int(ba) > int(ab) ) - (int(ba) < int(ab)))


def myCompare(mycmp):

    class K(object):

        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


if __name__ == "__main__":
    a = [34234,1231,43,4123,23,24,23423]
    sorted_array = sorted(a, key=myCompare(comparator))
    number = "".join([str(i) for i in sorted_array])
    print(number)
```
