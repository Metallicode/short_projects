#https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-465
#https://towardsdatascience.com/linear-algebra-basics-dot-product-and-matrix-multiplication-2a7624942810

import numpy as np

a = np.random.rand(2,3,3,5)
b = np.random.rand(2,3,5,3)


#a = np.random.rand(2,3)
#b = np.random.rand(3,2)

print(a)
print("- - - - - - - - - -")
print(b)

c = a @ b 
c2 = np.matmul(a,b)
d = np.dot(a, b)

print("@:\t", c.shape)
print("matmul:\t", c2.shape)
print("dot:\t",d.shape)
print("matmul\n", c2)
print("dot\n", d)

#https://en.wikipedia.org/wiki/Tensor_product
