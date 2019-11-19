# 05-jun-2019


### 2 - finding solutions through graphing

https://doisinkidney.com/posts/2019-06-04-solving-puzzles-without-your-brain.html

```python
def sequence(n,m):
    while n != m:
        yield (n,m)
        if n < m:
            m -= n
            n *= 2
        else:
            n -= m
            m *= 2

def loops(xs):
    seen = set()
    for x in xs:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False

def solution(n,m):
    return loops(sequence(n,m))


print(
    '\n'.join(
        ''.join(
            '*' if solution(x,y) else ' '
            for x in range(1,81)
        )
        for y in range(100,0,-1)
    )
)
```


### 1 - stack, heap, and code virtual locations

- from book OS three easy pieces

```C
#include <stdio.h>
#include <stdlib.h>

int main(){

	printf("code : %p\n",(void *) main);
	printf("heap : %p\n",(void *) malloc(1));
	int x = 3;
	printf("stack: %p\n",(void *) &x);

}
```
