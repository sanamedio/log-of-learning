# 09-nov-2018

### 5 - Flask + matplotlib ( nice stuff really )

- Didn't ever thought of dynamically generating images
- taken from some gist

```python
import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG


from matplotlib.figure import Figure


app = Flask(__name__)


@app.route("/")
def index():

    num_x_points = int(request.args.get("num_x_points",50))

    return f"""

    <h2> Rnadom data with numxpoints={num_x_points}</h2>

    <form method=get action="/">
        <input name="num_x_points" type=number value="{num_x_points}" />
        <input type=submit value="update graph">
    </form>


    <img src="/matplot-as-image-{num_x_points}.png" height="200">

    <img src="/matplot-as-image-{num_x_points}.svg" height="200">
    """




@app.route("/matplot-as-image-<int:num_x_points>.png")
def plot_png(num_x_points=50):
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    x_points = range(num_x_points)
    axis.plot(x_points, [ random.randint(1,30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")



@app.route("/matplot-as-image-<int:num_x_points>.svg")
def plot_svg(num_x_points=50):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")



if __name__ == '__main__':
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)
```

### 4 - Generate a random binary number

```python
>>> def get_random_bits(n):
...     return format( random.getrandbits(n), '0' +str(n) + 'b' )
... 
>>> get_random_bits(10)
'0110011010'
>>> get_random_bits(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in get_random_bits
ValueError: number of bits must be greater than zero
>>> get_random_bits(1)
'0'
>>> get_random_bits(1)
'0'
>>> get_random_bits(1)
'1'
>>> 
```

### 3 - In-memory String compression using gzip and StringIO

```python
>>> import gzip
>>> import StringIO
>>> buf = StringIO.StringIO()
>>> compressed = gzip.GzipFile(fileobj=buf, mode="wb")
>>> compressed.write("hello wrold")
11
>>> print buf.getvalue()
vb�[�
>>> 
```

### 2 - Using dict to get attributes of a object( I think I mentioend it earlier also )

```python
>>> class A(object):
...     def __init__(self):
...             self.a = 'one'
...             self.b = 'two'
...     def mymethod(self):
...             pass
... 
>>> a = A()
>>> for attr, value in a.__dict__.iteritems():
...     print( attr, value)
... 
('a', 'one')
('b', 'two')
>>> 
```

### 1 - Using inner function to save data and printing a nested object 

```python
EXAMPLE_DATA = {
    'jobs': [{'frequency': '* * * * *',
              'jobconfig': [{'config': [('*',
                                         {'maxspeed': 1048576,
                                          'password': 'onesecretpassword',
                                          'port': 22,
                                          'url': 'basset://basset1.domain.com/tootsiepop/123.csv',
                                          'username': 'myusername'})],
                             'hasbro': 'basset'},
                            {'config': [('*',
                                         {'field_delim': ',',
                                          'field_line': True,
                                          'no_blanks': True,
                                          'quote_char': '"'})],
                             'hasbro': 'pen'},
                            {'config': [('*',
                                         {'db_database': 'mydatabase',
                                          'db_host': 'myhost',
                                          'db_password': 'anothersecretpassword',
                                          'db_table': 'mytable',
                                          'db_user': 'myuser'})],
                             'hasbro': 'dart'}],
              'jobdesc': 'Data from tootsiepop',
              'jobname': 'tootsiepop',
              'max_records_fail': '110%',
              'min_failure_time': '1000y'}],
    'vendor': 'tootsiepop'}



def print_all_leaf_nodes(data):
    if isinstance(data, dict):
        for item in data.values():
            print_all_leaf_nodes(item)
    elif isinstance(data, list) or isinstance(data, tuple):
        for item in data:
            print_all_leaf_nodes(item)
    else:
        print data


def get_all_leaf_nodes(data):
    class Namespace(object):
        pass

    ns = Namespace()
    ns.results = []

    def inner(data):
        if isinstance(data, dict):
            for item in data.values():
                inner(item)
        elif isinstance(data, (list,tuple)):
            for item in data:
                inner(item)
        else:
            ns.results.append(data)

    inner(data)
    return ns.results


from pprint import pprint
pprint(get_all_leaf_nodes(EXAMPLE_DATA))
```
