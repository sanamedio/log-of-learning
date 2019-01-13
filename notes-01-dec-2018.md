# 01-01-2018

### 5 - visualizing random.random

```python
import matplotlib.pyplot as plt
import seaborn as sns
import random


data = [ random.random() for x in range(1,100000)]
sns.distplot(data,kde=False,color='blue')
plt.show()
```

### 4 - matplotlib + seaborn + scipy normal distribution


```python
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

# normal distribution simulation data with mean 10 and deviation 2
data_normal = norm.rvs(size= 100000 , loc=10, scale=2)



from pprint import pprint

pprint(data_normal)

ax = sns.distplot(data_normal)
plt.show()
```

### 3 - matplotlib + seaborn + scipy binomial distribution

```python
In [23]: n = 10                                                                                                                             

In [24]: p = 0.3                                                                                                                            

In [25]: import numpy as np                                                                                                                 

In [26]: k = np.arange(0,21)                                                                                                                

In [27]: k                                                                                                                                  
Out[27]: 
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20])

In [28]: from scipy.stats import binom                                                                                                      

In [29]: binomial = binom.pmf(k, n  , p )                                                                                                   

In [30]: binomial                                                                                                                           
Out[30]: 
array([2.82475249e-02, 1.21060821e-01, 2.33474440e-01, 2.66827932e-01,
       2.00120949e-01, 1.02919345e-01, 3.67569090e-02, 9.00169200e-03,
       1.44670050e-03, 1.37781000e-04, 5.90490000e-06, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00])

In [31]: plt.plot(k, binomial, 'o-')                                                                                                        
Out[31]: [<matplotlib.lines.Line2D at 0x7fd1fa30d860>]

In [32]: plt.show()                                                                                                                         

In [33]: binom_simulation = binom.rvs(n=10, p = 0.3, size = 10000)                                                                          

In [34]: binom_simulation                                                                                                                   
Out[34]: array([2, 2, 2, ..., 4, 4, 3])

In [35]: plt.hist(binom_simulation, bins = 10, normed=True)                                                                                 
/home/kuroop/.local/lib/python3.6/site-packages/matplotlib/axes/_axes.py:6521: MatplotlibDeprecationWarning: 
The 'normed' kwarg was deprecated in Matplotlib 2.1 and will be removed in 3.1. Use 'density' instead.
  alternative="'density'", removal="3.1")
Out[35]: 
(array([0.03255556, 0.14133333, 0.26888889, 0.28788889, 0.22033333,
        0.11155556, 0.03944444, 0.00777778, 0.001     , 0.00033333]),
 array([0. , 0.9, 1.8, 2.7, 3.6, 4.5, 5.4, 6.3, 7.2, 8.1, 9. ]),
 <a list of 10 Patch objects>)

In [36]: plt.hist(binom_simulation, bins = 10, density=True)                                                                                
Out[36]: 
(array([0.03255556, 0.14133333, 0.26888889, 0.28788889, 0.22033333,
        0.11155556, 0.03944444, 0.00777778, 0.001     , 0.00033333]),
 array([0. , 0.9, 1.8, 2.7, 3.6, 4.5, 5.4, 6.3, 7.2, 8.1, 9. ]),
 <a list of 10 Patch objects>)

In [37]: plt.show()                                                                                                                         

In [38]:  
```

### 2 - matplotlib + seaborn + scipy uniform distribution

- from here : http://cmdlinetips.com/2018/03/probability-distributions-in-python/

```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import matplotlib.pyplot as plt                                                                            

In [2]: import seaborn as sns                                                                                                               
sns.
In [3]: sns.set(color_codes=True)                                                                                                           

In [4]: sns.set(rc={'figure.figsize':(4.5,3)})                                                                                              

In [5]: from scipy.stats import uniform                                                                                                     

In [6]: n = 10000                                                                                                                           

In [7]: a = 0                                                                                                                               

In [8]: b = 10                                                                                                                              

In [9]: data_uniform = uniform.rvs(size=n, loc=a , scale = b)                                                                               

In [10]: data_uniform                                                                                                                       
Out[10]: 
array([0.27858719, 5.21872471, 3.27208027, ..., 4.12754139, 8.53596404,
       6.76789163])

In [11]: ax = sns.distplot(data_uniform, bins = 100, kde=False, color='skyblue', hist_kws={"linewidth": 15 , 'alpha' : 1} )                 

In [12]: ax.set(xlabel = 'Uniform', ylabel = 'Frequency')                                                                                   
Out[12]: [Text(0, 0.5, 'Frequency'), Text(0.5, 0, 'Uniform')]

In [13]: plt.show()                                                                                                                         

In [14]: ax = sns.distplot(data_uniform, bins = 100, kde=False, color='black', hist_kws={"linewidth": 15 , 'alpha' : 1} )                   

In [15]: plt.show()                                                                                                                         

In [16]: ax = sns.distplot(data_uniform, bins = 100, kde=True, color='black', hist_kws={"linewidth": 15 , 'alpha' : 1} )                    

In [17]: plt.show()      
```

### 1 - flask + datatables + pygithub3

- python2, takes a organization name and puts all the repo data into a datatable. crappy code 
- https://github.com/copitux/python-github3
- https://datatables.net/
- put 'google' into search query and run to test

```python
from flask import Flask,jsonify,request
from pygithub3 import Github
import requests


app = Flask(__name__)


USERNAME=''
PASSWORD=''

g= Github(login=USERNAME,password= PASSWORD)


def input_form():
    r = ''
    r += '<form method="POST" target="/">'
    r += '<input name="org_name">'
    r += '<input type="submit">'
    r += '</form>'
    return r


def jquery():
    return """<head><script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
<script src="https://cdn.datatables.net/1.10.4/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.10.4/css/jquery.dataTables.min.css"></head>"""

def html(x):
    return '<html>' + jquery() + x + '</html>'


def datatable(x):
    r = ''

    r += '<table id="myTable">'

     
    r += '<thead><tr><th>repo_name</th></tr></thead>'
    r += '<tbody>'
    r += "\n".join( '<tr><td>' + l + '</td></tr>' for l in x)
    r += '</tbody>'
    r += '</table>'



    r+= """<script>
    $(document).ready( function () {
    $('#myTable').DataTable();
    } );
    </script>"""


    return r



@app.route('/')
def my_form():
   return html(input_form())

@app.route('/', methods=['POST'])
def my_form_post():
    org_name = request.form['org_name']
    repos = get_repos(org_name)
    r =''
    r += input_form()
#    r += ul_list(repos)
    r += datatable(repos)
    return html(r)


def get_repos(organization_name):
    try:
        return ( x.name for x in g.repos.list_by_org(organization_name).all())
    except:
        print "get repos exception"
        return []

if __name__ == '__main__':
    app.run()
```
