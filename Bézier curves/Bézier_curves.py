#https://towardsdatascience.com/b%C3%A9zier-curve-bfffdadea212

import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def get_bezier_curve(points):
    n = len(points) - 1
    return lambda t: sum(
        comb(n, i) * t**i * (1 - t)**(n - i) * points[i]
        for i in range(n + 1)
    )

def evaluate_bezier(points, total):
    bezier = get_bezier_curve(points)
    new_points = np.array([bezier(t) for t in np.linspace(0, 1, total)])
    return new_points[:,0], new_points[:,1]

points = np.array([
    [0, 0],
    [-1, 3],
    [4, 3],
    [6, 0],
    [7, 2.5]
])

x, y = points[:,0], points[:,1]
bx, by = evaluate_bezier(points, 50)
plt.plot(bx, by, 'b-')
plt.plot(x, y, 'r.')
plt.show()
