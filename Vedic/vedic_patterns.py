def gematria(x):
	return x if len(str(x)) == 1 else gematria(sum(list(map(int,str(x)))))
		
def printMx(mx, num=None):
	st = f""
	for line in mx:
		st+=' '.join(map(str, line))+"\n"

	print(st.replace(str(num), "\033[91m"+u"\u25C9"+"\033[00m"))


#Set Matrix size		
MTX_SIZE = 50				

#Create Table			
m = [[gematria(x*j) for x in range(1,MTX_SIZE)] for j in range(1, MTX_SIZE)]

#Print
for i in range(1, 10):
	print(f"The Number {i}")
	print("--------------")
	printMx(m, num=i)
