# 04-nov-2018

### 2 - pyenv and pipenv

- Pyenv helps in managing different python versions. It can automatically install and stuff different versions, even jython and pypy also.
- pipenv is pip + virtualenv combined but depends on already install versions of python.

### 1 - Python Fire to expose internals

```bash
pip install fire
```

```python
#filename : t.py
import fire

if __name__ == "__main__":
        fire.Fire(); exit()
```

```bash
python t.py fire
```



