# 02-dec-2019

### 2 - buy and sell stocks in python

This is standard programming interview puzzle.

It has even more solutions, and divide and conquer one is plain cool.
http://keithschwarz.com/interesting/code/?dir=single-sell-profit
https://stackoverflow.com/questions/7086464/maximum-single-sell-profit

version2: solution based on simple observation of local minima and maximas
```python3
def stockBuySell(prices,size):

    n = len(prices)

    if n == 1:
        return

    i = 0

    while i < n-1:


        while (i < n-1) and (prices[i+1] <= prices[i]):
            i = i + 1


        if i == n - 1:
            break


        buy = i
        i = i + 1

        while (i < n) and (prices[i] >= prices[i-1]):
            i = i + 1

        sell = i - 1

        print( "Buy: ", buy, " Sell: ", sell )


if __name__ == '__main__':
        prices = [100,180,260,310,40, 535, 695]
        n = len(prices)

        stockBuySell(prices,n)

```




version1: brute force, observe the number of function call is even more than n^2
```python3


cnt = 0


def maxProfit( price, start, end):

    global cnt

    cnt += 1

    if end <= start:
        return 0

    profit = 0


    for i in range(start,end):
        for j in range(i+1,end+1):

            if price[j] > price[i]:

                curr_profit = price[j] - price[i]

                curr_profit += maxProfit(price,start, i-1)
                curr_profit += maxProfit(price,j+1, end)

                profit = max(profit, curr_profit)

    return profit


if __name__ == '__main__':

    prices = [ 100,180,260,310,40,535,695 ]

    n = len(prices)

    print (maxProfit(prices, 0 , n-1))
    print (cnt)
```


### 1 - Reversing a Linked list in Python

From here :- https://www.geeksforgeeks.org/reverse-a-linked-list/

```python
# Python program to reverse a linked list  
# Time Complexity : O(n) 
# Space Complexity : O(1) 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to reverse the linked list 
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
          
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print temp.data, 
            temp = temp.next
  
  
# Driver program to test above functions 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print "Given Linked List"
llist.printList() 
llist.reverse() 
print "\nReversed Linked List"
llist.printList() 
```
