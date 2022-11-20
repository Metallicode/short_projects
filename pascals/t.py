def get_diagonal_indexs(L):
	ii = [0]
	jj = [0]
		
	for x in range(1, L):
		for k in range(2):
			for i in range(x+k):
				ii.append(i+x)
	for q in range(-1,L):	
		for k in range(2):
			for i in range(q+1+k, -1, -1):
				jj.append(i)

	return list(zip(ii,jj))


print(get_diagonal_indexs(5))
