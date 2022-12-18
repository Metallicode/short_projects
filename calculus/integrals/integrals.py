import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

def f(n):
	return np.abs(((n**2)/((-0.2*n)**3))*np.sin(n/100)**3)

t = np.arange(1, 1000, 1)
y = f(t)

fig, ax = plt.subplots()

delta = len(t)//100	 #dx
border_margin = 2	 #just for visual preferance

theta = []		 #here we will save each slop 

#calculate bins and triangels
for i in range(0, len(t)-delta, delta):
	triangle_pts =  plt.Polygon(np.array([[t[i],y[i]], [t[i+delta-border_margin],y[i]], [t[i+delta-border_margin],y[i+delta-border_margin]]]), facecolor = 'orange')
	ax.add_patch(plt.Rectangle((t[i], 0), delta-border_margin, y[i] ,facecolor = 'red'))
	theta.append(((y[i+delta]-y[i])/delta)*10) # append current slop of the hypotenuse 
	#ax.add_patch(triangle_pts)

#plot the Derivativs

'''
plt.plot(range(0, len(t)-delta, delta), theta, "green") #plot triangles slop
plt.plot(t[:-1], (y[1:]-y[:-1])*10, "orange") 	#plot the differences between every 2 items
plt.plot(t, [derivative(f, i)*10 for i in t], "purple") #plot the Derivative
'''


#color a range on the data
a_limit = 0
b_limit = 300

plt.fill_between(t, y, where = [(j>a_limit) and (j<b_limit) for j in t],color ="yellow", alpha=0.7)

plt.axvline(x=a_limit, color='red', linestyle='--')
plt.axvline(x=b_limit, color='red', linestyle='--')



#Integrate bins height
integral = []
bin_height = y[0]

for i in range(0, len(t)-delta, delta):
	bin_height+=y[i]
	integral.append(bin_height)
	#print(bin_height)

#plot the integration
plt.plot(range(0, len(t)-delta, delta), integral)

#height of the F(a)-F(b)
integral_h = integral[b_limit//delta]-integral[a_limit//delta]

#plot the height of the F(a)-F(b)
ax.add_patch(plt.Rectangle((b_limit, integral[b_limit//delta]), delta, -integral_h ,facecolor = 'red'))

print(f"S a->b f(x)*dx = {integral_h*delta}")


#solve Definite Integral with sympy

from sympy import *
def ff(n):
	return Abs(((n**2)/((-0.2*n)**3))*sin(n/100)**3)
x = Symbol('x')
print(integrate(ff(x), (x, a_limit, b_limit)).evalf())


plt.plot(t, y)
plt.show()
