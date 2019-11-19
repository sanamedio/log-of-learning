# 21-jan-2019


### 1 - probability simulations!

```python
#Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.
#The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you #pay, in dollars.
#The second game: same, except that the stopping condition is a five followed by a five.
#Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their #expected value.


import random

def roll():
    return random.randrange(1,7)
    
def consecutive_roll(X):
    A = X[0]
    B = X[1]
    a = roll()
    b = roll()
    cnt = 1
    while not ( a == A and b == B ):
        a = b
        b = roll()
        cnt = cnt + 1
    return cnt

def simulate( num , f , args ):
   return sum( [ f(args) for x in range(num) ])*1.0/num

if __name__ == '__main__':

    print(simulate( 100000, consecutive_roll, (5,6) ))
    print(simulate( 100000, consecutive_roll, (5,5) ))
```

- https://math.stackexchange.com/questions/192177/how-many-times-to-roll-a-die-before-getting-two-consecutive-sixes
