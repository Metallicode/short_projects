'''
For matrix multiplication, the number of columns in the first matrix must be equal to the number of rows in the second matrix. The result matrix has the number of rows of the first and the number of columns of the second matrix.

Multiplication of two matrices involves dot products between rows of first matrix and columns of the second matrix.

'''


import numpy as np

ma = [[45,2,3,4,5],
      [3,3,5,6,7],
      [4,5,25,7,8],
      [5,6,7,7,9]]
      

mb = [[1,2,3,4],
      [1,2,3,4],
      [1,2,3,4],
      [1,2,3,4],
      [1,2,3,4]]
      
      

      
      

'''
res[0][0] = (45*1)+(2*1)+(3*1) +(4*1)+(5*1) 
res[1][0] = (3*1) +(3*1)+(5*1) +(6*1)+(7*1) 
res[2][0] = (4*1) +(5*1)+(25*1)+(7*1)+(8*1) 
res[3][0] = (5*1) +(6*1)+(7*1) +(7*1)+(9*1) 

res[0][1] = (45*2)+(2*2)+(3*2) +(4*2)+(5*2) 
res[1][1] = (3*2) +(3*2)+(5*2) +(6*2)+(7*2) 
res[2][1] = (4*2) +(5*2)+(25*2)+(7*2)+(8*2) 
res[3][1] = (5*2) +(6*2)+(7*2) +(7*2)+(9*2) 

'''

def matrix_multiplication(v1, v2):
	v = [[] for x in range(len(v1))]
	
	for i in range(len(v1)):	
		for j in range(len(v2[0])):
			vx =[]
			for k in range(len(v2)):
				print(j, k , "--" ,k, i )
				vx.append(v1[j][k]*v2[k][i])
			v[j].append(sum(vx))	

	return v



print(matrix_multiplication(ma, mb))

print(np.dot(ma, mb))
print(np.matmul(ma, mb))
