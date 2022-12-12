import matplotlib.pyplot as plt
import numpy as np

"0 < |x - a| < δ, then |f(x) - L| < ε."


#euler number estimation
def e(n=0):
	while 1:
		n+=1	
		yield (1+(1/n))**n	

def sin(n=0):
	while 1:
		n+=1
		yield np.sin(n*np.pi/180)

def tan(n=0):
	while 1:
		n+=1
		#yield np.tan(n*(np.pi/180))
		yield np.sin(n*np.pi/180) / np.cos(n*np.pi/180)



def n_plus_1(n=0):
	while 1:
		n+=1
		yield n

def one_over_n(n=0):
	while 1:
		n+=1
		yield 1/n


def n_root_of_n(n=0):
	while 1:
		n+=1	
		yield n**(1/n)
		
def sum_one_over_n(n=1):
	a = 0
	while 1:
		n+=1
		a+=1/n
		yield a
		
def one_plus_tenth_to_n_power(n=0):	
	while 1:
		n+=1	
		yield 1+(1/(10**n))
		
def n_plus_1_over_n(n=0):
	while 1:
		n+=1	
		yield (n+1)/n	



#-1,1,-1,1...
def one_plus_n1_power_n_over_2(n=0):
	while 1:
		n+=1	
		yield (1+((-1)**n))/2
		
def n_times_1_plus_n1_power_n_over_2(n=0):
	while 1:
		n+=1	
		yield n*(1+((-1)**n))/2

	
s = tan()
l = 500
plt.ylim(-10, 10)
t = np.arange(0,l,1)

plt.plot([x for x in t], [next(s) for x in t])
plt.show()
