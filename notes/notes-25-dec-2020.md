# 25-dec-2020


### 2 - git log of function

```
git log -L :funcname:file_path
```

https://stackoverflow.com/questions/4781405/git-how-do-i-view-the-change-history-of-a-method-function/33953022#33953022

### 1 - map reduce with pyspark

rule discovery from data of transactions

```python
import pyspark

data = [
        ("Bread","Diaper" ,"Milk"),
        ("Beer", "Bread"),
        ("Milk", "Diaper", "Beer", "Coke"),
        ("Bread", "Milk", "Diaper", "Beer"),
        ("Milk", "Diaper", "Coke")
] 


from pyspark import SparkContext 
sc = SparkContext.getOrCreate() 
w = sc.parallelize(data)

total_txns = len(data)

def mapfunc(txn):
  return (txn, 1)

def reducefunc(x, y):
  return x+y

w = sc.parallelize(data)
item_counts = w.flatMap(lambda txn: txn) \
          .map(lambda txn: mapfunc(txn)) \
          .reduceByKey(lambda x, y: reducefunc(x, y))

item_count_dict = dict(item_counts.collect())
support = {k:(v/total_txns) for k,v in item_count_dict.items()}
print(support)


def mapfunc(txn):
  return (txn, 1)

def reducefunc(x, y):
  return x+y

def createPairs(lst):

  lst = sorted(lst)
  result = []
  for i,e1 in enumerate(lst):
    for j,e2 in enumerate(lst[i+1:]):
      result += [e1+"_"+e2,]

  return tuple(result)


w = sc.parallelize(data)
item_pair_counts = w.flatMap(createPairs) \
          .map(lambda txn: mapfunc(txn)) \
          .reduceByKey(lambda x, y: reducefunc(x, y))

item_pair_count_dict = dict(item_pair_counts.collect())
supportXY = {k:(v/total_txns) for k,v in item_pair_count_dict.items()}
print(supportXY)



confidence = {}
for e1 in support.keys():
  for e2 in support.keys():
    if e1 != e2:
      key = "_".join(sorted([e1,e2]))
      rule = str(e1) + " => " +  str(e2)
      if key in supportXY and supportXY[key] > 0.2:
        confidence[rule] = supportXY[key]/support[e1]
        print(rule, supportXY[key], confidence[rule])

```
