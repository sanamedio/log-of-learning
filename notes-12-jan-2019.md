# 12-jan-2019

### 2 - ijson

- https://pypi.org/project/ijson/
- Streaming json as events
```python
import ijson
f = open("test.json")
gen = ijson.parse(f)
print( next(gen))
print( next(gen))
print( next(gen))
```


### 1 - selenium webdriver

- selenium can help a lot in simplifying webscraping for websites which dynamically load content

```python
from selenium import webdriver

t= webdriver.Firefox()

with open("problemset.all","w") as f:
    for i in range(1,61):
        url = "https://practice.abcdefghi.org/explore/?page={}&sortBy=accuracy".format(i)
        print(url)
        t.get(url)
        links = [ x.find_elements_by_tag_name('a') for x in t.find_elements_by_class_name('problems')]
        all_links = [ item for sublist in links for item in sublist ]
        f.write('\n'.join([ a.get_attribute('href') for a in all_links if '/problems' in a.get_attribute('href') ]))
```
