def gematria(x):
	return x if len(str(x)) == 1 else gematria(sum(list(map(int,str(x)))))

for j in range(1, 10):	
	for i in range(0, 50*j, j):
		x = gematria(i)
		if(x==9):
			print( "\033[91m"+str(x)+"\033[00m", end=" ")
		else:
			print(x, end=" ")

	print()
	
	
	

