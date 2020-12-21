# 21-dec-2020

### 2 - Fast write counter usihng GIL

https://julien.danjou.info/atomic-lock-free-counters-in-python/

```python
import itertools
import threading

class FastWriteCounter(object):
    def __init__(self):
        self._number_of_read = 0
        self._counter = itertools.count()
        self._read_lock = threading.Lock()

    def increment(self):
        next(self._counter)

    def value(self):
        with self._read_lock:
            value = next(self._counter) - self._number_of_read
            self._number_of_read += 1
        return value
```



### 1 - eBPF filters for kernel tracing

https://filipnikolovski.com/posts/ebpf/

```python
from bcc import BPF
from bcc.utils import printb
# define BPF program
prog = """
int hello(void *ctx) {
    bpf_trace_printk("Hello, World!\\n");
    return 0;
}
"""
# load BPF program
b = BPF(text=prog)
b.attach_kprobe(event=b.get_syscall_fnname("clone"), fn_name="hello")
# header
print("%-18s %-16s %-6s %s" % ("TIME(s)", "COMM", "PID", "MESSAGE"))
# format output
while 1:
    try:
        (task, pid, cpu, flags, ts, msg) = b.trace_fields()
    except ValueError:
        continue
    except KeyboardInterrupt:
        exit()
    printb(b"%-18.9f %-16s %-6d %s" % (ts, task, pid, msg))
```
