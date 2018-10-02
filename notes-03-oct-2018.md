# python-notes - 03-oct-2018

### 7 - versions 

```python
>>> from distutils.version import StrictVersion
>>> versions = ['1.3.12', '1.3.3', '1.2.5', '1.2.15', '1.2.3', '1.2.1']
>>> versions.sort(key=StrictVersion)
>>> print versions
['1.2.1', '1.2.3', '1.2.5', '1.2.15', '1.3.3', '1.3.12']
```

```python
>> l = ['v1.3.12', 'v1.3.3', 'v1.2.5', 'v1.2.15', 'v1.2.3', 'v1.2.1']
>>> l.sort(key=LooseVersion)
>>> l
['v1.2.1', 'v1.2.3', 'v1.2.5', 'v1.2.15', 'v1.3.3', 'v1.3.12']
```

### 6 - Python HTTP and SMTP servers

```bash
 python3 -m http.server
 ```
 ```bash
 python -m SimpleHTTPServer
 ```
 ```bash
 python -m smtpd -c DebuggingServer -n
 ```

### 5 - Removes duplicates while maintaining order

```python
from collections import OrderedDict
x = [1, 8, 4, 5, 5, 5, 8, 1, 8]
list(OrderedDict.fromkeys(x))
```

### 4 - itertools groupby

```python
from itertools import groupby

data = [
    {'animal': 'dog', 'name': 'Roxie', 'age': 5},
    {'animal': 'dog', 'name': 'Zeus', 'age': 6},
    {'animal': 'dog', 'name': 'Spike', 'age': 9},
    {'animal': 'dog', 'name': 'Scooby', 'age': 7},
    {'animal': 'cat', 'name': 'Fluffy', 'age': 3},
    {'animal': 'cat', 'name': 'Oreo', 'age': 5},
    {'animal': 'cat', 'name': 'Bella', 'age': 4}   
    ]

for key, group in groupby(data, lambda x: x['animal']):
    for thing in group:
        print(thing['name'] + " is a " + key)
```

### 3 - pprint

```python
import pprint as pp
animals = [{'animal': 'dog', 'legs': 4, 'breeds': ['Border Collie', 'Pit Bull', 'Huskie']}, {'animal': 'cat', 'legs': 4, 'breeds': ['Siamese', 'Persian', 'Sphynx']}]
pp.pprint(animals, width=1)
```

### 2 - Calling external command in python

```python
import subprocess
subprocess.call(['mkdir', 'empty_folder'])
```
```python
import subprocess
output = subprocess.check_output(['ls', '-l'])
```
```python
import subprocess
output = subprocess.call(['cd', '/'], shell=True)
```

### 1 - Flask simple app

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there!"
if __name__ == '__main__':
    app.run(debug=True)
```





