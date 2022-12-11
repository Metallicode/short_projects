import numpy as np
import matplotlib.pyplot as plt

def circle(x,r, h=0, k=0):
    y = -((x-h)**2 - r**2)
    if y < 0:
        return None
    else:
        return np.sqrt(y)+k

# Create an array of x values from 0 to 10, with a step size of 0.1
x_values = np.arange(0, 10, 0.1)

# Create an empty list to store the y-coordinates of the points on the circle's circumference
y_values = []

# Call the circle function for each x value to calculate the corresponding y-coordinate
for x in x_values:
    y = circle(x, 10, 5, 5)
    if y is not None:
        y_values.append(y)

# Use the x and y values to plot the circle
# (Assumes you are using a library such as matplotlib to do the plotting)
plt.plot(x_values, y_values)
plt.show()
