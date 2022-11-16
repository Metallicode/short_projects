import numpy as np

a = [1,2,3,4,5]
b = [2,3,4,5,6]

def dot(v1, v2):
	r = []
	for i in range(len(v1)):
		r.append(v1[i]*v2[i])
			
	return sum(r)
	

print(dot(a, b))

print(np.dot(a, b))
