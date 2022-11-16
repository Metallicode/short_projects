def factorial(x):
	return factorial(x-1)*x if x > 1 else 1

# input n
n = 20

for i in range(n):
	print(" "*(n-i+1), end=" ")
	for j in range(i+1):
		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	print()

