# 03-oct-2019


### 1 - Probability game

https://www.evanward.org/posts/a-counterintuitive-probability-game

```python
import random
#this function gets you the win/loss rate given c's relationship to the intervals a & b are selected from
def trials():
  N_trials=10000
  R=10000 #range random variables selected from
  wins, losses=0, 0
  print('Simulation of '+str(N_trials)+' trials:')
  for _ in range(N_trials):
    a=random.randint(-R,R) 
    b=random.randint(-R,R)
    c=random.randint(-R,R) #third random number
    if a<c: #implementing the procedure
      if a<b:
        wins+=1
      else:
        losses+=1
    else:
      if a>b:
        wins+=1
      else:
        losses+=1
  print('Wins: '+str(wins)+ '  Losses: '+str(losses), " Win Percentage: "+str(wins/(wins+losses)))
trials()
print('-----------------------------')


#below is to illustrate how powerful the procedure is. If a disbeliever had the patience and weren't a very good Bayesian, you could make a lot of money at a bar with them.
def game():
  print("Iterated game starting at $100 and going to $0 or $1000:")
  #you can play around with these 4 vars to experiment
  winPrice=1
  losePrice=-1.90
  trialLimit=10
  startMoney=100

  trials=0
  wins=0
  losses=0
  while trials < trialLimit:
    money=startMoney
    iterations=0
    while money >0 and money<1000: #game stops at $1000
      iterations+=1
      a=random.randint(-1000000,1000000)
      b=random.randint(-1000000,1000000)
      c=random.randint(-1000000,1000000)
      if a<c:
        if a<b:
          money+=winPrice
        else:
          money+=losePrice
      else:
        if a>b:
          money+=winPrice
        else:
          money+=losePrice
    print(str(trials)+': '+str(int(money))+'  Iterations: '+str(iterations))
    trials+=1
    if money<=0:
      losses+=1
    else:
      wins+=1
  print('Wins: '+str(wins)+ '  Losses: '+str(losses), " Win Percentage: "+str(wins/(wins+losses)))
game()
```
