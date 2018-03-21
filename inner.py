def outerfunction(x):
	def innerfunction(x):
		return x+1
	y=innerfunction(30)
	print(x,'   ',y)
	
outerfunction(20)