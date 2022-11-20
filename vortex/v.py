def gematria(x):
	return x if len(str(x)) == 1 else gematria(sum(list(map(int,str(x)))))

n = 100


'''
g = [gematria(2**x) for x in range(n)]


for i in range(0,len(g)-6, 6):
	print(g[i:i+6])



#see the pattern of summing two following numbers
for i in range(len(g)-1):
	print(gematria(g[i]+(g[i+1])))
	
	
	
	
	
#calculate sum of pattern
for i in range(0, len(g)-6, 6):
	print(gematria(sum(g[i:i+6])))

'''



#with division
g = []
i = 1
for x in range(n):
	i/=2
	g.append("{:.100f}".format(i).replace(".", ""))

	
	
for i in g:
	print(gematria(i))






