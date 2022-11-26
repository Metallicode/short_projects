from collections import defaultdict

def is_prime(x):
	if x == 0 or x == 1:
		return False
	for i in range(2, x):
		if x%i==0:
			return False
	return True 


primes = (x for x in range(500) if is_prime(x)==True)

#print(list(primes))


#create dictionery
polyDict = defaultdict(int)


#set value
original_vale = int(input("\n"))

#keep running until result is done
while True:
	f = next(primes)
	
	#try to divide our value as much as we can with current prime
	while True:
		if original_vale>1:
			if(original_vale%f==0):#division ok, calc result and add to dict
				original_vale//=f
				polyDict[f]+=1
			else:
				break#go get the next prime
		else:
			break#go get the next prime
	if original_vale<=9:
		break#our work is done




#print the result:
if original_vale>1:
	print(f"{original_vale}", end=" ")
	
for k, v in polyDict.items():
	if v!=0:
		print(f"{k}**{v} ", end="")
		
print()

#print(polyDict, original_vale)
			

