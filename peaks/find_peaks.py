import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
from pol import f

x , series = f()
maxima, _ = find_peaks(series)
minima, _ = find_peaks(series*-1)

plt.plot(x, series, color='black');
plt.plot(x[minima], series[minima], 'x', label='minima')
plt.plot(x[maxima], series[maxima], '*', label='maxima')
plt.legend()
plt.show()
