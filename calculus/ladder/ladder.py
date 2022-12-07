import numpy as np
import matplotlib.pyplot as plt
import math

#bottom distance from wall
x = 6
#height ladder reache up the wall
y = 13

#ladder lenght
ab = math.sqrt(x**2 + y**2)

print(f"bottom distance from wall {x}, ladder height {y}, ladder lenght {ab}")

#function to calc height of ladder
def f(x, ab):
	return math.sqrt(-((x**2) - (ab**2)))

#f'(x)
def f_t(x, ab):
	return -x / math.sqrt(-((x**2) - (ab**2)))

#lists for plots
h = []
x_dis = []

#delta x
dx = 1

#mesure every x+(dx*n)
while x<ab-dx:			#as long x < ab-dx
	x += dx			#move ladder one more dx
	dy = y-f(x, ab)		#calc new height and save the diff to dy
	h.append(dy)		#append dy
	x_dis.append(x)		#append current length from wall
	y = y-dy		#set y to new current height 
	

plt.plot([x for x in x_dis], [f_t(x, ab) for x in x_dis])
#plt.plot([x for x in x_dis], [ab-sum(h[:x]) for x in range(len(h))])
plt.show()


