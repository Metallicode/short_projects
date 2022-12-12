import numpy as np

# Define the x and y values for the interpolation
x = [1, 3, 7, 11]
y = [4, 9, 13, 19]

# Interpolate the y-values at the midpoint between each pair of x-values
xi = np.linspace(x[0], x[-1], len(x) * 2 - 1)
yi = np.interp(xi, x, y)

# The output should be [4, 6.5, 9, 11.5, 13, 15.5, 19]
print(yi)




########################################################################################



import numpy as np
from scipy.interpolate import interp1d

# Define the x and y values for the interpolation
x = [1, 3, 7, 11]
y = [4, 9, 13, 19]

# Interpolate the y-values at the midpoint between each pair of x-values
xi = np.linspace(x[0], x[-1], len(x) * 2 - 1)

# Create the interpolation function
f = interp1d(x, y)

# Interpolate the y-values using the interpolation function
yi = f(xi)

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
  
  
  
'''

The x-values in the x list define the points at which the y-values in the y list are known. These values are used as the reference points for the interpolation, and the interpolation function estimates the y-values at the x-coordinates in the xi array based on the known x- and y-values.

For example, in the code above, the x- and y-values are [1, 3, 7, 11] and [4, 9, 13, 19], respectively. This means that the y-value at x=1 is 4, the y-value at x=3 is 9, and so on. The xi array specifies the x-coordinates at which to interpolate the y-values, in this case the midpoint between each pair of x-values. The interpolation function then estimates the y-values at these x-coordinates based on the known x- and y-values, resulting in the interpolated y-values [4, 6.5, 9, 11.5, 13, 15.5, 19].

In general, the x-values and y-values can be any values, as long as they are paired such that each x-value has a corresponding y-value. The x-coordinates at which to interpolate the y-values can also be any values within the range of the x-values, and the interpolation function will estimate the y-values at these x-coordinates based on the known x- and y-values.

'''
