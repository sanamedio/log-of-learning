# 27-nov-2019

### 3 - pip can directly work on URLS!

```python
pip install https://github.com/mitsuhiko/flask/tarball/master
```

### 2 - dutch national flag 3-way sort

nice stuff

```python

a = [2,2,2,1,1,1,0]

N = len(a)


l, m , h  = 0 , 0 , N-1




while m <= h:
    if a[m] == 0:
        a[l] , a[m] = a[m], a[l]
        l = l + 1
        m = m + 1
    elif a[m] == 1:
        m  = m + 1
    elif a[m] == 2:
        a[m] , a[h] = a[h], a[m]
        h = h - 1


print(a)
```


### 1 - Pseudo random numbers

I think randomness is both an easy and a difficult concept. It's easy to talk about it casually, but when you go into definition of things millions of questions arise. Been experimenting with distribution of random numbers while generating via python from random.random() function, and their correlation with the previously generated keys. What I did in this experiment is to try to predict next number generated in the sequence. I took two plots, one where I have used the same seeeds in the PRNG and second where I let the seed by system timestamp. The results were clearly showing the there is certain level of predictability which can be easily exploited to predict next number of the sequence.

```python3

def get_prob(set_size, ngram_size , num_samples, seeded=True):


    import random
    import sys
    from collections import defaultdict



    if seeded:
        random.seed(0)

    NUM_SET = set_size
    k = ngram_size

    training_data = [ int(random.random()*NUM_SET) for _ in range(int(num_samples)) ]
    frequency_stats = defaultdict(int)

    for i in range(k,len(training_data)):
        key =  "_".join([ str(x) for x in training_data[i-k:i]]) 
        if key in frequency_stats:
            frequency_stats[key][training_data[i]]+=1
        else:
            frequency_stats[key] = { i:0 for i in range(set_size) } 


    if seeded:
        random.seed(0)

    test_data = [int(random.random()*NUM_SET) for _ in range(int(num_samples)) ]

    success = 0

    for i in range(k, len(test_data)):

        key = "_".join([ str(x) for x in test_data[i-k:i] ])

        if key in frequency_stats:
            m = frequency_stats[key]
            prediction = max(m,key=m.get)

            if prediction == test_data[i]:
                success+=1



    return (success/(len(test_data)-k))




        
p1 = [ [ get_prob(i,j,100,seeded=True)  for i in range(2,12)] for j in range(2,22)]
p2 = [ [ get_prob(i,j,100,seeded=False) for i in range(2,12)] for j in range(2,22)]

import numpy as np
import matplotlib.pyplot as plt


f, axarr = plt.subplots(1,2)



H1 = np.array(p1)
axarr[0].imshow(H1,cmap='gray')

H2 = np.array(p2)
axarr[1].imshow(H2,cmap='gray')


plt.show()
```
