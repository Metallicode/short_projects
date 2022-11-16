def factorial(x):
	return factorial(x-1)*x if x > 1 else 1

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

n = 30
digz = 10

fibonacci = []

f = []

for i in range(n):
	m = []
	for j in range(i+1):
		x = factorial(i)//(factorial(j)*factorial(i-j))
		m.append(x)
	f.append(m)

dx = get_diagonal_indexs(digz)

b = []


for i in range(1,digz):
	b.append(i)
	b.append(i)
	
zx=0

for i in b:
	wq = []
	for q in range(i):
		wq.append(f[dx[zx][0]][dx[zx][1]])
		zx+=1
	fibonacci.append(sum(wq))

for i in fibonacci:	
	print("."*i)



