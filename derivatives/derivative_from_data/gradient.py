import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from signals import *

def gradient(y):
	if len(y)<2:
		return None
	g = []
	for i in range(len(y)):
		if i == 0: 
			x = (y[i+1]-y[i])/1
		elif i == len(y)-1:
			x = (y[i]-y[i-1])/1
		else:
			x = (y[i+1]-y[i-1])/2
		
		g.append(x)
	
	return np.array(g)

#x, y = get_stonks()
x, y = get_sin()

dxdy = gradient(y)

plt.plot( x, y)
plt.plot( x, dxdy*10)
plt.show()

