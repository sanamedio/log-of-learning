# 29-jan-2019

### 2 - radix sort

```python

def radix_sort(l):
    max_len = max([ len(str(x)) for x in l])
    rlist = [ str(x).zfill(max_len)[::-1]  for x in l ]

    for i in range(max_len):
        rlist = sorted( rlist, key=lambda x: x[i])


    rlist = [ int(x[::-1]) for x in rlist ]
    return rlist




if __name__ == '__main__':



    ans = radix_sort([2312,423,234,4,233423,43])
    print(ans)


```


### 1 - partitions of a integer

- partitions of a number

```python

def recurse(num,l):
    if num == 1:
        print( l + [1])
    else:
        for i in range(1,num+1):
            recurse(num-i, l + [i] )


if __name__ == '__main__':
    recurse(int(input()),[])


```
