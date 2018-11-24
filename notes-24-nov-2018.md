# 24-nov-2018

### 1 - brainfuck interpreter

- https://en.wikipedia.org/wiki/Brainfuck
- need to test it, especially bracket matchign

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
                match_bracket = 0
                while (memory[f] != ']' and match_bracket != 0  ):
                    if memory[f] == '[':
                        match_bracket+=1
                    elif memory[f] == ']':
                        match_bracket-=1
                    f = f+1
                code_pointer = f
        elif memory[code_pointer] == ']':
            if memory[data_pointer] == 0:
                f = code_pointer
                match_bracket = 0
                while memory[f] != '[' and match_bracket !=0:
                    if memory[f] == ']':
                        match_bracket+=1
                    elif memory[f] == '[':
                        match_bracket-=1
                    f = f-1
                code_pointer = f



        code_pointer+= 1

        if code_pointer == len(source_code):
            print("\bprogram ended")
            print(code_pointer, data_pointer, source_code,memory,sep='\n')
            return

        if (code_pointer> DATA_SIZE-1) or (data_pointer > DATA_SIZE-1)  or (code_pointer < 0) or (data_pointer < 0):
            raise Exception("Out of memory read or write")




cmpile(list('>>>>+++[>.,[+++]>>>+++]'))
```
