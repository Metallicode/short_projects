#https://stackoverflow.com/questions/54961306/how-to-plot-the-slope-tangent-line-of-parabola-at-any-point

import matplotlib.pyplot as plt
import numpy as np

#parabola
def f(x): 
    return x**2

#parabola derivative
def slope(x): 
    return 2*x
    
#define tangent line
# y = m*(x - x1) + y1
def line(x, x1, y1):
    return slope(x1)*(x - x1) + y1

# Define x data range for parabola
x = np.linspace(-5,5,100)



#point to plot tangent line
x1 = 4
y1 = f(x1)

#range for tangent
x_range = np.linspace(x1-1, x1+1, 10)


#plot 
plt.figure()
plt.plot(x, f(x))
plt.scatter(x1, y1, color='C1', s=50)
plt.plot(x_range, line(x_range, x1, y1))
plt.show()



