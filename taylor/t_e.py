import numpy as np
import math

e = 0

for n in range(50):
	e += 1**n/math.factorial(n)

print(e)
print(np.e)
