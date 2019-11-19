# 04-nov-2018

### 15 - better_exceptions module

- Shows values of variables in stacktrace, very useful
```bash
pip install better_exceptions
export BETTER_EXCEPTIONS=1
python test.py
```

for interactive prompt:
```bash
python -m better_exceptions
```

- https://github.com/Qix-/better-exceptions

### 14 - simple reactive dashboards in python using dash

- https://github.com/pydata/pandas-datareader 
- https://github.com/plotly/dash

```python
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Hello World')

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2017, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
        app.run_server()
```


### 13 - StringIO vs BytesIO (from SO)

- StringIO works with str data, while BytesIO works with bytes data. bytes are raw data, e.g. 65, while str interprets this data, e.g. using the ASCII encoding 65 is the letter 'A'.
- bytes data is preferable when you want to work with data agnostically - i.e. you don't care what is contained in it. For example, sockets only transmit raw bytes data.
- str is used when you want to present data to users, or interpret at a higher level. For example, if you know that a file contains text, you can directly interpret the raw bytes as text.


### 12 - iterators use c recusion stack

```python
i=''
for _ in range(9**6):i=filter(int,i)
del i
```

### 11 - crashing using marshal

- According to python wiki this should cause seg fault, but on my system it hangs everything down and causes a restart later on. It is trying to load data from random places in memory. I think behaviour will be dependent on random numbers. DONT USE THIS IT CAUSES CRASH OF OS
- https://wiki.python.org/moin/CrashingPython

```python
  >>> import os, marshal
    >>> while True:
    ...     try:
    ...         marshal.loads(os.urandom(16))
    ...     except:
    ...         pass
    ... 
    #(caused my system to hang : ubuntu 16 linux )
```

### 10 - tracing program execution using -m trace

- very useful to see each line of python code executing and subsequence program behaviour. But can't change the values in between. for that use pdb

```bash
python3 -u -m trace -t test.py
```


### 9 - segfault using ctypes 

```python
Python 3.7.0 (default, Nov  4 2018, 00:07:25) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ctypes
>>> p = ctypes.pointer(ctypes.c_char.from_address(5))
>>> p[0] = b'x'
Segmentation fault (core dumped)
```

```python
>>> import ctypes; ctypes.string_at(1)
Segmentation fault (core dumped)
```

### 8 - segfault in python recursion

```python
>>> import sys
>>> sys.setrecursionlimit(1<<30)
>>> f = lambda f : f(f)
>>> f(f)
Segmentation fault (core dumped)
```

### 7 - Elementary cellular automata plotted using matplotlib

- TODO: improve the code later!

```python
import sys;


if len(sys.argv) >= 5:
	RULE = int(sys.argv[1])
	WIDTH = int(sys.argv[2])
	HEIGHT = int(sys.argv[3])
	TIME = float(sys.argv[4])
elif len(sys.argv) == 4:
	RULE = int(sys.argv[1])
	WIDTH = int(sys.argv[2])
	HEIGHT = int(sys.argv[3])
	TIME = 0.1
elif len(sys.argv) == 3:
	RULE = int(sys.argv[1])
	WIDTH = int(sys.argv[2])
	HEIGHT = 100
	TIME = 0.1
elif len(sys.argv) == 2:
	RULE = int(sys.argv[1])
	WIDTH = 100
	HEIGHT = 100
	TIME = 0.1
else:
	RULE = 150
	WIDTH = 100
	HEIGHT = 100
	TIME = 0.1
	

binary_rule = format(RULE, '08b')

def get_next_row(binary_rule,windo):
	
	for i,v in enumerate(reversed(binary_rule)):
		if v  == '1':
			prec = format(i,'03b')

			if prec == windo:
				return '1'

	return '0'
			




def print_blocks(x):
	for i in x :
		if i == '0':
			print(bytes((219,)).decode('cp437'),end='')
		else:
			print(' ',end='')
	print('')



print('binary rule : ' +  binary_rule)
	

for i,v in enumerate(reversed(binary_rule)):
	print(  format(i,'03b') + " -> " + v )



tstr = "0"*WIDTH + "1" + "0"*WIDTH


#print(tstr)
#print_blocks(tstr)

array_twod = []

iterations = 0

import time
while True:
	if iterations > HEIGHT:
		break
	iterations = iterations + 1

	array_twod += [ [ float(x) for x in tstr] ]
	result = ""
	for i in range(len(tstr)):
		temp_str = tstr
		if i ==0 :
			result = result + get_next_row( binary_rule , temp_str[-1] + temp_str[0] + temp_str[1] )
		elif i == len(tstr)-1:
			result = result + get_next_row( binary_rule , temp_str[i-1] + temp_str[i] + temp_str[0] )	
		else:
			result  = result +  get_next_row(binary_rule,temp_str[i-1:i+2])

			
	#print_blocks(result)
	tstr = result
	#time.sleep(TIME)



def plotme(x):
	import matplotlib.pyplot as plt 
	import numpy as np 
 
	a = np.array(x)
	#print(a) 
	plt.imshow(a, cmap='hot') 
	plt.show()


plotme(array_twod)
```


