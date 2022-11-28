#https://en.wikipedia.org/wiki/Bernstein_polynomial
#https://towardsdatascience.com/b%C3%A9zier-curve-bfffdadea212

import numpy as np
import matplotlib.pyplot as plt
from math import comb

def get_b(k, n):
	return lambda t: comb(n, k) * t**k * (1 - t)**(n - k)


v = np.linspace(0, 1.0, 100)

ber = get_b(1,2)

'''
plt.plot(v, ber(v))
plt.show()
'''

q = []

for i in range(10):
	for j in range(i+1):
		q.append(get_b(j,i))
		
for func in q:
	plt.plot(v, func(v))

plt.show()
