# 04-nov-2018

### 2 - pyenv and pipenv

- Pyenv helps in managing different python versions. It can automatically install and stuff different versions, even jython and pypy also.
- pipenv is pip + virtualenv combined but depends on already install versions of python.
- pipenv (atleast on my system) is not able to directly refer to all pyenv pythons. It tries and fails. A workaround is to use pyenv to global that particular python which we want to use for pipenv beforehand and that way it works.

### 1 - Python Fire to expose internals and debugging

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



