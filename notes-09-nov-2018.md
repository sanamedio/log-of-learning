# 09-nov-2018

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
