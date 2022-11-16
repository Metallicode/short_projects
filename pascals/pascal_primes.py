def factorial(x):
	return factorial(x-1)*x if x > 1 else 1

def is_prime(x):
	if x == 0 or x == 1:
		return False
	for i in range(2, x):
		if x%i==0:
			return False
	return True 

# input n
n = 20

for i in range(n):
	print(" "*(n-i+1), end=" ")
	for j in range(i+1):
		# nCr = n!/((n-r)!*r!)
		x = factorial(i)//(factorial(j)*factorial(i-j))
		if(is_prime(x)):
			print( "\033[91m"+str(x)+"\033[00m", end=" ")
		else:
			print(x, end=" ")
	print()

