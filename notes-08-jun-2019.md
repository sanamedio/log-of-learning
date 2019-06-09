# 08-jun-2019

### 2 - finding bitwise and of a range

https://www.geeksforgeeks.org/bitwise-and-or-of-a-range/

boring method
```python
import functools
M = 8
N = 15
print(functools.reduce(  lambda x,y: x & y, range(M,N) ))
```
better approach
```python
# finding bitwise and of a range
# if the numbers differ in the binary sizes or the position of MSB bit - leftmost bit, it means there will be a number in between which will have lot of tailing zeroes and one 1 in the left.. which will nullify the smaller number, and beyond that the padding zeroes of the smaller number will nullify the larger number
# so, 



M , N = [ int(x.strip()) for x in input().strip().split() ]

def get_msb(x):
    return len(bin(x)[2:])


result  = 0

while M and N: #both are not zero

    if get_msb(M) == get_msb(N):
        x = pow(2,get_msb(M)-1)
        result += x
        M -= x
        N -= x
    else:
        break


print(result)
```






### 1 - building grep with keras 99.57% accuracy


learner.py
```python
import random
import string
import os


TOTAL_SAMPLES=10000
CONTENT_LENGTH = 10
REGEX_LENGTH = 4
LANGUAGE='0123456789'
N_CLASSES=2

def randString(length):
    your_letters=LANGUAGE
    return ''.join((random.choice(your_letters) for i in range(length)))

print("generating...")

l = []

cnt = 0
zeros = 0 



def generate_case(t,*v):
    temp = ''.join([ t[vv] for vv in v])
    #print(temp)
    if temp not in t:
        return t+temp
    return None






for i in range(TOTAL_SAMPLES):
    t = randString(CONTENT_LENGTH)

    
    for i in range(CONTENT_LENGTH-REGEX_LENGTH+1):
        l += [ ( t + t[i:i+REGEX_LENGTH], 1)]
        #print(t+t[i:i+REGEX_LENGTH],1)
        cnt+=1
   

    if generate_case(t,2,3,5,9):
        l += [ (generate_case(t,2,3,5,9),0)]
        zeros+=1


    if generate_case(t,0,1,8,9):
        l += [ (generate_case(t,0,1,8,9),0)]
        zeros+=1


    if (t[0:2] + t[4:6]) not in t:
        l+= [ (t + t[0:2] + t[4:6],0 )]
        zeros+=1


    if (t[1:3] + t[4:6]) not in t:
        l+= [ (t + t[1:3] + t[4:6],0 )]
        zeros+=1


    if (t[4:6] + t[0:2]) not in t:
        l+= [ (t + t[4:6] + t[0:2],0 )]
        zeros+=1


    if (t[4:6] + t[1:3]) not in t:
        l+= [ (t + t[4:6] + t[1:3],0 )]
        zeros+=1
    
    if (t[0]+t[2] + t[4] + t[6] ) not in t:
        l += [ (t + t[0] + t[2] + t[4] + t[6]  , 0 )]
        zeros+=1
    
    if (t[6] + t[4] + t[2] + t[0] ) not in t:
        l += [  ( t + t[6] + t[4] + t[2] + t[0] , 0 )]
        zeros+=1

    if (t[1] + t[3] + t[5] + t[7] ) not in t:
        l += [ ( t + t[1] + t[3] + t[5] + t[7] , 0 )]
        zeros +=1

    if (t[7] + t[5] + t[3] + t[1] ) not in t:
        l += [ (t + t[7] + t[5] + t[3] + t[1] , 0 )]
        zeros +=1

   

    if (t[1:3] + t[7:9]) not in t:
        l+= [ (t + t[1:3] + t[7:9],0 )]
        zeros+=1


    if (t[0:2] + t[7:9]) not in t:
        l+= [ (t + t[0:2] + t[7:9],0 )]
        zeros+=1


    if (t[4:6] + t[7:9]) not in t:
        l+= [ (t + t[4:6] + t[7:9],0 )]
        zeros+=1


    if (t[7:9] + t[1:3]) not in t:
        l+= [ (t + t[7:9] + t[1:3],0 )]
        zeros+=1
    
    if (t[2]+t[4] + t[6] + t[8] ) not in t:
        l += [ (t + t[2] + t[4] + t[6] + t[8]  , 0 )]
        zeros+=1
    
    if (t[8] + t[4] + t[2] + t[6] ) not in t:
        l += [  ( t + t[8] + t[4] + t[2] + t[6] , 0 )]
        zeros+=1

    if (t[3] + t[5] + t[7] + t[9] ) not in t:
        l += [ ( t + t[3] + t[5] + t[7] + t[9] , 0 )]
        zeros +=1

    if (t[9] + t[7] + t[5] + t[3] ) not in t:
        l += [ (t + t[9] + t[7] + t[5] + t[3] , 0 )]
        zeros +=1








    for _ in range(CONTENT_LENGTH-REGEX_LENGTH+1): #to max sure samples are equal
        while True:
            m = randString(REGEX_LENGTH)
            if m not in t:
                l += [( t +m  ,0)]
                #print(t+m,0)
                zeros+=1
                break


print(cnt, zeros)


def convertToPoints(s):
    lt = []
    for c in s:
        for ch in LANGUAGE:
            if c == ch:
                lt += [1]
            else:
                lt += [0]
    return lt

print("converting...")

d =  [ convertToPoints(x[0]) + [x[1]] for x in l ]

import pandas as pd 
dataset = pd.DataFrame(d)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

from sklearn.model_selection import train_test_split

trainingSet, testSet = train_test_split(dataset, test_size=0.1)


print(trainingSet)
print(testSet)



INPUT_DIM = len(LANGUAGE)*(REGEX_LENGTH+CONTENT_LENGTH)

X_train = trainingSet.iloc[:,0:INPUT_DIM]
y_train = trainingSet.iloc[:,INPUT_DIM]
X_test = testSet.iloc[:,0:INPUT_DIM]
y_test = testSet.iloc[:,INPUT_DIM]


print("X_train shape", X_train.shape)
print("y_train shape", y_train.shape)
print("X_test shape", X_test.shape)
print("y_test shape", y_test.shape)


n_classes = N_CLASSES

#Y_train = np_utils.to_categorical(y_train, n_classes)
#Y_test = np_utils.to_categorical(y_test, n_classes)

Y_train = y_train
Y_test = y_test



print(Y_train)
print(Y_test)



model = Sequential()




model.add(Dense(512, input_shape=(INPUT_DIM,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))


model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))



model.add(Dense(1))
model.add(Activation('sigmoid'))
print(model)




#model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam' )
model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='adam' )


# training the model and saving metrics in history
history = model.fit(X_train, Y_train,
          batch_size=128, epochs=20,
          verbose=2,
          validation_data=(X_test, Y_test))

# saving the model
save_dir = "results/"
model_name = 'keras_grep.h5'
model_path = os.path.join(save_dir, model_name)
model.save(model_path)
print('Saved trained model at %s ' % model_path)





grep_model = load_model("results/keras_grep.h5")
loss_and_metrics = grep_model.evaluate(X_test, Y_test, verbose=2)
print("Test Loss", loss_and_metrics[0])
print("Test Accuracy", loss_and_metrics[1])
```





