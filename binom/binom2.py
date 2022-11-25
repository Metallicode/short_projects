import math

#create the series
g = []
g.append([(x**6)+(12*x)*(x**32)-45*x for x in range(15)])

i=1

#print the base 
for item in g[0]:
	print(item, end=" ")
print()

#print the rows
while (len(set(g[i-1]))!=1):
	l = []
	print(" "*i, end= " ")
	for q in range(len(g[i-1])-1):
		delta = g[i-1][q+1]-g[i-1][q]
		l.append(delta)
		#print("{:.2f}".format(delta), end=" ")
		print(delta, end=" ")
		
	g.append(l)
	i+=1
	print()
	if(i>1000):
		print("are we sure about this..? this is not order...")

#print first value from each row
for j in range(len(g)):
	print(g[j][0])

#make calc
x = 0	#this will be the result
n = 5	#this is the n for which we are asking for

for k in range(len(g)):
	print(f"{g[k][0]} * ({n}!/[({n}-{k})!{k}!])", end=" ")
	x+=g[k][0]*math.comb(n, k)
	if (k<len(g)-1):
		print(" + ", end="")

print(f"the real value is: {g[0][n]}, our result is {x}")



