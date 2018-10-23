# 24-oct-2018

### 1 - Meddling with a program in middle

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
