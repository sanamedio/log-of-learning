# 05-may-2019

### 2 - ipc queues 

nix systems come with different methods of shared communication, posix and sysv queues are one of them. shared memory is another. ipcs command can be used to see currently open channels. worth exploring..

- https://pythonhosted.org/ipcqueue/#module-ipcqueue.posixmq

```python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from ipcqueue import posixmq
>>> q = posixmq.Queue('/foo')
>>> q.qsize()
0
>>> q.put([1,'A'])
>>> q.put([2,'B'])
>>> q.put([3,'C'],priority=2)
>>> q.put([4,'D'],priority=0)
>>> q.get()
[3, 'C']
>>> q.get()
[1, 'A']
>>> q.get()
[2, 'B']
>>> q.get()
[4, 'D']
>>> q.get()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/loki/.local/lib/python2.7/site-packages/ipcqueue/posixmq.py", line 170, in get
    raise QueueError(res)
ipcqueue.posixmq.QueueError: 6, Interrupted by signal
>>> q.close()
>>> q.unlink()
>>> 
```


### 1 - Turing machine

https://www.python-course.eu/turing_machine.php

```python
class Tape(object):
    
    blank_symbol = " "
    
    def __init__(self,
                 tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))
        # last line is equivalent to the following three lines:
        #self.__tape = {}
        #for i in range(len(tape_string)):
        #    self.__tape[i] = input[i]
        
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class TuringMachine(object):
    
    def __init__(self, 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self): 
        return str(self.__tape)
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False



if __name__ == '__main__':
    initial_state = "init",
    accepting_states = ["final"],
    transition_function = {("init","0"):("init", "1", "R"),
                           ("init","1"):("init", "0", "R"),
                           ("init"," "):("final"," ", "N"),
                           }
    final_states = {"final"}

    t = TuringMachine("010011 ",
                      initial_state = "init",
                      final_states = final_states,
                      transition_function=transition_function)

    print("Input on Tape:\n" + t.get_tape())

    while not t.final():
        t.step()

    print("Result of the Turing machine calculation:")
    print(t.get_tape())
```
