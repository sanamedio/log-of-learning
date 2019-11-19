# 27-jan-2019


### 1 - trie

```python
class Trie:
    def __init__(self):
        self.root = {} # root node filledw ith blank and no child ? 
        # if we know the maximum item in a map, we can say that it's behaviour is constant time? 

    def insert(self,word):
        self.insert_recursive(self.root,  word)
    

    def insert_recursive(self, node , word):
        if len(word) == 0 :
            if '$' not in node:
                node['$']  =1
            else:
                node['$'] += 1
        else:    
            if word[0] not in node:
                node[word[0]] =  {} 
            
            self.insert_recursive(node[word[0]],word[1:])


    def print_all(self):
        self.print_all_helper(self.root, "")

    def print_all_helper(self, node, s):
        if '$' in node and node['$'] > 0 :
            for i in range(node['$']):
                print (s )
        
        for k in node:
            if k != '$':
                self.print_all_helper(node[k],s+k)


    def search(self,word):
        return self.search_recursive(self.root,word)


    def search_recursive(self,node,word):
        if len(word)==0:
            if node['$'] > 0:
                return True
            else:
                return False
        else:
            c = word[0]
            if c in node :
                return self.search_recursive(node[c],word[1:])
            else:
                return False
        return False



if __name__ == '__main__':
    t = Trie()

    t.insert("a")
    t.insert("abcd")
    t.insert("ab")
    t.insert("abc")
    t.insert("abcd")

    t.print_all()
    print( t.search("abcd"))
    print( t.search("abcx"))
```
