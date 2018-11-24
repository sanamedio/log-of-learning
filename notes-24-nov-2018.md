# 24-nov-2018

### 2 - Generating magic squares

```python
def permutations(t,i):
    if i == len(t)-1:
        yield tuple(t)
    else:
        for j in range(i,len(t)):
            t[i],t[j] = t[j],t[i]
            yield from permutations(t,i+1)
            t[i],t[j] = t[j],t[i]


def check_magic(t):
    a = [ [None for i in range(3) ] for j in range(3) ]

    for i in range(3):
        for j in range(3):
            a[i][j] = t[i*3+j]

    for row in a:
        if sum(row) != 15:
            return False

    for row in zip(*a):
        if sum(row) != 15:
            return False

    if sum([ a[i][i] for i in range(3) ]) != 15:
        return False

    if sum([ a[2-i][i] for i in range(3) ]) != 15:
        return False

    return True




m_squares = set()

for m in permutations([1,2,3,4,5,6,7,8,9],0):
    if check_magic(m) :
        m_squares.add(m)


class Matrix:
    def __init__(self,l):
        self.m = [ [None for x in range(3) ] for y in range(3) ] 
        for i in range(3):
            print('')
            for j in range(3):
                print(l[i*3+j],end=' ')
        print('')





for m in m_squares:
   Matrix(m)
```

### 1 - brainfuck interpreter

- https://en.wikipedia.org/wiki/Brainfuck
- works on simple addition example of wikipedia, but failing on others!

```python
import sys


def cmpile(source_code):


    DATA_SIZE=10 + len(source_code)
    memory = [0 for x in range(DATA_SIZE)]
    memory = source_code + memory

    code_pointer= 0
    data_pointer=len(source_code)


    while True:

        print( code_pointer, data_pointer )
        if memory[code_pointer] == '>':
            data_pointer = data_pointer+1
        elif memory[code_pointer] == '<':
            data_pointer = data_pointer-1
        elif memory[code_pointer] == '+':
            memory[data_pointer] += 1
        elif memory[code_pointer] == '-' :
            memory[data_pointer] -= 1
        elif memory[code_pointer] == '.':
            print(ascii(memory[data_pointer]),end='')
        elif memory[code_pointer] == ',':
            memory[data_pointer] = int(input())
        elif memory[code_pointer] == '[':
            if memory[data_pointer] == 0:
                f = code_pointer
                match_bracket = 1
                while True:
                    if match_bracket ==0:
                        break
                    if memory[f] == '[':
                        match_bracket+=1
                    elif memory[f] == ']':
                        match_bracket-=1
                    f = f+1
                code_pointer = f
        elif memory[code_pointer] == ']':
            if memory[data_pointer] != 0:
                f = code_pointer
                match_bracket = 1
                while True:
                    f = f-1
                    if memory[f] == ']':
                        match_bracket+=1
                    elif memory[f] == '[':
                        match_bracket-=1
                    if match_bracket == 0:
                        break
                code_pointer = f



        code_pointer+= 1

        if code_pointer == len(source_code):
            print("\bprogram ended")
            print(code_pointer, data_pointer, source_code,memory,sep='\n')
            return

        if (code_pointer> DATA_SIZE-1) or (data_pointer > DATA_SIZE-1)  or (code_pointer < 0) or (data_pointer < 0):
            raise Exception("Out of memory read or write")



cmpile(list('++>+++++[<+>-]'))
```
