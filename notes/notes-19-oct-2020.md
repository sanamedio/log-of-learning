# 19-oct-2020

### 1 - _init_subclass_

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
