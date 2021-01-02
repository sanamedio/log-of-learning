# 03-jan-2020

### 1 - zipfly for big files

Saw this cool python project on hacker news. 

https://github.com/BuzonIO/zipfly#lib

Use case is to write zips in a memory efficient manner. 

```python
import zipfly

    paths = [
        {
            'fs': '/path/to/large/file'
        },
    ]

    zfly = zipfly.ZipFly(paths = paths)

    generator = zfly.generator()
    print (generator)
    # <generator object ZipFly.generator at 0x7f74d52bcc50>


    with open("large.zip", "wb") as f:
        for i in generator:
            f.write(i)
```

It appears like a generator wrapper looking at the implementation file on an existing library.
https://github.com/BuzonIO/zipfly/blob/master/zipfly/zipfly.py

