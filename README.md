# python-notes
Just notes from here and there.

1. List
```
mylist  = [ x for x in range(3) ]
```

2. Generator List
```
mygenerator = ( x for x in range(3) )
```

3. Yeild list from function
```
def createGenerator()
  mylist = range(3)
  for i in mylist:
    yield i*i

mygenerator = createGenerator()
```


