# 22-dec-2020


### 1 - building tree from inorder and postorder


```python
class Node:
 
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

    
def createTree(in_order, post_order):
  
  if len(in_order) == 0 or len(post_order) == 0:
    return None
  
  if len(post_order) > 0:
    
    val = post_order[-1] # last element of the post order array
    
    index_of_root_inorder = in_order.index(val)
    

    inorder_left_part = in_order[0:index_of_root_inorder] #arrays
    inorder_right_part = in_order[index_of_root_inorder+1:]
    
    post_order_left_part = [ x for x in post_order if (x in inorder_left_part)]
    post_order_right_part = [ x for x in post_order if (x in inorder_right_part)]
    
    
    left_node = createTree(inorder_left_part, post_order_left_part)
    right_node = createTree(inorder_right_part, post_order_right_part)
    
    curr_node = Node(val, left_node, right_node)
  
    return curr_node

mytree = createTree([4,8 ,2 ,5 ,1 ,6 ,3 ,7], [8 ,4 ,5 ,2, 6, 7, 3 ,1 ])

def preOrder(s):
  if not s: return
  else:
    print(s.val)
    preOrder(s.left)
    preOrder(s.right)

preOrder(mytree)
```
