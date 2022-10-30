#https://docs.python.org/3.8/library/itertools.html#module-itertools

import itertools

int_list =  [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]
char_list = ["a","b","c","d","e","f","g","h"]


#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#= Infinite #=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#count()

if(0):
	counter = itertools.count(4)

	print(next(counter))
	print(next(counter))
	print(next(counter))

	c = map(lambda x: x*next(counter),int_list)
	print(list(c))

#cycle()

if(0):

	c = itertools.cycle(char_list)

	for i in range(100):
		print(next(c), end='')
	print()

#repeat()

if(0):

	#s = itertools.repeat("$")
	s = itertools.repeat("$", 4)

	for i in range(50):
		print(next(s), end='')
	print()



#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#= terminating on the shortest input =#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#accumulate()

if(0):

	accu = itertools.accumulate(int_list)
	print(list(accu))

#chain()
if(0):

	chain = itertools.chain(int_list, char_list)
	print(list(chain))

#compress()
if(0):

	comp = itertools.compress(char_list, itertools.cycle([1,1,0]))
	print(list(comp))

#dropwhile()
if(0):
	dw = itertools.dropwhile(lambda x: x<5, int_list)
	print(list(dw))

#filterfalse()
if(0):
	filtfal = itertools.filterfalse(lambda x: x%2, range(10))
	print(list(filtfal))
	
#groupby()
if(0):

	key_function = lambda x: x[0]

	L = [("cat",1), ("dog",2), ("cat",3), ("bird",4), ("dog",5), ("dog",6), ("bird",7)]
	L.sort(key=key_function)

	for key, group in itertools.groupby(L, key_function):
		print(key + " :", list(group))

#islice()
if(0):
	isli = itertools.islice(char_list, 2, 6,2)
	print(list(isli))
	print(char_list[2:6:2])	

#starmap()
if(0):

	c = itertools.starmap(lambda x, y: x*y,[(1,2),(4,2),(5,6)])
	print(list(c))

#takewhile()
if(0):
	tw = itertools.takewhile(lambda x: x<5, int_list)
	print(list(tw))

#tee()
if(0):
	te = itertools.tee(int_list,3)
	print(te)
	
	print(list(te[0]))
	print(list(te[0])) #notice empty iterator
	
	print(list(te[1]))
	print(list(te[2]))

#zip_longest()
if(0):

	z = zip(int_list, char_list[:-1])
	print(list(z))

	z = itertools.zip_longest(int_list, char_list[:-1])
	print(list(z))


#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#= Combinatoric #=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


#product()
#has repeating items (AA)
#AB != BA
if(0):
	p = itertools.product(char_list, repeat=2)
	print(list(p))


#permutations()
#Elements are treated as unique based on their position, not on their value. 
#no repeating items 
#AB != BA
if(0):
	p = itertools.permutations(char_list,2)
	print(list(p))


#combinations_with_replacement()
#has repeating items (AA)
#AB == BA
if(0):
	p = itertools.combinations_with_replacement(char_list,2)
	print(list(p))
	
	
#combinations()
#no repeating items 
#AB == BA
if(0):
	p = itertools.combinations(char_list,2)
	print(list(p))



#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#= Example =#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


if(1):
	#calc combinations of cash
	##############################################################
	amount_to_return = 133
	
	cash_list = [50,50,20,20,20,20,10,10,10,5,5,5,5,2,2,1,1,1,1,1]

	options = []

	for i in range(1,len(cash_list)):
		c_options = itertools.combinations(cash_list, i)
		for option in c_options:
			if(sum(option)==amount_to_return):
				options.append(option)
	
	s = set(options)	
	print(s)



