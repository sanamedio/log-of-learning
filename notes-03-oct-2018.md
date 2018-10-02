# python-notes - 03-oct-2018

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
