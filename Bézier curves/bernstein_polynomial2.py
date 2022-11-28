#https://en.wikipedia.org/wiki/Bernstein_polynomial
#https://towardsdatascience.com/b%C3%A9zier-curve-bfffdadea212

import numpy as np
import matplotlib.pyplot as plt
from math import comb

def bernstein_polynomial(k, n):
	return lambda t: comb(n, k) * t**k * (1 - t)**(n - k)

def bezier_curve(points):
    return lambda t: sum(
        bernstein_polynomial(k,len(points) - 1)(points[k])
        for k in range(len(points))
    )


points = np.array([
    [0, 0],
    [2, 3],
    [4, 3],
    [6, 0],
    [10, 2.5]
])



x, y = points[:,0], points[:,1]

bezier = bezier_curve(points)
new_points = np.array([bezier(t) for t in np.linspace(0, 1, 50)])

bx, by = new_points[:,0], new_points[:,1]
plt.plot(bx, by, 'b-')
plt.plot(x, y, 'r.')
plt.show()







