# 09-may-2019

### 1 - Python with cockroach DB

https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb.html#insecure

psycopg2 is postgres python client which can be used for cockroach db

```python
import psycopg2


conn = psycopg2.connect(
        database="bank",
        user="maxroach",
        sslmode="disable",
        port=26257,
        host="localhost"
        )


conn.set_session(autocommit=True)


cur = conn.cursor()


cur.execute("create table if not exists accounts(id INT PRIMARY KEY , balance int)")


cur.execute("INSERT INTO accounts (id,balance) values (1,1000),     (2,250)")


cur.execute("SELECT id, balance FROM accounts")
rows = cur.fetchall()
print('Initial balances:')
for row in rows:
    print([str(cell) for cell in row])

# Close the database connection.
cur.close()
conn.close()
```
