def factorial(x):
	return factorial(x-1)*x if x > 1 else 1


# input n
n = 45

for i in range(n):
	print(" "*(n-i+1), end=" ")
	for j in range(i+1):
		# nCr = n!/((n-r)!*r!)
		x = factorial(i)//(factorial(j)*factorial(i-j))
		if(x%2==0):
			print( "\033[91m"+u"\u25C9"+"\033[00m", end=" ")
		else:
			print(u"\u25C9", end=" ")
	print()

