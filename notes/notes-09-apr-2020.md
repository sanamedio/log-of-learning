# 09-apr-2020


### 1 - pytorch examples

https://github.com/jcjohnson/pytorch-examples

tut1:
```python
import numpy as np


N, D_in, H , D_out = 64, 1000 , 100, 10


x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)


w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)


learning_rate = 1e-6

for t in range(500):

    h = x.dot(w1)
    h_relu = np.maximum(h,0)
    y_pred = h_relu.dot(w2)


    loss = np.square(y_pred - y ).sum()
    print(t,loss)


    grad_y_pred = 2.0 * (y_pred -y )
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h<0] = 0
    grad_w1 = x.T.dot(grad_h)


    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
```

tut2:
```python
import torch


device = torch.device('cpu')


N, D_in, H, D_out = 64, 1000, 100, 10


x = torch.randn(N, D_in, device=device)
y = torch.randn(N, D_out, device=device)


w1 = torch.randn(D_in, H, device=device)
w2 = torch.randn(H, D_out, device=device)

learning_rate = 1e-6

for t in range(500):
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)

    loss = (y_pred - y).pow(2).sum()
    print(t, loss.item())


    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    # Update weights using gradient descent
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
```

tut3:
```python
import torch

device = torch.device('cpu')


N, D_in, H, D_out = 64, 1000, 100, 10


x = torch.randn(N, D_in, device=device)
y = torch.randn(N, D_out, device=device)


w1 = torch.randn(D_in, H, device=device, requires_grad=True)
w2 = torch.randn(H, D_out, device=device, requires_grad=True)


learning_rate = 1e-6


for t in range(500):

    y_pred = x.mm(w1).clamp(min=0).mm(w2)

    loss = (y_pred - y).pow(2).sum()
    print(t, loss.item())


    loss.backward()


    with torch.no_grad():

        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad


        w1.grad.zero_()
        w2.grad.zero_()
```

tut4:
```python
import torch

device = torch.device('cpu')


N, D_in, H, D_out = 64, 1000, 100, 10


x = torch.randn(N, D_in, device=device)
y = torch.randn(N, D_out, device=device)

model = torch.nn.Sequential(
            torch.nn.Linear(D_in, H),
            torch.nn.ReLU(),
            torch.nn.Linear(H, D_out),
        ).to(device)


loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4

for t in range(500):


    y_pred = model(x)

    loss = loss_fn(y_pred,y)
    print(t, loss.item())


    model.zero_grad()


    loss.backward()


    with torch.no_grad():
        for param in model.parameters():
            param.data -= learning_rate * param.grad
```

tut5:
```python
import torch


N, D_in, H, D_out = 64, 1000, 100, 10


x = torch.randn(N, D_in)
y = torch.randn(N, D_out)


model = torch.nn.Sequential(
        torch.nn.Linear(D_in, H),
        torch.nn.ReLU(),
        torch.nn.Linear(H,D_out),
        )

loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


for t in range(500):

    y_pred = model(x)

    loss = loss_fn(y_pred, y)

    print( t, loss.item())

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
```

