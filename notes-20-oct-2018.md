# 20-oct-2018


### 1 - pyrasite shell

- Allows to get shell on a running python process
- https://pyrasite.readthedocs.io/en/latest/Shell.html

Step 1:
```bash
pip install pyrasite
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
```
Step 2: Run a Python program or something like ipython

Step 3:
```bash
pyrasite-shell <pid of python process>
```
