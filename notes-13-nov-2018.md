# 13-nov-2018

### 2 - Plotly offline with Jupyter tutorial

- https://plot.ly/python/offline/

```python
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print __version__
import plotly.graph_objs as go

plot([go.Scatter(x=[1,2,3], y=[3,1,6])])

init_notebook_mode(connected=True)
iplot([{'x' : [1,2,3], 'y': [ 3,1,6]}])

import numpy as np

x = np.random.randn(2000)
y = np.random.randn(2000)

iplot([go.Histogram2dContour(x=x, y=y),
       go.Scatter(x=x, y=y)], show_link=False)

```

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
