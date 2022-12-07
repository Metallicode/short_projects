import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import math

#define a function
def test_func(x):
	#return (x**2*np.sin(x)**2)**(1/x)
	return (4*x**2)*(3*x**5)

def fsin(x):
	return np.sin(x*20)
	

f = fsin

#draw true function
t = np.arange(-1,1,1/1000)


###################### Taylor Series #########################

dx=0.01				#our mesure size (smaller is better)
center = 0.25			#"a" the value we are approximating the function around, the further we are from it our approximation will be less accurate
order =5		#how many terms we are goind to calculate from the taylor series this has a effect on our results.
coefficients = []		#here we will store our coefficients
n_points = order*2		#must be odd and greater than derivative order
if n_points % 2 == 0:
	n_points+=1

#find coefficients
for i in range(0, order+1):
	coefficients.append(derivative(f, center, n=i, dx=dx, order=n_points)/math.factorial(i))
#print(coefficients)


'''
#print the Taylor Series terms 
eqn = ""
for i in range(0,order+1):
	if coefficients[i] != 0:
		eqn+=str(coefficients[i])+("(x-{})^{}".format(center, i) if i>0 else "")+" + "

if eqn.endswith(" + "):
	eqn = eqn[:-3]	

print(eqn)

'''


#calculate the Taylor Series at given x
def approximate(x, coefficients, center):
	fx = 0
	for i in range(0,len(coefficients)):
		fx += coefficients[i] * ((x-center)**i)	
	return fx

#draw function
fig, ax = plt.subplots()
plt.plot(t, f(t), "black")
plt.plot(t, [approximate(x, coefficients, center) for x in t], "red")
ax.set_ylim([-5,5])
plt.show()


