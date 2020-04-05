# 05-apr-2020

### 1 - pytorch basic example

Tries to find out a equation based on data; but very handtuned by the author.

```python
import numpy as np
import torch

w = torch.randn([3,1]).clone().detach().requires_grad_(True)


opt = torch.optim.Adam([w], 0.1)

def model(x):
    f = torch.stack([x * x, x, torch.ones_like(x)], 1)
    yhat = torch.squeeze(f @ w, 1)
    return yhat

def compute_loss(y, yhat):
    loss = torch.nn.functional.mse_loss(yhat, y)
    return loss

def generate_data():
    x = torch.rand(100) * 20 - 10
    y = 5 * x * x + 3
    return x, y

def train_step():
    x, y = generate_data()

    yhat = model(x)
    loss = compute_loss(y, yhat)

    opt.zero_grad()
    loss.backward()
    opt.step()

for _ in range(1000):
    train_step()

print(w.detach().numpy())
```
