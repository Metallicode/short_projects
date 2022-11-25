xv = [x**3 for x in range(20)]
l = xv

#print the first row
for i in range(len(xv)):
	print(xv[i], end=" ")
print()

#print the rows
for i in range(6):
	g = l
	l = []
	if(len(set(g))==1):
		break
	print(" "*i, end= " ")
	for k in range(len(g)-1):
		delta = g[k+1]-g[k]
		l.append(delta)
		#print("{:.2f}".format(delta), end=" ")
		print(delta, end=" ")
		
	print()
