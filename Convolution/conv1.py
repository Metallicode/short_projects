import numpy as np
import matplotlib.pyplot as plt

y = [3,7,12,2,13,1,17,5]
flt = np.ones(3)/3

c = np.convolve(y,flt, 'same')
print(c)

t=range(0, len(y))

plt.plot(t,y, "black")
plt.plot(t,c, "red")
plt.show()
