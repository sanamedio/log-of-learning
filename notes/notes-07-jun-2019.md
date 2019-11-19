# 07-jun-2019


### 2 - building grep using keras part 2

learner.py
```python
import random
import string
import os


TOTAL_SAMPLES=100000
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

for i in range(TOTAL_SAMPLES):
    t = randString(CONTENT_LENGTH)

    
    for i in range(CONTENT_LENGTH-REGEX_LENGTH+1):
        l += [ ( t + t[i:i+REGEX_LENGTH], 1)]
        print(t+t[i:i+REGEX_LENGTH],1)
        cnt+=1
    
    for _ in range(CONTENT_LENGTH-REGEX_LENGTH+1): #to max sure samples are equal
        while True:
            m = randString(REGEX_LENGTH)
            if m not in t:
                l += [( t +m  ,0)]
                print(t+m,0)
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

trainingSet, testSet = train_test_split(dataset, test_size=0.2)


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

Y_train = np_utils.to_categorical(y_train, n_classes)
Y_test = np_utils.to_categorical(y_test, n_classes)



model = Sequential()
model.add(Dense(512, input_shape=(INPUT_DIM,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))


model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))



model.add(Dense(2))
model.add(Activation('softmax'))
print(model)



model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam' )



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


'''
# plotting the metrics
fig = plt.figure()
plt.subplot(2,1,1)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')

plt.subplot(2,1,2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')

plt.tight_layout()
'''



grep_model = load_model("results/keras_grep.h5")
loss_and_metrics = grep_model.evaluate(X_test, Y_test, verbose=2)
print("Test Loss", loss_and_metrics[0])
print("Test Accuracy", loss_and_metrics[1])

```

tester.py
```python

import pandas as pd 

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

from sklearn.model_selection import train_test_split

import string


LANGUAGE='0123456789'

def convertToPoints(s):
    lt = []
    for c in s:
        for ch in LANGUAGE:
            if c == ch:
                lt += [1]
            else:
                lt += [0]
    return lt




grep_model = load_model("results/keras_grep.h5")

input_string = input("content >> ").strip()[:10]

while True:
    
    grep_string = input("regex >> ").strip()[:4]


    if  len( input_string + grep_string ) != 14:
        continue

    x = pd.DataFrame(convertToPoints(input_string + grep_string)).transpose()


    print(grep_model.predict_classes(x))

```

### 1 - building grep using keras

tried to teach a neural net how to grep from a string

```python
import random
import string
import os


def randString(length=5):
    your_letters='abcdefghi'
    return ''.join((random.choice(your_letters) for i in range(length)))



l = []


print("generating...")

for i in range(10000):
    t = randString(10)
    l += [ ( t + t[0:4], 1)]
    l += [ ( t + t[4:8], 1)]
    m = randString(4)
    if m not in t:
        l += [( t +m  ,0)]

def convertToPoints(s):
    l = []
    for c in s:
        for ch in string.ascii_lowercase:
            if c == ch:
                l += [1]
            else:
                l += [0]
    return l

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

trainingSet, testSet = train_test_split(dataset, test_size=0.2)


print(trainingSet)
print(testSet)




X_train = trainingSet.iloc[:,0:364]
y_train = trainingSet.iloc[:,364]
X_test = testSet.iloc[:,0:364]
y_test = testSet.iloc[:,364]


print("X_train shape", X_train.shape)
print("y_train shape", y_train.shape)
print("X_test shape", X_test.shape)
print("y_test shape", y_test.shape)

#X_train = X_train.astype('float32')
#X_test = X_test.astype('float32')

n_classes = 2

print("Shape before one-hot encoding: ", y_train.shape)
Y_train = np_utils.to_categorical(y_train, n_classes)
Y_test = np_utils.to_categorical(y_test, n_classes)
print("Shape after one-hot encoding: ", Y_train.shape)



model = Sequential()
model.add(Dense(512, input_shape=(364,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))


model.add(Dense(2))
model.add(Activation('softmax'))
print(model)



model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam' )



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

# plotting the metrics
fig = plt.figure()
plt.subplot(2,1,1)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')

plt.subplot(2,1,2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')

plt.tight_layout()




grep_model = load_model("results/keras_grep.h5")
loss_and_metrics = grep_model.evaluate(X_test, Y_test, verbose=2)
print("Test Loss", loss_and_metrics[0])
print("Test Accuracy", loss_and_metrics[1])



# In[22]:
'''

predicted_classes = grep_model.predict_classes(X_test)

# see which we predicted correctly and which not
correct_indices = np.nonzero(predicted_classes == y_test)[0]
incorrect_indices = np.nonzero(predicted_classes != y_test)[0]
print()
print(len(correct_indices)," classified correctly")
print(len(incorrect_indices)," classified incorrectly")

'''


while True:
    input_string = input("content >> ").strip()[:10]
    
    grep_string = input("regex >> ").strip()[:4]


    if  len( input_string + grep_string ) != 14:
        continue

    x = pd.DataFrame(convertToPoints(input_string + grep_string)).transpose()


    print(grep_model.predict_classes(x))
```






