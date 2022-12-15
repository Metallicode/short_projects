import numpy as np
import matplotlib.pyplot as plt

y = [0,0,1,0]
x = [0,49,50,100]

xi = np.linspace(x[0], x[-1], 1000)
yi = np.interp(xi, x, y)

plt.plot(xi,yi)

flt = np.ones(400)/250

print(flt)

#the convolution operator flips the second array before “sliding”
c = np.convolve(flt,yi, 'same')

#plt.plot(xi[:len(flt)],flt)
plt.plot(xi,c)
plt.show()
