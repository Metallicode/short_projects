import numpy as np
import matplotlib.pyplot as plt

plt.xlim(0,100)
plt.ylim(0,100)

#Linear Equations
# m = rise/run

#slope intercept form
def slope_intercept(m, b=0):
	return lambda x: m*x+b    #m is slope, b is y intercept

#point slope form 
def point_slope(m, x1, y1):
	return lambda x : m(x-x1)+y1    #m is slope, b is y intercept


#my_line = slope_intercept(1, 4)
ps = point_slope(slope_intercept(0.4),2,5)

v =  np.linspace(0,100,100)
#plt.plot(v, my_line(v))




plt.scatter(2,5)
plt.plot(v,ps(v))

plt.show()
