# 13-jan-2019

### 3 - red black tree

- in general hieght grows more than avl trees
- less rotations cuz in few cases, just color change happens; less strict bound on height than avl trees
- rotations are similar to AVL tree, but with color modifications for nodes
- colors helps in keeping additional data with nodes, so that we know when to rotate. So it's kind of a delayed rotation where colors help in keeping track how delayed it is? ( don't know that's all intiution I have got on this )
- https://brilliant.org/wiki/red-black-tree/

```python
## have to implement the other side of rotation so this code doesn't work. It's taken from this tutorial which is unfinished.
class node:
    def __init__(self, key):
        self.key = key
        self.red = True
        self.left = None
        self.right = None
        self.parent = None

class RBTree:
    self.root = None



    def search(self, key):
        currentNode = self.root
        while currentNode != None and key != currentNode.key:
            if key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return currentNode



    def insert(self, key):
        node = Node(key)
        #Base Case - Nothing in the tree
        if self.root == None:
            node.red = False
            self.root = node
            return
        #Search to find the node's correct place
        currentNode = self.root
        while currentNode != None:
            potentialParent = currentNode
            if node.key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        #Assign parents and siblings to the new node
        node.parent = potentialParent
        if node.key < node.parent.key:
            node.parent.left = node
        else:
            node.parent.right = node
        node.left = None
        node.right = None
        self.fixTree(node)



    def fixTree(self, node):
        while node.parent.red == True and node != self.root:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.red:
                    #This is Case 1
                    node.parent.red = False
                    uncle.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        #This is Case 2
                        node = node.parent
                        self.left_rotate(node)
                    #This is Case 3
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.red:
                    #Case 1
                    node.parent.red = False
                    uncle.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        #Case 2
                        node = node.parent
                        self.right_rotate(node)
                    #Case 3
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.left_rotate(node.parent.parent)
        self.root.red = False


    def left_rotate(self, node):
        sibling = node.right
        node.right = sibling.left
        #Turn sibling's left subtree into node's right subtree
        if sibling.left != None:
            sibling.left.parent = node
        sibling.parent = node.parent
        if node.parent == None:
            self.root = sibling
        else:
            if node == node.parent.left:
                node.parent.left = sibling
            else:
                node.parent.right = sibling
        sibling.left = node
        node.parent = sibling
```

### 2 - pycuber

- nice library to manipulate rubic cube.
- need to keep it for later use in a solver https://github.com/adrianliaw/PyCuber
```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pycuber as pc
>>> mycube = pc.Cube()
>>> print(mycube)
         [y][y][y]
         [y][y][y]
         [y][y][y]
[r][r][r][g][g][g][o][o][o][b][b][b]
[r][r][r][g][g][g][o][o][o][b][b][b]
[r][r][r][g][g][g][o][o][o][b][b][b]
         [w][w][w]
         [w][w][w]
         [w][w][w]

>>> mycube("R U R' U'")
>>> print(mycube)
         [y][y][r]
         [y][y][g]
         [y][y][g]
[b][r][r][g][g][w][o][o][y][b][o][o]
[r][r][r][g][g][y][b][o][o][b][b][b]
[r][r][r][g][g][g][y][o][o][b][b][b]
         [w][w][o]
         [w][w][w]
         [w][w][w]

>>> 
```


### 1 - uninstalling things with pip

- When you do multiple pip uninstalls; they remove packages from multiple places. In order to delete a package completely; keep doing it until it does not show any new uninstall