### 6 - Elementary cellular automata in python

- http://mathworld.wolfram.com/ElementaryCellularAutomaton.html

```python
import sys;
RULE = int(sys.argv[1])
TIME = float(sys.argv[2])

binary_rule = format(RULE, '08b')

def get_next_row(binary_rule,windo):
	
	for i,v in enumerate(reversed(binary_rule)):
		if v  == '1':
			prec = format(i,'03b')

			if prec == windo:
				return '1'

	return '0'
			




def print_blocks(x):
	for i in x :
		if i == '0':
			print(bytes((219,)).decode('cp437'),end='')
		else:
			print(' ',end='')
	print('')



print('binary rule : ' +  binary_rule)
	

for i,v in enumerate(reversed(binary_rule)):
	print(  format(i,'03b') + " -> " + v )



tstr = "0"*70 + "1" + "0"*70


print(tstr)
print_blocks(tstr)

import time
while True:
	result = ""
	for i in range(len(tstr)):
		temp_str = tstr
		if i ==0 :
			result = result + get_next_row( binary_rule , temp_str[-1] + temp_str[0] + temp_str[1] )
		elif i == len(tstr)-1:
			result = result + get_next_row( binary_rule , temp_str[i-1] + temp_str[i] + temp_str[0] )	
		else:
			result  = result +  get_next_row(binary_rule,temp_str[i-1:i+2])

			
	print_blocks(result)
	tstr = result
	time.sleep(TIME)

## call the program with some arguments like 150 0.1, where 150 will be cellular automata id, and 0.1 is time between rendering each line, speed of simulation
```

### 5 - prime numbers with lambda

```python
>>> nums = range(100)
>>> for i in range(2,10):
...     nums = list( filter(lambda x : x == i or x %i , nums))
... 
>>> nums
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> 
```

### 4 - Flask uses Werkzeug internally

```python
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
	return Response('Hello world')


if __name__ == "__main__":
	from werkzeug.serving import run_simple
	run_simple('localhost', 4000, application)
```


### 3 - Flask JWT example

- https://pythonhosted.org/Flask-JWT/

```python
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity



app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']
app.secret_key = 'loki'
api = Api(app)


class User(object):
    def __init__(self, id , username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id 

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz')
]

username_table = { u.username: u for u in users}
userid_table = { u.id: u for u in users }

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password.encode('utf-8') ==   password.encode('utf-8'):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)




jwt = JWT(app, authenticate, identity)

items = [

	{ 'name' : 'foo' , 'price' : 1} ,
	{ 'name' : 'bar' ,  'price' : 2} 
]


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        return {'item' : next( filter(lambda x : x['name' == name, items])  , None)} 

    
    @jwt_required()
    def post(self, name):
        if next(filter(lambda x : x['name']== name, items),None) is None:
            return {'message' : "An item with name '{}' already exists".format(name)}
        
        data = Item.parser.parse_args()

        item = {'name' : name , 'price' : data['price']}
        items.append(item)
        return item


    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter( lambda x : x['name'] != name, items))
        return {'message' : 'Item deleted'}
    
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x : x['name'] == name,items), None)
        if item is None:
            item = {'name' : name, 'price' : data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    
class ItemList(Resource):
    def get(self):
        return {'items' : items }


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(debug=True)
    

# request JWT token first with /auth url, and providing username and passsword in body
# then call items, and from list of items use either to call item, like item/foo, and in body provide a price
```


### 2 - pyenv and pipenv

- Pyenv helps in managing different python versions. It can automatically install and stuff different versions, even jython and pypy also.
- pipenv is pip + virtualenv combined but depends on already install versions of python.
- pipenv (atleast on my system) is not able to directly refer to all pyenv pythons. It tries and fails. A workaround is to use pyenv to global that particular python which we want to use for pipenv beforehand and that way it works.

### 1 - Python Fire to expose internals and debugging

```bash
pip install fire
```

```python
#filename : t.py
import fire

if __name__ == "__main__":
        fire.Fire(); exit()
```

```bash
python t.py fire
```



