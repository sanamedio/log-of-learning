# 28-nov-2019

### 7 - classmethod vs staticmethod

```python
class A(object):
    def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x    

a = A()
```


### 6 - nim game play with DP

- https://www.programcreek.com/2014/04/leetcode-nim-game-java/
- two person game theory play. You either win immediately, or find a way to push other player to a loser state ( of mind :D )

```python
import functools


@functools.lru_cache(maxsize=128)
def nim(n):
    if n < 4:
        return True #the caller is the winner
    else:
        for i in range(1,4):
            if (not nim(n-i)) == True:
                return True

    return False




for i in range(1,100):
    print(i, " --> " , nim(i))
```


### 5 - the mathematics of bulb switch problem

- https://www.programcreek.com/2014/05/leetcode-bulb-switcher-java/
- why it turns out to be perfect squares patterns ; one argument is that perfect squares have odd number of  divisors, as the factors all are having even powers and then if we use the divisor count formula it makes number of divisors as odd and the implication is reverse as well. -> 
https://math.stackexchange.com/questions/906159/a-number-is-a-perfect-square-if-and-only-if-it-has-odd-number-of-positive-diviso


### 4 - pain fence problem - memory optimized DP

- This is like many problems where you can count for a higher N by observing a simple pattern between nearby elements and write a recurrance

```python
#https://www.programcreek.com/2014/05/leetcode-pain-fence-java/


def num_way(n, k ):


    

    dp[] = {0, k , k*k, 0 }


    if n <= 2:
        return dp[n]


    for i in range(2,n):
        dp[3] = (k*1)* (dp[1] + dp[2])
        dp[1] = dp[2]
        dp[2] = dp[3]


    return dp[3]

```

### 3 - Removing duplicates by swapping the dupes to the end

- given an array, bring the unique elements to the front without using any extra space

```python
def remove_dup(A):

    if len(A) < 2:
        return len(A)


    j = 0
    i = 1

    while i < len(A):
        if A[i] != A[j]:
            j+=1
            A[j] = A[i]
        i+=1


    return j + 1


if __name__ == '__main__':
    print(remove_dup([1,1,1,1,2,2,2,2,2,3,3,3,3,3]))

```


### 2 - finding lattice point is easier than I thought

```python
import math


def count_lattice(r):


    if r <= 0:
        return 0


    result = 4


    for x in range(1,r):

        ys = r*r - x*x

        y = int(math.sqrt(ys))


        if y*y  == ys:
            result +=  4



    return result



r = 5
print(count_lattice(r))
```


### 1 - two way data binding in pure JS

- good example to create two way binding with pure structs

```html
<input type=text id="myText1">
<input type=text id="myText2">
<span type=text id="myDomElement"></span>
```


```javascript
function Binding(b) {
    _this = this
    this.elementBindings = []
    this.value = b.object[b.property]
    this.valueGetter = function(){
        return _this.value;
    }
    this.valueSetter = function(val){
        _this.value = val
        for (var i = 0; i < _this.elementBindings.length; i++) {
            var binding=_this.elementBindings[i]
            binding.element[binding.attribute] = val
        }
    }
    this.addBinding = function(element, attribute, event){
        var binding = {
            element: element,
            attribute: attribute
        }
        if (event){
            element.addEventListener(event, function(event){
                _this.valueSetter(element[attribute]);
            })
            binding.event = event
        }       
        this.elementBindings.push(binding)
        element[attribute] = _this.value
        return _this
    }

    Object.defineProperty(b.object, b.property, {
        get: this.valueGetter,
        set: this.valueSetter
    }); 

    b.object[b.property] = this.value;
}

var obj = {a:123}
var myInputElement1 = document.getElementById("myText1")
var myInputElement2 = document.getElementById("myText2")
var myDOMElement = document.getElementById("myDomElement")

new Binding({
	object: obj,
	property: "a"
})
.addBinding(myInputElement1, "value", "keyup")
.addBinding(myInputElement2, "value", "keyup")
.addBinding(myDOMElement, "innerHTML")

obj.a = 456;
```
