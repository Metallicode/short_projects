import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_ylim([-40,40])

f = lambda x: (x**3 + 4*x**2 + 2*x + 4)/x
asymptote = lambda x: x**2 + 4*x + 2

'''
f = lambda x: (x**3 + 2*x**2 + 3*x + 4)/x
asymptote = lambda x: x**2 + 2*x + 3
'''

t = np.linspace(-5, 5, 1000)

plt.plot(t, f(t))
plt.plot(t, f2(t))
plt.show()
