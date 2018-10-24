# 24-oct-2018

### 2 - Source code for objects, classes, closures, generators, iterators

- object protocol : https://docs.python.org/2/c-api/object.html
- data model : https://docs.python.org/2/reference/datamodel.html
- iterators
  - Include/iterobject.h
  - Objects/iterobject.c
  - Objects/abstract.c
  - Python/ceval.c
- classes and objects 
  - Include/classobject.h
  - Objects/classobject.c
  - Objects/abstract.c
  - Python/ceval.c
- Generators 
  - Include/genobject.h
  - Objects/genobject.c
  - Python/ceval.c

### 1 - Meddling with a program in middle

[SO link](https://stackoverflow.com/questions/132058/showing-the-stack-trace-from-a-running-python-application?noredirect=1&lq=1)

```python
import code
import traceback
import signal

def debug(sig, frame):
	"""Interrupt the running process and provide
		python prompt for interactive debugging."""
	d= { '_frame' : frame }
	d.update(frame.f_globals)
	d.update(frame.f_locals)

	i = code.InteractiveConsole(d)
	message = "Signal received :entering python shell\n Traceback.\n"
	message += ''.join(traceback.format_stack(frame))
	i.interact(message)


def listen():
	signal.signal(signal.SIGUSR1, debug) #Register handler

if __name__ == "__main__":
	listen()
  ## Your program logic starts here after we have registered this signal
	x = "Hello"
	while True:
		print x
		pass	
```
In a separate shell,
```python
import os,signal
os.kill( "PID of previous python process" , signal.SIGUSR1)
```
and bam, you got a shell to your previous infinite loop! and good thing is you can resume it back with Ctrl-D ( atleast on linux)
