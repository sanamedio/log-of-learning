# 19-dec-2018


### 1 - finding length of maximum common subsequence with recursion and memorization

- idea is to start from the right of the arrays and find the common pairs
- at each common pair, recurse over a subproblem
- seems like a n^2*m^2 complexity approach, but improvement over the bruteforce exponential time algorithm
- what can be done better?  that for loop can be rethought. amongst different recursive subproblems; that will overlap

```python
saved = {}


def recurse(A,B,a,b ):


    print(A,B,a,b)

    if a == -1:
        return 0
    elif b == -1:
        return 0
    else:

        global saved
        if (a,b) in saved:
            return saved[(a,b)]


        temp = 0
        for i in range(a,-1,-1):
            for j in range(b,-1,-1):
                x = A[i]
                y = B[j]

                if x == y :
                    print("comparing : ", x , y )
                    temp= max(temp, 1 + recurse(A,B,i-1,j-1))

        saved[(a,b)] = temp
        return saved[(a,b)]






if __name__ == '__main__':

    print( recurse([1,2,3,4,5,6],[5,0,0,0,6],5,4))
```
