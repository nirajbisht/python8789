class Powtwo:
	def __init__(self,max=0):
		self.max=max
	def __iter__(self):
		self.n=0
		return self
	def __next__(self):
		if self.n<=self.max:
			result =2 ** self.n
			self.n+=1
			return result
		else:
			raise stopIteration
for x in Powtwo(5):
	print(x)