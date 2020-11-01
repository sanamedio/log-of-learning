# 01-nov-2020

### 1 - lsm-db transactions

- https://charlesleifer.com/blog/using-sqlite4-s-lsm-storage-engine-as-a-stand-alone-nosql-database-with-python/

```bash
>>> with db.transaction() as txn:
...     db['k1'] = '1-mod'
...     with db.transaction() as txn2:
...         db['k2'] = '2-mod'
...         txn2.rollback()
...
True
>>> print db['k1'], db['k2']
1-mod 2
```

```bash
>>> with db.transaction() as txn:
...    db['k1'] = 'outer txn'
...    txn.commit()  # The write is preserved.
...
...    db['k1'] = 'outer txn-2'
...    with db.transaction() as txn2:
...        db['k1'] = 'inner-txn'  # This is commited after the block ends.
...    print db['k1']  # Prints "inner-txn".
...    txn.rollback()  # Rolls back both the changes from txn2 and the preceding write.
...    print db['k1']
...
1              <- Return value from call to commit().
inner-txn      <- Printed after end of txn2.
True           <- Return value of call to rollback().
outer txn      <- Printed after rollback.
```

```
>> db.begin()
>>> db['foo'] = 'baze'
>>> print db['foo']
baze
>>> db.rollback()
True
>>> print db['foo']
bar
```
