# 09-may-2019

### 1 - Python with cockroach DB using psycopg2 driver

https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb.html#insecure

psycopg2 is postgres python client which can be used for cockroach db

Python DBAPI spec
https://www.python.org/dev/peps/pep-0249/

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


Doing transactions:-

```python
import psycopg2
import psycopg2.errorcodes

conn = psycopg2.connect(
            database="bank",
            user="maxroach",
            sslmode="disable",
            port=26257,
            host="localhost"

        )


def onestmt(conn, sql):
    with conn.cursor() as cur:
        cur.execute(sql)


def run_transaction(conn, op):

    with conn:
        onestmt(conn, "SAVEPOINT cockroach_restart")
        while True:
            try:
                op(conn)


                onestmt(conn, "RELEASE SAVEPOINT cockroach_restart")
                break
            except psycopg2.OperationalError as e:
                if e.pgcode != psycopg2.errorcodes.SERIALIZATION_FAILURE:
                    raise e
                onestmt(conn, "ROLLBACK TO SAVEPOINT cockroach_restart")


def transfer_funds(txn, frm, to, amount):
    with txn.cursor() as cur:

        cur.execute("SELECT balance FROM accounts WHERE id = " + str(frm))
        from_balance = cur.fetchone()[0]

        if from_balance < amount:
            raise "Insufficient funds"

        cur.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount,frm))
        cur.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, to))


run_transaction(conn, lambda conn: transfer_funds(conn, 1, 2 , 100))



with conn:
    with conn.cursor() as cur:
        cur.execute("SELECT id, balance FROM accounts")
        rows = cur.fetchall()
        print("Balances after transfer:")
        for row in rows:
            print([str(cell) for cell in row])


conn.close()

```



