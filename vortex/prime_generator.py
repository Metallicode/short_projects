class PrimeGenerator:
	def __init__(self, length=100):
		self.length = length
		self.primes = self._make_primes()
	
	def _make_primes(self):
		x = []
		c = 0
		while len(x)<self.length:
			if(self._is_prime(c)):
				x.append(self._digital_sum(c))
			c+=1
		
		return x
		
	def _is_prime(self, x):
		if (x <=  1):
			return False
		if(x==2):
			return True
		if (x%2 == 0):
			return False
		for i in range(3, int(x**0.5 + 1), 2):
			if (x % i == 0):
				return False
		return True
		
	
	def _digital_sum(self, x):
		return x if len(str(x)) == 1 else self._digital_sum(sum(list(map(int,str(x)))))
		
	def __iter__(self):
		return iter(self.primes)



if __name__ == "__main__":
	pg = PrimeGenerator()#basic usage
	
	for i in pg:
		print(i)
