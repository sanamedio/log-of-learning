# 24-dec-2018

### 5 - Graph representation; adjacency list

- http://interactivepython.org/courselib/static/pythonds/Graphs/Implementation.html

```python
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

```
test:
```bash
>>> g = Graph()
>>> for i in range(6):
...    g.addVertex(i)
>>> g.vertList
{0: <adjGraph.Vertex instance at 0x41e18>,
 1: <adjGraph.Vertex instance at 0x7f2b0>,
 2: <adjGraph.Vertex instance at 0x7f288>,
 3: <adjGraph.Vertex instance at 0x7f350>,
 4: <adjGraph.Vertex instance at 0x7f328>,
 5: <adjGraph.Vertex instance at 0x7f300>}
>>> g.addEdge(0,1,5)
>>> g.addEdge(0,5,2)
>>> g.addEdge(1,2,4)
>>> g.addEdge(2,3,9)
>>> g.addEdge(3,4,7)
>>> g.addEdge(3,5,3)
>>> g.addEdge(4,0,1)
>>> g.addEdge(5,4,8)
>>> g.addEdge(5,2,1)
>>> for v in g:
...    for w in v.getConnections():
...        print("( %s , %s )" % (v.getId(), w.getId()))
...
( 0 , 5 )
( 0 , 1 )
( 1 , 2 )
( 2 , 3 )
( 3 , 4 )
( 3 , 5 )
( 4 , 0 )
( 5 , 4 )
( 5 , 2 )
```

- http://interactivepython.org/courselib/static/pythonds/Graphs/BuildingtheWordLadderGraph.html

word ladder problem:
```python
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
```


### 4 - AVL tree python

- https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

```python
# Python code to insert a node in AVL tree 

# Generic tree node class 
class TreeNode(object): 
	def __init__(self, val): 
		self.val = val 
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the 
# Insert operation 
class AVL_Tree(object): 

	# Recursive function to insert key in 
	# subtree rooted with node and returns 
	# new root of subtree. 
	def insert(self, root, key): 
	
		# Step 1 - Perform normal BST 
		if not root: 
			return TreeNode(key) 
		elif key < root.val: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 

		# Step 2 - Update the height of the 
		# ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and key < root.left.val: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and key > root.right.val: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def leftRotate(self, z): 

		y = z.right 
		T2 = y.left 

		# Perform rotation 
		y.left = z 
		z.right = T2 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def rightRotate(self, z): 

		y = z.left 
		T3 = y.right 

		# Perform rotation 
		y.right = z 
		z.left = T3 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def getHeight(self, root): 
		if not root: 
			return 0

		return root.height 

	def getBalance(self, root): 
		if not root: 
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right) 

	def preOrder(self, root): 

		if not root: 
			return

		print("{0} ".format(root.val), end="") 
		self.preOrder(root.left) 
		self.preOrder(root.right) 


# Driver program to test above function 
myTree = AVL_Tree() 
root = None

root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 



# Preorder Traversal 
print("Preorder traversal of the", 
	"constructed AVL tree is") 
myTree.preOrder(root) 
print() 

# This code is contributed by Ajitesh Pathak 
```

```python
# Python code to delete a node in AVL tree 
# Generic tree node class 
class TreeNode(object): 
	def __init__(self, val): 
		self.val = val 
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports insertion, 
# deletion operations 
class AVL_Tree(object): 

	def insert(self, root, key): 
		
		# Step 1 - Perform normal BST 
		if not root: 
			return TreeNode(key) 
		elif key < root.val: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 

		# Step 2 - Update the height of the 
		# ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and key < root.left.val: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and key > root.right.val: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	# Recursive function to delete a node with 
	# given key from subtree with given root. 
	# It returns root of the modified subtree. 
	def delete(self, root, key): 

		# Step 1 - Perform standard BST delete 
		if not root: 
			return root 

		elif key < root.val: 
			root.left = self.delete(root.left, key) 

		elif key > root.val: 
			root.right = self.delete(root.right, key) 

		else: 
			if root.left is None: 
				temp = root.right 
				root = None
				return temp 

			elif root.right is None: 
				temp = root.left 
				root = None
				return temp 

			temp = self.getMinValueNode(root.right) 
			root.val = temp.val 
			root.right = self.delete(root.right, 
									temp.val) 

		# If the tree has only one node, 
		# simply return it 
		if root is None: 
			return root 

		# Step 2 - Update the height of the 
		# ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
							self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and self.getBalance(root.left) >= 0: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and self.getBalance(root.right) <= 0: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and self.getBalance(root.left) < 0: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and self.getBalance(root.right) > 0: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def leftRotate(self, z): 

		y = z.right 
		T2 = y.left 

		# Perform rotation 
		y.left = z 
		z.right = T2 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def rightRotate(self, z): 

		y = z.left 
		T3 = y.right 

		# Perform rotation 
		y.right = z 
		z.left = T3 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def getHeight(self, root): 
		if not root: 
			return 0

		return root.height 

	def getBalance(self, root): 
		if not root: 
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right) 

	def getMinValueNode(self, root): 
		if root is None or root.left is None: 
			return root 

		return self.getMinValueNode(root.left) 

	def preOrder(self, root): 

		if not root: 
			return

		print("{0} ".format(root.val), end="") 
		self.preOrder(root.left) 
		self.preOrder(root.right) 


myTree = AVL_Tree() 
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2] 

for num in nums: 
	root = myTree.insert(root, num) 

# Preorder Traversal 
print("Preorder Traversal after insertion -") 
myTree.preOrder(root) 
print() 

# Delete 
key = 10
root = myTree.delete(root, key) 

# Preorder Traversal 
print("Preorder Traversal after deletion -") 
myTree.preOrder(root) 
print() 

```

### 3 - Binary Search Tree, OOPs

- http://interactivepython.org/courselib/static/pythonds/Trees/SearchTreeImplementation.html

```python
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)




mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
```

### 2 - heap data structure

- http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html 

```python
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             self.heapList[i // 2], self.heaplist[i] = self.heapList[i], self.heapList[i//2]
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
```


### 1 - z3-solver

- its a sat solver, given a constraint it will give solution.

```python

In [4]: from z3 import *

In [5]: x = Real('x')

In [6]: y = Real('y')

In [7]: s = Solver()

In [8]: s.add( x + y > 5 , x > 1 , y > 1 )

In [9]: print(s.check())
sat

In [10]: print(s.model())
[y = 3/2, x = 4]
```
