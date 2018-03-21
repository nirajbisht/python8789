def make_multiplier_of(n):
	def mult(x):
		return x/n
	return mult
time3=make_multiplier_of(3)
time5=make_multiplier_of(5)
print(time3(9))
print(time5(20))
print(time5(time3(18)))