# 13-nov-2018

### 1 - Plotly offline interactive graphs

- https://github.com/SayaliSonawane/Plotly_Offline_Python

```python
import plotly
import numpy as np
from plotly.graph_objs import Layout,Scatter

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

trace =Scatter(x = random_x,y=random_y)

plotly.offline.plot({ "data": [trace]})
```
