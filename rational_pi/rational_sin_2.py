#https://mathworld.wolfram.com/Sine.html

import numpy as np
import matplotlib.pyplot as plt

def factorial(x):
	fact = 1
	for i in range(1,x+1):
		fact *= i
	return fact

def analytic_sin(x):
	s = []
	for n in range(1,10):
		s.append((((-1)**(n-1))/factorial(((2*n)-1)))*x**((2*n)-1))	
	
	return sum(s)

freq = 10
	
t = np.arange(0,2*np.pi,(2*np.pi)/(44100/freq))

s3 = [analytic_sin(x) for x in t]*freq



####PLOT SIGNAL####
plt.plot(range(len(s3)), s3,'black')
plt.show()

