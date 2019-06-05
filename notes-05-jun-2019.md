# 05-jun-2019


### 1 - stack, heap, and code virtual locations

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
