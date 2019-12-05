# 05-dec-2019

### 3 - CSS selectors and Beautiful soup 

- Python can do a lot with minimal lines of code. Many times we want links present in webpage and that can help us in scripting in bash during scraping. I personally use this small flexible snippet for the same.

Something like getting all the links from wikipedia webpage can be achieved on command line with this script as:-

```bash
python3 select-by-css.py "https://wikipedia.com" "a" "href"
```

code:-
```python3
from bs4 import BeautifulSoup
import requests
import sys

soup  = BeautifulSoup(requests.get(sys.argv[1]).content, features = "lxml")

css_selector = sys.argv[2]

attrib_selector = None

if len(sys.argv) == 4:
    attrib_selector = sys.argv[3]


for s in soup.select(css_selector):
    if attrib_selector:
        print(s.attrs[attrib_selector])
    else:
        print(s)
```

We can use Xpath, etc also; but for a bare minimal version this works well with other scripts. 

### 2 - Watching youtube videos in turtle window

- this one is basically an experiment on how a simple graphic renderer can be used to display videos. All the code and instructions are put in this github gist. Note: ffmpeg is cool.

https://gist.github.com/l0k3ndr/f269da2cdecacab2b7494d3dc71fd54f

### 1 - Python2 vs Python3 comparision

https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
