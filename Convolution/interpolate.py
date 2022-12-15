import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Define the x and y values for the interpolation
x = [1, 3, 7, 11]
y = [4, 9, 13, 19]

# Interpolate the y-values at the midpoint between each pair of x-values
xi = np.linspace(x[0], x[-1], len(x) * 2 - 1)
yi = np.interp(xi, x, y)

'''
f = interp1d(x, y)
yi = f(xi)
'''


# The output should be [4, 6.5, 9, 11.5, 13, 15.5, 19]
print(yi)




#############################################################################################



def interpolate_array(arr, n):
  # Make a new empty list to hold the interpolated values
  interpolated_values = []

  # Loop through the input array, and add n interpolated values between each pair of values
  for i in range(len(arr) - 1):
    # Get the two values that we are interpolating between
    val1 = arr[i]
    val2 = arr[i + 1]

    # Calculate the step size for the interpolation
    step = (val2 - val1) / (n + 1)

    # Add n interpolated values to the list
    for j in range(n):
      interpolated_value = val1 + (step * (j + 1))
      interpolated_values.append(interpolated_value)

  # Add the original values to the list of interpolated values
  interpolated_values = arr[:1] + interpolated_values + arr[-1:]

  # Return the interpolated values
  return interpolated_values
  
  
ia = interpolate_array([1,2,3,6,9], 10)
plt.plot(range(len(ia)), ia)
plt.show()
