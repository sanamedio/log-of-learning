# 19-oct-2020

### 2 - apply decorator to all subclassess

- https://stackoverflow.com/questions/35624872/apply-a-python-decorator-to-all-inheriting-classes

```python
def your_decorator(_cls):
    print("Hello, I'm decor!")
    def wrapper():
        return _cls()
    return wrapper


class ParentClass:
    def __init_subclass__(cls, **kwargs):
        return your_decorator(_cls=cls)


class A(ParentClass):
    pass

a = A()
```


### 1 - init subclass

- hook executed whenever a subclass is getting made from parent class

```python
#https://stackoverflow.com/questions/45400284/understanding-init-subclass
class Philosopher:
    def __init_subclass__(cls, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Called __init_subclass({cls}, {default_name})")
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass

class GermanPhilosopher(Philosopher, default_name="Nietzsche"):
    default_name = "Hegel"
    print("Set name to Hegel")

Bruce = AustralianPhilosopher()
Mistery = GermanPhilosopher()
print(Bruce.default_name)
print(Mistery.default_name)
```
