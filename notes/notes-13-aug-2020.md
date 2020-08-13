# 13-aug-2020


### 1 - Removed calls between two commits

I faced a issue at work where a function call was removed mistakenly in a PR for a python project. So I thought let's automate identifying such removals of function calls. It's not perfect but it definetly finds out such issues.

```
python script.py v2.19.1 v2.20.0
```

```python
#script.py
import sys
import os

data = os.popen("find . -name '*.py' -exec grep -H \"^def \w.*(\" {} \;").read()

lines = [ x for x in data.split("\n") if len(x) > 1]

flist = []

for line in lines:
    x = line.split(":")
    flist += [ (x[1].split("(")[0][4:] , x[0] ) ]

fset =set( [x[0] for x in flist ])
removed_lines =[ x for x in  os.popen("git diff " + sys.argv[1] + " " +  sys.argv[2]).read().split("\n") if x.startswith("- ") ]
print("\n".join( [ line for line in removed_lines if any([(x in line) for x in fset]) ]))
```
