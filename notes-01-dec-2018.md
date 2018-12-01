# 01-01-2018


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
