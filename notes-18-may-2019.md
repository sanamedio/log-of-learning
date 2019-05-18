# 18-may-2019


### 1 - a simple CPU emulator 

v0.3
```python
class Memory:

    __memory = None


    def __init__(self,size):
        self.__memory = [ 0 for x in range(size) ]


    def read(self,position):
        return self.__memory[position]


    def write(self,position,value):
        self.__memory[position] = value

    def size(self):
        return len(self.__memory)


class Cpu:

    accumulator = 0
    ipointer = 0
    memory = None
    stack = []


    instr_map = {
                0: 'add',# add some value to accumulator
                1: 'jmp', # jmp to a relative position if accumulator is non zero
                2: 'load', # load value of a memory location to accumulator
                3: 'unload', # write value of accumulator to a memory location
                4: 'prn', # print to visual output
                
            }


    def __init__(self, mem):
        self.accumulator=0
        self.memory = mem
        self.ipointer=0


   


    def execute(self):
        #import pdb; pdb.set_trace()
            
        while self.ipointer < self.memory.size()-1:

            #print ('ipointer : ' + str(self.ipointer))
            

            instruction = 'nop'

            if self.memory.read(self.ipointer) in self.instr_map:
                instruction = self.instr_map[self.memory.read(self.ipointer)]

            if instruction == 'add': #1 operand
                operand = self.memory.read(self.ipointer+1)
                self.accumulator += operand
                self.ipointer += 2

            elif instruction == 'jmp':
                if self.accumulator != 0:
                    operand = self.memory.read(self.ipointer+1)
                    self.ipointer = (operand)%self.memory.size()
                else:
                    self.ipointer += 2

            elif instruction == 'load':
                operand = self.memory.read(self.ipointer+1)
                self.accumulator = self.memory.read(operand)
                self.ipointer += 2

            elif instruction == 'unload':
                operand = self.memory.read(self.ipointer+1)
                self.memory.write(operand,self.accumulator)
                self.ipointer += 2

            elif instruction == 'prn':
                print (self.accumulator)
                self.ipointer += 1

            elif instruction == 'nop':
                self.ipointer+=1


if __name__ == '__main__':  

    program_bytes = [
            2 ,  8, # load the 9th index item into accumulator
            0 , -1, # decrement 1 from accumulator
            4 , # print to output
            1 , 2, # just to -4 byte
            99, 10, # dummy operation, just to separate memory
            ]


    mem = Memory(100)

    for i in range(len(program_bytes)):
        mem.write(i,program_bytes[i])

    cpu = Cpu(mem)
    cpu.execute()
```
- removed a print option
- made all references absolute
- the bug which took time was that memory addressing was wrong

v0.2
```python
class Memory:

    __memory = None


    def __init__(self,size):
        self.__memory = [ 0 for x in range(size) ]


    def read(self,position):
        return self.__memory[position]


    def write(self,position,value):
        self.__memory[position] = value

    def size(self):
        return len(self.__memory)


class Cpu:

    accumulator = 0
    ipointer = 0
    memory = None


    instr_map = {
                0: 'add',# add some value to accumulator
                1: 'jmp', # jmp to a relative position if accumulator is non zero
                2: 'load', # load value of a memory location to accumulator
                3: 'unload', # write value of accumulator to a memory location
                4: 'prn', # print to visual output
                

            }


    def __init__(self, mem):
        self.accumulator=0
        self.memory = mem
        self.ipointer=0


   


    def execute(self ):

            
        while self.ipointer < self.memory.size():

            #print ('ipointer : ' + str(self.ipointer))
            

            instruction = 'nop'

            if self.memory.read(self.ipointer) in self.instr_map:
                instruction = self.instr_map[self.memory.read(self.ipointer)]

            if instruction == 'add': #1 operand
                operand = self.memory.read(self.ipointer+1)
                self.accumulator += operand
                self.ipointer += 2

            elif instruction == 'jmp':
                if self.accumulator != 0:
                    operand = self.memory.read(self.ipointer+1)
                    self.ipointer = (self.ipointer +  operand)%self.memory.size()
                else:
                    self.ipointer += 2

            elif instruction == 'load':
                operand = self.memory.read(self.ipointer+1)
                self.accumulator = self.memory.read(operand)
                self.ipointer += 2

            elif instruction == 'unload':
                operand = self.memory.read(self.ipointer+1)
                self.memory.write(operand,self.accumulator)
                self.ipointer += 2

            elif instruction == 'prn':
                operand = self.memory.read(self.ipointer+1)
                print (operand, (self.accumulator))
                self.ipointer += 2


            elif instruction == 'nop':
                self.ipointer+=1
                pass


        



if __name__ == '__main__':

    


    program_bytes = [
            2,9,
            0, -1,
            4, "msg",
            1, -4,
            99, 10,
            ]


    mem = Memory(100)

    for i in range(len(program_bytes)):
        mem.write(i,program_bytes[i])

    cpu = Cpu(mem)
    cpu.execute()

```
- this is still pretty high level
- how different threads work on the same cpu, that part
- how strings need to be saved?
- how devices are interfaced ?
- how the addressing is done?
- how can I make the jump simpler?
- 



v0.1
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

