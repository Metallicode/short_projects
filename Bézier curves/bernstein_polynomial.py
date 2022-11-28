#https://en.wikipedia.org/wiki/Bernstein_polynomial
#https://towardsdatascience.com/b%C3%A9zier-curve-bfffdadea212
import numpy as np
import matplotlib.pyplot as plt
from math import comb

#return the bernstein_polynomial from n, k values
def get_bernstein_polynomial(k, n):
	return lambda t: comb(n, k) * t**k * (1 - t)**(n - k)

bernstein_polynomials = []

#create collection of bernstein_polynomials
for i in range(10):
	for j in range(i+1):
		bernstein_polynomials.append(get_bernstein_polynomial(j,i))

#create linear set from 0 - 1 with 100 steps 
v = np.linspace(0, 1.0, 100)

#plot each bernstein_polynomial 
for func in bernstein_polynomials:
	plt.plot(v, func(v))

plt.show()
