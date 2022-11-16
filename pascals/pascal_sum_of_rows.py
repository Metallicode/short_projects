def factorial(x):
	return factorial(x-1)*x if x > 1 else 1

row_sums = []

# input n
n = 20

for i in range(n):
	print(" "*(n-i+1), end=" ")
	row = []
	for j in range(i+1):
		# nCr = n!/((n-r)!*r!)
		x = factorial(i)//(factorial(j)*factorial(i-j))
		row.append(x)
		print(x, end=" ")
	row_sums.append(sum(row))
	print()

print(row_sums)
