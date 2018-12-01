# 01-01-2018

### 1 - requests + flask + datatables + pygithub3

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
