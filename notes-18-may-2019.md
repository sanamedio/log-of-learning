# 18-may-2019


### 1 - a simple CPU emulator v0.00001

```python
class Cpu:

    accumulator = 0
    ipointer = 0

    def __init__(self):
        self.accumulator=0
        self.ipointer=0
        self.memory = [0 for x in range(256) ]



    def execute(self,instruction,operand ):

        if instruction == 'add':
            self.accumulator += operand
        elif instruction == 'jmp':
            self.ipointer += operand
        elif instruction == 'load':
            self.accumulator = self.memory[operand]
        elif instruction == 'unload':
            self.memory[operand] = self.accumulator
        elif instruction == 'prn':
            print operand, (self.accumulator)







if __name__ == '__main__':

    program = [

                ('add' , 1),
                ('unload', 0),
                ('prn', "msg")

            ]

    cpu = Cpu()

    for instr in program:
        cpu.execute(instr[0], instr[1])
```

- this isn't a correct emulation. The jump won't really work
- the instructions should be given some id's which can be put into memory
- we don't need to pass the program to cpu. I guess the whole thing can boot up from memory

