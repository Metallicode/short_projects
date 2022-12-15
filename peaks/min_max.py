import matplotlib.pyplot as plt
import numpy as np
from pol import f

#real data
x, data = f()
plt.plot(x,data)

#calc differences
diffs = (data[1:] - data[:-1])*100
#plt.plot(x[:-1],diffs)

#calc differences of absolute diffs from original data
q_abs = data[:-1]-(abs(diffs)*10)
#plt.plot(x[:-1], q_abs , "orange")

#calc differences of q_abs
q_diffs = (q_abs[1:]-q_abs[:-1])*10
#plt.plot(x[:-2], q_diffs , "pink")

delta = 0.99
peaks = np.where((q_diffs[:-1]-q_diffs[1:])>delta)

plt.scatter(x[peaks], data[peaks], color="red")
plt.show()
