import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from signals import *

x, y = get_stonks()
plt.plot( x, y)

dxdy = np.gradient(y, x)
plt.plot( x, dxdy)
plt.show()

