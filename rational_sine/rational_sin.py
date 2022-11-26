'''
https://www.maa.org/press/maa-reviews/indian-mathematics-engaging-with-the-world-from-ancient-to-modern-times
'''

import numpy as np
import matplotlib.pyplot as plt

def rational_sin(x):
	return ((4*x)*(180-x))/(40500 - (x*(180-x)))

L = 180
freq = 5
sample_rate = 44100

t = np.arange(0,L,1.0/(sample_rate/freq))

#s2 = [rational_sin(x) for x in t]
s2 = [rational_sin(x) for x in t]+[-rational_sin(x) for x in t]


####PLOT SIGNAL####
plt.plot(range(len(t)*2), s2,'black')
plt.show()

