class VortexGenerator:
	def __init__(self, length=100, base=10, n = 2):	
		self.base = base
		self.digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.v = (self._digital_sum(self._int2str(n**x)) for x in range(length))
	
	def _digital_sum(self, x):
		return x if len(str(x)) == 1 else self._digital_sum(self._int2str(sum(list(map(int,str(x))))))

	def _int2str(self, x):
    		if x < 0:
        		return "-" + self._int2str(-x, self.base)
    		return ("" if x < self.base else self._int2str(x//self.base)) + self.digits[x % self.base]
    		
	def __iter__(self):
		return self.v
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
	vg = VortexGenerator(base=10, n=2)#basic usage
	print(type(vg.v))

	for i in vg.v:
		print(i)
