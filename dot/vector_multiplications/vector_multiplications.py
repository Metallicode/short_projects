import numpy as np
from numpy import linalg as LA
import math


vector_a = np.array([1,-2,3,-4,5])
vector_b = np.array([5,6,-7,8,-9])


'''
#dot product
dot_product = np.dot(vector_a, vector_b)
#dot_product = np.dot(vector_b, vector_a) #same
print(f"{dot_product=}")
'''

'''
#linear weighted combination
w1 = 3
w2 = 2

print("linear weighted combination: ", vector_a*w1 + vector_b+w2)
'''

'''
#outer product
outer_product = np.outer(vector_b,vector_a)
#outer_product = np.outer(vector_b, vector_a) #this will swap raws and columns
print(f"{outer_product=}")
'''

'''
#element-wise 
print(f"element-wise: {vector_a*vector_b}")
'''


#cross product works on 3 dimentional vectors

def cross_product(v1, v2):
	# Calculate the magnitudes of the vectors
	v1_magnitude = LA.norm(v1)
	v2_magnitude = LA.norm(v2)
	
	# Calculate the angle between the vectors
	dot_product = np.dot(v1, v2)
	angle = np.arccos(dot_product / (v1_magnitude * v2_magnitude))
        
        # Calculate the perpendicular direction to both vectors
	nx = v1[1]*v2[2] - v1[2]*v2[1]
	ny = v1[2]*v2[0] - v1[0]*v2[2]
	nz = v1[0]*v2[1] - v1[1]*v2[0]
	n_magnitude = LA.norm(np.array([nx,ny,nz]))# Calculate the magnitudes of the perpendicular vector
	n = np.array([nx/n_magnitude, ny/n_magnitude, nz/n_magnitude])#create unit vector
	
	# Calculate the cross product using the geometric formula
	v3 = v1_magnitude * v2_magnitude * np.sin(angle) * n
	return v3


v1=np.array([5,3,4])
v2=np.array([-2,1,-1])

#cross_product = [v1[1]*v2[2] - v1[2]*v2[1],v1[2]*v2[0] - v1[0]*v2[2],v1[0]*v2[1] - v1[1]*v2[0]]
cross_product = cross_product(v1, v2)

print(f"{cross_product=}")

