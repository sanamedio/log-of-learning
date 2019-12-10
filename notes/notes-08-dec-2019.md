# 08-dec-2019

### 6 - Award Budget Cuts (coding problem)

- [link](https://www.pramp.com/question/r1Kw0vwG6OhK9AEGAyWV)

correct solution:-
```python3
def findGrantsCap(grants, new_budget):

	n = len(grants)
	grants = list(reversed(sorted(grants)))
	grants.append(0)
	surplus = sum(grants) - new_budget

	if surplus <= 0:
		return grants[0]
	
	for i in range(0,n):
		surplus -= (i+1) * (grants[i] - grants[i+1])
		if surplus <= 0:
			break

	return grants[i+1] + ( -surplus / float(i+1) )
```


### 5 - Difference between let and var in JS

We can say let is more strict than var and helps in predicting scopes easily

https://stackoverflow.com/questions/762011/whats-the-difference-between-using-let-and-var

### 4 - CircleCI tutorial with Flask and Github

Something other than our old Jenkins:

https://circleci.com/blog/setting-up-continuous-integration-with-github/


### 3 - A + B = C using regex

This is absolutely brilliant.(for a fun excercise)

http://www.drregex.com/2018/09/a-regex-i-submitted-to-reddit-climbed.html?m=1

### 2 - Mongodb oplog access

```bash
MongoDB shell version: 2.0.4
connecting to: mongodb:27017/test
PRIMARY> use local
PRIMARY> db.oplog.rs.find()
```

### 1 - Entry points

https://amir.rachum.com/blog/2017/07/28/python-entry-points/
